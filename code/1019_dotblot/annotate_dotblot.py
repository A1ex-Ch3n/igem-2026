#!/usr/bin/env python
"""Annotated figure for the 2026-10-19 His-tag dot blot.

Panel A marks every spotted position on the membrane, whether or not anything
developed there. Panel B gives the measured intensity of each, with the negative
control drawn as the line a spot has to clear to be called.

Usage:  python code/1019_dotblot/annotate_dotblot.py
Writes: code/output/1019_dotblot/fig_dotblot_annotated.{png,pdf}
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from PIL import Image

from quantify_dotblot import IMG, SPOTS, measure

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "code/output/1019_dotblot"

INK, MUTED = "#222222", "#8a8a8a"
HIT, MISS = "#1b6ca8", "#c25b5b"      # clears the negative / does not

CROP = (208, 432, 700, 822)           # membrane bounding box, native px
SCALE = 2.5

# A spot is only called positive if it reaches this multiple of the negative
# control. CDS12+ lands at 1.03x, i.e. inside the noise, and is not a call.
POS_FACTOR = 2.0

# Two-line labels for panel A, kept short enough to sit between 85 px columns.
SHORT = {
    "CDS12+ (rough lysate)": "CDS12+\nrough",
    "CDS12+": "CDS12+",
    "e1+ (rough lysate, 10/18)": "e1+\nrough",
    "e1+": "e1+",
    "e40+ (1:10)": "e40+\n1:10",
    "e40+": "e40+",
    "e281+ (1:10)": "e281+\n1:10",
    "e281 FT1": "e281\nFT1",
    "CDS12- (negative)": "CDS12−\nneg.",
    "e1+ (1:10)": "e1+\n1:10",
    "positive control": "positive\ncontrol",
}


def main() -> None:
    rows = measure()
    by_label = {r[0]: r for r in rows}
    neg = by_label["CDS12- (negative)"][5]

    im = Image.open(IMG).convert("RGB").crop(CROP)
    im = im.resize((int(im.width * SCALE), int(im.height * SCALE)), Image.LANCZOS)

    fig = plt.figure(figsize=(12.4, 5.4))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.12, 1], wspace=0.22)
    a = fig.add_subplot(gs[0, 0])
    b = fig.add_subplot(gs[0, 1])

    # ---- Panel A: the membrane, every spotted position marked ----------------
    a.imshow(np.asarray(im))
    a.set_xticks([])
    a.set_yticks([])
    for side in a.spines.values():
        side.set_edgecolor("#d0d0d0")

    for label, x0, y0 in SPOTS:
        cx, cy = (x0 - CROP[0]) * SCALE, (y0 - CROP[1]) * SCALE
        dk = by_label[label][5]
        clears = dk >= POS_FACTOR * neg and label != "CDS12- (negative)"
        colour = HIT if clears else MUTED
        if label == "positive control":
            colour = INK
        if label == "CDS12- (negative)":
            colour = MISS          # the hollow drying ring, same role as panel B's line
        radius = 26 * SCALE / 2.5 * 1.7
        a.add_patch(
            Circle((cx, cy), radius,
                   fill=False, lw=2.0 if clears else 1.2,
                   ls="-" if clears else (0, (3, 2)), edgecolor=colour)
        )
        # clear the circle itself, or the label lands on top of the spot
        offset = radius + 15
        above = label not in ("CDS12- (negative)", "e1+ (1:10)", "positive control")
        a.annotate(
            SHORT[label],
            (cx, cy - offset if above else cy + offset),
            ha="center", va="bottom" if above else "top",
            fontsize=7.4, color=colour,
            linespacing=1.15,
            weight="bold" if clears or label in ("positive control",
                                                 "CDS12- (negative)") else "normal",
        )

    a.annotate("cut corner",
               ((300 - CROP[0]) * SCALE, (443 - CROP[1]) * SCALE),
               xytext=((390 - CROP[0]) * SCALE, (470 - CROP[1]) * SCALE),
               fontsize=7.5, color=MUTED,
               arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9))
    a.annotate("run-off from the\npositive control",
               ((545 - CROP[0]) * SCALE, (700 - CROP[1]) * SCALE),
               xytext=((635 - CROP[0]) * SCALE, (793 - CROP[1]) * SCALE),
               fontsize=7.5, color=MUTED, linespacing=1.2, ha="center", va="top",
               arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9))

    # ---- Panel B: measured intensity ----------------------------------------
    order = sorted(rows, key=lambda r: r[5])
    ys = np.arange(len(order))
    for y, r in zip(ys, order):
        label, dk = r[0], r[5]
        is_neg = label == "CDS12- (negative)"
        clears = dk >= POS_FACTOR * neg and not is_neg
        colour = INK if label == "positive control" else (HIT if clears else MUTED)
        b.barh(y, dk, height=0.62, color=colour,
               alpha=1.0 if (clears or label == "positive control") else 0.45)
        b.text(dk + 1.1, y, f"{dk:.1f}", va="center", fontsize=8.5,
               color=colour, weight="bold" if clears else "normal", zorder=4,
               bbox=dict(facecolor="white", edgecolor="none", pad=0.9, alpha=0.85))

    b.axvline(neg, color=MISS, lw=1.4, ls="--", zorder=0)
    b.axvline(POS_FACTOR * neg, color=MUTED, lw=1.1, ls=":", zorder=0)
    # staggered so the two lines, only ~4 units apart, do not collide
    b.text(neg, len(order) - 0.30, "negative control", fontsize=7.8, color=MISS,
           ha="center", va="bottom")
    b.text(POS_FACTOR * neg, len(order) + 0.42,
           f"{POS_FACTOR:g}x = call threshold", fontsize=7.8, color=MUTED,
           ha="center", va="bottom")

    b.set_yticks(ys)
    b.set_yticklabels([r[0] for r in order], fontsize=9)
    b.set_xlabel("darkness vs. local background (relative units, this image only)",
                 fontsize=9.5)
    b.set_xlim(0, max(r[5] for r in rows) * 1.16)
    b.set_ylim(-0.7, len(order) + 1.5)
    b.grid(axis="x", color="#f0f0f0", lw=0.9)
    b.set_axisbelow(True)
    for side in ("top", "right", "left"):
        b.spines[side].set_visible(False)
    b.tick_params(axis="y", length=0)

    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "fig_dotblot_annotated.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / "fig_dotblot_annotated.pdf", bbox_inches="tight")
    print(f"wrote {(OUT / 'fig_dotblot_annotated.png').relative_to(REPO)}")
    print(f"wrote {(OUT / 'fig_dotblot_annotated.pdf').relative_to(REPO)}")


if __name__ == "__main__":
    main()
