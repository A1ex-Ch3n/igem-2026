---
title: Maintenance, IPTG Induction, BugBuster Extraction & SDS-PAGE (printed bench document)
type: workflow
purpose: The four-part printed protocol behind the expression work — daily passaging of transformed BL21(DE3), IPTG induction of a 100 mL culture, BugBuster lysis to a soluble protein fraction, and SDS-PAGE with Coomassie detection.
references:
  - "[[plasmid_miniprep_transformation_seed_culture]]"
  - "[[bradford_protein_assay]]"
  - "[[his_tag_purification_ni_spin_column]]"
  - "[[dot_blot_his_tag]]"
  - "[[od600_measurement]]"
  - "[[lb_broth]]"
source:
  - protocol/printed_2026-10-20/IMG_6614.JPG
  - protocol/printed_2026-10-20/IMG_6615.JPG
  - lab_notebook/digitalized/2026-09-17_daily-passing.md
  - lab_notebook/digitalized/2026-09-27_protein-extraction-gel.md
  - lab_notebook/digitalized/2026-10-14_protein-extraction-bugbuster-scaling.md
estimated_time: 1 day per induction round (overnight seed + ~4 h to induction + overnight expression), then ~1.5 h lysis and ~3 h gel
---

# Maintenance, IPTG Induction, BugBuster Extraction & SDS-PAGE

## Purpose
This is the **single printed document that carried the whole expression workflow**, from
keeping a transformed BL21(DE3) culture alive day to day, through IPTG induction, to a soluble
lysate and a stained gel. It is the protocol behind the 9/15, 9/27–9/29, 10/10 and 10/14 bench days.
Its input is a transformed working stock from [[plasmid_miniprep_transformation_seed_culture]]; its
outputs feed [[his_tag_purification_ni_spin_column]] and [[dot_blot_his_tag]].

> [!warning] Provenance — printed bench document with handwritten amendments
> Transcribed from photographs of the team's printed working copy, taken **2026-10-20**:
> [IMG_6614](../../printed_2026-10-20/IMG_6614.JPG) (sections 1–2) and
> [IMG_6615](../../printed_2026-10-20/IMG_6615.JPG) (sections 3–4a). The printed pages carry **no
> page footer and no author line**. Every handwritten change on them is reproduced below and
> **labelled as handwritten**; nothing handwritten has been merged silently into the printed text.

> [!failure] The document is incomplete — the end of section 4 is missing
> The second photograph **stops mid-section-4a**, after "Load samples: 20 µL of each prepared
> sample …". **Running conditions, Coomassie staining and destaining are not in the photo set.** A
> third photograph ([IMG_6616](../../printed_2026-10-20/IMG_6616.JPG)) was taken of what appears to
> be the next sheet but is **unrecoverable motion blur** — sharpening and autocontrast recover no
> glyphs at all. Those steps are therefore `==UNDONE==` here. Do not treat section 4 as runnable
> from this file alone.

## Quick-lookup table — the three culture scales actually used

| Scale | Vessel | Medium | Seed | Induction | Where it comes from |
|---|---|---|---|---|---|
| **Daily passage** | 50 mL tube | 50 mL LB + Kan 50 µg/mL | 250 µL of yesterday's culture | — | printed §1 |
| **Expression, printed** | 500 mL baffled flask | 100 mL LB + Kan | 1 mL seed (1:100) | 400 µM IPTG = 1.4 mL stock | printed §2 |
| **Expression, handwritten** | 20 mL tube | 2 mL LB | one colony | **700 µL IPTG in 50 mL culture, after 4 h** | handwritten on §2 |
| **Expression, as run 9/27** | — | 25 mL media + 25 mL sample | — | **200 µL of 40 mg/mL IPTG** (≈ 0.16 mg/mL ≈ 0.67 mM) | [9-27](../../../lab_notebook/digitalized/2026-09-27_protein-extraction-gel.md) |

**All four are kept.** They disagree, and the repo rule is to preserve every version rather than
reconcile to one. `==CONFIRM: which scale was used on which bench day. 9-27 is the only one with a
recorded IPTG amount.==`

## Materials & equipment
- 50 mL tubes (daily passage); **500 mL baffled Erlenmeyer flask** (printed §2) or **20 mL culture
  tubes** (handwritten variant)
- Shaking incubator at **37 °C**, able to run 180 / 220 rpm
- Spectrophotometer for [[od600_measurement]]
- Falcon tubes; **2 mL Eppendorf tubes** (handwritten; printed says 1.5 mL)
- Centrifuge reaching **4000 × g** and a microcentrifuge reaching **16 000 × g at 4 °C**
- **Bolt Mini Gel Tank**; **Bolt 4–12 % gel cassette**
- Pipettes P20/P200/P1000

## Reagents
- **LB broth with kanamycin (50 µg/mL)** — see [[lb_broth]]
- **IPTG stock solution** `[TBD: the printed document never states the stock concentration — only
  "add 1.4 mL … to a final concentration of 400 µM". 9-27 records a 40 mg/mL stock.]`
- **BugBuster Master Mix**
- **Proteinase inhibitor pill** — preparation: **dissolve 1 pill in 10 mL of BugBuster Master Mix
  Buffer** in a Falcon tube. *(Handwritten after this line: **"on ice"**.)*
- **MOPS Buffer 1X** — dissolve 1 provided package of MOPS Buffer into **1 L** of MilliQ water
- **Laemmli Sample Buffer 2X**
- **Coomassie Blue R-250 stain solution**
- **Destaining buffer** — **200 mL pure methanol + 50 mL glacial acetic acid + 250 mL MilliQ water**
- **PageRuler Prestained Protein Ladder**

## Procedure

### 1. Daily maintenance passaging
*Materials: LB broth with kanamycin.* Each day, at roughly the same time:
1. Add **50 mL sterile LB broth (Kanamycin 50 µg/mL)** to the tube.
2. Near the flame, transfer **250 µL of the previous day's culture** (if OD = 0.4–0.6) into the new
   tube. If it looks weak or under-grown, use **V_seed = (0.02 × V_final) / OD_seed** instead.
3. Incubate at **37 °C, 180 rpm**.
4. After **~16–20 h** the culture should be visibly turbid (**OD600 ≈ 2–4**, stationary phase).
   Repeat all the steps.

### 2. 100 mL culture and IPTG induction *(protein expression)*
*Materials: LB broth with kanamycin.*
1. In a **500 mL baffled Erlenmeyer flask**, add **100 mL sterile LB**.
   - *Handwritten alternative:* **"20 mL tubes, 2 mL LB; inoculate a colony …"**
     `==CONFIRM: the rest of this note. The words after "a colony and" are a small inserted scrawl
     ending "… on a plate", with one superscripted word above it that cannot be read reliably.==`
2. Inoculate with **1 mL of the seed culture (1:100 dilution)**.
3. Incubate at **37 °C, 220 rpm**.
4. Start checking OD600 after ~2 h. When **OD600 reaches 0.4–0.6** the cells are in mid-log — this
   is the induction window.
   - *Handwritten over this step:* **"— no need."** i.e. the team **skipped the OD-gated induction
     window** and induced on a clock instead, per the next note.
5. Add IPTG to a final concentration of **400 µM**: add **1.4 mL of IPTG stock solution**.
   - *Handwritten, with "400 µM" struck through:* **"(after 4 hrs) 700 µL IPTG in 50 mL culture."**
6. **Split the media into two flasks (induced and non-induced) to have a control.**
7. Keep incubating **both** flasks at **37 °C, 220 rpm, overnight**.

> [!note] Handwritten instruction across the bottom of §2
> **"Do everything with untransformed host (without antibiotic)."**
> This is an instruction to run an **untransformed BL21 arm in parallel, with no antibiotic** — i.e.
> the empty-host background control. The notebook shows it was **never run**: the 2026-10-19 dot
> blot entry records *"Still no BL21 empty-vector control … the fourth protein assay in a row
> without one."* The instruction exists on paper and was not executed.

### 3. Lysis and purification *(protein extraction)*
*Materials: BugBuster Master Mix, proteinase inhibitor pill (prepared as above).*
1. Take **15 mL of overnight culture** into a Falcon tube.
2. **Pellet at 4000 × g, 10 min.** Discard supernatant.
3. Resuspend the pellet with **1 mL** *(handwritten: **2 mL**)* of "BugBuster Master Mix Buffer +
   Proteinase Inhibitor". Transfer the resuspension to a **1.5 mL** *(handwritten: **2 mL**)*
   Eppendorf tube.
   - *Handwritten brace spanning steps 2–3:* **"twice"** — i.e. pellet and resuspend twice.
   - *Handwritten in the right margin:* **"(for analysis no need for proteinase)"** — the protease
     inhibitor is treated as optional for analytical samples.
4. **Incubate 20 min at room temperature**, with gentle mixing from time to time.
5. **Centrifuge at 16 000 × g for 20 min at 4 °C.**
6. **Transfer the supernatant to another 1.5 mL Eppendorf tube. This is the soluble protein portion
   used in the next steps**, at 4 °C.
7. **Keep the pellet just in case at 4 °C.**
   - *Handwritten immediately below:* **"use it for dot-blotting with HRP-conjugated anti-His Ab."*
     — the origin of [[dot_blot_his_tag]].
     `==CONFIRM: whether "it" is the retained pellet (the line sits directly under step 7) or the
     soluble fraction from step 6. The 10/19 blot spotted lysates and a flow-through, which points
     to the soluble fraction.==`

### 4. SDS-PAGE and Coomassie Blue staining *(protein detection)* — INCOMPLETE
*Handwritten beside the heading:* **"Nanodrop to standardize conc."**

**a) SDS-PAGE**
1. Fill the **Bolt Mini Gel Tank** partially with **MOPS Buffer 1X**.
2. Remove the **Bolt 4–12 % gel cassette from its pouch.** Rinse briefly with distilled water.
   **Peel off the tape at the bottom** — this is critical; if left on, current cannot flow — and
   remove the comb by pulling straight up gently. Secure it on the Bolt Mini Gel Tank.
3. **Sample preparation:** use **20 µL of 2× Laemmli Sample Buffer with 20 µL of your sample**.
4. **Load the ladder:** **7 µL of PageRuler Prestained** directly into the **first and last** well.
   It needs no loading buffer — it comes ready-to-load.
5. **Load samples:** **20 µL** of each prepared sample into subsequent wells. Pipette slowly to let
   the sample sink to the bottom of the well without spilling into adjacent wells.

> [!failure] Stops here
> `==UNDONE: run voltage/current and duration, Coomassie staining time, destaining time and number
> of destain changes. Not in the photographed pages.==` One known as-run detail survives in the
> notebook: destaining is a **separate, next-day operation** — see
> [9-10](../../../lab_notebook/digitalized/2026-09-10_destain-sds-gel-revive-culture.md).

## Notes / common deviations
- **The BugBuster-to-culture ratio is contested across three sources.** This document says **15 mL
  culture : 1 mL** BugBuster (15 : 1), amended by hand to 2 mL (7.5 : 1). The
  [10-14](../../../lab_notebook/digitalized/2026-10-14_protein-extraction-bugbuster-scaling.md)
  entry instead quotes the protocol ratio as **50 mL : 2 mL (25 : 1)** and scales it to
  **2 mL : 100 µL (20 : 1)** for small cultures. All three are recorded; none is canonical.
  `==CONFIRM: which document the 10-14 "25:1" refers to — it does not match this page.==`
- **The induction window was abandoned in practice.** The printed protocol gates induction on
  OD600 = 0.4–0.6; the handwritten amendment replaces it with a fixed 4-hour wait, and the 9/27
  entry records OD600 values of 1.27–1.75 in the morning and 1.8–1.9 at 4 h — far past mid-log.
  Induction at high density is a plausible contributor to the low yields seen on every gel.
- **Total protein saturated the reader on the first attempt.** On 9/27 four of six lysates read
  exactly **3.000** at 562 nm (the instrument ceiling) and had to be re-read at 1:10 and 1:20 the
  next day. Dilute before reading, or use [[bradford_protein_assay]] with its standard curve.
- **The ± IPTG split (step 6) is the control that was actually run**, and it is a matched one. The
  9/28 BCA readings show that in **10 of 12 pairs the non-induced arm carries more total protein**
  than the induced arm — the expected cost of induction, and a reason to normalise before
  comparing gel lanes.

## Checklist — where do the outputs go?
- [ ] Overnight passage culture → **37 °C shaking incubator**, then 4 °C if not passaged same day
- [ ] Induced + non-induced flasks → **37 °C, 220 rpm, overnight**
- [ ] Soluble protein fraction (§3 step 6) → **4 °C**, use same day for gel / purification
- [ ] Cell pellet (§3 step 7) → **4 °C**, retained for [[dot_blot_his_tag]]
- [ ] Stained gel → photograph and archive under `data/assays/`

## Source
- Printed bench document, photographed 2026-10-20:
  [IMG_6614](../../printed_2026-10-20/IMG_6614.JPG),
  [IMG_6615](../../printed_2026-10-20/IMG_6615.JPG);
  [IMG_6616](../../printed_2026-10-20/IMG_6616.JPG) is unreadable.
- As-run records: [9-17](../../../lab_notebook/digitalized/2026-09-17_daily-passing.md),
  [9-27](../../../lab_notebook/digitalized/2026-09-27_protein-extraction-gel.md),
  [9-28](../../../lab_notebook/digitalized/2026-09-28_protein-dilution-bca-quantification.md),
  [10-14](../../../lab_notebook/digitalized/2026-10-14_protein-extraction-bugbuster-scaling.md).

---
## Log
- 2026-10-20 — Initial transcription from two photographs of the printed working copy. Handwritten
  amendments were read at 2× magnification on crops of the originals and are reproduced separately
  from the printed text throughout. Section 4 is **incomplete** — the photo set ends mid-step and
  the only candidate photograph of the next sheet is unrecoverable motion blur. Three mutually
  inconsistent IPTG recipes and three mutually inconsistent BugBuster ratios are preserved
  side-by-side per the repo's preserve-all-versions rule.
