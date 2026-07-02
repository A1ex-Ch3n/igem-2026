"""
Turn PhageRBPdetect v4 prediction CSVs into the deliverable RBP list.

For each sample (a prediction CSV + its source protein FASTA), keep proteins the
model called as RBPs (preds == 1, i.e. score >= 0.5 -- the tool's default boundary)
and emit:
  <LABEL>_RBPs.tsv   protein_name, score, length  (sorted by score desc)
  <LABEL>_RBPs.faa   FASTA of those proteins, pulled from the source .faa

Also writes a combined all_metagenome_RBPs.{tsv,faa} across samples and prints
counts and a score-distribution summary.

Usage:
  python summarize_rbps.py --out-dir <dir> \
      --sample MG08 predictions_MG08.csv /path/MG08.faa \
      --sample MG09 predictions_MG09.csv /path/MG09.faa
"""

import argparse
import csv
import os

from Bio import SeqIO

THRESHOLD = 0.5  # tool default: preds==1 == argmax == score>=0.5


def read_rbp_predictions(pred_csv):
    """Return dict name -> score for rows with preds == 1, plus total row count."""
    rbps = {}
    total = 0
    with open(pred_csv, newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            total += 1
            if int(row["preds"]) == 1:
                rbps[row["protein_name"]] = float(row["score"])
    return rbps, total


def score_histogram(scores):
    bins = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0001]
    labels = ["0.5-0.6", "0.6-0.7", "0.7-0.8", "0.8-0.9", "0.9-1.0"]
    counts = [0] * len(labels)
    for s in scores:
        for i in range(len(labels)):
            if bins[i] <= s < bins[i + 1]:
                counts[i] += 1
                break
    return list(zip(labels, counts))


def process_sample(label, pred_csv, fasta, out_dir):
    rbps, total = read_rbp_predictions(pred_csv)
    print(f"\n[{label}] {len(rbps)} RBPs / {total} proteins "
          f"({100.0 * len(rbps) / max(total, 1):.2f}%)")

    # pull sequences + lengths for the RBP hits from the source FASTA
    records = {}
    lengths = {}
    for rec in SeqIO.parse(fasta, "fasta"):
        if rec.id in rbps:
            records[rec.id] = rec
            lengths[rec.id] = len(str(rec.seq).rstrip("*"))

    missing = set(rbps) - set(records)
    if missing:
        print(f"  WARNING: {len(missing)} RBP IDs not found in {fasta}")

    rows = sorted(rbps.items(), key=lambda kv: kv[1], reverse=True)

    tsv_path = os.path.join(out_dir, f"{label}_RBPs.tsv")
    with open(tsv_path, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["protein_name", "score", "length"])
        for name, score in rows:
            w.writerow([name, f"{score:.6f}", lengths.get(name, "NA")])

    faa_path = os.path.join(out_dir, f"{label}_RBPs.faa")
    with open(faa_path, "w") as fh:
        for name, _ in rows:
            if name in records:
                SeqIO.write(records[name], fh, "fasta")

    for lab, cnt in score_histogram(list(rbps.values())):
        print(f"    score {lab}: {cnt}")

    # tag each record with sample for the combined FASTA
    return label, rbps, records, lengths


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--sample", nargs=3, action="append", metavar=("LABEL", "PRED_CSV", "FASTA"),
                    required=True, help="repeatable: label, prediction CSV, source protein FASTA")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    combined = []  # (label, name, score, length, record)
    for label, pred_csv, fasta in args.sample:
        lab, rbps, records, lengths = process_sample(label, pred_csv, fasta, args.out_dir)
        for name, score in rbps.items():
            combined.append((lab, name, score, lengths.get(name, "NA"), records.get(name)))

    combined.sort(key=lambda x: x[2], reverse=True)

    comb_tsv = os.path.join(args.out_dir, "all_metagenome_RBPs.tsv")
    with open(comb_tsv, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["sample", "protein_name", "score", "length"])
        for lab, name, score, length, _ in combined:
            w.writerow([lab, name, f"{score:.6f}", length])

    comb_faa = os.path.join(args.out_dir, "all_metagenome_RBPs.faa")
    with open(comb_faa, "w") as fh:
        for lab, name, _, _, rec in combined:
            if rec is not None:
                rec.id = f"{lab}|{rec.id}"
                rec.description = ""
                SeqIO.write(rec, fh, "fasta")

    print(f"\nCombined: {len(combined)} RBPs across {len(args.sample)} samples")
    print(f"Wrote {comb_tsv} and {comb_faa}")


if __name__ == "__main__":
    main()
