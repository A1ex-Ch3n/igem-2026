"""Animations for the computational side: the cycle wheel, why an interface score
carries no signal, the screen and its control gate, and the rung-period fold test.

    python code/1025_presentation_deck/anim_method.py
"""
import math

import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch

from anim_style import (GOLD, HEAD, INK, LW, LW_THIN, MUTED, PURPLE, RUST, TEAL,
                        WALL, arrow, blob, canvas, label, save, tag)

STEPS = ("Design", "Build", "Test", "Learn")
CYCLES = ("The wrong question", "Ask the protein what it is",
          "Build the enzymes", "Let the bacteria answer")


# --------------------------------------------------------------------------- #
# the loop itself — the spine that returns at every act
# --------------------------------------------------------------------------- #

def wheel(ax, cx, cy, r, active=None, colour=TEAL, dim="#D6DEDC"):
    """Four arcs around a ring, one of them lit."""
    for i, name in enumerate(STEPS):
        a0, a1 = 90 - i * 90 - 78, 90 - i * 90 - 12
        on = (active == i)
        ax.add_patch(Arc((cx, cy), 2 * r, 2 * r, theta1=a0, theta2=a1,
                         lw=11 if on else 8, color=colour if on else dim,
                         capstyle="round", zorder=3))
        mid = math.radians((a0 + a1) / 2)
        ax.text(cx + (r + 6.0) * math.cos(mid), cy + (r + 6.0) * math.sin(mid),
                name, fontsize=16, ha="center", va="center",
                color=INK if on else MUTED, weight="bold" if on else "normal")
    for i in range(4):
        a = math.radians(90 - i * 90 - 95)
        ax.add_patch(FancyArrowPatch(
            (cx + r * math.cos(a + 0.18), cy + r * math.sin(a + 0.18)),
            (cx + r * math.cos(a - 0.04), cy + r * math.sin(a - 0.04)),
            arrowstyle="-|>", mutation_scale=15, color=dim, lw=0, zorder=2))


def cycle_wheels():
    made = []
    for i in range(4):
        fig, ax = canvas(xlim=(0, 124), ylim=(0, 52))
        wheel(ax, 30, 26, 15, active=None)
        for k in range(4):
            wheel(ax, 30, 26, 15, active=k if k == i else None)
        ax.text(30, 28.5, f"Cycle {i + 1}", fontsize=27, ha="center", va="center",
                color=INK, weight="bold")
        ax.text(30, 22.5, "of four", fontsize=16, ha="center", va="center",
                color=MUTED)
        label(ax, 60, 30, CYCLES[i], TEAL, size=26, weight="bold")
        label(ax, 60, 23.5, "Design · Build · Test · Learn", MUTED, size=17)
        made.append((f"{i + 1:02d}-cycle", fig))
    for name, fig in made:
        print(save(fig, name, "wheel").name)
    return len(made)


# --------------------------------------------------------------------------- #
# why an interface score carries no signal
# --------------------------------------------------------------------------- #

def _pair(ax, x, y, s=1.0, hit=None, z=4):
    """Two protein blobs facing each other; hit marks a co-varying residue pair."""
    blob(ax, x - 4.4 * s, y, 3.4 * s, 2.6 * s, "#BBD3CF", seed=3, edge=TEAL, z=z)
    blob(ax, x + 4.4 * s, y, 3.4 * s, 2.6 * s, "#E3CDBE", seed=8, edge=RUST, z=z)
    if hit:
        ax.add_patch(ax.scatter([x - 1.4 * s], [y], s=46 * s, color=TEAL,
                                zorder=z + 1).get_paths() and
                     __import__("matplotlib.patches", fromlist=["Circle"]).Circle(
                         (x - 1.4 * s, y), 0.55 * s, color=GOLD, zorder=z + 2))
        ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle(
            (x + 1.4 * s, y), 0.55 * s, color=GOLD, zorder=z + 2))


def interface_noise():
    made = []

    # 1 — the question
    fig, ax = canvas()
    _pair(ax, 42, 30, s=1.7)
    label(ax, 42, 14, "do these two touch?", INK, ha="center", size=22)
    made.append(("01-question", fig))

    # 2 — the model does not simulate; it reads other species
    fig, ax = canvas()
    _pair(ax, 42, 42, s=1.0)
    for r in range(4):
        y = 31 - r * 7.4
        _pair(ax, 42, y, s=0.72)
        label(ax, 10, y, f"species {r + 2}", MUTED, size=14)
    label(ax, 10, 42, "species 1", MUTED, size=14)
    label(ax, 90, 30, "the model looks\nacross thousands\nof species", INK)
    made.append(("02-species", fig))

    # 3 — residues that change in step
    fig, ax = canvas()
    for r in range(5):
        y = 42 - r * 7.4
        _pair(ax, 42, y, s=0.72 if r else 1.0, hit=True)
    arrow(ax, 88, 26, 50, 25, colour=GOLD, curve=0.2)
    label(ax, 90, 26, "when this residue changes,\nthat one changes to match", INK)
    made.append(("03-covary", fig))

    # 4 — that pattern is the fingerprint of contact
    fig, ax = canvas()
    for r in range(5):
        _pair(ax, 42, 42 - r * 7.4, s=0.72 if r else 1.0, hit=True)
    tag(ax, 42, 2.5, "that pattern is the fingerprint of contact", TEAL, size=20)
    made.append(("04-fingerprint", fig))

    # 5 — but a phage and a bacterium never share a genome
    fig, ax = canvas()
    label(ax, 24, 47, "phage genomes", TEAL, ha="center", size=17, weight="bold")
    label(ax, 62, 47, "bacterial genomes", RUST, ha="center", size=17, weight="bold")
    for r in range(5):
        y = 40 - r * 7.6
        blob(ax, 24, y, 3.2, 2.4, "#BBD3CF", seed=r, edge=TEAL, z=4)
        blob(ax, 62, y, 3.2, 2.4, "#E3CDBE", seed=r + 9, edge=RUST, z=4)
        ax.plot([32, 54], [y, y], color="#E2E6E4", lw=2.4, ls=(0, (2, 4)), zorder=2)
    label(ax, 90, 24, "never in the same genome,\nnever inherited together", INK)
    made.append(("05-separate", fig))

    # 6 — so there is nothing to read
    fig, ax = canvas()
    label(ax, 24, 47, "phage genomes", TEAL, ha="center", size=17, weight="bold")
    label(ax, 62, 47, "bacterial genomes", RUST, ha="center", size=17, weight="bold")
    for r in range(5):
        y = 40 - r * 7.6
        blob(ax, 24, y, 3.2, 2.4, "#E8ECEA", seed=r, edge="#C8D0CE", z=4)
        blob(ax, 62, y, 3.2, 2.4, "#EFE8E3", seed=r + 9, edge="#D9C9BF", z=4)
    tag(ax, 43, 24, "the record was never written", RUST, size=22)
    label(ax, 90, 16, "so the interface score\nis noise — and more\ncompute cannot help",
          RUST)
    made.append(("06-never-written", fig))

    for name, fig in made:
        print(save(fig, name, "interface").name)
    return len(made)


# --------------------------------------------------------------------------- #
# the screen, and the control gate that retired it
# --------------------------------------------------------------------------- #

def _grid(ax, x0, y0, cols, rows, cell, values=None, cmap=None, grey=False):
    for r in range(rows):
        for c in range(cols):
            v = 0.5 if values is None else values[r][c]
            col = "#E4E8E6" if grey else (cmap(v) if cmap else "#BBD3CF")
            ax.add_patch(__import__("matplotlib.patches", fromlist=["FancyBboxPatch"])
                         .FancyBboxPatch((x0 + c * cell, y0 + r * cell),
                                         cell * 0.86, cell * 0.86,
                                         boxstyle="round,pad=0.02,rounding_size=0.25",
                                         facecolor=col, edgecolor="none", zorder=3))


def screen_gate():
    import matplotlib.cm as cm
    made = []
    rng = np.random.default_rng(7)
    vals = rng.random((9, 16))

    fig, ax = canvas()
    _grid(ax, 8, 8, 16, 9, 3.4, grey=True)
    label(ax, 90, 30, "114 binding proteins\n× 63 receptors", INK)
    label(ax, 90, 20, "7,182 pairs", TEAL, size=22, weight="bold")
    made.append(("01-matrix", fig))

    fig, ax = canvas()
    _grid(ax, 8, 8, 16, 9, 3.4, values=vals, cmap=cm.get_cmap("BuGn"))
    label(ax, 90, 28, "every pair folded,\nevery pair scored", INK)
    label(ax, 90, 18, "and the ranking\nlooked reasonable", MUTED)
    made.append(("02-scored", fig))

    fig, ax = canvas()
    _grid(ax, 8, 8, 16, 9, 3.4, values=vals, cmap=cm.get_cmap("BuGn"))
    for i, (txt, col) in enumerate((("known binder", TEAL), ("scrambled", RUST),
                                    ("mismatched", RUST))):
        y = 40 - i * 6.5
        ax.add_patch(__import__("matplotlib.patches", fromlist=["FancyBboxPatch"])
                     .FancyBboxPatch((66, y - 2.1), 15, 4.2,
                                     boxstyle="round,pad=0.1,rounding_size=1.0",
                                     facecolor="#F3F5F4", edgecolor=col, lw=2,
                                     zorder=5))
        label(ax, 73.5, y, txt, col, ha="center", size=14)
    label(ax, 90, 20, "before trusting it,\nwe scored pairs whose\nanswer we knew", INK)
    made.append(("03-controls-in", fig))

    fig, ax = canvas()
    for i, (txt, val, col) in enumerate((("known binder", 0.137, TEAL),
                                         ("scrambled", 0.136, RUST),
                                         ("mismatched", 0.139, RUST))):
        y = 38 - i * 11
        ax.add_patch(__import__("matplotlib.patches", fromlist=["FancyBboxPatch"])
                     .FancyBboxPatch((10, y - 2.6), 48 * val / 0.2, 5.2,
                                     boxstyle="round,pad=0.05,rounding_size=1.2",
                                     facecolor=col, edgecolor="none", alpha=0.85,
                                     zorder=4))
        label(ax, 10, y + 5.6, txt, MUTED, size=15)
        label(ax, 12 + 48 * val / 0.2, y, f"{val:.3f}", INK, size=19, weight="bold")
    label(ax, 90, 24, "they did not separate", RUST, size=20, weight="bold")
    made.append(("04-no-separation", fig))

    fig, ax = canvas()
    _grid(ax, 8, 8, 16, 9, 3.4, grey=True)
    tag(ax, 36, 42, "the ranking means nothing", RUST, size=21)
    label(ax, 90, 24, "nine control folds\ndecided the fate\nof seven thousand", INK)
    made.append(("05-retired", fig))

    for name, fig in made:
        print(save(fig, name, "screen").name)
    return len(made)


# --------------------------------------------------------------------------- #
# how a rung period names a fold
# --------------------------------------------------------------------------- #

def rung_period():
    made = []

    def prism(ax, x, y0, coils=7, pitch=4.6, half=7.0, colour=TEAL, bonds=False):
        for k in range(coils):
            yy = y0 + k * pitch
            t = np.linspace(0, 1, 60)
            ax.plot(x - half + 2 * half * t, yy + 1.5 * np.sin(t * math.pi * 2),
                    color=colour, lw=LW, solid_capstyle="round", zorder=4)
            if bonds and k:
                for bx in (x - half * 0.55, x, x + half * 0.55):
                    ax.plot([bx, bx], [yy - pitch + 0.4, yy - 0.4], color=GOLD,
                            lw=LW_THIN, ls=(0, (1.5, 2)), zorder=3)

    fig, ax = canvas()
    prism(ax, 34, 8)
    label(ax, 90, 26, "a chain coiled\ninto a long prism", INK)
    made.append(("01-prism", fig))

    fig, ax = canvas()
    prism(ax, 34, 8, bonds=True)
    arrow(ax, 88, 24, 48, 22, colour=GOLD, curve=0.22)
    label(ax, 90, 24, "neighbouring coils\nhydrogen-bond in register", INK)
    made.append(("02-bonds", fig))

    fig, ax = canvas()
    prism(ax, 26, 8, bonds=True)
    xs = np.arange(2, 40)
    h = np.exp(-((xs - 17) ** 2) / 7.0) + 0.06 * np.random.default_rng(2).random(len(xs))
    ax.bar(50 + xs * 0.95, h * 22, width=0.8, color=TEAL, zorder=4)
    label(ax, 62, 30, "offsets between\nbonded partners", MUTED, size=15)
    label(ax, 90, 18, "a β-helix peaks at\nits coil period: 16–26", TEAL)
    made.append(("03-histogram", fig))

    fig, ax = canvas()
    for i, (nm, period, col) in enumerate((("β-helix", 17, TEAL),
                                           ("α-helix", 4, PURPLE),
                                           ("β-sandwich", None, MUTED))):
        x0 = 6 + i * 27
        xs = np.arange(2, 36)
        if period:
            h = np.exp(-((xs - period) ** 2) / 6.0)
        else:
            h = 0.18 + 0.1 * np.random.default_rng(i).random(len(xs))
        ax.bar(x0 + xs * 0.62, h * 20, width=0.55, color=col, zorder=4)
        label(ax, x0 + 11, 30, nm, col, ha="center", size=17, weight="bold")
    label(ax, 90, 20, "the shape of the histogram\nnames the fold — with no\nstructure database at all",
          INK)
    made.append(("04-three-folds", fig))

    for name, fig in made:
        print(save(fig, name, "rung").name)
    return len(made)


if __name__ == "__main__":
    n = cycle_wheels() + interface_noise() + screen_gate() + rung_period()
    print(f"{n} frames")
