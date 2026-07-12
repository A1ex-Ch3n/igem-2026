"""
Build the ColabFold control-set input from the existing, sequence-complete
control pairs at code/output/0703_phage_host_matrix/fold/control_pairs.tsv
(3 literature positives + 3 scrambled + 3 mismatched negatives).

Run these THROUGH THE IDENTICAL pipeline (same MSA mode + colabfold_batch flags)
as the 120-pair screen. The screen's ipTM ranking is only trustworthy if the
positives separate from the scrambled/mismatched negatives here. Literature
positives: T5 pb5×FhuA, λ gpJ(rbd)×LamB, gp54×LptD.

Writes:
  control_pairs.csv   ColabFold `id,sequence` (id = <rbp>__<rec>, seq = rbp:rec)
  control_key.csv     id,class  (positive / scrambled / mismatch)
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC_PAIRS = os.path.join(REPO, "code/output/0703_phage_host_matrix/fold/control_pairs.tsv")
SRC_KEY = os.path.join(REPO, "code/output/0703_phage_host_matrix/fold/control_key.tsv")


def main():
    key = {}
    with open(SRC_KEY) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            key[(row["rbp_id"], row["rec_id"])] = row["class"]

    pairs_out = os.path.join(HERE, "control_pairs.csv")
    key_out = os.path.join(HERE, "control_key.csv")
    n = 0
    with open(SRC_PAIRS) as fh, \
            open(pairs_out, "w", newline="") as pf, open(key_out, "w", newline="") as kf:
        pw, kw = csv.writer(pf), csv.writer(kf)
        pw.writerow(["id", "sequence"])
        kw.writerow(["id", "class"])
        for row in csv.DictReader(fh, delimiter="\t"):
            rid, cid = row["rbp_id"], row["rec_id"]
            assert "__" not in rid and "__" not in cid
            jid = f"{rid}__{cid}"
            pw.writerow([jid, f"{row['rbp_seq']}:{row['rec_seq']}"])
            kw.writerow([jid, key.get((rid, cid), "unknown")])
            n += 1
    print(f"Wrote {pairs_out} ({n} control pairs) and {key_out}")


if __name__ == "__main__":
    main()
