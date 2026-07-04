#!/usr/bin/env python3
"""Concatenate per-chunk ESMFold result CSVs into binding_matrix.csv (columns include
rbp_id, rec_id, iptm — what fold_heatmap.py reads). Usage: python3 collect_esm.py [results] [binding_matrix.csv]"""
import csv
import glob
import os
import sys

d = sys.argv[1] if len(sys.argv) > 1 else "results"
out = sys.argv[2] if len(sys.argv) > 2 else "binding_matrix.csv"

files = sorted(f for f in glob.glob(os.path.join(d, "*.csv")) if os.path.basename(f) != os.path.basename(out))
header, rows = None, []
for f in files:
    rr = list(csv.reader(open(f)))
    if not rr:
        continue
    header = rr[0]
    rows.extend(rr[1:])

header = header or ["rbp_id", "rec_id", "iptm", "ptm", "interchain_pae_min",
                    "interchain_pae_mean", "plddt_mean", "len", "status"]
with open(out, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(header)
    w.writerows(rows)

ok = sum(1 for r in rows if len(r) >= 9 and r[8] == "OK")
print(f"{len(rows)} rows from {len(files)} chunk files -> {out}  ({ok} OK)")
