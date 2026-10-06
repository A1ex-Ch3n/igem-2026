---
title: PBS (Phosphate-Buffered Saline), pH 7.4
type: media
purpose: Dilution buffer and negative-control buffer for the depolymerase activity assay; general isotonic wash buffer.
references:
  - "[[depolymerase_activity_assay]]"
source:
  - "Otwinowska A et al. DepoCatalog. Nat Commun 17, 6724 (2026). doi:10.1038/s41467-026-73570-7 — Methods, 'Depolymerase activity assay'"
  - lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md
estimated_time: ≈ 20 min + autoclave
---

# PBS (Phosphate-Buffered Saline), pH 7.4

> [!warning] Literature-derived, like [[depolymerase_activity_assay]]
> The molar recipe below is the one specified in the DepoCatalog paper, transcribed
> verbatim. The team has separately used "PBS" as a wash buffer during pellet prep
> ([[bacteria_pellet_for_sequencing]]), but **the notebook never records which PBS
> formulation or supplier that was**. `==CONFIRM: is the lab's existing PBS the same
> formulation, or a commercial tablet/10× stock?==` If a commercial PBS is already on the
> shelf, use it and record the brand here rather than mixing this from salts.

## Purpose
Isotonic, phosphate-buffered saline at pH 7.4. In [[depolymerase_activity_assay]] it has
two jobs: it is the diluent for the enzyme's two-fold dilution series, and it is the
negative-control spot. Both roles require the *same* buffer, so mix one batch.

⚠️ **Not interchangeable with [[phage_buffer]]**, which is Tris + MgSO₄ + CaCl₂ at
pH 7.5. Do not substitute without recording it as a deviation.

## Quick-lookup table — 1× recipe

| Component | Final conc. | g per 1 L (1×) | Formula weight used |
|---|---|---|---|
| NaCl | **137 mM** | 8.00 g | 58.44 |
| KCl | **2.7 mM** | 0.20 g | 74.55 |
| Na₂HPO₄ *(anhydrous)* | **10 mM** | 1.42 g | 141.96 |
| KH₂PO₄ *(anhydrous)* | **1.8 mM** | 0.245 g | 136.09 |

Final **pH 7.4**.

`==CONFIRM: anhydrous vs hydrated salts.==` The paper gives molarities only. The gram
weights above assume **anhydrous** Na₂HPO₄ and KH₂PO₄. If the shelf stock is
Na₂HPO₄·7H₂O (FW 268.07 → 2.68 g/L) or ·12H₂O (FW 358.14 → 3.58 g/L), recalculate.
Same issue the team already hit with [[phage_buffer]]'s MgSO₄ and CaCl₂.

## Materials & equipment
- 1 L bottle (autoclavable)
- Balance, weigh boats, spatula
- Stir plate + stir bar
- pH meter
- Graduated cylinder
- Autoclave, or 0.22 µm filter unit for filter sterilisation

## Reagents
- NaCl
- KCl
- Na₂HPO₄
- KH₂PO₄
- MiniQ or DI water `==CONFIRM: repo has an open MiniQ-vs-DI standardisation item==`

## Procedure
1. Add ≈ 800 mL water to the bottle with a stir bar.
2. Dissolve the four salts one at a time, in the order listed in the table. Wait for each
   to dissolve fully before adding the next.
3. Adjust to **pH 7.4** with HCl or NaOH.
4. Top up to **1 L**.
5. Sterilise: autoclave, **or** filter through 0.22 µm if it will contact purified
   protein. `==CONFIRM: autoclave cycle — the repo has the same open 30 min vs 1 hr
   question for LB.==`
6. Label with date and pH. Store at room temperature.

## Notes / common deviations
- **Adjust the pH before the final volume**, not after, or the final concentrations drift.
- For **protein work**, prefer filter sterilisation. Autoclaving is fine for the buffer
  itself but the bottle must be cool before any enzyme touches it.
- A 10× stock is convenient but the phosphates can precipitate on storage at 10×. If
  making 10×, warm and check for crystals before diluting.

## Checklist — where do the outputs go?
- [ ] Sterile PBS → **room temp** shelf, sealed bottle, dated
- [ ] Working aliquot for the assay → **4 °C** — see [[depolymerase_activity_assay]]
- [ ] Waste → **media disposal** — see [[media_disposal]]

## Source
- Recipe: Otwinowska A *et al.* **DepoCatalog.** *Nat Commun* **17**, 6724 (2026),
  doi:10.1038/s41467-026-73570-7 — Methods, "Depolymerase activity assay".
- Prior undocumented team use as a pellet wash:
  [2026-06-10](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md)

---
## Log
- 2026-09-21 — Initial draft, written alongside [[depolymerase_activity_assay]] (#26),
  which needs PBS as both diluent and negative control. Molarities are the paper's;
  the gram-per-litre column is computed here assuming anhydrous phosphates and is
  flagged `==CONFIRM==`. Whether the lab already stocks a commercial PBS is unresolved.
