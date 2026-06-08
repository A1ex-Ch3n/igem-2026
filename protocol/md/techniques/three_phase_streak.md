---
title: Three-Phase Streak Plate
type: technique
purpose: Mechanical isolation of single bacterial colonies from a liquid enrichment by progressive dilution across three regions of an agar plate.
references:
  - "[[pmm]]"
  - "[[soil_enrichment_bacteria]]"
  - "[[soil_enrichment_phage]]"
source:
  - lab_notebook/digitalized/2026-05-22_streak-test-trial.md
  - lab_notebook/digitalized/2026-05-26_streak-soil-enrichment.md
estimated_time: ~ 2 min per plate; full panel of 60 plates ≈ 1.5 hr
---

# Three-Phase Streak Plate

## Purpose
Mechanically dilute a bacterial suspension across the surface of a solid plate so that, by the third region, individual cells are deposited far enough apart to grow into isolated single colonies. Used to recover *Pseudomonas* candidates from soil enrichments on [[pmm]] plates.

## Materials & equipment
- Agar plates ([[pmm]] for the project's primary use)
- Inoculation loops:
  - 1 µL loops (5-22 trial run)
  - Sterilized loops, one per sample (5-26 real run; **6 loops** used for 6 enrichments)
- Source bacterial suspension (e.g., soil enrichment)
- Bunsen burner (for flame sterilization between phases)
- Marker for plate labels

## Reagents
- Source bacterial suspension (typically a soil enrichment — see [[soil_enrichment_bacteria]] or [[soil_enrichment_phage]])
- Agar plates ([[pmm]] for the project's primary use)

## Procedure
1. Label the plate (sample ID, date) on the bottom edge.
2. Mentally divide the plate into **three blocks** of decreasing density (see diagram on p.14 of the notebook). For visual reference: "most intense" → "less / medium" → "dilute".
3. Dip a sterile loop in the source suspension.
4. **Block 1 — most intense:** streak the loop in a back-and-forth zig-zag across roughly one-third of the plate surface, depositing the bulk of the cells.
5. Sterilize the loop (or use a fresh loop) before moving to Block 2.
6. **Block 2 — medium:** start the streak by **overlapping** the end of Block 1, then drag into the fresh region. This carries a small fraction of cells from Block 1 into a new area.
7. Sterilize the loop again.
8. **Block 3 — dilute:** start by overlapping the end of Block 2, then streak across the final third. By this point cells should be sparse enough to grow as isolated colonies.
9. Replace the lid and incubate (see Checklist).

## Notes / common deviations
- **Overlap matters.** On 5-22 the team initially did *not* overlap streaks. The PI corrected the technique — successive streaks must start at the endpoint of the previous one. The 5-26 real run does overlap correctly.
- **Don't tear the agar.** Apply just enough pressure to deposit cells; tearing the agar surface creates artefacts.
- **Loop hygiene.** On 5-22 Olivia forgot to change the loop between two of her replicates ("Olivia forgot to change the loop :("), which is a confounded result — always change/sterilize the loop between blocks and between samples.
- **Duplication.** On 5-22 the team plated 4 replicates per enrichment as a control for loop / streaking artefacts — if all 4 fail it's probably the loop, not the bacteria.
- Expected output: isolated single colonies visible after incubation, ready for picking into liquid culture (see [[single_colony_inoculation]]).

## Checklist — where do the outputs go?
- [ ] Streaked plates → **30 °C incubator** (or per the source organism's optimum — project default is 30 °C).
- [ ] After overnight growth and inspection → **4 °C fridge**, sealed, until colonies are picked.

## Source
- Lab notebook: [2026-05-22](../../../lab_notebook/digitalized/2026-05-22_streak-test-trial.md) (trial run, diagram), [2026-05-26](../../../lab_notebook/digitalized/2026-05-26_streak-soil-enrichment.md) (real run, three-phase method with overlap).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entries.
- 2026-06-08 — Proofread improvement (**#17**): added `[[soil_enrichment_bacteria]]` and `[[soil_enrichment_phage]]` to frontmatter `references:` list (they were already cross-refed in the body Reagents section — frontmatter just needed to match).
