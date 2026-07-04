#!/usr/bin/env python3
"""
Build the ESMFold pair list from probes.fasta (114 RBP families) x receptors_panel.fasta
(63 receptors), both copied into this workspace. Writes:
  esm_pairs.tsv        all 7,182 pairs  (rbp_id  rec_id  rbp_seq  rec_seq)
  esm_pairs_smoke.tsv  6 pairs (RBP0001..3 x REC001..2) for the smoke test
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def read_fasta(path):
    seqs, cur = {}, None
    for ln in open(path):
        ln = ln.rstrip()
        if ln.startswith(">"):
            cur = ln[1:].split()[0]
            seqs[cur] = []
        elif cur is not None:
            seqs[cur].append(ln)
    return {k: "".join(v) for k, v in seqs.items()}


def find(name):
    for c in (os.path.join(HERE, name),
              os.path.join(HERE, "..", "..", "..", "output", "0703_phage_host_matrix", "fold", name)):
        if os.path.exists(c):
            return c
    raise SystemExit(f"cannot find {name} (copy probes.fasta + receptors_panel.fasta into this dir)")


def main():
    rbps = read_fasta(find("probes.fasta"))
    recs = read_fasta(find("receptors_panel.fasta"))
    rbp_ids = sorted(rbps)
    rec_ids = sorted(recs)
    with open(os.path.join(HERE, "esm_pairs.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rbp_id", "rec_id", "rbp_seq", "rec_seq"])
        for rb in rbp_ids:
            for rc in rec_ids:
                w.writerow([rb, rc, rbps[rb], recs[rc]])
    with open(os.path.join(HERE, "esm_pairs_smoke.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rbp_id", "rec_id", "rbp_seq", "rec_seq"])
        for rb in rbp_ids[:3]:
            for rc in rec_ids[:2]:
                w.writerow([rb, rc, rbps[rb], recs[rc]])
    print(f"{len(rbp_ids)} RBP x {len(rec_ids)} receptor = {len(rbp_ids) * len(rec_ids)} pairs -> esm_pairs.tsv")
    print("6 smoke pairs -> esm_pairs_smoke.tsv")


if __name__ == "__main__":
    main()
