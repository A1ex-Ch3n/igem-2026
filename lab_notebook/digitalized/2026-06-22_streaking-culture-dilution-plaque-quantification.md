---
date: 2026-06-22
notebook_pages:
  - p52
  - p53
authors:
  - Alex
  - Olivia
title: Streaking & Culture, Phage Dilution, Plaque Assays, 18-Sample Qubit + 2nd Sequencing Submission
---

# Bacteria Streaking & Culture · Phage Dilution · Plaque Assays · Bacteria Genome Quantification

**Source pages:** ![p52](images/p52.jpg) ![p53](images/p53.jpg)

> [!important] This page closes two long-standing record gaps
> p.53 carries **"20 µL for sequencing (~50 ng/µL)"** and the decision to submit **`8-5-2`** and **`8-10-2`** — the missing second bacterial sequencing submission, and independent confirmation of the 50 ng/µL normalisation that the [2026-06-08](2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) entry had recorded as "NOT diluted". See the Log there.

> [!note] Photo legibility
> p52 is upright and legible. p53 is rotated ~90°; the numbers are legible except the **Std 100** value (see below).

## Objective (p52)
1. Make a **new round of bacteria culture** for this week.
2. **Phage plaque assay** for purified phage genome.
3. **Quantification** for bacteria genome extracts.

## Procedure (p52)

### ① Media
Made **50 mL 0.7 % soft agar**, autoclaved. See [[lb_agar]].

### ② Revive `8-7-1`
Took the **`8-7-1`** stock from the **−80 °C freezer** and streaked it on a plate. See [[revive_bacteria_from_glycerol_stock]], [[three_phase_streak]].

### ③ Culture from yesterday's streaks
From the `9-2-1` and `9-6-2` streak plates made [2026-06-21](2026-06-21_plaque-assays-dilution-streaking.md): **picked 3 isolated colonies each** and mixed into **5 mL LB broth**.

### ④ + ⑤ Plaque assays (**9 plates in total**) — see [[plaque_assay_layered_plate]], [[phage_purification]]
- For **`9-9-2` Φ8 1:2** and **`9-9-2` Φ8 1:4** (labelled **`9-9-2`** and **`9-9-2*`**) as pre-dilution: diluted **1:2, 1:4, 1:8** and plated → **8 plates**.
- Plus **1 plate** for **`8-7-1` Φ8**.

## Data — Qubit quantification (p53)

Green channel, read **@ 470 nm**. Analysis: [`code/0622_quantification.ipynb`](../../code/0622_quantification.ipynb).

**Standards (RFU):**

| Std 0 | Std 1 | Std 3 | Std 10 | Std 30 | Std 100 |
|---|---|---|---|---|---|
| 155.01 | 331.83 | 778.30 | 1931.41 | 5462.82 | 16434.66 `==CONFIRM: p53 reads like "10434.66"; the analysis notebook (entered from the bench) has 16434.66. 16434.66 is the value consistent with a linear curve — confirm the digit.==` |

**Samples — 18 Round-2 bacteria-genome extracts (RFU):**

| Sample | RFU | Sample | RFU | Sample | RFU |
|---|---:|---|---:|---|---:|
| 9-9-2 | 5863.49 | 8-1-2 | 8766.86 | 6-7-2 | 989.73 |
| 6-2-1 | 5370.16 | 10-9-1 | 3200.50 | 6-6-1 | 10163.27 |
| 6-8-2 | 3692.72 | 8-7-1 | 2693.19 | | |
| 6-10-2 | 9343.18 | 6-6-2 | 6949.00 | | |
| 8-10-2 | 11774.60 | 9-1-2 | 6702.02 | | |
| 9-10-1 | 7053.49 | 6-2-2 | 2284.72 | | |
| 6-8-1 | 4896.63 | 10-10-1 | 1296.26 | | |
| 9-1-1 | 13525.83 | 10-7-2 | 1570.95 | | |

> On the page, `6-2-2` is first written as a **second `6-6-2`** and struck through — the corrected label is `6-2-2` (already applied in the analysis notebook).

## Sequencing submission — 2nd bacterial batch (p53)

**"20 µL for sequencing (~50 ng/µL)."**

**Positive-interaction candidates considered** (✱ = status noted on the page):

| Candidate | Note on page |
|---|---|
| ~~8-7-1~~ | ✱ today |
| ~~9-6-1~~ → **9-6-2** | ✱ **sent** (already sequenced 6-08) |
| 9-9-2 | ✱ today |
| 9-2-1 | ✱ **sent** (already sequenced 6-08) |

**→ Changed to: ① `8-5-2` ② `8-10-2` for dilution.**

**Dilution arithmetic on the page** (for `8-10-2`, whose reading was the highest of the two):
```
70 / x = 50 / 100   →   x = 140   →   "70 of water"
```
i.e. **70 µL DNA + 70 µL water** to bring ~100 ng/µL down to **~50 ng/µL**, of which **20 µL** was submitted.
Loose scratch figures at the bottom of the page: **`245.5`** and **`280`** — almost certainly the
`8-5-2` dilution: its Round-1 concentration is **245.51 ng/µL** (`0605_quantification.ipynb`), and
**70 µL DNA + 280 µL water = 350 µL** is a 5× dilution → **49.1 ng/µL ≈ 50**.

> [!note] The `8-10-2` dilution was a bench rough estimate
> The page rounds `8-10-2` to ~100 ng/µL, while the curve on this same page puts its 11774.60 RFU
> reading at **≈ 70.7 ng/µL** — so `70 µL + 70 µL water` lands nearer **35 ng/µL** than 50. This is
> a rough estimate made at the bench (Alex, 2026-08-29), not a transcription error; recorded as
> written.

These two extracts are the **`8-5-2` and `8-10-2` assemblies that came back 2026-06-26/27** into [`data/bacteria_genome/`](../../data/bacteria_genome/) — i.e. the previously unrecorded second submission.

## Checklist — where do the outputs go?
- [ ] 9 soft plates → **incubator**.
- [ ] `8-7-1` streak plate → **incubator**.
- [ ] `9-2-1` / `9-6-2` 3-colony cultures → **incubator**.
- [x] **`8-5-2` + `8-10-2`, diluted to ~50 ng/µL, 20 µL each → sent for sequencing** (assemblies returned 6/26–6/27).

## Source
- Lab notebook: p.52–53 (this entry).
- Analysis: [`code/0622_quantification.ipynb`](../../code/0622_quantification.ipynb).

---
## Log
- 2026-08-29 — Initial digitization from `lab_notebook/0615-0716/IMG_8526.JPG`→`p52.jpg`, `IMG_8527.JPG`→`p53.jpg`. **Two record gaps closed:** (1) the second bacterial sequencing submission (`8-5-2`, `8-10-2`) is documented here and nowhere else; (2) **"20 µL for sequencing (~50 ng/µL)"** independently confirms Alex's 2026-08-08 correction that submitted DNA was normalised to 50 ng/µL, against the 6-08 entry's "NOT diluted" record. `code/0622_quantification.ipynb` had said "there is no digitalized notebook entry for this session yet" — there is now.
- 2026-08-29 — **Alex:** the `~50 ng/µL` targets on this page are **bench rough estimates**; the `8-10-2` arithmetic is recorded as written and marked with a callout rather than flagged as an error.
