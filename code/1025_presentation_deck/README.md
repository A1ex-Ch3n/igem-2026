# Presentation deck

`build_deck.py` writes `documents/2026-10-25_presentation_deck.pptx` — 56 slides,
16:9, built from the narration in `documents/2026-10-25_presentation_video_script.md`.
Every slide carries its narration in the speaker notes.

Run it with the `igem2026` env, after `python -m pip install python-pptx`:

```
python code/1025_presentation_deck/build_deck.py
```

## Where the pictures come from

The script reads already-prepared PNGs from a scratch folder rather than the repo
directly, so re-running it needs that folder repopulated. The sources are:

| key | repo path |
|---|---|
| `trimer`, `body-side`, `body-axial`, `gh5` | `code/output/0729_prof_figures/panels/` |
| `anc-wt`, `anc-n1`, `anc-n40`, `anc-n281`, `anc-overlay`, `virion`, `cds10` | `code/output/1018_construct_structures/panels/` |
| `controls` | `documents/2026-07-13_binding_controls_comparison.png` |
| `oantigen`, `clusters` | `code/output/0727_o_antigen_comparison/` |
| `zymctrl` | `code/output/1020_zymctrl_figure/fig_zymctrl_perplexity.png` |
| `gel0929`, `gel1010` | `code/output/0929_gel_annotation/`, `code/output/1010_gel_annotation/` |
| `dotblot`, `spottest`, `mutation` | `code/output/1019_dotblot/`, `1016_spot_test_result/`, `1010_resistant_mutant_comparison/` |
| `phagemap`, `bactgenomes`, `folds` | `code/output/0729_prof_figures/`, `code/output/0712_phage_rbp_detect/structure/` |

Each is thumbnailed to 1800 px on its long edge and saved as PNG.

## How the animation works

There are no PowerPoint entrance animations. Movement comes from **Morph
transitions** between near-identical slides: a build is a short run of slides,
shapes that should tween carry the same `!!`-prefixed name, and PowerPoint
interpolates between them. That survives export to video and PDF better than a
timing tree, and it is editable by hand afterwards.

Seven builds use it — the bacterial envelope, the screen funnel, the control
scores, the tail-spike strip-down, the two enzymes, the ancestral panel, and the
capsule masking an intact O-antigen.

## Log

- 2026-10-25 — first build, 56 slides
