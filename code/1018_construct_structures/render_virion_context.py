#!/usr/bin/env python3
"""CDS_0010, CDS_0011 and CDS_0012 in one picture — how the three parts relate.

There is no experimental or predicted structure of the three together, and we are
not able to fold a complex this size (CDS_0011 alone is a 941 aa trimer). So this
figure makes only the claims the data support:

* **Panel A is a real result.** CDS_0010 and CDS_0011 share the same N-terminal
  Calx-β anchor (42 % identity over 107 aa). Superposing the two anchors gives
  RMSD ~0.5 Å, so the two fibers really do carry the same virion-attachment
  module — they are paralogous fibers, not unrelated proteins.
* **Panel B is to scale, and its placement is an illustration.** One camera, so the
  relative sizes are true (tail spike trimer ~238 Å long, the two globular partners
  ~80-90 Å). CDS_0010 is positioned by superposing its anchor on the tail spike's
  and then stepping it sideways; that lateral spacing is drawn, not predicted, and
  no inter-protein contact is implied.

Outputs -> code/output/1018_construct_structures/
    panels/virion_shared_anchor.png, panels/virion_assembly.png
    fig_virion_context.{png,svg}
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pymol import cmd

from render_constructs import (C, FOLDS, OUT, PANELS, RAY, _crop_white, _hex2rgb,
                               BODY, CALX, FOLDON, GH5_BARREL, rng, setup, snap)

# lateral offsets used to separate the proteins in the illustration, in Angstrom
FIBER_SPACING = 130.0
GH5_OFFSET = 250.0
WIDE_RAY = (2600, 1200)   # panels B and C are wide scenes, not single proteins


def load_all() -> None:
    cmd.load(FOLDS / "fold_cds_0010/fold_cds_0010_model_0.cif", "m10")
    cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "t11")
    cmd.load(FOLDS / "fold_cds_0012/fold_cds_0012_model_0.cif", "m12")
    cmd.hide("everything")
    cmd.show("cartoon")


def colour_all() -> None:
    cmd.color("pg_unknown", "m10")
    cmd.color("pg_shaft", "t11")
    cmd.color("pg_body", rng("t11", *BODY))
    cmd.color("pg_foldon", rng("t11", *FOLDON))
    cmd.color("pg_calx", "m10 and resi 1-110")
    cmd.color("pg_calx", rng("t11", *CALX))
    cmd.color("pg_excluded", "m12")
    cmd.color("pg_barrel", rng("m12", *GH5_BARREL))


def panel_shared_anchor() -> tuple[Path, float, int]:
    """The one real structural claim: the two fibers share their anchor module."""
    setup()
    cmd.load(FOLDS / "fold_cds_0010/fold_cds_0010_model_0.cif", "m10")
    cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "t11")
    cmd.create("anchor10", "m10 and resi 1-110")
    cmd.create("anchor11", "t11 and chain A and resi 1-110")
    cmd.delete("m10")
    cmd.delete("t11")
    rms, n_atoms = cmd.super("anchor10", "anchor11")[:2]
    cmd.hide("everything")
    cmd.show("cartoon", "anchor10 or anchor11")
    cmd.set_color("anchor_a", _hex2rgb("#2980b9"))
    cmd.set_color("anchor_b", _hex2rgb("#e17055"))
    cmd.color("anchor_a", "anchor11")
    cmd.color("anchor_b", "anchor10")
    cmd.orient("anchor11")
    cmd.zoom("anchor11", 3)
    return snap("virion_shared_anchor"), float(rms), int(n_atoms)


def panel_assembly() -> Path:
    """Illustration: both fibers anchored in one plane, the GH5 free beside them."""
    setup()
    load_all()
    # stand the tail spike on its long axis, tip down
    cmd.orient("t11")
    cmd.turn("z", 90)
    # put CDS_0010's anchor where the tail spike's anchor is, then step it sideways
    cmd.super("m10 and resi 1-110", "t11 and chain A and resi 1-110", object="anchor_fit")
    cmd.delete("anchor_fit")
    cmd.translate([FIBER_SPACING, 0.0, 0.0], object="m10", camera=0)
    # the GH5 is not part of the virion — park it well clear of both fibers
    cmd.translate([GH5_OFFSET, 0.0, 0.0], object="m12", camera=0)
    colour_all()
    cmd.zoom("all", 2)
    path = PANELS / "virion_assembly.png"
    cmd.ray(*WIDE_RAY)
    cmd.png(str(path), dpi=300)
    _crop_white(path)
    return path


def assemble(anchor: Path, trio: Path, rms: float, n_atoms: int) -> None:
    fig = plt.figure(figsize=(17.5, 8.4))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.55])
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])

    ax_a.imshow(mpimg.imread(anchor))
    ax_a.set_title("A  The two fibers share one anchor — a real superposition",
                   fontsize=12.5, fontweight="bold", loc="left", pad=8)
    ax_a.set_xlabel(
        f"CDS_0010 res 1–110 (orange) on CDS_0011 chain A res 1–110 (blue).\n"
        f"RMSD {rms:.2f} Å over {n_atoms} atoms; 42 % sequence identity over 107 aa.\n"
        "Paralogous fibers carrying the same Calx-β virion-attachment module.",
        fontsize=9.5, loc="left")

    ax_b.imshow(mpimg.imread(trio))
    ax_b.set_title("B  The three proteins together, to scale",
                   fontsize=12.5, fontweight="bold", loc="left", pad=8)
    ax_b.set_xlabel(
        "One camera, so the relative sizes are true: the CDS_0011 tail-spike trimer is ≈ 238 Å\n"
        "long, CDS_0010 ≈ 88 Å and CDS_0012 ≈ 82 Å, and the spike is the only trimer of the three.\n"
        "CDS_0010 is positioned by superposing its anchor on the tail spike's, then stepping it\n"
        "sideways: that spacing is drawn, not predicted, and no contact between the proteins is\n"
        "implied. CDS_0012 is a free enzyme, not a virion component, so it is parked clear of\n"
        "both. There is no model of the assembled complex — none was predicted.",
        fontsize=9.5, loc="left")

    for ax in (ax_a, ax_b):
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    key = [
        Patch(facecolor=C["calx"], label="Calx-β anchor (res 1–110), shared"),
        Patch(facecolor=C["shaft"], label="CDS_0011 shaft (AF3 cannot place it)"),
        Patch(facecolor=C["body"], label="β-helix depolymerase body"),
        Patch(facecolor=C["foldon"], label="foldon tip"),
        Patch(facecolor=C["unknown"], label="CDS_0010, unknown function"),
        Patch(facecolor=C["barrel"], label="CDS_0012 GH5 TIM barrel"),
    ]
    fig.legend(handles=key, loc="lower center", ncol=6, frameon=False, fontsize=9)
    fig.suptitle("The three wild-type parts in context — 9-2-1 Φ8 tail proteins",
                 fontsize=14, fontweight="bold")
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig_virion_context.{ext}", dpi=220)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    anchor, rms, n_atoms = panel_shared_anchor()
    print(f"shared Calx-β anchor: RMSD {rms:.2f} Å over {n_atoms} atoms")
    trio = panel_assembly()
    assemble(anchor, trio, rms, n_atoms)
    print(f"wrote {OUT / 'fig_virion_context.png'}")


if __name__ == "__main__":
    main()
