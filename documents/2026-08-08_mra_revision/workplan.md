# MRA00793-26 revision — work plan and evidence pack

**Manuscript:** MRA00793-26, "Complete genome sequences of three co-occurring *Pseudomonas* isolates from California Botanic Garden topsoil"
**Decision letter:** 2026-07-31, Annette Rowe (Editor) · forwarded by Cesar 2026-08-01 · **60-day deadline ≈ 2026-09-29**
**Purpose:** everything needed to produce the two files Cesar asked for — a tracked-changes manuscript and a Response to Reviewers — assembled from the repo's primary records.

> 中文導讀：這份是改稿的工作底稿，正文用英文寫，方便直接搬進要交出去的兩份文件。最上面 ⚠️ 是現在卡住的四件事；接著是給 Cesar 的信稿；再來是八條審稿意見逐條的「答案／來源／還缺什麼」；最後是**審稿人沒問、但我們自己查出來的五處方法段錯誤**——那一節最重要。

---

## ⚠️ Blocked — cannot proceed without these

1. **We do not have the submitted manuscript.** The repo's only full draft is `documents/2026-06-27_MRA_Pseudomonas.docx`, titled "Complete genome sequences of **two closely related** soil *Pseudomonas* **strains**", covering **four** isolates (8-5-2, 9-2-1, 9-6-2, 10-10-2) and excluding 8-10-2. The decision letter's title says **three co-occurring isolates**. Reviewer #1 says line 4 of Table 1 holds a BioSample number; the repo draft says `pending`. Both reviewers cite line numbers (11, 19), so the submitted file is line-numbered. `git log` shows no manuscript commit since 2026-06-28. **A later, three-isolate, line-numbered .docx exists and is not in this repository.** Track changes must be applied to that file, and every reviewer comment is anchored to its line numbers. Do not edit the 0627 draft.

2. **Which three isolates?** Two competing readings, and this changes the taxonomy and ANI text substantially:
   - **(a) the three ANI-distinct strains** — one of {8-5-2, 10-10-2}, one of {9-2-1, 9-6-2}, plus **8-10-2** (*P. capeferrum*, a different species). Fits Reviewer #1's phrase "three *Pseudomonas* strains isolated from soils near **different plant species**", and fits "co-occurring".
   - **(b) the three isolates the lab notebook records as sent for sequencing on 2026-06-08** — 9-2-1, 9-6-2, 10-10-2. But 9-2-1 and 9-6-2 are 100% ANI to each other and share the same adjacent plant (*Aesculus californica*), which contradicts "different plant species".

   Reading (a) is more likely, **but this must not be guessed.** Note that Alex already asked the PI this exact question on 2026-07-29 ("When you say 'our three isolates' — which three?") and it was left unanswered — see `documents/2026-07-29_pi_conversation/README.md:211-227`. Ask again, with the two options spelled out so it can be answered in one line.

3. **Deposition status, and who owns it.** No BioSample, BioProject, SRA or GCA accession for our own data exists anywhere in the repo — the only `GCA_`/`GCF_` strings found are reference genomes used for comparison. The newest statement on record (`documents/2026-07-29_results_synthesis_EN.qmd:283`) still says every accession is `pending` and that "submission is blocked on deposition, not on analysis" — and line 458 of that same document assigns **GenBank / SRA deposition to Alex**. If that is still true, this is Alex's task, not Cesar's, and it is the item most likely to blow the 60-day deadline. The MRA author checklist is explicit: *"All resources have been made publicly available **before submission**. All raw reads … must be submitted to NCBI's SRA."* The editor's letter makes live, resolving accession links a condition of publication.

4. **Word budget.** MRA hard limits (Author Checklist, July 2025): **abstract ≤ 50 words**, **Announcement ≤ 500 words** excluding abstract and acknowledgments, **at most one figure and/or one table**. The 0627 draft measures **59 words** (abstract) and **586 words** (body) — already over on both. The reviewers ask us to *add* six things. The editor states that when cutting, priority goes to the review requests and the MRA checklist items. **A cut list is needed, and choosing what to cut is an author-level decision for Cesar, not ours to make unilaterally.**

---

## 1. Draft email to Cesar

> Subject: MRA00793-26 revision — five things I need before I can start
>
> Hi Cesar,
>
> Happy to take the first pass at the revision. Yes, I have access to Microsoft Word and can keep track changes on, and I'll write the Response to Reviewers as a separate document as the editorial office requires.
>
> Before I start editing I need five things, because the version I have in our shared files is an earlier draft than the one that went to review:
>
> 1. **The submitted .docx**, the line-numbered version. The reviewers refer to specific line numbers (lines 11 and 19) and to a Table 1 row that currently holds a BioSample number — neither matches the draft I have, which is the four-isolate version titled "two closely related soil *Pseudomonas* strains."
> 2. **Which three isolates the submitted version covers.** I want to be sure before I touch the taxonomy text. My guess is the three ANI-distinct strains — one of 8-5-2/10-10-2, one of 9-2-1/9-6-2, and 8-10-2 (*P. capeferrum*) — since Reviewer #1 mentions three strains from soils near different plant species. But it could equally be 9-2-1, 9-6-2 and 10-10-2, which are the three our lab notebook records as sent for sequencing. One line from you settles it.
> 3. **Deposition status.** Reviewer #1 is right that Table 1 currently shows a BioSample rather than a genome accession, and the MRA checklist requires the assemblies and raw reads to be publicly available with resolving links before publication. Could you tell me where the GenBank and SRA submissions currently stand, and whether that is on me to finish? If the assemblies still have to go through GenBank, that is the item most likely to run past the 60-day window (the letter is dated 31 July, so we are looking at roughly 29 September).
> 4. **The Plasmidsaurus run report, or just the flow cell type.** Both reviewers ask which flow cell was used. Our manuscript only records the library kit (ONT ligation kit v14), and the flow cell does not appear in any of the deliverable files they sent us. I'd rather ask them than guess. While we're asking: do they fragment or shear the DNA during their prep? Reviewer #1 asks that too, and we did not shear anything on our end.
> 5. **How the sequencing candidates were chosen.** Reviewer #1 reads the OD 0.6 threshold as our sequencing selection criterion. Looking at the notebook, OD 0.6 was the threshold for freezing a culture as a glycerol stock — all 28 stocks cleared it, and the isolates we sequenced were not the highest-OD ones. So there was some other basis for picking them, and I don't have it written down anywhere.
>
> One more thing worth flagging: while checking the methods against our lab notebook I found a few places where the text does not match what we actually did — most importantly, the manuscript says DNA was renormalised to 50 ng/µL, but the notebook records the bacterial genomic DNA as submitted undiluted at 139–195 ng/µL. I've listed them all and I'd propose correcting them in this revision and mentioning it briefly in the response letter. Let me know if you'd rather handle that differently.
>
> Alex

---

## 2. Reviewer comments, point by point

Comments are quoted verbatim for reuse in the Response to Reviewers. **Do not add line numbers until the submitted file is in hand.**

### Reviewer #1

**R1.0 —** *"This manuscript describes the isolation and sequencing of three Pseudomonas strains isolated from soils near different plant species."*
Context only; useful because it implies the three isolates come from **different** adjacent plants — evidence for reading (a) in blocker 2 above.

**R1.1 —** *"The manuscript gives a nice overview of the isolation procedure, but it is not clear to me, if only these three isolates were obtained (out of how many?) or what was the rationale for the selection criteria for sequencing (reaching an OD of 0.6?)."*

*Answerable from the notebook, except the last clause.* The chain is: **10 soil sites** sampled 2026-05-19 (`lab_notebook/digitalized/2026-05-19_soil-sample-collection.md:14-16`) → **6 enrichments**, from sites #2, #5, #6, #8, #9, #10 (`2026-05-20_dna-extraction-soil-enrichment.md:25`) → **60 PMM plates**, 10 per enrichment (`2026-05-26_streak-soil-enrichment.md:19`) → 2 colonies picked per plate onto PIA (`2026-05-27_dna-quantification-pia-plates.md:43`) → **28 glycerol stocks** (`2026-05-29_optical-density-bacteria-stock.md:113`, physically re-verified 2026-06-13 per `data/dna_extraction_inventory.md:79`) → **5 genomes completed**.

> **Integrity note.** The honest answer is "28 isolates were banked and *five* genomes were sequenced", not "only three were obtained". Whatever the submitted version covers, the response must not imply three was the total. If the other genomes are held for a separate publication, say so plainly.

*Not answerable:* the actual rationale for choosing which stocks went to sequencing. See R1.1b.

**R1.1b — the OD 0.6 clause is a genuine error in the manuscript, not just an unclear one.**
The notebook says: *"The threshold to take as stock is OD of 0.6 or above at full concentration (no dilution). **We stored all of them as stock.**"* (`2026-05-29_optical-density-bacteria-stock.md:44`). All 28 stocks measured ≥ 0.645, so **the 0.6 threshold excluded nobody**. And the isolates that went to sequencing (9-2-1 = 0.830, 9-6-2 = 0.904, 10-10-2 = 0.871) were **not** the highest-OD stocks — 9-1-1 at 1.671 was never sequenced.

So OD 0.6 gated *freezing a stock*, not *selecting for sequencing*. The current text runs the two together in one sentence, which is exactly what the reviewer caught. **Fix:** attach the OD sentence to the stock-freezing step, and state the actual sequencing-selection basis separately — pending Cesar's answer. (Also: the "OD > 0.8" in the older 0626 draft appears nowhere in the notebook, protocol or scheme; that figure has no support.)

**R1.2 —** *"Were any controls instituted to make sure contamination during the enrichment process was not an issue."*

*Answer honestly: no dedicated blank.* No no-soil, media-only, or blank control tube or plate is recorded anywhere between 2026-05-19 and 2026-06-10. What was done, and what should be stated:
- repeated three-phase streak-to-single-colony purification at every transfer — PMM (`2026-05-26...md:14,23-28`), PMM→PIA (`2026-05-27...md:43`), and again on each revival from frozen stock (`2026-06-01_lb-agar-phage-buffer.md:47-51`, `2026-06-08...md:34-35`)
- **PIA is a selective medium** restricting growth to *Pseudomonas* (`protocol/md/media/pia.md:8-14`)
- fresh loop per colony, fresh tip per enrichment, bulk reagents aliquoted to avoid pipetting from stock bottles (`2026-06-09_bacteria-culture-phage-isolation.md:27,36`, `2026-06-02_inoculation-phage-isolation.md:51`)

> **The strongest reply is the empirical one:** CheckM contamination is **0.87–1.94%** and every isolate assembled into a **single closed contig** at 99.74–100% completeness. If enrichment-stage contamination had carried through, the assemblies would not look like this. Lead the response with the purification regime, concede that no dedicated blank was run, then close with the CheckM/assembly evidence.

**R1.3 —** *"Please clarify if DNA was sheard for the ONT library preparation and if so how."*

*Partly answerable.* On our side, nothing was deliberately sheared: the bacterial-genome track used the Zymo Quick-DNA Miniprep column workflow with a 4–6 s vortex and column spins only (`protocol/md/workflows/bacteria_genome_extraction.md`). **Bead-beating was used only on the separate metagenomic track**, never on the sequenced isolates (`2026-06-08_metagenomic-extraction-dna-concentration-quantification.md:64`). No explicit "not sheared" statement exists in the notebook. Whether Plasmidsaurus fragments during their own prep is unknown — **ask them** (email item 4). Note that the manuscript's existing phrase "without size selection" answers a different question and cannot stand in for this.

**R1.4 —** *"What ONT Flow cell/device was used for sequencing"* · **and R2.2 (same ask)**

*Not in the repo at all.* A repo-wide search for `FLO-MIN|FLO-PRO|FLO-FLG|R10.4.1|R9.4.1|MinION|GridION|PromethION` returns zero hits in any file type, including all five Plasmidsaurus HTML deliverable reports. Only the **library kit** and **basecaller** are recorded: "ONT ligation sequencing kit v.14 (SQK0LSK1114)" and "Dorado … super-accuracy (sup) basecalling model (v4.3.0)". Kit ≠ flow cell. **Must come from Plasmidsaurus.** Do not guess a model number.

**R1.5 —** *"In Table 1, what does line 3 mean ? (it is the same name as the isolate?)"* · **and R2.3 (same ask)**

Table 1's first data row is "Isolate (internal name)" repeating the column headers verbatim (8-5-2 / 9-2-1 / 9-6-2 / 10-10-2). **Delete the row.** Both reviewers flagged it; it is the cheapest fix in the set and also buys back a little space.

**R1.6 —** *"Line 4, this is the biosample number not the genome accession number. Assemblies start with GCA_XXXX"*

Relabel that row **BioSample** and add a separate **Genome assembly accession (GCA_…)** row, plus an **SRA run accession** row for the raw reads — the MRA checklist requires accessions for *both* assembly and raw reads, each hyperlinked to a live public record. **This is gated on blocker 3**; the row cannot be filled until deposition completes.

**R1.7 —** *"Check consistency of italicizing: Table one closest species and make sure to italicize the genus Pseudomonas. (e.g., line 11)"* · **and R2.1**, *"ensure all species and genus names are italicized as appropriate (see line 19)"*

Sweep every occurrence: *Pseudomonas*, *Pseudomonas_E* sp013179515, *P. capeferrum*, *P. aeruginosa*, *P. putida*, and every "Closest species (GTDB)" cell in Table 1. Also check the adjacent-plant row — *Chilopsis linearis*, *Aesculus californica*, *Nicotiana quadrivalvis* are species names and take italics too. Purely mechanical; can be done the moment the file arrives.

### Reviewer #2

*"This is an excellent announcement that contains most of the information needed to publish these genomes. I commend the authors on their attention to detail. A few minor comments:"* — worth quoting in the response's opening thank-you.

**R2.1** italicisation → see R1.7. **R2.3** remove Table 1 row 1 → see R1.5.

**R2.2 —** *"specify which flowcell type was used for sequencing, and total number of raw reads obtained"*

Flow cell → see R1.4 (blocked). **Raw read counts are already in hand and, in fact, already in Table 1** — they just are not labelled as raw. Plasmidsaurus's own report states, for 9-2-1, *"Total number of reads 354,501 reads"* and *"Raw coverage 313x"*, and the arithmetic confirms it: 1,934,820,303 bp ÷ 6,178,779 bp = 313.1× = the `est_cov_raw` field. So Table 1's "Total reads" row **is** the pre-filter count.

| Isolate | Raw reads | Total bases | Raw coverage | Final assembly coverage (Table 1 "depth") |
|:--|--:|--:|--:|--:|
| 8-5-2 | 559,553 | 3,026 Mb | 510× | 95 |
| 9-2-1 | 354,501 | 1,935 Mb | 313× | 94 |
| 9-6-2 (rerun) | 107,609 | 435 Mb | 70× | 67 |
| 9-6-2 (original) | 30,070 | 157 Mb | 25× | 24 |
| 10-10-2 | 128,866 | 522 Mb | 88× | 84 |
| 8-10-2 (rerun) | 546,337 | 3,220 Mb | 565× | 96 |

Source: each isolate's `*_ont-stats.tsv` (`total_num_reads`, `total_seq`, `est_cov_raw`, `est_cov`) and the matching `*_report.html`. **Fix:** rename the row "Total raw reads" and add a "Raw coverage (×)" row, so raw and final coverage are no longer conflated. Note the post-Filtlong read count does not exist anywhere in the repo — no Filtlong log, no NanoStat output — so we can report raw reads but not "reads after filtering".

---

## 3. Reruns — what to disclose

Correcting an earlier assumption: **9-6-2's first run was not a failure.** It was low-yield (157 Mb, 25× raw, below Plasmidsaurus's stated 210 Mb standard-service target) but it still produced a complete, single-contig, 99.74%-complete assembly. The run that *did* fail is **8-10-2's first run** (`data/bacteria_genome/8-10-2/B9TF7H_2_Sample_2_8B_report.html`, 2026-06-25): *"Your sample was not able to be assembled. Your genome was not able to assemble likely because not enough reads were obtained."*

**One thing to check before reporting 9-6-2's read count.** `longest_read` is **92,268 bp in both** the original and the rerun `ont-stats.tsv`. Two independent runs matching to the base pair is not plausible by chance, and Plasmidsaurus's own failure-report boilerplate states their policy is to *"Combine the data from the two runs together to increase chances of a successful assembly."* So 9-6-2's 107,609 reads may **include** the original run's 30,070 rather than being a fresh independent count. This is an inference from file contents, not a documented fact — **confirm with Plasmidsaurus before stating a raw read count for 9-6-2 in print.** If reruns were combined for 8-10-2 as well, the same caveat applies to its 546,337.

---

## 4. Methods errors the reviewers did *not* catch

None of these were raised in review. All are inaccuracies in a submitted manuscript's methods section and should be corrected in this revision, with a brief note in the response letter ("on re-checking our primary records during this revision we also corrected the following"). Volunteering these is a credit, not a liability.

1. **"renormalized to 50 ng/µL" — not what happened.** The bacterial genomic DNA was submitted **undiluted**, at its extraction concentration: 9-2-1 = 139.29, 9-6-2 = 194.53, 10-10-2 = 140.44 ng/µL, ~90 µL each. The notebook states it explicitly: *"Bacterial genomes (9-2-1, 9-6-2, 10-10-2) — **NOT diluted**: submitted at their 2026-06-05 extraction concentration"* (`2026-06-08_metagenomic-extraction-dna-concentration-quantification.md:154`, corroborated `data/dna_extraction_inventory.md:116-128`). No 50 ng/µL normalisation step is recorded anywhere. (The 50 ng/µL figure may have come from the metagenome track, which *was* diluted — 125.33 and 69.39 ng/µL — but even those are not 50.)

2. **"pelleted at 3000 g" — the notebook records rpm, not g.** *"Centrifuge at 3000 **rpm** for 15 min"* (`2026-06-03_phage-plaque-assay.md:39-42`). These are not interchangeable without the rotor radius. Either convert it properly using the rotor spec or report it as rpm with the rotor named.

3. **A centrifugation step is missing.** The same notebook passage records a second, higher-speed spin — 10,000 × g for 10 min — after the PBS washes. The manuscript does not mention it.

4. **"washed twice with PBS" — the notebook reads as three.** 5 mL PBS ×2 ("repeat twice"), then a further 1.5 mL wash on transfer to the 2 mL tube.

5. **`SQK0LSK1114` is a typo.** No such ONT catalogue code exists; the ligation sequencing kit v14 is **`SQK-LSK114`**. Fix in both the methods text and anywhere else it appears.

6. **The Filtlong parameters are stated two different ways.** The manuscript says *"--min_length 300 --keep_percent 95"*; Plasmidsaurus's report says *"Remove the bottom 5% worst fastq reads via Filtlong v0.2.1 (default parameters)"*. Decide which is true — if the vendor ran it, their description governs — and state it once, consistently.

Two further items to verify rather than assume, both from `protocol/md/workflows/bacteria_genome_extraction.md:24-47`: the run used **450 µL** lysis buffer (kit default 400 µL), **15,000 × g / 5 min** spins (kit default ≥10,000 × g / 1 min, changed because the default spin failed for most samples), and **100 µL** elution. The manuscript compresses all of this to "following manufacturer's instructions", which is not accurate if the protocol was modified. MRA's checklist asks for "detailed methods for DNA isolation, library preparation, and sequencing (including the technology and chemistry used)".

---

## 5. Deliverables and mechanics

The editorial office requires **three separate uploads**:

1. **"Response to Reviewers"** — a standalone file with point-by-point responses. Explicitly *"NOT in your cover letter."*
2. **"Marked-Up Manuscript"** — a compare copy **without figures**, tracked changes from the original submission, all changes highlighted no matter how minor.
3. **A clean .doc/.docx** of the revised manuscript, with the previous version removed. Each figure uploaded separately as an editable high-resolution file (TIFF or EPS preferred); multipanel figures assembled into one file.

Submit at `https://mra.msubmit.net/cgi-bin/main.plex` → Author Tasks → the manuscript title.

**On Word:** Cesar asked directly whether you use it. Word on the web handles track changes fine. Google Docs suggestion mode exported to .docx does preserve the markup, but open the exported file and confirm the revisions render before sending — a marked-up file whose marks don't show defeats the point.

**Word budget arithmetic.** Limits are abstract ≤ 50, Announcement ≤ 500, one figure and/or one table. The 0627 draft is 59 and 586. The reviewers ask us to add: total isolates obtained, sequencing-selection rationale, contamination-control statement, shearing statement, flow cell, raw read count. Deleting Table 1's redundant first row helps the table, not the body. **Once the submitted file arrives, count it first, then bring Cesar a proposed cut list** rather than cutting unilaterally — the editor's instruction is that review requests and checklist items take priority over everything else when reducing.

---

## Evidence appendix

- Decision letter and Cesar's instructions: `documents/2026-08-08_mra_revision/decision_letter.pdf` (2 pages; letter dated 2026-07-31, forwarded 2026-08-01)
- MRA limits and requirements: ASM MRA Author Checklist, July 2025 revision — abstract ≤ 50 words, Announcement ≤ 500 words exclusive of abstract and acknowledgments, one figure and/or one table, all resources public *before* submission, raw reads to SRA, accessions for both assembly and raw reads hyperlinked
- Repo manuscript drafts (four-isolate, superseded): `documents/2026-06-27_MRA_Pseudomonas.docx`, `documents/2026-06-26_MRA_Pseudomonas_Annotation.docx`, `documents/2026-06-26_MRA_Pseudomonas.docx.bak`
- Isolation chain and counts: `lab_notebook/digitalized/2026-05-19_soil-sample-collection.md:14-16`, `2026-05-20_dna-extraction-soil-enrichment.md:25`, `2026-05-26_streak-soil-enrichment.md:19`, `2026-05-27_dna-quantification-pia-plates.md:43`, `2026-05-29_optical-density-bacteria-stock.md:113`
- OD600 data and threshold: `2026-05-29_optical-density-bacteria-stock.md:44,60-112`; raw table `data/assays/0529_OD.xlsx`
- Purification practice and media selectivity: `2026-05-26_streak-soil-enrichment.md:14,23-28`, `2026-06-01_lb-agar-phage-buffer.md:47-51`, `protocol/md/media/pia.md:8-14`
- Extraction protocol as run, including deviations: `protocol/md/workflows/bacteria_genome_extraction.md:24-47,95,102-130`
- Submitted concentrations, undiluted: `lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md:147-166`, `data/dna_extraction_inventory.md:116-128`
- Sequencing statistics: `data/bacteria_genome/*/*_ont-stats.tsv` and `*_report.html` (fields `total_num_reads`, `total_seq`, `est_cov_raw`, `est_cov`, `rN50`, `median_read`, `median_phred`)
- 8-10-2 failed first run and vendor rerun policy: `data/bacteria_genome/8-10-2/B9TF7H_2_Sample_2_8B_report.html` (2026-06-25)
- Deposition still pending, ownership assigned: `documents/2026-07-29_results_synthesis_EN.qmd:283,458`
- "Which three isolates" asked and unanswered: `documents/2026-07-29_pi_conversation/transcript.md:102`, `README.md:211-227`

---

*Log: 2026-08-08 — Assembled by Claude from `documents/2026-08-08_mra_revision/decision_letter.pdf` (the MRA00793-26 decision letter), the ASM MRA Author Checklist (July 2025), the lab notebook, the Plasmidsaurus deliverable files, and the repo's manuscript drafts. Four blockers identified, the submitted manuscript's absence from the repo being the one that stops all editing. Six reviewer asks are answerable from primary records (isolate counts, OD semantics, contamination practice, shearing on our side, raw reads, Table 1 fixes); three require Cesar or Plasmidsaurus (flow cell, vendor-side fragmentation, deposition). Section 4 lists five methods statements that do not match the primary record and were not raised by either reviewer — these were found by checking the manuscript against the notebook rather than by reading the reviews. One earlier assumption corrected during drafting: 9-6-2's first sequencing run was low-yield but successful; the run that failed outright was 8-10-2's first run. Flagged as an inference needing vendor confirmation: 9-6-2's rerun read count may include the original run's reads (identical `longest_read` of 92,268 bp in both, plus Plasmidsaurus's stated policy of combining runs).*
