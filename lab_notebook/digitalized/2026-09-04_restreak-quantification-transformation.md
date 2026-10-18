---
date: 2026-09-04
notebook_pages:
  - p86
  - p87
  - p88
authors:
  - Olivia
  - Alex
  - Carol
title: Construct Re-streaking, Plasmid Quantification & Transformation into BL21
---

# Construct Re-streaking, Plasmid Quantification & Transformation into BL21

**Source pages:** ![p86](images/p86.jpg) ![p87](images/p87.jpg) ![p88](images/p88.jpg)

> [!note] Photo legibility
> All three pages are legible. p88 carries the **transformation protocol** as a standalone
> numbered list with no date header — it sits between the 9/4 results (p.87) and the 9/6 entry (p.89),
> and the 9/4 objective list names transformation as step 3, so it is filed here.

## Objective & procedure (p86)
1. **Re-streaking of Ⓚ `CDS10 WT xAG`**, stored in the incubator upside down.
2. **Quantification of plasmids from yesterday.**
3. **Transformation.**

## Experiment notes — quantification (p86)
- `5 samples + 6 standards + 2 extra = 13` µL of **Ⓐ**
- `13 × 200 = 2600 µL` of component **Ⓑ**
- **We are using 5 µL per sample in quantification.**
- Plate layout: **row 1** = standards `0 1 3 10 30 100`; **row 3** = `e1, e40, e281, CDS11, CDS12`.
- `50 µL − 5 µL = 45 µL left in each.`

## Results — quantification, 5 µL (p87)
*"blue"* written over a struck-through *"green"* — i.e. the **blue** (dsDNA high-sensitivity) reagent.

| Standard | RFU | | Sample | RFU |
|---|---|---|---|---|
| S0 | 143.23 | | e1 | 339.87 |
| S1 | 238.53 | | e40 | 274.75 |
| S3 | 439.12 | | e281 | 325.10 |
| S10 | 917.66 | | CDS11 | 337.19 |
| S30 | 2924.99 | | CDS12 | 312.05 |
| S100 | 7346.87 | | | |

These are the readings analysed in [`code/0904_quantification.ipynb`](../../code/0904_quantification.ipynb)
(LOWEND S0/S1/S3 fit, no volume correction — standards were loaded at 5 µL too).

## Transformation protocol (p88)
1. **Thaw cells (BL21) and SOC on ice until the last crystal disappears**, from −80 °C.
2. **Add 50 µL cells + 5 µL DNA plasmid** to a new EP tube and label correspondingly
   *(we have 5, plus 1 control from cells only)*. **Flick the tube wall 4–5 times, NO VORTEX.**
3. **Let the 6 EP tubes sit on ice for 30 min.**
4. **Heat shock at 42 °C for EXACTLY 10 s** (pre-set the smaller water bath to 42 °C).
5. **Add 950 µL room-temperature SOC to each tube.**
6. **Incubate the 6 tubes at 37 °C for 60 min; flick occasionally.**
7. **Pipette 100 µL from one tube to a Ⓚ plate**; use an "L" shape to spread the cell solution evenly,
   **3 angles, 5 times each**. **This step MUST be done in a clean area** (vacuum under the Bunsen burner).
8. **Incubate 5 × 8 + 3 CTs at 30 °C overnight.**

## Notes / continuity
Step 8's "5 × 8" = the five constructs × eight plates each; "3 CTs" = three control plates.
The plate readout is on **p.89 (9/6)**: ~43 plates grew, one `e40` plate had fungus.

## Checklist — where do the outputs go?
- [x] `CDS10 WT xAG` re-streaked → **incubator, inverted**.
- [x] Plasmid quantification done (5 µL per sample; 45 µL left per tube).
- [x] 5 constructs + 1 cells-only control transformed into **BL21** → **30 °C overnight**.

## Open items
- `==CONFIRM: step 7's "3 angles, 5 times each" — the second digit is written like "[" in the photo.==`
- `==CONFIRM: the identity of the "2 extra" wells in the 13-reaction count.==`

## Source
- Lab notebook: p.86–p.88 (this entry).
- Analysis: [`code/0904_quantification.ipynb`](../../code/0904_quantification.ipynb).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6580.JPG`→`p86.jpg`,
  `IMG_6581.JPG`→`p87.jpg`, `IMG_6582.JPG`→`p88.jpg`. The p.86–p.87 readings were already
  transcribed into `code/0904_quantification.ipynb` on 2026-09-04; this entry is the page-level record.
