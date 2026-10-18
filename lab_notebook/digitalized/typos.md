# Lab notebook — corrections to apply

Handwritten errors and unclear items identified during digitization. Tick off each box once the physical notebook has been corrected.

## Typos to fix

- [ ] **p.16** — "we found **note** of the extract …" → should read "we found **none** of the extract …"
- [ ] **p.18** — `t26` is correctly the 26-hour timepoint; the inline annotation "(16 hours)" appears to be a slip — confirm/fix.
- [ ] **p.19** — "Use loop to collect each sample (**10 mL**)" → should read "**10 µL**" (loop volume).
- [ ] **p.20** — "We striked each bacteria sample on the **8 uL** agar plates" → should read "**8 mL agar plates**" (volume per plate).
- [ ] **p.24** — "We mixed 5 mL LB agar with **500 mL** of each bacteria sample" → should read "**500 µL**".
- [ ] **p.24** — "2 plates with **2750 mL** mixture" → should read "**2750 µL**".
- [ ] **p.27** — Material list ① ends with "(**sale**) agar [with hand]" → should read "(**scale**) agar [with hand]" (i.e. agar weighed by hand on a scale).
- [ ] **p.27** — PI shorthand "**cp 8 / cp 9 / cp 10**" is actually the Greek letter **ϕ (phi)** for phage → consider rewriting as "ϕ 8 / ϕ 9 / ϕ 10" for clarity.
- [ ] **p.27** — Right-margin temperature near step 4 reads "9 °C" but should be "**4 °C**".

## Items pending clarification

### 2026-06-08 (p.32–36) — open
- [x] **p.34/p.35** — the four **unconcentrated** Qubit RFU readings (sites #1, #6, #8, #9) → confirmed **119.87 / 195.94 / 3600.46 / 1139.16** (user). The p.35-top "360 / 1129" was a garbled partial of #8/#9. Before/after table in `code/0608_quantification.ipynb` now complete.
- [ ] **p.36** — new 4-point standard curve: blurry digits — **S0** ("15 6326" → 156.326? started notebook read 156.26), **S1** (173.90 vs started-notebook 173.70). Confirm.
- [ ] **p.36** — 4th standard subscript reads like **"S₅₀"** and value like **"7224.52"**, but resolved with the team to **Std 30 = 724.52** on linearity grounds (a conc-50 point would be ~10× off the line). Confirm label + value against the bench record.
- [ ] **p.36** — concentrated samples: **C1** last digit ("151.6x"), **C8** ("5655.31" vs "5455.31"), **C9** last digits (".36" vs ".86"). Confirm.
- [ ] **p.36** — right-margin concentration-factor calc (≈250 ng/µL, ×30, ≈180 ng/µL, "16k ng/µL → 30 µL") needs exact transcription; confirm the concentrated-eluate final volume.
- [ ] **p.32/p.33** — day objective/procedure sub-steps and the bead-beater / standard-curve sketches are partly illegible; LB-broth volume is `[TBD]`. (Phage soil-enrichment resolved: sites **#3, 5, 6, 8, 9, 10**, 6 flasks — user, 2026-06-09.)
- [x] **Sequencing submission (6-8) — bacterial dilution** → confirmed **NOT diluted** (user); submitted at 6-5 extraction concentration. Only metagenomes were diluted (38 µL + 50 µL kit buffer). Still `[ ]` open: the exact **bacterial submitted volume** (taken as ≈ 90 µL from the 6-5 margin; confirm if less than the full eluate).
- [x] **p.32 (kit page `0608/IMG_4411.png`)** — metagenomic input mass → confirmed **0.12 g/tube** (user; lab scale has no mg mode). Still `[ ]` open: the **"mix 4 tubes into 1" pooling ratio** ("1-1, 1, 1×1").
- Note (not a physical-notebook typo): the user's started `code/0608_quantification.ipynb` had `C1 = 316.95` — that is the Std-10 RFU, not C1; corrected to the p.36 value during digitization.

### 2026-06-09 (p.37–38) — open
- [ ] **p.37** — entry **authors** not legible; confirm.
- [ ] **p.37** — objective/goal wording partly illegible (incl. the name of whoever banked the bacteria).
- [ ] **p.37** — bacteria-culture **label scheme** ("00/0 / plate number (D in E, C)") and **total tube count** (~30 = "next 27" + 3) unclear; confirm.
- [x] **p.37/p.38** — phage-isolation **enrichment site list** → confirmed **#3, 5, 6, 8, 9, 10** (user; the 6-8 batch, same as 6-1). The p.37 "#3,6,8,9" / p.38 "#3,5,7,8,9,10" reads were both garbled. 6 enrichments × 4 tubes = 24 tubes.
- [ ] **p.37** — phage-isolation **centrifuge speed** reads "5×g" — a misread of a higher rpm/×g ("higher than last time, cleaner supernatant"). Confirm the value.
- [ ] **p.38** — phage **filtrate volume** per enrichment (~2–3 mL?) unclear; confirm.

### 2026-06-10 (p.39–41) — open
- [ ] **p.39** — phage-buffer volume into the two **1.5 mL** Eppendorfs reads **"2 mL"** (impossible in a 1.5 mL tube) — likely **1 mL**; confirm.
- [ ] **p.40** — observation "pellets **loose** after PBS added" — confirm wording (loose vs larger).
- [x] **p.40** — extraction list = the **10 revived stocks**; **8 extracted** (9-1-1, 6-8-1, 9-10-1, 6-2-1, 8-10-2, 9-9-2, 6-8-2, 6-10-2), **2 pellets** banked (8-1-2, 9-1-2). The kit's **last 8 spin columns were all used** on the 8 extractions (none remain); the 2 pellets wait for new columns (user). Verified against the 6-08 revival panel.
- [ ] **p.40** — margin note "**update the Zymo protocol**" (store eluted DNA at **4 °C**, not −20 °C) — action item for the protocol, confirm intent.
- [x] **Hosts (continuity, user-confirmed):** *both* this week's plaque assays — 6/10 ϕ3/5/6 and 6/11 ϕ8/9/10 — ran on the **10 newly revived hosts** (same panel as the pellet prep/extraction), *not* old hosts. The only old-host element is the 06/05 source plates picked on 6/10 (⑤, a purification pick).
- [x] **Two successful 06/05 plates (user-confirmed 2026-06-13):** = **`9-6-2` Φ8** + **`9-2-1` Φ8** (the only week-1 phage hits). Named in the 6/10 ⑤; picks stored at 4 °C (see `data/dna_extraction_inventory.md`, `data/week_3_bacteria_list.md`).
- [ ] **`8-3-1` ≈ `8-5-1` (6/5 bacterial extract):** `8-3-1` is not one of the 28 glycerol stocks; `8-5-1` is (and was a 6/3 plaque host). Almost certainly `8-5-1` mislabelled — label kept per user; **verify + relabel the physical tube**.
- [ ] **p.42 phage source (continuity):** the 6/11 ϕ8/9/10 screen's phage source is unstated — fresh 06/09 ϕ8/9/10 filtrate (parsimonious) vs the 06/10 eluate picked from the 06/05 plates. Do not assume the 06/10 pick fed it (`==CONFIRM==` in the entries).

### 2026-06-11 (p.42) — open
- [ ] **p.42** — entry **authors** not legible; confirm.
- [ ] **p.42** — host isolate count reads **"10 out of >8"** (garbled) — confirm (10 isolates, picked by Rafael).

### 2026-06-12 (p.43) — open
- [ ] **p.43** — largely legible; confirm the picked-plaque labels `6-8-1 Φ3` and `8-1-2 Φ6` against the physical plates.

### Resolved earlier (2026-06-04)
- [x] **p.27** — Left-margin annotation is an illustration of the plate-labelling convention: row 1 = date (e.g. `26/6/4`), row 2 = phage ID (`ϕ<n>`, where `n` = the soil enrichment the phage filtrate came from), row 3 = bacteria label (e.g. `8-8-2`).
- [x] **p.19** — Right-margin OD data lives in `data/assays/0529_OD.xlsx` and has been transcribed into the 2026-05-29 entry.
- [x] **p.10** — Six enrichment samples are **#2, #5, #6, #8, #9, #10** (of the 10 total sites collected on 2026-05-19).

### Carried over from elsewhere (added 2026-08-29, updated after digitizing p.44–p.81)

- [x] **Sequencing submission concentration** → **corroborated by p.53 (2026-06-22)**, which reads
  *"20 µL for sequencing (~50 ng/µL)"*. Note the provenance: p.53 documents the **6-22** batch, so it
  shows 50 ng/µL is the team's submission practice; for the **6-08** batch itself the correction still
  rests on **Alex's 2026-08-08 statement + the MRA methods**, against the 6-08 entry's "NOT diluted". Still `[ ]` open:
  **`data/dna_extraction_inventory.md`** (Quantification appendix) still carries the superseded
  submitted-concentration figures 139.29 / 194.53 / 140.44 — corrected 2026-08-29, verify.
- [x] **`8-5-2` / `8-10-2` had no submission record** → **RESOLVED by p.53**: chosen on 2026-06-22
  from the 18-sample Qubit run, diluted 1:1 with water (70 µL + 70 µL) to ~50 ng/µL, 20 µL submitted;
  assemblies returned 6/26–6/27.
- [ ] **Phage `9-2-1 Φ8` submission date** — still unrecorded on any page (extraction is p.64–66,
  6/29; results back 2026-07-08).
- [ ] **Entry authors for 2026-06-09 (p.37) and 2026-06-11 (p.42)** — still `[TBD]`; add the same
  question for **p.55–p.59 (6/24)** and **p.60–p.61 (6/25)**, which carry no author line either.

### 2026-06-15 → 2026-07-16 (p.44–p.81) — open

Full review agenda: [`documents/2026-08-29_notebook_open_questions.md`](../../documents/2026-08-29_notebook_open_questions.md).

**Physical typos to fix**
- [ ] **p.62** — header written **`2025`-06-26**; the year should be **2026**.
- [ ] **p.69** — host list for the first host-range test has **`8-3-2` written twice**, `8-7-1` struck
  through and `9-9-2` added in the margin; the 8 hosts actually plated are unclear.
- [ ] **p.76** — the EOP "NOs" list has **`8-5-1` twice** and three struck-through entries.

**Resolved 2026-08-29 (Alex)**
- [x] **`8-5-2` host range (p.71 vs p.72)** — not a conflict. The plates were **not clearly readable**,
  so the ambiguous strains were carried forward for **repeat testing by EOP** instead of being scored;
  that is why `8-5-2` sits in the 13-strain EOP panel from 7/6 onward. Host-range calls for those
  strains come from the EOP series (7/8 → 7/15), not from p.71/p.72.
- [x] **"Yes, X webbed" (p.71)** — `X` is the shorthand for ***not* webbed**.
- [x] **Ditto marks (p.71)** — a `〃` **carries the cell above it**.
- [x] **`8-10-2` dilution arithmetic (p.53)** — a **bench rough estimate**, not an error; recorded as
  written with a callout in the 6/22 entry and in `data/dna_extraction_inventory.md`.

**Values / labels to confirm**
- [ ] **p.53** — Std 100 reads like **10434.66**; `code/0622_quantification.ipynb` has **16434.66**
  (the value consistent with the curve). *(The loose figures **245.5 / 280** are resolved: the `8-5-2`
  dilution — 245.51 ng/µL, 70 µL + 280 µL water = 5× → 49.1.)*
- [ ] **p.65** — round-2 phage reading **3116.13** (page) vs **3116.15** (notebook).
- [ ] **p.45 / p.37** — centrifuge **"5.0 ×g"**: the same notation on both pages, so it is the team's
  shorthand for the machine setting rather than a misread. Confirm the real units.
- [ ] **p.44** — header day-digit (`2026.6.15`, could read 6.16).
- [ ] **p.56** — the four `9-9-2` overnight readings (0.837 / 0.546 / 0.397 / 0.740).
- [ ] **p.61** — header ratio annotation "bac 3 : Φ 1".
- [ ] **p.67** — the **24 streaked strains** are not listed on the page.
- [ ] **p.69** — the dilution/volume row (8 dilutions, 7 volumes; "3.3 µL").
- [ ] **p.72** — circled `Φ` marks, the `?` on `9-2-2` / `9-10-1`, and "#9 stronger than #8"
  (soil sites or phages?).
- [ ] **p.78** — titres "1:20 W / 1:30 W / 1:40 W" (W = thousand?).

**Gaps in the record itself**
- [ ] **p.46 (6/17)** — "quantification for 8 bacteria samples" is listed as a goal but no data
  appears; next Qubit page is p.53 (6/22). Skipped, or rolled into 6/22?
- [ ] **p.62 (6/26)** — the **Procedure section is blank**.
- [ ] **p.77 (7/9)** — every sample read **above the 30 ng/µL top standard**; the
  **dilute-and-re-read is UNDONE**.
- [ ] **p.80 / p.81 (7/15, 7/16)** — the EOP plates and the site-6 soft lawns have **no recorded
  readout**; the notebook stops at p.81.
- [x] **p.82+** — resolved 2026-10-18: bench work **did** continue. p.82–p.100 (2026-09-01 → 2026-09-27) plus a second notebook (p.06–p.08, 9/28 → 10/14) are now digitized; see the block below.
- [ ] **Quantification page (9/4)** — the `e1` reading is written `339.8` with the last digit
  overwritten; read as **339.87** in [`code/0904_quantification.ipynb`](../../code/0904_quantification.ipynb)
  (immaterial: <0.001 ng/µL either way). Same page: **`5 µL` load applies to the standards as well
  as the samples** (Alex, 2026-09-04) — resolved, so no volume correction. Volume budget also
  resolved: ~45 µL per tube at the read, 5 µL per sample to the transformation, ~40 µL left.
  **Still open: what are `e1` / `e40` / `e281`?**

### 2026-09-01 → 2026-10-14 (p.82–p.100, notebook 2 p.06–p.08) — open

The protein-expression block. Digitized 2026-10-18.

**Physical typos to fix**
- [ ] **p.95** — step 1 lists the constructs as "`e1`, `e40`, **`e81`**, `CDS11`, `CDS12`" → should read
  **`e281`**.
- [ ] **p.82** — the margin question "kanamycin will not denature if below **220 °C**?" — likely a slip
  for a much lower temperature (the step itself says add at ~40 °C). Confirm what was meant.
- [ ] **nb2 p.08** — "100 µL of BugBuster instead of 2 mL (**more diluted** than the protocol)", but the
  arithmetic on the same line goes 25:1 → 20:1, i.e. **less** diluted. Confirm which was meant.

**Structural / page questions**
- [x] **A second notebook** — confirmed (Alex, 2026-10-18): notebook 1 ends at **p.100**, a second
  notebook is used from **2026-09-27** onward, and its **p.01–p.05 are reserved for a table of contents**
  to be written later. Hence the printed `06`/`07`/`08` on the 9/28, 10/01 and 10/14 pages.
- [x] **p.98 / p.101+** — nothing missing to photograph. **9/18–9/23 was a note-keeping lapse** while the
  team repeated protein-expression rounds (Alex, 2026-10-18).
- [x] **2026-09-29 and 2026-10-10 have no notebook page** — same cause. The `code/` gel analyses
  (`0915_`, `0929_`, `1010_gel_annotation.ipynb`) are to be read as the record for those days.
- [ ] **p.93 has no date and no authors** — filed as **2026-09-09** by position (between 9/8 and the 9/10
  entry, which refers to "the SDS gel from yesterday"). Confirm.
- [ ] **nb2 p.06 (9/28) has no author line.**

**Values / labels to confirm**
- [ ] **p.82** — LB agar "(1 %)"; earlier plates in this notebook were 1.5 %.
- [ ] **p.84** — "`CDS10 WT xAG`": what **xAG** denotes, and the Ⓚ shorthand used throughout.
- [ ] **p.85** — the **"Results (OD600)" heading is empty**; no values were recorded that day.
- [ ] **p.89** — colony labels `T2 / T4 / T5 / T8` and `e1 ⑥`; and whether the **cells-only control
  plates** were among the "~43" that grew (growth there would be a problem).
- [ ] **p.94** — the gel-lane table: lane 2 reads like "G1" (almost certainly `e1`), the X/V induction
  marks on lanes 4–5 and 9 are overwritten, and the dilution row may start at lane 5 rather than lane 6.
  Also "**100 mL +**" — 100 mL of what.
- [ ] **p.96** — induction was done at **OD ≈ 1.4–2.0**, while p.94 sets the rule "**till 0.8 for OD to
  add IPTG**". Was that deliberate?
- [ ] **p.99** — stocks labelled **DH5α**, while p.82 records the streaked host as "DH10-B like" and p.88
  transforms into **BL21**. Which host is which.
- [ ] **p.99** — `e1` quantification reads **173.57** against an S0 blank of **161.14**, i.e. effectively
  no plasmid; was that miniprep repeated?
- [ ] **p.100** — the "OD600 at 4 hrs" block has one struck label and a ⊕ value (**1.938**) with no
  construct in line with it; `e40` has no ⊕ value.
- [ ] **nb2 p.06** — was a **BCA standard series** run? Without standards the OD562 values cannot be
  converted to mg/mL. Also `CDS11` 1:20 non-induced = **0.394**, the only pair that breaks the
  half-of-1:10 pattern.
- [ ] **nb2 p.07** — the protocol note says "**8 samples**" but the loading plan has 10 sample lanes;
  and whether the 1:1 / 1:2 lanes are the crude load or the flow-through.
- [ ] **nb2 p.08** — which constructs were extracted on 10/14 (not written).


## Log
- 2026-06-04 — Initial cataloging during digitization of `pre_0604.pdf` + `0604/` photos.
- 2026-06-04 — All three pending-clarification items resolved (p.27 margin illustration described; p.19 OD data added from `data/assays/0529_OD.xlsx`; p.10 enrichment samples confirmed as #2/5/6/8/9/10).
- 2026-06-08 — Added p.32–36 pending-clarification block during digitization of the 0608 session (unconcentrated readings, p.36 blurry standards/samples, S30-vs-S50 resolution, concentration-factor calc, p.32/33 objective + kit-page annotations).
- 2026-06-08 — Resolved (user): unconcentrated readings (119.87/195.94/3600.46/1139.16), input mass (0.12 g/tube), bacterial sequencing dilution (not diluted). Remaining open: pooling ratio, blurry p.36 digits, concentration-factor calc, bacterial submitted volume.
- 2026-06-09 — Added p.37–38 pending-clarification block during digitization of the 0609 session (authors, objective wording, label scheme + tube count, enrichment site list discrepancy, centrifuge speed, filtrate volume).
- 2026-06-12 — Added p.39–43 pending-clarification blocks during digitization of the 0610 / 0611 / 0612 sessions (phage-buffer "2 mL"→likely 1 mL; "pellets loose" wording; Zymo 4 °C protocol-update note; 0611 authors + "10 out of >8" isolate count; 0612 picked-plaque labels). Resolved: 0610 extraction list = 8 extracted + 2 pellets from the 10 revived stocks (user). Noted the 6/11 phage source as inferred (`==CONFIRM==` in entries).
- 2026-06-12 — **User corrections:** (1) spin columns were all *used up* by the 8 extractions (not "8 left over"); (2) *both* this week's plaque assays ran on the 10 newly revived hosts (not old hosts) — updated the 0610 resolved item + replaced the "two-thread" continuity note with the corrected host/phage framing.
- 2026-06-13 — **User physical re-check (inventory restructure):** named the 2 week-1 phage hits (`9-6-2 Φ8` + `9-2-1 Φ8`); flagged `8-3-1` ≈ `8-5-1` (not in the 28-stock list — verify/relabel tube). Both folded into `data/dna_extraction_inventory.md` (now storage-based) + new `data/week_3_bacteria_list.md`.
- 2026-08-29 — **Coverage audit** (see [`README.md`](README.md) "Coverage & gaps"): digitization stops at p.43 / 2026-06-12; 8 later bench sessions have no entry. Added the four carried-over open items above (50 ng/µL propagation into `data/dna_extraction_inventory.md`, the unrecorded 8-5-2/8-10-2 submission, the phage submission date, the two `[TBD]` author fields). All 9 physical-notebook typos are still unticked — they need the notebook in hand.
- 2026-08-29 — **p.44–p.81 digitized** (26 entries, 2026-06-15 → 2026-07-16). Two carried-over items
  resolved by p.53 (the 50 ng/µL normalisation and the `8-5-2`/`8-10-2` submission). New blocking
  item: the **p.71 vs p.72 `8-5-2` host-range conflict**, which touches a prediction in the synthesis
  documents — left unreconciled by design. Full agenda in
  `documents/2026-08-29_notebook_open_questions.md`.
- 2026-08-29 — **Alex answered the p.71/p.72 questions:** `X` = not webbed; `〃` carries the cell above;
  the plates were unclear so those strains went to EOP for repeat testing — no reconciliation needed.
  The p.53 `~50 ng/µL` figures are bench rough estimates. Per Alex, digitization records everything as
  written; only genuine handwriting typos get flagged here.
- 2026-09-04 — Added the 9/4 quantification-page items (the `e1` overwritten digit, the 5 µL vs
  10 µL standard-load question, and the unidentified `e1`/`e40`/`e281` sample names) while writing
  `code/0904_quantification.ipynb`. That page is not yet digitized — digitization still stops at p.81.
- 2026-09-04 — **Alex confirmed the standards were also loaded at 5 µL**, so the 9/4 load-volume
  question is closed and `code/0904_quantification.ipynb` applies no volume correction
  (`VOL_CORRECTION = 1`).
- 2026-09-04 — Alex supplied the volume budget (45 µL per tube at the read, 5 µL per sample drawn
  for the transformation, 40 µL left) and confirmed the LOWEND (S0/S1/S3) fit as the one to quote.
  `code/0904_quantification.ipynb` Section 3 now reports DNA mass at all three stages; ≈356 ng left
  across the five tubes.
- 2026-10-18 — Added the p.82–p.100 / notebook 2 p.06–p.08 block during digitization of the
  `0901-1014` photo set (protein-expression block, 9/1 → 10/14).
- 2026-10-18 — Alex resolved the structural questions: second notebook from 9/27 (p.01–05 = TOC),
  notebook 1 ends at p.100, and the 9/18–9/23 / 9/29 / 10/10 gaps are a note-keeping lapse covered by
  the `code/*_gel_annotation.ipynb` analyses.
