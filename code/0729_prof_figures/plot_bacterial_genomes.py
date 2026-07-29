#!/usr/bin/env python3
"""
Q3 -- diagram of the bacterial genomes we sequenced.

Five isolates were sequenced but they collapse to three ANI-distinct strains
(code/0627_unique_strain_table.ipynb), so the figure shows one circular map per
STRAIN, not per isolate -- drawing 9-2-1 and 9-6-2 separately would be drawing
the same genome twice (they are 100.000% ANI).

CDS counts are read from Bakta's own summary .txt, not by counting CDS features
in the .gbff: Bakta writes its 4 sORFs as CDS features but reports them
separately, so a naive feature count reads 4 high and would not match the MRA.

Each map: CDS by strand, GC content, GC skew, Mb ticks, and the O-antigen
cassette from code/0727_o_antigen_comparison/ marked in red -- which is what
ties this figure to the Q7 result (same slot, different cargo in each strain).

Outputs -> code/output/0729_prof_figures/
    fig_bacterial_genomes.{png,svg}   assembled 3-panel figure + stats
    panels/circos_*.png               individual circular maps
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from pycirclize import Circos
from pycirclize.parser import Genbank

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/0729_prof_figures"
PANELS = OUT / "panels"
BOUNDS = ROOT / "code/output/0727_o_antigen_comparison/locus_bounds.tsv"

# one representative per ANI-distinct strain
REPS = [
    ("Strain 1", "8-5-2", "data/bacteria_genome/8-5-2",
     "$\\it{Pseudomonas\\_E}$ sp013179515", "also: 10-10-2 (99.997% ANI)"),
    ("Strain 2", "9-2-1", "data/bacteria_genome/9-2-1",
     "$\\it{Pseudomonas\\_E}$ sp013179515", "also: 9-6-2 (100.000% ANI)  ·  phage host"),
    ("Strain 3", "8-10-2", "data/bacteria_genome/8-10-2",
     "$\\it{P.\\ capeferrum}$", "87.4–87.7% ANI to the others"),
]

C_FWD, C_REV = "#2c7fb8", "#7fcdbb"
C_GC, C_SKEW_P, C_SKEW_N = "#34495e", "#27ae60", "#8e44ad"
C_OAG = "#c0392b"


def circular_map(gbff: Path, title: str, oag: tuple[int, int] | None) -> Path:
    gbk = Genbank(gbff)
    circos = Circos(sectors={gbk.name: gbk.range_size})
    sector = circos.sectors[0]

    # --- O-antigen cassette, outermost so it reads as an annotation ---
    if oag:
        hl = sector.add_track((97, 100))
        hl.axis(fc="none", ec="none")
        hl.rect(oag[0], oag[1], fc=C_OAG, ec=C_OAG, lw=1.2)

    # --- CDS by strand ---
    f_track = sector.add_track((88, 96), r_pad_ratio=0.02)
    f_track.axis(fc="#fafafa", ec="none")
    f_track.genomic_features(gbk.extract_features("CDS", target_strand=1),
                             plotstyle="arrow", fc=C_FWD, lw=0.05)
    r_track = sector.add_track((79, 87), r_pad_ratio=0.02)
    r_track.axis(fc="#fafafa", ec="none")
    r_track.genomic_features(gbk.extract_features("CDS", target_strand=-1),
                             plotstyle="arrow", fc=C_REV, lw=0.05)

    # --- GC content (deviation from genome mean) ---
    pos, gc = gbk.calc_gc_content(window_size=10000, step_size=5000)
    gc = gc - gbk.calc_genome_gc_content()
    gc_track = sector.add_track((62, 77))
    gc_track.axis(fc="none", ec="#dddddd")
    # values straddle zero, so the symmetric range has to be given explicitly
    gc_lim = float(abs(gc).max())
    gc_track.fill_between(pos, gc, 0, vmin=-gc_lim, vmax=gc_lim, fc=C_GC, lw=0.1)

    # --- GC skew ---
    pos, skew = gbk.calc_gc_skew(window_size=10000, step_size=5000)
    sk_track = sector.add_track((45, 60))
    sk_track.axis(fc="none", ec="#dddddd")
    sk_lim = float(abs(skew).max())
    # `where=` is applied after pycirclize interpolates to a finer grid, so the
    # mask length no longer matches -- clip into two series instead.
    sk_track.fill_between(pos, np.clip(skew, 0, None), 0,
                          vmin=-sk_lim, vmax=sk_lim, fc=C_SKEW_P, lw=0.1)
    sk_track.fill_between(pos, np.clip(skew, None, 0), 0,
                          vmin=-sk_lim, vmax=sk_lim, fc=C_SKEW_N, lw=0.1)

    # --- Mb ticks ---
    f_track.xticks_by_interval(
        1_000_000, outer=True, show_label=True, label_size=7,
        label_formatter=lambda v: f"{v / 1e6:.0f} Mb")

    fig = circos.plotfig(figsize=(6, 6))
    p = PANELS / f"circos_{title}.png"
    fig.savefig(p, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return p


def _bakta_cds_count(summary_txt: Path) -> int:
    """Bakta's reported CDS count (excludes sORFs, which it writes as CDS)."""
    for line in summary_txt.read_text().splitlines():
        if line.strip().lower().startswith("cdss:"):
            return int(line.split(":")[1])
    raise SystemExit(f"no CDSs line in {summary_txt}")


def main() -> None:
    PANELS.mkdir(parents=True, exist_ok=True)
    bounds = pd.read_csv(BOUNDS, sep="\t").set_index("isolate")

    panels, stats = [], []
    for strain, iso, rel, species, note in REPS:
        ann = ROOT / rel / "annotation"
        gbff = next(ann.glob("*_reference.gbff"))
        gbk = Genbank(gbff)
        n_cds = _bakta_cds_count(next(ann.glob("*_reference.txt")))
        oag = (int(bounds.loc[iso, "start_bp"]), int(bounds.loc[iso, "end_bp"]))
        panels.append(circular_map(gbff, iso, oag))
        stats.append({
            "strain": strain, "isolate": iso, "species": species, "note": note,
            "length": gbk.range_size, "gc": gbk.calc_genome_gc_content(),
            "cds": n_cds, "oag_kb": (oag[1] - oag[0]) / 1000,
            "oag_genes": int(bounds.loc[iso, "n_genes"]),
        })
        print(f"  {iso}: {gbk.range_size:,} bp, {n_cds} CDS, "
              f"GC {gbk.calc_genome_gc_content():.1f}%")

    fig, axes = plt.subplots(1, 3, figsize=(16.5, 6.6))
    for ax, p, s in zip(axes, panels, stats):
        ax.imshow(mpimg.imread(p))
        ax.axis("off")
        ax.set_title(f"{s['strain']} — {s['isolate']}",
                     fontsize=13, fontweight="bold", pad=26)
        ax.text(0.5, 1.005, s["species"], transform=ax.transAxes,
                ha="center", va="bottom", fontsize=11.5)
        ax.text(0.5, -0.02,
                f"{s['length']:,} bp  ·  GC {s['gc']:.1f}%  ·  {s['cds']:,} CDS\n"
                f"{s['note']}\n"
                f"O-antigen cassette: {s['oag_genes']} genes / {s['oag_kb']:.1f} kb",
                transform=ax.transAxes, ha="center", va="top",
                fontsize=9.2, color="#444", linespacing=1.5)

    handles = [
        Patch(fc=C_FWD, label="CDS, forward strand"),
        Patch(fc=C_REV, label="CDS, reverse strand"),
        Patch(fc=C_GC, label="GC content (deviation from mean)"),
        Patch(fc=C_SKEW_P, label="GC skew +"),
        Patch(fc=C_SKEW_N, label="GC skew −"),
        Patch(fc=C_OAG, label="O-antigen cassette (see Q7)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncols=6, fontsize=9.5,
               frameon=False, bbox_to_anchor=(0.5, -0.10))
    fig.suptitle(
        "Complete closed genomes of three ANI-distinct soil $\\it{Pseudomonas}$ strains\n"
        "five isolates sequenced (ONT + Autocycler, single circular contig each) "
        "→ three strains; CheckM completeness 99.74–100%",
        fontsize=14, y=1.06)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig_bacterial_genomes.{ext}", dpi=200,
                    bbox_inches="tight")
    print("wrote fig_bacterial_genomes.png|svg")


if __name__ == "__main__":
    main()
