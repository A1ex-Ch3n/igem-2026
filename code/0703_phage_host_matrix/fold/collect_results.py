#!/usr/bin/env python3
"""
Collect ColabFold scores for the RBP × receptor fold into a matrix (local, no GPU).

Walks a ColabFold results dir for each job's top-ranked score JSON
(`*_scores_rank_001_*.json`), reads ipTM / pTM / max_pae, decodes the id
(<rbp_id>__<rec_id>), and writes binding_matrix.csv.

Usage: python3 collect_results.py <results_dir> [out.csv]   (default out: binding_matrix.csv)
"""
import csv
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: collect_results.py <results_dir> [out.csv]")
    results = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("binding_matrix.csv")
    files = sorted(results.rglob("*_scores_rank_001_*.json"))
    rows, bad = [], 0
    for f in files:
        parts = f.name.split("_scores_rank")[0].split("__")
        if len(parts) != 2:
            bad += 1; continue
        rbp, rec = parts
        try:
            d = json.load(open(f))
        except Exception:
            bad += 1; continue
        if d.get("iptm") is None:
            bad += 1; continue
        rows.append([rbp, rec, d.get("iptm"), d.get("ptm"), d.get("max_pae")])
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rbp_id", "rec_id", "iptm", "ptm", "max_pae"])
        w.writerows(rows)
    print(f"parsed {len(rows)} pairs from {len(files)} rank_001 files -> {out}"
          + (f"  ({bad} skipped)" if bad else ""))


if __name__ == "__main__":
    main()
