---
title: Plaque Assay — Layered-Plate Method (Top Agar over Hard Base)
type: workflow
purpose: Detect phage activity by pouring a bacteria + phage soft-agar mixture over a pre-solidified hard agar plate as the base.
references:
  - "[[lb_agar]]"
  - "[[lb_broth]]"
  - "[[phage_buffer]]"
  - "[[phage_isolation]]"
  - "[[single_colony_inoculation]]"
source:
  - lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md
estimated_time: ≈ 2–3 hr setup + overnight incubation
---

# Plaque Assay — Layered-Plate Method

## Purpose
Combine actively growing bacteria, soft agar, and phage filtrate in a falcon tube, then pour the mixture as an overlay onto a pre-solidified hard agar plate. The hard base provides a reliable platform that prevents the soft-agar layer from failing to solidify (the failure mode of the [[plaque_assay_soft_agar]] method).

This was the **second** plaque assay attempt by the project, after the 6-3 soft-agar overlay attempt failed.

## Quick-lookup table — per-plate mix (as used on 6-4)

| Component | Volume |
|---|---|
| 0.7 % LB soft agar (molten, 50 °C) | 3 mL |
| Actively grown bacteria (overnight culture) | 250 µL |
| Phage filtrate (ϕ8 / ϕ9 / ϕ10) | 10 µL |
| **→ Poured onto** | one pre-solidified hard agar plate |

> **Scale (6-4 run):** 30 plates total = **3 phages (ϕ8, ϕ9, ϕ10) × 10 bacteria samples**.

## Materials & equipment
- Pre-solidified hard agar plates (1 % LB agar) — see [[lb_agar]] quick-lookup table
- Molten 0.7 % LB soft agar in a **50 °C water bath** — see [[lb_agar]]
- Falcon tubes (one per plate)
- Pipettes + tips
- Phage filtrates ([[phage_isolation]] outputs)
- Actively grown bacteria ([[single_colony_inoculation]] outputs)
- Alcohol burner (the 6-4 notebook explicitly notes turning on the burner while staging falcon tubes)

## Reagents
- Pre-solidified 1 % hard [[lb_agar]] plates (base layer)
- 0.7 % soft [[lb_agar]] — molten, held at 50 °C (overlay)
- Actively grown bacterial culture (output of [[single_colony_inoculation]])
- Phage filtrate (output of [[phage_isolation]])
- Optional: [[phage_buffer]] for any dilution steps

## Procedure
1. **Prepare the 0.7 % soft agar:** per [[lb_agar]] — 100 mL LB broth + 0.7 g agar; autoclave 30 min in a 200 mL bottle.
   - Notebook 6-4 totals: 3 mL × 30 plates = 90 mL needed; made 100 mL.
2. **Warm the water bath to 50 °C** (to keep soft agar pourable but cool enough not to kill bacteria).
3. **In a falcon tube**, combine:
   - 3 mL of molten 0.7 % soft agar
   - 250 µL of actively grown bacteria
   - 10 µL of phage filtrate (ϕ8 / ϕ9 / ϕ10 per plate)
4. **Pour the falcon-tube contents** onto a pre-solidified hard agar plate. Discard the empty falcon tube.
5. **Tilt the plate** so the new agar layer covers the entire surface.
6. **Repeat steps 3–5** for the remaining ~9 plates per group.
7. **Wait until the last 3 plates have solidified (≈ 10 min).**
8. Place plates in the **30 °C incubator**, **upside-down (lid on the bottom)**. The 6-4 entry trails off mid-sentence here ("The middle of …") — `[TBD: confirm final plate-placement detail.]`

## Plate-labelling convention (per 6-4 left-margin illustration)
Each plate gets a three-row label:
1. **Date** (e.g., `26/6/4`)
2. **Phage ID** — `ϕ<n>`, where `n` = soil enrichment the phage filtrate came from
3. **Bacteria label** (e.g., `8-8-2` — format `sample_site.duplicate.plate_half`)

## Notes / common deviations
- **3 phages × 10 bacteria = 30 plates** in 3 groups of 10. Each group uses one phage (ϕ8, ϕ9, or ϕ10) across all 10 bacteria samples.
- Phage filtrate is kept at **4 °C** between transfers to the falcon tube — the 6-4 right margin notes "4 °C" near step 4.
- Lessons from the prior 6-3 failure are baked into this method: the hard agar base + smaller overlay volume per plate (3 mL vs 5.5 mL) makes solidification more reliable.

## Checklist — where do the outputs go?
- [ ] Poured plates (after the 10-min solidification wait) → **30 °C incubator**, inverted (lid on bottom).
- [ ] Phage filtrate aliquots after use → return to **4 °C fridge**.
- [ ] Soft-agar leftovers / failed pours → [[media_disposal]].

## Source
- Lab notebook: [2026-06-04](../../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) (Procedure ①).
- User confirmation in chat (2026-06-05): "Second plaque run only has thirty plates, and it's the combination of 3 phages (8, 9, 10) and 10 bacteria samples."

---
## Log
- 2026-06-05 — Initial draft from lab notebook + user clarification on 30-plate / 3-phage / 10-bacteria layout.
