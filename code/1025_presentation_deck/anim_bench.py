"""Animations for the bench and the genomes: the nickel column that failed at
capture, the three outcomes a gel cannot tell apart, the cassette that swaps in
one slot, a capsule hiding an intact O-antigen, walking back up a tree, and
checking a variant at read level.

    python code/1025_presentation_deck/anim_bench.py
"""
import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

from anim_style import (GOLD, HEAD, INK, LW, LW_THIN, MUTED, PURPLE, RUST, TEAL,
                        WALL, arrow, blob, canvas, capsule, envelope_base, label,
                        save, sugar_layer, tag)


def card(ax, x, y, w, h, fill="#F4F6F5", edge=None, lw=2.0, z=3):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.1,rounding_size=1.4",
                                facecolor=fill, edgecolor=edge or "none",
                                lw=lw, zorder=z))


# --------------------------------------------------------------------------- #
# the nickel column, and where it actually failed
# --------------------------------------------------------------------------- #

def column(ax, x, y0, h=26, w=11, beads=True, z=3):
    card(ax, x, y0, w, h, fill="#F2F4F3", edge="#C9D2D0", lw=2.0, z=z)
    if beads:
        rng = np.random.default_rng(3)
        for r in range(9):
            for c in range(3):
                ax.add_patch(Circle((x + 2.2 + c * 3.3 + rng.uniform(-.4, .4),
                                     y0 + 2.4 + r * 2.6 + rng.uniform(-.3, .3)),
                                    1.15, color="#CBD7CF", lw=0, zorder=z + 1))


def protein(ax, x, y, tagged=True, colour=TEAL, s=1.0, z=6):
    blob(ax, x, y, 1.9 * s, 1.5 * s, "#BBD3CF", seed=int(x * 7) % 11, edge=colour, z=z)
    if tagged:
        ax.add_patch(Circle((x + 1.9 * s, y + 0.9 * s), 0.6 * s, color=GOLD, lw=0,
                            zorder=z + 1))


def nickel():
    made = []

    fig, ax = canvas()
    column(ax, 30, 12)
    for i, dx in enumerate((-4.5, 0, 4.5)):
        protein(ax, 36 + dx, 45)
    label(ax, 90, 34, "His-tagged protein\ngoes onto the column", INK)
    label(ax, 90, 22, "the tag should hold it\non the resin", MUTED)
    made.append(("01-load", fig))

    fig, ax = canvas()
    column(ax, 30, 12)
    for dx in (-4.5, 0, 4.5):
        protein(ax, 36 + dx, 33)
    arrow(ax, 88, 30, 48, 30, colour=MUTED, curve=0.2)
    label(ax, 90, 30, "it runs through the resin", MUTED)
    made.append(("02-through", fig))

    fig, ax = canvas()
    column(ax, 30, 12)
    for dx in (-4.5, 0, 4.5):
        protein(ax, 36 + dx, 6)
    tag(ax, 16, 44, "nothing bound", RUST, size=20)
    arrow(ax, 88, 8, 50, 6, curve=0.2)
    label(ax, 90, 8, "it all came off in\nthe flow-through", RUST)
    made.append(("03-flowthrough", fig))

    fig, ax = canvas()
    column(ax, 30, 12)
    card(ax, 56, 4, 13, 9, fill="#FFFFFF", edge="#C9D2D0")
    label(ax, 62.5, 8.5, "empty", MUTED, ha="center", size=17)
    label(ax, 62.5, 15.5, "elution", MUTED, ha="center", size=15)
    label(ax, 90, 24, "and the elutions\ncame off blank", RUST)
    made.append(("04-elution-empty", fig))

    fig, ax = canvas()
    for i, (lab, dark) in enumerate((("negative\ncontrol", 0.10),
                                     ("flow-\nthrough", 0.82))):
        x = 22 + i * 26
        ax.add_patch(Circle((x, 26), 6.6, color=INK, alpha=dark, lw=0, zorder=4))
        label(ax, x, 14, lab, MUTED, ha="center", size=15)
    label(ax, 48, 26, "2.9×", TEAL, size=26, weight="bold")
    tag(ax, 36, 42, "the protein was there all along", TEAL, size=20)
    label(ax, 90, 24, "it failed at capture,\nnot at expression", INK)
    made.append(("05-dotblot", fig))

    for name, fig in made:
        print(save(fig, name, "nickel").name)
    return len(made)


# --------------------------------------------------------------------------- #
# three outcomes a gel cannot tell apart
# --------------------------------------------------------------------------- #

def gel_lane(ax, x, y0, band=None, h=22, w=9, z=4):
    card(ax, x, y0, w, h, fill="#E9ECEB", edge=None, z=z)
    if band is not None:
        ax.add_patch(FancyBboxPatch((x + 0.9, y0 + band), w - 1.8, 1.5,
                                    boxstyle="round,pad=0.05,rounding_size=0.4",
                                    facecolor=INK, edgecolor="none", zorder=z + 1))


def indistinguishable():
    made = []
    cases = (("no protein\nwas made", TEAL),
             ("made, but\ninsoluble", PURPLE),
             ("made — not\ncaptured", RUST))

    fig, ax = canvas()
    for i, (txt, col) in enumerate(cases):
        x = 6 + i * 27
        card(ax, x, 22, 23, 15, fill="#F6F8F7", edge=col, lw=2.2)
        label(ax, x + 11.5, 29.5, txt, col, ha="center", size=16)
    label(ax, 90, 30, "three different things\nmight be happening", INK)
    made.append(("01-three-cases", fig))

    fig, ax = canvas()
    for i, (txt, col) in enumerate(cases):
        x = 6 + i * 27
        card(ax, x, 33, 23, 12, fill="#F6F8F7", edge=col, lw=2.2)
        label(ax, x + 11.5, 39, txt, col, ha="center", size=15)
        arrow(ax, x + 11.5, 31.5, 38.5, 24, colour=col,
              curve=0.26 if i != 1 else 0.02)
        gel_lane(ax, 34, 1, band=None, h=21)
    label(ax, 90, 16, "and all three give you\nthe same blank lane", MUTED)
    made.append(("02-same-lane", fig))

    fig, ax = canvas()
    gel_lane(ax, 34, 12, band=None)
    tag(ax, 38.5, 42, "a gel cannot separate them", RUST, size=21)
    made.append(("03-cannot", fig))

    fig, ax = canvas()
    for i, (txt, col, dark) in enumerate((("no protein", TEAL, 0.10),
                                          ("insoluble", PURPLE, 0.12),
                                          ("in the flow-through", RUST, 0.82))):
        x = 16 + i * 24
        ax.add_patch(Circle((x, 28), 6.2, color=INK, alpha=dark, lw=0, zorder=4))
        label(ax, x, 17, txt, col, ha="center", size=14)
    tag(ax, 40, 44, "one cheap assay does", TEAL, size=21)
    label(ax, 90, 24, "an anti-His dot blot\nreads the tag directly", INK)
    made.append(("04-dotblot-splits", fig))

    for name, fig in made:
        print(save(fig, name, "indistinguishable").name)
    return len(made)


# --------------------------------------------------------------------------- #
# the same slot, three unrelated cargoes
# --------------------------------------------------------------------------- #

PALETTES = {
    23: ["#9FBDB8", "#BBD3CF", "#7FA8A2", "#A8C4BF"],
    15: ["#D9C4B3", "#E3CDBE", "#C9AE98", "#EFE1D6"],
    25: ["#BDAED4", "#D2C7E3", "#A796C4", "#E0D8EC"],
}


def gene_row(ax, y, genes, x0=10, width=62, flank=TEAL, z=4):
    ax.plot([x0 - 5, x0 + width + 5], [y + 1.6, y + 1.6], color="#D6DEDC", lw=3,
            solid_capstyle="round", zorder=z - 1)
    for side in (x0 - 4.4, x0 + width + 0.6):
        ax.add_patch(FancyBboxPatch((side, y), 3.8, 3.2,
                                    boxstyle="round,pad=0.05,rounding_size=0.6",
                                    facecolor=flank, edgecolor="none", zorder=z))
    rng = np.random.default_rng(genes)
    n = genes
    w = width / n
    for i in range(n):
        ax.add_patch(FancyBboxPatch((x0 + i * w + 0.25, y + 0.1), w - 0.5, 3.0,
                                    boxstyle="round,pad=0.04,rounding_size=0.5",
                                    facecolor=rng.choice(
                                        PALETTES.get(n, ["#9FBDB8", "#BBD3CF"])),
                                    edgecolor="none", zorder=z))


def cassette():
    made = []
    strains = ((23, "Strain 2 — the host", TEAL),
               (15, "Strain 1", MUTED),
               (25, "Strain 3", PURPLE))

    fig, ax = canvas()
    gene_row(ax, 24, 23)
    label(ax, 5.6, 32, "ihfB", TEAL, ha="center", size=14)
    label(ax, 78, 32, "flank", TEAL, ha="center", size=14)
    label(ax, 90, 26, "one slot in the genome,\nfixed by the genes\non either side", INK)
    made.append(("01-slot", fig))

    for i, (n, name, col) in enumerate(strains):
        fig, ax = canvas()
        for k in range(i + 1):
            gn, nm, cc = strains[k]
            y = 38 - k * 13
            gene_row(ax, y, gn)
            label(ax, 10, y + 6.4, nm, cc, size=15, weight="bold")
            label(ax, 80, y + 1.6, f"{gn} genes", MUTED, size=14)
        if i == 2:
            label(ax, 90, 26, "same slot, same flanks —\nand no shared genes\ninside",
                  RUST)
        made.append((f"{i + 2:02d}-strain", fig))

    fig, ax = canvas()
    for k, (gn, nm, cc) in enumerate(strains):
        y = 38 - k * 13
        gene_row(ax, y, gn)
        label(ax, 10, y + 6.4, nm, cc, size=15, weight="bold")
    tag(ax, 42, 4, "4 of 45 clusters shared — all generic sugar chemistry", RUST,
        size=18)
    made.append(("05-verdict", fig))

    for name, fig in made:
        print(save(fig, name, "cassette").name)
    return len(made)


# --------------------------------------------------------------------------- #
# a capsule over an intact O-antigen
# --------------------------------------------------------------------------- #

def masking():
    made = []

    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top)
    arrow(ax, 88, 20, 56, 17, colour=TEAL, curve=0.22)
    label(ax, 90, 20, "Cycle 2 said the receptor\nis this sugar", TEAL)
    made.append(("01-oantigen", fig))

    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top)
    capsule(ax, 22.0)
    ax.add_patch(Circle((43, 23.4), 2.0, color=RUST, lw=0, zorder=6))
    arrow(ax, 88, 30, 48, 25, curve=0.22)
    label(ax, 90, 30, "Cycle 4 found the one\nmutation up here", RUST)
    made.append(("02-capsule", fig))

    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top)
    capsule(ax, 22.0)
    ax.add_patch(Circle((43, 23.4), 2.0, color=RUST, lw=0, zorder=6))
    tag(ax, 43, 40, "both can be true at once", INK, size=21)
    label(ax, 90, 18, "a capsule lies over\nan O-antigen that is\nstill intact", INK)
    made.append(("03-both", fig))

    for name, fig in made:
        print(save(fig, name, "masking").name)
    return len(made)


# --------------------------------------------------------------------------- #
# walking back up the tree
# --------------------------------------------------------------------------- #

def tree_up():
    made = []
    tips = [(62, 6 + i * 6.2) for i in range(7)]
    nodes = [(48, 15.4), (40, 21.6), (30, 27.8)]

    def draw(ax, upto):
        for x, y in tips:
            ax.add_patch(Circle((x, y), 1.0, color="#BBD3CF", lw=0, zorder=5))
            ax.plot([x, 48], [y, y], color="#D6DEDC", lw=2.2, zorder=3)
        ax.plot([48, 48], [tips[0][1], tips[-1][1]], color="#D6DEDC", lw=2.2, zorder=3)
        for i, (x, y) in enumerate(nodes):
            on = i < upto
            ax.plot([x, nodes[i - 1][0] if i else 48], [y, nodes[i - 1][1] if i else y],
                    color=TEAL if on else "#D6DEDC", lw=3.0 if on else 2.2, zorder=3)
            ax.add_patch(Circle((x, y), 1.9 if on else 1.3,
                                color=TEAL if on else "#D6DEDC", lw=0, zorder=5))

    labels = ("the enzyme Φ8 carries today", "Node 1", "Node 40", "Node 281")
    for step in range(4):
        fig, ax = canvas()
        draw(ax, step)
        label(ax, 68, 42, "present-day relatives", MUTED, size=15)
        if step == 0:
            arrow(ax, 88, 20, 64, 20, colour=TEAL, curve=0.2)
            label(ax, 90, 20, labels[0], TEAL)
        else:
            x, y = nodes[step - 1]
            arrow(ax, 88, y + 6, x + 3, y + 1, colour=TEAL, curve=0.22)
            label(ax, 90, y + 6, f"{labels[step]} — reconstructed", TEAL)
        made.append((f"{step + 1:02d}-node", fig))

    fig, ax = canvas()
    draw(ax, 3)
    tag(ax, 42, 44, "three sequences that exist nowhere in nature", TEAL, size=19)
    made.append(("05-three", fig))

    for name, fig in made:
        print(save(fig, name, "tree").name)
    return len(made)


# --------------------------------------------------------------------------- #
# checking a variant at read level
# --------------------------------------------------------------------------- #

def reads():
    made = []

    fig, ax = canvas()
    for i in range(17):
        x = 8 + i * 4.2
        ax.add_patch(FancyBboxPatch((x, 24), 3.0, 3.0,
                                    boxstyle="round,pad=0.04,rounding_size=0.5",
                                    facecolor="#E3CDBE", edgecolor="none", zorder=4))
    label(ax, 90, 26, "17 sites differ between\nthe assemblies", MUTED)
    label(ax, 8, 33, "candidate differences", MUTED, size=15)
    made.append(("01-candidates", fig))

    fig, ax = canvas()
    for i in range(17):
        x = 8 + i * 4.2
        keep = (i == 8)
        ax.add_patch(FancyBboxPatch((x, 24), 3.0, 3.0,
                                    boxstyle="round,pad=0.04,rounding_size=0.5",
                                    facecolor=RUST if keep else "#EDEFEE",
                                    edgecolor="none", zorder=4))
    arrow(ax, 88, 16, 44, 22, curve=0.22)
    label(ax, 90, 16, "every one taken back\nto the raw reads", INK)
    label(ax, 8, 33, "candidate differences", MUTED, size=15)
    made.append(("02-filtered", fig))

    fig, ax = canvas()
    for i, (lab, frac, col) in enumerate((("mutant reads", 263 / 264, RUST),
                                          ("parent reads", 0.0, MUTED),
                                          ("other pick", 0.0, MUTED))):
        y = 36 - i * 11
        ax.add_patch(FancyBboxPatch((10, y - 2.2), 52, 4.4,
                                    boxstyle="round,pad=0.05,rounding_size=1.1",
                                    facecolor="#EDEFEE", edgecolor="none", zorder=3))
        if frac:
            ax.add_patch(FancyBboxPatch((10, y - 2.2), 52 * frac, 4.4,
                                        boxstyle="round,pad=0.05,rounding_size=1.1",
                                        facecolor=col, edgecolor="none", zorder=4))
        label(ax, 10, y + 5.0, lab, MUTED, size=15)
        label(ax, 64, y, "263 of 264" if frac else "0", col if frac else MUTED,
              size=17, weight="bold" if frac else "normal")
    tag(ax, 40, 4, "one mutation survives", RUST, size=20)
    made.append(("03-support", fig))

    for name, fig in made:
        print(save(fig, name, "reads").name)
    return len(made)


if __name__ == "__main__":
    n = nickel() + indistinguishable() + cassette() + masking() + tree_up() + reads()
    print(f"{n} frames")
