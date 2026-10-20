# 2026-10-19 His-tag dot blot — the last bench day before the freeze

Two photographs taken 2026-10-19, supplied by Alex. Written up in
[`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`](../../../lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md).

| File | What it is |
|---|---|
| `dotblot.jpeg` | the developed membrane in a Petri dish, cut corner top-left |
| `dotblot_label.jpeg` | the hand-drawn layout sheet, circled sample names in a 4 + 4 + 3 grid |

Both are **raw photographs** — nothing is overlaid or annotated, unlike the `1001_sds_page`
composites. There is **no notebook page** for this day; the layout sheet is the only written
record.

## Layout

Read in the orientation of `dotblot.jpeg` (Alex confirmed the photograph and the sheet share an
orientation). Row 3 sits ~45 px left of rows 1–2.

|  | col 1 | col 2 | col 3 | col 4 |
|---|---|---|---|---|
| row 1 | CDS12+ (rough lysate) | CDS12+ | e1+ (rough lysate, 10/18) | e1+ |
| row 2 | e40+ (1:10) | e40+ | e281+ (1:10) | **e281 FT1** |
| row 3 | CDS12− (negative) | e1+ (1:10) | **positive control** (wide) | — |

The positive control was **borrowed from a neighbouring lab and its identity is unknown to us**,
so it validates the chemistry but is not a quantitative reference.

## What the blot shows

Quantified by [`code/1019_dotblot/quantify_dotblot.py`](../../../code/1019_dotblot/quantify_dotblot.py)
→ [`code/output/1019_dotblot/spot_intensities.tsv`](../../../code/output/1019_dotblot/spot_intensities.tsv).

The positive control is 16× the negative, so the His-tag probe and the development step both
worked. **Only two samples clear the negative control:** `e281 FT1` (2.6×) and the `e1` rough
lysate (2.2×). Everything else sits at or below `CDS12−`, which is itself a hollow drying ring
rather than signal. All four 1:10 spot-test dilutions are under detection.

The `e281 FT1` positive is the informative one: it says `e281` **was expressed and failed to bind
the Ni-NTA column**, which reframes the failed 10/10 purification
(`code/1010_gel_annotation.ipynb`) from an expression problem into a capture problem.

A dot blot reports the His tag and not the protein's size, so none of this distinguishes
full-length product from a truncation. Caveats in full — no replicate, no loading normalisation,
a run-off smear on the positive control, and still no BL21 empty-vector control anywhere in the
protein work — are in the notebook entry.
