---
title: Phage Amplification on Host Isolate
type: workflow
purpose: Amplify a filtered phage stock on an actively-growing bacterial host isolate, harvesting daily aliquots of enriched filtrate to feed downstream spot testing / plaque assays / purification.
references:
  - "[[lb_broth]]"
  - "[[phage_buffer]]"
  - "[[single_colony_inoculation]]"
  - "[[phage_isolation]]"
  - "[[phage_purification]]"
source:
  - protocol/Genomic_And_Phage_Work.docx
estimated_time: ≈ 30 min setup; multi-day incubation with daily sampling
---

# Phage Amplification on Host Isolate

> [!failure] DEPRECATED 2026-06-06 — protocol removed from prof's `Genomic_And_Phage_Work.docx`
> Prof updated `Genomic_And_Phage_Work.docx` on / before 2026-06-06 and **crossed out steps 15–17** of the master protocol (Enrichment Set-Up → Incubation → Daily phage Sampling) — i.e., the entire host-amplification + daily-sampling routine that this protocol was drafted from. The phage workflow no longer includes this step.
>
> **What replaces it:** nothing direct — the simplified phage pipeline now goes `[[soil_enrichment_phage]] → [[phage_isolation]] → [[plaque_assay_layered_plate]] → [[phage_purification]]` (× 3 rounds). Mixed phage stocks from initial isolation feed plaque assay directly, with no host-amplification step in between.
>
> **Team status:** team **never executed** this protocol — it was a prof-only draft. Content below preserved as historical reference for what was originally planned. Do not run.

> **Status:** ~~Project has not yet executed this protocol — drafted verbatim from the prof's `Genomic_And_Phage_Work.docx` (Part 2, post-filtration steps). No team-recorded values exist yet.~~ → see DEPRECATED callout above.

## Purpose
Take a phage filtrate (the cell-free output of [[phage_isolation]] or a 6-2 working stock) and **amplify it on an actively-growing bacterial host isolate** so the phage population grows to titres useful for spot testing ([[spot_testing]]), plaque assays ([[plaque_assay_soft_agar]] / [[plaque_assay_layered_plate]]), and ultimately purification ([[phage_purification]]) → sequencing.

This is the **bridge step** between initial soil-derived filtrate and downstream plaque work — the initial filtrate from [[phage_isolation]] is rarely titred high enough on its own.

## Quick-lookup table — enrichment setup

| Component | Volume | Notes |
|---|---|---|
| Actively-growing bacterial host culture | **0.5 mL** | Prepared the same way as [[single_colony_inoculation]] for plaque-assay lawns |
| Phage filtrate ([[phage_isolation]] output) | **8–12 mL** | Depending on how much volume you successfully filtered |
| Daily harvest aliquot (per sampling day) | **1.4 mL** | Centrifuge → 0.22 µm filter → store at 4 °C |

## Materials & equipment
- Falcon tubes (one per enrichment, sized for ~8–13 mL total)
- Incubator (30 °C is project standard for the host) — preferably **shaking**; if not, tilt-and-shake periodically
- Centrifuge (for daily aliquot pellet step)
- Syringes + **0.22 µm syringe filters** (one per daily aliquot)
- Pipettes + tips
- Storage tubes for daily filtrates (4 °C fridge)

## Reagents
- **Actively-growing bacterial host culture** (overnight in LB broth) — see [[single_colony_inoculation]]
- **Phage filtrate** — output of [[phage_isolation]]
- [[lb_broth]] (if any top-up volume is needed)

## Procedure

### Setup (Day 0)
1. **Prepare an actively-growing bacterial isolate** following [[single_colony_inoculation]] — use the same host strain you plan to amplify the phage against.
2. **Set up the enrichment:** in a Falcon tube, mix:
   - **0.5 mL** of the growing bacterial culture
   - **8–12 mL** of your phage filtrate (depending on what was recovered from [[phage_isolation]])
3. **Incubate** the mixture for **a few days** at 30 °C to allow the phage population to enrich. Remember to **tilt and shake** the tube periodically if you are not using a continuous shaking incubator.

### Daily phage sampling (Days 1, 2, …)
4. Each day, harvest a **1.4 mL aliquot** of the enrichment culture into a separate microcentrifuge tube.
5. **Centrifuge** to pellet the bacteria.
6. **Filter the supernatant** through a **0.22 µm** syringe filter into a fresh, labelled tube.
7. **Store the filtrate at 4 °C** — this is your enriched phage **viral stock**. *(Note: these stocks are not yet axenic / pure and won't last a long time.)*
8. **Repeat steps 4–7 for 1–2 additional days** (once per day), giving 2–3 daily filtrates per enrichment.

## Notes / common deviations
- The **daily-sampling cadence** captures the phage population at different stages of amplification — typically the later samples have higher titre but may also accumulate bacterial debris.
- These stocks are **not pure** — they're a mixed population that needs [[phage_purification]] (3 rounds of single-plaque pick + re-plate) before phage DNA extraction and sequencing.
- The **0.5 mL bacteria + 8–12 mL filtrate** ratio gives the bacteria room to grow while ensuring the phage has many host targets — adjust if the bacterial culture is unusually dense or dilute.

## Checklist — where do the outputs go?
- [ ] Enrichment Falcon tube (during incubation) → **30 °C incubator** (shaking, or tilted manually).
- [ ] Daily filtered phage stocks → **4 °C fridge** (short-term — these are not stable for long).
- [ ] Pelleted bacteria from the daily aliquot → [[media_disposal]] (bleached) or saved for separate downstream analysis if needed.
- [ ] Spent enrichment at end of campaign → [[media_disposal]].

## Source
- [`../Genomic_And_Phage_Work.docx`](../../Genomic_And_Phage_Work.docx) — Part 2: Phage Isolation & Enrichment from Soil, post-filtration enrichment steps.

---
## Log
- 2026-06-05 — Initial draft from prof's `Genomic_And_Phage_Work.docx` Part 2 (amplification half). Project has not executed this protocol yet — no team-recorded values to fold in.
- 2026-06-06 — **DEPRECATED.** Prof crossed out steps 15–17 of `Genomic_And_Phage_Work.docx` (Enrichment Set-Up + Incubation + Daily phage Sampling) — i.e., the entire host-amplification routine this protocol was drafted from. Team never executed it. Content kept as historical reference; replaced in the project pipeline by going directly from [[phage_isolation]] → plaque assay → [[phage_purification]] with no in-host amplification step between.
