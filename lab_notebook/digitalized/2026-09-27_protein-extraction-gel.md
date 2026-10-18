---
date: 2026-09-27
notebook_pages:
  - p100
authors:
  - Alex
  - Olivia
title: Induction, Crude-lysate Protein OD562 & Gel Prep
---

# Induction, Crude-lysate Protein OD562 & Gel Prep

**Source page:** ![p100](images/p100.jpg)

> [!note] Photo legibility
> p100 is crowded: four blocks of numbers share the lower half and several labels are struck or
> overwritten. The ⊖/⊕ assignments in the "OD600 at 4 hrs" block carry `==CONFIRM==` marks.

## Goals (p100)
- **Morning OD600.**
- **Daily passing: 100 µL culture + 50 mL LB with kanamycin.**

## Experiment notes (p100) — induction setup

| IPTG | Non-induced |
|---|---|
| 25 mL media + 25 mL sample + **IPTG (200 µL), 40 mg/mL** | 25 mL media + 25 mL sample |

## Data — OD600 morning (p100)

| Construct | OD600 |
|---|---|
| `CDS10` | 1.269 |
| `e281` | 1.750 |
| `e40` | 1.466 |

## Data — OD600 at 4 hrs (p100)

| Construct | ⊖ | ⊕ |
|---|---|---|
| `CDS10` | 1.829 | 1.929 |
| *(struck label)* | | 1.938 |
| `e281` | 1.916 | 1.882 |
| `e40` | 1.852 | `==UNDONE: no ⊕ value in line with `e40`.==` |

## Data — crude-lysate protein OD at 562 nm (p100)
Written as **"Soup Protein OD 562 nm"**; ⊖ = non-induced, ⊕ = IPTG.

| Construct | ⊖ | ⊕ |
|---|---|---|
| `CDS11` | 2.134 | 2.459 |
| `CDS12` | 2.699 | 2.252 |
| `e1` | 3.000 | 2.787 |
| `CDS10` | 3.000 | 3.000 |
| `e40` | 3.000 | 3.000 |
| `e281` | 3.000 | 3.000 |

**Four of the six read exactly 3.000 on both arms — the reader's ceiling**, which is why the samples
are diluted 1:10 and 1:20 and re-read the next day (9/28, notebook 2 p.06).

## Notes / continuity
**This is the last page of notebook 1.** The second physical notebook is started on this day
(2026-09-27) and used from 9/28 onward; its p.01–p.05 are held for a table of contents, so its first
written page is p.06 (Alex, 2026-10-18).

The **2026-09-29 gels** run from these lysates have **no notebook page** — see
[`code/0929_gel_annotation.ipynb`](../../code/0929_gel_annotation.ipynb), which serves as the record.

These lysates are the ones run on the **two 2026-09-29 gels** analysed in
[`code/0929_gel_annotation.ipynb`](../../code/0929_gel_annotation.ipynb) — the first gels with
candidate bands (`CDS12` IPTG-only at 40–43 kDa; `e1` at 45–50 kDa), neither assigned.

## Checklist — where do the outputs go?
- [x] Morning OD600 (3 constructs) + 4 h OD600.
- [x] ± IPTG pairs set up at 25 mL + 25 mL, IPTG 200 µL of 40 mg/mL.
- [x] Crude lysates read at 562 nm (saturated for 4 of 6) → diluted and re-read 9/28.

## Open items
- `==CONFIRM: the "OD600 at 4 hrs" block — one label is struck out and one ⊕ value (1.938) has no construct in line with it.==`
- `==CONFIRM: why only `CDS10`, `e281`, `e40` have a morning OD600 while all six have a 562 nm reading.==`
- `==CONFIRM: the final IPTG concentration — 200 µL of 40 mg/mL into 50 mL ≈ 0.16 mg/mL ≈ 0.67 mM.==`

## Source
- Lab notebook: p.100 (this entry).
- Analysis of the resulting gels: [`code/0929_gel_annotation.ipynb`](../../code/0929_gel_annotation.ipynb).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6593.JPG`→`p100.jpg`.
- 2026-10-18 — Noted the switch to notebook 2 on this date (Alex).
