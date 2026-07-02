---
title: Single-Colony Inoculation into Liquid Culture
type: technique
purpose: Transfer one (or a defined small number of) isolated colony from a plate into liquid LB broth to grow a pure overnight culture.
references:
  - "[[lb_broth]]"
source:
  - lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md
  - lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md
  - lab_notebook/digitalized/2026-06-09_bacteria-culture-phage-isolation.md
  - lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md
  - lab_notebook/digitalized/2026-06-11_bacteria-culture-plaque-assay.md
  - lab_notebook/digitalized/2026-06-12_plaque-assay-extracted-phage.md
  - protocol/Genomic_And_Phage_Work.docx
estimated_time: ≈ 5 min per tube
---

# Single-Colony Inoculation into Liquid Culture

## Purpose
Take an isolated single colony (or a defined small number, e.g., 3 per plate for the 6-2 round) from an agar plate and grow it in liquid LB broth overnight. The resulting overnight culture feeds both bacterial sequencing prep ([[bacteria_pellet_for_sequencing]]) and plaque-assay lawn preparation.

## Materials & equipment
- LB broth tubes (sized per the use case — see [[lb_broth]])
- Rack
- Loop
- Pipette + tips (e.g., 5 mL)
- Source plate with isolated colonies (e.g., PIA plate from streak isolation)
- Bunsen burner or alcohol burner (for flame-sterilization, also for sterile zone)

## Quick-lookup table — colonies per tube (all recorded variants)

| Use case | Source | Colonies / tube | LB broth volume |
|---|---|---|---|
| Sequencing prep — 2nd DNA extraction | Team — as run [5-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) | 1 | **5 mL** |
| Phage-isolation round — next-round culture | Team — as run [6-2](../../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md) | 3 | **5 mL** `[TBD: confirm volume — notebook says "same as 5-28"]` |
| Sequencing prep — bacterial isolation & growth | Prof — `Genomic_And_Phage_Work.docx` Part 1 | 1 | **10 mL** |

> [!tip] iGEM 26 team practice — confirmed 2026-06-06 (pending teammate cross-check)
> The team uses the **5 mL** LB volume for both use cases above (1 colony for sequencing prep, 3 colonies for phage-isolation prep) — the prof's 10 mL variant is recorded for reference but the team has not adopted it. Volume choice between rows 1 and 2 is decided by what the culture feeds downstream:
> - **1 colony / 5 mL** → narrow downstream use (e.g., DNA extraction from a single isolate)
> - **3 colonies / 5 mL** → broader / scaled-up downstream use (e.g., a plaque-assay lawn, where colony diversity is OK)

## Reagents
- [[lb_broth]] (5 mL per tube)
- Source plate carrying isolated colonies (typically a PIA plate following [[pia]] + [[three_phase_streak]])

## Procedure
1. Pipette **5 mL** of [[lb_broth]] into each LB tube.
2. Label each tube with the source plate's number / colony ID.
3. Select and mark an isolated single colony on the source plate.
4. Pick that colony onto the loop and dissolve it into the LB broth in  the tube.
5. Repeat for the remaining plates / colonies.
6. Place the rack in the incubator (see Checklist).

## Notes / common deviations
- **Single colony for sequencing; 3 colonies for plaque assay.** Same procedure, different number of colonies picked per plate.
- **As run [2026-06-09](../../../lab_notebook/digitalized/2026-06-09_bacteria-culture-phage-isolation.md):** 3 colonies/plate into LB tubes, **~30 tubes** total (the "3 colonies / 5 mL" row above), scraping the colony surface gently (not too deep) and **changing the loop per colony**. `[TBD: confirm tube count; flagged inference that the source plates are the 6-8 revived P. aeruginosa candidate stocks.]`
- "Be careful of contamination!" appears explicitly in the 5-28 notebook entry — work in the sterile zone near the burner.
- On [2026-06-04](../../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) the team used **50 µL of an existing culture** as a 1:100 inoculum into fresh LB instead of picking from a plate ("Add 50 µL of first tube of bacteria to the new tube … 1:100 for bacteria culturing"). This is the **passage** variant of the technique — same idea, source is a liquid culture rather than a plate.
- **Passage variant, as run [2026-06-10](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) ③ and [2026-06-12](../../../lab_notebook/digitalized/2026-06-12_plaque-assay-extracted-phage.md) ①:** **5 mL LB broth + 50 µL of the prior overnight culture** per tube (same 1:100 passage as 6-04).
- **As run [2026-06-11](../../../lab_notebook/digitalized/2026-06-11_bacteria-culture-plaque-assay.md):** 10 isolates picked from LB plates (by Rafael) into tubes. **Cultures may show sediment & floc — vortex first, then pipette only the clear liquid on top** when using the culture downstream (e.g., for a plaque-assay lawn).
- **Prof's 10 mL volume** (`Genomic_And_Phage_Work.docx` Part 1) is recommended specifically for sequencing-prep inoculation — gives more total culture for the harvest spin in [[bacteria_pellet_for_sequencing]]. The team's 5 mL variant works for the project's scale but produces less pellet biomass per tube.

## Checklist — where do the outputs go?
- [ ] Inoculated LB tubes → **30 °C incubator**, rack with **tilted slope** to maximize surface area to oxygen (notebook 6-4 explicit guidance).
- [ ] After overnight growth → use immediately for downstream (sequencing prep, plaque-assay lawn, OD reading), or short-term **4 °C fridge** if delaying.

## Source
- Lab notebook: [2026-05-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) (single-colony version), [2026-06-02](../../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md) (3-colony version), [2026-06-04](../../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) / [2026-06-10](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) / [2026-06-12](../../../lab_notebook/digitalized/2026-06-12_plaque-assay-extracted-phage.md) (passage variant), [2026-06-11](../../../lab_notebook/digitalized/2026-06-11_bacteria-culture-plaque-assay.md) (10 isolates from LB plates; vortex sediment/floc).
- [`../Genomic_And_Phage_Work.docx`](../../Genomic_And_Phage_Work.docx) — Part 1: Bacterial Isolation & Growth (1 colony → **10 mL** LB variant for sequencing prep).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entries.
- 2026-06-05 — Added the prof's **10 mL** sequencing-prep variant as a third row in the quick-lookup table (alongside the team's two 5 mL rows). All three rows preserved per *the project rule of preserving all version variants from disagreeing sources*. Added G&PW as a Source.
- 2026-06-06 — Added **iGEM 26 team practice** spotlight callout flagging the two **5 mL** rows as the team's actual practice (1 colony for sequencing prep, 3 colonies for phage-isolation prep); prof's 10 mL kept for reference. Pending teammate cross-check.
- 2026-06-09 — Added a 6-9 as-run note (3 colonies/plate, ~30 tubes) + 6-9 to `source:`. Covered by the existing "3 colonies / 5 mL" quick-lookup row — no new variant.
- 2026-06-12 — Added 6-10/6-11/6-12 as-run notes: 6-10/6-12 passage (5 mL LB + 50 µL prior culture, same 1:100 as 6-04); 6-11 (10 isolates from LB plates by Rafael; vortex sediment/floc, pipette clear top). Added 6-10/6-11/6-12 to `source:`. No new variant rows.
