#!/usr/bin/env python
"""Spot intensities for the 2026-10-19 His-tag dot blot.

Reads the membrane photograph and reports, for each spotted position, how much
darker the membrane is inside the spot than the local background. No ladder and
no standard, so the numbers are relative to this one image only.

Grid positions were read off the photograph by eye and are hard-coded below;
the membrane was laid out 4 + 4 + 3 and row 3 is offset ~45 px left of rows 1-2.

Usage:  python quantify_dotblot.py
Writes: code/output/1019_dotblot/spot_intensities.tsv
"""
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

REPO = Path(__file__).resolve().parents[2]
IMG = REPO / "data/assays/1019_dotblot/dotblot.jpeg"
OUT = REPO / "code/output/1019_dotblot/spot_intensities.tsv"

RADIUS = 18          # px, spot sampling disc
BG_INNER, BG_OUTER = 26, 42   # px, local background annulus
SEARCH = 25          # px, allowed drift when re-centring a spot on the grid

# (label, x, y) in native image pixels
SPOTS = [
    # Centres read off the photograph at 4x zoom against a 20 px grid. Rows 1-2
    # share a column pitch of ~90 px and tilt ~16 px down to the right; row 3 was
    # spotted separately, with its own ~94 px pitch, and sits lower and further left.
    ("CDS12+ (rough lysate)",      322, 531),
    ("CDS12+",                     413, 537),
    ("e1+ (rough lysate, 10/18)",  503, 537),
    ("e1+",                        593, 547),
    ("e40+ (1:10)",                322, 628),
    ("e40+",                       413, 634),
    ("e281+ (1:10)",               503, 639),
    ("e281 FT1",                   585, 643),
    ("CDS12- (negative)",          261, 730),   # hollow drying ring
    ("e1+ (1:10)",                 355, 739),
    ("positive control",           449, 748),
]


def measure():
    """Return [(label, x, y, background, spot_lum, darkness, dx, dy), ...].

    Each spot re-centres on the darkest disc within SEARCH px of its nominal
    grid position before being measured; dx/dy record how far it moved. A spot
    that drifts to the full +/-SEARCH limit is one the search never found.
    """
    lum = np.asarray(Image.open(IMG).convert("RGB")).astype(float).mean(2)
    yy, xx = np.mgrid[: lum.shape[0], : lum.shape[1]]
    smooth = ndimage.gaussian_filter(lum, 6)

    rows = []
    for label, x0, y0 in SPOTS:
        win = smooth[y0 - SEARCH : y0 + SEARCH + 1, x0 - SEARCH : x0 + SEARCH + 1]
        dy, dx = np.unravel_index(np.argmin(win), win.shape)
        # Hitting the edge of the search box means no spot was found, only a
        # downhill gradient; re-centring on that would measure somewhere else
        # entirely, so fall back to the nominal grid position.
        if dx in (0, 2 * SEARCH) or dy in (0, 2 * SEARCH):
            dx = dy = SEARCH
        x, y = x0 - SEARCH + dx, y0 - SEARCH + dy
        d2 = (xx - x) ** 2 + (yy - y) ** 2
        spot = d2 <= RADIUS ** 2
        ring = (d2 > BG_INNER ** 2) & (d2 <= BG_OUTER ** 2)
        bg = np.median(lum[ring])
        rows.append((label, x, y, bg, lum[spot].mean(), bg - lum[spot].mean(),
                     x - x0, y - y0))
    return rows


def main() -> None:
    rows = measure()
    peak = max(r[5] for r in rows)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as fh:
        fh.write("label\tx\ty\tdx\tdy\tbackground_lum\tspot_lum\tdarkness\t"
                 "relative_to_max\n")
        for label, x, y, bg, sl, dk, dx, dy in rows:
            fh.write(f"{label}\t{x}\t{y}\t{dx}\t{dy}\t{bg:.1f}\t{sl:.1f}\t{dk:.2f}\t"
                     f"{dk / peak:.3f}\n")

    width = max(len(r[0]) for r in rows)
    print(f"{'spot'.ljust(width)}  darkness  rel")
    for label, _, _, _, _, dk, dx, dy in sorted(rows, key=lambda r: -r[5]):
        print(f"{label.ljust(width)}  {dk:7.2f}  {dk / peak:5.2f}   drift {dx:+3d},{dy:+3d}")
    print(f"\nwrote {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
