---
title: Soil Enrichment — Bacteria (PMM-based)
type: workflow
purpose: Enrich Pseudomonas-capable bacteria from a soil sample by inoculating into PMM-based selective broth.
references:
  - "[[pmm]]"
source:
  - lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md
  - protocol/PMM_ProtocoL (1).docx
estimated_time: ≈ 30 min setup; enrichment grows over several days
---

# Soil Enrichment — Bacteria (PMM-based)

## Purpose
Inoculate soil into a Pseudomonas-selective liquid medium so that *Pseudomonas* (and other bacteria able to grow on PMM) outgrow the rest of the soil community. The resulting enrichment broth becomes the input for streak isolation on solid PMM plates ([[three_phase_streak]] → [[pmm]]).

## Materials & equipment
- Flasks (one per sample)
- Scale (for soil mass)
- PMM broth — see [[pmm]] (use the broth form, no agar)

## Reagents
- [[pmm]] (broth form — no agar)
- Soil sample (from [[soil_sample_collection]])

## Procedure
1. Prepare PMM broth following [[pmm]] (Variant A — notebook 5-21 recipe — without agar).
2. For each soil sample to enrich:
   - Add `[TBD: specific soil mass — notebook 5-20 says "Prepared 6 soil sample enrichment in a flask. Ingredients:" then trails off. The 6-1 phage enrichment uses 1 g soil + 25 mL LB broth; the bacterial-enrichment ingredient ratio is not written in the 5-20 entry.]` soil to a flask.
   - Add `[TBD: PMM broth volume per flask]`.
3. Cap and incubate at `[TBD: temperature & duration — not documented in 5-20]`.

## Selected samples (project record)
On 2026-05-20 the team enriched **6 of the 10 collected sites**: **#2, #5, #6, #8, #9, #10**.

## Notes / common deviations
- The 5-20 notebook entry trails off mid-recipe ("Ingredients:" with nothing after). The user has confirmed the recipe should be pulled from [`../PMM_ProtocoL (1).docx`](../../PMM_ProtocoL%20(1).docx). Fill the `[TBD]` entries above when the team confirms the exact mass/volume ratio they used.
- This protocol is the **bacterial** track. The **phage** track ([[soil_enrichment_phage]]) uses plain LB broth instead — different medium, different selection.

## Checklist — where do the outputs go?
- [ ] Inoculated enrichment flasks → **30 °C incubator** (project standard) for the enrichment period.
- [ ] After enrichment, before streaking → keep at **4 °C fridge** if streaking is delayed.

## Source
- Lab notebook: [2026-05-20](../../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) (Procedure step 3).
- Existing protocol: `../../PMM_ProtocoL (1).docx`.

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry. Multiple `[TBD]` values where the 5-20 entry trails off — needs team confirmation.
- 2026-06-08 — Proofread cosmetic fix (**#12**): backtick source-path display corrected from `../PMM_ProtocoL (1).docx` → `../../PMM_ProtocoL (1).docx` (the file is at `protocol/PMM_ProtocoL (1).docx` which is `../../X` from `workflows/`).
