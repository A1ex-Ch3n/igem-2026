#!/usr/bin/env python3
"""Split colabfold_input/all_pairs.csv into fixed-size chunk CSVs for a Slurm array.
Run from the binding_screen root (or anywhere — paths are resolved relative to this file).
  python3 cluster/split_input.py [chunk_size]   # default 40
Prints the array range to use in tier1_array.sbatch (#SBATCH --array=0-<N>).
"""
import csv, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent           # binding_screen/
SRC = ROOT / "colabfold_input/all_pairs.csv"
OUT = ROOT / "colabfold_input/chunks"
SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 40

def main():
    OUT.mkdir(exist_ok=True)
    rows = list(csv.reader(open(SRC)))
    header, data = rows[0], rows[1:]
    n = 0
    for i in range(0, len(data), SIZE):
        with open(OUT / f"chunk_{n:03d}.csv", "w", newline="") as fh:
            w = csv.writer(fh); w.writerow(header); w.writerows(data[i:i+SIZE])
        n += 1
    print(f"{len(data)} pairs -> {n} chunks of {SIZE} in colabfold_input/chunks/")
    print(f"set in tier1_array.sbatch:  #SBATCH --array=0-{n-1}%8")

if __name__ == "__main__":
    main()
