#!/usr/bin/env python3
"""
Draw the O-antigen cassette comparison figure.

Five tracks, ordered so that the two clone pairs sit adjacent -- that way the
100%-identity links between 9-2-1/9-6-2 and 8-5-2/10-10-2 read as the internal
control they are, and the sparse links across strain groups read as the result.

Genes are coloured by functional role; links are MMseqs best hits shaded by
percent identity.

Outputs -> code/output/0727_o_antigen_comparison/
    o_antigen_loci_comparison.{png,svg}
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from pygenomeviz import GenomeViz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/0727_o_antigen_comparison"

# clone pairs adjacent; strain groups in genome-size order
ORDER = ["9-2-1", "9-6-2", "8-5-2", "10-10-2", "8-10-2"]
STRAIN_OF = {
    "9-2-1": "Strain 2", "9-6-2": "Strain 2",
    "8-5-2": "Strain 1", "10-10-2": "Strain 1",
    "8-10-2": "Strain 3",
}

CATEGORIES = [
    ("chain-length regulator (wzz)", "#c0392b",
     ("chain length regulator", "chain length determinant")),
    ("flippase (wzx)", "#e67e22", ("flippase",)),
    ("polymerase / ligase (wzy)", "#8e44ad",
     ("repeat unit polymerase", "o-antigen ligase", "polymerase")),
    ("glycosyltransferase", "#2980b9",
     ("glycosyltransferase", "glycosyl transferase")),
    ("dTDP-rhamnose pathway", "#16a085", ("dtdp-",)),
    ("nucleotide-sugar enzyme", "#27ae60",
     ("epimerase", "dehydratase", "reductase", "dehydrogenase", "oxidase",
      "aminotransferase", "acetyltransferase", "amidotransferase",
      "acyltransferase", "sdr family", "capd", "hish", "acetamidino")),
]
# "EpsG family protein" and "Polysaccharide biosynthesis protein" are the usual
# labels for Wzy- and Wzx-family proteins, but Bakta assigns them no Pfam/
# InterPro domain here (UniRef50 only), so they stay unassigned rather than
# being coloured as machinery we have not actually confirmed.  See README UNDONE.
OTHER = ("other / unassigned", "#95a5a6")

VMIN = 20.0  # link shading floor, matches the MMseqs easy-search identity floor

SHORT = {
    "O-antigen chain length regulator": "wzz",
    "Polysaccharide chain length determinant N-terminal domain-containing protein": "wzz-like",
    "Oligosaccharide flippase family protein": "wzx",
    "Oligosaccharide repeat unit polymerase": "wzy",
    "O-antigen ligase domain-containing protein": "waaL-like",
    "glucose-1-phosphate thymidylyltransferase RfbA": "rfbA",
    "dTDP-glucose 4,6-dehydratase": "rfbB",
    "dTDP-4-dehydrorhamnose reductase": "rfbD",
    "Glycosyltransferase WbuB": "wbuB",
    "Glycosyltransferase WbpL": "wbpL",
    "EpsG family protein": "epsG",
    "Capsular polysaccharide biosynthesis protein CapD": "capD",
    "N-acetyl sugar amidotransferase": "amidoT",
    "AglZ/HisF2 family acetamidino modification protein": "aglZ",
    "D-glucuronyl C5-epimerase family protein": "C5-epi",
    "UDP-N-acetyl-D-mannosamine dehydrogenase": "ManNAc-DH",
}


def categorise(product: str) -> tuple[str, str]:
    p = product.lower()
    for label, colour, keys in CATEGORIES:
        if any(k in p for k in keys):
            return label, colour
    return OTHER


def main() -> None:
    tbl = pd.read_csv(OUT / "locus_table.tsv", sep="\t", dtype=str)
    tbl["start"] = tbl["start"].astype(int)
    tbl["stop"] = tbl["stop"].astype(int)
    bounds = pd.read_csv(OUT / "locus_bounds.tsv", sep="\t").set_index("isolate")

    hits = pd.read_csv(OUT / "all_vs_all_hits.m8", sep="\t", header=None,
                       names=["query", "target", "fident", "alnlen", "evalue", "bits"])
    for col, new in (("query", "q"), ("target", "t")):
        hits[f"{new}i"] = hits[col].str.split("|").str[0]
        hits[f"{new}tag"] = hits[col].str.split("|").str[1]
    hits = hits[hits["qi"] != hits["ti"]]

    gv = GenomeViz(fig_track_height=0.95, feature_track_ratio=0.38,
                   track_align_type="left")

    track_name = {
        iso: (f"{iso}   [{STRAIN_OF[iso]}]   "
              f"{(tbl['isolate'] == iso).sum()} genes / "
              f"{int(bounds.loc[iso, 'span_bp']) / 1000:.1f} kb")
        for iso in ORDER
    }

    coords: dict[str, dict[str, tuple[int, int]]] = {}
    for iso in ORDER:
        sub = tbl[tbl["isolate"] == iso].copy()
        origin = int(bounds.loc[iso, "start_bp"])
        span = int(bounds.loc[iso, "span_bp"])
        track = gv.add_feature_track(track_name[iso], span, labelsize=11)
        seg = track.get_segment()

        coords[iso] = {}
        for _, r in sub.iterrows():
            s, e = r["start"] - origin, r["stop"] - origin
            coords[iso][r["locus_tag"]] = (s, e)
            _, colour = categorise(r["product"])
            seg.add_feature(
                s, e, 1 if r["strand"] == "+" else -1,
                plotstyle="bigarrow", facecolor=colour,
                edgecolor="black", lw=0.35,
                label=SHORT.get(r["product"], ""),
                text_kws=dict(size=7, rotation=45, vpos="top", hpos="center"),
            )

    # links between vertically adjacent tracks only
    for a, b in zip(ORDER, ORDER[1:]):
        sub = hits[(hits["qi"] == a) & (hits["ti"] == b)]
        best = sub.sort_values("bits", ascending=False).drop_duplicates("query")
        for _, r in best.iterrows():
            if r["qtag"] not in coords[a] or r["ttag"] not in coords[b]:
                continue
            s1, e1 = coords[a][r["qtag"]]
            s2, e2 = coords[b][r["ttag"]]
            # easy-search floor is 20% id; clamp so weak hits still draw
            ident = min(100.0, max(VMIN, float(r["fident"]) * 100))
            gv.add_link((track_name[a], s1, e1), (track_name[b], s2, e2),
                        color="#b0b0b0", v=ident, vmin=VMIN, vmax=100, alpha=0.75)

    gv.set_scale_bar(ymargin=1.2, labelsize=9)
    fig = gv.plotfig()

    handles = [Patch(fc=c, ec="black", lw=0.3, label=l) for l, c, _ in CATEGORIES]
    handles.append(Patch(fc=OTHER[1], ec="black", lw=0.3, label=OTHER[0]))
    fig.legend(handles=handles, loc="upper center", ncols=3, fontsize=10,
               frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle(
        "O-antigen (OSA) biosynthesis cassette — three ANI-distinct "
        "$\\it{Pseudomonas}$ strains\n"
        "same syntenic slot (ihfB → lpsA → MBL hydrolase), different cargo",
        fontsize=14, y=1.13)

    for ext in ("png", "svg"):
        fig.savefig(OUT / f"o_antigen_loci_comparison.{ext}",
                    dpi=300, bbox_inches="tight")
    print(f"wrote {OUT}/o_antigen_loci_comparison.png|svg")


if __name__ == "__main__":
    main()
