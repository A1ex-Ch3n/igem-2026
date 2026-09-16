---
title: Lab-notebook open questions (single review list)
date: 2026-08-29
purpose: Everything in the digitized lab notebook that still needs a second check, in one place, so it can be gone through in one sitting with the physical notebook and the plates in hand.
scope: lab_notebook/digitalized/ — entries 2026-05-18 → 2026-07-16 (p.01, p.09–p.12, p.14–p.81)
sources:
  - lab_notebook/digitalized/typos.md
  - lab_notebook/digitalized/README.md
  - lab_notebook/digitalized/*.md
---

# Lab-notebook open questions

Compiled after digitizing **p.44–p.81** (2026-06-15 → 2026-07-16) on 2026-08-29. Items are grouped
by **how much depends on the answer**, not by date. `typos.md` remains the working tick-list for the
physical notebook; this document is the review agenda.

Legend: **A** = changes a scientific conclusion · **B** = changes a record other files cite ·
**C** = transcription detail, local to one entry.

---

## A. Blocking — these change what the project claims

### A1. ~~Does Φ8 plaque on `8-5-2`? (p.71 vs p.72)~~ — **ANSWERED 2026-08-29 (Alex)**

Not a conflict between two results. **The plates were not clearly readable**, so the ambiguous
strains were carried forward for **repeat testing by EOP** rather than scored from p.71/p.72 — which
is why `8-5-2` appears in the 13-strain EOP panel from [7/6](../lab_notebook/digitalized/2026-07-06_plaque-titer-and-culture.md)
onward. **Host-range calls for those strains come from the EOP series (7/8 → 7/15), not from these
two pages.**

Also settled: **`X` = *not* webbed**, and a **ditto mark carries the cell above it**. Both entries
have been updated with an expanded reading column; nothing was propagated to the synthesis documents.

**What is still open** is therefore not the transcription but the biology — see **A2**, and the fact
that the 7/15 EOP plates and 7/16 lawns have no recorded readout.

### A2. The host-range positives disappear at high dilution

`6-3-2`, `6-6-2`, `6-7-2`, `9-1-2`, `9-2-2` score **T** on the 7/4 matrix (1:3000), but the 7/8 EOP
test at **1:10⁵** lists `6-3-2`, `9-2-2`, `6-6-2` (struck) among the **"NOs"**. Then 7/14–7/16 treat
the whole **site-6 group as possible contamination or prophage**, not host range.

**Question:** as of the last bench day (7/16), what is the team's standing interpretation — real but
weak host range, or artefact? Is there a readout for the 7/15 EOP plates and the 7/16 soft lawns
that never got written down?

### A3. `8-3-1` ≈ `8-5-1` (carried over, still open)

`8-3-1` is not one of the 28 glycerol stocks; `8-5-1` is. Almost certainly a mislabelled tube.
**Verify and relabel the physical tube.** Note this now matters more: `8-5-1` appears in the 7/4
host-range matrix and the 7/8 EOP list.

---

## B. Record-level — other files cite these

### B1. `9-2-1 Φ8` phage sequencing submission date — still unrecorded
Results came back 2026-07-08; the extraction is written up on **p.64–66 (6/29)**; the submission
itself appears on **no page**. `data/dna_extraction_inventory.md` has it as `[TBD]`.

### B2. 6/22 Qubit — the **Std 100** digit
p.53 reads like **10434.66**; `code/0622_quantification.ipynb` (entered at the bench) has
**16434.66**. Only 16434.66 is consistent with the rest of the curve. Confirm.

### B3. 6/29 phage quantification — **3116.13** (page) vs **3116.15** (notebook)
One digit. Confirm which is the bench value.

### B4. `code/0710_quantification.ipynb` — now known to be misdescribed
p.77 shows the samples are **phage-resistant colonies (3 per host), pelleted and extracted 7/9** —
not the 6/05 bacterial extracts with ~90 µL remaining, and the bench date is **7/9**, not 7/10.
A dated correction note has been added to the notebook. **Also still owed: the dilute-and-re-read**,
since every sample read above the 30 ng/µL top standard.

### B5. 6/17 quantification — did it happen?
p.46 lists "quantification for 8 bacteria samples" as a goal, but no data appears on p.46/p.47 and
the next Qubit page is p.53 (6/22, 18 samples). Was it skipped and rolled into 6/22?

### B6. 6/26 — the Procedure section is blank
p.62 heads a "Procedure" for the phage harvest / genome extraction and leaves it empty; the
extraction is written up on 6/29. Was anything done on 6/26 that never got written?

### B7. Carried over from the 6/08 block (unchanged)
- p.36 blurry digits: **S0** (156.326?), **S1** (173.90 vs 173.70), **S30 label** (reads like S₅₀; value 724.52 vs 7224.52), **C1** last digit, **C8** (5655.31 vs 5455.31), **C9** (.36 vs .86).
- p.36 right-margin concentration-factor calculation; the concentrated-eluate final volume.
- p.32/33 objective sub-steps, the bead-beater / standard-curve sketches, the LB-broth volume.
- The **"mix 4 tubes into 1" pooling ratio**.

---

## C. Transcription details (one entry each)

| Where | Item |
|---|---|
| p.44 (6/15) | Header day-digit reads `2026.6.15`; confirm it is not 6.16 |
| p.45 (6/16) & p.37 (6/09) | **Centrifuge "5.0 ×g"** — the same notation on both pages, so it is the team's shorthand for the machine's setting, not a misread. Confirm the actual units (5,000 × g?) |
| p.53 (6/22) | ~~Scratch `245.5` / `280`~~ — **resolved**: the `8-5-2` dilution (245.51 ng/µL; 70 µL + 280 µL = 5× → 49.1). The `8-10-2` arithmetic (~50 target, actually ~35) is a **bench rough estimate** per Alex — recorded as written, no action |
| p.55–59 (6/24) | **No author line** on any of the five pages; also confirm the four `9-9-2` overnight readings (0.837 / 0.546 / 0.397 / 0.740) |
| p.60–61 (6/25) | **No author line**; confirm the p.61 header ratio "bac 3 : Φ 1" |
| p.62 (6/26) | Header written **`2025`-06-26** — wrong year (physical typo) |
| p.67 (6/30) | The **24 streaked strains** are not listed; confirm the set |
| p.69 (7/2) | Dilution/volume row does not line up (8 dilutions, 7 volumes; "3.3 µL" is odd); host list has `8-3-2` twice with `8-7-1` struck and `9-9-2` in the margin |
| p.72 (7/4) | Circled `Φ` before `6-7-2`/`9-6-2` and `8-1-2`/`9-2-1`; `?` on the `9-2-2` and `9-10-1` rows; margin note "#9 stronger than #8" — sites or phages? |
| p.76 (7/8) | The "NOs" list has `8-5-1` twice and three struck entries — confirm the final set |
| p.78 (7/13) | Titres written "1:20 W / 1:30 W / 1:40 W" — confirm W = thousand |
| p.16, p.18, p.19, p.20, p.24 ×2, p.27 ×3 | The nine original handwritten typos — **still all unticked** in `typos.md` |

---

## Not a question — corrections already applied in this pass

- **Bacterial DNA was normalised to 50 ng/µL before sequencing.** p.53 (6/22) reads
  *"20 µL for sequencing (~50 ng/µL)"*, which independently confirms your 2026-08-08 correction
  against the 6/08 entry's "NOT diluted" record.
- **The second bacterial sequencing submission is `8-5-2` + `8-10-2`, decided 2026-06-22**, diluted
  1:1 with water (`70 µL + 70 µL`). Assemblies returned 6/26–6/27. This was previously recorded nowhere.
- **`data/assays/0624_od600_phage.csv`** was missing the **t = 33** row (19:42 — 1.262 / 1.160 / 1.076),
  which is on p.59; added.

---

## Log
- 2026-08-29 — Created while digitizing p.44–p.81. Supersedes nothing: `typos.md` stays the
  tick-list against the physical notebook; this is the single review agenda across all 45 entries.

- 2026-08-29 — **A1 answered by Alex** (unclear plates → repeat testing by EOP; `X` = not webbed;
  dittos carry the cell above), and the p.53 `~50 ng/µL` figures confirmed as bench rough estimates.
  Entries updated. Standing instruction recorded: **digitization transcribes everything as written —
  only genuine handwriting typos are flagged.**
