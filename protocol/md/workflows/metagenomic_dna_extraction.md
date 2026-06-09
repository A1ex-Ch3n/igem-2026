---
title: Metagenomic DNA Extraction from Soil (Kit-Based)
type: workflow
purpose: Extract whole-community DNA directly from soil samples — no culturing step — to produce input for metagenomic sequencing.
references: []
source:
  - lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md
  - lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md
  - lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md
  - lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md
estimated_time: per the kit's instructions
---

# Metagenomic DNA Extraction from Soil (Kit-Based)

## Purpose
Extract DNA directly from a soil sample — bypassing any enrichment or culturing step — to capture the full community in the soil as DNA suitable for metagenomic sequencing. The extract is later quantified by [[dna_quantification_qubit]] before submission for sequencing.

## Materials & equipment
- **Quick-DNA™ Miniprep Kit** (Zymo Research). `[TBD: catalog number + lot from the physical box.]`
- Flask (for any pre-processing steps the kit calls for)
- Scale (for weighing input soil to the kit's specification)
- 4 °C fridge (for storing the eluted DNA)

## Reagents
- Quick-DNA Miniprep Kit reagents (kit-supplied — lysis buffer, binding buffer, wash buffers, elution buffer)
- Soil sample (from [[soil_sample_collection]])

## Procedure

> [!note] Buffer / column names transcribed from the kit page
> The 13 steps below are transcribed from the printed kit "DNA Purification" page used on 2026-06-08 (`../../../lab_notebook/0608/IMG_4411.png`, with the team's run annotations). The named consumables (ZR BashingBead Lysis Tube, Zymo-Spin III-F, Zymo-Spin IICR, Zymo-Spin IV-HRC) and buffers (Genomic Lysis, DNA Pre-Wash, g-DNA Wash, DNA Elution) are recorded as written on that page. `[TBD: confirm the exact Quick-DNA kit/catalog from the physical box — these spin columns are the soil/fecal-microbe configuration of the Quick-DNA family.]`

1. **Add 0.12 g (120 mg) of soil** to a **ZR BashingBead Lysis Tube** (0.1 & 0.5 mm) and add **BashingBead Buffer**. This is the **small-biomass loading** — down from the team's earlier ~**1 g/tube** (which over-saturated the silica column and caused the 0527/0605 low yields), an ~8× per-tube reduction landing near the kit's 150 mg spec. Run 4 such tubes per site and pool them (step 13) to recover total DNA mass. *(Mass confirmed 2026-06-08; recorded in g because the lab scale has no mg mode.)*
2. **Bead-beat to lyse.** Kit recommendation is a dedicated bead-beater at high speed for ≥ 5 min; **the team used the vortex at level 3 (max) for 40 min**. *(Optional stopping point: samples can be stored after this step at −80 °C.)*
3. **Centrifuge** the BashingBead Lysis Tube at **≥ 10,000 × g for 1 min**.
4. **Transfer up to 400 µL supernatant** (P1000) to a **Zymo-Spin III-F Filter** in a collection tube; centrifuge at **8,000 × g for 1 min**; **discard the III-F filter**.
5. **Add 1,200 µL Genomic Lysis Buffer** (P1000) to the filtrate in the collection tube; mix well.
6. **Transfer 800 µL** of the step-5 mixture to a **Zymo-Spin IICR Column** in a collection tube; centrifuge at **≥ 10,000 × g for 1 min**.
7. **Discard the flow-through** and **repeat step 6** with the remaining mixture (load 800 µL ×2).
8. **Add 200 µL DNA Pre-Wash Buffer** to the IICR column in a new collection tube; centrifuge at **≥ 10,000 × g for 1 min**.
9. **Add 500 µL g-DNA Wash Buffer** to the IICR column; centrifuge at **≥ 10,000 × g for 1 min**.
10. **Transfer the IICR column to a clean 1.5 mL tube**; add **100 µL DNA Elution Buffer** (50 µL minimum; P200) directly onto the column matrix; centrifuge at **≥ 10,000 × g for 30 s** to elute. *(Team annotation: discard the old eppendorf, elute into a new one.)*
11. **Prepare a Zymo-Spin IV-HRC Filter:** loosen the cap, snap off the bottom tip, place in a clean collection tube, and centrifuge at **exactly 8,000 × g for 3 min**.
12. **Transfer the eluted DNA** onto the prepared **IV-HRC filter** (in a clean 1.5 mL tube); centrifuge at **exactly 8,000 × g for 30 s**. The filtered DNA is now suitable for PCR / downstream applications.
13. **Pool the parallel extractions: "mix 4 tubes into 1"** — the 6-8 small-biomass run split each sample across 4 lysis tubes and pooled the eluates to recover enough DNA. `[TBD: exact pooling ratio — annotation reads "1-1, 1, 1×1".]`
14. Label each pooled DNA eluate as **Metagenomic Sample <site#>** with the date. Store at **4 °C fridge**; concentrate via [[dna_concentration]] if the [[dna_quantification_qubit]] read is too dilute, then re-quantify.

## Project record — extraction batches

| Date | Batch | Soil sites used | Outcome |
|---|---|---|---|
| [2026-05-20](../../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) | First trial | **All 10 soil sites (#1–#10)** | [[dna_quantification_qubit]] on 5-27 failed for samples 1–9; only #10 read above detection. Conclusion: redo selected samples. |
| [2026-05-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) | Second trial — re-extraction | **#1, #3, #4, #7** (selected from the original 10-site collection for a re-pull; per labelled rack + photo `photos/0605/`) | [2026-06-05](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) Qubit re-quant: concentrations still **low** across all 4 samples; mixing batch-1 + batch-2 samples (**M1 / M3 / M4 / M7 mix** — one mix per 2nd-batch site #1, #3, #4, #7) did not recover usable concentration. |
| [2026-06-08](../../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) | Third trial — **small-biomass + pooling** | **#1, #6, #8, #9**, **0.12 g soil per BashingBead tube** (~8× down from the team's prior 1 g/tube), **4 tubes pooled per site** (step 13), then column-concentrated ([[dna_concentration]]) | **Worked.** Before/after concentration: #6 ~17×, #8 ~14×, #9 ~27× (lifted to 3.6–290 ng/µL); #1 ≈ 0 (no DNA). Sites #8/#9 sent for sequencing — see the 6-8 entry. |

## Notes / common deviations
- The 5-28 procedure for the 2nd DNA extraction is described as "same as 1st DNA Extraction" — i.e., reuse this protocol identically.
- Worth recording in the per-day notebook entry: the **kit lot number** (in case extraction failures correlate with a particular lot).
- **Low-yield pattern across both batches** so far. PI's hypothesis: 1 g of soil saturates the Quick-DNA column with co-extracted inhibitors / particulates that compete with DNA binding. Mitigation = **smaller per-sample soil mass** for the next round of trials. Mixing two batches' eluates (tried 2026-06-05) did **not** recover concentration, so re-extraction with less soil is the path forward.

## Checklist — where do the outputs go?
- [ ] Eluted DNA filtrates → **4 °C fridge** until quantification.
- [ ] After successful quantification → **−20 °C freezer** for longer-term storage before submission for sequencing.
- [ ] Used kit consumables (lysis bead tubes, binding columns) → **media disposal** ([[media_disposal]]) or per kit-specific waste guidance.

## Source
- Lab notebook: [2026-05-20](../../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) (Procedure steps 1–2), [2026-05-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) (Procedure for ②), [2026-06-08](../../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) (Procedure ④ + run params).
- Kit-protocol page: `../../../lab_notebook/0608/IMG_4411.png` (printed "DNA Purification" page, 13 steps, with the 6-8 run annotations).
- Photo evidence: `../../../photos/0605/` (labelled rack "26/05/28 second trial of soil DNA purification" with tubes #1, #3, #4, #7).

---
## Log
- 2026-06-05 — Initial draft. Kit identity is `[TBD]` — needs physical-box confirmation.
- 2026-06-05 — Filled in kit identity: **Quick-DNA™ Miniprep Kit (Zymo Research)** per user confirmation. Added 2026-06-05 re-quant outcome (low yields persisted; mix experiment didn't help) and planned small-biomass third trial.
- 2026-06-05 — Corrected project-record table: **first trial covered all 10 soil sites** (not 6 — the 6-site list was the bacterial enrichment, a different operation done the same day). Second trial reclassified as a "re-extraction of selected sites" rather than "the remaining sites".
- 2026-06-08 — Proofread fixes: (**#2**) corrected wrong mix labels — "M1 / M2 / M3 mix" → "**M1 / M3 / M4 / M7 mix**" to match the actual 6-05 lab-notebook record (one mix per 2nd-batch site #1, #3, #4, #7). (**#4**) added `2026-06-05_plaque-assay-r3-…md` to `source:` frontmatter — body had already referenced it but frontmatter missed the link.
- 2026-06-08 — **Replaced the thin "follow the kit" Procedure with the 13-step transcription** from the printed kit page (`0608/IMG_4411.png`) + the team's run annotations (40 min vortex level 3, IICR load 800 µL ×2, IV-HRC inhibitor-removal, "mix 4 tubes into 1"). Resolved the UNDONE "Planned next" project-record row → the executed **2026-06-08 small-biomass + pooling trial** on sites #1/6/8/9, feeding [[dna_concentration]]. Added the 6-8 entry + kit page to `source:`. Kit catalog still `[TBD]` (buffer/column names indicate the soil/fecal-microbe Quick-DNA configuration; not asserted per user — kept as Quick-DNA Miniprep).
- 2026-06-08 — **Per-tube input mass confirmed: 0.12 g** (user — lab scale has no mg mode). This is an ~8× reduction from the team's prior 1 g/tube (the over-loading that caused the 0527/0605 column saturation) → the genuine small-biomass fix, with 4 tubes pooled per site. Updated step 1 + the project-record row with the confirmed before/after result (#6 ~17×, #8 ~14×, #9 ~27×; #1 ≈ 0). Dropped the 0.12 g-vs-12.5 mg ambiguity.
