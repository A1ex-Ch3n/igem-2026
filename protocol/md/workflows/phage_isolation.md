---
title: Phage Isolation from Enrichment (Centrifuge + 0.22 µm Filter)
type: workflow
purpose: Recover cell-free phage filtrate from a phage-enriched broth by removing bacterial cells via centrifugation and sterile filtration.
references:
  - "[[soil_enrichment_phage]]"
  - "[[phage_purification]]"
source:
  - lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md
  - lab_notebook/digitalized/2026-06-09_bacteria-culture-phage-isolation.md
  - protocol/Genomic_And_Phage_Work.docx
estimated_time: ≈ 30 min for 6 enrichments (bulk filtration)
---

# Phage Isolation from Enrichment

## Purpose
After [[soil_enrichment_phage]], the enriched broth still contains bacteria, debris, and any phage amplified during the enrichment. This protocol removes cells and debris by centrifugation followed by 0.22 µm sterile filtration, leaving a cell-free filtrate that contains only sub-bacterial particles — the working phage stock.

## Materials & equipment
- 15 mL falcon tubes (one per enrichment)
- Centrifuge (rotor + balance)
- Syringes
- 0.22 µm syringe filters (one per enrichment)
- Fresh falcon tubes for filtrate collection
- Marker / labels

## Reagents
- Phage-enriched broth (output of [[soil_enrichment_phage]]) — no chemical reagents are added in this protocol; the procedure is purely physical separation (centrifugation + 0.22 µm filtration).

## Procedure — Variant A: bulk filtration (team — as run [6-2](../../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md))

Process each enrichment in one batch of its full volume.

1. **Transfer enrichment to falcon tubes.** Pipette **12 mL of [[soil_enrichment_phage]] broth** into a 15 mL falcon tube. Label each tube with the source sample number. Repeat for all enrichments.
2. **Centrifuge.** Spin 6 falcon tubes at a time:
   - **2,800 rpm**
   - **5 min**
   - Balance tubes (opposite positions in the rotor).
3. **Filter the supernatant.** Draw the supernatant into a syringe in **5 mL aliquots per pull**, then push through a **0.22 µm syringe filter** into a fresh, labelled falcon tube.
4. The filtrate that comes out the other side of the filter is the **isolated phage stock** (`ϕ<n>` where `n` is the source enrichment number).
5. Cap, label with sample ID + collection date, transfer to fridge (see Checklist).

## Procedure — Variant B: daily aliquot (prof — `Genomic_And_Phage_Work.docx` Part 2) — DEPRECATED

> [!failure] DEPRECATED 2026-06-06 — upstream context removed from prof's `Genomic_And_Phage_Work.docx`
> Variant B was the daily-aliquot scheme paired with the host-amplification protocol (steps 15–17 of `Genomic_And_Phage_Work.docx`). Prof crossed out steps 15–17 on / before 2026-06-06 — there is no longer a host-amplification step to pull daily aliquots from. The simplified pipeline goes `[[soil_enrichment_phage]] → Variant A bulk filtration → plaque assay → [[phage_purification]]` with no daily-aliquot stage.
>
> **Team status:** team **never executed** Variant B (no host amplification was ever set up). Content kept as historical reference. Use **Variant A** above for all phage isolation.

1. ~~**Each day**, harvest a **1.4 mL aliquot** of the enrichment culture into a separate microcentrifuge tube.~~
2. ~~**Centrifuge** to pellet the bacteria.~~
3. ~~**Filter the supernatant** through a **0.22 µm syringe filter** into a fresh, labelled tube.~~
4. ~~**Store the filtrate at 4 °C.** (These daily stocks are not pure and will not last long — process to [[phage_purification]] promptly.)~~
5. ~~**Repeat for 1–2 additional days** (once per day), giving 2–3 daily filtrates per enrichment.~~

> [!tip] iGEM 26 team practice — confirmed 2026-06-06 (pending teammate cross-check)
> The team's actual practice is **Variant A** (bulk filtration, as run on [2026-06-02](../../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md)): 12 mL of soil-enrichment broth per falcon tube → 2,800 rpm × 5 min → 5 mL aliquots through 0.22 µm syringe filter → 4 °C. Variant B above is deprecated and kept only as historical reference.

## Quick-lookup table — round 1 outputs (2026-06-02)

| Source enrichment | Phage stock label |
|---|---|
| #3 | ϕ3 |
| #5 | ϕ5 |
| #6 | ϕ6 |
| #8 | ϕ8 |
| #9 | ϕ9 |
| #10 | ϕ10 |

(Source: photo `../../../photos/0605/` "phage isolation round 1, 4/6/2".)

## As-run record — round 2 (2026-06-09): smaller tubes, higher speed

A second isolation round on [2026-06-09](../../../lab_notebook/digitalized/2026-06-09_bacteria-culture-phage-isolation.md) processed a fresh soil enrichment with the **same Variant A logic (centrifuge + single 0.22 µm filtration)** but **different vessel/speed parameters** — recorded here side-by-side with the 6-2 parameters (don't overwrite):

| Parameter | Round 1 (6-2) | Round 2 (6-9) |
|---|---|---|
| Vessel | 15 mL falcon, 12 mL/tube | **2 mL microcentrifuge tubes**, 4 tubes/enrichment (24 tubes, 2 runs) |
| Spin | 2,800 rpm × 5 min | **higher speed × ~5 min** `[TBD: exact speed — notebook reads "5×g", a misread]` |
| Filtration | 5 mL pulls through 0.22 µm (single pass) | draw supernatant → **single 0.22 µm syringe-filter** into new 2 mL tube |
| Output | ϕ3/5/6/8/9/10 → 4 °C | **ϕ3/5/6/8/9/10** (same 6 sites), ~2–3 mL each → 4 °C |

**Lesson (6-9): the higher centrifuge speed gave a visibly cleaner / smoother / less-smelly supernatant** than the 6-2 round — a worthwhile parameter change for future rounds.

## Notes / common deviations
- **Higher centrifuge speed → cleaner supernatant (6-9).** The 2026-06-09 round spun at a higher speed than the 6-2 round (in 2 mL microcentrifuge tubes) and got a visibly cleaner, less-smelly supernatant before filtration — see the round-2 table above.
- The centrifugation removes intact cells; the 0.22 µm filtration removes anything cell-sized that's left. Together they give a "cell-free lysate" — i.e., anything that grows from this on a host lawn is necessarily a sub-bacterial particle (phage being the most likely).
- **Downstream pipeline (simplified per prof's 2026-06-06 update):** this protocol feeds → [[plaque_assay_layered_plate]] (the team's screening method) → [[phage_purification]] (3 rounds of single-plaque re-isolation) → phage DNA extraction → sequencing. The previously-planned `[[phage_amplification]]` (host amplification) and `[[spot_testing]]` (multi-spot screening) steps are deprecated and no longer in the pipeline.
- **Iterative re-isolation lives in [[phage_purification]].** That's the protocol that picks a single plaque from a positive assay, re-elutes it into [[phage_buffer]], and re-plates on a fresh lawn — repeated ≥ 3 times to drive the lysate toward monoclonality. Re-isolation rounds 2 and 3 are currently UNDONE in the scheme.

## Checklist — where do the outputs go?
- [ ] Phage filtrate (working stock) → **4 °C fridge**, in fresh capped falcon tube.
- [ ] Spent enrichment / cell pellets from the centrifugation → [[media_disposal]] (or recover for separate bacteria sequencing if appropriate).
- [ ] Used syringes / filters → biohazard waste per local guidance.

## Source
- Lab notebook: [2026-06-02](../../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md) (Procedure for ② — Variant A bulk filtration), [2026-06-09](../../../lab_notebook/digitalized/2026-06-09_bacteria-culture-phage-isolation.md) (round 2 — 2 mL tubes, higher speed, single filter).
- [`../Genomic_And_Phage_Work.docx`](../../Genomic_And_Phage_Work.docx) — Part 2: Phage Isolation & Enrichment from Soil (step 14 Filtering → Variant A here; Variant B daily-aliquot scheme **deprecated** 2026-06-06 along with the now-removed steps 15–17).
- Photo evidence: `../../../photos/0605/` (round-1 phage isolation rack).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry.
- 2026-06-05 — Restructured Procedure into **Variant A** (team's bulk filtration, as run 6-2) + **Variant B** (prof's daily-aliquot scheme paired with [[phage_amplification]]). Both variants preserved per *the project rule of preserving all version variants from disagreeing sources*. Added cross-refs to the new [[phage_amplification]] (upstream of Variant B) and [[phage_purification]] (downstream re-isolation rounds). Added G&PW as a Source.
- 2026-06-06 — Added **iGEM 26 team practice** spotlight callout flagging **Variant A** (bulk filtration, as run 6-2) as the team's actual practice; Variant B kept for when the team starts running [[phage_amplification]]. Pending teammate cross-check.
- 2026-06-06 — **Deprecated Variant B** (daily-aliquot scheme). Prof crossed out steps 15–17 of `Genomic_And_Phage_Work.docx` (Enrichment Set-Up + Incubation + Daily phage Sampling), eliminating the upstream host-amplification step that Variant B fed off. Variant B procedure steps struck through but content preserved as historical reference; references frontmatter no longer links `[[phage_amplification]]`; "Downstream pipeline" Note updated to the simplified path `phage_isolation → plaque_assay_layered_plate → phage_purification`. Variant A unchanged. Prof's separate "filter 2×" update to step 14 deliberately **not yet applied** — pending team discussion.
- 2026-06-08 — Proofread fixes (**#7** + **#5**): Variant A step 5 "label with sample ID + isolation round number" → "label with sample ID + collection date" (Variant B was the multi-round one; now deprecated, "round number" no longer applies). Spin-format house style: 2800 rpm → 2,800 rpm.
- 2026-06-09 — Added an **as-run round-2 record** (2026-06-09): 2 mL microcentrifuge tubes + higher centrifuge speed → cleaner supernatant, then the **same single 0.22 µm filtration** as 6-2 (preserved 6-2's parameters side-by-side, didn't overwrite). Added the cleaner-supernatant lesson to Notes + 6-9 to `source:`. **Prof's "filter 2×" update remains NOT adopted** — the team confirmed 6-9 followed the 6-2 single-filter procedure, so it stays pending team discussion.
