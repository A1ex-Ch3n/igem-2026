#!/usr/bin/env python3
"""Rasterise the PI's GH5 phylogenies for the wiki, and label the CDS_0012 mark.

The trees arrive from iTOL as ~2 MB SVGs, 1914x915, carrying about a thousand tip
labels. Inlining one into a page is not reasonable, and the thing the figure
exists to show -- where the modern enzyme sits among its homologues -- is a red
dash four pixels wide that nobody will find unaided. So each tree is rendered at
2x, cropped to its ink, and annotated with an arrow.

The red mark is located by colour rather than by hard-coded coordinates, so this
still works if the PI re-exports the tree at a different size.

Input  : documents/2026-10-20_prof_zymctrl/tree_{ultrametric,phylogram}.svg
Output : code/output/1020_zymctrl_figure/fig-gh5-tree-{...}.png
"""
from __future__ import annotations

from pathlib import Path

import cairosvg
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "documents/2026-10-20_prof_zymctrl"
OUT = ROOT / "code/output/1020_zymctrl_figure"

SCALE = 2.0
MARK = "#c0392b"


def find_red(img: Image.Image) -> tuple[int, int]:
    """Centre of iTOL's #ff0000 range marker -- the PI's CDS_0012 highlight."""
    a = np.array(img)
    red = (a[:, :, 0] > 180) & (a[:, :, 1] < 90) & (a[:, :, 2] < 90)
    ys, xs = np.nonzero(red)
    if not len(xs):
        raise SystemExit("no red marker found -- did the export lose the highlight?")
    return int(xs.mean()), int(ys.mean())


def render(stem: str) -> Path:
    svg = SRC / f"tree_{stem}.svg"
    png = OUT / f"fig-gh5-tree-{stem}.png"
    OUT.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(url=str(svg), write_to=str(png), scale=SCALE,
                     background_color="white")

    im = Image.open(png).convert("RGB")
    bbox = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).getbbox()
    im = im.crop(bbox)
    im.save(png)

    mx, my = find_red(im)
    img = mpimg.imread(png)
    h, w = img.shape[:2]
    fig = plt.figure(figsize=(w / 300, h / 300), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(img)
    ax.axis("off")
    ax.annotate("CDS_0012\n(the modern enzyme)",
                xy=(mx, my), xytext=(mx + w * 0.17, my + h * 0.11),
                fontsize=13, color=MARK, fontweight="bold", va="center",
                arrowprops=dict(arrowstyle="->", color=MARK, lw=2.0))
    fig.savefig(png, dpi=300)
    plt.close(fig)
    print(f"[ok] {png}  {w}x{h}  marker at ({mx},{my})")
    return png


def main() -> None:
    for stem in ("ultrametric", "phylogram"):
        render(stem)


if __name__ == "__main__":
    main()
