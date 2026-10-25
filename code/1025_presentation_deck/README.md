# Presentation deck

Three scripts, run in this order:

```
python code/1025_presentation_deck/anim_adsorption.py   # 7 frames
python code/1025_presentation_deck/anim_method.py       # 19 frames
python code/1025_presentation_deck/anim_bench.py        # 25 frames
python code/1025_presentation_deck/prep_figs.py         # 16 figures
python code/1025_presentation_deck/build_deck.py        # the .pptx
```

Everything lands in `code/output/1025_presentation_deck/`; the deck is written to
`documents/2026-10-25_presentation_deck.pptx`. Needs `python-pptx`
(`python -m pip install python-pptx`) and the `igem2026` env.

## Why the diagrams are rendered rather than drawn in PowerPoint

Nothing here can render a .pptx, so a layout written directly in PowerPoint
shapes is arithmetic that nobody has looked at — which is how the first version
ended up with overlapping text. Matplotlib output can be looked at before it goes
anywhere, so each mechanism is a frame sequence that is checked, then placed.

A mechanism slide therefore carries one image and one short eyebrow label and
nothing else. The prose that summarises the mechanism waits for a slide of its
own, after the build has run.

`build_deck.py` also estimates, for every text box, how many wrapped lines its
text needs against the box height. That check is the reason the prose columns
are 16pt and the card bodies 13pt.

## anim_style.py

The whole drawing vocabulary: palette, line weight, and the primitives for a
membrane, a sugar chain, a capsule, a phage, a protein blob, a curved pointer
and a label. Every animation imports it, so they cannot drift apart. Chains lean
and curve from a seeded sway, bands are feathered with no hard ends, the capsule
lies over the chain tops in three soft passes, and outlines are a dark teal
rather than black.

## The builds

| folder | frames | what it explains |
|---|---|---|
| `adsorption` | 7 | how a phage gets through the sugar, and where host range is decided |
| `wheel` | 4 | the DBTL loop, one lap lit, returning at every act |
| `interface` | 6 | why an interface score has no co-evolutionary record to read |
| `screen` | 5 | the 7,182-pair screen and the control gate that retired it |
| `rung` | 4 | how a backbone hydrogen-bond period names a fold, with no database |
| `nickel` | 5 | the column failing at capture rather than at expression |
| `indistinguishable` | 4 | three outcomes a gel cannot tell apart, and the assay that can |
| `cassette` | 5 | one genomic slot, three unrelated cargoes |
| `masking` | 3 | a capsule lying over an O-antigen that is still intact |
| `tree` | 5 | walking back up the tree to the reconstructed nodes |
| `reads` | 3 | seventeen candidate variants filtered to one at read level |

Movement between the frames of a build is a Morph transition; shapes that should
tween share a `!!`-prefixed name. 39 slides carry one.

## Log

- 2026-10-25 — rebuilt picture-first: 85 slides, 51 rendered frames, 0 estimated
  text overflows, narration on 82 slides
