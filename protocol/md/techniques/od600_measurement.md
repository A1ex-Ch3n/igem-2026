---
title: OD₆₀₀ Measurement
type: technique
purpose: Quantify bacterial cell density in a liquid culture by absorbance at 600 nm. Two modes (diluted and undiluted) used at different timepoints.
references:
  - "[[lb_broth]]"
source:
  - lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md
estimated_time: ≈ 5 min per sample (after spectrometer warm-up + calibration)
---

# OD₆₀₀ Measurement

## Purpose
Measure the absorbance of a bacterial culture at 600 nm to estimate cell density. Two complementary modes are used:
- **Diluted mode** (1 % concentration) catches very dense cultures without saturating the detector.
- **Undiluted mode** reads dilute cultures directly.

The output drives downstream decisions: which cultures are dense enough for [[glycerol_stock_storage]] (the 0.6–1.0 candidate band from the [2026-05-29](../../../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) entry).

## Quick-lookup table — two modes used on 5-29

| Mode | Used at | Bacteria volume | LB broth volume | Effective dilution |
|---|---|---|---|---|
| **Diluted** — t22 (22 h after inoculation) | high-density cultures | 100 µL | 9900 µL (1 mL total going in cuvette) | 1:100 |
| **Undiluted** — t26 (26 h after inoculation) | direct reading | 1 mL | 0 (no dilution) | 1:1 |

## Materials & equipment
- UV/Vis spectrophotometer set to 600 nm
- 1.5 mL cuvettes
- Pipettes (100 µL, 1000 µL)
- [[lb_broth]] (for blanks + diluent)
- Bacterial samples

## Reagents
- [[lb_broth]] — used as the blank and as the diluent for the diluted (1 %) reading
- Bacterial culture sample (overnight liquid culture — output of [[single_colony_inoculation]])

## Procedure

### Calibration (do once per session)
1. Prepare 3 blank cuvettes containing 1 mL of [[lb_broth]].
2. Calibrate the spectrometer with the three blanks at 600 nm.

### Mode A — Diluted reading
1. **In a 15 mL tube**, mix **100 µL of bacteria sample** + **9900 µL of [[lb_broth]]** for a 1 % (1:100) dilution (10 mL total — too large for a 1.5 mL cuvette directly).
2. **Transfer 1 mL** of the diluted mixture into a 1.5 mL cuvette.
3. Insert into the spectrometer, measure, record the reading.

### Mode B — Undiluted (concentrated) reading
1. Continue with the calibration from the diluted run.
2. Pipette 1 mL of the bacteria sample directly into a clean cuvette.
3. Measure and record the reading.

## Notes / common deviations
- The **undiluted** raw A₆₀₀ is the value used to decide stock candidacy: **A₆₀₀ ≥ 0.6** marks a *P. aeruginosa* candidate; the **0.6–1.0** band is the preferred range for [[glycerol_stock_storage]] (above 1.0 risks being past log phase — no continuous 24-h OD curve was done, so log-phase absorbance is unknown).
- Always blank against the same lot of broth as the cultures were grown in — different broth lots have slightly different baseline absorbance.

## Checklist — where do the outputs go?
- [ ] OD readings → recorded in `data/assays/0529_OD.xlsx` (or equivalent for future days).
- [ ] Measured cuvette contents → discard via [[media_disposal]].

## Source
- Lab notebook: [2026-05-29](../../../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) (Procedures ①ₐ and ①ᵦ).
- Data file: `../../../data/assays/0529_OD.xlsx`.

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry.
- 2026-06-08 — **Fixed Mode A vessel bug** (proofread #1): recipe said "in a 1.5 mL cuvette, mix 100 µL + 9900 µL" which is physically impossible (10 mL doesn't fit a 1.5 mL cuvette). Rewritten as "mix in a 15 mL tube, then transfer 1 mL aliquot to a 1.5 mL cuvette" — preserves the 1:100 dilution from the 5-29 lab-notebook record. Removed the trailing `[TBD: confirm vessel]` flag.
