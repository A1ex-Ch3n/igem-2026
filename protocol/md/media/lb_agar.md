---
title: LB Agar
type: media
purpose: LB-based solid / semi-solid medium for bacterial plating, soft-agar overlays in plaque assay, and layered (top-agar) plates.
references:
  - "[[lb_broth]]"
source:
  - lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md
  - lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md
  - lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md
estimated_time: 10 min prep + 30 min – 1 hr autoclave + cooling
---

# LB Agar

## Purpose
LB agar serves three distinct purposes in this project, each at a different agar concentration:
1. **1.0 %** — hard agar plates for streaking bacteria stocks, and as the base layer for the layered-plate plaque assay.
2. **0.7 %** — soft agar for plaque-assay overlays.
3. **0.8 %** — proposed alternative for soft agar after 0.7 % failed to solidify on [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md).

## Quick-lookup table

| Use case | Conc. | Per 50 mL | Per 100 mL | Per 500 mL | Source |
|---|---|---|---|---|---|
| Soft-agar overlay / layered-plate top | 0.7 % | 50 mL LB broth + **0.35 g agar** | 100 mL LB broth + **0.7 g agar** | 500 mL LB broth + 3.5 g agar | [6-3](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md), [6-4](../../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) |
| Soft-agar overlay (alt. — solidifies more reliably) | 0.8 % | 50 mL LB broth + **0.40 g agar** | 100 mL LB broth + **0.8 g agar** | 500 mL LB broth + 4.0 g agar | [6-3](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) deviation note |
| Hard plate base | 1.0 % | 50 mL LB broth + **0.5 g agar** | 100 mL LB broth + **1.0 g agar** | **500 mL LB broth + 5.0 g agar** | [6-1](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) |

> The "LB broth" column refers to either pre-made [[lb_broth]] or DI water + LB broth powder dissolved together before adding agar.

## Materials & equipment
- Autoclave-safe bottle (sized to final volume)
- Scale (for agar + LB powder)
- Autoclave
- Autoclave indicator tape
- Water bath set to 50 °C (for keeping melted agar pourable, see plaque-assay workflows)
- Petri dishes

## Reagents
- LB broth powder (or pre-made [[lb_broth]])
- Agar powder. `[TBD: brand / catalog number]`
- DI water

## Procedure

> [!important] Label as you prepare
> Label every bottle and tube with its **substance, volume, and date** (e.g. `LB agar 1.0 % — 500 mL — 2026-06-08`) before it goes on a shelf or into the fridge.

1. Add DI water to the bottle (volume per the table).
2. Weigh out LB broth powder (12.5 g per 500 mL is the project standard) and agar powder (per the table for the desired concentration).
3. Add both to the bottle, swirl to wet.
4. Cap loosely with autoclave tape (Autoclave Indicator Tape) over the cap, then autoclave.
   - 1 hr was used on 6-1 for hard agar.
   - 1 hr was used on 6-3 for 0.7 % soft agar.
   - 30 min was used on 6-4 for 0.7 % soft agar.
   - `[TBD: standardize one cycle.]`
5. For **plates** (1.0 %): allow to cool to pourable temperature, then pour into Petri dishes — the project standard plate volume is **8 mL** ([6-1](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md), Procedure ④).
6. For **soft-agar overlays** (0.7 % / 0.8 %): hold the molten agar in a **50 °C water bath** between batches so it stays pourable but is cool enough not to kill the bacteria you'll mix in.

## Notes / common deviations
- **0.7 % works in the layered-plate method; failed in the soft-agar overlay method.** The 6-3 attempt with [[plaque_assay_soft_agar]] (no hard-agar base) at 0.7 % **did not solidify**. The same 0.7 % concentration works fine in the [[plaque_assay_layered_plate]] method (6-4 and 6-5) because the hard-agar base underneath provides a solid platform. So the 0.7 % row above is correct for layered-plate top-agar; if you're doing soft-agar overlay without a hard base, use the **0.8 % row** instead.
- **[2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) — soft-agar failure record.** The "Learning from the day" notes recommend (a) raising agar to **0.8 %** for the overlay-only method, and (b) **making extra** (e.g., 2 × 50 mL) so a failed pour isn't fatal.
- On 6-1, the volume of LB broth made just barely covered the 10 × 8 mL plates ("used up all of the LB agar to make 8 mL plates"). Make extra to avoid running out.

## Checklist — where do the outputs go?
- [ ] Autoclaved hard-agar plates (1 %) → **4 °C fridge**, sealed in plastic bag. `[TBD: shelf life — not documented; the PseudomonasClassAppendixes PDF states "All solid media are stable for months when stored at 4 °C in sealed plastic bags".]`
- [ ] Molten soft agar (0.7 / 0.8 %) intended for same-day use → **50 °C water bath** until poured.
- [ ] Unused molten soft agar at end of day → discard via [[media_disposal]].

## Source
- Lab notebook: [2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) (Procedure ①a + ④), [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (Procedure ① + Deviation + Learning), [2026-06-04](../../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) (Procedure ① step 1).
- Reference: `../../PseudomonasClassAppendixes.pdf` (JMBE 2014, storage note).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entries.
- 2026-06-08 — Proofread fixes (**#6** + **#19**): renamed the 0.7 % row label "Soft-agar overlay (failed)" → "Soft-agar overlay / layered-plate top" because 0.7 % only failed in the overlay-only method (6-3) — it works fine in the layered-plate method (6-4 / 6-5). Renamed the 0.8 % row to "Soft-agar overlay (alt. — solidifies more reliably)". Added a Notes paragraph explaining when to choose 0.7 % vs 0.8 % based on whether a hard-agar base is present. Aligned the Source column formatting on the 0.8 % row.
- 2026-06-08 — Proofread cosmetic fix (**#12**): backtick source-path display corrected from `../PseudomonasClassAppendixes.pdf` → `../../PseudomonasClassAppendixes.pdf`.
- 2026-06-08 — Named the autoclave tape (**Autoclave Indicator Tape**) in the cap-loosely step and added it to Materials & equipment. Added a labelling reminder callout (substance / volume / date on every bottle and tube).
