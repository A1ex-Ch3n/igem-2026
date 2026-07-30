#!/usr/bin/env python
"""
0730 synteny + similarity — stage 1: extract proteomes and gene tables.

Our phage (9-2-1 Phi8) proteome comes from the PI's canonical UUAIURNK_ Pharokka
run (numbering convention adopted repo-wide on 0716). Reference proteomes are
parsed from RefSeq GenBank flat files:
  T7      NC_001604  Autographiviridae type species (coliphage)
  phiKMV  NC_005045  Pseudomonas T7-like podophage (host-matched)
  KP32    NC_013647  KP32virus type (the genus Latka & Briers 2019 classify)

Writes, for our phage and each reference:
  <name>.faa   protein FASTA (id = CDS/locus id)
  <name>.tsv   id <TAB> start <TAB> end <TAB> strand <TAB> product   (genome order)

faa/tsv are written to WORK (a no-space dir) because mmseqs breaks on the repo
path's space; see memory local_env_gotchas.
"""
import sys, os, csv
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GFF  = os.path.join(REPO, "code/0713_espinoza_structural_mapping/pharokka_espinoza/pharokka.gff")
FAA  = os.path.join(REPO, "code/0713_espinoza_structural_mapping/pharokka_espinoza/phanotate.faa")
REFS = os.path.join(REPO, "code/0730_synteny_group_d/refs")

WORK = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "code/0730_synteny_group_d/work")
os.makedirs(WORK, exist_ok=True)


def write(name, rows, seqs):
    """rows: list of (id, start, end, strand, product) in genome order."""
    with open(os.path.join(WORK, name + ".tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["id", "start", "end", "strand", "product"])
        for r in rows:
            w.writerow(r)
    with open(os.path.join(WORK, name + ".faa"), "w") as fh:
        for i, _, _, _, _ in rows:
            if i in seqs:
                fh.write(f">{i}\n{seqs[i]}\n")
    print(f"{name}: {len(rows)} CDS, {sum(1 for i,*_ in rows if i in seqs)} with protein")


def our_phage():
    seqs = {r.id: str(r.seq).rstrip("*") for r in SeqIO.parse(FAA, "fasta")}
    rows = []
    for line in open(GFF):
        if line.startswith("#") or "\tCDS\t" not in line:
            continue
        f = line.rstrip("\n").split("\t")
        start, end, strand = int(f[3]), int(f[4]), f[6]
        attrs = dict(kv.split("=", 1) for kv in f[8].split(";") if "=" in kv)
        cid = attrs.get("ID", "")
        prod = attrs.get("product", "").strip()
        rows.append((cid, start, end, strand, prod))
    rows.sort(key=lambda r: r[1])
    write("our_phage", rows, seqs)


def reference(name, gb):
    rec = SeqIO.read(gb, "genbank")
    rows, seqs = [], {}
    n = 0
    for feat in rec.features:
        if feat.type != "CDS":
            continue
        q = feat.qualifiers
        # stable id: locus_tag > protein_id > synthetic
        cid = (q.get("locus_tag") or q.get("protein_id") or [f"{name}_{n:04d}"])[0]
        n += 1
        start = int(feat.location.start) + 1
        end = int(feat.location.end)
        strand = "+" if feat.location.strand == 1 else "-"
        prod = (q.get("product") or ["hypothetical protein"])[0]
        rows.append((cid, start, end, strand, prod))
        tr = q.get("translation")
        if tr:
            seqs[cid] = tr[0]
    rows.sort(key=lambda r: r[1])
    write(name, rows, seqs)


if __name__ == "__main__":
    our_phage()
    reference("T7", os.path.join(REFS, "T7.gb"))
    reference("phiKMV", os.path.join(REFS, "phiKMV.gb"))
    reference("KP32", os.path.join(REFS, "KP32.gb"))
    print("WORK =", WORK)
