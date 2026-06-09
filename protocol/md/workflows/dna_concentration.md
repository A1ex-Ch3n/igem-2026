---
title: DNA Concentration / Cleanup (Spin-Column)
type: workflow
purpose: Concentrate and clean a dilute DNA eluate (e.g. low-yield metagenomic extract) by re-binding it to a silica spin column and eluting into a smaller volume, raising ng/µL before sequencing submission.
references:
  - "[[metagenomic_dna_extraction]]"
  - "[[dna_quantification_qubit]]"
source:
  - lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md
estimated_time: ≈ 30–45 min for a batch of 4–5 tubes
---

# DNA Concentration / Cleanup (Spin-Column)

## Purpose
Take a **dilute DNA eluate** — typically the pooled, low-yield output of [[metagenomic_dna_extraction]] — and concentrate it by re-binding the DNA to a silica spin column and eluting into a **smaller final volume**, so the ng/µL reading clears the sequencing-submission floor. Run after a [[dna_quantification_qubit]] read shows the eluate is too dilute, and re-quantify the concentrated eluate afterward.

> [!note] Source — 2026-06-08
> Transcribed from the [2026-06-08](../../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) entry (p.35). The team applied this to the small-biomass metagenomic extracts (sites #1, #6, #8, #9) immediately after extraction, then re-quantified before vs after.

## Materials & equipment
- Silica DNA spin column + collection tubes. `[TBD: exact kit/catalog — the p.35 step names ("binding buffer", "g-DNA Wash Buffer", "DNA Elution Buffer") read like a Zymo DNA Clean & Concentrator / Quick-DNA column; confirm the box.]`
- 2 mL microcentrifuge tubes (for pooling the eluate before loading)
- 1.5 mL microcentrifuge tubes (for the concentrated eluate)
- Microcentrifuge (≥ 10,000 × g)
- Pipettes (P1000, P200)

## Reagents
- Dilute DNA eluate to be concentrated (e.g. pooled metagenomic extract — see [[metagenomic_dna_extraction]])
- **DNA Binding Buffer** (column-binding buffer)
- **g-DNA Wash Buffer**
- **DNA Elution Buffer**

## Procedure
1. **Pool the eluate** into a 2 mL tube, transferring **≤ 1.5 mL at a time**. Work in **batches of 4–5** tubes. `[TBD: p.35 reads "transfer from ~7.5 mL eppendorf to 2 mL" — confirm the starting pooled volume.]`
2. **Bind:** add **DNA Binding Buffer at a 3 : 1 ratio** (3 volumes buffer : 1 volume sample) and mix. Load onto the spin column in a collection tube.
3. **Spin to bind.** Centrifuge so the sample passes through the column; the DNA stays bound to the membrane. Move the column to a new collection tube, **re-pass the flow-through** through the column, and spin again — **repeat at least once** to maximize capture.
4. **Repeat** steps 1–3 for **all** the pooled solution (across both source tubes / the whole batch), so the full sample volume's DNA is collected onto the one column.
5. **Wash:** add **500 µL g-DNA Wash Buffer** to the column; centrifuge at **10,000 × g for 1 min**; discard the flow-through.
6. **Elute:** add **DNA Elution Buffer** to the column matrix; centrifuge at **10,000 × g for 3 min** into a clean **1.5 mL** tube. `[TBD: elution volume — p.35 reads "total DNA Elution Buffer"; the p.36 margin math implies a small final volume (~30 µL). Confirm.]`
7. **Quantify** the concentrated eluate by [[dna_quantification_qubit]] and compare against the pre-concentration reading.

## Notes / common deviations
- **3 : 1 binding ratio** is the volume of binding buffer to sample — load buffer plus sample together onto the column.
- **Re-passing the flow-through** (step 3) is the key concentration trick: running the same lysate over the membrane more than once captures DNA that didn't bind on the first pass — important when starting from a dilute, large-volume input.
- **Re-quantify against an appropriate curve.** On 2026-06-08 the concentrated eluates were read against a **freshly made smaller-volume standard curve**, while the unconcentrated samples used the prior session's curve — see [[dna_quantification_qubit]]. Concentrated reads can land **far above the top standard** (C8/C9 on 6-8) and be heavily extrapolated; consider a higher standard or a dilution if so.
- **Expected output:** a smaller-volume, higher-ng/µL eluate suitable for sequencing submission. `[TBD: record the before/after fold-change once the unconcentrated readings are confirmed.]`

## Checklist — where do the outputs go?
- [ ] Concentrated DNA eluate → **4 °C fridge** (short-term) or **−20 °C freezer** (longer-term) until sequencing submission.
- [ ] Used spin columns / collection tubes → [[media_disposal]] (or per kit waste guidance).

## Source
- Lab notebook: [2026-06-08](../../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) (Procedure ⑤ + p.35).

---
## Log
- 2026-06-08 — Initial draft from the 6-8 entry (p.35). Fills a gap: the concentration/cleanup step (re-bind dilute eluate → elute small) previously had no protocol. Kit catalog left `[TBD]` (buffer names read like a Zymo clean-and-concentrate column — not asserted). Elution volume and starting pooled volume flagged `[TBD]`.
