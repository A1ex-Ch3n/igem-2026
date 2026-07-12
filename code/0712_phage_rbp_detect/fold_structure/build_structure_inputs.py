"""
Build ColabFold structure-prediction inputs for the 9-2-1 Phi8 union RBP set.

Reads the union FASTA (RBP Detect union Pharokka) and writes two ColabFold CSVs
(`id,sequence`; a homo-oligomer is the same sequence joined by ':'):
  structures_monomers.csv   every union RBP, folded as a monomer
  structures_trimers.csv    the homotrimeric candidates (tail spikes + tail fiber)

Tail spikes/fibers are functional as homotrimers, so the trimer fold is the
decisive test for the right-handed beta-helix / beta-solenoid depolymerase
signature. Run both with `--msa-mode single_sequence` on Laguna (novel phage
sequences must NOT be uploaded to the public MSA server).
"""

import csv
import os
import re

from Bio import SeqIO

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
UNION_FAA = os.path.join(REPO, "code/output/0712_phage_rbp_detect/9-2-1_phi8_RBPs_union.faa")

# CDS to also fold as a homotrimer (functional oligomeric state of tail spikes/fibers).
TRIMER_CDS = {"0015", "0016", "0018"}

CDS_RE = re.compile(r"CDS_(\d+)")


def cds_num(rec_id):
    m = CDS_RE.search(rec_id)
    return m.group(1) if m else rec_id


def main():
    recs = list(SeqIO.parse(UNION_FAA, "fasta"))

    mono_path = os.path.join(HERE, "structures_monomers.csv")
    tri_path = os.path.join(HERE, "structures_trimers.csv")

    with open(mono_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "sequence"])
        for r in recs:
            n = cds_num(r.id)
            w.writerow([f"9-2-1_phi8__CDS_{n}__monomer", str(r.seq)])

    with open(tri_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "sequence"])
        for r in recs:
            n = cds_num(r.id)
            if n in TRIMER_CDS:
                s = str(r.seq)
                w.writerow([f"9-2-1_phi8__CDS_{n}__trimer", ":".join([s, s, s])])

    n_tri = sum(1 for r in recs if cds_num(r.id) in TRIMER_CDS)
    print(f"Wrote {mono_path} ({len(recs)} monomers)")
    print(f"Wrote {tri_path} ({n_tri} trimers: CDS {sorted(TRIMER_CDS)})")


if __name__ == "__main__":
    main()
