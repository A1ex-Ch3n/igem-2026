---
date: 2026-09-24
notebook_pages:
  - p99
authors:
  - Alex
title: Plasmid Extraction, Stock Preparation & DNA Quantification (6 constructs)
---

# Plasmid Extraction, Stock Preparation & DNA Quantification

**Source page:** ![p99](images/p99.jpg)

> [!note] Photo legibility
> p99 is legible. The title has **"Daily passing"** struck through, leaving
> "& DNA plasmid extraction & Stock Preparation & DNA Quantification".

## Experiment notes (p99)
- **500 µL glycerol + 500 µL sample for STOCK.**
- **DH5α stocks stored in −80 °C.**
- Plate rows: **row A** = `S0 S1 S3 S10 S30 S100`; **row B** = `e1 e40 e281 CDS10 CDS11 CDS12`.
- **12 + 3 = 15 µL of Helixyte**, **3 mL of Ⓑ**, **5 µL for sample quantification.**

## Data — OD600 (p99)

| Construct | OD600 | | Construct | OD600 |
|---|---|---|---|---|
| `CDS10` | 1.818 | | `e1` | 1.980 |
| `CDS11` | 1.796 | | `e40` | 2.029 |
| `CDS12` | 1.814 | | `e281` | 1.981 |

## Data — DNA quantification (p99)

| Standard | RFU | | Sample | RFU |
|---|---|---|---|---|
| S0 | 161.14 | | `e1` | 173.57 |
| S1 | 257.89 | | `e40` | **2169.50 →** |
| S3 | 378.83 | | `e281` | 690.99 |
| S10 | 1053.39 | | `CDS10` | **2032.14 →** |
| S30 | 2800.73 | | `CDS11` | 1216.17 |
| S100 | 12564.02 | | `CDS12` | **1231.45 →** *(underlined twice)* |

## Notes / continuity
All **six** constructs are back in play here, including `CDS10`, which had been parked at the stock
stage on 9/7. **`e1` reads 173.57 — barely above the S0 blank (161.14)**, i.e. essentially no plasmid
recovered from that miniprep.

**`DH5α`** is named here for the first time; the 9/1 streak was recorded as "DH10-B like" and the 9/4
transformation used **BL21**. So this day's minipreps are presumably from the cloning host, with BL21
kept as the expression strain. `==CONFIRM.==`

## Checklist — where do the outputs go?
- [x] Glycerol stocks (500 µL + 500 µL) → **−80 °C** (labelled DH5α).
- [x] Plasmids extracted and quantified for all 6 constructs.
- [ ] A notebook analysing these readings → `==UNDONE: no `code/0924_quantification.ipynb` exists; only the 9/4 set was worked up.==`

## Open items
- `==CONFIRM: DH5α vs the "DH10-B like" strain on p.82 and the BL21 transformation on p.88 — which host these stocks are.==`
- `==CONFIRM: what the arrows/underlines on `e40`, `CDS10`, `CDS12` mark.==`
- `==CONFIRM: "12 + 3 = 15 µL of Helixyte" — 12 reactions + 3 spare?==`

## Source
- Lab notebook: p.99 (this entry).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6592.JPG`→`p99.jpg`.
