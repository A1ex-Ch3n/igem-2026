"""How a phage gets through the sugar, and where host range is decided.

Picture first: each frame carries only short labels on the drawing, and the
prose that summarises the mechanism goes on a slide of its own after the build.

    python code/1025_presentation_deck/anim_adsorption.py
"""
from anim_style import (GUTTER_X, INK, MUTED, PURPLE, RUST, TEAL, arrow, canvas,
                        capsule, envelope_base, label, phage, save, sugar_layer, tag)

SUB = "adsorption"


def frames():
    made = []

    # 1 — the surface on its own
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top)
    capsule(ax, 22.0)
    label(ax, 90, 24.5, "capsule", RUST)
    label(ax, 90, 16.5, "O-antigen", TEAL)
    label(ax, 90, 5.6, "membrane", MUTED)
    made.append(("01-surface", fig))

    # 2 — a phage arrives
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top)
    capsule(ax, 22.0)
    phage(ax, 43, 47)
    made.append(("02-arrive", fig))

    # 3 — what it actually touches
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top)
    capsule(ax, 22.0)
    phage(ax, 43, 42)
    arrow(ax, 89, 31, 49, 27.5, curve=0.22)
    label(ax, 90, 31, "the spike meets sugar,\nnot a protein", RUST)
    made.append(("03-contact", fig))

    # 4 — the spike is an enzyme
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top, gap=43)
    capsule(ax, 22.0, gap=43)
    phage(ax, 43, 34)
    arrow(ax, 88, 26, 48, 19, colour=TEAL, curve=-0.3)
    label(ax, 90, 26, "it is an enzyme —\nit digests a channel", TEAL)
    made.append(("04-cut", fig))

    # 5 — down to the membrane
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top, gap=43)
    capsule(ax, 22.0, gap=43)
    phage(ax, 43, 27)
    arrow(ax, 89, 12, 50, 11, colour=TEAL, curve=0.2)
    label(ax, 90, 12, "now it reaches\nthe membrane", TEAL)
    made.append(("05-reach", fig))

    # 6 — and in goes the DNA
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top, gap=43)
    capsule(ax, 22.0, gap=43)
    phage(ax, 43, 27, dna=9)
    arrow(ax, 89, 7, 50, 5, colour=INK, curve=0.2)
    label(ax, 90, 7, "and injects", INK)
    made.append(("06-inject", fig))

    # 7 — the same phage on a sugar it cannot cut
    fig, ax = canvas()
    top = envelope_base(ax)
    sugar_layer(ax, top, n=10, colour=PURPLE, length=6.0, branched=True, seed=11)
    phage(ax, 43, 34)
    tag(ax, 17, 39, "no cut")
    arrow(ax, 22, 36, 39, 21.5, curve=-0.28)
    arrow(ax, 88, 17, 56, 19, curve=0.22)
    label(ax, 90, 18, "a sugar this enzyme\ncannot digest", RUST)
    made.append(("07-other-strain", fig))

    for name, fig in made:
        print(save(fig, name, SUB).name)
    return len(made)


if __name__ == "__main__":
    print(f"{frames()} frames")
