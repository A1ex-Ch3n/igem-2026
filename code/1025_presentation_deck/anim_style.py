"""Shared drawing style for every animation in the deck.

One module so the frames look like they came from the same hand: one palette,
one line weight, one way of drawing a membrane, a sugar chain, a phage, a
protein, an arrow and a label. Nothing in here is axis-aligned and perfectly
regular — chains lean and curve, bands have soft ends, corners are rounded —
because the stiff version read as a diagram rather than as a drawing.

Import it; don't restyle anything locally.
"""
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, PathPatch
from matplotlib.path import Path as MPath

matplotlib.rcParams["font.family"] = ["Avenir Next", "Avenir", "DejaVu Sans"]

ROOT = Path(__file__).resolve().parents[2]
OUTDIR = ROOT / "code/output/1025_presentation_deck"

# One palette, used everywhere.
INK = "#24383A"          # outlines and body text — never pure black
TEAL = "#2D6A6A"
RUST = "#B4542E"
MUTED = "#6B7674"
PURPLE = "#7B5EA7"
GOLD = "#C9A227"
MEMBRANE = "#93ABA8"
WALL = "#CBD7CF"
PAPER = "#FFFFFF"
HEAD = "#EDF1F0"

LW = 3.2                 # the one line weight for structure
LW_THIN = 2.0            # for detail inside a structure
GUTTER_X = 88            # drawings live left of this; labels live right of it


def canvas(w=13.0, h=6.0, xlim=(0, 124), ylim=(0, 52)):
    fig, ax = plt.subplots(figsize=(w, h), dpi=150)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    fig.patch.set_facecolor(PAPER)
    return fig, ax


def save(fig, name, sub=""):
    out = OUTDIR / sub if sub else OUTDIR
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{name}.png"
    fig.savefig(path, facecolor=PAPER, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
# primitives
# --------------------------------------------------------------------------- #

def soft_band(ax, x0, x1, y, thickness, colour, alpha=1.0, wobble=0.0, seed=0,
              z=1, caps=True):
    """A horizontal band, optionally rounded at the ends and gently undulating."""
    xs = np.linspace(x0, x1, 240)
    if wobble:
        rng = np.random.default_rng(seed)
        base = y + wobble * np.sin(xs / 11.0 + rng.uniform(0, 3))
    else:
        base = np.full_like(xs, float(y))
    ax.fill_between(xs, base, base + thickness, color=colour, alpha=alpha, lw=0,
                    zorder=z)
    if caps:
        for end in (x0, x1):
            ax.add_patch(plt.Circle((end, y + thickness / 2), thickness / 2,
                                    color=colour, alpha=alpha, lw=0, zorder=z))


def envelope_base(ax, x0=0, x1=88, y=0, z=1):
    """Outer membrane, wall, inner membrane — soft bands, not rectangles."""
    soft_band(ax, x0, x1, y + 0.0, 3.6, MEMBRANE, z=z, caps=False)
    soft_band(ax, x0, x1, y + 4.4, 2.4, WALL, z=z, caps=False)
    soft_band(ax, x0, x1, y + 7.6, 3.6, MEMBRANE, z=z, caps=False)
    return y + 11.2


def sugar_chain(ax, x, y0, length, colour=TEAL, lean=0.0, beads=4, seed=0, z=3):
    """A flexible chain: a leaning curve with beads along it, not a straight rule."""
    rng = np.random.default_rng(seed)
    sway = rng.uniform(-1.0, 1.0)
    t = np.linspace(0, 1, 60)
    xs = x + lean * t + sway * np.sin(t * math.pi) * 1.5
    ys = y0 + length * t
    ax.plot(xs, ys, color=colour, lw=LW, solid_capstyle="round", zorder=z)
    for k in range(1, beads + 1):
        f = k / beads
        bx = x + lean * f + sway * math.sin(f * math.pi) * 1.5
        ax.add_patch(plt.Circle((bx, y0 + length * f), 0.68, color=colour, lw=0,
                                zorder=z + 1))


def branched_chain(ax, x, y0, length, colour=PURPLE, seed=0, z=3):
    """A visibly different sugar: short, forked."""
    rng = np.random.default_rng(seed)
    lean = rng.uniform(-1.2, 1.2)
    t = np.linspace(0, 1, 40)
    xs = x + lean * t
    ys = y0 + length * t
    ax.plot(xs, ys, color=colour, lw=LW, solid_capstyle="round", zorder=z)
    tipx, tipy = x + lean, y0 + length
    for dx in (-2.4, 2.4):
        ax.plot([tipx, tipx + dx], [tipy, tipy + 2.7], color=colour, lw=LW_THIN + 0.6,
                solid_capstyle="round", zorder=z)
        ax.add_patch(plt.Circle((tipx + dx, tipy + 2.7), 0.62, color=colour, lw=0,
                                zorder=z + 1))


def sugar_layer(ax, y0, x0=4, x1=82, n=13, colour=TEAL, length=9.0, gap=None,
                branched=False, seed=4, z=3):
    """A field of chains, with an optional cleared gap at x = gap."""
    rng = np.random.default_rng(seed)
    for i, x in enumerate(np.linspace(x0, x1, n)):
        if gap is not None and abs(x - gap) < 7.5:
            continue
        lean = rng.uniform(-1.6, 1.6)
        jitter = rng.uniform(-1.0, 1.0)
        if branched:
            branched_chain(ax, x, y0, length + jitter, colour, seed=i, z=z)
        else:
            sugar_chain(ax, x, y0, length + jitter, colour, lean=lean, seed=i, z=z)


def capsule(ax, y, x0=0, x1=88, gap=None, colour=RUST, alpha=0.22, z=2):
    """A soft blanket lying over the chain tops — feathered, no hard edges."""
    spans = [(x0, x1)] if gap is None else [(x0, gap - 7.5), (gap + 7.5, x1)]
    for a, b in spans:
        if b - a < 1:
            continue
        for off, thick, al in ((-1.4, 4.4, alpha * 0.45),
                               (0.0, 3.2, alpha),
                               (1.0, 1.8, alpha * 0.8)):
            soft_band(ax, a, b, y + off, thick, colour, alpha=al, wobble=0.9,
                      seed=7, z=z, caps=False)


def rounded_poly(ax, pts, facecolor, edgecolor=INK, lw=LW, z=6):
    """A polygon whose corners are rounded by stroking it with a round join."""
    path = MPath(list(pts) + [pts[0]], closed=True)
    ax.add_patch(PathPatch(path, facecolor=facecolor, edgecolor=edgecolor, lw=lw,
                           joinstyle="round", capstyle="round", zorder=z))


def phage(ax, x, y, dna=0.0, z=6):
    """Head, collar and a tapered spike — rounded, with no pure black anywhere."""
    pts = [(x + 4.6 * math.cos(a), y + 4.6 * math.sin(a))
           for a in np.linspace(math.pi / 6, 2 * math.pi + math.pi / 6, 7)[:-1]]
    rounded_poly(ax, pts, HEAD, INK, LW, z=z)
    ax.plot([x, x], [y - 4.4, y - 8.4], color=INK, lw=LW + 0.6,
            solid_capstyle="round", zorder=z)
    t = np.linspace(0, 1, 40)
    half = 1.7 * (1 - t) ** 1.4 + 0.25
    ys = y - 8.4 - 6.0 * t
    ax.fill_betweenx(ys, x - half, x + half, color=INK, lw=0, zorder=z)
    ax.add_patch(plt.Circle((x, ys[-1]), 0.3, color=INK, lw=0, zorder=z))
    for k in range(4):
        f = (k + 1) / 5.5
        yy = y - 8.4 - 6.0 * f
        hw = 1.7 * (1 - f) ** 1.4 + 0.25
        ax.plot([x - hw * 0.8, x + hw * 0.8], [yy, yy], color="#8AA6A2",
                lw=1.2, solid_capstyle="round", zorder=z + 1)
    if dna > 0:
        ys = np.linspace(y - 14.6, y - 14.6 - dna, 80)
        ax.plot(x + 1.2 * np.sin(ys * 1.4), ys, color=GOLD, lw=LW - 0.6,
                solid_capstyle="round", zorder=z - 1)


def blob(ax, x, y, rx, ry, colour, seed=0, alpha=1.0, edge=None, z=4):
    """An organic rounded shape, for a protein or a cell, never a perfect oval."""
    rng = np.random.default_rng(seed)
    a = np.linspace(0, 2 * math.pi, 160)
    r = 1 + 0.07 * np.sin(3 * a + rng.uniform(0, 3)) + 0.05 * np.sin(5 * a)
    ax.fill(x + rx * r * np.cos(a), y + ry * r * np.sin(a), color=colour,
            alpha=alpha, lw=0, zorder=z)
    if edge:
        ax.plot(x + rx * r * np.cos(a), y + ry * r * np.sin(a), color=edge,
                lw=LW_THIN, zorder=z + 1)


def arrow(ax, x0, y0, x1, y1, colour=RUST, lw=2.2, curve=0.18, z=8):
    """A curved pointer — a straight line reads as a technical callout."""
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=17, lw=lw, color=colour,
                                 connectionstyle=f"arc3,rad={curve}",
                                 shrinkA=2, shrinkB=2, zorder=z))


def label(ax, x, y, body, colour=INK, ha="left", size=17, weight="normal"):
    ax.text(x, y, body, fontsize=size, color=colour, ha=ha, va="center",
            weight=weight, linespacing=1.45)


def tag(ax, x, y, body, colour=RUST, size=19):
    """A short verdict set on the drawing, underlined rather than boxed."""
    ax.text(x, y, body, fontsize=size, color=colour, ha="center", va="center",
            weight="bold")
    ax.plot([x - len(body) * size * 0.021, x + len(body) * size * 0.021],
            [y - 2.3, y - 2.3], color=colour, lw=2.6, solid_capstyle="round")
