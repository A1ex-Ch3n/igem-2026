---
title: Bacteria Pellet Preparation for Sequencing
type: workflow
purpose: Wash and pellet overnight bacterial cultures into clean cell pellets ready for whole-genome sequencing.
references:
  - "[[single_colony_inoculation]]"
  - "[[bacteria_genome_extraction]]"
source:
  - lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md
  - protocol/Genomic_And_Phage_Work.docx
estimated_time: ≈ 1 hr for ~10 samples
---

# Bacteria Pellet Preparation for Sequencing

## Purpose
Concentrate an overnight liquid bacterial culture into a washed cell pellet free of growth medium and extracellular debris, ready for downstream DNA extraction ([[bacteria_genome_extraction]]) and whole-genome sequencing.

## Quick-lookup table — centrifugation conditions (variants preserved per source)

Two recorded specs for the harvest spin — the team's two-stage scheme (used 6-3) and the prof's single-stage spec. Both produce washed pellets; the team's scheme is what's reflected in the project record below.

| Source | Vessel | Speed | Time | Use |
|---|---|---|---|---|
| **Team — as run [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md)** | 15 mL falcon tube | **3,000 rpm** | **15 min** | First pellet from overnight culture; PBS washes |
| **Team — as run [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md)** | 2 mL Eppendorf | **10,000 × g** | **10 min** | Final wash & pellet, ready for storage |
| **Prof — `Genomic_And_Phage_Work.docx` Part 1** | centrifuge tube (sized to overnight culture, typically 15 mL or 50 mL) | **4,000 rpm** | until a bacterial pellet forms | One-stage harvest of the entire culture |

> [!tip] iGEM 26 team practice — confirmed 2026-06-06 (pending teammate cross-check)
> The team uses the **two-stage scheme** (rows 1 + 2 above): start in the 15 mL falcon tube at 3,000 rpm × 15 min for the initial pellet + PBS washes, then transfer to a 2 mL Eppendorf and finish at 10,000 × g × 10 min. Prof's one-stage 4,000 rpm variant (row 3) is recorded for reference but not adopted — the two-stage scheme gives a smaller final tube volume that's easier to carry into [[bacteria_genome_extraction]] downstream.

## Materials & equipment
- 15 mL falcon tubes
- 2 mL Eppendorf tubes
- Pipettes (1 mL, 5 mL)
- PBS (commercial 1×)
- Centrifuge — must accept both falcon tubes and Eppendorf tubes (or two centrifuges)
- −20 °C freezer

## Reagents
- Overnight bacterial cultures (output of [[single_colony_inoculation]])
- PBS (1 ×, commercial)

## Procedure
1. **Pool overnight cultures into falcon tubes.** Add tubes #1 and #2 from the source culture into one 15 mL falcon tube (per 6-3 step 1; for the project this combined the duplicate inoculations from 6-2).
2. **First spin.** Centrifuge at **3,000 rpm for 15 min** (balanced). Pour off the supernatant to waste.
3. **First wash.** Resuspend the pellet in **5 mL of PBS**. Centrifuge again at **3,000 rpm for 15 min**. Pour off the supernatant.
4. **Second wash.** Repeat step 3 (i.e., a second 5 mL PBS wash and second 3,000 rpm × 15 min spin).
5. **Transfer to Eppendorf.** Wash with **1.5 mL PBS**, transfer the suspension into a 2 mL Eppendorf tube.
6. **Final pellet.** Centrifuge the Eppendorf at **10,000 × g for 10 min**. Pour the supernatant to waste.
7. **Store the pellet at −20 °C** until DNA extraction / sequencing submission.

## Project record (2026-06-03)
Pellets prepared for sequencing from **10 cultures**:
`9-2-2`, `10-9-2`, `8-5-2`, `8-3-2`, `9-2-1`, `6-3-2`, `8-2-2`, `10-10-2`, `8-5-2`, `9-6-2`

`==CONFIRM: cross-day inconsistency — the 6-3 pellet list (this page) shows `8-5-2 × 2` + `8-3-2 × 1`, but the 6-05 lab-notebook entry's Set A bacterial-genome extracts records the opposite (`8-3-2 × 2` + `8-5-2 × 1`). One of these was mislabelled — verify against the physical freezer rack. See [`2026-06-05_…md`](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) Procedure ③ for the original cross-day flag.==`

Photo evidence: `../../../photos/0605/` "6/3 bacteria pellet for sequencing".

## Notes / common deviations
- The two centrifugation speeds (3,000 rpm in falcon tubes, 10,000 × g in Eppendorfs) are appropriate for the respective vessels — large bottles can't spin at high g without unsafe rotor stresses, but small tubes pellet faster at high g.
- The 6-3 entry includes a parenthetical note that on the same day the team **"continued on p.26"** for the final Eppendorf spin — i.e., the full procedure spans both notebook pages 24 and 26.
- The "Experiment notes" block on 6-3 also records future-use parameters that are already incorporated above.
- **Downstream:** the stored pellets are processed through [[bacteria_genome_extraction]] (Quick-DNA Miniprep Kit) → [[dna_quantification_qubit]] → whole-genome sequencing. The 6-05 lab notebook entry shows the end-to-end run that took these pellets through extraction and quant.
- **Prof's alternative (one-stage harvest):** `Genomic_And_Phage_Work.docx` Part 1 describes a simpler one-stage spin at 4,000 rpm until a pellet forms (no separate Eppendorf transfer). Either approach works; the team's two-stage scheme gives smaller final tube volume for downstream extraction.

## Checklist — where do the outputs go?
- [ ] Washed bacterial pellets in 2 mL Eppendorfs → **−20 °C freezer**, ready for sequencing.
- [ ] Used PBS supernatants → [[media_disposal]] (or sink with bleach treatment per [[media_disposal]] guidance).

## Source
- Lab notebook: [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (Procedure ③ — `Prepare bacteria pellets`, plus the Experiment notes block).
- Photo evidence: `../../../photos/0605/` (6/3 bacteria-pellet rack).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry + 6-3 photo from `photos/0605/`.
- 2026-06-05 — Added the prof's **one-stage 4,000 rpm** spin from `Genomic_And_Phage_Work.docx` as a third row in the centrifugation quick-lookup table — both variants preserved per *the project rule of preserving all version variants from disagreeing sources*. Added downstream cross-ref to [[bacteria_genome_extraction]] (new) so the pipeline reads forward into DNA extraction. Added G&PW as a Source.
- 2026-06-06 — Added **iGEM 26 team practice** spotlight callout flagging the **two-stage scheme** (3,000 rpm in falcon → 10,000 × g in Eppendorf) as the team's actual practice; prof's 4,000 rpm one-stage variant kept for reference. Pending teammate cross-check.
- 2026-06-08 — Proofread fix (**#3**): updated the `==CONFIRM==` marker on the `8-5-2` duplicate to record the **cross-day discrepancy** with the 6-05 lab notebook (today's Set A is `8-3-2 × 2 + 8-5-2 × 1` — the opposite of this 6-3 record). One of the two days mislabelled; needs physical freezer-rack verification.
- 2026-06-08 — Proofread fix (**#5** — spin format house style): standardized RPM values to use a comma (3,000 / 4,000 — was 3000 / 4000) and `g` values to use the `× g` symbol (10,000 × g — was 10,000 g). Applies throughout the file; no underlying values changed.
