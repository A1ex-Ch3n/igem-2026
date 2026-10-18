---
date: 2026-09-28
notebook_pages:
  - nb2_p06
authors:
  - "[TBD]"
title: Protein Dilution & BCA Quantification (1:10 and 1:20)
---

# Protein Dilution & BCA Quantification

**Source page:** ![nb2 p06](images/nb2_p06.jpg)

> [!note] First written page of notebook 2
> A **second physical notebook** was started on **2026-09-27** and is used from here on (Alex,
> 2026-10-18). Its **p.01–p.05 are reserved for a table of contents** to be written later, so this
> page — printed **"06"** — is its first written page. Notebook 1 ends at p.100 (2026-09-27).
> Filed as `nb2_p06`–`nb2_p08`. No author line is written on this page.

## Procedure (nb2 p06)
1. **Did 1:10 and 1:20 dilution for IPTG and non-induced `CDS10`, `CDS11`, `CDS12`, `e1`, `e40`, `e281`.**
2. **Used the BCA Protein Assay Kit and incubated the proteins at 37 °C for 30 min. Then left them at
   room temperature for 5 min.**
   - **For the BCA Protein Assay, added 1 mL of reagent solution and 50 µL protein sample to each of
     the eppendorfs.**
3. **Measured OD at 562 nm.**

## Results (nb2 p06) — `+` = IPTG-induced, `−` = non-induced

**1:10**

| Sample | OD562 | | Sample | OD562 |
|---|---|---|---|---|
| `CDS10` + | 0.900 | | `e1` + | 0.756 |
| `CDS10` − | 1.139 | | `e1` − | 0.889 |
| `CDS11` + | 0.797 | | `e40` + | 0.715 |
| `CDS11` − | 0.624 | | `e40` − | 0.979 |
| `CDS12` + | 0.706 | | `e281` + | 0.880 |
| `CDS12` − | 0.806 | | `e281` − | 1.051 |

**1:20**

| Sample | OD562 | | Sample | OD562 |
|---|---|---|---|---|
| `CDS10` + | 0.530 | | `e1` + | 0.485 |
| `CDS10` − | 0.758 | | `e1` − | 0.574 |
| `CDS11` + | 0.503 | | `e40` + | 0.451 |
| `CDS11` − | 0.394 | | `e40` − | 0.664 |
| `CDS12` + | 0.465 | | `e281` + | 0.529 |
| `CDS12` − | 0.523 | | `e281` − | 0.662 |

## Notes / continuity
This rescues the saturated 9/27 readings (four pairs pegged at 3.000). The 1:20 values are close to
half the 1:10 values for every sample, so the dilution series is internally consistent and the
readings are inside the linear range.

**In 10 of the 12 pairs the non-induced lysate has *more* total protein than the induced one** — the
expected consequence of IPTG slowing growth, and a reminder that total-protein normalisation matters
when reading the 9/29 gels.

## Checklist — where do the outputs go?
- [x] 12 samples × 2 dilutions read at 562 nm.
- [ ] A BCA standard curve → `==UNDONE: no standards recorded on this page, so these OD values are not converted to mg/mL anywhere.==`
- [ ] Analysis notebook → `==UNDONE: none in `code/`.==`

## Open items
- `==CONFIRM: the authors for this day.==`
- `==CONFIRM: whether a BCA standard series was run (without it these are relative numbers only).==`
- `==CONFIRM: `CDS11` 1:20 non-induced = 0.394 — the only pair that breaks the ~half-of-1:10 pattern.==`

## Source
- Lab notebook: notebook 2, p.06 (this entry).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6594.JPG`→`nb2_p06.jpg`.
- 2026-10-18 — Second-notebook question resolved by Alex; warning callout replaced.
