"""
Batched, resumable RBP inference with PhageRBPdetect v4 (fine-tuned ESM-2 t12).

Adapts dimiboeckaerts/PhageRBPdetection's PhageRBPdetect_v4_inference.py, which
processes sequences one-at-a-time with no checkpointing, into a form that scales
to the ~1.36M metagenome proteins (MG08/MG09) on an Apple-Silicon Mac (MPS).

Same model call as upstream: score = softmax(logits)[:, 1]; pred = argmax (score >= 0.5).
Output columns are kept identical: protein_name, preds, score.

Key differences from upstream:
  - streams the FASTA (never holds all sequences in memory)
  - runs the model in padded batches (one forward pass per batch)
  - length-sorts within a read-chunk to cut padding waste
  - appends to the output CSV incrementally and resumes by skipping IDs already written
  - device auto-selects mps -> cuda -> cpu

Usage:
  python run_rbp_inference.py --fasta MG08.faa --model-dir <dir>/RBPdetect_v4_ESMfine \
      --out predictions_MG08.csv [--batch-size 64] [--limit N] [--device auto]
"""

import argparse
import csv
import os
import sys
import time

import torch
from Bio import SeqIO
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def pick_device(choice):
    if choice != "auto":
        return torch.device(choice)
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def load_done_ids(out_path):
    """Return the set of protein_name values already present in an existing output CSV."""
    done = set()
    if not os.path.exists(out_path):
        return done
    with open(out_path, newline="") as fh:
        reader = csv.reader(fh)
        header = next(reader, None)
        for row in reader:
            if row:
                done.add(row[0])
    return done


def count_records(fasta_path):
    n = 0
    with open(fasta_path) as fh:
        for line in fh:
            if line.startswith(">"):
                n += 1
    return n


def stream_records(fasta_path, done_ids, limit):
    """Yield (name, seq) for records not already done, up to `limit` NEW records."""
    seen = 0
    for rec in SeqIO.parse(fasta_path, "fasta"):
        if limit is not None and seen >= limit:
            break
        seen += 1
        name = rec.id
        if name in done_ids:
            continue
        seq = str(rec.seq).rstrip("*").strip()
        if not seq:
            print(f"[skip] empty sequence: {name}", file=sys.stderr)
            continue
        yield name, seq


def chunked(iterable, size):
    buf = []
    for item in iterable:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", required=True)
    ap.add_argument("--model-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--batch-size", type=int, default=64)
    ap.add_argument("--max-length", type=int, default=1024)
    ap.add_argument("--chunk-batches", type=int, default=100,
                    help="read this many batches at a time, length-sort them, then run")
    ap.add_argument("--limit", type=int, default=None,
                    help="process only the first N records of the FASTA (for pilot runs)")
    ap.add_argument("--device", default="auto", choices=["auto", "mps", "cuda", "cpu"])
    args = ap.parse_args()

    device = pick_device(args.device)
    print(f"Device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(args.model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(args.model_dir)
    model.eval().to(device)

    done_ids = load_done_ids(args.out)
    if done_ids:
        print(f"Resuming: {len(done_ids)} proteins already in {args.out}, will skip them.")

    total_records = count_records(args.fasta)
    if args.limit is not None:
        total_records = min(total_records, args.limit)
    remaining = total_records - len(done_ids)
    print(f"FASTA records: {total_records} | to process: {max(remaining, 0)}")

    new_file = not os.path.exists(args.out) or os.path.getsize(args.out) == 0
    out_fh = open(args.out, "a", newline="")
    writer = csv.writer(out_fh)
    if new_file:
        writer.writerow(["protein_name", "preds", "score"])
        out_fh.flush()

    processed = 0
    t0 = time.time()
    chunk_size = max(args.batch_size * args.chunk_batches, args.batch_size)
    records = stream_records(args.fasta, done_ids, args.limit)

    for chunk in chunked(records, chunk_size):
        # length-sort the chunk so each padded batch has similar-length sequences
        chunk.sort(key=lambda x: len(x[1]))
        for batch in chunked(iter(chunk), args.batch_size):
            names = [n for n, _ in batch]
            seqs = [s for _, s in batch]
            enc = tokenizer(seqs, return_tensors="pt", padding=True,
                            truncation=True, max_length=args.max_length).to(device)
            with torch.no_grad():
                logits = model(**enc).logits
                probs = logits.softmax(-1)[:, 1]
                preds = logits.argmax(-1)
            probs = probs.tolist()
            preds = preds.tolist()
            for name, p, s in zip(names, preds, probs):
                writer.writerow([name, int(p), f"{float(s):.6f}"])
            out_fh.flush()
            processed += len(names)
            if processed % (args.batch_size * 20) < args.batch_size:
                rate = processed / max(time.time() - t0, 1e-6)
                eta = (remaining - processed) / rate if rate > 0 else float("inf")
                print(f"  {processed}/{remaining} | {rate:.1f} seq/s | ETA {eta/60:.1f} min",
                      flush=True)

    out_fh.close()
    dt = time.time() - t0
    print(f"Done. Processed {processed} new proteins in {dt/60:.1f} min "
          f"({processed/max(dt,1e-6):.1f} seq/s). Output: {args.out}")


if __name__ == "__main__":
    main()
