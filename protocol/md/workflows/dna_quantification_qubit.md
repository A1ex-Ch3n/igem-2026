---
title: DNA Quantification — Portelite BDR DNA Kit on Qubit 4
type: workflow
purpose: Quantify dsDNA concentration of an extracted sample over the 0.2–100 ng/µL range using the AAT Bioquest Portelite Fluorimetric DNA Quantitation Kit with Broad Dynamic Range on the Qubit 4 Fluorometer.
references: []
source:
  - lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md
  - lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md
  - lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md
  - protocol/protocol-for-portelite-fluorimetric-dna-quantitation-kit-with-broad-dynamic-range-optimized-for-cytocite-and-qubit-fluorometers-version-OFFcC.pdf
estimated_time: ≈ 30 min for ≤ 8 samples + 6–7 standards
---

# DNA Quantification — Portelite BDR DNA Kit on Qubit 4

## Purpose
Determine the dsDNA concentration of an extracted sample (e.g., [[metagenomic_dna_extraction]] or bacterial-genome extract from [[bacteria_pellet_for_sequencing]]) using the **Portelite™ Fluorimetric DNA Quantitation Kit with Broad Dynamic Range** (AAT Bioquest, cat. **17665**) on the **Qubit 4 Fluorometer** via the green fluorescence channel (480 / 530 nm). The standards calibrate the fluorometer over a linear curve; samples are read against that fit. Output: ng/µL.

The output decides whether a sample has enough DNA to submit for sequencing or needs to be re-extracted.

## Quick-lookup table — assay tube setup

| Tube type | Helixyte BR working solution | Sample / standard input | Total volume |
|---|---|---|---|
| **Standard** (×6 — see project default below; ×7 if following kit recommendation) | 190 µL | 10 µL of standard | 200 µL |
| **Sample** (×N) | 190 µL | 10 µL of DNA extract | 200 µL |

> [!tip] iGEM 26 team practice — confirmed 2026-06-05
> Sample volume per assay run: **10 µL** (matches the kit default). The team consistently uses the **10 µL sample / 190 µL working solution / 200 µL total** split shown above — no per-tube volume adjustments.

> **Tube format:** **0.2 mL thin-wall clear PCR tubes** (e.g., AAT Bioquest **CCT100**) — *not* the larger 0.5 mL Invitrogen Qubit assay tubes. Wrong tubes → wrong readings.

## Standard dilution series

### Project default (6-point, used 2026-06-05)
Uses Component D directly as the top standard:

| Standard | **team label** | Concentration (ng/µL) | How prepared |
|---|---|---|---|
| Std 0 (blank) | **s0** | 0 | Component C, undiluted |
| Std 1 | **s1** | 1 | 1/3 serial dilution from Std 2 (`s3`) in Component B |
| Std 2 | **s3** | 3 | 1/3 serial dilution from Std 3 (`s10`) in Component B |
| Std 3 | **s10** | 10 | 1/3 serial dilution from Component D (`s100`) in Component B |
| Std 4 | **s30** | 30 | Component D (`s100`) diluted 1:3.33 in Component B |
| Std 5 | **s100** | 100 | **Component D, undiluted** |

> [!tip] iGEM 26 team practice — confirmed 2026-06-05
> The team labels the six standards by concentration: **s0, s1, s3, s10, s30, s100** (the number is the ng/µL value — see the *team label* column above). Source + diluent mapping:
> - **s0** → Component C, undiluted (blank)
> - **s1, s3, s10, s30, s100** → all traced back to **Component D**; all dilutions are made in **Component B (Assay Buffer)** — never water, never any other buffer
>
> No other deviations from the 6-point series. `[Question: confirm whether s30 / s10 / s3 / s1 are prepared as a serial 1/3-ish chain (as the "How prepared" column says) or as direct dilutions from Component D — both reach the same target concentrations but differ in pipette path and error propagation.]`

### Kit-recommended alternative (7-point)
Per the protocol: 1/3 serial dilution from Component D (100 ng/µL) gives **30 / 10 / 3 / 1 / 0.3 / 0.1 / 0 ng/µL** — denser low end, no high-concentration top point. Use this when samples are expected to be in the <10 ng/µL range.

### Smaller-volume 4-point series (used 2026-06-08)
On [2026-06-08](../../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) the team made a **fresh, smaller-volume standard series** to read the **concentrated** metagenomic eluates (the **unconcentrated** samples were read against the prior 6-point curve from 2026-06-05 — a before/after-concentration comparison). Top point at 30 ng/µL, four points:

| Standard | team label | Conc (ng/µL) | RFU (green, p.36) |
|---|---|---:|---:|
| Std 0 (blank) | S0 | 0 | 156.326 `[TBD: photo "15 6326"]` |
| Std 1 | S1 | 1 | 173.90 |
| Std 10 | S10 | 10 | 316.95 |
| Std 30 | S30 | 30 | 724.52 `[TBD: p.36 subscript reads like "S₅₀"/value "7224.52"; resolved to Std 30 = 724.52 on linearity grounds]` |

> [!tip] Pick the curve to match the samples
> Read **concentrated / high-DNA** samples and **dilute** samples on appropriate curves. With only a 30 ng/µL top point, concentrated eluates can read **far above the top standard** (sites C8/C9 on 6-8 were ~3,000–5,600 RFU, heavily extrapolated) — quote with caution or re-dilute / add a higher standard. See [[dna_concentration]] for the concentration step that precedes this read.

## Materials & equipment
- **Qubit 4 Fluorometer** (also compatible with AAT Bioquest CytoCite Fluorometer)
- 0.2 mL thin-wall clear PCR tubes (e.g., AAT Bioquest **CCT100**)
- Vortex mixer
- Timer
- Pipettes (10 µL, 200 µL)
- Plastic container (recommended over glass) for the working solution — Helixyte™ Green BR can adsorb to glass surfaces

## Reagents
- **Portelite BDR kit components** (cat. 17665):
  - **Component A:** Helixyte™ Green **BR** (200X in DMSO) — store frozen (<−15 °C), minimize light
  - **Component B:** Assay Buffer — store refrigerated (2–8 °C); used to dilute Component A and to make the standard dilution series
  - **Component C:** DNA Standard BR #1 (Calf thymus DNA, 0 ng/µL) — refrigerated
  - **Component D:** DNA Standard BR #2 (Calf thymus DNA, **100 ng/µL**) — refrigerated
- DNA extract(s) to be quantified

> **Light-sensitive:** the working solution is light-sensitive — protect with foil or work in a darker space. Working solution is best used within a few hours of preparation.

## Procedure
1. **Bring all kit components to room temperature** before opening.
2. **Prepare the Helixyte™ Green BR working solution** (200-fold dilution of Component A):
   - **For ≤ 8 samples** (kit example): 5 µL Component A + 1 mL Component B.
   - **Scaling rule:** 1 µL Component A per 200 µL final volume. Make enough working solution for 190 µL per assay tube (standards + samples), plus ~10 % overage.
3. **Prepare the standard dilution series** (project default — 6-point) using Component B as the diluent. Mix gently after each dilution.
4. **Set up assay tubes** (0.2 mL PCR tubes): 6 for standards + 1 per sample.
5. **Fill each tube** per the lookup table:
   - 190 µL Helixyte BR working solution
   - 10 µL of standard or sample
   - Mix by vortexing 2–3 seconds.
6. **Incubate at room temperature for 2 minutes.**
7. **Insert tubes** into the Qubit 4 Fluorometer and monitor fluorescence on the **green** channel (480 nm ex / 530 nm em — the Qubit's fluorescence page may display the channel as "470 nm" or similar; that's the instrument's label, not the actual ex wavelength).
8. Read all standards first to build the curve, then each sample.
9. **Record both** the kit's computed ng/µL output **and** the raw fluorescence (RFU) reading per tube — RFU is what lets you plot the standard curve and refit later if needed.

## Standard curve & data interpretation
- **Fit type:** **linear regression** (RFU vs. concentration in ng/µL) — *not* log-log. Subtract the Std 0 (blank) RFU from every other standard's RFU before fitting (background subtraction).
- **Optimized sample concentration range:** 0.2 → 100 ng/µL.
- **Linear region of the standard curve:** roughly 10 pg/µL → 10 ng/µL — well within the project's 6-point series. Above 10 ng/µL the RFU response is still monotonic but rolls off slightly from perfect linearity.
- **Recommended fit tool:** the kit references AAT Bioquest's online linear-regression calculator (<https://www.aatbio.com/tools/linear-logarithmic-semi-log-regression-online-calculator>). For project use, fitting in Python / a spreadsheet is fine.
- **PI guidance (2026-06-05):** the curve can be **extrapolated a bit beyond the 100 ng/µL top standard** — the response stays well-behaved above 100 ng/µL within reason, so samples reading slightly above Std 5 can still be quoted from the extrapolated line rather than re-diluted, as long as they are not orders of magnitude above 100.
- The kit is highly selective for **dsDNA** over RNA; it is several orders of magnitude more sensitive than UV absorbance.

## Notes / common deviations
- **[2026-05-27](../../../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md) outcome:** of the 10 1st-batch metagenomic samples, only **sample #10** read above the detection floor. Conclusion: redo all samples — drove the [2026-05-28](../../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) second-batch extraction.
- **[2026-06-05](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) outcome:** re-quant of the 5-28 second batch was still **low** across sites #1, #3, #4, #7. Mixing batch-1 + batch-2 paired samples (**M1 / M3 / M4 / M7 mix** — one per 2nd-batch site) did not recover usable concentration. Next plan: re-extract with **smaller per-sample soil mass** to avoid silica-column saturation (see [[metagenomic_dna_extraction]]).
- **Helixyte BR adsorbs to glass.** Use plastic for the working-solution container.
- **Light protect** the working solution (foil or dark).
- **Two Portelite variants exist** — make sure you're using the **BDR** (cat. 17665) and not the HS (cat. 17660 / 17661). The BDR Component D is 100 ng/µL; the HS Component D is 10 ng/µL — using the wrong kit will give every standard wrong by a factor of 10.

## Checklist — where do the outputs go?
- [ ] DNA samples after measurement → return to **4 °C fridge** (short-term) or **−20 °C freezer** (longer-term).
- [ ] Used 0.2 mL PCR tubes (now stained with Helixyte BR / DMSO) → [[media_disposal]] (or per kit waste guidance — Helixyte is in DMSO).
- [ ] Numerical readings (standards RFU + samples RFU + computed concentrations) → recorded in `data/` (per-day file, e.g. `data/0605_qubit.xlsx`, following the [2026-05-29 pattern](../../../data/assays/0529_OD.xlsx)).

## Source
- Lab notebook: [2026-05-27](../../../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md) (Procedure ① + outcome), [2026-06-05](../../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) (Procedure ④ + 6-point Standards section + PI extrapolation note).
- Kit protocol: [`../../protocol-for-portelite-fluorimetric-dna-quantitation-kit-with-broad-dynamic-range-optimized-for-cytocite-and-qubit-fluorometers-version-OFFcC.pdf`](../../protocol-for-portelite-fluorimetric-dna-quantitation-kit-with-broad-dynamic-range-optimized-for-cytocite-and-qubit-fluorometers-version-OFFcC.pdf) (AAT Bioquest, last revised October 2019).

---
## Log
- 2026-06-05 — Initial draft from lab notebook entry.
- 2026-06-05 — Rewritten to be Portelite HS-specific per user clarification.
- 2026-06-05 — **Corrected** to Portelite **BDR** (cat. 17665), not HS — user originally pointed at the HS protocol PDF by mistake. Updated kit components (Component D = 100 ng/µL), instrument settings (480 / 530 nm), fit type (linear regression, not log-log), linear range (0.2–100 ng/µL sample range, 10 pg/µL–10 ng/µL strict linear region), and 6-point series construction (Std 5 is Component D undiluted).
- 2026-06-05 — Annotated with **iGEM 26 team practice** callouts (Obsidian `[!tip]` boxes): confirmed **10 µL** sample volume per assay run + team's **s0 / s1 / s3 / s10 / s30 / s100** label convention (named by concentration). Added a `team label` column to the 6-point standard table. No procedural changes — original kit and prof source content unchanged. Open question on serial-vs-direct dilution path flagged inline for user confirmation.
- 2026-06-05 — Added explicit diluent confirmation to the standards callout: all team standard dilutions are made in **Component B (Assay Buffer)** — never water or another buffer. (The "How prepared" column rows already named Component B; the callout now states it too for at-a-glance clarity.)
- 2026-06-08 — Proofread fix (**#2**): corrected wrong mix labels in Notes — "M1 / M2 / M3 mix" → "**M1 / M3 / M4 / M7 mix**" to match the actual 6-05 lab-notebook record (one mix per 2nd-batch site #1, #3, #4, #7).
- 2026-06-08 — Proofread cosmetic fix (**#13**): markdown link label for the Portelite kit PDF corrected from `../protocol-for-portelite-…pdf` → `../../protocol-for-portelite-…pdf` to match the actual target.
- 2026-06-08 — Added the **smaller-volume 4-point standard series** (used 2026-06-08 for concentrated metagenomic eluates) **alongside** the existing 6-point and kit 7-point series (preserve-all-versions). Noted the before/after-concentration workflow with [[dna_concentration]] and the extrapolation caution for concentrated reads. Added the 6-8 entry to `source:`. Several p.36 standard digits flagged `[TBD]`; S30-vs-S50 resolution recorded.
