---
date: 2026-06-24
notebook_pages:
  - p55
  - p56
  - p57
  - p58
  - p59
authors:
  - "[TBD]"
title: OD600 Phage-Infection Time-Course (9-9-2 + Φ8 picks #2 / #4)
---

# OD600 — Phage Infection Time-Course (9-9-2)

**Source pages:** ![p55](images/p55.jpg) ![p56](images/p56.jpg) ![p57](images/p57.jpg) ![p58](images/p58.jpg) ![p59](images/p59.jpg)

> [!note] Photo legibility & dating
> p56–p59 are rotated ~90°; the tables are legible. **No date or author line is written on p55–p59** — the date comes from the "Result (on 06/24)" note on [p54](2026-06-23_phage-extraction-bacteria-prep.md) and from the timestamps in [`data/assays/0624_od600_phage.csv`](../../data/assays/0624_od600_phage.csv) (t = 0 at 10:42 on 2026-06-24). `==CONFIRM: entry authors for p55–p59.==`

## Objective
Growth/lysis curves for **`9-9-2` colony (1)** challenged with **two plaque-picked `9-9-2` Φ8 phages** (**pick #2** and **pick #4**, from the 7 plaques picked on [2026-06-23](2026-06-23_phage-extraction-bacteria-prep.md)). Hourly OD₆₀₀; phage spiked in once the culture reaches **OD ≈ 0.4**.

## Procedure (p55) — see [[od600_measurement]]
1. Measure the **raw concentrations of the overnight bacteria** on the spectrometer.
2. **Pick the most concentrated one** as the culture used for all OD groups (**9 tubes in today's lab**).
3. Prepare the **blanks**.
4. Prepare **4 tubes for each phage extract**.
5. Prepare all **9 tubes** by adding **1 mL of bacteria working solution** from the tube (**50 µL overnight culture + 5 mL LB**).
6. **Start measurements.**
7. **Wait until the concentration reaches ~0.4, then start adding phage** to the tubes.
8. **Pour the solution back into its tube after each measurement; keep the same cuvette for all.**

**Layout (6 cuvettes → 9 tubes):**

| Group | Tubes | Phage |
|---|---|---|
| `no Φ` | 1 | none (control) |
| `Φ2a … Φ2d` | 4 | `9-9-2` Φ8 **pick #2** |
| `Φ4a … Φ4d` | 4 | `9-9-2` Φ8 **pick #4** |

## Data (p56–p59)

Raw hourly readings, **t = 0 at 10:42** running to **t = 33 (19:42 on 6/25)**.
Machine-readable copy: [`data/assays/0624_od600_phage.csv`](../../data/assays/0624_od600_phage.csv); analysis: [`code/0624_od600_phage.ipynb`](../../code/0624_od600_phage.ipynb).

- **p56** — overnight raw concentrations for the four `9-9-2` colonies, then the `no Φ` + `Φ2a–d` columns.
  `==CONFIRM: the four raw readings transcribe as ① 0.837 ② 0.546 ③ 0.397 ④ 0.740 — colony ① is the highest and is the one used, which is consistent, but confirm the digits.==`
- **p57** — the `Φ4a–d` columns, headed **"For 9-9-2"**. **Phage was added between t = 11 (21:42) and t = 12 (22:42)**, when the cultures read ≈ 0.40.
- **p58** — continuation, 11:42 → 16:42 on 6/25 (`no Φ`, `Φ2a–d`).
- **p59** — from **t = 30 (16:42)** the note **"we mix tubes, change to new cuvette"**: the four replicates of each group were pooled, so the columns become `no Φ`, `Φ2-mix`, `Φ4-mix`.

| time | t | no Φ | Φ2-mix | Φ4-mix |
|---|---:|---:|---:|---:|
| 16:42 | 30 | 1.156 | 1.090 | 1.028 |
| 17:42 | 31 | 1.173 | 1.127 | 1.052 |
| 18:42 | 32 | 1.244 | 1.128 | 1.071 |
| 19:42 | 33 | 1.262 | 1.160 | 1.076 |
| 20:42–22:42 | 34–36 | — | — | — (not read) |

## Result
No lysis: both phage groups track the no-phage control upward. This is the run whose failure prompts the [2026-06-25](2026-06-25_od600-redo-fixed-time-phage.md) redo (phage added at a fixed time / into a dense culture instead of at OD 0.4).

## Checklist
- [x] Readings entered into `data/assays/0624_od600_phage.csv`.
- [ ] `==CONFIRM==` items above.

## Source
- Lab notebook: p.55–59 (this entry).
- Data: [`data/assays/0624_od600_phage.csv`](../../data/assays/0624_od600_phage.csv); analysis [`code/0624_od600_phage.ipynb`](../../code/0624_od600_phage.ipynb).

---
## Log
- 2026-08-29 — Initial digitization from `lab_notebook/0615-0716/IMG_8529.jpeg`→`p55.jpg` … `IMG_8533.JPG`→`p59.jpg`. The **t = 33 row (19:42: 1.262 / 1.160 / 1.076)** is on p59 but was **missing from `0624_od600_phage.csv`** — added to the CSV in this pass. Authors left `[TBD]`; no author line is written on any of the five pages.
