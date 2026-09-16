---
date: 2026-06-25
notebook_pages:
  - p60
  - p61
authors:
  - "[TBD]"
title: OD600 Redo — 9-6-2 / 9-2-1 + Φ8 (fixed-time addition) and 9-9-2 Consistency Trial
---

# OD600 Redo — Fixed-Time Phage Addition

**Source pages:** ![p60](images/p60.jpg) ![p61](images/p61.jpg)

> [!note] Photo legibility
> p60 is rotated ~90°; p61 is upright. Both tables are legible. `==CONFIRM: entry authors — no author line on either page.==`

Two runs started the same evening, both a **redo of the [2026-06-24](2026-06-24_od600-phage-infection-timecourse.md) time-course**, which showed no lysis:

## Run A — `9-6-2` and `9-2-1` with Φ8 (p60)

**Change vs 6/24:** phage is added at a **fixed clock time (8:08 pm)** rather than at OD ≈ 0.4. The non-control cultures were transferred to a smaller tube when the phage went in, **diluting them to ≈ ¾** of their original concentration — this falls **between the t = 6 (19:37) and t = 7 (20:37) readings**.

- Hosts: **`9-6-2`**, **`9-2-1`**; each with a **no-phage control** + **2 phage replicates**.
- t = 0 at **13:37**, hourly.
- Data: [`data/assays/0625_od600_phage(9-6-2_p8, 9-2-1_p8).csv`](../../data/assays/) · analysis [`code/0625_od600_phage.ipynb`](../../code/0625_od600_phage.ipynb).

**Bench notes on p60:**
- *"Close inside door → low O₂ level → slow growth; open → opposite."*
- *"Next time add another control — dilute the bacteria with plate buffer?"* (i.e. a dilution-only control to separate the ¾ dilution from any lysis effect).

## Run B — `9-9-2` consistency trial (p61)

Header: **`9-9-2` Consistency Trial (bac 3 : Φ 1)** `==CONFIRM: the ratio annotation reads like "bac 3 : Φ 1"; confirm the intended bacteria : phage ratio.==`

Phage added at **t = 0 (8:08 pm)** into an already dense culture — no spike-in step, no mid-run dilution.

| time | t | `9-9-2` no Φ | `9-9-2` ① | `9-9-2` ② |
|---|---:|---:|---:|---:|
| 20:08 (add phage) | 0 | 1.168 | 0.968 | 0.948 |
| 21:08 | 1 | 1.175 | 0.964 | 0.983 |
| 22:08 | 2 | 1.210 | 0.969 | 0.981 |
| 23:08 | 3 | 1.236 | 1.019 | 1.029 |
| 00:08 | 4 | 1.283 | 1.079 | 1.087 |
| 10:08 (next morning) | 14 | 1.566 | 1.540 | 1.369 |
| | | | | **STOP** |

Data: [`data/assays/0625_od600_phage(9-9-2_p8_redo).csv`](../../data/assays/) · analysis [`code/0625_od600_phage_9-9-2_redo.ipynb`](../../code/0625_od600_phage_9-9-2_redo.ipynb).

## Result
Both phage tubes stay **below the control but keep rising** — no lysis. The run is **stopped** the next day; see the experiment note on [2026-06-26](2026-06-26_od600-phage-harvest-genome-extraction.md) p63.

## Source
- Lab notebook: p.60–61 (this entry).
- Data + analysis: `data/assays/0625_*.csv`, `code/0625_od600_phage.ipynb`, `code/0625_od600_phage_9-9-2_redo.ipynb`.

---
## Log
- 2026-08-29 — Initial digitization from `lab_notebook/0615-0716/IMG_8534.JPG`→`p60.jpg`, `IMG_8535.JPG`→`p61.jpg`. p61 matches `0625_od600_phage(9-9-2_p8_redo).csv` value-for-value. **Redo pair:** 6/24 (phage at OD 0.4) → 6/25 (phage at fixed time / into dense culture); both negative for lysis.
