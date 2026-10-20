---
title: Bradford Protein Assay (Pierce™ Bradford Plus)
type: technique
purpose: Measure total protein concentration in a lysate or purified fraction against a nine-point BSA standard curve, read at A595 in 2 mL microtubes.
references:
  - "[[iptg_induction_and_protein_extraction]]"
  - "[[his_tag_purification_ni_spin_column]]"
source:
  - protocol/printed_2026-10-20/IMG_6611.JPG
  - protocol/printed_2026-10-20/IMG_6612.JPG
estimated_time: ≈ 1 h 15 min (30 min reagent warm-up + 20 min standards + 10 min incubation + reading)
---

# Bradford Protein Assay (Pierce™ Bradford Plus)

## Purpose
Quantify **total protein** in crude lysates and purification fractions, so that gel lanes, dot-blot
spots and activity assays can be loaded on a known protein basis rather than by volume. The kit
standard-tube format is **50 µL sample + 1.5 mL reagent = 1.55 mL in a 2 mL microtube**, read at
**A595**.

> [!warning] Provenance — a printed bench document, not a notebook transcription
> This file is transcribed from **photographs of the team's printed working copy**, taken
> **2026-10-20**: [IMG_6611](../../printed_2026-10-20/IMG_6611.JPG) (p.1) and
> [IMG_6612](../../printed_2026-10-20/IMG_6612.JPG) (p.2). The printed document carries no page
> footer and no author line, and it is **not** derived from our lab notebook — unlike protocols
> #1–#25. Its values follow the Thermo Pierce Bradford Plus kit insert. It is kept here because it
> is the document that was physically on the bench.

> [!failure] No notebook record of a Bradford run
> **The team has never recorded running this assay.** The only protein quantification in the
> notebook is **BCA at OD562** — [9-28](../../../lab_notebook/digitalized/2026-09-28_protein-dilution-bca-quantification.md)
> (1:10 and 1:20 dilutions of all six constructs, ± IPTG) and the saturated readings it rescues on
> [9-27](../../../lab_notebook/digitalized/2026-09-27_protein-extraction-gel.md). Bradford reads at
> **595 nm** and BCA at **562 nm**; they are different chemistries and the numbers are not
> interchangeable. Treat this protocol as **planned, not performed**, until a dated run exists.

## Quick-lookup table — BSA standards, Curve S (kit Table 1)

Prepare **strictly in the order A → I**; vials D–H are made from earlier vials.

| Vial | Diluent (µL) | BSA volume (µL) | BSA source | Final [BSA] (µg/mL) |
|---|---|---|---|---|
| S-A | 0 | 300 | 2 mg/mL stock | 2000 |
| S-B | 125 | 375 | 2 mg/mL stock | 1500 |
| S-C | 325 | 325 | 2 mg/mL stock | 1000 |
| S-D | 175 | 175 | Vial S-B | 750 |
| S-E | 325 | 325 | Vial S-C | 500 |
| S-F | 325 | 325 | Vial S-E | 250 |
| S-G | 325 | 325 | Vial S-F | 125 |
| S-H | 400 | 100 | Vial S-G | 25 |
| S-I | 400 | 0 | — (blank) | 0 |

The whole set consumes **1.0 mL of the 2 mg/mL stock** (300 + 375 + 325 µL). Every row checks out
arithmetically against the stated final concentration.

> [!note] Handwritten annotation on the table
> Below the S-I row, in pen: **"Blank 100"**. Its meaning is not recorded.
> `==CONFIRM: whether "Blank 100" means a 100 µL blank volume, or a separate buffer blank.==`

## Materials & equipment
- **Pierce™ Bradford Plus Protein Assay Reagent** — stored at **4 °C**
- 50 mL conical tube(s), for the working aliquot of reagent
- Nine clean **1.5 mL** microtubes (standards S-A … S-I)
- **2.0 mL** microtubes + racks (reaction tubes)
- P200, P1000, vortex
- Timer
- UV/Vis spectrophotometer able to read **595 nm**
- Bench space at stable room temperature

## Reagents
- Pierce Bradford Plus Protein Assay Reagent
- **2 mg/mL BSA ampule** (kit standard)
- **Diluent** — the *same buffer the samples are in*, wherever possible; otherwise ultrapure H₂O
  (and then run a buffer blank alongside the samples)
- Sample(s): crude lysate from [[iptg_induction_and_protein_extraction]], or fractions from
  [[his_tag_purification_ni_spin_column]]

## Procedure

### 1. Assay reagent preparation
1. **Gently invert** the reagent bottle **5–10 times** just before pouring. **Do not shake** — on
   standing the reagent forms dye aggregates that gentle mixing redisperses; shaking makes foam.
2. **Pour** the volume you need into a 50 mL conical tube. Do **not** pipette from the stock bottle,
   and never return unused reagent to it.
3. ★ **Leave the capped aliquot on the bench for ≥ 30 min to reach room temperature. Cold reagent
   gives low A595 values.**
4. Invert the conical gently again just before dispensing.
5. The reagent is **brown** (absorbance maximum 465 nm) and turns **blue** (595 nm) when it binds
   protein.

### 2. BSA standards — Curve S (25–2000 µg/mL)
1. **Diluent:** use the **same buffer your samples are in** whenever possible. If you use ultrapure
   H₂O instead, run a buffer blank with the samples.
2. Label nine clean 1.5 mL microtubes **S-A … S-I**.
3. **Vortex the 2 mg/mL BSA ampule briefly** before use.
4. Pipette the **diluent into each vial first**, then add the BSA source, following the
   quick-lookup table above **in order A → I**.
5. **Vortex 2–3 s after each addition.** This is critical — the next vial depends on this one being
   fully mixed.
6. Keep the standards at **room temperature** during the assay.

### 3. Reaction tube setup
1. **Pre-label all reaction tubes before pipetting anything.**
2. **Load standards:** with a P200, pipette **50 µL** of each standard into the bottom of its
   reaction tube. **Change tips between standards.**
   `==CONFIRM: the printed digit is partly obscured by a pen mark; the document's own header line
   ("Kit standard tube protocol: 50 µL + 1.5 mL = 1.55 mL, 2 mL microtube") gives 50 µL, which is
   what is written here.==`
3. **Add reagent:** with a P1000 set to **1.5 mL**, dispense reagent directly onto the standard
   droplet in each tube.
4. **Stagger:** add reagent in reading order (row 1 → row 9) at a steady pace — e.g. **one tube
   every 20 s**. Start the timer at the first tube.
5. **Mix:** cap and **invert 5 times**. Do **not** vortex hard — foam and bubbles distort the
   reading.

### 4. Incubation and reading
1. **Incubate 10 min at room temperature.** Unlike BCA, **there is no heating step.**
2. Keep **every** tube at room temperature.
3. Start reading **10 min after the first tube received reagent**. Read at **A595**.
4. ★ **Finish all readings within ~30 min of adding reagent.** Dye–protein aggregates keep forming
   with time and make late readings scattered.

## Notes / common deviations
- **The 30-minute room-temperature equilibration is the step most likely to be skipped and the one
  the document flags hardest.** Cold reagent under-reads.
- **The staggered addition is what makes the 10-minute incubation meaningful.** If reagent is added
  to all tubes at once and then read one at a time, each tube has a different incubation time.
- **Bradford ≠ BCA.** The team's only quantification to date is BCA at 562 nm with **no standard
  curve recorded** (see [9-28](../../../lab_notebook/digitalized/2026-09-28_protein-dilution-bca-quantification.md),
  open item: *"whether a BCA standard series was run — without it these are relative numbers only"*).
  Running this protocol with its nine-point curve would convert those relative numbers into mg/mL
  for the first time.
- **Bradford is sensitive to detergent.** `==CONFIRM: whether BugBuster-based lysates
  ([[iptg_induction_and_protein_extraction]] §3) are compatible with this reagent, or need a
  compatible-kit variant / detergent removal first. The printed document does not mention it and
  this is a real failure mode for a detergent lysis reagent.==`

## Checklist — where do the outputs go?
- [ ] BSA standards S-A … S-I → **room temperature**, discard after the session
- [ ] A595 readings + fitted curve → an analysis notebook in `code/` (none exists yet)
- [ ] Remaining sample → back to **4 °C** or **−20 °C** per its own protocol

## Source
- Printed bench document, photographed 2026-10-20:
  [IMG_6611](../../printed_2026-10-20/IMG_6611.JPG),
  [IMG_6612](../../printed_2026-10-20/IMG_6612.JPG).
- Cross-checked against the notebook's BCA quantification:
  [9-27](../../../lab_notebook/digitalized/2026-09-27_protein-extraction-gel.md),
  [9-28](../../../lab_notebook/digitalized/2026-09-28_protein-dilution-bca-quantification.md).

---
## Log
- 2026-10-20 — Initial transcription from the two photographs of the printed working copy. Both
  pages are legible and the document appears complete (no page footer, content runs 1 → 4 without a
  break). The nine-row dilution table was verified arithmetically row by row before being written
  down. Flagged as **planned, not performed**: the notebook records BCA at 562 nm, never Bradford.
