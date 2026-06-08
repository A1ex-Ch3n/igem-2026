---
date: 2026-05-29
notebook_pages:
  - "p18"
  - "p19"
authors: [Alex, Olivia]
title: Optical Density & Bacteria Stock Preparation
---

# Optical Density & Bacteria Stock Preparation

**Source pages:** ![p18](images/p18.jpg) ![p19](images/p19.jpg)

## Purpose & summary
1. Optical Density (OD), with diluted bacteria & concentrated, at **t22** (22 h after inoculation, diluted reading) and **t26** (26 h after inoculation, stock reading).
2. Prepare & freeze high-concentration bacteria with glycerol as stock for later use.
3. Culture transfer (from PIA plates to LB broth in snap-cap tubes).

## Procedures

### ①ₐ Optical Density (diluted) — t22
1. Have 3 cuvettes for blanks (1 mL of LB broth in 1.5 mL cuvettes).
2. Calibrate the spectrometer with three blanks.
3. Mix 100 µL of sample (bacteria) and 9900 µL of LB broth (1 % concentration for sample).
4. Measure and record the reading.

### ①ᵦ Optical Density (concentrated) — t26
1. Continue with calibration listed above.
2. Directly pipette 1 mL of bacteria sample and transfer to the cuvette.
3. Measure and record the reading.

### ② Bacteria stock
1. Prepare 50 % glycerol (diluted w/ MiniQ water).
2. Mix 650 µL of OG (original / undiluted) bacteria sample and 650 µL of glycerol (50 %) in an Eppendorf.
3. Store in −80 °C.

### ③ Culture transfer
1. Take out the overnight-grown bacteria on PIA plates from the 30 °C incubator.
2. Move plates into the safety cabin and proceed with protocols in the safety cabin.
3. Use a yellow loop to collect each sample (10 µL) and transfer them into 15 mL of LB broth (1 %) in snap-cap tubes.
4. Store the cultures in the 30 °C incubator.

## Data → conclusion
The threshold to take as stock is OD of **0.6 or above** at full concentration (no dilution). We stored all of them as stock.

**Stock labels** *(format `sample_site . duplicate_number . plate_section`; 1 = left half, 2 = right half):*

| Sample | | | | |
|---|---|---|---|---|
| 10-10-1 | 10-9-1 | 10-7-2 | 8-2-2 | 10-9-2 |
| 9-6-2 | 8-3-2 | 10-10-2 | 8-5-1 | 9-2-1 |
| 9-2-2 | 8-5-2 | 6-3-2 | | |

### OD measurement data

Full readings live in [`data/0529_OD.xlsx`](../../data/0529_OD.xlsx). Summary below.

**Sheet 1 — Per-plate readings** *(collection time 12 PM, UV spectrophotometer at A₆₀₀)*

| Plate | Sample | Repetition | Absorbance (A₆₀₀) | Average T0 (×100 dilution) | Average T4 (4 PM) |
|---|---|---|---|---|---|
| 6 | 3 | 1 | 0.002 / 0.002 | 0.20 | 0.238 |
| 6 | 3 | 2 | 0.004 / 0.004 | 0.40 | 0.220 |
| 6 | 4 | 1 | 0.004 | 0.40 | 0.450 |
| 6 | 4 | 2 | 0.004 | — | — |
| 8 | 2 | 1 | 0.008 / 0.007 | 0.75 | 0.927 |
| 8 | 3 | 1 | 0.008 / 0.007 | 0.75 | 0.895 |
| 8 | 5 | 1 | 0.008 / 0.005 | 0.65 | 0.836 |
| 8 | 5 | 2 | 0.008 / 0.009 | 0.85 | 0.697 |
| 9 | 2 | 1 | 0.001 / 0.004 | 0.25 | 0.830 |
| 9 | 2 | 2 | 0.014 / 0.009 | 1.15 | 0.809 |
| 9 | 6 | 1 | 0.004 / 0.004 | 0.40 | 0.581 |
| 9 | 6 | 2 | 0.012 / 0.009 | 1.05 | 0.904 |
| 10 | 7 | 1 | 0.008 / 0.009 | 0.85 | 1.135 |
| 10 | 9 | 1 | 0.003 / 0.003 | 0.30 | 1.215 |
| 10 | 9 | 2 | 0.010 / 0.006 | 0.80 | 0.905 |
| 10 | 10 | 1 | 0.007 / 0.004 | 0.55 | 1.235 |
| 10 | 10 | 2 | 0.013 / 0.009 | 1.10 | 0.871 |

**Sheet 2 — Stock Solution List** *(Raw culture A₆₀₀, sorted by descending OD)*

| # | Sample | A₆₀₀ |
|---|---|---|
| 1 | 10-10-1 | 1.235 |
| 2 | 10-9-1 | 1.215 |
| 3 | 10-7-2 | 1.135 |
| 4 | 8-2-2 | 0.927 |
| 5 | 10-9-2 | 0.905 |
| 6 | 9-6-2 | 0.904 |
| 7 | 8-3-2 | 0.895 |
| 8 | 10-10-2 | 0.871 |
| 9 | 8-5-1 | 0.836 |
| 10 | 9-2-1 | 0.830 |
| 11 | 9-2-2 | 0.809 |
| 12 | 8-5-2 | 0.697 |
| 13 | 6-3-2 | 0.645 |
| 14 | 6-2-1 | 0.826 — **Most Likely *P. aeruginosa*** |
| 15 | 6-2-2 | 1.166 |
| 16 | 6-6-1 | 0.962 |
| 17 | 6-6-2 | 0.817 |
| 18 | 6-7-2 | 0.646 |
| 19 | 6-8-1 | 1.175 |
| 20 | 6-8-2 | 0.848 |
| 21 | 6-10-2 | 0.766 |
| 22 | 8-1-2 | 1.176 |
| 23 | 8-7-1 | 0.841 |
| 24 | 8-10-2 | 0.934 |
| 25 | 9-1-1 | 1.671 |
| 26 | 9-1-2 | 1.224 |
| 27 | 9-9-2 | 1.498 |
| 28 | 9-10-1 | 1.554 |

Total: **28 stocks**.

---
## Log
- 2026-06-04 — Initial digitization from `pre_0604.pdf` pp.18–19. Corrected handwritten "10 mL" → "10 µL" loop volume (logged in `typos.md`).
- 2026-06-04 — Added full OD measurement tables transcribed from `data/0529_OD.xlsx`.
