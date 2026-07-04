#!/usr/bin/env python3
"""Split all_pairs.csv into fixed-size chunk CSVs for a Slurm array.
Run from the fold workspace (paths relative to this file's dir).
  python3 split_input.py [chunk_size]   # default 40
Prints the array range for rbp_receptor.sbatch.
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "all_pairs.csv")
OUT = os.path.join(ROOT, "chunks")
SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 40

os.makedirs(OUT, exist_ok=True)
rows = list(csv.reader(open(SRC)))
header, data = rows[0], rows[1:]
n = 0
for i in range(0, len(data), SIZE):
    with open(os.path.join(OUT, f"chunk_{n:03d}.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(header); w.writerows(data[i:i + SIZE])
    n += 1
print(f"{len(data)} pairs -> {n} chunks of {SIZE} in chunks/")
print(f"set in rbp_receptor.sbatch:  #SBATCH --array=0-{n - 1}%8")
