#!/usr/bin/env python3
"""
Q4 -- genome map of phage 9-2-1 Phi8, structural proteins highlighted.

Drawn from Prof. Espinoza's Pharokka run on the canonical `Version_1` assembly
(62,416 bp, UUAIURNK_ numbering).  This matters: the earlier figure in
code/output/0708_phage_genome_analysis/ was drawn on our reverse-complemented +
rotated 62,338 bp frame with the deprecated FHABPWTM_ numbers, so its module
order is MIRRORED.  Do not reuse that one.

Two outputs:
  fig_phage_genome_map.{png,svg}   whole genome, 80 CDS, key genes labelled
  fig_phage_tail_module.{png,svg}  zoom on the tail / RBP cluster

Genes are coloured with Pharokka's own PHROG category colours so the figure is
readable next to standard Pharokka output.  Two labels come from OUR work, not
from Pharokka, and are marked with a dagger in the figure:
  CDS_0012 -- Pharokka says "hypothetical"; AF3 templates say GH5 TIM barrel
  CDS_0024 -- Pharokka says "hypothetical"; RBP Detect + fold say depolymerase
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from matplotlib.patches import Patch
from pygenomeviz import GenomeViz

ROOT = Path(__file__).resolve().parents[2]
TSV = ROOT / ("code/0713_espinoza_structural_mapping/pharokka_espinoza/"
              "pharokka_cds_final_merged_output.tsv")
OUT = ROOT / "code/output/0729_prof_figures"

GENOME_LEN = 62_416           # Version_1, PI assembly
TAIL_ZOOM = (11_500, 21_200)  # CDS_0008 .. CDS_0012, whole genes

# our own calls, layered on top of Pharokka's annotation
OURS = {
    "CDS_0012": "GH5 glycoside hydrolase†",
    "CDS_0024": "β-helix depolymerase†",
}

# genes worth naming on the whole-genome panel
LABEL = {
    "CDS_0001": "DarB-like antirestriction",
    "CDS_0008": "internal virion protein",
    "CDS_0009": "tail fiber",
    "CDS_0010": "tail protein",
    "CDS_0011": "TAIL SPIKE",
    "CDS_0012": OURS["CDS_0012"],
    "CDS_0017": "major head",
    "CDS_0020": "portal",
    "CDS_0024": OURS["CDS_0024"],
    "CDS_0027": "terminase small subunit",
    "CDS_0047": "helicase loader",
    "CDS_0061": "RecE-like exonuclease",
    "CDS_0070": "excisionase",
    "CDS_0075": "Rz-like spanin",
    "CDS_0078": "endolysin",
}

STAR = "CDS_0011"  # the one the PI asked to highlight


def load() -> pd.DataFrame:
    df = pd.read_csv(TSV, sep="\t", dtype=str)
    df["cds"] = df["gene"].str.replace("UUAIURNK_", "", regex=False)
    df["s"] = df[["start", "stop"]].astype(int).min(axis=1)
    df["e"] = df[["start", "stop"]].astype(int).max(axis=1)
    df["strand_i"] = df["strand"].map({"+": 1, "-": -1})
    return df.sort_values("s").reset_index(drop=True)


def category_colors(df: pd.DataFrame) -> dict[str, str]:
    """Pharokka ships one colour per PHROG category -- reuse it."""
    return (df.groupby("category")["color"]
              .agg(lambda s: s.value_counts().index[0]).to_dict())


def draw(df: pd.DataFrame, rng: tuple[int, int], track_label: str,
         labels: dict[str, str], fig_w: float, label_size: float,
         out_stem: str, title: str, subtitle: str, title_pad: float) -> None:
    colors = category_colors(df)
    start, end = rng
    sub = df[(df["e"] > start) & (df["s"] < end)]

    gv = GenomeViz(fig_track_height=1.5, feature_track_ratio=0.5,
                   track_align_type="left")
    track = gv.add_feature_track(track_label, (start, end), labelsize=0)
    seg = track.get_segment()

    for _, r in sub.iterrows():
        is_star = r["cds"] == STAR
        # a gene straddling the window edge would raise FeatureRangeError
        s, e = max(int(r["s"]), start), min(int(r["e"]), end)
        seg.add_feature(
            s, e, r["strand_i"],
            plotstyle="bigarrow",
            facecolor=colors.get(r["category"], "#bdc3c7"),
            edgecolor="#c0392b" if is_star else "black",
            lw=2.2 if is_star else 0.4,
            label=labels.get(r["cds"], ""),
            text_kws=dict(size=label_size + (1.5 if is_star else 0),
                          rotation=40, vpos="top", hpos="left",
                          color="#c0392b" if is_star else "black",
                          weight="bold" if is_star else "normal"),
        )

    gv.set_scale_bar(ymargin=0.8, labelsize=9)
    fig = gv.plotfig()
    fig.set_size_inches(fig_w, fig.get_size_inches()[1])

    order = ["tail", "head and packaging", "lysis", "integration and excision",
             "DNA, RNA and nucleotide metabolism", "transcription regulation",
             "moron, auxiliary metabolic gene and host takeover", "other",
             "unknown function"]
    shown = set(sub["category"])  # only legend what is actually in this window
    handles = [Patch(fc=colors[c], ec="black", lw=0.3, label=c)
               for c in order if c in colors and c in shown]
    fig.legend(handles=handles, loc="upper center", ncols=3, fontsize=9,
               frameon=False, bbox_to_anchor=(0.5, 0.0), title="PHROG category",
               title_fontsize=9)
    # A suptitle is positioned in *figure* fractions, but bbox_inches="tight"
    # expands the canvas upward to fit the rotated gene labels -- which drops
    # the suptitle in among them.  Anchor to the track axes instead.
    track.ax.set_title(title + "\n" + subtitle, fontsize=13, pad=title_pad)

    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{out_stem}.{ext}", dpi=300, bbox_inches="tight")
    print(f"wrote {out_stem}.png|svg  ({len(sub)} CDS)")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = load()

    draw(df, (0, GENOME_LEN),
         "9-2-1 Φ8", LABEL, 19.0, 7.5,
         "fig_phage_genome_map",
         "Bacteriophage 9-2-1 Φ8 — 62,416 bp, linear with 77 bp DTR, 80 CDS",
         "canonical Version_1 orientation, Prof. Espinoza's UUAIURNK_ numbering"
         "  ·  † = our assignment, not Pharokka's",
         title_pad=150)

    zoom_labels = {c: LABEL.get(c, "") for c in
                   ["CDS_0008", "CDS_0009", "CDS_0010", "CDS_0011", "CDS_0012"]}
    zoom_labels["CDS_0011"] = "TAIL SPIKE  (941 aa, β-helix depolymerase)"
    zoom_labels["CDS_0010"] = "tail protein (917 aa, paralogous Calx-β anchor)"
    draw(df, TAIL_ZOOM,
         "tail module", zoom_labels, 13.0, 9.0,
         "fig_phage_tail_module",
         "Tail / RBP cluster of 9-2-1 Φ8",
         "the receptor-binding module the PI is cloning  ·  "
         "† = our assignment, not Pharokka's",
         title_pad=190)


if __name__ == "__main__":
    main()
