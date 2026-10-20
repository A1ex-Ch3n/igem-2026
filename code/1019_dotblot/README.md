# 1019_dotblot — spot intensities for the His-tag dot blot

Measures the eleven spots on the 2026-10-19 dot blot so the entry's intensity table is measured
rather than eyeballed.

- Input: [`data/assays/1019_dotblot/dotblot.jpeg`](../../data/assays/1019_dotblot/dotblot.jpeg)
- Output: [`output/1019_dotblot/spot_intensities.tsv`](../output/1019_dotblot/spot_intensities.tsv)
- Write-up: [`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`](../../lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md)

```
python code/1019_dotblot/quantify_dotblot.py
```

Needs only NumPy, SciPy and Pillow — all in the `igem2026` env.

## Method, and what the numbers do and do not mean

For each spot the script takes the mean luminance of an 18 px disc and subtracts it from the
median of a surrounding annulus (26–42 px), giving a local **darkness**. A local background is
used per spot because the membrane is wet and unevenly lit — the right-hand side carries a
specular glare that a single global background would smear across every reading.

Grid positions were read off the photograph by eye, so each spot is allowed to **re-centre on the
darkest disc within ±25 px** of its nominal position before being measured. The `dx`/`dy` columns
record how far each one moved. Five spots drift to the full ±25 limit; that is not a measurement,
it is the search failing to find a spot, and those five are exactly the positions called "no
spot" in the entry.

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
