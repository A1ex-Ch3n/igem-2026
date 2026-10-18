---
date: 2026-09-09
notebook_pages:
  - p93
authors:
  - "[TBD]"
title: OD600 Time-course of the 25 mL Flask Cultures (date inferred)
---

# OD600 Time-course of the 25 mL Flask Cultures

**Source page:** ![p93](images/p93.jpg)

> [!warning] Date and authors not written on the page
> p93 carries **no date header and no author line** — only the table title. It sits between
> **p.92 (2026-09-08)** and **p.94 (2026-09-10)**, it reads the 25 mL flasks set up on 9/8, and the
> 9/10 entry refers to "the SDS gel from yesterday", which implies a gel was run on **9/9**.
> The date here is therefore **inferred as 2026-09-09**. `==CONFIRM.==`

## Data (p93) — OD600 for 25 mL of liquid culture

| | `e1` | `e40` | `e281` |
|---|---|---|---|
| **Blank** | 0.390 | 0.317 | ~~0.5??~~ → 0.295 |
| **t0 — 10:30 am** | 0.505 *(digit overwritten)* | ~~0.5?4~~ → 0.538 | ~~struck~~ → 0.567 |
| **t1 — 12:3? pm** | 0.433 ; ~~struck~~ | ~~struck~~ ; 0.481 | ~~struck~~ ; 0.576 |
| **t1 — rezero** | 0.143 | 0.164 | 0.301 |
| **t2 — 14:30 pm** | 0.991 | ~~0.5??~~ | ~~0.577~~ |
| **t2 — rezero** | 0.201 | 0.211 | 0.302 |
| **t3 — 16:30 pm, rezero** | `==UNDONE: row written, no values.==` | | |

## Notes / continuity
Per [`feedback_preserve_all_versions`], both the struck and the replacement readings are kept above.
The "rezero" rows are a second reading after re-blanking the spectrometer — those are the values that
track growth; the un-rezeroed t0–t2 numbers sit on top of a drifting blank.

The t3 row being empty is the first sign of what p.94 records: the gel run that evening only showed
clear bands in two lanes.

## Checklist — where do the outputs go?
- [x] t0, t1, t2 read for `e1`, `e40`, `e281`.
- [ ] t3 (16:30) → `==UNDONE: never recorded.==`
- [ ] Induction/gel from these flasks → recorded indirectly on p.94 (9/10).

## Open items
- `==CONFIRM: the date (inferred 2026-09-09) and the authors.==`
- `==CONFIRM: the t1 time — "12:3? pm", the minutes digit is overwritten.==`
- `==CONFIRM: `e1` t2 = 0.991 against its rezero of 0.201 — the un-rezeroed value looks out of family.==`

## Source
- Lab notebook: p.93 (this entry).

---
## Log
- 2026-10-18 — Initial digitization from `lab_notebook/0901-1014/IMG_6587.JPG`→`p93.jpg`. Date inferred, not written.
