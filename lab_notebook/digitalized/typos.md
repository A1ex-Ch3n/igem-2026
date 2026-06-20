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
- [x] **p.19** — Right-margin OD data lives in `data/0529_OD.xlsx` and has been transcribed into the 2026-05-29 entry.
- [x] **p.10** — Six enrichment samples are **#2, #5, #6, #8, #9, #10** (of the 10 total sites collected on 2026-05-19).

## Log
- 2026-06-04 — Initial cataloging during digitization of `pre_0604.pdf` + `0604/` photos.
- 2026-06-04 — All three pending-clarification items resolved (p.27 margin illustration described; p.19 OD data added from `data/0529_OD.xlsx`; p.10 enrichment samples confirmed as #2/5/6/8/9/10).
- 2026-06-08 — Added p.32–36 pending-clarification block during digitization of the 0608 session (unconcentrated readings, p.36 blurry standards/samples, S30-vs-S50 resolution, concentration-factor calc, p.32/33 objective + kit-page annotations).
- 2026-06-08 — Resolved (user): unconcentrated readings (119.87/195.94/3600.46/1139.16), input mass (0.12 g/tube), bacterial sequencing dilution (not diluted). Remaining open: pooling ratio, blurry p.36 digits, concentration-factor calc, bacterial submitted volume.
- 2026-06-09 — Added p.37–38 pending-clarification block during digitization of the 0609 session (authors, objective wording, label scheme + tube count, enrichment site list discrepancy, centrifuge speed, filtrate volume).
- 2026-06-12 — Added p.39–43 pending-clarification blocks during digitization of the 0610 / 0611 / 0612 sessions (phage-buffer "2 mL"→likely 1 mL; "pellets loose" wording; Zymo 4 °C protocol-update note; 0611 authors + "10 out of >8" isolate count; 0612 picked-plaque labels). Resolved: 0610 extraction list = 8 extracted + 2 pellets from the 10 revived stocks (user). Noted the 6/11 phage source as inferred (`==CONFIRM==` in entries).
- 2026-06-12 — **User corrections:** (1) spin columns were all *used up* by the 8 extractions (not "8 left over"); (2) *both* this week's plaque assays ran on the 10 newly revived hosts (not old hosts) — updated the 0610 resolved item + replaced the "two-thread" continuity note with the corrected host/phage framing.
- 2026-06-13 — **User physical re-check (inventory restructure):** named the 2 week-1 phage hits (`9-6-2 Φ8` + `9-2-1 Φ8`); flagged `8-3-1` ≈ `8-5-1` (not in the 28-stock list — verify/relabel tube). Both folded into `data/dna_extraction_inventory.md` (now storage-based) + new `data/week_3_bacteria_list.md`.
