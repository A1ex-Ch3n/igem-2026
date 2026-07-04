#!/usr/bin/env python3
"""
Build the ESMFold pair list from probes.fasta (114 RBP families) x receptors_panel.fasta
(63 receptors), both copied into this workspace. Writes:
  esm_pairs.tsv        all 7,182 pairs  (rbp_id  rec_id  rbp_seq  rec_seq)
  esm_pairs_smoke.tsv  6 pairs (RBP0001..3 x REC001..2) for the smoke test
  truncated_rbps.txt   the big RBPs whose row would otherwise be all-SKIP (see below)

Domain-aware truncation (--rbp-cap / --rbp-keep, default 1000 / 700): RBPs longer than the cap
get their row skipped entirely at --max-len 1600 (RBP + linker + receptor > 1600 for ~every
receptor). Tailspike/tail-fiber receptor-binding domains are C-TERMINAL, so we substitute the
C-terminal `--rbp-keep` residues for those RBPs — keeping 700 aa lets each big RBP score against
~62/63 receptors instead of 0, and still contains the RBD. These rows are flagged low-confidence
in truncated_rbps.txt. Pass --rbp-cap 0 to disable and fold full-length.
"""
import argparse
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--rbp-cap", type=int, default=1000,
                    help="RBPs longer than this get C-terminal-truncated (0 disables)")
    ap.add_argument("--rbp-keep", type=int, default=700,
                    help="keep this many C-terminal residues for over-cap RBPs (the RBD is C-terminal)")
    a = ap.parse_args()

    rbps = read_fasta(find("probes.fasta"))
    recs = read_fasta(find("receptors_panel.fasta"))

    truncated = {}
    if a.rbp_cap:
        for k, s in rbps.items():
            if len(s) > a.rbp_cap:
                truncated[k] = (len(s), a.rbp_keep)
                rbps[k] = s[-a.rbp_keep:]

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
    with open(os.path.join(HERE, "truncated_rbps.txt"), "w") as fh:
        fh.write("# RBPs C-terminally truncated to fit --max-len (flag these rows low-confidence)\n")
        fh.write("# rbp_id\torig_len\tkept_Cterm\n")
        for k in sorted(truncated):
            fh.write(f"{k}\t{truncated[k][0]}\t{truncated[k][1]}\n")

    print(f"{len(rbp_ids)} RBP x {len(rec_ids)} receptor = {len(rbp_ids) * len(rec_ids)} pairs -> esm_pairs.tsv")
    if truncated:
        print(f"C-terminally truncated {len(truncated)} big RBPs (>{a.rbp_cap} aa) to {a.rbp_keep} aa: "
              + ", ".join(sorted(truncated)) + "  (see truncated_rbps.txt)")
    print("6 smoke pairs -> esm_pairs_smoke.tsv")


if __name__ == "__main__":
    main()
