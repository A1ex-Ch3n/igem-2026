#!/usr/bin/env python3
"""
Extract the O-antigen (OSA) biosynthesis locus from each isolate's Bakta
annotation and write a per-gene table + per-strain protein/nucleotide FASTA.

Why an anchor-based extraction instead of hard-coded coordinates:
the locus is a variable cassette dropped into a conserved slot, so the only
stable landmark is its flanks.  In all five genomes the upstream flank reads

    30S ribosomal protein S1 -> integration host factor subunit beta (ihfB)
    -> Lipopolysaccharide assembly protein A -> MBL fold metallo-hydrolase

`ihfB` (a.k.a. himD) is the canonical upstream flank of the Pseudomonas OSA
cluster in the literature, so this anchor is not an arbitrary choice.  The
cassette starts at the gene immediately after the MBL hydrolase; it ends where
the run of polysaccharide-biosynthesis genes stops (gap-tolerant, see GAP).

Outputs -> code/output/0727_o_antigen_comparison/
    locus_table.tsv        one row per cassette gene, all strains
    locus_<strain>.faa     cassette proteins
    locus_<strain>.ffn     cassette CDS nucleotides
    locus_bounds.tsv       resolved cassette boundaries + flank check
"""
from __future__ import annotations

import io
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/0727_o_antigen_comparison"

# strain -> directory holding the Bakta `annotation/` folder
GENOMES = {
    "9-2-1":   "data/bacteria_genome/9-2-1",
    "9-6-2":   "data/bacteria_genome/9-6-2/rerun_QB9Y48",
    "10-10-2": "data/bacteria_genome/10-10-2",
    "8-5-2":   "data/bacteria_genome/8-5-2",
    "8-10-2":  "data/bacteria_genome/8-10-2",
}

# which ANI-distinct strain each isolate belongs to (code/0627_unique_strain_table)
STRAIN_OF = {
    "9-2-1": "Strain 2", "9-6-2": "Strain 2",
    "8-5-2": "Strain 1", "10-10-2": "Strain 1",
    "8-10-2": "Strain 3",
}

UPSTREAM_ANCHOR = "Lipopolysaccharide assembly protein A"
ANCHOR_NEXT = "MBL fold metallo-hydrolase"

# A cassette gene is one whose product looks like sugar/polysaccharide biology.
KEEP = re.compile(
    r"glycosyl|glycosyltransferase|transferase|epimerase|dehydratase|reductase|"
    r"dehydrogenase|oxidase|flippase|polymerase|polysaccharide|O-antigen|sugar|"
    r"amidotransferase|aminotransferase|acyltransferase|CapD|Eps[A-Z]|Wb[a-z]|"
    r"Wz[a-z]|isomerase|synthase subunit HisH|acetamidino|hypothetical|DUF|"
    r"kinase|ligase|SDR family|NAD-dependent|Spore maturation|Competence",
    re.I,
)
# genes that mark the far side of the cassette even though they match KEEP
STOP_AT = re.compile(r"Beta-ketoacyl synthase|Competence protein ComEA", re.I)
GAP = 3  # tolerate this many consecutive non-matching genes inside a cassette


def load_bakta_tsv(path: Path) -> pd.DataFrame:
    lines = path.read_text().splitlines()
    h = next(i for i, l in enumerate(lines) if l.startswith("#Sequence Id"))
    txt = "\n".join([lines[h].lstrip("#")] + lines[h + 1:])
    df = pd.read_csv(io.StringIO(txt), sep="\t", dtype=str)
    return df[df["Type"] == "cds"].reset_index(drop=True)


def read_fasta(path: Path) -> dict[str, str]:
    seqs, key = {}, None
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            key = line[1:].split()[0]
            seqs[key] = []
        elif key:
            seqs[key].append(line.strip())
    return {k: "".join(v) for k, v in seqs.items()}


def find_cassette(df: pd.DataFrame) -> tuple[int, int]:
    """Return (start_row, end_row) inclusive for the variable cassette."""
    hits = df.index[df["Product"].str.contains(UPSTREAM_ANCHOR, na=False)]
    if len(hits) != 1:
        raise SystemExit(f"expected exactly 1 '{UPSTREAM_ANCHOR}', got {len(hits)}")
    anchor = hits[0]
    if ANCHOR_NEXT not in str(df.loc[anchor + 1, "Product"]):
        raise SystemExit(f"flank check failed: {df.loc[anchor + 1, 'Product']!r}")

    start = anchor + 2
    end, gap = start - 1, 0
    for i in range(start, len(df)):
        product = str(df.loc[i, "Product"])
        if STOP_AT.search(product):
            break
        if KEEP.search(product):
            end, gap = i, 0
        else:
            gap += 1
            if gap > GAP:
                break
    return start, end


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows, bounds = [], []

    for strain, rel in GENOMES.items():
        ann = ROOT / rel / "annotation"
        tsv = next(ann.glob("*_reference.tsv"))
        df = load_bakta_tsv(tsv)
        faa = read_fasta(next(ann.glob("*_reference.faa")))
        ffn = read_fasta(next(ann.glob("*_reference.ffn")))

        s, e = find_cassette(df)
        anchor = s - 2
        cassette = df.loc[s:e]

        bounds.append({
            "isolate": strain,
            "strain_group": STRAIN_OF[strain],
            "upstream_flank": df.loc[anchor, "Locus Tag"],
            "first_gene": df.loc[s, "Locus Tag"],
            "last_gene": df.loc[e, "Locus Tag"],
            "downstream_flank": df.loc[e + 1, "Locus Tag"],
            "downstream_flank_product": df.loc[e + 1, "Product"],
            "n_genes": len(cassette),
            "start_bp": df.loc[s, "Start"],
            "end_bp": df.loc[e, "Stop"],
            "span_bp": int(df.loc[e, "Stop"]) - int(df.loc[s, "Start"]) + 1,
        })

        for pos, (_, r) in enumerate(cassette.iterrows(), start=1):
            tag = r["Locus Tag"]
            rows.append({
                "isolate": strain,
                "strain_group": STRAIN_OF[strain],
                "position": pos,
                "locus_tag": tag,
                "gene": r["Gene"] if pd.notna(r["Gene"]) else "",
                "product": r["Product"],
                "strand": r["Strand"],
                "start": r["Start"],
                "stop": r["Stop"],
                "length_aa": len(faa.get(tag, "")),
            })

        for ext, seqs in (("faa", faa), ("ffn", ffn)):
            path = OUT / f"locus_{strain}.{ext}"
            with path.open("w") as fh:
                for _, r in cassette.iterrows():
                    tag = r["Locus Tag"]
                    if tag in seqs:
                        fh.write(f">{strain}|{tag} {r['Product']}\n{seqs[tag]}\n")

    pd.DataFrame(rows).to_csv(OUT / "locus_table.tsv", sep="\t", index=False)
    bdf = pd.DataFrame(bounds)
    bdf.to_csv(OUT / "locus_bounds.tsv", sep="\t", index=False)
    print(bdf.to_string(index=False))
    print(f"\nwrote {len(rows)} cassette genes -> {OUT}/locus_table.tsv")


if __name__ == "__main__":
    main()
