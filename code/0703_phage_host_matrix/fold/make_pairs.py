#!/usr/bin/env python3
"""
Rebuild all_pairs.csv + smoke.csv from probes.fasta + receptors_panel.fasta.

all_pairs.csv (~8 MB) is gitignored, so regenerate it after a fresh clone. This is just the
cartesian product (no mmseqs, no upstream data needed) — probes/receptors are the committed
inputs. Run from the workspace where probes.fasta and receptors_panel.fasta live.

Run: python3 make_pairs.py
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def read_fasta(path):
    name, buf = None, []
    for line in open(path):
        if line.startswith(">"):
            if name:
                yield name, "".join(buf)
            name, buf = line[1:].split()[0], []
        else:
            buf.append(line.strip())
    if name:
        yield name, "".join(buf)


def main():
    probes = dict(read_fasta(os.path.join(HERE, "probes.fasta")))
    recs = dict(read_fasta(os.path.join(HERE, "receptors_panel.fasta")))
    pairs = [(f"{r}__{c}", f"{rs}:{cs}") for r, rs in probes.items() for c, cs in recs.items()]
    with open(os.path.join(HERE, "all_pairs.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "sequence"]); w.writerows(pairs)
    fam, rec = list(probes)[:3], list(recs)[:2]
    smoke = [(f"{r}__{c}", f"{probes[r]}:{recs[c]}") for r in fam for c in rec][:6]
    with open(os.path.join(HERE, "smoke.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "sequence"]); w.writerows(smoke)
    print(f"{len(probes)} RBP × {len(recs)} receptor = {len(pairs)} pairs -> all_pairs.csv | smoke.csv: {len(smoke)}")


if __name__ == "__main__":
    main()
