"""Moving version of the infection mechanism.

The phage descends, the channel is digested open under it, the genome goes in.
Everything is a function of time; nothing cross-fades between finished pictures.
"""
from anim_style import (INK, MUTED, PURPLE, RUST, TEAL, arrow, canvas, capsule,
                        envelope_base, label, phage, sugar_layer, tag)


def draw(ax, s):
    top = envelope_base(ax)
    sugar_layer(ax, top, gap=43, gap_w=s["gap"])
    capsule(ax, 22.0, gap=43, gap_w=s["gap"], alpha=0.22 * s["cap"])

    label(ax, 90, 24.5, "capsule", RUST, alpha=s["l_cap"])
    label(ax, 90, 16.5, "O-antigen", TEAL, alpha=s["l_oag"])
    label(ax, 90, 5.6, "membrane", MUTED, alpha=s["l_mem"])

    phage(ax, 43, s["ph_y"], dna=s["dna"], alpha=s["ph"])

    arrow(ax, 89, 31, 49, 27.5, curve=0.22, alpha=s["a_touch"], draw=s["a_touch"])
    label(ax, 90, 31, "the spike meets sugar,\nnot a protein", RUST,
          alpha=s["a_touch"])

    arrow(ax, 88, 26, 48, 19, colour=TEAL, curve=-0.3, alpha=s["a_cut"],
          draw=s["a_cut"])
    label(ax, 90, 26, "it is an enzyme —\nit digests a channel", TEAL,
          alpha=s["a_cut"])

    arrow(ax, 89, 12, 50, 11, colour=TEAL, curve=0.2, alpha=s["a_reach"],
          draw=s["a_reach"])
    label(ax, 90, 12, "now it reaches\nthe membrane", TEAL, alpha=s["a_reach"])

    arrow(ax, 89, 7, 50, 5, colour=INK, curve=0.2, alpha=s["a_inject"],
          draw=s["a_inject"])
    label(ax, 90, 7, "and injects", INK, alpha=s["a_inject"])


ZERO = dict(gap=0.0, cap=0.0, ph=0.0, ph_y=52.0, dna=0.0,
            l_cap=0.0, l_oag=0.0, l_mem=0.0,
            a_touch=0.0, a_cut=0.0, a_reach=0.0, a_inject=0.0)

KEYS = [
    (0.0, ZERO),
    (0.8, dict(cap=0.0, l_mem=0.0)),
    (1.8, dict(l_oag=1.0)),
    (2.6, dict(cap=1.0, l_cap=1.0)),
    (3.4, dict(l_mem=1.0)),
    (4.6, dict()),
    (5.4, dict(l_cap=0.0, l_oag=0.0, l_mem=0.0)),
    (5.6, dict(ph=1.0, ph_y=51.0)),
    (7.0, dict(ph_y=42.0)),
    (8.2, dict(a_touch=1.0)),
    (10.6, dict(a_touch=1.0)),
    (11.0, dict(a_touch=0.0)),
    (11.2, dict(a_cut=1.0)),
    (13.6, dict(gap=7.5, ph_y=34.0)),
    (14.6, dict(a_cut=1.0)),
    (15.0, dict(a_cut=0.0)),
    (16.2, dict(ph_y=27.0, a_reach=1.0)),
    (18.4, dict(a_reach=1.0)),
    (18.8, dict(a_reach=0.0)),
    (19.0, dict(a_inject=1.0)),
    (20.6, dict(dna=9.0)),
    (21.6, dict()),
]


# --------------------------------------------------------------------------- #
# the same phage on a sugar it cannot cut — a separate clip, a separate beat
# --------------------------------------------------------------------------- #

def draw_other(ax, s):
    top = envelope_base(ax)
    sugar_layer(ax, top, n=10, colour=PURPLE, length=6.0, branched=True, seed=11)
    phage(ax, 43, s["ph_y"], alpha=s["ph"])
    tag(ax, 17, 39, "no cut", alpha=s["t_nocut"], rule=s["t_nocut"])
    arrow(ax, 22, 36, 39, 21.5, curve=-0.28, alpha=s["t_nocut"], draw=s["t_nocut"])
    arrow(ax, 88, 17, 56, 19, curve=0.22, alpha=s["l_why"], draw=s["l_why"])
    label(ax, 90, 18, "a sugar this enzyme\ncannot digest", RUST, alpha=s["l_why"])


KEYS_OTHER = [
    (0.0, dict(ph=0.0, ph_y=50.0, t_nocut=0.0, l_why=0.0)),
    (0.6, dict(ph=1.0, ph_y=49.0)),
    (2.2, dict(ph_y=34.0)),
    (2.9, dict(ph_y=35.4)),
    (3.4, dict(ph_y=34.0)),
    (3.9, dict(ph_y=35.2)),
    (4.4, dict(ph_y=34.4)),
    (5.2, dict(t_nocut=1.0)),
    (7.0, dict(l_why=1.0)),
    (8.4, dict()),
]

SCENES = {
    "adsorption": (draw, KEYS),
    "adsorption-other-strain": (draw_other, KEYS_OTHER),
}
