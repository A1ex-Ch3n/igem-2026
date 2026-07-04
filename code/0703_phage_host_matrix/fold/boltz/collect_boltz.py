#!/usr/bin/env python3
"""
Collect Boltz-2 confidence scores into binding_matrix.csv (local, no GPU).

Walks a results dir for `confidence_<RBP>__<REC>_model_0.json`, reads iptm / ptm /
protein_iptm / complex_plddt, decodes the id, and writes binding_matrix.csv
(rbp_id, rec_id, iptm, ptm, protein_iptm) — same shape fold_heatmap.py expects.

Usage: python3 collect_boltz.py <results_dir> [out.csv]   (default out: binding_matrix.csv)
"""
import csv
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: collect_boltz.py <results_dir> [out.csv]")
    results = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("binding_matrix.csv")
    files = sorted(results.rglob("confidence_*_model_0.json"))
    rows, bad = [], 0
    for f in files:
        stem = f.name[len("confidence_"):-len("_model_0.json")]   # -> RBP__REC
        parts = stem.split("__")
        if len(parts) != 2:
            bad += 1; continue
        rbp, rec = parts
        try:
            d = json.load(open(f))
        except Exception:
            bad += 1; continue
        if d.get("iptm") is None:
            bad += 1; continue
        rows.append([rbp, rec, d.get("iptm"), d.get("ptm"), d.get("protein_iptm")])
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rbp_id", "rec_id", "iptm", "ptm", "protein_iptm"])
        w.writerows(rows)
    print(f"parsed {len(rows)} pairs from {len(files)} confidence files -> {out}"
          + (f"  ({bad} skipped)" if bad else ""))


if __name__ == "__main__":
    main()
