"""
Build the ColabFold binding-screen input for the 9-2-1 Φ8 union RBPs × the
15-receptor 9-2-1 shortlist (8 × 15 = 120 pairs).

Output `binding_pairs.csv` is ColabFold format: `id,sequence` where the complex
is the two chains joined by ':' (RBP:receptor). id = `<RBP>__<REC>` so the
existing collector (`collect_binding.py`, single '__' split) can decode it.

Run this screen with REAL MSA (default remote mmseqs2_uniref_env), NOT
single_sequence — that mode's controls don't separate (see project docs).
"""

import csv
import os
import re

from Bio import SeqIO

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RBP_FAA = os.path.join(REPO, "code/output/0712_phage_rbp_detect/9-2-1_phi8_RBPs_union.faa")
REC_FAA = os.path.join(REPO, "code/0708_rbp_analysis/fold/receptor_shortlist_9-2-1.faa")

CDS_RE = re.compile(r"CDS_(\d+)")


def rbp_id(rec_id):
    m = CDS_RE.search(rec_id)
    return f"CDS_{m.group(1)}" if m else rec_id.split()[0]


def main():
    rbps = [(rbp_id(r.id), str(r.seq)) for r in SeqIO.parse(RBP_FAA, "fasta")]
    recs = [(r.id.split()[0], str(r.seq)) for r in SeqIO.parse(REC_FAA, "fasta")]

    out = os.path.join(HERE, "binding_pairs.csv")
    n = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "sequence"])
        for rid, rseq in rbps:
            for cid, cseq in recs:
                assert "__" not in rid and "__" not in cid, "ids must not contain '__'"
                w.writerow([f"{rid}__{cid}", f"{rseq}:{cseq}"])
                n += 1
    print(f"Wrote {out}: {len(rbps)} RBP × {len(recs)} receptor = {n} pairs")
    lens = [len(rs) + len(cs) for _, rs in rbps for _, cs in recs]
    print(f"complex length min/mean/max = {min(lens)}/{sum(lens)//len(lens)}/{max(lens)}")


if __name__ == "__main__":
    main()
