---
title: Quick-DNA™ Miniprep Kit (Zymo Research)
type: media
purpose: Reusable reference for the Zymo Quick-DNA Miniprep Kit components, buffer prep, and chemistry — cross-referred by the two project workflows that use it.
references: []
source:
  - protocol/_d3024_d3025_quick-dna_miniprep_kit.pdf
estimated_time: ≈ 15 min hands-on per sample once setup is complete
---

# Quick-DNA™ Miniprep Kit (Zymo Research)

## Purpose
Reference doc for the **Zymo Quick-DNA™ Miniprep Kit** (catalog **D3024** for 50 preps / **D3025** for 200 preps). This file documents the kit's components, one-time buffer prep, storage, and shared chemistry. The two end-to-end workflows that use the kit ([[metagenomic_dna_extraction]] for soil and [[bacteria_genome_extraction]] for bacterial pellets) cross-ref here for the kit details so the chemistry isn't duplicated.

The kit's purification chemistry: **silica-spin column** (Zymo-Spin™ IICR) using a unique lysis-buffer system that **omits Proteinase K** for biological fluids and cell cultures. Yields ultra-pure dsDNA / mtDNA / vDNA up to ~40 kb, A₂₆₀/A₂₈₀ > 1.8, suitable for PCR, restriction digestion, bisulfite conversion, sequencing, genotyping.

> The team uses the **Whole Blood / Serum / Plasma protocol** (p.4 of the kit instruction manual) — applied to bacterial-cell suspensions — see [[bacteria_genome_extraction]] for the project-specific application.

## Quick-lookup table — kit components

| Component | D3024 (50 preps) | D3025 (200 preps) | Storage |
|---|---|---|---|
| Genomic Lysis Buffer¹ | 50 mL | 100 mL (2 ×) | **Room temp** |
| DNA Pre-Wash Buffer² | 15 mL | 50 mL | **Room temp** |
| g-DNA Wash Buffer | 50 mL | 100 mL | **Room temp** |
| DNA Elution Buffer | 10 mL | 10 mL (2 ×) | **Room temp** |
| Zymo-Spin™ IICR Columns | 50 | 200 | **Room temp** |
| Collection Tubes | 100 | 400 | **Room temp** |
| Instruction Manual | 1 | 1 | — |

¹ **Add β-mercaptoethanol (BME) before first use:** 0.5 % v/v final → **250 µL BME per 50 mL** or **500 µL BME per 100 mL** Genomic Lysis Buffer. *(BME is user-supplied — not in the kit.)*

² **If a precipitate has formed in the DNA Pre-Wash Buffer on shipping/storage:** incubate the bottle at **30–37 °C for 30 min** and mix by inversion. **DO NOT microwave.**

## Quick-lookup table — assay tube volumes (Whole Blood / Serum / Plasma protocol)

Per the kit's p.4 protocol used by the project for bacterial-pellet extraction:

| Step | Reagent | Volume per sample |
|---|---|---|
| Lysis (4:1 ratio buffer : sample) | Genomic Lysis Buffer | **400 µL** |
| Lysis input | sample (resuspended pellet) | **100 µL** |
| Pre-wash | DNA Pre-Wash Buffer | **200 µL** |
| Wash | g-DNA Wash Buffer | **500 µL** |
| Elution | DNA Elution Buffer | **≥ 50 µL** |

> Column binding capacity: **800 µL** total volume per spin.
> Maximum recoverable DNA: **up to 25 µg** per column (mammalian blood ≈ 3–7 µg per 100 µL).

## Materials & equipment
- Microcentrifuge (capable of ≥ 10,000 × g)
- Vortex mixer

## Reagents
- Kit components above
- **β-mercaptoethanol** (user-supplied) for one-time addition to Genomic Lysis Buffer
- Isopropanol (user-supplied) — for some sample sources (small samples, blood < 50 µL), add 0.3 volumes of isopropanol to the lysis mixture
- DNA Elution Buffer (kit) **or** water (user-supplied — for elution; pH > 6.0 strongly recommended)

> **Note on water vs. Elution Buffer:** elution efficiency depends on pH and temperature. If using water, ensure pH > 6.0 and consider pre-equilibrating to 60–70 °C for higher yield. The kit's DNA Elution Buffer is 10 mM Tris-HCl, pH 8.5, 0.1 mM EDTA.

## Procedure
All kit workflows reduce to the same **four-step common chemistry** once the sample is in the lysis mixture:

1. **Bind:** transfer lysis mixture to a Zymo-Spin™ IICR Column in a Collection Tube. Centrifuge at **≥ 10,000 × g for 1 min**. Discard flow-through.
2. **Pre-wash:** transfer the column to a new Collection Tube. Add 200 µL DNA Pre-Wash Buffer. Centrifuge at **≥ 10,000 × g for 1 min**.
3. **Wash:** add 500 µL g-DNA Wash Buffer. Centrifuge at **≥ 10,000 × g for 1 min**.
4. **Elute:** transfer the column to a clean microcentrifuge tube. Add ≥ 50 µL DNA Elution Buffer (or water at pH > 6.0). Incubate **2–5 min at room temperature**. Centrifuge at **≥ 10,000 × g for 30 s**.

The variant protocols (Whole Blood, Cell Suspensions, Solid Tissue, etc.) differ only in the **lysis input** (sample type + buffer ratio + any homogenisation). The chemistry from "transfer to column" onward is identical.

## Notes / common deviations
- The kit's published protocols cover blood, serum, plasma, buccal/swabs, solid tissue, cell monolayers, cell suspensions, and DNA/RNA Shield samples. **Bacterial cell pellets are not a listed sample type** — the team adapts the Whole Blood protocol (p.4) by resuspending the bacterial pellet to act as the "biological liquid" input. See [[bacteria_genome_extraction]] for the project's exact resuspension recipe.
- **Compatible with common anticoagulants** (EDTA, heparin, citrate) and detergents (≤ 5 % Triton X-100, ≤ 5 % Tween-20, ≤ 5 % Sarkosyl, ≤ 0.1 % SDS).
- **Excludes Proteinase K** in the standard workflow — for samples that need PK digestion (solid tissue, complex matrices), Zymo recommends the **Quick-DNA™ Miniprep Plus Kit (D4068 / D4069)** instead — *not* this kit.

## Checklist — where do the outputs go?
- [ ] Unopened kit components → **room temp** shelf (per the storage column above).
- [ ] Once BME is added to Genomic Lysis Buffer → keep at room temp, but use within a reasonable time window (BME is unstable on prolonged storage).
- [ ] Eluted DNA → **4 °C fridge** (short-term, days) or **−20 °C freezer** (long-term).
- [ ] Used spin columns + collection tubes → biohazard / chemical waste per local guidance.

## Source
- Kit manual: [`../protocol/_d3024_d3025_quick-dna_miniprep_kit.pdf`](../../_d3024_d3025_quick-dna_miniprep_kit.pdf) (Zymo Research, instruction manual v2.0.0, revised 2022-07-05).
- Used by: [[metagenomic_dna_extraction]], [[bacteria_genome_extraction]].

---
## Log
- 2026-06-05 — Initial draft from Zymo kit instruction manual. Created as the shared kit reference both extraction workflows can cross-ref.
- 2026-06-08 — Proofread fix (**#8**): renamed section heading `## Shared procedure (the four-step common chemistry)` → `## Procedure` to match the project's `_TEMPLATE.md` structural convention. Moved the "four-step common chemistry" descriptor into the section's intro sentence.
