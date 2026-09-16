---
date: 2026-06-29
notebook_pages:
  - p64
  - p65
  - p66
authors:
  - Olivia
  - Alex
title: Phage Genome Extraction (10 + 20 tubes) & Qubit Quantification
---

# Phage Genome Extraction · Quantification

**Source pages:** ![p64](images/p64.jpg) ![p65](images/p65.jpg) ![p66](images/p66.jpg)

> [!note] Photo legibility
> p64 is rotated ~90° (with red-ink annotations); p65–p66 are upright. All legible.

## Summary (p64)
- **Do 10 extractions** on the **phage lysate collected last week**.
- **Quantify 1 of them.**

## Procedure (p64)
- Follow the **Zymo kit instruction** — see [[quick_dna_miniprep_kit]].
- Follow the **quantification instruction** — see [[dna_quantification_qubit]].

## Experiment note — round 1 (p64)
- The team has **16 lysates from last week's work** (from **`9-2-1` Φ8** and **`9-6-2` Φ8**, the 1:256 picks of [2026-06-23](2026-06-23_phage-extraction-bacteria-prep.md)); **`9-2-1` Φ8 is the one taken for quantification**. Two of the tubes come from `9-6-2`.
- **10 extractions** were done, laid out as tubes ①–⑧ plus two `9-6-2` Φ8 tubes ⑨/⑩.
- ⚠ **Columns ⑤ and ⑥ broke, so those were discarded** (red note).
- **Redo:** the extraction was repeated with **6 µL of buffer added at the end to increase concentration** (red note).
- **Quantification loading:** **2 (samples: `9-2-1`, `9-6-2`) + 6 (standards) + 2 (extra) = 10 µL of (A) + 2000 µL of (B)**.

## Data (p65) — Qubit, green channel @ 470 nm

Analysis: [`code/0629_quantification.ipynb`](../../code/0629_quantification.ipynb).

| Standard | RFU |
|---|---:|
| S0 | 148.72 |
| S1 | 359.54 |
| S3 | 862.17 |
| S10 | 2073.23 |
| S30 | 6390.88 |
| S100 | 21543.99 |

| Sample | RFU | Note |
|---|---:|---|
| `9-2-1` / `9-6-2` (round-1 phage DNA) | **517.73** | ⚠ red note: **"too low, need to redo for a higher concentration"** |
| **extraction round 2**, 5 µL collected DNA | **3116.13** | *"50 % phage genome"* → **dilute to 10–11 ng/µL** |

`==CONFIRM: p65 reads 3116.13; code/0629_quantification.ipynb has 3116.15. One digit differs — confirm which is the bench value.==`

## Extraction round 2 (p66)

| Phage | Tubes |
|---|---|
| `9-2-1` Φ8 | ①②③④ ⑤⑥⑦⑧ (× 1) |
| `9-6-2` Φ8 | ①②③④ ⑤⑥⑦⑧ (× 2) |

→ **20 tubes in total.**

- Each was mixed with **Viral DNA Buffer**, centrifuged, and the DNA collected across **4 columns** — so **each column collected DNA from 5 different samples**.
- **300 µL DNA wash buffer**, centrifuge, **dump** the flow-through — **× 2**.
- Added **6 µL elution buffer**, centrifuged and **collected all 4 flow-throughs into 1 tube**.
- **Used 5 µL for quantification.**
- *"Data on p.65."*

## Notes / continuity
This is the material that becomes the sequenced **`9-2-1` Φ8** phage genome (results back 2026-07-08). The **submission date itself is still not written anywhere** — see `typos.md`.

## Checklist — where do the outputs go?
- [x] Round-1 extraction — **too low**, superseded by round 2.
- [ ] Round-2 pooled eluate → dilute to **10–11 ng/µL** → sequencing.
- [ ] `==CONFIRM==` items above.

## Source
- Lab notebook: p.64–66 (this entry).
- Analysis: [`code/0629_quantification.ipynb`](../../code/0629_quantification.ipynb).

---
## Log
- 2026-08-29 — Initial digitization from `lab_notebook/0615-0716/IMG_8538.JPG`→`p64.jpg`, `IMG_8539.JPG`→`p65.jpg`, `IMG_8540.JPG`→`p66.jpg`. `0629_quantification.ipynb` labelled these only "Sample 1 / Sample 2, prepared by different methods" — they are now identified: **Sample 1 = the round-1 phage DNA (517.73, too low), Sample 2 = the round-2 pooled extraction (3116.1x, read at 50 %)**. **Failed step recorded:** columns ⑤/⑥ broke and round 1 was too dilute → round 2 with 6 µL elution.
