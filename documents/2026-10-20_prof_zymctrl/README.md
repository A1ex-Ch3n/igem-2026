# ZymCTRL perplexity — the PI's data, and what it says

Received from Prof. Espinoza on **2026-10-20**, answering the four questions in
`2026-10-20_engineering_number_consistency.md`'s sibling email.

| File | What |
|---|---|
| `perp.csv` | **997 reconstructed nodes x 24 glycoside-hydrolase EC classes.** Values are ZymCTRL **perplexity** (his answer to Q1). Column order is the x-axis order of his figure |
| `panelD.jpeg` | his original panel D. Pink cloud = all nodes; red circles = the nine on the CDS_0012 -> root path, shaded light (Node1) to dark (Node281) |
| `seaview_curated_alignment.jpeg` | the curated MUSCLE alignment in SeaView — evidence for the "manually curated" step |
| `tree_ultrametric.svg` | the PhyML tree drawn ultrametric (tips aligned). **CDS_0012 is the red mark**; the nine reconstructed nodes are the internal nodes on the path from it to the centre. The PI's preferred version: "the ultrametric is cleaner" |
| `tree_phylogram.svg` | the same tree with branch lengths, scale bar 0.1 substitutions/site. More informative, harder to read at 997 tips |

His answers, verbatim in substance:

1. **y axis = perplexity.**
2. **EC labels** are `3.2.1.XX` where XX is the number on the figure. The notebook we
   were sent is a later day's version with the EC list swapped, which is why its
   `--ec` list and the figure disagree. `perp.csv` is the figure's own data.
3. **The cloud is all nodes; the highlighted points are the CDS_0012 -> root path.**
4. **Raster only** — no vector original.

## What the numbers say

Recomputed from `perp.csv` by `code/1020_zymctrl_figure/plot_perplexity.py`.

**Across EC classes, the scan discriminates, and it picks the right chemistry.**

| EC | median perplexity over all 997 nodes |
|---|---|
| **3.2.1.4** (endoglucanase) | **8.61** |
| **3.2.1.123** | **9.03** |
| 3.2.1.164 | 14.11 |
| 3.2.1.91 | 14.23 |
| ... | ... |
| 3.2.1.25 (worst) | 17.51 |

3.2.1.4 is cellulase/endo-1,4-beta-glucanase — the activity the GH5 assignment and
all four AlphaFold3 templates (1ECE with cellotetraose bound, 1VRX, 4TUF, 2ZUM)
point at. The model was given no structure and no annotation, only sequence.

**Along the ancestry path, perplexity falls monotonically.** Under 3.2.1.4,
Node1 11.55 -> Node281 **6.81**, a drop of 4.74, Spearman rho **-0.983** against
the recent-to-ancestral order.

**The control that stops this being an overclaim.** The same monotonic direction
appears in 11 of the 24 classes, which is what the PI's own caveat predicts —
reconstructed ancestors are consensus-like by construction, and a more averaged
sequence scores better under almost any label. What separates signal from that
artefact is magnitude: the fall is **4.74 units in 3.2.1.4 and 4.03 in 3.2.1.123,
but under 1 unit in every other class**, and two classes even run the other way.

A second check, same conclusion: the nine path nodes sit at the 12th-22nd
percentile of the cloud in *every* EC, so "the path is low" is a general property
of those sequences. "The path is low *specifically under the cellulase label*" is
not — that is where the cloud itself collapses from ~17 to ~8.6.

**What it still does not say.** Perplexity ~7 is far above the 1.75 the model card
calls decent, so this is a relative statement across labels, not an absolute
claim that these are good endoglucanases. And perplexity is not activity: nothing
here measures substrate range, which is what the wet-lab panel exists to test.

## Correction to an earlier reading

On 2026-10-19 this repository recorded that the ZymCTRL scan "did not
discriminate", from the log-likelihood ratios in `EC_Scoring.ipynb`'s stored
output, which are ~0 across the nodes. That reading was wrong in scope: those
ratios compare one EC against decoys *within a single run*, and the discrimination
in this analysis is **across EC labels**, which the notebook's stored output does
not show. `code/1018_prof_asr_zymctrl/README.md` has been corrected.

## Rendering the trees

Both arrived as SVG from iTOL, 1914x915 with ~1,000 tip labels and roughly 2 MB each.
Inlining either into a wiki page would be unreasonable, so
`code/1020_zymctrl_figure/render_trees.py` rasterises them at 2x with cairosvg,
crops the surrounding whitespace, and labels the red mark as CDS_0012 — without
which the one thing the figure is for is a 4-pixel dash.

The wiki uses the **ultrametric** one, per the PI's preference. The phylogram is kept
here because it is the version that carries branch lengths.

---
*Log — 2026-10-20: received, verified against `perp.csv`, figure rebuilt as vector,
trees rasterised and annotated.*
