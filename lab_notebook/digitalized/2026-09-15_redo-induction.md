---
date: 2026-09-15
notebook_pages:
  - p96
authors:
  - Rafael
  - Alex
title: Redo Induction — Morning and New-batch OD600
---

# Redo Induction — Morning and New-batch OD600

**Source page:** ![p96](images/p96.jpg)

> [!note] Photo legibility
> p96 is legible. `CDS11`/`CDS12` are written as `CDS₁₁`/`CDS₁₂`, `e40`/`e281` as `E₄₀`/`E₂₈₁`.

## Goals (p96)
- **Redo induction.**

## Notes (p96)
- **25 mL of overnight culture + 75 mL of fresh LB (kanamycin).**

## Data (p96)

**Morning OD**

| Construct | OD600 |
|---|---|
| `CDS11` | 2.639 |
| `CDS12` | 2.327 |
| `e40` | 2.721 |
| `e281` | 2.610 |

**New batch OD** — ⊖ = non-induced, ⊕ = **with IPTG**

| Construct | ⊖ | ⊕ |
|---|---|---|
| `CDS11` | 1.902 | 1.876 |
| `CDS12` | 1.368 | 1.354 |
| `e40` | 1.953 | 1.946 |
| `e281` | 1.847 | 1.810 |

## Notes / continuity
This is the induction behind the **two 2026-09-15 gels** analysed in
[`code/0915_gel_annotation.ipynb`](../../code/0915_gel_annotation.ipynb) — gel 1 `e40`/`e281`,
gel 2 `CDS11`/`CDS12`, matching the four constructs on this page. That notebook's verdict is
**inconclusive**: `CDS11`, `e40` and `e281` lanes came out essentially blank, and `CDS12` showed no
difference between induced and uninduced.

The new-batch ODs are ~1.4–2.0 at the point of induction, i.e. **well above the "till 0.8" rule
written on p.94** — worth noting as a possible reason the induction did not show.

## Checklist — where do the outputs go?
- [x] 25 mL overnight + 75 mL fresh LB (Kan) per construct; ± IPTG pair per construct.
- [x] Gels run and photographed → `data/assays/0915_sds_page/`.
- [ ] `e1` → not on this page; `==UNDONE: dropped from the 9/15 round without comment.==`

## Open items
- `==CONFIRM: the IPTG concentration/volume used on 9/15 (not written; the 9/27 page records 200 µL of 40 mg/mL into 50 mL).==`
- `==CONFIRM: why induction was done at OD ≈ 1.4–2.0 rather than 0.8.==`
- `==CONFIRM: whether the ⊖/⊕ ODs were taken at induction (t0) or after the induction period.==`

## Source
- Lab notebook: p.96 (this entry).
- Analysis: [`code/0915_gel_annotation.ipynb`](../../code/0915_gel_annotation.ipynb).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6590.JPG`→`p96.jpg`.
