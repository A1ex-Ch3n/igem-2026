#!/usr/bin/env python3
"""
Build the phage-RBP x bacterial-receptor binding screen inputs.

Scope (decided 2026-06-16):
  Phage side  : tail fiber/spike + hypothetical YP_ accessions from *_phage_matches*.tsv (col2)
  Receptor side: surface-exposed outer-membrane proteins from *_potential_receptors.fasta
  Matrix       : per strain, phage_rbp x receptor

Outputs (under binding_screen/):
  phage_rbp/phage_rbp_accessions.tsv   strain, accession, class, description
  phage_rbp/phage_rbp_accessions.txt   unique accessions (for NCBI efetch)
  receptors/<strain>_receptors.fasta   filtered surface-OMP receptor sequences
  manifest/pairs.csv                   strain, phage_acc, receptor_locus, receptor_product
"""
import re, csv, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # .../binding_screen
DATA = ROOT.parent                              # .../0616_bacteria_genome

STRAINS = {
    "10-10-2": dict(tsv="10-10-2_phage_matches.tsv",        fasta="10-10-2_potential_receptors.fasta"),
    "9-2-1":   dict(tsv="9-2-1_phage_matches_summary.tsv",  fasta="9-2-1_potential_receptors.fasta"),
    "9-6-2":   dict(tsv="9-6-2_phage_matches_summary.tsv",  fasta="9-6-2_potential_receptors.fasta"),
}

# --- phage RBP classification (applied to col6 description = NCBI product of the YP_ hit) ---
TAIL = re.compile(r"tail fiber|tail spike|tailspike|fibre|baseplate|spike|tail protein", re.I)
HYPO = re.compile(r"hypothetical|uncharacteri|DUF|unknown function", re.I)

# --- surface outer-membrane receptor filter (applied to receptor product) ---
SURFACE = re.compile(
    r"TonB|siderophore|ferri|porin|Omp[A-Z]|Opr[A-Z]|LamB|BtuB|Fhu[A-Z]|Fep[A-Z]|Fox[A-Z]|"
    r"outer membrane|autotransporter|TolC|efflux|flagell|pil[iu]|fimbri|usher|LptD|O-antigen|LPS",
    re.I,
)

def read_fasta(path):
    name, seq, out = None, [], []
    for line in open(path):
        if line.startswith(">"):
            if name: out.append((name, "".join(seq)))
            name = line[1:].rstrip("\n"); seq = []
        else:
            seq.append(line.strip())
    if name: out.append((name, "".join(seq)))
    return out

def main():
    phage_rows, phage_acc = [], {}
    for strain, f in STRAINS.items():
        for line in open(DATA / f["tsv"]):
            c = line.rstrip("\n").split("\t")
            if len(c) < 6: continue
            acc, desc = c[1], c[5]
            cls = "tail" if TAIL.search(desc) else ("hypothetical" if HYPO.search(desc) else None)
            if not cls: continue
            phage_rows.append((strain, acc, cls, desc))
            phage_acc.setdefault(acc, desc)

    # phage outputs
    with open(ROOT / "phage_rbp/phage_rbp_accessions.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["strain", "accession", "class", "description"])
        w.writerows(sorted(set(phage_rows)))
    (ROOT / "phage_rbp/phage_rbp_accessions.txt").write_text("\n".join(sorted(phage_acc)) + "\n")

    # receptor outputs + pairs
    pairs = []
    recept_by_strain = {}
    for strain, f in STRAINS.items():
        kept = [(h, s) for h, s in read_fasta(DATA / f["fasta"]) if SURFACE.search(h)]
        recept_by_strain[strain] = kept
        with open(ROOT / f"receptors/{strain}_receptors.fasta", "w") as fh:
            for h, s in kept:
                fh.write(f">{h}\n{s}\n")

    phage_by_strain = {}
    for strain, acc, cls, desc in phage_rows:
        phage_by_strain.setdefault(strain, {}).setdefault(acc, cls)

    with open(ROOT / "manifest/pairs.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["strain", "phage_acc", "phage_class", "receptor_locus", "receptor_product"])
        for strain in STRAINS:
            for acc, cls in sorted(phage_by_strain.get(strain, {}).items()):
                for h, _ in recept_by_strain[strain]:
                    locus = h.split()[0]
                    product = " ".join(h.split()[1:])
                    w.writerow([strain, acc, cls, locus, product])
                    pairs.append(1)

    # summary
    print(f"unique phage RBP accessions (union): {len(phage_acc)}")
    for strain in STRAINS:
        np_ = len(phage_by_strain.get(strain, {}))
        nr = len(recept_by_strain[strain])
        print(f"  {strain:<8} phage={np_:<3} receptors={nr:<4} pairs={np_*nr:,}")
    print(f"TOTAL pairs (Tier-1 folds): {len(pairs):,}")

if __name__ == "__main__":
    main()
