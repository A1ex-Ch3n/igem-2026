---
title: Soil Sample Collection
type: workflow
purpose: Field collection of soil samples from defined locations as the upstream input for all bacteria-isolation and metagenomic-sequencing tracks.
references: []
source:
  - lab_notebook/digitalized/2026-05-19_soil-sample-collection.md
estimated_time: ≈ 1 hr field time for 10 sites + travel
---

# Soil Sample Collection

## Purpose
Collect soil samples in the field at defined locations, labelled in a way that preserves the location metadata (longitude / altitude) for downstream interpretation. Provides the upstream input for both the bacteria-isolation track ([[soil_enrichment_bacteria]]) and the phage-isolation track ([[soil_enrichment_phage]]), as well as for direct [[metagenomic_dna_extraction]].

## Materials & equipment
- Soil probe
- Zip bags (one per sample)
- Marker / labelling tape
- GPS-capable device (phone) for recording longitude / altitude

## Reagents
*None* — this protocol is purely field collection of soil; no chemical reagents are used.

## Procedure
1. Choose sampling spots **by different types of vegetation** so the collected set spans distinct micro-habitats.
2. At each chosen spot, use the soil probe to collect one sample.
3. Place the sample into a zip bag.
4. Label the bag with:
   - sample number (1–N)
   - longitude
   - altitude
   - `[TBD: also latitude — notebook says "longitude and altitude" only; latitude is typically captured alongside]`
5. Repeat at all chosen spots. (Project collected **10 samples** on [2026-05-19](../../../lab_notebook/digitalized/2026-05-19_soil-sample-collection.md).)

## Notes / common deviations
- Of the 10 sites collected on 5-19, the project's downstream use split into two subsets:
  - Bacterial enrichment ([2026-05-20](../../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md)) used **#2, #5, #6, #8, #9, #10**.
  - Phage enrichment ([2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md)) used **#3, #5, #6, #8, #9, #10**.
- Collect more sites than you immediately need — splits like the above are easier when you have headroom.

## Checklist — where do the outputs go?
- [ ] Labelled zip bags of soil → **room temp** in the lab if processed within a few days; otherwise **4 °C fridge** to slow community drift before extraction / enrichment.
- [ ] GPS coordinates → recorded in `data/` or scheme doc.

## Source
- Lab notebook: [2026-05-19](../../../lab_notebook/digitalized/2026-05-19_soil-sample-collection.md).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry.
