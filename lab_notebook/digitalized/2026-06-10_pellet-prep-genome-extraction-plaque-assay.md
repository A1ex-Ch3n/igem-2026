---
date: 2026-06-10
notebook_pages:
  - p39
  - p40
  - p41
authors:
  - Alex
  - Olivia
  - Carol
title: Bacteria Pellet Prep; Bacteria Genome Extraction (8 of 10); Plaque Assay (Φ3/5/6); Phage Picked from 06-05 Plates
---

# Bacteria Pellet Prep; Genome Extraction; Plaque Assay; Phage Picking

**Source pages:** ![p39](images/p39.png) ![p40](images/p40.png) ![p41](images/p41.png)

> [!note] Photo legibility
> p39–p41 are rotated ~90° and moderate-resolution. The structure and most values are clear; a few numbers are flagged `[TBD]` inline / in `typos.md`.

## Objective (p39)
1. **Prepare bacteria pellets** from the bacteria grown in LB on [2026-06-09](2026-06-09_bacteria-culture-phage-isolation.md).
2. **Extract bacterial genome DNA** from the pellets.
3. ~~Bacteria genome extract quantification~~ *(crossed out on p39 — quantification deferred; see Experiment note.)*
4. **Bacteria culture** for the [2026-06-11](2026-06-11_bacteria-culture-plaque-assay.md) work.
5. **Phage plaque assay.**
6. **Inoculate / pick phage** from the 06/05 plates.

## Procedure (p39–p41)

### ① Bacteria pellet preparation — see [[bacteria_pellet_for_sequencing]]
Refer to the [2026-06-03](2026-06-03_phage-plaque-assay.md) procedure (Procedure ③). Pellets prepared from the overnight LB cultures set up on [2026-06-09](2026-06-09_bacteria-culture-phage-isolation.md).

### ② Bacteria genome extraction — see [[bacteria_genome_extraction]]
Refer to the [2026-06-05](2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) procedure (Quick-DNA Miniprep Kit, Zymo).

**Bacteria list for extraction (10; p40 "Experiment note"):**

| # | Sample | Fate |
|---|---|---|
| 1 | 9-1-1 | extract |
| 2 | 6-8-1 | extract |
| 3 | 9-10-1 | extract |
| 4 | 6-2-1 | extract |
| 5 | 8-10-2 | extract |
| 6 | 9-9-2 | extract |
| 7 | 6-8-2 | extract |
| 8 | 6-10-2 | extract |
| 9 | 8-1-2 | **store as pellet** |
| 10 | 9-1-2 | **store as pellet** |

> These 10 are exactly the **10 revived stocks** cultured on [2026-06-09](2026-06-09_bacteria-culture-phage-isolation.md) (from the [2026-06-08](2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) ① revival panel — the likely *P. aeruginosa* candidates).

- **Only 8 were extracted.** The kit's **last 8 spin columns were all used on these 8 extractions — none remain afterwards.** The 2 leftover samples (9: `8-1-2`, 10: `9-1-2`) were **stored as pellets at −20 °C**, to be extracted once more spin columns are obtained.
- **Extracted DNA storage:** proceed to extract, then **store at 4 °C** *(p40 corrects an initial "−20 °C" → "4 °C")*. Margin note: **"update the Zymo protocol"** to reflect 4 °C storage of eluted DNA.
- **Quantification deferred:** *"wait until next week for quantification for all 8."* No Qubit values recorded today.
- Observation: **pellets were loose after PBS was added** `[TBD: p40 reads "pellets loose after PBS added ✓"]`.

### ③ Bacteria culture (for 06/11) — see [[single_colony_inoculation]]
Same steps as on [2026-06-09](2026-06-09_bacteria-culture-phage-isolation.md) (p37), but this round **added 5 mL LB broth + 50 µL bacteria culture from 06/09** per tube (sub-culture, not a fresh colony pick). Stored in the incubator.

### ④ Phage plaque assay (Φ3/5/6) — see [[plaque_assay_layered_plate]]
**Plaque assay for the 10 (new) bacteria cultures and phage Φ3, Φ5, Φ6.** Followed the [2026-06-05](2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) procedure (p.29, layered-plate method). Stored the soft plates in the incubator and returned the phage filtrate to the fridge.

> *Phage = the **ϕ3/5/6 filtrate** isolated on [2026-06-09](2026-06-09_bacteria-culture-phage-isolation.md) (from [[soil_enrichment_phage]] sites); hosts = the **10 newly revived candidates** (the same 10 in the extraction list above). This is the first half of the week's six-phage screen; ϕ8/9/10 run [2026-06-11](2026-06-11_bacteria-culture-plaque-assay.md).*

### ⑤ Pick phage from the 06/05 plates — see [[phage_purification]]
1. **Took out the two successful plates made on 06/05** (the Φ8/9/10 plaque assay, [2026-06-05](2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) ②) — these were **host `9-6-2` / Φ8** and **host `9-2-1` / Φ8** (the only 2 plates that grew phage that week; user-confirmed 2026-06-13); **found the plaques and marked them on the back** of each plate.
2. **Put out two 1.5 mL Eppendorf tubes and added phage buffer to each** `[TBD: p39 reads "2 mL" buffer into a 1.5 mL tube — likely 1 mL; confirm]`.
3. (p41) **Used a 20 mL-pipette tip, inserted vertically into the soft agar where the plaque was marked** (as vertical as possible), to core out the plaque plug.
4. **Pipetted the gel plug into the phage buffer and vortexed thoroughly** to elute the phage.

> *Both successful 06/05 plaques were **Φ8** (on hosts `9-6-2` and `9-2-1`), picked from the **old plates** — the 06/05 assay used the earlier 06/03-banked host panel — and eluted into buffer as a **purification-style pick** of confirmed hits (→ [[phage_purification]]). The 2 phage picks are stored at 4 °C (see [[dna_extraction_inventory]]). This is distinct from today's ④ plaque assay (which is on the new hosts).*

## Notes / continuity — this week's phage work
This week the team screened the **six phage isolates (ϕ3, 5, 6, 8, 9, 10)** — isolated on [2026-06-09](2026-06-09_bacteria-culture-phage-isolation.md) — against the **10 newly revived host candidates** (the *same* 10 used for pellet prep + extraction above; user-confirmed), split across two days:

- **ϕ3/5/6 → 6/10 (④):** plaques appeared on **6-8-1 (Φ3)** and **8-1-2 (Φ6)** → picked and re-assayed on [2026-06-12](2026-06-12_plaque-assay-extracted-phage.md). *(Live lead.)*
- **ϕ8/9/10 → [2026-06-11](2026-06-11_bacteria-culture-plaque-assay.md):** **none grew** (reported [2026-06-12](2026-06-12_plaque-assay-extracted-phage.md)).

Separately, in **⑤** the team picked the **two successful 06/05 plates** — **`9-6-2` Φ8** and **`9-2-1` Φ8** (the week-1 phage hits; which used the *old* 06/03-banked hosts) — into buffer as a purification-style pick of confirmed hits (now at 4 °C; see [[week_3_bacteria_list]]). `==CONFIRM: whether this 06/10 eluate is the phage used in the 06/11 ϕ8/9/10 screen, or whether that screen used the fresh 06/09 ϕ8/9/10 filtrate — not stated on p39–42.==`

## Checklist — where do the outputs go?
- [ ] **8 bacterial genome DNA eluates** (9-1-1, 6-8-1, 9-10-1, 6-2-1, 8-10-2, 9-9-2, 6-8-2, 6-10-2) → **4 °C**, quantification next week.
- [ ] **2 spare pellets** (8-1-2, 9-1-2) → **−20 °C**, for a later extraction round.
- [ ] **Φ3/5/6 soft plates** → **incubator**; phage filtrate → **4 °C fridge**.
- [ ] **Eluted Φ8 plaque picks** — `9-6-2` Φ8 + `9-2-1` Φ8 (2 Eppendorfs) → **4 °C fridge**.

## Source
- Lab notebook: p.39–41 (this entry).

---
## Log
- 2026-06-10 — Initial digitization from `lab_notebook/0610/IMG_4505.png`→`p39.png`, `IMG_4506.png`→`p40.png`, `IMG_4507.png`→`p41.png`. Bacteria pellet prep (from 6-09 cultures) + genome extraction (**8 of 10** extracted; the kit's last 8 spin columns all used, none remain; 2 pellets `8-1-2`/`9-1-2` banked at −20 °C for a later round; eluates → 4 °C; quant deferred) + bacteria culture for 6-11 (5 mL LB + 50 µL 6-09 culture) + plaque assay ϕ3/5/6 on the 10 revived hosts + plaque picking from the 06/05 ϕ8/9/10 plates. Extraction list verified = the 10 revived stocks.
- 2026-06-12 — **User corrections applied:** (1) spin columns were not "left over" — the kit's last 8 were *all used* on the 8 extractions (none remain), 2 samples banked as pellets until more columns are obtained; (2) **both** this week's plaque assays (6/10 ϕ3/5/6 and 6/11 ϕ8/9/10) ran on the **10 newly revived hosts** (same panel as pellet prep/extraction), not old hosts — reframed the "two-thread" Notes accordingly (the only old-host element is the 06/05 source plates picked in ⑤). **Open `[TBD]`s:** phage-buffer volume into the 1.5 mL tubes ("2 mL" likely 1 mL); "pellets loose after PBS" wording. `==CONFIRM==` retained on the 06/11 ϕ8/9/10 phage source (fresh 06/09 filtrate vs the 06/10 pick).
- 2026-06-13 — **User-confirmed:** the "two successful 06/05 plates" picked in ⑤ are **`9-6-2` Φ8** and **`9-2-1` Φ8** (the only 2 plates that grew phage in week 1); both phage picks now stored at 4 °C. Named them in ⑤ + Notes + Checklist. Recorded in the new [[dna_extraction_inventory]] (4 °C table) and [[week_3_bacteria_list]].
