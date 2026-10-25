"""Frame sequence: how a phage gets through the sugar, and where host range is decided.

Picture first. Each frame carries only short labels on the drawing itself; the
prose that summarises the mechanism belongs on a slide of its own, after the
build has run. Paging through the frames reads as motion.

    python code/1025_presentation_deck/anim_adsorption.py
"""
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle

matplotlib.rcParams["font.family"] = ["Avenir Next", "Avenir", "DejaVu Sans"]

OUT = Path(
    "/private/tmp/claude-501/-Users-alexy-Desktop-iGEM-26/"
    "77c93b6d-bdc5-452e-8971-b54893d1cd43/scratchpad/anim/adsorption"
)

DARK = "#1C2B2B"
TEAL = "#2D6A6A"
RUST = "#B4542E"
MUTED = "#55605F"
PURPLE = "#7B5EA7"
MEMBRANE = "#8FA7A4"
WALL = "#C2CFC6"

W, H = 13.0, 6.0
CHAIN_N = 15


def canvas():
    fig, ax = plt.subplots(figsize=(W, H), dpi=150)
    ax.set_xlim(0, 124)
    ax.set_ylim(0, 52)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    return fig, ax


def base(ax):
    ax.add_patch(Rectangle((0, 0), 86, 4, color=MEMBRANE, lw=0))
    ax.add_patch(Rectangle((0, 4.4), 86, 2.6, color=WALL, lw=0))
    ax.add_patch(Rectangle((0, 7.4), 86, 4, color=MEMBRANE, lw=0))


def envelope(ax, cut_at=None, capsule=True):
    """The cell surface. cut_at: x of a channel digested through the sugar."""
    base(ax)
    rng = np.random.default_rng(4)
    for x in np.linspace(4, 82, CHAIN_N):
        if cut_at is not None and abs(x - cut_at) < 7.5:
            continue
        top = 20.4 + rng.uniform(-1.3, 1.3)
        ax.plot([x, x], [11.4, top], color=TEAL, lw=3.4, solid_capstyle="round")
        for k in range(4):
            ax.add_patch(plt.Circle((x, 11.4 + (top - 11.4) * (k + 1) / 4), 0.62,
                                    color=TEAL, zorder=3))
    if capsule:
        band = np.linspace(0, 86, 300)
        if cut_at is None:
            lo = 21.6 + 1.1 * np.sin(band / 9.0)
            ax.fill_between(band, lo, lo + 4.0, color=RUST, alpha=0.30, lw=0)
        else:
            for part in (band[band < cut_at - 7.5], band[band > cut_at + 7.5]):
                if len(part) > 1:
                    lo = 21.6 + 1.1 * np.sin(part / 9.0)
                    ax.fill_between(part, lo, lo + 4.0, color=RUST, alpha=0.30, lw=0)


def phage(ax, x, y, dna=0.0):
    """Head, tail and beta-helix spike, with (x, y) the centre of the head."""
    ax.add_patch(Polygon(
        [(x + 4.4 * math.cos(a), y + 4.4 * math.sin(a))
         for a in np.linspace(math.pi / 6, 2 * math.pi + math.pi / 6, 7)[:-1]],
        closed=True, facecolor="#E8EDEB", edgecolor=DARK, lw=2.4, zorder=6))
    ax.plot([x, x], [y - 4.4, y - 8.6], color=DARK, lw=3.6, zorder=6)
    ax.add_patch(Polygon([(x - 1.5, y - 8.6), (x + 1.5, y - 8.6), (x, y - 14.6)],
                         closed=True, facecolor=DARK, edgecolor="none", zorder=6))
    for k in range(5):
        yy = y - 9.3 - k * 1.05
        ax.plot([x - 1.25 + k * 0.19, x + 1.25 - k * 0.19], [yy, yy],
                color="#7E9C98", lw=1.3, zorder=7)
    if dna > 0:
        ys = np.linspace(y - 14.4, y - 14.4 - dna, 60)
        ax.plot(x + 1.1 * np.sin(ys * 1.5), ys, color="#C9A227", lw=2.4, zorder=5)


def note(ax, x, y, body, colour=DARK, ha="left", size=17):
    ax.text(x, y, body, fontsize=size, color=colour, ha=ha, va="center")


def arrow(ax, x0, y0, x1, y1, colour=RUST, lw=2.4):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=lw,
                                shrinkA=0, shrinkB=0))


def frames():
    OUT.mkdir(parents=True, exist_ok=True)
    steps = []

    fig, ax = canvas()
    envelope(ax)
    note(ax, 2, 24.5, "capsule", RUST)
    note(ax, 2, 16, "O-antigen", TEAL)
    note(ax, 2, 5.6, "membrane", MUTED)
    steps.append(("01-surface", fig))

    fig, ax = canvas()
    envelope(ax)
    phage(ax, 43, 47)
    steps.append(("02-arrive", fig))

    fig, ax = canvas()
    envelope(ax)
    phage(ax, 43, 42)
    arrow(ax, 89, 31, 50, 28)
    note(ax, 90, 31, "the spike meets sugar,\nnot a protein", RUST)
    steps.append(("03-contact", fig))

    fig, ax = canvas()
    envelope(ax, cut_at=43)
    phage(ax, 43, 34)
    arrow(ax, 89, 18, 50, 15)
    note(ax, 90, 18, "it is an enzyme —\nit digests a channel", TEAL)
    steps.append(("04-cut", fig))

    fig, ax = canvas()
    envelope(ax, cut_at=43)
    phage(ax, 43, 26)
    arrow(ax, 89, 12, 50, 11, colour=TEAL)
    note(ax, 90, 12, "now it reaches\nthe membrane", TEAL)
    steps.append(("05-reach", fig))

    fig, ax = canvas()
    envelope(ax, cut_at=43)
    phage(ax, 43, 26, dna=9)
    arrow(ax, 89, 8, 50, 6, colour=DARK)
    note(ax, 90, 8, "and injects", DARK)
    steps.append(("06-inject", fig))

    fig, ax = canvas()
    base(ax)
    rng = np.random.default_rng(11)
    for x in np.linspace(4, 82, CHAIN_N):
        top = 17.8 + rng.uniform(-0.7, 0.7)
        ax.plot([x, x], [11.4, top], color=PURPLE, lw=3.4, solid_capstyle="round")
        ax.plot([x, x - 2.2], [top, top + 2.6], color=PURPLE, lw=3.0,
                solid_capstyle="round")
        ax.plot([x, x + 2.2], [top, top + 2.6], color=PURPLE, lw=3.0,
                solid_capstyle="round")
    phage(ax, 43, 42)
    ax.plot([35.5, 50.5], [25.4, 25.4], color=RUST, lw=3.4)
    note(ax, 43, 29, "no cut", RUST, ha="center", size=23)
    arrow(ax, 89, 18, 56, 19)
    note(ax, 90, 18, "a sugar this enzyme\ncannot digest", RUST)
    steps.append(("07-other-strain", fig))

    for name, fig in steps:
        path = OUT / f"{name}.png"
        fig.savefig(path, facecolor="white", bbox_inches="tight", pad_inches=0.08)
        plt.close(fig)
        print(path.name)
    return len(steps)


if __name__ == "__main__":
    print(f"{frames()} frames -> {OUT}")
