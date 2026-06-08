---
title: Metagenomic DNA Extraction from Soil (Kit-Based)
type: workflow
purpose: Extract whole-community DNA directly from soil samples — no culturing step — to produce input for metagenomic sequencing.
references: []
source:
  - lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md
  - lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md
  - lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md
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
1. **Follow the kit's manufacturer instructions** for soil samples exactly. The 5-20 entry phrases the procedure as "Followed the guidance for soil sample in the kit; did 10 groups of DNA extraction." Replicate the kit's exact protocol on the day — do not improvise on lysis, binding, or elution.
2. Label each DNA filtrate output as **Metagenomic Sample <site#>** with the date.
3. Store at **4 °C fridge** until [[dna_quantification_qubit]].

## Project record — extraction batches

| Date | Batch | Soil sites used | Outcome |
|---|---|---|---|
| [2026-05-20](../../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) | First trial | **All 10 soil sites (#1–#10)** | [[dna_quantification_qubit]] on 5-27 failed for samples 1–9; only #10 read above detection. Conclusion: redo selected samples. |
| [2026-05-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) | Second trial — re-extraction | **#1, #3, #4, #7** (selected from the original 10-site collection for a re-pull; per labelled rack + photo `photos/0605/`) | [2026-06-05](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) Qubit re-quant: concentrations still **low** across all 4 samples; mixing batch-1 + batch-2 samples (**M1 / M3 / M4 / M7 mix** — one mix per 2nd-batch site #1, #3, #4, #7) did not recover usable concentration. |
| **Planned next** | Third trial — small-biomass | All 10 sites, **smaller per-sample soil mass** (PI suggestion to avoid silica-column saturation by soil particulates). | UNDONE. `[TBD: target soil mass per tube — possibly ~12.5 mg vs the standard 1 g; confirm.]` |

## Notes / common deviations
- The 5-28 procedure for the 2nd DNA extraction is described as "same as 1st DNA Extraction" — i.e., reuse this protocol identically.
- Worth recording in the per-day notebook entry: the **kit lot number** (in case extraction failures correlate with a particular lot).
- **Low-yield pattern across both batches** so far. PI's hypothesis: 1 g of soil saturates the Quick-DNA column with co-extracted inhibitors / particulates that compete with DNA binding. Mitigation = **smaller per-sample soil mass** for the next round of trials. Mixing two batches' eluates (tried 2026-06-05) did **not** recover concentration, so re-extraction with less soil is the path forward.

## Checklist — where do the outputs go?
- [ ] Eluted DNA filtrates → **4 °C fridge** until quantification.
- [ ] After successful quantification → **−20 °C freezer** for longer-term storage before submission for sequencing.
- [ ] Used kit consumables (lysis bead tubes, binding columns) → **media disposal** ([[media_disposal]]) or per kit-specific waste guidance.

## Source
- Lab notebook: [2026-05-20](../../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) (Procedure steps 1–2), [2026-05-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) (Procedure for ②).
- Photo evidence: `../../../photos/0605/` (labelled rack "26/05/28 second trial of soil DNA purification" with tubes #1, #3, #4, #7).

---
## Log
- 2026-06-05 — Initial draft. Kit identity is `[TBD]` — needs physical-box confirmation.
- 2026-06-05 — Filled in kit identity: **Quick-DNA™ Miniprep Kit (Zymo Research)** per user confirmation. Added 2026-06-05 re-quant outcome (low yields persisted; mix experiment didn't help) and planned small-biomass third trial.
- 2026-06-05 — Corrected project-record table: **first trial covered all 10 soil sites** (not 6 — the 6-site list was the bacterial enrichment, a different operation done the same day). Second trial reclassified as a "re-extraction of selected sites" rather than "the remaining sites".
- 2026-06-08 — Proofread fixes: (**#2**) corrected wrong mix labels — "M1 / M2 / M3 mix" → "**M1 / M3 / M4 / M7 mix**" to match the actual 6-05 lab-notebook record (one mix per 2nd-batch site #1, #3, #4, #7). (**#4**) added `2026-06-05_plaque-assay-r3-…md` to `source:` frontmatter — body had already referenced it but frontmatter missed the link.
