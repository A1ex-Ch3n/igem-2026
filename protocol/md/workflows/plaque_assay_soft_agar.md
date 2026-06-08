---
title: Plaque Assay — Soft-Agar Overlay Method
type: workflow
purpose: Detect phage activity on a bacterial lawn by mixing bacteria with soft agar, pouring as an overlay, and spotting phage filtrate on the surface.
references:
  - "[[lb_agar]]"
  - "[[lb_broth]]"
  - "[[phage_buffer]]"
  - "[[phage_isolation]]"
source:
  - lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md
estimated_time: ≈ 2–3 hr (incl. agar autoclave); overnight incubation
---

# Plaque Assay — Soft-Agar Overlay Method

> **⚠️ This method failed on [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md)** — the 0.7 % soft agar did not solidify, so only partial coverage was obtained. The team's lesson was to **raise agar to 0.8 %** and **make extra**. See Notes section. The successor method actually adopted on 6-4 is [[plaque_assay_layered_plate]].

## Purpose
Mix bacterial culture into molten soft agar and pour onto a Petri dish to form a thin bacterial-bearing lawn layer. Once solidified, spot phage filtrate onto the surface; phages that successfully lyse the host produce visible clearings (plaques).

## Quick-lookup table — per-plate mix (as planned for 6-3)

| Component | Volume |
|---|---|
| 0.7 % LB soft agar (molten, 50 °C) | 5 mL |
| Bacteria sample (overnight culture) | 500 µL |
| **→ Total mix poured per plate** | **5500 µL** (notebook recorded as "2750 µL mixture" — `==CONFIRM: this is half the total, likely 2 plates per bacteria sample==`) |
| Phage filtrate (per spot, on solidified plate) | 0.2 mL (200 µL) |

## Materials & equipment
- 0.7 % LB soft agar — see [[lb_agar]] quick-lookup table. **Recommended: 0.8 %** based on lesson from 6-3 (see Notes).
- Petri dishes
- Overnight bacterial cultures (output of [[single_colony_inoculation]])
- Phage filtrates (output of [[phage_isolation]])
- 50 °C water bath (to keep soft agar molten)
- Pipettes + tips
- Marker (to subdivide plates and label sectors)

## Reagents
- 0.7 % (or 0.8 %, recommended) soft [[lb_agar]] — molten, held at 50 °C
- Overnight bacterial culture (output of [[single_colony_inoculation]])
- Phage filtrate (output of [[phage_isolation]])
- Optional: [[phage_buffer]] for any dilution steps

## Procedure
1. **Autoclave soft agar.** Per [[lb_agar]] (0.7 % recipe), 50 mL LB broth + 0.35 g agar → cap loosely with autoclave tape (Autoclave Indicator Tape) over the cap, then autoclave 1 hr. Keep molten in a **50 °C water bath**. (Recommend 0.8 % per the failure lesson.)
2. **Mix per-plate volumes** for each bacteria sample:
   - 5 mL molten soft agar + 500 µL of one bacteria sample → quickly invert to mix.
3. **Pour the mix** over a Petri dish (or onto a hard-agar base for the related layered-plate method — see [[plaque_assay_layered_plate]]). Use **2 plates per bacteria sample** (≈ 2750 µL per plate).
4. **Subdivide plates with a marker** into 3 sectors so that 2 plates × 3 sectors = **6 different phage tests per bacteria sample**.
5. **Wait for solidification.**
6. **Spot 0.2 mL of each phage filtrate** (ϕ3 / ϕ5 / ϕ6 / ϕ8 / ϕ9 / ϕ10) onto its assigned sector.
7. Wait for the spot to absorb.
8. Incubate inverted (lid on the bottom) at **30 °C** overnight.

## Notes / common deviations
- **Failure mode on 6-3.** Plates did not solidify at 0.7 %. Only the following bacteria × phage combinations had readable coverage:
  - `10-10-2` × phages 3 / 5 / 6 / 8 / 9 / 10
  - `6-3-2` × phages 3 / 5 / 6 / 8 / 9 / 10
  - `10-9-2` × phages 3 / 5 / 6
  - `8-2-2` × phages 8 / 9 / 10
- **Lessons (from 6-3 "Learning from the day"):**
  1. Make extra LB agar (e.g., 2 × 50 mL).
  2. Raise the concentration to **0.8 %** so it actually solidifies.
- **Successor method:** the team moved to [[plaque_assay_layered_plate]] (poured over a hard agar base) on 6-4 — more robust for the subsequent runs.

## Checklist — where do the outputs go?
- [ ] Inoculated / poured plates → **30 °C incubator**, **inverted** (lid on bottom).
- [ ] Phage filtrates after use → return to **4 °C fridge**.
- [ ] Failed / un-solidified plates → [[media_disposal]].

## Source
- Lab notebook: [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (Procedures ①–②, Deviation, Learning).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry, including the failure record + lesson.
- 2026-06-08 — Added autoclave-tape instruction (cap loosely with **Autoclave Indicator Tape** over the cap before autoclaving) to the soft-agar prep step.
