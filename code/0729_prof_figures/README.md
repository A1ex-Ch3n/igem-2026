# 0729 — figures for the PI's questions 3, 4 and 6

Three of the seven items in Prof. Espinoza's 2026-07-27 email were figure work
where the underlying data already existed. This directory produces them.

Status after this run: **Q3, Q4, Q6 done**. Q7 was answered separately in
[`../0727_o_antigen_comparison/`](../0727_o_antigen_comparison/); Q1 is
[`documents/2026-07-28_results_synthesis.qmd`](../../documents/2026-07-28_results_synthesis.qmd).

```bash
conda activate igem2026
python code/0729_prof_figures/plot_bacterial_genomes.py     # Q3
python code/0729_prof_figures/plot_phage_genome_map.py      # Q4
python code/0729_prof_figures/render_enzymatic_domains.py   # Q6
```

Outputs → [`../output/0729_prof_figures/`](../output/0729_prof_figures/);
individual PyMOL / pyCirclize renders land in `output/.../panels/`.

## Q3 — `fig_bacterial_genomes.{png,svg}`

> *Prepare a diagram of the bacterial genomes we sequenced.*

Three circular maps, **one per ANI-distinct strain, not per isolate**. We
sequenced five isolates but they collapse to three strains
([`../0627_unique_strain_table.ipynb`](../0627_unique_strain_table.ipynb)) —
drawing 9-2-1 and 9-6-2 separately would be drawing the same genome twice
(100.000% ANI).

Rings, outside in: O-antigen cassette (red), CDS forward, CDS reverse, GC
content deviation, GC skew. The GC-skew polarity flips cleanly near the
terminus in all three, which is what a correctly closed assembly should look
like.

Marking the O-antigen cassette is deliberate — it is what connects this figure
to the Q7 result (same syntenic slot, different cargo in each strain).

⚠️ **CDS counts come from Bakta's summary `.txt`, not from counting CDS features
in the `.gbff`.** Bakta writes its 4 sORFs as `CDS` features but reports them
separately, so a naive feature count reads exactly 4 high in every genome
(5,268 vs 5,264 for 8-5-2, etc.) and would not match the MRA.

## Q4 — `fig_phage_genome_map.{png,svg}` + `fig_phage_tail_module.{png,svg}`

> *Create a genome map of our phage highlighting the structural proteins,
> particularly the tail spike protein.*

Drawn from **Prof. Espinoza's Pharokka run on the canonical `Version_1`
assembly** (62,416 bp, `UUAIURNK_` numbering), coloured with Pharokka's own
PHROG category colours. The tail spike (`CDS_0011`) is outlined in red.

⚠️ **This supersedes `code/output/0708_phage_genome_analysis/fig2_genome_map.png`**,
which was drawn on our reverse-complemented + rotated 62,338 bp frame with the
deprecated `FHABPWTM_` numbers — its module order is **mirrored**. Do not reuse
the old one.

A second panel zooms on the tail / RBP cluster (`CDS_0008–0012`), the module the
PI is cloning.

Two labels are **ours, not Pharokka's**, and are marked with † in the figure:

| CDS | Pharokka says | we say | evidence |
|---|---|---|---|
| `CDS_0012` | hypothetical protein | GH5 glycoside hydrolase | 4/4 AF3 templates are GH5 endoglucanases |
| `CDS_0024` | hypothetical protein | β-helix depolymerase | RBP Detect 0.998 + H-bond rung period 22–24 |

## Q6 — `fig_enzymatic_domains.{png,svg}`

> *Generate 3D models of the enzymatic domains within the tail spike protein.*

Four panels from the PI's own AlphaFold3 folds:

| panel | what |
|---|---|
| **A** | `CDS_0011` full trimer, coloured by domain — Calx-β 1–110, shaft 111–300, β-helix body 301–941, foldon 921–941 |
| **B** | the body alone (301–941) — the β-solenoid, rigid across all 5 AF3 models (RMSD 0.44–0.99 Å) |
| **C** | the same body end-on down the 3-fold axis |
| **D** | `CDS_0012` — CBM + GH5 TIM barrel, pLDDT 95–98 |

::: note
**The PI's wording is ambiguous and the figure resolves it explicitly.** He asked
for the enzymatic domains *within* the tail spike, but the **template-confirmed**
glycoside hydrolase (GH5) is `CDS_0012` — a **separate protein**, not a domain of
`CDS_0011`. Panel D is labelled as such. The enzyme genuinely inside the tail
spike is the β-helix depolymerase body in panels B and C, and its fold is called
from H-bond rung geometry, **not** from a named structural homolog — no foldseek
match has been run.
:::

`CDS_0010` is deliberately **not** drawn as an enzyme: the PI's glycosidase
assignment for it is unsupported (one weak IspD hit; ~460 aa with no template).
That remains an open question to put to him.

Panel A also shows *why* the ordered construct starts at residue 305: the
Calx-β anchor and shaft are placed differently in every AF3 model (RMSD 41–92 Å),
while the body is rigid.

## Notes on tooling

- `pyCirclize` was installed for Q3 (`python -m pip install pycirclize`).
- PyMOL runs headless via `from pymol import cmd`; hex colours must be
  registered with `cmd.set_color` first, they cannot be passed to `cmd.color`.
- `pyCirclize`'s `fill_between` needs an explicit symmetric `vmin`/`vmax` for
  values straddling zero, and its `where=` argument does not survive the
  internal interpolation — clip into two series instead.
- PyMOL centres molecules in the canvas, so each render is auto-cropped to its
  ink before tiling.

---
*Log — 2026-07-29: created. Q3 (three circular genome maps, one per ANI-distinct
strain, O-antigen cassette marked), Q4 (phage genome map on the canonical
orientation + tail-module zoom, superseding the mirrored 0708 figure), Q6
(four-panel AF3 domain figure, with the CDS_0011-vs-CDS_0012 scope ambiguity
resolved in the labels). CDS counts switched from .gbff feature counts to
Bakta's summary .txt after finding a consistent +4 sORF discrepancy.*
