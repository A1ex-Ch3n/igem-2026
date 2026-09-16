---
date: 2026-07-09
notebook_pages:
  - p77
authors:
  - Carol
title: Resistant-Colony Pellets, Genome Extraction & Qubit (9-2-1 R1–R3, 9-6-2 R1–R3)
---

# Resistant Bacteria — Pellet, Extraction, Quantification

**Source page:** ![p77](images/p77.jpg)

> [!note] Photo legibility
> p77 is upright and legible.

> [!important] This page re-identifies the samples in `0710_quantification.ipynb`
> The analysis notebook is dated **2026-07-10** and describes the samples as "two strains, each with three variants (`r1/r2/r3`) picked from different plates", assuming they are the **6/05 bacterial genome extracts** (`VOL_REMAINING_uL = 90.0`). This page shows they are **phage-resistant colonies** — 3 per host — **pelleted and extracted on 7/9**. The standard-curve values match exactly, so it is the same session.

## Purpose & procedure (p77)
- **Resistant bacteria: 3 colonies per strain, 6 in total**, taken from the **7/8 LB tubes**.
- **Pellet** → **genome extraction** → **quantification**.
  See [[bacteria_pellet_for_sequencing]], [[bacteria_genome_extraction]], [[dna_quantification_qubit]].

## Data — Qubit (p77)

**Standards (RFU):** no Std-0 blank this session.

| Std 1 | Std 3 | Std 10 | Std 30 |
|---:|---:|---:|---:|
| 210.50 | 308.30 | 485.05 | 1369.67 |

**Samples (RFU):**

| Sample | RFU | | Sample | RFU |
|---|---:|---|---|---:|
| `9-2-1` R1 | 2378.22 | | `9-6-2` R1 | 5123.33 |
| `9-2-1` R2 | 18378.32 | | `9-6-2` R2 | 47703.89 |
| `9-2-1` R3 | 3399.31 | | `9-6-2` R3 | 10563.26 |

**Bench note:** *"The reads go up when you increase waiting time."*

⚠ **Every sample reads above the top standard (30 ng/µL)** — the concentrations from this curve are order-of-magnitude estimates only. **A dilute-and-re-read is owed.** `==UNDONE: not re-read as of 2026-08-29.==`

## Plan written on the page — bacteria for the 07/13 EOP redo

| | | |
|---|---|---|
| 8-7-1 | ~~8-3-2~~ | 9-9-2 |
| 9-2-2 | 6-7-2 | 6-2-1 |
| 6-6-1 | 6-2-2 | 6-6-2 |
| 6-8-2 | | |

## Source
- Lab notebook: p.77 (this entry).
- Analysis: [`code/0710_quantification.ipynb`](../../code/0710_quantification.ipynb) (dated 7/10; readings are this session's).

---
## Log
- 2026-08-29 — Initial digitization from `lab_notebook/0615-0716/IMG_8551.jpeg`→`p77.jpg`. **Corrects `code/0710_quantification.ipynb` on two points:** the samples are **phage-resistant colonies extracted 7/9**, not 6/05 bacterial extracts with ~90 µL remaining, and the bench date is **7/9**. A dated note was added to the notebook rather than rewriting its narrative.
