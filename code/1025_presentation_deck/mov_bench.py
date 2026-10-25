"""Moving versions of the bench and genome mechanisms.

The protein falls straight through the resin; the blank lane stays blank
whichever cause fed it; the cassette fills one slot three different ways; the
capsule settles over an intact O-antigen; the walk up the tree happens step by
step; the candidate variants go out one at a time.
"""
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

from anim_style import (GOLD, INK, MUTED, PURPLE, RUST, TEAL, arrow, blob, canvas,
                        capsule, envelope_base, label, sugar_layer, tag)
from motion import fan


def card(ax, x, y, w, h, fill="#F4F6F5", edge=None, lw=2.0, z=3, alpha=1.0):
    if alpha <= 0.004:
        return
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.1,rounding_size=1.4",
                                facecolor=fill, edgecolor=edge or "none",
                                lw=lw, zorder=z, alpha=alpha))


# --------------------------------------------------------------------------- #
# the nickel column, and where it actually failed
# --------------------------------------------------------------------------- #

def _column(ax, x, y0, h=26, w=11, z=3):
    card(ax, x, y0, w, h, fill="#F2F4F3", edge="#C9D2D0", lw=2.0, z=z)
    rng = np.random.default_rng(3)
    for r in range(9):
        for c in range(3):
            ax.add_patch(Circle((x + 2.2 + c * 3.3 + rng.uniform(-.4, .4),
                                 y0 + 2.4 + r * 2.6 + rng.uniform(-.3, .3)),
                                1.15, color="#CBD7CF", lw=0, zorder=z + 1))


def _protein(ax, x, y, s=1.0, colour=TEAL, alpha=1.0, z=6):
    blob(ax, x, y, 1.9 * s, 1.5 * s, "#BBD3CF", seed=int(x * 7) % 11, edge=colour,
         z=z, alpha=alpha)
    ax.add_patch(Circle((x + 1.9 * s, y + 0.9 * s), 0.6 * s, color=GOLD, lw=0,
                        zorder=z + 1, alpha=alpha))


def draw_column(ax, s):
    _column(ax, 30, 12)
    for i, dx in enumerate((-4.5, 0, 4.5)):
        # a slight stagger, so the three do not fall as one rigid block
        y = s["py"] + (i - 1) * 1.4 * min(1.0, s["py"] / 45)
        _protein(ax, 36 + dx, y, alpha=s["prot"])
    label(ax, 90, 34, "His-tagged protein\ngoes onto the column", INK,
          alpha=s["l_load"])
    label(ax, 90, 22, "the tag should hold it\non the resin", MUTED,
          alpha=s["l_load"])
    arrow(ax, 88, 30, 48, 30, colour=MUTED, curve=0.2, alpha=s["l_through"],
          draw=s["l_through"])
    label(ax, 90, 30, "it runs through the resin", MUTED, alpha=s["l_through"])
    tag(ax, 16, 44, "nothing bound", RUST, size=20, alpha=s["t_none"],
        rule=s["t_none"])
    arrow(ax, 88, 8, 50, 6, curve=0.2, alpha=s["l_ft"], draw=s["l_ft"])
    label(ax, 90, 8, "it all came off in\nthe flow-through", RUST, alpha=s["l_ft"])
    if s["elu"] > 0.01:
        card(ax, 56, 4, 13, 9, fill="#FFFFFF", edge="#C9D2D0", alpha=s["elu"])
        label(ax, 62.5, 8.5, "empty", MUTED, ha="center", size=17, alpha=s["elu"])
        label(ax, 62.5, 15.5, "elution", MUTED, ha="center", size=15,
              alpha=s["elu"])
    label(ax, 90, 24, "and the elutions\ncame off blank", RUST, alpha=s["l_elu"])


KEYS_COLUMN = [
    (0.0, dict(py=45.0, prot=0.0, l_load=0.0, l_through=0.0, t_none=0.0, l_ft=0.0,
               elu=0.0, l_elu=0.0)),
    (0.6, dict(prot=1.0)),
    (1.4, dict(l_load=1.0)),
    (4.0, dict(l_load=1.0)),
    (4.6, dict(l_load=0.0)),
    (5.0, dict(l_through=1.0)),
    (6.6, dict(py=33.0)),
    (8.0, dict(l_through=1.0)),
    (8.6, dict(l_through=0.0)),
    (9.8, dict(py=6.0)),
    (10.4, dict(t_none=1.0, l_ft=1.0)),
    (12.6, dict(l_ft=1.0)),
    (13.2, dict(l_ft=0.0)),
    (13.6, dict(elu=1.0)),
    (14.6, dict(l_elu=1.0)),
    (16.0, dict()),
]


def draw_dotblot(ax, s):
    spots = fan(2, s["spots"], step=0.3, span=0.5)
    for i, (lab, dark) in enumerate((("negative\ncontrol", 0.10),
                                     ("flow-\nthrough", 0.82))):
        x = 22 + i * 26
        a = spots[i]
        ax.add_patch(Circle((x, 26), 6.6, color=INK, alpha=dark * a, lw=0, zorder=4))
        label(ax, x, 14, lab, MUTED, ha="center", size=15, alpha=a)
    label(ax, 48, 26, "2.9×", TEAL, size=26, weight="bold", alpha=s["ratio"])
    tag(ax, 36, 42, "the protein was there all along", TEAL, size=20, alpha=s["t"],
        rule=s["t"])
    label(ax, 90, 24, "it failed at capture,\nnot at expression", INK, alpha=s["l"])


KEYS_DOTBLOT = [
    (0.0, dict(spots=0.0, ratio=0.0, t=0.0, l=0.0)),
    (2.0, dict(spots=1.0)),
    (3.0, dict(ratio=1.0)),
    (4.0, dict(t=1.0)),
    (5.4, dict(l=1.0)),
    (7.0, dict()),
]


# --------------------------------------------------------------------------- #
# three outcomes a gel cannot tell apart
# --------------------------------------------------------------------------- #

CASES = (("no protein\nwas made", TEAL), ("made, but\ninsoluble", PURPLE),
         ("made — not\ncaptured", RUST))


def _lane(ax, x, y0, h=22, w=9, z=4, alpha=1.0):
    card(ax, x, y0, w, h, fill="#E9ECEB", edge=None, z=z, alpha=alpha)


def draw_cases(ax, s):
    cards = fan(3, s["cards"], step=0.2, span=0.45)
    up = s["up"]
    for i, (txt, col) in enumerate(CASES):
        x = 6 + i * 27
        y = 22 + (33 - 22) * up
        h = 15 + (12 - 15) * up
        a = cards[i] * (1 - s["clear"])
        card(ax, x, y, 23, h, fill="#F6F8F7", edge=col, lw=2.2, alpha=a)
        label(ax, x + 11.5, y + h / 2, txt, col, ha="center", size=16 - up,
              alpha=a)
        if s["arrows"] > 0.01:
            d = min(1.0, max(0.0, (s["arrows"] * 3 - i) / 1.0))
            arrow(ax, x + 11.5, y - 1.5, 38.5, 24, colour=col,
                  curve=0.26 if i != 1 else 0.02,
                  alpha=d * (1 - s["clear"]), draw=d)
    _lane(ax, 34, 1 + 11 * (1 - min(1.0, up * 2)), h=21, alpha=s["lane"])
    label(ax, 90, 30, "three different things\nmight be happening", INK,
          alpha=s["l_three"])
    label(ax, 90, 16, "and all three give you\nthe same blank lane", MUTED,
          alpha=s["l_same"])
    tag(ax, 38.5, 42, "a gel cannot separate them", RUST, size=21, alpha=s["t"],
        rule=s["t"])


KEYS_CASES = [
    (0.0, dict(cards=0.0, up=0.0, lane=0.0, arrows=0.0, clear=0.0, l_three=0.0,
               l_same=0.0, t=0.0)),
    (1.6, dict(cards=1.0)),
    (2.4, dict(l_three=1.0)),
    (4.6, dict(l_three=1.0)),
    (5.2, dict(l_three=0.0)),
    (6.4, dict(up=1.0, lane=1.0)),
    (7.8, dict(arrows=1.0)),
    (8.6, dict(l_same=1.0)),
    (11.0, dict(l_same=1.0)),
    (11.8, dict(l_same=0.0, clear=1.0)),
    (12.6, dict(t=1.0)),
    (14.0, dict()),
]


def draw_splits(ax, s):
    spots = fan(3, s["spots"], step=0.22, span=0.45)
    for i, (lab, col, dark) in enumerate((("no protein", TEAL, 0.10),
                                          ("insoluble", PURPLE, 0.12),
                                          ("in the flow-through", RUST, 0.82))):
        x = 16 + i * 24
        a = spots[i]
        ax.add_patch(Circle((x, 28), 6.2, color=INK, alpha=dark * a, lw=0, zorder=4))
        label(ax, x, 17, lab, col, ha="center", size=14, alpha=a)
    tag(ax, 40, 44, "one cheap assay does", TEAL, size=21, alpha=s["t"],
        rule=s["t"])
    label(ax, 90, 24, "an anti-His dot blot\nreads the tag directly", INK,
          alpha=s["l"])


KEYS_SPLITS = [
    (0.0, dict(spots=0.0, t=0.0, l=0.0)),
    (2.4, dict(spots=1.0)),
    (3.4, dict(t=1.0)),
    (4.8, dict(l=1.0)),
    (6.2, dict()),
]


# --------------------------------------------------------------------------- #
# the same slot, three unrelated cargoes
# --------------------------------------------------------------------------- #

PALETTES = {
    23: ["#9FBDB8", "#BBD3CF", "#7FA8A2", "#A8C4BF"],
    15: ["#D9C4B3", "#E3CDBE", "#C9AE98", "#EFE1D6"],
    25: ["#BDAED4", "#D2C7E3", "#A796C4", "#E0D8EC"],
}
STRAINS = ((23, "Strain 2 — the host", TEAL), (15, "Strain 1", MUTED),
           (25, "Strain 3", PURPLE))


def _gene_row(ax, y, genes, fill=1.0, x0=10, width=62, flank=TEAL, z=4, alpha=1.0):
    """The backbone and flanks come first; the cargo fills in left to right."""
    if alpha <= 0.004:
        return
    ax.plot([x0 - 5, x0 + width + 5], [y + 1.6, y + 1.6], color="#D6DEDC", lw=3,
            solid_capstyle="round", zorder=z - 1, alpha=alpha)
    for side in (x0 - 4.4, x0 + width + 0.6):
        ax.add_patch(FancyBboxPatch((side, y), 3.8, 3.2,
                                    boxstyle="round,pad=0.05,rounding_size=0.6",
                                    facecolor=flank, edgecolor="none", zorder=z,
                                    alpha=alpha))
    rng = np.random.default_rng(genes)
    w = width / genes
    for i in range(genes):
        a = alpha * min(1.0, max(0.0, (fill * genes * 1.25 - i) / 1.4))
        if a <= 0.01:
            continue
        ax.add_patch(FancyBboxPatch((x0 + i * w + 0.25, y + 0.1), w - 0.5, 3.0,
                                    boxstyle="round,pad=0.04,rounding_size=0.5",
                                    facecolor=rng.choice(PALETTES[genes]),
                                    edgecolor="none", zorder=z, alpha=a))


def draw_cassette(ax, s):
    # the host row starts centred, then rises to the top of the stack
    y0 = 24 + (38 - 24) * s["stack"]
    _gene_row(ax, y0, 23, fill=s["fill0"])
    label(ax, 5.6, y0 + 8, "ihfB", TEAL, ha="center", size=14, alpha=s["l_slot"])
    label(ax, 78, y0 + 8, "flank", TEAL, ha="center", size=14, alpha=s["l_slot"])
    label(ax, 90, 26, "one slot in the genome,\nfixed by the genes\non either side",
          INK, alpha=s["l_slot"])
    label(ax, 10, y0 + 6.4, STRAINS[0][1], TEAL, size=15, weight="bold",
          alpha=s["stack"])
    label(ax, 80, y0 + 1.6, "23 genes", MUTED, size=14, alpha=s["stack"])

    for k in (1, 2):
        gn, nm, cc = STRAINS[k]
        a = s[f"r{k}"]
        y = 38 - k * 13
        _gene_row(ax, y, gn, fill=s[f"f{k}"], alpha=a)
        label(ax, 10, y + 6.4, nm, cc, size=15, weight="bold", alpha=a)
        label(ax, 80, y + 1.6, f"{gn} genes", MUTED, size=14, alpha=a)

    label(ax, 90, 26, "same slot, same flanks —\nand no shared genes\ninside", RUST,
          alpha=s["l_none"])
    tag(ax, 42, 4, "4 of 45 clusters shared — all generic sugar chemistry", RUST,
        size=18, alpha=s["t"], rule=s["t"])


KEYS_CASSETTE = [
    (0.0, dict(stack=0.0, fill0=0.0, l_slot=0.0, r1=0.0, f1=0.0, r2=0.0, f2=0.0,
               l_none=0.0, t=0.0)),
    (1.8, dict(fill0=1.0)),
    (2.6, dict(l_slot=1.0)),
    (5.0, dict(l_slot=1.0)),
    (5.8, dict(l_slot=0.0)),
    (6.6, dict(stack=1.0)),
    (7.4, dict(r1=1.0)),
    (8.8, dict(f1=1.0)),
    (9.6, dict(r2=1.0)),
    (11.0, dict(f2=1.0)),
    (11.8, dict(l_none=1.0)),
    (13.6, dict(l_none=1.0)),
    (14.2, dict(l_none=0.0)),
    (14.6, dict(t=1.0)),
    (16.0, dict()),
]


# --------------------------------------------------------------------------- #
# a capsule over an intact O-antigen
# --------------------------------------------------------------------------- #

def draw_masking(ax, s):
    top = envelope_base(ax)
    sugar_layer(ax, top)
    # the capsule descends onto the chain tops rather than appearing over them
    capsule(ax, 22.0 + 10 * (1 - s["cap_in"]), alpha=0.22 * s["cap"])
    arrow(ax, 88, 20, 56, 17, colour=TEAL, curve=0.22, alpha=s["l_oag"],
          draw=s["l_oag"])
    label(ax, 90, 20, "Cycle 2 said the receptor\nis this sugar", TEAL,
          alpha=s["l_oag"])
    if s["dot"] > 0.01:
        ax.add_patch(Circle((43, 23.4), 2.0 * min(1.0, s["dot"] * 1.3), color=RUST,
                            lw=0, zorder=6, alpha=min(1.0, s["dot"] * 2)))
    arrow(ax, 88, 30, 48, 25, curve=0.22, alpha=s["l_mut"], draw=s["l_mut"])
    label(ax, 90, 30, "Cycle 4 found the one\nmutation up here", RUST,
          alpha=s["l_mut"])
    tag(ax, 43, 40, "both can be true at once", INK, size=21, alpha=s["t"],
        rule=s["t"])
    label(ax, 90, 18, "a capsule lies over\nan O-antigen that is\nstill intact", INK,
          alpha=s["l_both"])


KEYS_MASKING = [
    (0.0, dict(cap=0.0, cap_in=0.0, dot=0.0, l_oag=0.0, l_mut=0.0, t=0.0,
               l_both=0.0)),
    (1.0, dict(l_oag=1.0)),
    (3.4, dict(l_oag=1.0)),
    (4.0, dict(l_oag=0.0)),
    (5.4, dict(cap=1.0, cap_in=1.0)),
    (6.2, dict(dot=1.0, l_mut=1.0)),
    (8.6, dict(l_mut=1.0)),
    (9.2, dict(l_mut=0.0)),
    (9.8, dict(t=1.0)),
    (11.2, dict(l_both=1.0)),
    (12.8, dict()),
]


# --------------------------------------------------------------------------- #
# walking back up the tree
# --------------------------------------------------------------------------- #

TIPS = [(62, 6 + i * 6.2) for i in range(7)]
NODES = [(48, 15.4), (40, 21.6), (30, 27.8)]
NODE_LABELS = ("Node 1", "Node 40", "Node 281")


def draw_tree(ax, s):
    for x, y in TIPS:
        ax.add_patch(Circle((x, y), 1.0, color="#BBD3CF", lw=0, zorder=5))
        ax.plot([x, 48], [y, y], color="#D6DEDC", lw=2.2, zorder=3)
    ax.plot([48, 48], [TIPS[0][1], TIPS[-1][1]], color="#D6DEDC", lw=2.2, zorder=3)
    walk = s["walk"]                       # 0..3, continuous
    for i, (x, y) in enumerate(NODES):
        on = min(1.0, max(0.0, walk - i))
        px, py = (NODES[i - 1][0], NODES[i - 1][1]) if i else (48, y)
        ax.plot([px, px + (x - px) * on], [py, py + (y - py) * on],
                color=TEAL, lw=3.0, zorder=3, alpha=min(1.0, on * 3))
        ax.plot([px, x], [py, y], color="#D6DEDC", lw=2.2, zorder=2)
        ax.add_patch(Circle((x, y), 1.3 + 0.6 * on,
                            color=TEAL if on > 0.5 else "#D6DEDC", lw=0, zorder=5))
    label(ax, 68, 42, "present-day relatives", MUTED, size=15, alpha=s["l_tips"])
    arrow(ax, 88, 20, 64, 20, colour=TEAL, curve=0.2, alpha=s["l_today"],
          draw=s["l_today"])
    label(ax, 90, 20, "the enzyme Φ8 carries today", TEAL, alpha=s["l_today"])
    for i, (x, y) in enumerate(NODES):
        a = s[f"n{i}"]
        arrow(ax, 88, y + 6, x + 3, y + 1, colour=TEAL, curve=0.22, alpha=a, draw=a)
        label(ax, 90, y + 6, f"{NODE_LABELS[i]} — reconstructed", TEAL, alpha=a)
    tag(ax, 42, 44, "three sequences that exist nowhere in nature", TEAL, size=19,
        alpha=s["t"], rule=s["t"])


KEYS_TREE = [
    (0.0, dict(walk=0.0, l_tips=0.0, l_today=0.0, n0=0.0, n1=0.0, n2=0.0, t=0.0)),
    (0.8, dict(l_tips=1.0)),
    (1.6, dict(l_today=1.0)),
    (4.0, dict(l_today=1.0)),
    (4.6, dict(l_today=0.0)),
    (5.6, dict(walk=1.0, n0=1.0)),
    (7.6, dict(n0=1.0)),
    (8.0, dict(n0=0.0)),
    (9.0, dict(walk=2.0, n1=1.0)),
    (11.0, dict(n1=1.0)),
    (11.4, dict(n1=0.0)),
    (12.4, dict(walk=3.0, n2=1.0)),
    (14.4, dict(n2=1.0)),
    (14.8, dict(n2=0.0)),
    (15.2, dict(t=1.0)),
    (16.6, dict()),
]


# --------------------------------------------------------------------------- #
# checking a variant at read level
# --------------------------------------------------------------------------- #

def draw_reads(ax, s):
    order = [i for i in range(17) if i != 8]
    for i in range(17):
        x = 8 + i * 4.2
        if i == 8:
            ax.add_patch(FancyBboxPatch((x, 24), 3.0, 3.0,
                                        boxstyle="round,pad=0.04,rounding_size=0.5",
                                        facecolor="#E3CDBE", edgecolor="none",
                                        zorder=4))
            col, a = RUST, s["keep"]
        else:
            k = order.index(i)
            gone = min(1.0, max(0.0, (s["filter"] * 17 - k) / 1.6))
            col, a = "#E3CDBE", 1.0
            if gone > 0.01:
                ax.add_patch(FancyBboxPatch((x, 24), 3.0, 3.0,
                                            boxstyle="round,pad=0.04,rounding_size=0.5",
                                            facecolor="#EDEFEE", edgecolor="none",
                                            zorder=3))
                a = 1 - gone
        if a > 0.01:
            ax.add_patch(FancyBboxPatch((x, 24), 3.0, 3.0,
                                        boxstyle="round,pad=0.04,rounding_size=0.5",
                                        facecolor=col, edgecolor="none", zorder=4,
                                        alpha=a))
    label(ax, 8, 33, "candidate differences", MUTED, size=15, alpha=s["l_head"])
    label(ax, 90, 26, "17 sites differ between\nthe assemblies", MUTED,
          alpha=s["l_17"])
    arrow(ax, 88, 16, 44, 22, curve=0.22, alpha=s["l_reads"], draw=s["l_reads"])
    label(ax, 90, 16, "every one taken back\nto the raw reads", INK,
          alpha=s["l_reads"])


KEYS_READS = [
    (0.0, dict(filter=0.0, keep=0.0, l_head=0.0, l_17=0.0, l_reads=0.0)),
    (0.8, dict(l_head=1.0)),
    (1.6, dict(l_17=1.0)),
    (3.8, dict(l_17=1.0)),
    (4.4, dict(l_17=0.0)),
    (4.8, dict(l_reads=1.0)),
    (8.0, dict(filter=1.0)),
    (8.6, dict(keep=1.0)),
    (10.0, dict()),
]


SUPPORT = (("mutant reads", 263 / 264, RUST), ("parent reads", 0.0, MUTED),
           ("other pick", 0.0, MUTED))


def draw_support(ax, s):
    grow = fan(3, s["grow"], step=0.2, span=0.5)
    for i, (lab, frac, col) in enumerate(SUPPORT):
        y = 36 - i * 11
        g = grow[i]
        ax.add_patch(FancyBboxPatch((10, y - 2.2), 52, 4.4,
                                    boxstyle="round,pad=0.05,rounding_size=1.1",
                                    facecolor="#EDEFEE", edgecolor="none", zorder=3,
                                    alpha=min(1.0, g * 3)))
        if frac and g > 0.02:
            ax.add_patch(FancyBboxPatch((10, y - 2.2), 52 * frac * g, 4.4,
                                        boxstyle="round,pad=0.05,rounding_size=1.1",
                                        facecolor=col, edgecolor="none", zorder=4))
        label(ax, 10, y + 5.0, lab, MUTED, size=15, alpha=min(1.0, g * 3))
        label(ax, 64, y, "263 of 264" if frac else "0", col if frac else MUTED,
              size=17, weight="bold" if frac else "normal",
              alpha=max(0.0, (g - 0.75) * 4))
    tag(ax, 40, 4, "one mutation survives", RUST, size=20, alpha=s["t"],
        rule=s["t"])


KEYS_SUPPORT = [
    (0.0, dict(grow=0.0, t=0.0)),
    (3.0, dict(grow=1.0)),
    (4.0, dict(t=1.0)),
    (5.4, dict()),
]


SCENES = {
    "nickel-column": (draw_column, KEYS_COLUMN),
    "nickel-dotblot": (draw_dotblot, KEYS_DOTBLOT),
    "indistinguishable-cases": (draw_cases, KEYS_CASES),
    "indistinguishable-dotblot": (draw_splits, KEYS_SPLITS),
    "cassette": (draw_cassette, KEYS_CASSETTE),
    "masking": (draw_masking, KEYS_MASKING),
    "tree": (draw_tree, KEYS_TREE),
    "reads-filter": (draw_reads, KEYS_READS),
    "reads-support": (draw_support, KEYS_SUPPORT),
}
