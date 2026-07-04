#!/usr/bin/env python3
"""Distribute boltz_input/*.yaml into chunks/chunk_NNN/ subdirs for a Slurm array.
  python3 split_boltz.py [chunk_size]   # default 40
Prints the array range for boltz.sbatch.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "boltz_input")
OUT = os.path.join(HERE, "chunks")
SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 40

yamls = sorted(f for f in os.listdir(SRC) if f.endswith(".yaml"))
os.makedirs(OUT, exist_ok=True)
n = 0
for i in range(0, len(yamls), SIZE):
    d = os.path.join(OUT, f"chunk_{n:03d}")
    os.makedirs(d, exist_ok=True)
    for f in yamls[i:i + SIZE]:
        shutil.copy(os.path.join(SRC, f), os.path.join(d, f))
    n += 1
print(f"{len(yamls)} YAMLs -> {n} chunks of {SIZE} in chunks/")
print(f"set:  sbatch --array=0-{n - 1}%8 boltz.sbatch")
