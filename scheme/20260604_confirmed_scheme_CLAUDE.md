Written by Alex & Claude. 
Reviewed by Carol. 

This document serves as a confirmation of the existing schemes and labs we have done so far since the start of May, 2026. 

The ongoing goals include a few:
- Plaque assay
- DNA sequencing (metagenomics, bacteria, phage) 

On May 19th, we collected 10 soil samples from different locations in California Botanic Garden. 

After that, we start to prepare for sequencing and plaque assay in parallel. 

DNA sequencing's preparations is done along different stages in the lab. 
- For metagenomics sequencing, it has a unique procedure to collect DNA and wash them from the original sample in enrichment. 
- For bacteria sequencing, it consists of isolating pseudomonas and growing them overnight to prepare bacteria pellets for sequencing. 
- For phage sequencing, it comes last. Once we finish some batch of plaque essay, we will also inoculate phage and process them to be sequenced. ==NEED CONFIRMATION==

Plaque assay is the way we identify phage that has the potential to lyse bacteria. 
- Prepare and grow bacteria, including to ensure that the bacteria we used later are pseudomonas bacteria. After successful isolation, we prepare the soft plate from these bacteria in log phase for the plaque assay. 
- We enrich the samples again and filter them to get phages. We have 6 phages in total from sample sites 3, 5, 6, 8, 9, 10. 
- After we have the phage, we conduct the plaque assay, and isolate the phage again. We repeat this process for three times, and each time we use the isolated phage to confirm that it's one phage that is lysing the bacteria. 
- After all these, we complete this part by sequencing the phage to identify and study the phage. 

---
## DNA Sequencing

### Metagenomics DNA Sequencing

**Purpose.** Extract whole-community DNA directly from each soil site — independent of any bacterial isolation — to enable shotgun metagenomic profiling of the soil microbiome at each location we sampled.

- **[2026-05-20](../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md)** — First-trial metagenomic extraction covering **all 10 soil sites** (#1–#10). DNA filtrates stored at 4 °C, labelled Metagenomic Sample 1–10. *(The bacteria-track soil enrichment started the same day used the 6-site subset #2, #5, #6, #8, #9, #10 — a different operation; see Bacteria DNA Sequencing section.)*
- **[2026-05-27](../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md)** — Qubit DNA quantification at 470 nm. **Failed for samples #1–9** (none showed observable concentration); only **sample #10** read above the detection floor. **Conclusion: redo all samples.**
- **[2026-05-28](../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md)** — Second-batch metagenomic extraction — re-extraction of selected sites **#1, #3, #4, #7** (per labelled rack `26/05/28 — second trial of soil DNA purification`, photo `photos/0605/`). These 4 were re-pulled from the original 10-site collection to retry after the 5-27 quant failures.
- **[2026-06-05](../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md)** — Qubit re-quant of the 2nd-batch (#1, #3, #4, #7) extracts on the **Portelite Broad Dynamic Range** kit (AAT Bioquest cat. 17665, Helixyte Green BR) run in raw-RFU mode on Qubit 4. Six-point standard curve `0 / 1 / 3 / 10 / 30 / 100 ng/µL` fit by linear regression (slope 165.64, intercept 33.43, R² 0.99993). Results: concentrations **still low** across all 4 samples (sample RFUs in the 190–430 range vs Std 1 RFU = 325.6). Tried recovering signal by mixing batch-1 + batch-2 paired samples (M1 / M3 / M4 / M7 mixes) — no improvement.
- **PI guidance + plan (2026-06-05):** PI's hypothesis is that 1 g of soil saturates the Quick-DNA silica column with co-extracted inhibitors that out-compete DNA binding. Plan: **4 more metagenomic extractions** with **smaller per-sample soil mass** (`[TBD: target mass — possibly ~12.5 mg vs the standard 1 g; ambiguous on p.30, confirm]`). PI also confirmed the standard curve can be **extrapolated a bit beyond the 100 ng/µL top point** when needed.
- **UNDONE** — Run the 4 smaller-biomass metagenomic extractions and Qubit re-quant.
- **UNDONE** — If yields are adequate across the combined sample set, submit for metagenomic library prep + sequencing.

### Bacteria DNA Sequencing

**Purpose.** Isolate single *Pseudomonas* colonies from the soil enrichments, grow them in liquid culture, and bank washed cell pellets ready for whole-genome sequencing. The selective media chain (PMM → PIA) enriches specifically for *Pseudomonas*.

**Pipeline overview.** The bacteria-isolation pipeline is a multi-stage selective filter that takes raw soil and ends with washed cell pellets ready for genome sequencing:

1. **Soil enrichment in PMM-based liquid broth** ([2026-05-20](../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md)) — selects for *Pseudomonas*-capable bacteria from the soil community by restricting carbon / nitrogen / phosphate sources to what *Pseudomonas* can metabolise on PMM.
2. **PMM agar plates poured** ([2026-05-21](../lab_notebook/digitalized/2026-05-21_pmm-agar-plates.md)) + **three-phase streak isolation on PMM plates** ([2026-05-22](../lab_notebook/digitalized/2026-05-22_streak-test-trial.md) trial, [2026-05-26](../lab_notebook/digitalized/2026-05-26_streak-soil-enrichment.md) real run) — physically separates the enriched mixed culture into isolated single colonies; each enrichment plated multiple times to give a population of single-cell-origin candidates.
3. **Re-streak on PIA (*Pseudomonas* Isolation Agar)** ([2026-05-27](../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md)) — second selective filter that produces visually distinctive colonies (pigment, morphology) confirming *Pseudomonas* identity before downstream commitment.
4. **Liquid culture in LB broth → OD₆₀₀ characterisation → glycerol-stock banking** ([2026-05-28](../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md) inoculation, [2026-05-29](../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) OD + stocks). Pure single-colony isolates are grown overnight; OD at 22–26 h selects log-phase candidates; the best (A₆₀₀ 0.6–1.0) bank to −80 °C glycerol stocks, with all tested cultures backed up at −20 °C.
5. **Scale-up culture → washed pellet** ([2026-06-01](../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) re-streak, [2026-06-02](../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md) re-inoculation, [2026-06-03](../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) pellet prep) — selected stocks are grown back up and harvested as PBS-washed cell pellets, stored at −20 °C.
6. **Genomic DNA extraction + Qubit quantification** ([2026-06-05](../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md)) — pellets processed through the Quick-DNA™ Miniprep Kit (Zymo Research); each extract quantified on the Portelite BDR kit / Qubit 4 in raw-RFU mode against the 6-point standard curve.
7. **UNDONE** — Submit extracted DNA for whole-genome sequencing.

After banking (step 4), the same isolates also feed the plaque-assay lawn (see [Plaque Assay → Growing Bacteria](#growing-bacteria)) — one pipeline serves two tracks.

**Chronological log:**

- **[2026-05-20](../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md)** — 6 soil enrichments started in PMM-based selective media using sites **#2, #5, #6, #8, #9, #10**. ==CONFIRM: bacteria track uses #2,5,6,8,9,10 while phage track (6-1) uses #3,5,6,8,9,10 — was the #3 vs #2 difference intentional?==
- **[2026-05-21](../lab_notebook/digitalized/2026-05-21_pmm-agar-plates.md)** — 40 PMM (Pseudomonas Minimum Media) agar plates prepared. PMM is selective: only bacteria able to grow on the minimal carbon/nitrogen + phosphate-buffered base will form colonies.
- **[2026-05-22](../lab_notebook/digitalized/2026-05-22_streak-test-trial.md)** — Streak-method practice + trial run on PMM plates using enrichments **#8** (Alex) and **#10** (Olivia). Purpose was to validate the streaking technique before committing all enrichments.
- **[2026-05-26](../lab_notebook/digitalized/2026-05-26_streak-soil-enrichment.md)** — 6 enrichments streaked on PMM plates using the three-phase streak method (60 plates total, 10 per sample) to isolate single colonies.
- **[2026-05-27](../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md)** — 500 mL of PIA (Pseudomonas Isolation Agar) prepared and poured. PIA further restricts growth to *Pseudomonas* species. 2 isolated colonies per PMM plate re-streaked onto PIA.
- **[2026-05-28](../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md)** — 16 single colonies picked from PIA plates into LB broth tubes for overnight liquid culture.
- **[2026-05-29](../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md)** — OD₆₀₀ readings at **t22** (22 h, diluted ×100) and **t26** (26 h, undiluted). Candidates flagged as **Most Likely *P. aeruginosa*** = **all stocks with raw A₆₀₀ > 0.6** (the merged annotation block in `data/assays/0529_OD.xlsx` covers multiple rows, not just `6-2-1`).
    - No 24-h continuous OD curve was done, so the log-phase absorbance is unknown.
    - **Best −80 °C glycerol-stock candidates: A₆₀₀ in the 0.6–1.0 band** (above that risks past log phase).
    - All ~20 tested cultures were also banked at **−20 °C** as backup.
- **[2026-06-01](../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md)** — 10 frozen bacteria stocks re-streaked onto LB agar plates for fresh growth.
- **[2026-06-02](../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md)** — 3 colonies/plate re-inoculated into LB broth for next-round culture (sequencing-prep liquid culture).
- **[2026-06-03](../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md)** — Bacteria pellets prepared for sequencing from 10 cultures: **`9-2-2, 10-9-2, 8-5-1, 8-3-2, 9-2-1, 6-3-2, 8-2-2, 10-10-2, 8-5-2, 9-6-2`**. Cells washed twice in PBS, then pelleted at 10,000 g for 10 min in 2 mL Eppendorfs and stored at **−20 °C** for sequencing (photo `photos/0605/` "6/3 bacteria pellet for sequencing").
- **[2026-06-05](../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md)** — **Bacteria genome extraction** from the 10 pellets banked 6-03 using the **Quick-DNA™ Miniprep Kit (Zymo Research)**; Qubit quantification on the Portelite BDR kit / Qubit 4 in raw-RFU mode against the same 6-point standard curve used for the metagenomic track. Per-sample RFU readings span **15.6k → 43.9k**; **several samples come in at or above the Std-5 (100 ng/µL) ceiling at 16.7k RFU**, so concentrations for the high-end samples are computed off the linear fit with PI-approved extrapolation. Volume remaining per tube after the Qubit aliquot: ~90 µL. Full per-sample RFU table in the 6-05 lab-notebook entry; computed concentrations in [`code/0605_quantification.ipynb`](../code/0605_quantification.ipynb).
- **UNDONE** — Submit bacteria DNA (or pellets, per sequencing-vendor preference) for whole-genome sequencing.

### Phage DNA Sequencing

**Purpose.** Sequence the phages we isolate from the plaque assay so we can identify them and study their host range / mechanism. This is the **last** track to begin — it depends on iterative re-isolation rounds confirming each plaque comes from a single phage. ==NEED CONFIRMATION==

- **UNDONE** — Phage amplification on confirmed-single-phage lysate (after re-isolation rounds 2 and 3 complete).
- **UNDONE** — Phage DNA extraction.
- **DONE** — Submit phage DNA for sequencing + assemble/annotate. `9-2-1 Φ8` sent (vendor code `3NKSC3`); results back **2026-07-08**, raw fastq in [`data/phage_genome/9-2-1/`](../data/phage_genome/9-2-1/). **Assembled + annotated 2026-07-08** ([`code/0708_phage_assembly/`](../code/0708_phage_assembly/)): the whole phage in **one complete 62,338 bp contig** (novel, likely circular but not yet confirmed) — temperate, safe (0 virulence / 0 AMR), carries RBPs; our own host removal found ~15% host vs the vendor's 1.9%. Write-up: [`data/phage_genome/9-2-1/assembly/NOTES.md`](../data/phage_genome/9-2-1/assembly/NOTES.md). Companion `9-6-2 Φ8` pick not yet sent. `[Note: this whole subsection predates a month of subsequent work (OD/growth tracking, RBP fold screening through 07-03) that isn't reflected here — updated in isolation because it directly matches the new data; the rest of this doc likely needs a fuller pass.]`

---
## Plaque Assay

### Growing Bacteria

**Purpose.** Produce a confirmed-*Pseudomonas* bacterial lawn in log phase, suitable for soft-agar overlay with phage filtrate. The isolation pipeline is the **same as the bacteria-sequencing track** above — the cultured stocks serve both purposes.

- Cross-reference the bacteria-sequencing entries from [2026-05-20](../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) through [2026-06-02](../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md) for the full PMM → PIA → LB isolation chain.
- **[2026-06-03](../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md)** — **First plaque-assay attempt failed/partial.** Intended 10 bacteria stocks for the soft-plate overlay, but the 0.7 % LB agar didn't fully solidify; coverage achieved on only 8 stocks: `6-3-2, 10-10-2, 10-9-2, 9-2-2, 8-3-2, 8-2-2, 9-2-1, 8-5-1`. **Lesson:** raise agar concentration to 0.8 % and make extra (2 × 50 mL).
- **[2026-06-04](../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md)** — Second plaque-assay prep returned to the **full 10-bacteria panel** (actively grown to log phase): `10-10-2, 6-3-2, 10-9-2, 9-2-2, 9-6-2, 8-5-2, 8-3-2, 8-2-2, 9-2-1, 8-5-1`. Used the layered-plate method (0.7 % LB + agar poured over a hard agar base).

### Assay with Filtrated Phage

**Purpose.** Detect phages in the soil enrichments by lysis of *Pseudomonas* lawns, then iteratively re-isolate each plaque to confirm single-phage origin before phage sequencing.

- **[2026-06-01](../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md)** — Phage enrichment started in 6 flasks using soil sites **#3, #5, #6, #8, #9, #10** (1 g soil + 25 mL LB broth each). `==CONFIRM: phage track uses #3,5,6,8,9,10 while bacteria track (5-20) uses #2,5,6,8,9,10 — was the #3 vs #2 difference intentional?==` LB agar (8 mL plates) and phage buffer (1.21 g Tris + 2.46 g MgSO₄ + 3.97 g NaCl + 0.15 g CaCl₂ in 1 L MiniQ) also prepped here for downstream use.
- **[2026-06-02](../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md)** — Phage isolation round 1: each enrichment centrifuged (2500 rpm, 5 min) → 0.22 µm syringe-filtered → filtrate stored at 4 °C as the working phage stocks **ϕ3, ϕ5, ϕ6, ϕ8, ϕ9, ϕ10** (photo `photos/0605/` "phage isolation round 1, 4/6/2").
- **[2026-06-03](../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md)** — **First plaque assay attempt** with 0.7 % LB soft-agar overlay. Plan: 10 bacteria × 6 phages = 60 plates (3-way plate split for 6 phages per pair of bacteria). **Failed/partial:** soft agar didn't fully solidify; only the following bacteria-phage combinations got readable coverage:
    - `10-10-2` × phages 3 / 5 / 6 / 8 / 9 / 10
    - `6-3-2`   × phages 3 / 5 / 6 / 8 / 9 / 10
    - `10-9-2`  × phages 3 / 5 / 6
    - `8-2-2`   × phages 8 / 9 / 10
- **[2026-06-04](../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md)** — **Second plaque-assay prep.** Switched to layered-plate method (3 mL of 0.7 % LB-agar overlay on hard agar). Scope: **30 plates total** = **3 phages (ϕ8, ϕ9, ϕ10) × 10 bacteria samples**. Per-plate composition: 3 mL soft agar + **250 µL** bacteria + **10 µL** phage filtrate. Soil-enrichment flasks disposed (bleached, washed) — phage-enrichment side now complete.
- **[2026-06-05](../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md)** — **Plaque assay round 3** (per the day's lab-notebook title; this is the third overall plating attempt, *not* a re-isolation round). Carol ran the layered-plate method again with **increased per-plate volumes** vs 6-04: 3 mL of 0.7 % soft agar + **300 µL** actively-grown bacteria (vs 250 µL) + **150 µL** phage filtrate (vs 10 µL — **15× more phage** to maximise plaque detection). Same scope as 6-04: **30 plates** = 3 phages (ϕ8, ϕ9, ϕ10) × 10 bacteria. **No plate failures observed during setup**; readout planned 2026-06-06. `[Question: were the 6-04 prep plates ever read out separately, or did the team move directly to the 6-05 increased-volume re-plate? Lab notebook 6-05 doesn't describe a 6-04 readout.]`
- **UNDONE — planned 2026-06-06** — Read out the 6-04 prep and 6-05 round-3 plates (count plaques per bacteria × phage combination). The 6-05 round, with its much higher phage input, is the bet for actually seeing plaques.
- **UNDONE — re-isolation round 2** — Pick single plaques, re-plate on fresh lawn to amplify single-phage progeny.
- **UNDONE — re-isolation round 3** — Repeat to confirm single-phage origin before sequencing.

---
## Log
- 2026-06-05 — Initial fill of the five subsections by Alex + Claude, sourced from the digitized lab-notebook entries in `lab_notebook/digitalized/`, the OD spreadsheet `data/assays/0529_OD.xlsx`, and the 0605 lab photos in `photos/0605/`. Intro paragraphs preserved verbatim. Three `==CONFIRM==` markers added (bacteria/phage #2-vs-#3 sample mismatch flagged in both sections; `8-5-2` duplicate in the 6-3 pellet list). `UNDONE` markers used for the 6-06 metagenomics quant, sequencing submissions, second-plaque readout, and re-isolation rounds 2–3. Original `==NEED CONFIRMATION==` flag in the intro preserved.
- 2026-06-05 — **Corrected 5-20 metagenomic-extraction scope** to **all 10 soil sites** (was previously misrecorded as just 6 — that 6-site subset is the bacterial enrichment, a separate operation done the same day). Adjusted the 5-28 entry's wording from "remaining sites" to "re-extraction of selected sites" since the original 10 had already been covered on 5-20.
- 2026-06-05 — **Backfill of 2026-06-05 work** across three sections: (a) Metagenomics — Qubit re-quant of the 2nd batch on Portelite BDR, results still low, PI hypothesis + 4-more-extractions plan with smaller biomass added as new UNDONEs; (b) Bacteria DNA Sequencing — new **Pipeline overview** subsection added explaining the 7-stage soil-enrichment → streak → isolate → liquid-culture → pellet → DNA → sequencing chain conceptually before the dated bullets, plus a new 6-05 dated bullet recording the bacteria-genome extraction (Quick-DNA Miniprep Kit) and Qubit quant against the same 6-point curve; (c) Plaque Assay → Assay with Filtrated Phage — new 6-05 round-3 bullet with the increased per-plate volumes (300 µL bacteria + 150 µL phage), and the readout UNDONE merged across the 6-04 and 6-05 platings. `[TBD]` markers retained for the smaller-biomass target mass and the 6-04-readout question.
- 2026-07-08 — **Flipped the "Submit phage DNA for sequencing" UNDONE to done (partial)**: `9-2-1 Φ8` results came back (vendor code `3NKSC3`), raw data organized into `data/phage_genome/9-2-1/`. Only this one line touched — the phage-amplification/extraction UNDONEs above it, and the rest of this document (frozen at 2026-06-05), do not yet reflect roughly a month of subsequent work visible elsewhere in the repo (OD/growth assays through 06-29, RBP fold screening through 07-03). Flagged inline rather than backfilled, since that's a separate, larger pass.
