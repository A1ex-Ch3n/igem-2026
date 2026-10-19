---
date: 2026-10-01
notebook_pages:
  - nb2_p07
authors:
  - Alex
  - Rafael
title: His-tag Protein Purification (NEB S1427) & Gel Loading Plan
---

# His-tag Protein Purification & Gel Loading Plan

**Source page:** ![nb2 p07](images/nb2_p07.jpg)

> [!note] Page numbering
> Printed **"07"** — second notebook, see the note in the 2026-09-28 entry.
> The loading plan is on a **blue sticky note** pasted onto the page.

## Goals (nb2 p07)
- **Protein purification.**

## Procedure (nb2 p07)
- **Protocol: "His Tag Protein Purification…" (NEB #S1427), … "8 samples".**

## Experiment notes (nb2 p07) — gel loading plan (sticky note)

| Lane | #1 | #2 | #3 | #4 | #5 | #6 |
|---|---|---|---|---|---|---|
| | ladder | `CDS10` 1:1 | `CDS10` 1:2 | `CDS10` W3 | `CDS10` E1 | `CDS10` E2 |

| Lane | #7 | #8 | #9 | #10 | #11 | #12 |
|---|---|---|---|---|---|---|
| | `e40` 1:1 | `e40` 1:2 | `e40` W3 | `e40` E1 | `e40` E2 | ladder |

Volumes written under the columns: **1:1 = 20 µL sample; 1:2 = 10 µL sample + 10 µL MQ water;
W3 = 20 µL; E1 = 20 µL; E2 = 20 µL**; **#1, #12 → ladder**.

## Notes / continuity
First purification attempt of the project, on **`CDS10`** and **`e40`**. `W3` = third wash fraction,
`E1`/`E2` = the two elutions. The same fraction layout is used for the **`e281` Ni-NTA run on 10/10**,
which [`code/1010_gel_annotation.ipynb`](../../code/1010_gel_annotation.ipynb) shows **failed** —
blank elutions, flow-through identical to the load.

## Checklist — where do the outputs go?
- [x] Purification run per NEB #S1427.
- [x] Gel of these fractions → `data/assays/1001_sds_page/` (two annotated gels, archived 2026-10-19).
- [x] Result/verdict for `CDS10` and `e40` → **nothing eluted.** Gel 2 shows lysate bands in
  Raw and Raw 1:2 and nothing at the expected size in W3, E1 or E2.

## Gels

Archived at [`data/assays/1001_sds_page/`](../../data/assays/1001_sds_page/), with a README.

- **Gel 2** is the gel this loading plan describes: `CDS10` and `e40`, Raw / Raw 1:2 / W3 / E1 / E2.
  Nothing eluted.
- **Gel 1** is a second gel run the same day on `CDS11`, `CDS12`, `e1` and `e281` (FT / E1 / E2),
  which this page does not mention. It is the **only purification of the project that eluted
  protein**: `e1` at ~41 kDa (expected 41.9) and `CDS11` at ~43 kDa — but `CDS11` is expected at
  **72.0 kDa**, so that band is ~29 kDa short and unexplained. `CDS12` and `e281` gave nothing.

Both files are annotated composites received by WhatsApp; the raw photographs are not in the repo
and there is no lane-quantification TSV behind them, unlike 0915 / 0929 / 1010.

## Open items
- `==CONFIRM: "8 samples" — what the protocol note's sample count refers to, given 10 loaded lanes.==`
- `==CONFIRM: whether the 1:1 / 1:2 lanes are the crude lysate (load) or the flow-through.==`
- `==CONFIRM: why only `CDS10` and `e40` were purified here, when `e281` was the one purified on 10/10.==`
  Partly answered by Gel 1: `e281` *was* run on 10/01, on the second gel, and gave no eluted band.
- `==CONFIRM: the ~43 kDa `CDS11` band on Gel 1 against the 72.0 kDa expected size — degradation,
  truncation, or a co-purifying contaminant.==`

## Source
- Lab notebook: notebook 2, p.07 (this entry).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6595.JPG`→`nb2_p07.jpg`.
- 2026-10-19 — Archived the two 10/01 annotated gels to `data/assays/1001_sds_page/`; closed both
  checklist items and added the `CDS11` size discrepancy as an open item.
