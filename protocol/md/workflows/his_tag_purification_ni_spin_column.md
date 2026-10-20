---
title: His-Tag Protein Purification — NEBExpress® Ni Spin Columns (NEB #S1427), 4 Samples in Parallel
type: workflow
purpose: Capture His-tagged protein from a clarified BugBuster lysate on a nickel spin column and elute it in 500 mM imidazole, keeping every fraction for a diagnostic gel.
references:
  - "[[iptg_induction_and_protein_extraction]]"
  - "[[bradford_protein_assay]]"
  - "[[dot_blot_his_tag]]"
source:
  - protocol/printed_2026-10-20/IMG_6617.JPG
  - protocol/printed_2026-10-20/IMG_6618.JPG
  - protocol/printed_2026-10-20/IMG_6619.JPG
  - protocol/printed_2026-10-20/IMG_6620.JPG
  - lab_notebook/digitalized/2026-10-01_protein-purification.md
estimated_time: ≈ 2 h for 4 columns in parallel, plus buffer preparation and a 30 min chill
---

# His-Tag Protein Purification — NEBExpress® Ni Spin Columns (NEB #S1427)

## Purpose
Take the clarified soluble fraction from [[iptg_induction_and_protein_extraction]] §3 and capture
the His-tagged construct on a **NEBExpress Ni Spin Column**, washing at 5 mM imidazole and eluting
at 500 mM. Written for **four samples in parallel (M1–M4)**. Every fraction is retained, because
the diagnostic value of this protocol is knowing *where* the protein went when it does not elute.

> [!warning] Provenance — printed bench document, four of seven pages photographed
> Transcribed from photographs of the team's printed working copy, taken **2026-10-20**. The
> document is footered **"Page n of 7"** and the photo set contains **pages 1, 3, 5 and 7 only**:
> [p1](../../printed_2026-10-20/IMG_6617.JPG) ·
> [p3](../../printed_2026-10-20/IMG_6618.JPG) ·
> [p5](../../printed_2026-10-20/IMG_6619.JPG) ·
> [p7](../../printed_2026-10-20/IMG_6620.JPG).
> **Pages 2, 4 and 6 were not photographed and are not transcribed here.** Nothing on them has been
> guessed at or reconstructed.

> [!failure] Known gaps, by position in the document
> - **Page 2** — between the tube-labelling table (§1b) and the start of §2. It must hold the
>   **lysate preparation and adjustment** steps, because §2b below cross-references *"adjusted
>   lysate (Section 2d)"* and no such section appears on any photographed page.
>   `==UNDONE: how the lysate is adjusted before loading — almost certainly the imidazole and salt
>   match to Lysis/Binding Buffer, and it is the step most likely to explain the 10/10 capture
>   failure. Re-photograph page 2.==`
> - **Page 4** — between §2c (sequential loading) and §2d (washes). Content unknown.
> - **Page 6** — between §2f (storage) and §4 (SDS-PAGE analysis). It holds **section 3**, whose
>   title and content are unknown.
> - The document's own numbering jumps from **§2** to **§4** across the photographed pages, which
>   is consistent with a §3 on page 6.

## Quick-lookup table — working buffers from NEB concentrates (4 samples, ~30 % overage)

Label three 15 mL conical tubes and combine:

| Component | Lysis/Binding (5 mL) | Wash (5 mL) | Elution (3 mL) |
|---|---|---|---|
| 2X IMAC Buffer (B1076) | 2.5 mL | 2.5 mL | 1.5 mL |
| 2 M Imidazole (B1077) | — | 12.5 µL | 750 µL |
| Ultrapure H₂O | 2.5 mL | 2.49 mL | 750 µL |
| **Final [imidazole]** | **0 mM** | **5 mM** | **500 mM** |
| Final [phosphate / NaCl] | 20 mM / 300 mM | 20 mM / 300 mM | 20 mM / 300 mM |
| pH | 7.4 | 7.4 | 7.4 |

Every column sums to its stated total volume. After combining:
- **Mix each buffer by inversion (10×).**
- **Verify pH with a strip or meter — must be 7.3–7.5.** Adjust with NaOH/HCl if needed.
- **Chill all three buffers on ice or at 4 °C for ≥ 30 min before use.**

## Quick-lookup table — tube labelling (8 tubes per sample, 32 in total)

| Tube label (per sample M1–M4) | Purpose |
|---|---|
| M#-Load | 2 µL lysate aliquot for SDS-PAGE |
| M#-FT1 (+ FT2, FT3 if multiple loads) | Flow-through from binding — SDS-PAGE only |
| M#-W1, M#-W2, M#-W3 | Three sequential washes — SDS-PAGE only |
| M#-E1, M#-E2 | Two sequential elutions — SDS-PAGE only |

**Pre-label ALL tubes before touching samples.**

## Materials & equipment
- **NEBExpress Ni Spin Columns (S1427)** — one per sample, with collection tubes and bottom plugs
- **2X IMAC Buffer (B1076)**, **2 M Imidazole (B1077)**, ultrapure H₂O
- Three 15 mL conical tubes
- **2 mL microcentrifuge tubes — 32 + 4 discard tubes**
- pH strips or pH meter
- Ice bucket; **microcentrifuge at 4 °C**
- End-over-end rotator (optional — a manual alternative is given)

## Procedure

### 1. Reagent preparation
Prepare **all** buffers **before** starting sample handling, per the two tables above.

`==UNDONE: section 1 may continue onto page 2, which was not photographed.==`

### 2. Column procedure (all 4 columns in parallel)
*Materials: Ni spin columns with collection tubes and bottom plugs, chilled Lysis/Binding, Wash and
Elution buffers, pre-labelled 2 mL tubes, microcentrifuge at 4 °C.*

**a) Column equilibration (once per column)**
1. Twist off the bottom tab and loosen the top cap.
2. Place the column in the provided 2 mL collection tube.
3. **Centrifuge at 800 × g, 1 min, 4 °C** to remove the storage buffer. Discard the flow-through
   and the tube.
4. Place the column in a new 2 mL tube and add **250 µL of chilled Lysis/Binding Buffer**.
5. **Centrifuge at 800 × g, 1 min, 4 °C.** Discard the flow-through.
6. Place the column in a new 2 mL tube labelled **M#-FT1**.

**b) Binding (first load)**
1. Add **500 µL of adjusted lysate** to each column.
   `==CONFIRM: the document cites "(Section 2d)" for the adjustment, but §2d on page 5 is the wash
   step. The real reference is on an unphotographed page.==`
2. Close the top cap firmly and **insert the bottom plug** (supplied with the kit).
3. **Mix by end-over-end rotation at 4 °C for 15 min.**
   - *Manual alternative:* slowly rotate the tube **180° over ~2 s**, hold upside-down for **1 s**,
     rotate back over ~2 s, then **rest on ice for 30 s**. Repeat for **~30 inversions in 15 min**.
4. ★ **Remove the bottom plug FIRST, then loosen the top cap.**
5. **Centrifuge at 800 × g, 1 min, 4 °C.** Keep the flow-through (**M#-FT1**) on ice for SDS-PAGE —
   **this fraction shows whether the protein failed to bind.**

**c) Optional — sequential loading (weak expression)**
1. If additional adjusted lysate was prepared, move the column to a new tube labelled **M#-FT2**.
2. Add another **500 µL of adjusted lysate** and repeat the binding (cap and plug, 15 min rotation,
   remove plug, spin).
3. **Up to 3–4 total loads** are possible. **Save every flow-through separately.**

**d) Washes (three per column)**
1. Place the column in a new tube labelled **M#-W1**.
2. Add **250 µL of chilled Wash Buffer**, dispensing against the column wall **above the resin bed**.
3. **Let stand 30 s** (allows the imidazole to compete off weak binders).
4. **Centrifuge at 800 × g, 1 min, 4 °C.** Keep M#-W1 on ice.
5. Move the column to **M#-W2** and repeat (buffer, 30 s, spin). Repeat once more in **M#-W3**.
6. **Keep all three wash fractions for diagnostic SDS-PAGE.**

**e) Elution (two per column)**
1. Place the column in a new tube labelled **M#-E1**.
2. Add **200 µL of chilled Elution Buffer**, dispensing against the wall above the resin.
3. Resuspend the resin bed thoroughly:
   - **Method A — cap-and-flick (recommended, more reproducible):** close the top cap, insert the
     bottom plug, and **flick the bottom of the column sharply 10–15 times**. If the bed does not
     disperse, invert 5 more times. The compacted bed should disappear and the liquid become
     uniformly turbid. Remove the plug and loosen the cap.
   - `==UNDONE: the document says "one of the two methods below" and only Method A is on the
     photographed page. Method B is not in the photo set.==`
4. **Incubate 2 min at 4 °C** (allows the imidazole to displace the bound His-tagged protein).
5. **Centrifuge at 800 × g, 1 min, 4 °C.** Keep M#-E1 on ice.
6. Move the column to **M#-E2** and repeat the elution (buffer, resuspension, 2 min, spin). The
   second elution typically recovers an additional **10–20 %**; combined yield **> 90 %**.
7. For a more concentrated eluate, reduce the elution volume to **100 µL per step** (E1 and E2).
   Total yield is comparable, but concentration doubles.

**f) Storage**
- **Short-term (< 1 day):** keep all fractions on ice or at 4 °C.
- **Longer-term:** add glycerol to **10 % final** and store at **−80 °C**, or dialyse into a storage
  buffer of choice.
- ★ **Keep every fraction (Load, all FTs, all Ws, E1, E2) until SDS-PAGE confirms the result.**

### 3. *(unknown — page 6 not photographed)*
`==UNDONE: section 3's title and content.==`

### 4. SDS-PAGE analysis (diagnostic)
*Materials: SDS-PAGE gel and running setup, protein ladder, retained fractions (M#-Load, M#-FT,
M#-W3, M#-E1, M#-E2).*

**a) Gel loading (per sample)**

| Lane | Sample | Volume to load |
|---|---|---|
| 1 | Ladder | per manufacturer |
| 2 | M#-Load (clarified lysate) | 10 µL |
| 3 | M#-FT1 (or pooled FTs) | 10 µL |
| 4 | M#-W3 (last wash) | 15 µL |
| 5 | M#-E1 | 5 µL |
| 6 | M#-E2 | 10 µL |

> [!note] Handwritten sticky note on page 7
> **"Warm up gel 10 min before loading."** (Blue sticky note, pasted over the lower half of the
> page; nothing printed is obscured by it.)

## Notes / common deviations
- **As run, 2026-10-01 — the lane layout differs from the one printed here.** The team's first
  purification ([10-01](../../../lab_notebook/digitalized/2026-10-01_protein-purification.md)) ran
  **12 lanes across two constructs**: ladder, then *CDS10* at 1:1 (20 µL), 1:2 (10 µL sample +
  10 µL MQ), W3, E1, E2, then the same six for *e40*, then a second ladder. W3/E1/E2 at 20 µL each,
  not the 15/5/10 µL above. The notebook page cites this protocol by name and number but records
  **"8 samples"** against 10 loaded lanes — unresolved.
- **The result of that run was nothing eluted**, for *CDS10* and *e40*. A second gel the same day
  on *CDS11*, *CDS12*, *e1* and *e281* is the **only purification of the project that eluted
  protein** — *e1* at ~41 kDa (expected 41.9) and *CDS11* at ~43 kDa against an expected 72.0 kDa.
- **The 2026-10-10 *e281* run failed at capture, not at expression.** The gel showed blank elutions
  and a flow-through matching the load; the 10/19 dot blot then found the **His tag in the e281
  flow-through** at 2.9× the negative control. That is a *binding* problem — and the step that
  governs binding is the lysate adjustment **on the unphotographed page 2**. Recovering that page
  is the single highest-value thing left in this file.
- **Keep the flow-through.** Both of this project's informative results came from fractions that a
  tidier workflow would have poured away.
- **Imidazole carries into the eluate at 500 mM.** Anything done downstream on E1/E2 — including a
  plate-based activity assay — needs an **imidazole vehicle control**; see the note in
  [[depolymerase_activity_assay]].

## Checklist — where do the outputs go?
- [ ] Working buffers (Lysis/Binding, Wash, Elution) → **ice / 4 °C**, ≥ 30 min before use
- [ ] M#-Load, M#-FT*, M#-W1–3 → **ice**, hold for the diagnostic gel
- [ ] M#-E1, M#-E2 → **ice / 4 °C** short-term; **−80 °C with 10 % glycerol** longer-term
- [ ] Gel photograph → `data/assays/`

## Source
- Printed bench document, photographed 2026-10-20 — pages 1, 3, 5, 7 of 7:
  [IMG_6617](../../printed_2026-10-20/IMG_6617.JPG),
  [IMG_6618](../../printed_2026-10-20/IMG_6618.JPG),
  [IMG_6619](../../printed_2026-10-20/IMG_6619.JPG),
  [IMG_6620](../../printed_2026-10-20/IMG_6620.JPG).
- As-run record: [10-01](../../../lab_notebook/digitalized/2026-10-01_protein-purification.md).
- Downstream evidence: [10-19 dot blot](../../../lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md),
  [`code/1010_gel_annotation.ipynb`](../../../code/1010_gel_annotation.ipynb).

---
## Log
- 2026-10-20 — Initial transcription from four photographs of the printed working copy. The
  document is seven pages; **pages 2, 4 and 6 were not photographed** and are marked `==UNDONE==`
  in place rather than reconstructed. Both buffer tables were checked against their stated totals
  (5 mL / 5 mL / 3 mL) before being written down. The dangling "(Section 2d)" cross-reference in
  §2b is recorded as a discrepancy, not silently repointed.
