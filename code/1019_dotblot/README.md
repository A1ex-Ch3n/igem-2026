# 1019_dotblot — spot intensities for the His-tag dot blot

Measures the eleven spots on the 2026-10-19 dot blot so the entry's intensity table is measured
rather than eyeballed.

- Input: [`data/assays/1019_dotblot/dotblot.jpeg`](../../data/assays/1019_dotblot/dotblot.jpeg)
- Outputs: [`output/1019_dotblot/spot_intensities.tsv`](../output/1019_dotblot/spot_intensities.tsv)
  and [`fig_dotblot_annotated.png`](../output/1019_dotblot/fig_dotblot_annotated.png) / `.pdf`
- Write-up: [`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`](../../lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md)

```
python code/1019_dotblot/quantify_dotblot.py     # measure, write the TSV
python code/1019_dotblot/annotate_dotblot.py     # the annotated two-panel figure
```

Needs only NumPy, SciPy and Pillow — all in the `igem2026` env.

## Method, and what the numbers do and do not mean

For each spot the script takes the mean luminance of an 18 px disc and subtracts it from the
median of a surrounding annulus (26–42 px), giving a local **darkness**. A local background is
used per spot because the membrane is wet and unevenly lit — the right-hand side carries a
specular glare that a single global background would smear across every reading.

Grid positions were read off the photograph by eye, so each spot is allowed to **re-centre on the
darkest disc within ±25 px** of its nominal position before being measured. The `dx`/`dy` columns
record how far each one moved. A spot whose search **hits the edge of that box** has not been
found — the search has only run downhill — so it falls back to the nominal position rather than
measuring somewhere else entirely; those are the positions reported at ~0 and called "nothing
there". `CDS12−` is a hollow drying ring whose centre had to be located by eye (261, 730); the
disc average there samples part of the rim, which is why the negative control reads 3.9 rather
than 0, and why it is used as the noise floor.

`annotate_dotblot.py` marks **every** spotted position, developed or not, and colours a spot as a
call only at **2x the negative control** (`POS_FACTOR`). That rule is what keeps `CDS12+` at 1.1x
out of the result.

**These values are relative to this one image.** There is no ladder, no standard and no loading
normalisation, so they support one comparison only: each spot against the negative control on the
same membrane. They are not concentrations, and intensities are not comparable between different
constructs.

The grid in `SPOTS` is hard-coded and assumes the orientation of `dotblot.jpeg` as supplied. If
the image is ever recropped or rotated, the coordinates must be redone.

---
*Log — 2026-10-19: written for the final bench day before the iGEM freeze. Spot identities come
from the hand-drawn layout sheet; the membrane-to-sheet orientation and the row-3 assignment were
confirmed with Alex, not inferred from the image. UNDONE: nothing here reads the `dotblot_label.jpeg`
sheet programmatically — the layout was transcribed by hand.*
