#!/usr/bin/env python3
"""Candidate Registry sequences for the six parts — CDS only, no vector, no tag.

What the Twist order sheets actually contain is an **insert**, not a part: it has
its own stop codon but **no start codon**, because translation initiates at
pET-28a's `ATG` inside the `MGSSHHHHHHSSGLVPRGSHM` leader. CDS11's insert carries
a further designed `GGSGGGGS`-His6-`ENLYFQ`-`GGGGSGGGGS` purification linker in
front of the fiber itself.

Neither the vector leader nor the purification linker is the biological part, so
what goes on the Registry is: **`ATG` + the protein's own coding sequence + stop**.
This script writes exactly that, plus a table of what was trimmed, so the decision
is visible rather than buried.

Outputs -> code/output/1018_construct_structures/registry/
    registry_parts.ffn     nucleotide, ready to paste into the Registry
    registry_parts.faa     the protein each one encodes
    registry_parts.tsv     lengths, what was trimmed, translation check
"""
from __future__ import annotations

import csv
from pathlib import Path

from Bio.Seq import Seq

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/1018_construct_structures/registry"
ORDERS = [
    ROOT / "documents/2026-07-27_twist_construct_order/constructs/iGEM-design_First_Set.csv",
    ROOT / "documents/2026-09-10_twist_construct_order_second_set/constructs/iGEM-design_Second_Set.csv",
]

# Twist's sheet name -> the name we use everywhere else
RENAME = {
    "CDS10_WT_NOTAG": "CDS10_WT",
    "CDS11_WT_CTERM_HIS6TAG": "CDS11_WT",
    "CDS12_WT_NOTAG": "CDS12_WT",
}

# protein-level prefix designed into the insert for purification, not part of the
# biological sequence; trimmed in frame. CDS11 only.
DESIGNED_LINKERS = {"CDS11_WT": "GGSGGGGSHHHHHHENLYFQGGGGSGGGGS"}

DESCRIPTION = {
    "CDS10_WT": "CDS_0010 res 105-917, unknown-function virion fiber sharing the "
                "Calx-beta anchor of the tail spike",
    "CDS11_WT": "CDS_0011 res 305-941, tail-spike beta-helix depolymerase body + foldon",
    "CDS12_WT": "CDS_0012 res 117-477, GH5 glycoside hydrolase (TIM barrel)",
    "CDS12_ANC_Node1": "reconstructed ancestor of CDS_0012 (GH5), node 1",
    "CDS12_ANC_Node40": "reconstructed ancestor of CDS_0012 (GH5), node 40",
    "CDS12_ANC_Node281": "reconstructed ancestor of CDS_0012 (GH5), node 281",
}


def load_inserts() -> dict[str, str]:
    out = {}
    for path in ORDERS:
        with open(path, encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                name = RENAME.get(row["Name"], row["Name"])
                out[name] = row["Insert sequence"].strip().upper()
    return out


def to_registry_cds(name: str, insert: str) -> tuple[str, str, dict]:
    """ATG + the protein's own CDS + stop, with the designed linker trimmed."""
    trimmed_aa = 0
    linker = DESIGNED_LINKERS.get(name)
    if linker:
        protein = str(Seq(insert).translate())
        if not protein.startswith(linker):
            raise ValueError(f"{name}: expected linker {linker}, got {protein[:40]}")
        trimmed_aa = len(linker)
        insert = insert[trimmed_aa * 3:]

    cds = insert if insert.startswith("ATG") else "ATG" + insert
    protein = str(Seq(cds).translate())
    if not protein.endswith("*") or "*" in protein[:-1]:
        raise ValueError(f"{name}: translation is not a clean single ORF")

    note = {
        "name": name,
        "description": DESCRIPTION[name],
        "insert_bp_ordered": len(insert) + trimmed_aa * 3,
        "linker_trimmed_aa": trimmed_aa,
        "start_codon_added": "yes" if not insert.startswith("ATG") else "no",
        "registry_bp": len(cds),
        "protein_aa": len(protein) - 1,
        "clean_single_orf": "yes",
    }
    return cds, protein[:-1], note


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    inserts = load_inserts()
    notes, ffn, faa = [], [], []
    for name in DESCRIPTION:
        cds, protein, note = to_registry_cds(name, inserts[name])
        notes.append(note)
        header = f"{name} | {note['description']} | {note['registry_bp']} bp"
        ffn.append(f">{header}\n" + "\n".join(cds[i:i + 60] for i in range(0, len(cds), 60)))
        faa.append(f">{header}\n" + "\n".join(protein[i:i + 60]
                                              for i in range(0, len(protein), 60)))

    (OUT / "registry_parts.ffn").write_text("\n".join(ffn) + "\n")
    (OUT / "registry_parts.faa").write_text("\n".join(faa) + "\n")
    with open(OUT / "registry_parts.tsv", "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(notes[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(notes)
    for n in notes:
        print(f"{n['name']:20s} {n['registry_bp']:>5} bp  {n['protein_aa']:>4} aa  "
              f"ATG added: {n['start_codon_added']:3s}  linker trimmed: {n['linker_trimmed_aa']} aa")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
