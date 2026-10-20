---
title: Plasmid Miniprep, Transformation into E. coli BL21(DE3), and Seed Culture Preparation
type: workflow
purpose: Revive the six frozen plasmid stocks, miniprep them on Monarch columns, transform BL21(DE3) by heat shock with both controls, and bank a working glycerol stock that removes the need to ever re-transform.
references:
  - "[[iptg_induction_and_protein_extraction]]"
  - "[[revive_bacteria_from_glycerol_stock]]"
  - "[[glycerol_stock_storage]]"
  - "[[single_colony_inoculation]]"
  - "[[od600_measurement]]"
  - "[[lb_agar]]"
  - "[[lb_broth]]"
source:
  - protocol/printed_2026-10-20/IMG_6621.JPG
  - protocol/printed_2026-10-20/IMG_6622.JPG
  - protocol/printed_2026-10-20/IMG_6623.JPG
  - protocol/printed_2026-10-20/IMG_6624.JPG
  - protocol/printed_2026-10-20/IMG_6625.JPG
  - protocol/printed_2026-10-20/IMG_6626.JPG
  - lab_notebook/digitalized/2026-09-03_stock-prep-plasmid-extraction-od600.md
  - lab_notebook/digitalized/2026-09-04_restreak-quantification-transformation.md
estimated_time: ≈ 4 days end to end (revival overnight → seed overnight → miniprep + transformation day → colony pick overnight)
---

# Plasmid Miniprep, Transformation into BL21(DE3), and Seed Culture Preparation

## Purpose
The front half of the expression pipeline: get from **six frozen plasmid stocks** to **six banked
BL21(DE3) working glycerol stocks**, so that every later induction round starts from a scrape of
frozen cells rather than a fresh transformation. Hands off directly to
[[iptg_induction_and_protein_extraction]] §1.

> [!warning] Provenance — printed bench document, six of eleven pages photographed
> Transcribed from photographs of the team's printed working copy, taken **2026-10-20**. The
> document is footered **"Page n of 11"** and the photo set contains **pages 1, 3, 5, 7, 9 and 11
> only**:
> [p1](../../printed_2026-10-20/IMG_6621.JPG) ·
> [p3](../../printed_2026-10-20/IMG_6622.JPG) ·
> [p5](../../printed_2026-10-20/IMG_6623.JPG) ·
> [p7](../../printed_2026-10-20/IMG_6624.JPG) ·
> [p9](../../printed_2026-10-20/IMG_6625.JPG) ·
> [p11](../../printed_2026-10-20/IMG_6626.JPG).
> **Pages 2, 4, 6, 8 and 10 were not photographed.** Nothing on them is reconstructed below.

> [!note] Why the even pages are missing — and how to fix it in five minutes
> Both multi-page documents in this set are missing **exactly their even pages**: 1/3/5/7 of a
> 7-page document, 1/3/5/7/9/11 of an 11-page one. That is the signature of **double-sided
> printing photographed one side only** — six sheets, fronts captured, backs not turned over.
> **Re-photographing the reverse of each sheet would complete both protocols.** Until then the
> gaps below stand.

## Quick-lookup table — what gets made, per plasmid

| Stage | Output | Count | Storage |
|---|---|---|---|
| §1 Revival | LB+Kan streak plate | 6 | 4 °C, Parafilm, ~4 weeks |
| §1 Seed culture | 50 mL overnight | 6 | — |
| §2 Miniprep | plasmid eluate, 30–50 µL | 6 | −20 °C (or 4 °C if used within a week) |
| §3 Transformation | LB+Kan selection plates | 6 + 2 controls | 37 °C, 14–18 h |
| §4 Working stock | 25 % glycerol cryovial | 2–3 per plasmid | **−80 °C** |

## Materials & equipment
- **LB agar plates with kanamycin (50 µg/mL)** — see [[lb_agar]]; **LB broth with kanamycin
  (50 µg/mL)** — see [[lb_broth]]
- **Six source stocks** (one per plasmid), at −80 °C; dry ice
- **NEB Monarch Plasmid Miniprep Kit (T1010)**
- **NEB BL21(DE3) competent E. coli, High Efficiency (C2527H)** — one 50 µL aliquot per
  transformation, kept at −80 °C until use
- **NEB SOC Outgrowth Medium (B9020S)**
- Sterile 250 mL Erlenmeyer flasks; sterile **14 mL** culture tubes; sterile 1.5 mL and 2 mL tubes;
  **2 mL cryovials**
- Microcentrifuge (13 000–16 000 × g); **water bath or heat block at 42 °C** + an independent
  thermometer; ice bucket with crushed ice; **37 °C shaking incubator (250 rpm)**
- NanoDrop or Qubit
- **Sterile 50 % glycerol** (autoclaved); liquid nitrogen or dry ice

## Reagents
- Kanamycin, 50 µg/mL working concentration throughout
- Monarch **Plasmid Resuspension Buffer B1** (pink, contains RNase A), **Plasmid Lysis Buffer B2**
  (blue/green), **Neutralization Buffer B3** (yellow), **Plasmid Wash Buffer 1**, **Plasmid Wash
  Buffer 2**, **DNA Elution Buffer**
- **pUC19 control DNA** (supplied with the NEB competent-cell kit)

## Procedure

### 1. Revival of frozen source cells (−80 °C glycerol stocks)

**a) Streak-plate revival (recommended)**
1. **Pre-warm** one LB + Kanamycin agar plate per plasmid (6 total) to **37 °C for 15–20 min**.
   Label each plate clearly with the plasmid name and date.
2. Retrieve the frozen stocks from −80 °C and place them on **dry ice**. ★ **Do NOT let them thaw.**
3. Near the flame, **scrape a small amount** of frozen culture from the surface of the stock with a
   sterile loop or pipette tip. Take only what sticks to the tip — do not thaw the full vial.
4. Streak onto the pre-warmed LB + Kan plate using a standard **three-quadrant streak** for single
   colonies.
5. **Immediately return the frozen stock to −80 °C. Repeated freeze–thaw kills viability.**
6. Incubate the plates **inverted at 37 °C overnight (14–18 h)**.
7. **Checkpoint.** Next morning you should see well-defined single colonies.
   - **A lawn** → the stock was too concentrated; restreak from an existing colony onto a fresh plate.
   - **No colonies** → either the stock has lost viability, or the kanamycin concentration is too
     high; **streak on LB without antibiotic as a viability control**.

**b) Liquid overnight culture from a single colony**
1. Near the flame, pick **ONE well-isolated single colony per plasmid** with a sterile pipette tip.
2. Inoculate into **50 mL of sterile LB + Kanamycin (50 µg/mL)** in a sterile **250 mL** Erlenmeyer
   flask. Cover the mouth with a **doubled sheet of aluminium foil** pressed around the neck
   (autoclavable, allows gas exchange).
3. Incubate at **37 °C, 200 rpm** (or 220 rpm if the flask is not baffled) for **14–16 h**, until
   visibly turbid (**OD600 ≈ 2–4**).
4. Keep the streaked plates sealed with **Parafilm at 4 °C**. They are the working stock for the
   next ~4 weeks and let you skip revival on future rounds.

`==UNDONE: page 2 — whatever follows §1b.==`

### 2. Plasmid DNA extraction (NEB Monarch Plasmid Miniprep Kit, T1010)

**a) Cell harvest**
1. For each of the 6 overnight cultures, transfer **4.5 mL into a sterile 1.5 mL tube in successive
   1.5 mL fractions**: pipette 1.5 mL, spin at **13 000 × g for 1 min at room temperature**,
   discard supernatant, add the next 1.5 mL onto the same pellet, spin again, etc.
2. After the final spin, **aspirate and discard the supernatant completely**.

**b) Resuspension, lysis, neutralization**
1. Add **200 µL Plasmid Resuspension Buffer B1** (pink, contains RNase A) to the pellet.
2. ★ **Vortex vigorously until the pellet is completely resuspended** — no visible clumps. This is
   the **only** step where vortexing is required; incomplete resuspension is the most common cause
   of low miniprep yield.
3. Add **200 µL Plasmid Lysis Buffer B2** (blue/green). Mix by **gently inverting 5–6 times**. The
   solution should turn uniformly blue/green and become viscous.
4. **Incubate at room temperature for exactly 1 min. Do NOT exceed 5 min** — prolonged alkaline
   lysis irreversibly denatures the plasmid.
5. Add **400 µL Neutralization Buffer B3** (yellow). Mix gently by inversion **5–6 times** until the
   colour changes fully from blue to yellow, with a heavy white precipitate forming. **Do NOT
   vortex** — shearing here co-precipitates plasmid with genomic DNA.
6. **Centrifuge at 16 000 × g for 2–5 min at room temperature.** The white pellet is genomic DNA,
   protein and cell debris; the clear supernatant contains the plasmid.

**c) Column binding, washing, and elution**
1. Insert a Monarch spin column into a collection tube. Carefully transfer the cleared supernatant
   (**≈ 800 µL**) to the column without disturbing the pellet.
2. **Centrifuge at 16 000 × g for 1 min.** Discard the flow-through and re-insert the column in the
   same collection tube.
3. Add **200 µL Plasmid Wash Buffer 1**. Centrifuge at **16 000 × g, 1 min**. Discard flow-through.
4. Add **400 µL Plasmid Wash Buffer 2**. Centrifuge at **16 000 × g, 1 min**. Discard flow-through.
5. Transfer the column to a clean, labelled 1.5 mL tube.
6. Add **30–50 µL DNA Elution Buffer** directly to the centre of the column matrix. **Do not let the
   tip touch the matrix.**
7. **Incubate 1 min at room temperature** to let the DNA rehydrate off the matrix.
8. `==UNDONE: the final elution spin — page 4 was not photographed. Page 5 resumes at the elution
   volume tip below.==`
9. **Elution volume tip:** 30 µL gives higher concentration; 50 µL gives higher total yield at lower
   concentration. Since **1–100 ng is enough** for the transformation in §3, **elute in 30 µL** to
   keep concentration high for storage.

**d) Quantification and quality check**
1. On **NanoDrop**, blank with 1–2 µL of DNA Elution Buffer, then measure 1–2 µL of each eluate.
2. Record **concentration (ng/µL)**, **A260/A280** (target ≈ 1.8–2.0 for pure DNA) and **A260/A230**
   (target > 1.8; lower values indicate carryover of wash buffer).
3. **Expected yield: 15–25 µg total (500–800 ng/µL in 30 µL)** for a high-copy vector. Low-copy
   vectors (pBR322-derived) will give **3–8 µg**.
4. Label each tube: plasmid name, date, concentration. Store at **−20 °C** long-term, or **4 °C** if
   you will transform within a week.
5. **Optional QC:** if plasmid identity is in any doubt, run **200 ng** of each eluate on a **1 %
   agarose gel** next to a DNA ladder to confirm the expected size and the absence of genomic-DNA
   smearing. Alternatively do a diagnostic restriction digest with an enzyme that cuts the vector
   in a known pattern. **Worth doing before committing to the full transformation and induction
   workflow.**

`==UNDONE: page 6 — whatever sits between §2d and §3.==`

### 3. Transformation into E. coli BL21(DE3) chemically competent cells

**a) Preparation (do this first)**
1. **Pre-warm** the required LB + Kan plates (**6 for plasmids + 2 for controls = 8**) at **37 °C
   for 30 min**.
2. **Pre-warm the SOC medium to room temperature. Do NOT use it cold from the fridge** — cold SOC
   drops recovery efficiency significantly.
3. Set the water bath / heat block to **exactly 42 °C** and **verify with an independent
   thermometer**. Even ±2 °C matters for heat-shock efficiency in this specific NEB protocol.
4. Label eight 1.5 mL tubes: 6 for plasmids (one per construct) + 2 controls (**positive: pUC19**
   supplied with the kit; **negative: no DNA**).
5. Chill all 8 labelled tubes on ice for at least 5 min.

**b) Cell thawing and DNA addition**
1. Thaw the BL21(DE3) competent cells **on ice for 10 min**. Do NOT thaw at room temperature or in
   your hand — the cells lose competency rapidly above 4 °C.
2. **Gently flick the tube 2–3 times** to mix. **Do NOT vortex** — competent cells are extremely
   fragile.
3. Aliquot **50 µL of competent cells** into each of the 8 pre-chilled tubes on ice.
4. Add **1–5 µL of plasmid DNA (1–100 ng total)** to each of the 6 plasmid tubes. For eluates at
   ≈ 500 ng/µL from §2, **dilute 1:100 in DNA Elution Buffer first**, then add **1 µL (≈ 5 ng)**.
5. **Positive control:** add **10 pg of the pUC19 control DNA** supplied with the NEB kit.
6. **Negative control:** add **1 µL of DNA Elution Buffer only (no DNA)**.
7. Carefully **flick each tube 4–5 times** to mix cells and DNA. Do NOT pipette up and down, do NOT
   vortex.
8. Place all 8 tubes back on ice and incubate for **exactly 30 min**.

**c) Heat shock and recovery**
1. ★ Transfer all 8 tubes to the **42 °C** water bath **at once**. Incubate for **exactly 10
   seconds** — this is the NEB-specified time for BL21(DE3) High Efficiency. **Longer heat shocks
   (30 s, 45 s) that work for other cell lines will KILL these cells.**
2. Return all tubes to ice immediately. Incubate on ice for **exactly 5 min**.
3. Add **950 µL of room-temperature SOC medium** to each tube.
4. Incubate at **37 °C, 250 rpm, for exactly 60 min.** **Do NOT shorten this recovery** — the
   kanamycin resistance gene needs time to be expressed before selection.

**d) Plating on selection**
1. For each of the 6 plasmid transformations **and the positive control**: spread **50–100 µL** of
   the recovery culture onto a pre-warmed LB + Kan plate with a sterile spreader. If colonies are
   expected to be dense, also plate **200 µL** on a second plate to get a range of colony density.
2. **Negative control:** plate **100 µL** on the last LB + Kan plate. **This plate SHOULD BE EMPTY**
   the next morning. Any colonies here indicate kanamycin degradation, plate contamination, or
   untransformed cells growing through (a competency problem).
3. Let the plates dry **uncovered for 5 min near the flame**, then incubate **inverted at 37 °C for
   14–18 h**.
4. **Expected results.** Plasmid plates: dozens to hundreds of well-isolated colonies. Positive
   control (pUC19): a lawn or hundreds of colonies (NEB C2527H is rated **≥ 1 × 10⁶ CFU/µg
   pUC19**). Negative control: **zero** colonies. If the positive control fails, the competent
   cells were compromised — repeat with a fresh aliquot. If the negative control has colonies,
   **discard everything and remake the antibiotic plates**.

`==UNDONE: pages 8 and 10 — whatever follows §3c and §3d.==`

### 4. Colony selection, seed culture, and working glycerol stock

**a) Colony picking and overnight seed culture**
1. From each of the 6 transformation plates, pick **2–3 well-isolated single colonies** (in case one
   fails). Number them, e.g. `CDS11-c1`, `CDS11-c2`, `CDS11-c3`.
2. For each picked colony, inoculate into **5 mL sterile LB + Kanamycin (50 µg/mL)** in a **14 mL
   culture tube**, loose cap for aeration.
3. Incubate at **37 °C, 220 rpm, 14–16 h** until visibly turbid (**OD600 ≈ 2–4**).
4. Measure OD600 in the morning. **Pick the colony per plasmid that gave the most robust growth**
   (highest OD, no odd colour or smell). Discard the runners-up, or keep them at 4 °C as short-term
   backups.

**b) Working glycerol stock preparation — do this BEFORE any induction work**
1. For each of the 6 selected seed cultures, mix **500 µL of overnight culture with 500 µL of
   sterile 50 % glycerol** in a labelled 2 mL cryovial. Final glycerol concentration is **25 %**,
   which is optimal for long-term viability.
2. Mix by gently inverting 5–6 times, or a brief low-speed vortex.
3. **Snap-freeze in liquid nitrogen (30 s) or on dry ice (5 min).**
4. Transfer directly to **−80 °C** for long-term storage.
5. Prepare **2–3 cryovials per plasmid** — one working stock, the rest untouched backups. Label each
   with plasmid name, date, your initials, and strain (**BL21(DE3)**).
6. ★ **Why this matters.** These fresh working stocks eliminate the need to re-transform for every
   future experiment. All future IPTG induction runs — including the daily maintenance passaging in
   §1 of the induction protocol — can start by scraping directly from these stocks, **saving 3–4
   days per round**.

**c) Handoff to the IPTG induction protocol**
1. The remaining volume (**≈ 4 mL**) of each overnight seed culture is the input to **§1 (Daily
   maintenance passaging)** of [[iptg_induction_and_protein_extraction]].
2. Measure OD600 and record. Use it directly to inoculate the maintenance passage, or refrigerate at
   **4 °C for up to 24 h** if you cannot start the same day.
3. From this point forward, all IPTG induction and downstream analysis follow that protocol.

## Notes / common deviations
- **As run, 2026-09-04 — the transformation differs from the printed protocol in four ways.** The
  notebook's [9-4 entry](../../../lab_notebook/digitalized/2026-09-04_restreak-quantification-transformation.md)
  records: **5 µL** of plasmid DNA added to **50 µL** cells (the printed protocol says 1–5 µL of a
  1:100 dilution); **no pUC19 positive control** — only a cells-only negative; **100 µL plated**
  per construct; and recovery/selection plates incubated at **30 °C overnight**, not 37 °C.
  Outcome, from [9-6](../../../lab_notebook/digitalized/2026-09-06_inoculate-transformed-colonies.md):
  ~43 plates grew, one `e40` plate carrying fungus. All versions preserved; **the printed protocol
  is not a record of what was done in September.**
- **The miniprep as run is older than this document.** On
  [9-3](../../../lab_notebook/digitalized/2026-09-03_stock-prep-plasmid-extraction-od600.md) the
  team used **4 mL** of culture (not 4.5 mL) and recorded only *"follow the kit protocols with some
  modifications"*, leaving `==CONFIRM: which miniprep kit, and what the modifications were.==`
  **This file answers the first half of that question if — and only if — the printed document was
  already in use on 9/3**, which is not established.
  `==CONFIRM: the date this printed protocol entered use.==`
- **The 9/4 plasmid quantification was fluorimetric, not NanoDrop.** Six standards (0/1/3/10/30/100)
  plus five samples at 5 µL each, analysed in
  [`code/0904_quantification.ipynb`](../../../code/0904_quantification.ipynb) — no A260/A280 or
  A260/A230 purity ratios exist for these plasmids.
- **The 10-second heat shock is the step most likely to be got wrong**, because 30 s and 45 s are
  the numbers most people carry from other protocols. The document flags it; so does this note.
- **The working-stock step (§4b) is the one that paid off.** Every autumn induction round started
  from a scrape of these stocks rather than a fresh transformation.

## Checklist — where do the outputs go?
- [ ] Streaked LB + Kan plates → **4 °C**, Parafilm-sealed, ~4 weeks working stock
- [ ] Plasmid eluates → **−20 °C** long-term, **4 °C** if transforming within a week
- [ ] Transformation selection plates → **37 °C inverted, 14–18 h**, then 4 °C
- [ ] Working glycerol stocks (2–3 cryovials per plasmid, 25 % glycerol) → **−80 °C**
- [ ] Remaining ≈ 4 mL seed culture → **4 °C** for ≤ 24 h, or straight into the induction protocol

## Source
- Printed bench document, photographed 2026-10-20 — pages 1, 3, 5, 7, 9, 11 of 11:
  [IMG_6621](../../printed_2026-10-20/IMG_6621.JPG),
  [IMG_6622](../../printed_2026-10-20/IMG_6622.JPG),
  [IMG_6623](../../printed_2026-10-20/IMG_6623.JPG),
  [IMG_6624](../../printed_2026-10-20/IMG_6624.JPG),
  [IMG_6625](../../printed_2026-10-20/IMG_6625.JPG),
  [IMG_6626](../../printed_2026-10-20/IMG_6626.JPG).
- As-run records: [9-3](../../../lab_notebook/digitalized/2026-09-03_stock-prep-plasmid-extraction-od600.md),
  [9-4](../../../lab_notebook/digitalized/2026-09-04_restreak-quantification-transformation.md),
  [9-6](../../../lab_notebook/digitalized/2026-09-06_inoculate-transformed-colonies.md).

---
## Log
- 2026-10-20 — Initial transcription from six photographs of the printed working copy. The document
  is eleven pages; **pages 2, 4, 6, 8 and 10 were not photographed** and are marked `==UNDONE==` in
  place. Noted that both multi-page documents in this set are missing exactly their even pages,
  which points at double-sided sheets photographed on one side only — re-shooting the reverse of
  each sheet would close every gap. The September as-run transformation is recorded beside the
  printed version rather than merged into it: the two differ in DNA amount, controls, plating
  volume and incubation temperature.
