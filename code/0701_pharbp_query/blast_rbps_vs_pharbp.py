"""
Track B — annotate our RBPs by BLASTP against the PharBP database (pharbp.ugent.be).

For each of our predicted RBP protein sequences, submit a BLASTP query to PharBP and
record the top hits, each of which carries the matched phage + host bacterium. This
tells us which of our (de novo / literature) RBPs resemble catalogued phage RBPs and
what hosts those are associated with.

PharBP has NO bacterial-receptor field, so this is RBP<->RBP homology (phage side),
not receptor lookup. Hits give: percent_identity, evalue, coverage, phage_name, host_names.

Mechanics (verified live):
  - CSRF: GET /blastp/ to obtain the `csrftoken` cookie, then send it as the
    X-CSRFToken header with a matching Referer on every POST.
  - Upload is ONE sequence per request (multi-FASTA gets concatenated!), returns a
    query_id and completes synchronously.
  - GET /api/blastp/results/<query_id>/ -> {total, results:[{protein_id, phage_name,
    host_names[], percent_identity, evalue, bit_score, query_coverage, ...}]}

Identical sequences are de-duplicated (submitted once, results fanned back out).
Resumable: re-running skips query IDs already present in the --out TSV.

Usage:
  python blast_rbps_vs_pharbp.py --fasta all_metagenome_RBPs.faa \
      --out ../output/0701_pharbp_query/rbp_vs_pharbp_hits.tsv [--top 5] [--sleep 0.3] [--limit N]
"""

import argparse
import csv
import hashlib
import os
import sys
import time

import requests
from Bio import SeqIO

BASE = "https://pharbp.ugent.be"
UPLOAD = f"{BASE}/api/blastp/upload/"
RESULTS = f"{BASE}/api/blastp/results/"
PAGE = f"{BASE}/blastp/"

COLS = ["query_rbp_id", "hit_rank", "n_hits", "protein_id", "percent_identity",
        "evalue", "bit_score", "query_coverage", "phage_name", "host_names"]


def make_session():
    s = requests.Session()
    s.headers["User-Agent"] = "iGEM6317-pharbp-client/1.0"
    r = s.get(PAGE, timeout=30)
    r.raise_for_status()
    if "csrftoken" not in s.cookies:
        sys.exit("ERROR: no csrftoken cookie from /blastp/ — site layout changed?")
    return s


def blast_one(session, seq, top):
    """Submit one sequence, return list of up to `top` hit dicts (or None on failure)."""
    tok = session.cookies.get("csrftoken")
    headers = {"X-CSRFToken": tok, "Referer": PAGE}
    try:
        up = session.post(UPLOAD, data={"sequence": seq}, headers=headers, timeout=120)
        up.raise_for_status()
        qid = up.json().get("query_id")
        if not qid:
            return None
        res = session.get(f"{RESULTS}{qid}/", timeout=60)
        res.raise_for_status()
        return res.json().get("results", [])[:top]
    except (requests.RequestException, ValueError) as e:
        print(f"  [warn] request failed: {e}", file=sys.stderr)
        return None


def load_done(out_path):
    done = set()
    if os.path.exists(out_path):
        with open(out_path, newline="") as fh:
            r = csv.DictReader(fh, delimiter="\t")
            for row in r:
                done.add(row["query_rbp_id"])
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=5, help="top hits kept per query")
    ap.add_argument("--sleep", type=float, default=0.3, help="polite delay between requests")
    ap.add_argument("--limit", type=int, default=None, help="only first N records (testing)")
    args = ap.parse_args()

    # read fasta, group ids by identical sequence
    seq_to_ids = {}
    order = []
    for i, rec in enumerate(SeqIO.parse(args.fasta, "fasta")):
        if args.limit is not None and i >= args.limit:
            break
        seq = str(rec.seq).rstrip("*").strip()
        if not seq:
            continue
        seq_to_ids.setdefault(seq, []).append(rec.id)
        if seq not in order:
            order.append(seq)

    total_ids = sum(len(v) for v in seq_to_ids.values())
    print(f"{total_ids} RBPs -> {len(order)} unique sequences to BLAST")

    done = load_done(args.out)
    if done:
        print(f"Resuming: {len(done)} RBP IDs already in {args.out}")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    new_file = not os.path.exists(args.out) or os.path.getsize(args.out) == 0
    out = open(args.out, "a", newline="")
    w = csv.writer(out, delimiter="\t")
    if new_file:
        w.writerow(COLS)
        out.flush()

    session = make_session()
    t0 = time.time()
    done_seqs = 0
    for seq in order:
        ids = seq_to_ids[seq]
        if all(i in done for i in ids):
            continue
        hits = blast_one(session, seq, args.top)
        done_seqs += 1
        rows = []
        if hits:
            for rank, h in enumerate(hits, 1):
                hosts = h.get("host_names") or []
                rows.append([
                    "{id}", rank, len(hits), h.get("protein_id", ""),
                    h.get("percent_identity", ""), h.get("evalue", ""),
                    h.get("bit_score", ""), h.get("query_coverage", ""),
                    h.get("phage_name", ""), "; ".join(hosts),
                ])
        else:
            rows.append(["{id}", 0, 0, "", "", "", "", "", "", ""])
        # fan out to every RBP id sharing this sequence
        for rbp_id in ids:
            if rbp_id in done:
                continue
            for r in rows:
                w.writerow([rbp_id] + r[1:])
        out.flush()
        if done_seqs % 25 == 0:
            rate = done_seqs / max(time.time() - t0, 1e-6)
            print(f"  {done_seqs}/{len(order)} unique done | {rate:.1f} seq/s", flush=True)
        time.sleep(args.sleep)

    out.close()
    print(f"Done. {done_seqs} sequences queried in {(time.time()-t0)/60:.1f} min. Out: {args.out}")


if __name__ == "__main__":
    main()
