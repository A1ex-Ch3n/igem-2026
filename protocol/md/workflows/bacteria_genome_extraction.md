---
title: Bacteria Genome DNA Extraction (Quick-DNA on bacterial pellet)
type: workflow
purpose: Extract genomic DNA from a thawed bacterial cell pellet using the Zymo Quick-DNA Miniprep Kit (Whole Blood / Serum / Plasma protocol), producing Qubit-ready DNA for sequencing.
references:
  - "[[quick_dna_miniprep_kit]]"
  - "[[bacteria_pellet_for_sequencing]]"
  - "[[dna_quantification_qubit]]"
source:
  - lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md
  - lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md
  - protocol/_d3024_d3025_quick-dna_miniprep_kit.pdf
estimated_time: ≈ 15–20 min per sample once pellet is thawed
---

# Bacteria Genome DNA Extraction (Quick-DNA on bacterial pellet)

## Purpose
Take a washed bacterial cell pellet from [[bacteria_pellet_for_sequencing]] (banked at **−20 °C**) and extract genomic DNA suitable for Qubit quantification ([[dna_quantification_qubit]]) and downstream whole-genome sequencing.

The kit used is the **Zymo Quick-DNA™ Miniprep Kit** (D3024 / D3025) — see [[quick_dna_miniprep_kit]] for component details. The team applies the **Whole Blood / Serum / Plasma protocol** (kit manual p.4) by resuspending the bacterial pellet to act as the "biological liquid" input.

> [!tip] iGEM 26 team practice — confirmed 2026-06-05
> The team applies the Whole Blood / Serum / Plasma protocol from the kit with several **deliberate deviations** that have been confirmed and recorded below. Each deviation is flagged with a `[!tip]` callout at its procedure step. Headline differences from the kit default:
> - **Lysis buffer 450 µL** (kit default: 400 µL) added **directly into the pellet's existing Eppendorf** — no separate resuspension step / resuspension buffer.
> - **Every spin → 15,000 × g for 5 min** (kit default: ≥ 10,000 × g for 1 min) — the kit's ≥ 10,000 × g / 1 min spin **failed for most samples** in the team's first attempts. If liquid still hasn't passed through after 5 min, extend the spin until it does.
> - **Elution: 100 µL** DNA Elution Buffer (kit default: ≥ 50 µL minimum).
> - **Collection-tube discipline:** discard the collection tube after every spin step **except** between pre-wash and wash — those two share the same collection tube.
> - **Pipette assignments:** p1000 for steps 1, 2, 4; p200 for steps 3, 5 (numbering follows the kit's 5-step procedure, not this file's expanded numbering — see the pipette table below).

## Quick-lookup table — per-sample reagent volumes

Both the kit-default values (Whole Blood / Serum / Plasma protocol, p.4) and the iGEM 26 team's actual values are shown side-by-side. Multiply by sample count for batch volume.

| Step | Reagent | Kit default | **Team (2026-06-05)** |
|---|---|---|---|
| Resuspend pellet | — | resuspend in 100 µL of buffer | **not done** — lysis buffer added directly into the pellet's existing Eppendorf |
| Lysis | Genomic Lysis Buffer (with BME already added — see [[quick_dna_miniprep_kit]]) | 400 µL (4:1 ratio with 100 µL sample) | **450 µL** |
| Lysis input | bacterial pellet (no separate resuspension) | 100 µL of resuspended sample | the entire pellet **in its original Eppendorf** |
| Pre-wash | DNA Pre-Wash Buffer | 200 µL | 200 µL (unchanged) |
| Wash | g-DNA Wash Buffer | 500 µL | 500 µL (unchanged) |
| Elution | DNA Elution Buffer (or pH > 6.0 water) | ≥ 50 µL | **100 µL** |

> **Centrifugation — kit default:** ≥ 10,000 × g at every spin step (1 min for binding + washes, 30 s for elution).

>[!tip] iGEM 26 team practice — confirmed 2026-06-05
> **Every spin step uses 15,000 × g for 5 minutes** (not the kit's ≥ 10,000 × g / 1 min). The kit-default spin **failed for most of the team's first samples** — liquid remained in the column. If after 5 min at 15,000 × g liquid is still in the column, **extend the spin** until it has all passed through. Applies to binding, pre-wash, wash, and elution.

## Quick-lookup table — pipette by step (iGEM 26 team practice)

Pipette assignments follow the **kit's 5-step procedure numbering** (see kit manual p.4), not this file's expanded numbering.

| Kit step | Action | Pipette |
|---|---|---|
| 1 | Add 450 µL Genomic Lysis Buffer to the pellet's Eppendorf | **p1000** |
| 2 | Transfer the mixture to the Zymo-Spin column; first spin | **p1000** |
| 3 | Add 200 µL DNA Pre-Wash Buffer | **p200** |
| 4 | Add 500 µL g-DNA Wash Buffer | **p1000** |
| 5 | Add 100 µL DNA Elution Buffer | **p200** |

## Materials & equipment
- Zymo Quick-DNA Miniprep Kit (D3024 or D3025) — see [[quick_dna_miniprep_kit]]
- Microcentrifuge (capable of ≥ 10,000 × g)
- Vortex
- Pipettes (10 µL, 200 µL, 1000 µL) + tips
- 1.5 mL microcentrifuge tubes (for elution collection)
- Ice bucket (to keep thawed pellets cold while staging)

## Reagents
- Kit components (Genomic Lysis Buffer with BME pre-added, DNA Pre-Wash Buffer, g-DNA Wash Buffer, DNA Elution Buffer; Zymo-Spin™ IICR columns + collection tubes) — see [[quick_dna_miniprep_kit]]
- β-mercaptoethanol (BME) — already added to Genomic Lysis Buffer per [[quick_dna_miniprep_kit]] one-time prep

> [!tip] iGEM 26 team practice — confirmed 2026-06-05
> **No separate resuspension buffer.** The team adds Genomic Lysis Buffer directly into the bacterial pellet's existing Eppendorf — the pellet is not resuspended in PBS / TE / any other buffer first. The kit's listed sample types (whole blood, etc.) are pre-existing liquid samples, so the kit assumes "100 µL of resuspended sample" as input; the team's adaptation skips that step and treats the pellet itself as the input sample.

## Procedure (Whole Blood protocol baseline + team-modification flags)

### Setup
1. **Thaw** the bacterial pellets from the **−20 °C freezer** ([[bacteria_pellet_for_sequencing]] output). Keep on ice.

   > [!tip] iGEM 26 team practice — confirmed 2026-06-05
   > Wait for the pellets to **fully melt** on the bench before doing anything else. The kit assumes a liquid sample at the start; trying to add lysis buffer to a still-frozen pellet gives inconsistent lysis.

2. **Confirm BME has been added** to the Genomic Lysis Buffer per the kit's one-time prep (see [[quick_dna_miniprep_kit]]).
3. **Confirm the DNA Pre-Wash Buffer is free of precipitate** (if precipitate present, incubate bottle at 30–37 °C for 30 min, mix by inversion — do not microwave).

### Lysis

> [!tip] iGEM 26 team practice — confirmed 2026-06-05
> **No separate resuspension step.** Skip directly from Setup to Lysis: the lysis buffer is added straight into the pellet's original Eppendorf. The "Resuspension" header in the kit-default version of this protocol is intentionally omitted from the team practice.

4. **Add Genomic Lysis Buffer** (containing BME) directly into the pellet's Eppendorf.
   - **Kit default:** 400 µL into a 100 µL resuspended sample (4:1 ratio).
   - **Team (2026-06-05):** **450 µL** into the pellet's existing Eppendorf, using a **p1000**.
5. **Mix completely** by vortexing **4–6 seconds**.
6. **Stand 5–10 minutes at room temperature.**

### Column binding *(kit step 2)*
7. Transfer the lysis mixture (~550 µL with the team's 450 µL buffer + pellet volume) to a **Zymo-Spin™ IICR Column** in a Collection Tube, using a **p1000**.
8. Centrifuge.
   - **Kit default:** ≥ 10,000 × g for 1 minute.
   - **Team (2026-06-05):** **15,000 × g for 5 minutes** (extend if liquid hasn't fully passed through). See the centrifugation callout above for the rationale.
9. **Discard the Collection Tube with the flow-through.**

### Pre-wash *(kit step 3)*
10. Transfer the column to a **new** Collection Tube.
11. Add **200 µL DNA Pre-Wash Buffer** to the column, using a **p200**.
12. Centrifuge.
    - **Kit default:** ≥ 10,000 × g for 1 minute.
    - **Team (2026-06-05):** **15,000 × g for 5 minutes**.

> [!tip] iGEM 26 team practice — confirmed 2026-06-05
> **Keep the same Collection Tube for the next step (wash).** Do not discard the tube between pre-wash and wash — these two steps share one tube.

### Wash *(kit step 4)*
13. Add **500 µL g-DNA Wash Buffer** to the column (on the same Collection Tube from pre-wash), using a **p1000**.
14. Centrifuge.
    - **Kit default:** ≥ 10,000 × g for 1 minute.
    - **Team (2026-06-05):** **15,000 × g for 5 minutes**.
15. **Discard the Collection Tube with the flow-through.**

### Elution *(kit step 5)*
16. Transfer the column to a **clean 1.5 mL microcentrifuge tube**.
17. **Add DNA Elution Buffer** (or pH > 6.0 water) directly onto the silica membrane, using a **p200**.
    - **Kit default:** ≥ 50 µL.
    - **Team (2026-06-05):** **100 µL**.
18. **Incubate 2–5 minutes at room temperature** to allow rehydration of the DNA.
19. Centrifuge to elute.
    - **Kit default:** ≥ 10,000 × g for 30 seconds.
    - **Team (2026-06-05):** **15,000 × g for 5 minutes** (extend if liquid hasn't fully passed through).
20. The eluted DNA can be used immediately for downstream applications ([[dna_quantification_qubit]]) or stored at ≤ −20 °C.

## Notes / common deviations

- **Bacterial cell pellets are not a Zymo-listed sample type.** The team adapts the Whole Blood / Serum / Plasma protocol (p.4) by skipping resuspension and adding the lysis buffer directly into the pellet's Eppendorf. If the resulting yields prove insufficient or A₂₆₀/A₂₈₀ is poor, consider switching to the **Quick-DNA™ Miniprep Plus Kit (D4068 / D4069)** which adds Proteinase K digestion suitable for cells / tissue.
- **Why 15,000 × g for 5 min (vs the kit's ≥ 10,000 × g / 1 min).** The team's first attempts at the kit-default spin **left liquid in the column for most samples** — likely because the bacterial-pellet lysate is more viscous / particulate-laden than the whole-blood / serum samples the kit was optimised against. The team's higher-g, longer-time spin reliably moves the liquid through; if it still hasn't passed after 5 min, extend the spin until it does. *(See the centrifugation callout in the quick-lookup section.)*
- **The 6-05 lab notebook** ([2026-06-05](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md)) records only the high-level "Ran each through the Quick-DNA Miniprep Kit (Zymo Research) following the kit's manufacturer protocol" — the team-practice details (no resuspension, 450 µL lysis, 15K g × 5 min spin, 100 µL elution, tube discipline, pipette assignments) come from this annotation pass on 2026-06-05.
- **6-05 yields were excellent** — Set A samples gave 93–264 ng/µL DNA (8.4–23.8 µg per 90 µL tube), comfortably above the typical ≥ 10 ng/µL sequencing-submission floor. See the [6-05 Computed concentrations table](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md#set-a--bacteria-genome-extracts) for per-sample numbers.
- **As run [2026-06-10](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md):** a second batch from the 10 revived-stock cultures. **Only 8 of 10 were extracted — the kit's last 8 spin columns were all used on these 8 (none remain afterwards)**; the 2 leftover samples (`8-1-2`, `9-1-2`) were **banked as pellets at −20 °C** until more columns are obtained. **Spin-column stock is the throughput limit** — check (and reorder) columns before planning a batch. Eluates were **stored at 4 °C**; quantification was deferred ("next week"). The notebook margin flags **"update the Zymo protocol"** to record 4 °C eluate storage (already reflected in the Checklist below).

## Checklist — where do the outputs go?
- [ ] Eluted DNA → **4 °C fridge** (short-term, up to days for Qubit + downstream prep) or **−20 °C freezer** (long-term archive).
- [ ] Spent collection tubes + flow-through → biohazard / chemical waste per local guidance.
- [ ] Used columns → discard (single-use).
- [ ] Original thawed pellet (residual) → discard once extraction completes; do not re-freeze.

## Source
- Lab notebook: [2026-06-05](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) (Procedure ③ — Bacteria genome extraction); [2026-06-10](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) (Procedure ② — second batch, 8 of 10).
- Kit manual: [`../../_d3024_d3025_quick-dna_miniprep_kit.pdf`](../../_d3024_d3025_quick-dna_miniprep_kit.pdf) (Zymo Research, Whole Blood / Serum / Plasma protocol, p.4).
- Kit reference: [[quick_dna_miniprep_kit]].

---
## Log
- 2026-06-05 — Initial draft from Zymo kit p.4 (Whole Blood) + 6-05 lab-notebook entry. `[TBD: team modification pending]` flags inserted at the resuspension step + incubation time — user will fill in once specifics are recorded.
- 2026-06-05 — Annotated with **iGEM 26 team practice** (Obsidian `[!tip]` callouts), resolving all `[TBD]` flags. Confirmed deviations from the kit-default Whole Blood protocol: (1) wait for pellets to fully melt on the bench before starting; (2) **no separate resuspension** — Genomic Lysis Buffer added directly into the pellet's Eppendorf; (3) **lysis buffer 450 µL** (kit: 400 µL); (4) **every spin = 15,000 × g for 5 min** (kit: ≥ 10,000 × g / 1 min) — kit-default spin failed for most samples; extend if liquid remains; (5) **elution 100 µL** (kit: ≥ 50 µL); (6) **collection-tube discipline** — discard after every spin **except** between pre-wash and wash (same tube); (7) **pipette assignments** — p1000 for kit steps 1, 2, 4 and p200 for kit steps 3, 5 (added as a new quick-lookup table). Both kit-default and team values preserved side-by-side per the project's "preserve all versions" rule.
- 2026-06-08 — Proofread cleanups (**#9** + **#10** + **#13**): "input solid" → "input sample" in the no-resuspension callout; removed the parenthetical "if the team has adjusted this, update accordingly" on step 6 since the team uses the kit default 5–10 min as-is; markdown link label for the Zymo kit PDF corrected from `../protocol/_d3024…` → `../../_d3024…` to match the actual target.
- 2026-06-12 — Added the **2026-06-10 second batch** as-run note (8 of 10 extracted, limited by 8 remaining spin columns; 2 pellets banked at −20 °C; eluates → 4 °C; quant deferred; notebook "update the Zymo protocol" 4 °C note). Added 6-10 to `source:`. No procedure values changed.
