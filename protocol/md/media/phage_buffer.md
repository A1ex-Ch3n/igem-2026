---
title: Phage Buffer (Tris–MgSO₄–NaCl–CaCl₂)
type: media
purpose: Salt buffer used to dilute and store filtered phage stocks; preserves phage viability during plaque assay setup. Two recorded recipe variants — team's mass-based (6-1) and prof's molar-based (Genomic_And_Phage_Work).
references: []
source:
  - lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md
  - protocol/Genomic_And_Phage_Work.docx
estimated_time: 15 min prep + 1 hr autoclave
---

# Phage Buffer

## Purpose
A salt buffer (Tris-buffered, Mg²⁺ and Ca²⁺ supplemented) used to dilute filtered phage stocks and as a working buffer in plaque-assay setup and [[phage_purification]]. The Mg²⁺ and Ca²⁺ ions support phage adsorption to host cells. *(Was also used in `phage_amplification` until that protocol was [archived 2026-06-06](../../../archived/phage_amplification.md).)*

## Recipe variants

Two equivalent recipes are recorded — they give the **same final salt composition**. Pick whichever is easier to scale on the day.

### Variant A — Team's mass-based recipe (as run [2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md))

| Final volume | MiniQ water | Tris | MgSO₄·7H₂O | NaCl | CaCl₂·2H₂O |
|---|---|---|---|---|---|
| 500 mL | 500 mL | 0.605 g | 1.23 g | 1.985 g | 0.075 g |
| **1000 mL** | **1 L** | **1.21 g** | **2.46 g** | **3.97 g** | **0.15 g** |

### Variant B — Prof's molar-based recipe (from `Genomic_And_Phage_Work.docx`)

| Component | Final concentration | pH |
|---|---|---|
| Tris | **10 mM** | **7.5** |
| MgSO₄ | 10 mM | — |
| NaCl | 68 mM | — |
| CaCl₂ | 1 mM | — |

> [!tip] iGEM 26 team practice — confirmed 2026-06-06 (pending teammate cross-check)
> The team's actual practice is **Variant A** (mass-based, as recorded in the [2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) lab-notebook entry): weigh out 1.21 g Tris + 2.46 g MgSO₄·7H₂O + 3.97 g NaCl + 0.15 g CaCl₂·2H₂O per litre of MiniQ water, autoclave 1 hr. Variant B (prof's molar form) is kept as an equivalent reference recipe — same final composition, useful if making a different volume or pH-adjusting from Trizma base directly.

> **The two variants match exactly.** Reverse-checking Variant A's gram weights against the molar concentrations in Variant B (using molecular weights for the **hydrate forms** of MgSO₄ and CaCl₂):
> - Tris (Trizma base, MW 121.14): 10 mM × 1 L = **1.21 g/L** ✓
> - MgSO₄·**7H₂O** (heptahydrate, MW 246.47): 10 mM × 1 L = **2.46 g/L** ✓
> - NaCl (MW 58.44): 68 mM × 1 L = **3.97 g/L** ✓
> - CaCl₂·**2H₂O** (dihydrate, MW 147.01): 1 mM × 1 L = **0.15 g/L** ✓
>
> So the hydrate-form `[TBD]`s are resolved: **MgSO₄·7H₂O** and **CaCl₂·2H₂O**. The prof's recipe also pins the **pH at 7.5** — apply this when using Trizma base (or use Tris-HCl pH 7.5 directly).

## Materials & equipment
- 1 L autoclave-safe bottle (or sized to final volume)
- Scale
- pH meter or pH paper (to verify / adjust to pH 7.5 — only needed for Variant B / when using Trizma base)
- Autoclave
- Autoclave indicator tape

## Reagents
- **Tris** — Trizma base (then pH-adjusted to 7.5) or Tris-HCl pre-buffered at pH 7.5
- **MgSO₄·7H₂O** (heptahydrate)
- **NaCl**
- **CaCl₂·2H₂O** (dihydrate)
- MiniQ water

## Procedure

> [!important] Label as you prepare
> Label every bottle and tube with its **substance, volume, and date** (e.g. `Phage buffer — 1 L — 2026-06-08`) before it goes on a shelf or into the fridge. This matters especially for the small-tube aliquots (see Notes).

1. Add the water volume to the bottle.
2. Weigh out and add Tris, MgSO₄·7H₂O, NaCl, and CaCl₂·2H₂O in order.
3. Mix until fully dissolved.
4. *(Variant B only)* Verify pH is 7.5; adjust with HCl / NaOH if needed.
5. Cap loosely with autoclave tape (Autoclave Indicator Tape) over the cap, then autoclave for **1 hr** (notebook 6-1 cycle).

## Notes / common deviations
- On [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md), the team noted: **divide phage buffer (and PBS) into smaller tubes for routine use** to avoid contamination caused by repeatedly pipetting from the bulk bottle.
- `[TBD: standard small-tube aliquot volume — not specified.]`
- Used as the elution medium in [[phage_purification]] (100 µL per picked plaque) — confirmed cross-protocol consumer of this buffer.

## Checklist — where do the outputs go?
- [ ] Bulk bottle of autoclaved phage buffer → **room temp** shelf, cap snug.
- [ ] Small-tube aliquots for daily use → **4 °C fridge** (typical for phage work) `[TBD: confirm whether team uses 4 °C or room temp for aliquots]`.

## Source
- Lab notebook: [2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) (Procedure ①c — Variant A mass-based recipe), [2026-06-03](../../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (Objective ② — aliquot reminder).
- [`../Genomic_And_Phage_Work.docx`](../../Genomic_And_Phage_Work.docx) (Variant B molar-based recipe + pH 7.5).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry.
- 2026-06-05 — Added prof's molar-based recipe as **Variant B** alongside the team's existing mass-based recipe (Variant A). Resolved the hydrate-form `[TBD]`s by reverse-checking molar mass × concentration against the team's recorded gram weights — **MgSO₄·7H₂O** and **CaCl₂·2H₂O** confirmed. Added pH 7.5 from prof's spec. Both recipe variants preserved per *the project rule of preserving all version variants from disagreeing sources*.
- 2026-06-06 — Added **iGEM 26 team practice** spotlight callout flagging Variant A (mass-based, as run on 6-1) as the team's actual practice; Variant B kept as equivalent reference recipe. Pending teammate cross-check.
- 2026-06-08 — Named the autoclave tape (**Autoclave Indicator Tape**) in the cap-loosely step and added it to Materials & equipment. Added a labelling reminder callout (substance / volume / date on every bottle and tube — emphasised for the aliquot tubes).
