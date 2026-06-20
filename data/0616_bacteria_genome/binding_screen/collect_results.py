#!/usr/bin/env python3
"""
Stage 5 — collect ColabFold scores into a binding matrix (local, no GPU).

Walks a ColabFold results directory for the top-ranked score JSON of each job
(`*_scores_rank_001_*.json`), reads ipTM / pTM / max_pae, decodes the job id
(<strain>__<phage_id>__<receptor_id>), and writes binding_matrix.csv — the input
to make_heatmap.py.

Usage:
  python3 collect_results.py <results_dir> [out.csv]
  (default out: binding_matrix.csv)
"""
import sys, json, csv, re
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: collect_results.py <results_dir> [out.csv]")
    results = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("binding_matrix.csv")

    files = sorted(results.rglob("*_scores_rank_001_*.json"))
    rows, bad = [], 0
    for f in files:
        jid = f.name.split("_scores_rank")[0]
        parts = jid.split("__")
        if len(parts) != 3:
            bad += 1; continue
        strain, phage, receptor = parts
        try:
            d = json.load(open(f))
        except Exception:
            bad += 1; continue
        iptm = d.get("iptm")
        ptm = d.get("ptm")
        max_pae = d.get("max_pae")
        if iptm is None:
            bad += 1; continue
        rows.append([strain, phage, receptor, iptm, ptm, max_pae])

    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["strain", "phage_id", "receptor_id", "iptm", "ptm", "max_pae"])
        w.writerows(rows)
    print(f"parsed {len(rows)} pairs from {len(files)} rank_001 files -> {out}"
          + (f"  ({bad} skipped)" if bad else ""))

if __name__ == "__main__":
    main()
