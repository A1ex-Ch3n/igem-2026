---
date: 2026-09-10
notebook_pages:
  - p94
authors:
  - Rafael
  - Alex
  - Carol
title: Destaining the SDS Gel; Reviving the Liquid Cultures
---

# Destaining the SDS Gel; Reviving the Liquid Cultures

**Source page:** ![p94](images/p94.jpg)

> [!note] Photo legibility
> p94 is heavily struck through in places and the gel-lane table at the bottom is cramped, with a
> second small table sketched over the right margin. The lane assignments below carry `==CONFIRM==` marks.

## Objectives (p94)
- **Continue with the SDS gel from yesterday: destain it and take the picture under ultraviolet light.**
- **Put the liquid culture back into the incubator at 37 °C, to repeat the same process of IPTG
  induction and gel.**

## Procedure (p94)
- **For the last few destains: take 50 mL of destain solution and microwave for 30 s to boil a bit,
  add, shake a little, dry, and then to the picture.**

## Notes (p94)
- **The gel stained overnight is dry and curled; there's a slight crack on the left side of the gel,
  but no big deal.**
- **This is how the gel arranged:**

| Lane | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sample | ladder | `e1` | `e1` | `e40` | `e40` | `e281` | `e281` | `e281` | `e281` | `e281` | `e281` | ladder |
| Induction | | X | V | X | V | X | X | X | V | V | V | |
| Dilution | | | | | 1:1 | 1:1 | 1:5 | 1:10 | 1:1 | 1:5 | 1:10 | |

**Key written on the page: `X → non-induced`, `V → IPTG`.**

- **The SDS gel only shows clear bands for lanes 6 & 9** *(an "8" is struck before the "6 & 9")*,
  **so we are taking the concentration of IPTG.**
- **100 mL +**
- **Till 0.8 for OD to add IPTG.**

## Notes / continuity
This is the **first expression gel** of the project and it failed to show induction except in the two
`e281` 1:1 lanes. The response is the dilution/induction redo on 9/11 (p.95) and 9/15 (p.96) — and the
9/15 gels are the ones analysed in [`code/0915_gel_annotation.ipynb`](../../code/0915_gel_annotation.ipynb),
whose verdict is **inconclusive**.

The **"till 0.8 for OD to add IPTG"** line is the induction rule used for the rest of the block.

## Checklist — where do the outputs go?
- [x] Gel destained and photographed. `==UNDONE: no photo of this 9/10 gel is in `data/assays/`; the first archived gels are 0915.==`
- [x] Liquid cultures → back to the **37 °C incubator** for a second induction round.

## Open items
- `==CONFIRM: the lane table. Lane 2 reads like "G1" but is almost certainly `e1`; the X/V marks on lanes 4–5 and 9 are overwritten; the dilution row may start at lane 5 rather than lane 6.==`
- `==CONFIRM: "100 mL +" — the culture volume for the redo (100 mL + what?).==`
- `==CONFIRM: destain microwave time "30 s" (written over).==`

## Source
- Lab notebook: p.94 (this entry).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6588.JPG`→`p94.jpg`.
