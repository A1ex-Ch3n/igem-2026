#!/usr/bin/env python3
"""Split esm_pairs.tsv into chunks/chunk_NNN.tsv (N pairs each, header repeated).
Prints the sbatch array range. Usage: python3 split_esm.py [N=60] [esm_pairs.tsv]"""
import csv
import math
import os
import sys

n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
src = sys.argv[2] if len(sys.argv) > 2 else "esm_pairs.tsv"

rows = list(csv.reader(open(src), delimiter="\t"))
header, data = rows[0], rows[1:]
os.makedirs("chunks", exist_ok=True)
nch = math.ceil(len(data) / n)
for i in range(nch):
    with open(f"chunks/chunk_{i:03d}.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(header)
        w.writerows(data[i * n:(i + 1) * n])
print(f"{len(data)} pairs -> {nch} chunks of {n}")
print(f"sbatch --array=0-{nch - 1}%8 esmfold.sbatch")
