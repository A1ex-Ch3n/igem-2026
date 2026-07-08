#!/usr/bin/env python3
"""
Compare our SPAdes assembly of 9-2-1 Φ8 with the PI group's assembly.
Confirms: same genome (k-mer containment), the PI's terminal repeat (DTR), and that ours is the
same genome with one DTR copy trimmed + reverse-complemented + rotated.

Usage: python3 compare_to_PI_assembly.py <PI.fasta> <ours.fasta>
Local only — no sequences leave the machine.
"""
import sys
from pathlib import Path
TAB = str.maketrans("ACGT", "TGCA")
rc = lambda s: s.translate(TAB)[::-1]
def canon(k): r = k.translate(TAB)[::-1]; return k if k <= r else r
def rd(p): return "".join(l.strip() for l in Path(p).read_text().splitlines() if not l.startswith(">"))

def main():
    prof, ours = rd(sys.argv[1]), rd(sys.argv[2])
    K = 31
    pk = {canon(prof[i:i+K]) for i in range(len(prof)-K+1) if "N" not in prof[i:i+K]}
    ok = {canon(ours[i:i+K]) for i in range(len(ours)-K+1) if "N" not in ours[i:i+K]}
    inter = len(ok & pk)
    print(f"lengths: PI {len(prof)} bp | ours {len(ours)} bp | diff {len(prof)-len(ours)} bp")
    print(f"same-genome (k={K}): {100*inter/len(ok):.2f}% of ours' k-mers are in PI's")
    # PI terminal repeat (DTR)
    dtr = 0
    for k in range(400, 5, -1):
        if prof[:k] == prof[-k:]: dtr = k; break
    print(f"PI exact terminal repeat (DTR): {dtr} bp")
    if dtr:
        print(f"  DTR seq: {prof[:dtr]}")
        print(f"  DTR found in ours (fwd): {ours.find(prof[:dtr])}  (revcomp): {ours.find(rc(prof[:dtr]))}")
        print(f"  PI − 1 DTR copy = {len(prof)-dtr} bp  vs ours {len(ours)} bp")

if __name__ == "__main__":
    main()
