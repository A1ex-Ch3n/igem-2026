#!/usr/bin/env python3
"""
Terminal-redundancy / DTR check for a phage assembly — distinguishes:
  - LINEAR genome with a short Direct Terminal Repeat (T7-style): the DTR, collapsed once by the
    assembler, gets reads from BOTH genome ends -> a sharp ~2x read-coverage spike over the DTR.
  - CIRCULAR / circularly-permuted genome: uniform coverage, no terminal redundancy, no 2x spike,
    no coverage drop-off at the (arbitrary) contig ends.

Pure Python, no aligner needed: builds the contig's canonical k-mer set, streams a read subsample,
counts per-k-mer coverage, and profiles it along the contig. Local — no sequences leave the machine.

Usage:
  python3 check_terminal_redundancy.py <contig.fasta> <R1.fastq.gz> <R2.fastq.gz> [subsample_reads]
"""
import gzip, sys, statistics as st
from pathlib import Path

K = 31
TAB = str.maketrans("ACGT", "TGCA")

def canon(k):
    r = k.translate(TAB)[::-1]
    return k if k <= r else r

def read_contig(p):
    return "".join(l.strip() for l in Path(p).read_text().splitlines() if not l.startswith(">"))

def stream(path, maxr):
    n = 0
    with gzip.open(path, "rt") as f:
        while True:
            if not f.readline(): break
            s = f.readline().strip(); f.readline(); f.readline()
            yield s; n += 1
            if n >= maxr: break

def main():
    contig = read_contig(sys.argv[1]); L = len(contig)
    reads = sys.argv[2:4]
    sub = int(sys.argv[4]) if len(sys.argv) > 4 else 150000
    cov = {}
    for i in range(L - K + 1):
        km = contig[i:i+K]
        if "N" not in km: cov[canon(km)] = 0
    for path in reads:
        for s in stream(path, sub):
            for i in range(len(s) - K + 1):
                km = s[i:i+K]
                if "N" in km: continue
                ck = km if km <= (rk := km.translate(TAB)[::-1]) else rk
                c = cov.get(ck)
                if c is not None: cov[ck] = c + 1
    prof = [cov[canon(contig[i:i+K])] if "N" not in contig[i:i+K] else 0 for i in range(L - K + 1)]
    med = st.median(prof); mx = max(prof)
    print(f"contig {L} bp | subsample {sub} reads x{len(reads)} | median cov {med:.0f} | max {mx} "
          f"(max/median {mx/med:.2f}x)")
    thr = 1.6 * med
    runs = []
    i = 0
    while i < len(prof):
        if prof[i] >= thr:
            j = i
            while j < len(prof) and prof[j] >= thr: j += 1
            if j - i >= 15: runs.append((i+1, j, j-i))
            i = j
        else: i += 1
    print("first20 mean:", sum(prof[:20])//20, " last20 mean:", sum(prof[-20:])//20)
    if runs:
        print("Candidate DTR (>=1.6x median, >=15bp):", runs, "-> LINEAR + DTR")
    else:
        print("No >=1.6x-median run found -> uniform coverage -> CIRCULAR / no short linear DTR")

if __name__ == "__main__":
    main()
