"""Moving versions of the computational mechanisms.

The cycle wheel lights round once and settles; the question stack builds itself
and then empties; the matrix fills, the controls arrive and the ranking goes
grey; the prism coils up and its rung histogram grows out of it.
"""
import math

import matplotlib
import numpy as np
from matplotlib.patches import Arc, Circle, FancyBboxPatch

from anim_style import (GOLD, INK, LW, LW_THIN, MUTED, PURPLE, RUST, TEAL, arrow,
                        blob, label, tag)
from motion import fan

STEPS = ("Design", "Build", "Test", "Learn")
CYCLES = ("The wrong question", "Ask the protein what it is",
          "Build the enzymes", "Let the bacteria answer")
DIM = "#D6DEDC"


# --------------------------------------------------------------------------- #
# the loop itself — the spine that returns at every act
# --------------------------------------------------------------------------- #

def _wheel(ax, cx, cy, r, lit):
    """Four arcs around a ring; `lit` is a per-arc 0..1."""
    for i, name in enumerate(STEPS):
        a0, a1 = 90 - i * 90 - 78, 90 - i * 90 - 12
        on = lit[i]
        ax.add_patch(Arc((cx, cy), 2 * r, 2 * r, theta1=a0, theta2=a1,
                         lw=8, color=DIM, capstyle="round", zorder=3))
        if on > 0.01:
            ax.add_patch(Arc((cx, cy), 2 * r, 2 * r, theta1=a0, theta2=a1,
                             lw=11, color=TEAL, capstyle="round", zorder=4,
                             alpha=on))
        mid = math.radians((a0 + a1) / 2)
        ax.text(cx + (r + 6.0) * math.cos(mid), cy + (r + 6.0) * math.sin(mid),
                name, fontsize=16, ha="center", va="center",
                color=INK if on > 0.5 else MUTED,
                weight="bold" if on > 0.5 else "normal", zorder=6)


def _cycle_draw(i):
    def draw(ax, s):
        # the travelling highlight: a position on the ring, 0..3, that lands on i
        p = s["sweep"]
        lit = []
        for k in range(4):
            d = abs(p - k)
            lit.append(max(0.0, 1 - d / 0.85) * s["ring"])
        _wheel(ax, 30, 26, 15, lit)
        ax.text(30, 28.5, f"Cycle {i + 1}", fontsize=27, ha="center", va="center",
                color=INK, weight="bold", alpha=s["mid"], zorder=6)
        ax.text(30, 22.5, "of four", fontsize=16, ha="center", va="center",
                color=MUTED, alpha=s["mid"], zorder=6)
        label(ax, 60, 30, CYCLES[i], TEAL, size=26, weight="bold", alpha=s["name"])
        label(ax, 60, 23.5, "Design · Build · Test · Learn", MUTED, size=17,
              alpha=s["name"])
    return draw


def _cycle_keys(i):
    # the highlight runs all the way round, then parks on this cycle's step
    return [
        (0.0, dict(sweep=-1.0, ring=1.0, mid=0.0, name=0.0)),
        (0.4, dict(sweep=0.0)),
        (1.0, dict(sweep=1.0)),
        (1.6, dict(sweep=2.0)),
        (2.2, dict(sweep=3.0, mid=1.0)),
        (3.0, dict(sweep=float(i))),
        (3.8, dict(name=1.0)),
        (4.6, dict()),
    ]


# --------------------------------------------------------------------------- #
# why an interface score carries no signal
# --------------------------------------------------------------------------- #

def _pair(ax, x, y, s=1.0, hit=0.0, alpha=1.0, z=4):
    """Two protein blobs facing each other; `hit` lights the co-varying pair."""
    if alpha <= 0.004:
        return
    blob(ax, x - 4.4 * s, y, 3.4 * s, 2.6 * s, "#BBD3CF", seed=3, edge=TEAL, z=z,
         alpha=alpha)
    blob(ax, x + 4.4 * s, y, 3.4 * s, 2.6 * s, "#E3CDBE", seed=8, edge=RUST, z=z,
         alpha=alpha)
    if hit > 0.01:
        for dx in (-1.4 * s, 1.4 * s):
            ax.add_patch(Circle((x + dx, y), 0.55 * s, color=GOLD, zorder=z + 2,
                                alpha=alpha * hit))


def draw_covary(ax, s):
    # the first pair starts big and centred, then takes its place at the top
    big = s["big"]
    y1 = 30 + (42 - 30) * (1 - big)
    sc = 1.0 + 0.7 * big
    _pair(ax, 42, y1, s=sc, hit=s["hit"])
    rows = fan(4, s["stack"], step=0.17, span=0.42)
    for r, a in enumerate(rows):
        _pair(ax, 42, 31 - r * 7.4, s=0.72, hit=s["hit"], alpha=a)
        label(ax, 10, 31 - r * 7.4, f"species {r + 2}", MUTED, size=14, alpha=a)
    label(ax, 10, 42, "species 1", MUTED, size=14, alpha=rows[0])

    label(ax, 42, 14, "do these two touch?", INK, ha="center", size=22,
          alpha=s["q"])
    label(ax, 90, 30, "the model looks\nacross thousands\nof species", INK,
          alpha=s["l_many"])
    arrow(ax, 88, 26, 50, 25, colour=GOLD, curve=0.2, alpha=s["l_cov"],
          draw=s["l_cov"])
    label(ax, 90, 26, "when this residue changes,\nthat one changes to match", INK,
          alpha=s["l_cov"])
    tag(ax, 42, 2.5, "that pattern is the fingerprint of contact", TEAL, size=20,
        alpha=s["t_fp"], rule=s["t_fp"])


KEYS_COVARY = [
    (0.0, dict(big=1.0, hit=0.0, stack=0.0, q=0.0, l_many=0.0, l_cov=0.0,
               t_fp=0.0)),
    (0.9, dict(q=1.0)),
    (3.0, dict(q=1.0)),
    (3.6, dict(q=0.0)),
    (4.4, dict(big=0.0)),
    (5.0, dict(l_many=1.0)),
    (6.4, dict(stack=1.0)),
    (8.0, dict(l_many=1.0)),
    (8.6, dict(l_many=0.0)),
    (9.4, dict(hit=1.0, l_cov=1.0)),
    (12.0, dict(l_cov=1.0)),
    (12.6, dict(l_cov=0.0)),
    (13.4, dict(t_fp=1.0)),
    (14.6, dict()),
]


def draw_separate(ax, s):
    label(ax, 24, 47, "phage genomes", TEAL, ha="center", size=17, weight="bold",
          alpha=s["heads"])
    label(ax, 62, 47, "bacterial genomes", RUST, ha="center", size=17,
          weight="bold", alpha=s["heads"])
    rows = fan(5, s["rows"], step=0.13, span=0.4)
    for r, a in enumerate(rows):
        y = 40 - r * 7.6
        g = s["grey"]
        blob(ax, 24, y, 3.2, 2.4, "#BBD3CF", seed=r, edge=TEAL, z=4,
             alpha=a * (1 - g))
        blob(ax, 62, y, 3.2, 2.4, "#E3CDBE", seed=r + 9, edge=RUST, z=4,
             alpha=a * (1 - g))
        if g > 0.01:
            blob(ax, 24, y, 3.2, 2.4, "#E8ECEA", seed=r, edge="#C8D0CE", z=4,
                 alpha=a * g)
            blob(ax, 62, y, 3.2, 2.4, "#EFE8E3", seed=r + 9, edge="#D9C9BF", z=4,
                 alpha=a * g)
        ax.plot([32, 54], [y, y], color="#E2E6E4", lw=2.4, ls=(0, (2, 4)),
                zorder=2, alpha=a * s["dash"] * (1 - g))
    label(ax, 90, 24, "never in the same genome,\nnever inherited together", INK,
          alpha=s["l_never"])
    tag(ax, 43, 24, "the record was never written", RUST, size=22, alpha=s["t_rec"],
        rule=s["t_rec"])
    label(ax, 90, 16, "so the interface score\nis noise — and more\ncompute cannot help",
          RUST, alpha=s["l_noise"])


KEYS_SEPARATE = [
    (0.0, dict(heads=0.0, rows=0.0, dash=0.0, grey=0.0, l_never=0.0, t_rec=0.0,
               l_noise=0.0)),
    (0.7, dict(heads=1.0)),
    (2.0, dict(rows=1.0)),
    (3.2, dict(dash=1.0)),
    (4.0, dict(l_never=1.0)),
    (6.4, dict(l_never=1.0)),
    (7.0, dict(l_never=0.0)),
    (8.2, dict(grey=1.0)),
    (9.0, dict(t_rec=1.0)),
    (10.6, dict(l_noise=1.0)),
    (12.2, dict()),
]


# --------------------------------------------------------------------------- #
# the screen, and the control gate that retired it
# --------------------------------------------------------------------------- #

CMAP = matplotlib.colormaps["BuGn"]
RNG_VALS = np.random.default_rng(7).random((9, 16))


def _grid(ax, x0, y0, cell, fill, grey_alpha=1.0):
    """16 x 9 cells. `fill` is 0..1: how far the colour has swept across."""
    for r in range(9):
        for c in range(16):
            x, y = x0 + c * cell, y0 + r * cell
            ax.add_patch(FancyBboxPatch((x, y), cell * 0.86, cell * 0.86,
                                        boxstyle="round,pad=0.02,rounding_size=0.25",
                                        facecolor="#E4E8E6", edgecolor="none",
                                        zorder=3, alpha=grey_alpha))
            a = min(1.0, max(0.0, (fill * 18 - c - r * 0.25) / 1.6))
            if a > 0.01:
                ax.add_patch(FancyBboxPatch(
                    (x, y), cell * 0.86, cell * 0.86,
                    boxstyle="round,pad=0.02,rounding_size=0.25",
                    facecolor=CMAP(RNG_VALS[r][c]), edgecolor="none", zorder=4,
                    alpha=a))


def draw_matrix(ax, s):
    _grid(ax, 8, 8, 3.4, s["fill"], grey_alpha=1.0)
    label(ax, 90, 30, "114 binding proteins\n× 63 receptors", INK, alpha=s["l_size"])
    label(ax, 90, 20, "7,182 pairs", TEAL, size=22, weight="bold", alpha=s["l_n"])
    label(ax, 90, 28, "every pair folded,\nevery pair scored", INK, alpha=s["l_run"])
    label(ax, 90, 18, "and the ranking\nlooked reasonable", MUTED, alpha=s["l_run"])

    cards = fan(3, s["ctrl"], step=0.2, span=0.45)
    for i, (txt, col) in enumerate((("known binder", TEAL), ("scrambled", RUST),
                                    ("mismatched", RUST))):
        a = cards[i]
        if a <= 0.01:
            continue
        y = 40 - i * 6.5
        x = 66 + 10 * (1 - a)          # slides in from the right as it appears
        ax.add_patch(FancyBboxPatch((x, y - 2.1), 15, 4.2,
                                    boxstyle="round,pad=0.1,rounding_size=1.0",
                                    facecolor="#F3F5F4", edgecolor=col, lw=2,
                                    zorder=5, alpha=a))
        label(ax, x + 7.5, y, txt, col, ha="center", size=14, alpha=a)
    label(ax, 90, 20, "before trusting it,\nwe scored pairs whose\nanswer we knew",
          INK, alpha=s["l_ctrl"])


KEYS_MATRIX = [
    (0.0, dict(fill=0.0, l_size=0.0, l_n=0.0, l_run=0.0, ctrl=0.0, l_ctrl=0.0)),
    (0.8, dict(l_size=1.0)),
    (1.8, dict(l_n=1.0)),
    (3.4, dict(l_size=1.0, l_n=1.0)),
    (4.0, dict(l_size=0.0, l_n=0.0)),
    (4.3, dict(l_run=1.0)),
    (7.0, dict(fill=1.0)),
    (8.2, dict(l_run=1.0)),
    (8.8, dict(l_run=0.0)),
    (9.6, dict(ctrl=1.0, l_ctrl=1.0)),
    (11.6, dict()),
]


CONTROLS = (("known binder", 0.137, TEAL), ("scrambled", 0.136, RUST),
            ("mismatched", 0.139, RUST))


def draw_bars(ax, s):
    grow = fan(3, s["grow"], step=0.18, span=0.55)
    for i, (txt, val, col) in enumerate(CONTROLS):
        y = 38 - i * 11
        g = grow[i]
        label(ax, 10, y + 5.6, txt, MUTED, size=15, alpha=min(1.0, g * 3))
        w = 48 * val / 0.2 * g
        if w > 0.4:
            ax.add_patch(FancyBboxPatch((10, y - 2.6), w, 5.2,
                                        boxstyle="round,pad=0.05,rounding_size=1.2",
                                        facecolor=col, edgecolor="none", alpha=0.85,
                                        zorder=4))
        if g > 0.9:
            label(ax, 12 + w, y, f"{val:.3f}", INK, size=19, weight="bold",
                  alpha=(g - 0.9) * 10)
    # the line that makes the point: they all stop in the same place
    if s["rule"] > 0.01:
        x = 10 + 48 * 0.137 / 0.2
        ax.plot([x, x], [38 - 2 * 11 - 5.5, 38 + 5.5], color=INK, lw=2.0,
                ls=(0, (4, 3)), alpha=s["rule"], zorder=6)
    label(ax, 90, 24, "they did not separate", RUST, size=20, weight="bold",
          alpha=s["l_same"])


KEYS_BARS = [
    (0.0, dict(grow=0.0, rule=0.0, l_same=0.0)),
    (0.5, dict()),
    (3.4, dict(grow=1.0)),
    (4.4, dict(rule=1.0)),
    (5.4, dict(l_same=1.0)),
    (7.0, dict()),
]


def draw_retired(ax, s):
    _grid(ax, 8, 8, 3.4, 1 - s["drain"], grey_alpha=1.0)
    tag(ax, 36, 42, "the ranking means nothing", RUST, size=21, alpha=s["t"],
        rule=s["t"])
    label(ax, 90, 24, "nine control folds\ndecided the fate\nof seven thousand", INK,
          alpha=s["l"])


KEYS_RETIRED = [
    (0.0, dict(drain=0.0, t=0.0, l=0.0)),
    (2.2, dict(drain=1.0)),
    (3.0, dict(t=1.0)),
    (4.6, dict(l=1.0)),
    (6.0, dict()),
]


# --------------------------------------------------------------------------- #
# how a rung period names a fold
# --------------------------------------------------------------------------- #

def _prism(ax, x, y0, grown=1.0, coils=7, pitch=4.6, half=7.0, colour=TEAL,
           bonds=0.0):
    """Coils appear from the bottom up as `grown` goes 0 to 1."""
    for k in range(coils):
        a = min(1.0, max(0.0, (grown * coils - k) / 0.8))
        if a <= 0.01:
            continue
        yy = y0 + k * pitch
        t = np.linspace(0, 1, 60)
        ax.plot(x - half + 2 * half * t, yy + 1.5 * np.sin(t * math.pi * 2),
                color=colour, lw=LW, solid_capstyle="round", zorder=4, alpha=a)
        if bonds > 0.01 and k:
            b = min(1.0, max(0.0, (bonds * coils - k) / 0.8))
            for bx in (x - half * 0.55, x, x + half * 0.55):
                ax.plot([bx, bx], [yy - pitch + 0.4, yy - 0.4], color=GOLD,
                        lw=LW_THIN, ls=(0, (1.5, 2)), zorder=3, alpha=b * a)


HIST_X = np.arange(2, 40)
HIST_H = (np.exp(-((HIST_X - 17) ** 2) / 7.0)
          + 0.06 * np.random.default_rng(2).random(len(HIST_X)))


def draw_prism(ax, s):
    x = 34 + (26 - 34) * s["shift"]
    _prism(ax, x, 8, grown=s["grown"], bonds=s["bonds"])
    label(ax, 90, 26, "a chain coiled\ninto a long prism", INK, alpha=s["l_coil"])
    arrow(ax, 88, 24, 48, 22, colour=GOLD, curve=0.22, alpha=s["l_bond"],
          draw=s["l_bond"])
    label(ax, 90, 24, "neighbouring coils\nhydrogen-bond in register", INK,
          alpha=s["l_bond"])
    if s["hist"] > 0.01:
        ax.bar(50 + HIST_X * 0.95, HIST_H * 22 * s["hist"], width=0.8, color=TEAL,
               zorder=4, alpha=min(1.0, s["hist"] * 2))
    label(ax, 62, 30, "offsets between\nbonded partners", MUTED, size=15,
          alpha=s["l_off"])
    label(ax, 90, 18, "a β-helix peaks at\nits coil period: 16–26", TEAL,
          alpha=s["l_peak"])


KEYS_PRISM = [
    (0.0, dict(grown=0.0, bonds=0.0, shift=0.0, hist=0.0, l_coil=0.0, l_bond=0.0,
               l_off=0.0, l_peak=0.0)),
    (2.4, dict(grown=1.0)),
    (3.0, dict(l_coil=1.0)),
    (5.0, dict(l_coil=1.0)),
    (5.6, dict(l_coil=0.0)),
    (6.0, dict(l_bond=1.0)),
    (7.8, dict(bonds=1.0)),
    (9.4, dict(l_bond=1.0)),
    (10.0, dict(l_bond=0.0)),
    (10.6, dict(shift=1.0, l_off=1.0)),
    (12.4, dict(hist=1.0)),
    (13.4, dict(l_peak=1.0)),
    (15.0, dict()),
]


FOLDS = (("β-helix", 17, TEAL), ("α-helix", 4, PURPLE), ("β-sandwich", None, MUTED))


def draw_folds(ax, s):
    grow = fan(3, s["grow"], step=0.22, span=0.5)
    for i, (nm, period, col) in enumerate(FOLDS):
        x0 = 6 + i * 27
        xs = np.arange(2, 36)
        if period:
            h = np.exp(-((xs - period) ** 2) / 6.0)
        else:
            h = 0.18 + 0.1 * np.random.default_rng(i).random(len(xs))
        g = grow[i]
        if g > 0.01:
            ax.bar(x0 + xs * 0.62, h * 20 * g, width=0.55, color=col, zorder=4,
                   alpha=min(1.0, g * 3))
        label(ax, x0 + 11, 30, nm, col, ha="center", size=17, weight="bold",
              alpha=min(1.0, g * 2))
    label(ax, 90, 20,
          "the shape of the histogram\nnames the fold — with no\nstructure database at all",
          INK, alpha=s["l"])


KEYS_FOLDS = [
    (0.0, dict(grow=0.0, l=0.0)),
    (3.2, dict(grow=1.0)),
    (4.2, dict(l=1.0)),
    (5.8, dict()),
]


SCENES = {
    **{f"wheel-cycle-{i + 1}": (_cycle_draw(i), _cycle_keys(i)) for i in range(4)},
    "interface-covary": (draw_covary, KEYS_COVARY),
    "interface-separate": (draw_separate, KEYS_SEPARATE),
    "screen-matrix": (draw_matrix, KEYS_MATRIX),
    "screen-controls": (draw_bars, KEYS_BARS),
    "screen-retired": (draw_retired, KEYS_RETIRED),
    "rung-prism": (draw_prism, KEYS_PRISM),
    "rung-folds": (draw_folds, KEYS_FOLDS),
}
