# Response to Reviewers — MRA00793-26

**August 8, 2026**
**By Chun-Yu Chen**

Thank you, Reviewer #1 and Reviewer #2, for your detailed feedback on this manuscript. Your comments are essential for the clarity of sharing our scientific discovery. We are genuinely appreciative of your effort. Below is our response to the points raised in the review.

All line numbers refer to the originally submitted manuscript. Every change is shown in the marked-up manuscript file.

---

## Reviewer #1

**1.1 — Isolate yield.** "It is not clear to me, if only these three isolates were obtained (out of how many?)"

The three genomes reported here are not the total yield of the isolation, and we have made that explicit. Ten soil sites were sampled and six were carried into enrichment; enrichments were plated onto 60 *Pseudomonas* Minimal Agar plates, colonies were purified onto *Pseudomonas* Isolation Agar and grown in LB, giving 28 archived isolates. Five were taken to whole-genome sequencing, and on ANI comparison these collapsed into three distinct strains — 10-10-2 is a 99.997%-ANI clone of 8-5-2 and 9-6-2 is a 100.000%-ANI clone of 9-2-1 — so one representative genome per strain is reported. This is what the "Represents" row of Table 1 was meant to convey; see 1.6 below, where that row is corrected.

**Change:** new sentence after line 33 — "Five isolates spanning three collection sites and both colony types recovered on PIA were selected for whole-genome sequencing, and collapsed by ANI into the three strains reported here."

---

**1.2 — Selection criteria.** "or what was the rationale for the selection criteria for sequencing (reaching an OD of 0.6?)"

You are right that the OD600 > 0.6 threshold reads as a sequencing selection criterion; it is not one, and we have separated the two.

That threshold governed only whether an overnight culture was dense enough to be archived as a glycerol stock. Every one of the 28 archived isolates exceeded it (measured range 0.645–1.671), so it excluded nothing, and the isolates that were sequenced were not the highest-OD stocks in the collection.

The actual basis for selection was to maximise the diversity captured rather than to sample any one group repeatedly. Sampling sites had been chosen in the field by vegetation type, and the archived isolates were grouped by colony morphology and pigmentation on *Pseudomonas* Isolation Agar into two sets, one of which the team had flagged as putative *P. aeruginosa*. Five isolates were then taken forward for sequencing so as to draw from both morphological sets and from three separate collection sites, rather than from a single site or a single colony type. The outcome supports the approach: the five isolates resolved into three genomically distinct strains, including one that proved to be a different species altogether (*P. capeferrum*).

**Change:** lines 31–33 revised to "Next morning, cultures reaching an optical density (OD600) > 0.6 were archived as 25% glycerol stocks at -80°C; all 28 isolates archived in this study met this threshold." The selection basis is stated in the new sentence given under 1.1 above.

---

**1.3 — Contamination controls.** "Were any controls instituted to make sure contamination during the enrichment process was not an issue."

We did not run an uninoculated enrichment blank, and would rather say so plainly than imply otherwise. Purity was enforced procedurally and then verified from the assemblies themselves. Procedurally, every isolate passed through successive streak-to-single-colony rounds as described at lines 27–30 — from the enrichment onto *Pseudomonas* Minimal Agar, from there onto *Pseudomonas* Isolation Agar, a selective medium that restricts growth to *Pseudomonas*, and once more on revival from the frozen stock before DNA extraction. A fresh loop was used for every colony and a fresh pipette tip for every enrichment. Empirically, the assemblies are the strongest evidence available that enrichment-stage contamination did not carry through: each of the three isolates assembled into a single circular contig with CheckM completeness of 99.74–100.00% and CheckM contamination of 0.20–1.94%, and sourmash assigned each genome unambiguously to a single species. A mixed culture would not produce this result.

**Change:** line 34 revised to "colonies were revived from stocks by single-colony streak on LB agar (1% agar)". The purity evidence — single-contig assemblies, CheckM completeness and contamination — is already reported in Table 1.

---

**1.4 — DNA shearing.** "Please clarify if DNA was sheard for the ONT library preparation and if so how."

Thank you — checking this revealed that our description of the library preparation was inaccurate, and we have corrected it.

No shearing was performed by us. Genomic DNA was extracted on a silica column (Quick-DNA Kit, Zymo Research) with no bead-beating and no enzymatic or mechanical fragmentation, and was submitted intact to the sequencing provider.

The library preparation, however, does fragment the DNA, which the submitted manuscript did not convey. Plasmidsaurus prepare an amplification-free long-read library using v14 chemistry in which the input genomic DNA undergoes minimal, sequence-independent fragmentation by tagmentation. The manuscript described this as a ligation-based preparation, which was incorrect. No size selection is performed for the bacterial genome service.

**Change:** lines 39–40 revised to "…were sent for sequencing at Plasmidsaurus (Eugene, OR) on an Oxford Nanopore PromethION using R10.4.1 flow cells, with amplification-free v14 chemistry in which input DNA undergoes minimal sequence-independent fragmentation by tagmentation; no size selection was performed."

---

**1.5 — Flow cell and device.** "What ONT Flow cell/device was used for sequencing"

Sequencing was performed on an Oxford Nanopore PromethION using R10.4.1 flow cells. We apologise for the omission and have added both the instrument and the flow cell chemistry to the methods; the revised sentence is given under 1.4 above.

---

**1.6 — Table 1, row 3.** "In Table 1, what does line 3 mean ? (it is the same name as the isolate?)"

You are right, and the row as printed was meaningless. It was meant to record which additional isolates each reported genome stands in for — that is, the ≈100%-ANI clones that were sequenced but are not reported separately — but it was populated with each isolate's own name instead. It now names the clone, and the row label has been made explicit.

**Change:** the row has been relabelled "Additional ≈100%-ANI isolate represented", and its values corrected to "10-10-2 (99.997% ANI)" for 8-5-2, "9-6-2 (100.000% ANI)" for 9-2-1, and "none" for 8-10-2.

---

**1.7 — Table 1, row 4.** "Line 4, this is the biosample number not the genome accession number. Assemblies start with GCA_XXXX"

Correct, and thank you for catching it — that row contained BioSample accessions. Table 1 now reports the BioSample and the genome assembly accession on separate rows, and all three assemblies are publicly available.

**Change:** the row has been split into "BioSample" (SAMN61139397 for 8-5-2, SAMN61139396 for 9-2-1, SAMN61139398 for 8-10-2) and "Genome assembly (GenBank)" (GCA_059295255.1 for 8-5-2, GCA_059295275.1 for 9-2-1, GCA_059295235.1 for 8-10-2). The "Raw read accession (SRA)" row is unchanged. All accessions have been checked to resolve to their full public records.

---

**1.8 — Italicisation.** "Check consistency of italicizing: Table one closest species and make sure to italicize the genus Pseudomonas. (e.g., line 11)"

Corrected throughout. We have italicised every genus and species name in the title, abstract, body, and both the "Closest species (GTDB)" and "Adjacent plant" rows of Table 1.

**Change:** *Pseudomonas* italicised at lines 11 and 18–19, where it had been left in roman; the "Closest species (GTDB)" cells for 9-2-1 and 8-10-2 italicised to match the 8-5-2 cell; *Pseudomonas capeferrum* italicised in Table 1. Occurrences already italicised — the title, lines 17, 49 and 50–51, and the "Adjacent plant" row — were checked and left unchanged.

---

## Reviewer #2

We thank Reviewer #2 for the generous assessment of the manuscript.

**2.1 — Italicisation.** "ensure all species and genus names are italicized as appropriate (see line 19)"

Corrected throughout, including line 19. Please see our response to Reviewer #1, point 1.8, for the full list of changes.

---

> 🛑 **BLOCKED — DELETE THIS BOX BEFORE SUBMITTING.** The 8-10-2 read count below cannot be filled until Cesar and Plasmidsaurus answer. Table 1 says 546,337 reads / 3,220 Mb; the deposited run SRR39379360 holds 272,751 spots / 1,530 Mb. The question to send Cesar is drafted in the internal section at the end of this file, under "Question to send Cesar". **This is the last open item in the whole revision.**

**2.2 — Flow cell type and raw read count.** "specify which flowcell type was used for sequencing, and total number of raw reads obtained"

The instrument and flow cell are now stated in the methods; please see our responses to Reviewer #1, points 1.4 and 1.5.

On read counts: the "Total reads" row of Table 1 already reported the raw, pre-filtering read count, but the label did not say so, and the "Sequencing depth" row reported final assembly coverage, so the two could easily be read as belonging to the same stage. We have relabelled both rows and added the total bases sequenced and the raw coverage, so that the sequencing run and the finished assembly are reported separately.

**Change:** "Total reads" relabelled "Total raw reads"; new rows "Total bases sequenced" and "Raw coverage (×)" added; "Sequencing depth (×)" relabelled "Final assembly coverage (×)". Values: 8-5-2, 559,553 reads / 3,026 Mb / 510× raw / 95× final; 9-2-1, 354,501 reads / 1,935 Mb / 313× raw / 94× final; 8-10-2, [PENDING — see internal note].

---

**2.3 — Redundant Table 1 row.** "the first row in Table 1 (Isolate internal name) can be removed as it is redundant with the column headers."

Agreed and removed.

**Change:** Table 1's "Isolate (internal name)" row has been deleted; the column headers already carry the isolate names.

---

## Additional corrections made by the authors

While preparing this revision we checked the methods section against our primary laboratory records and against the sequencing provider's technical documentation, and found several statements that did not match what was done. Apart from the library preparation, which is covered under 1.4 above, none were raised in review, but we would rather correct them now than leave them in the published record.

**A.1 — Library preparation chemistry (lines 39–40).**

The manuscript described the library as prepared with the ONT ligation sequencing kit v14. The provider's whole-genome service in fact uses an amplification-free v14 preparation based on tagmentation, not ligation, and the catalogue number given in the submitted manuscript ("SQK0LSK1114") is not a valid Oxford Nanopore code in any case. This is the same correction described under Reviewer #1, point 1.4.

**Change:** the ligation-kit description replaced by the tagmentation-based description given under 1.4.

---

**A.2 — Centrifugation units (line 35).**

The manuscript states "pelleted at 3000 g for 15 minutes"; the recorded value is 3000 rpm, which is not equivalent to 3000 × g.

**Change:** revised to "pelleted at 3000 rpm for 15 minutes".

---

**A.3 — Wash steps (lines 35–36).**

The manuscript states the pellet was "washed twice with PBS"; the pellet was in fact washed twice with 5 mL PBS and then once more with 1.5 mL PBS on transfer.

**Change:** revised to "washed twice with 5 mL PBS and once with 1.5 mL PBS".

---

**A.4 — Read filtering parameters (lines 43–44).**

The manuscript specifies Filtlong with the flags "--min_length 300 --keep_percent 95". The provider's documentation describes basecalling with Dorado v4.3 super-accurate model and default Q10 quality filtering, followed by removal of the poorest 5% of reads with Filtlong. The `--keep_percent 95` flag corresponds to that step; the `--min_length 300` flag and the Q10 basecalling filter are not currently reflected in the manuscript in a way that matches the provider's description.

**Change:** revised to "Basecalling was performed with Dorado using the super-accuracy (sup) basecalling model (v4.3.0 [3]) with default Q10 quality filtering, and the poorest 5% of reads were removed with Filtlong (v0.2.1 [4])."

---

**A.5 — Data availability statement (lines 54–55).**

The sentence has been corrected for number agreement and the repository named explicitly.

**Change:** revised to "The complete genomes of our isolates and the raw sequencing data are available under BioProject PRJNA1482863 and PRJNA1483221 respectively. Individual accession numbers are listed in Table 1."

---

To accommodate the additions requested above while remaining within the 500-word limit for the Announcement section, we have condensed several passages that carry no information required by the MRA checklist: the description of the sampling tool and site listing, the phrasing of the carbon and nitrogen amendments, the two plating steps, the overnight LB step, and the closing sentence pointing to Table 1. Media compositions, catalogue numbers, and all software names and version numbers are retained in full. The revised Announcement is 494 words; the abstract is unchanged at 47.

---
---

# NOT FOR SUBMISSION — internal notes

**Delete everything below this line before the file goes to the journal.**

## What still blocks sending — one item

**The 8-10-2 read count in 2.2.** This is the only remaining hard blocker.

Table 1 reports **546,337 reads / 3,220 Mb** for 8-10-2, taken from the Plasmidsaurus `ont-stats.tsv` file. The deposited run **SRR39379360** holds **272,751 spots / 1,529,887,813 bases** — almost exactly half of each. The other two isolates match their deposited runs to the base pair (8-5-2: 559,553 reads / 3,026,040,055 bases; 9-2-1: 354,501 / 1,934,820,303), so this is specific to 8-10-2.

Why it matters: Reviewer #2 is asking us to state the raw read count, and the editor requires every accession to retrieve its full record. A reader who clicks SRR39379360 sees a number half the size of the one in our table.

Likely cause: 8-10-2's first sequencing run failed to assemble (`B9TF7H_2`, 2026-06-25 — "Your sample was not able to be assembled. Your genome was not able to assemble likely because not enough reads were obtained"; that run yielded 91,641,178 bp / 10,746 reads). Plasmidsaurus's stated policy on a failure is to repeat the run at no charge and "combine the data from the two runs together". So the vendor's combined statistics and the single FASTQ uploaded to SRA may not be the same dataset. The arithmetic does not close either way (3,220 − 1,530 = 1,690 Mb, not the 92 Mb of the failed run), so this needs the vendor rather than more guessing.

Note this affects the "Final assembly coverage" figure too: 96× in Table 1 was computed by the vendor from whatever read set their pipeline used.

### Question to send Cesar

> Subject: MRA revision — 8-10-2 read count doesn't match SRA
>
> Hi Cesar,
>
> Revision nearly done. Two things need you.
>
> **1. 8-10-2 read count is wrong somewhere.**
>
> Table 1 says 546,337 reads / 3,220 Mb. Deposited run SRR39379360 has 272,751 spots / 1,530 Mb. Half. Other two isolates match their runs exactly (8-5-2 / SRR39379362, 9-2-1 / SRR39379361).
>
> Our numbers came from the Plasmidsaurus `ont-stats` file for `CZJZZ4_1_rerun_Sample_2_8B_2`. 8-10-2's first run failed — `B9TF7H_2`, 25 June, 92 Mb / 10,746 reads. Plasmidsaurus say they combine a failed run with its rerun, so I assumed that was it. But 3,220 − 1,530 = 1,690 Mb, not 92 Mb. Doesn't explain it.
>
> Two questions:
>
> - Which FASTQ went to SRA for 8-10-2? Was there more than one read file in the delivery folder?
> - Can you ask Plasmidsaurus whether the `CZJZZ4_1_rerun` statistics cover the rerun alone or the rerun plus the failed run? Happy to email them myself if that's easier.
>
> Table 1 and the SRA record have to agree — the editor requires every accession to retrieve its full record, and a reader can check this in one click.
>
> **2. Our library prep description is wrong.**
>
> We wrote "ONT ligation sequencing kit v.14 (SQK0LSK1114)". Plasmidsaurus's technical documentation says the whole-genome service uses amplification-free v14 chemistry with tagmentation, on R10.4.1 flow cells — transposome, not ligation. That catalogue number doesn't exist either. Their prep also fragments the input DNA, which we didn't mention.
>
> I've rewritten it to match, which also answers Reviewer #1's question about whether the DNA was sheared. Happy with that?
>
> Three smaller things:
>
> - For the sequencing-selection rationale Reviewer #1 asks about, I've written that the five sequenced isolates were chosen to span both colony types we'd distinguished on PIA and three collection sites, since nothing in the notebook records a formal criterion. If you had a different reason in mind, tell me and I'll rewrite it.
> - Table 1 gives all three isolates the same coordinates and elevation (34°6'54"N 117°43'28"W, 410 m). By our sample numbering 8-5-2 and 8-10-2 are site 8 and 9-2-1 is site 9, and the earlier four-isolate draft did give 10-10-2 a different position. If the three really do share one coordinate, then my new sentence saying they span three collection sites will read as a contradiction to anyone who checks. Do you have the per-site GPS readings?
> - The abstract says "Two isolates share ~99.4% ANI". That's the 8-5-2 to 9-2-1 pairwise value, but the only ANI numbers in Table 1 are ANI-to-reference (99.75 / 99.53 / 98.66), so a reader can't find 99.4% anywhere in the paper. Should we add the pairwise value to Table 1, or reword the abstract?
>
> Alex

## Resolved

- **Flow cell and instrument.** Instrument (PromethION) from our own SRA submission metadata; flow cell chemistry (R10.4.1) from Plasmidsaurus's public technical documentation. Both sourced, no catalogue part number guessed. The exact part number would be FLO-PRO114M, but do not print that without asking them — R10.4.1 alone fully answers both reviewers.
- **Shearing — answered, and it uncovered a real error.** Plasmidsaurus's technical documentation states: *"We construct an amplification-free long-read sequencing library using the newest v14 library prep chemistry, including minimal fragmentation of the input genomic DNA in a sequence-independent manner via tagmentation."* Tagmentation is transposome-based, not ligation. **The submitted manuscript's "ONT ligation sequencing kit v.14 (SQK0LSK1114)" is wrong on two counts** — wrong chemistry, invalid catalogue number. Now item A.1, the most serious self-reported correction.
- **Selection rationale — written from the records.** The field notebook records that sampling spots were "chosen by different types of vegetation" (2026-05-19), and the OD entry records the 28 stocks split into a first batch and a block flagged as likely *P. aeruginosa* candidates (2026-05-29). Four of the five sequenced isolates came from the first block, one (8-10-2) from the second. **Still send to Cesar for confirmation** — he is corresponding author and may have had a different reason.
- **DNA concentration — dropped at your instruction, notebook annotated.** The manuscript's 50 ng/µL normalisation stands. A dated 2026-08-08 entry was added to the Log of `lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md`, plus an inline warning beside the claim, recording that the "NOT diluted" line is contradicted. Both accounts left in place. Supporting the corrected version: the submitted **volume was already flagged `[TBD]`** in that entry, and 50 ng/µL × 20 µL = 1 µg is a normal submission mass where the undiluted reading implies 12.5–17.5 µg. **Still outstanding:** `data/dna_extraction_inventory.md:116-128` carries the same undiluted figures, untouched.

## Two things for Cesar, not for the reviewers

The assemblies and the raw reads are attached to two different sets of BioSamples for the same three isolates — SAMN61139396/97/98 under PRJNA1482863 for the assemblies, SAMN61176482/83/84 under PRJNA1483221 for the reads. Both resolve publicly, so this will not block publication, but each isolate is represented twice in NCBI. His call whether to leave it.

The lab notebook and `data/dna_extraction_inventory.md` record no submission event for 8-5-2 or 8-10-2 — both listed "not sent" as of the 2026-06-13 inventory, despite completed genomes existing. Two of this paper's three genomes have no documented submission, so the selection rationale in 1.2 cannot be checked against the record for those two.

## Table 1 — complete change list

| # | Row | Change |
|:--|:--|:--|
| 1 | Isolate (internal name) | **Deleted** (R2.3) |
| 2 | Represents (≈100%-ANI clones) | **Relabelled** "Additional ≈100%-ANI isolate represented"; values corrected to 10-10-2 / 9-6-2 / none (R1.6) |
| 3 | Genome accession (GenBank) | **Split** into "BioSample" (SAMN…) and "Genome assembly (GenBank)" (GCA…) (R1.7) |
| 4 | Total reads | **Relabelled** "Total raw reads"; 8-10-2 value pending (R2.2) |
| 5 | — | **New row** "Total bases sequenced" (R2.2) |
| 6 | — | **New row** "Raw coverage (×)" (R2.2) |
| 7 | Sequencing depth (×) | **Relabelled** "Final assembly coverage (×)" (R2.2) |
| 8 | Closest species (GTDB) | **Italicised** for 9-2-1 and 8-10-2 (R1.8, R2.1) |
| 9 | Sequencing platform | **Updated** to "Oxford Nanopore PromethION, R10.4.1" (R1.5, R2.2) |
| 10 | N50 (bp) | **Left unchanged.** Relabelling it "Assembly N50" would be clearer — it equals genome size and sits two rows from "Read N50" — but it was not requested and is not described in this letter, so it was deliberately not touched. Author's call whether to add it to both. |

## Before sending

Every "Change" above is written in the past tense. The revised manuscript implementing all of them is `documents/2026-08-08_mra_revision/manuscript_revised.docx`, produced by editing the submitted file (`documents/2026-08-08_mra_revision/manuscript_submitted.docx`) in place, so its styles, fonts, margins, line numbering and table borders are the journal file's own.

An automated diff of that file against this letter has been run and passes: every "Change" sentence quoted above is present verbatim; every superseded string is gone (`SQK0LSK1114`, "ligation sequencing kit", "pelleted at 3000 g", "Genome accession (GenBank)", "Isolate (internal name)", "Sequencing depth", "Oxford Nanopore (long-read)", and the disputed 546,337); and no genus or species name is left un-italicised anywhere in the body, references, caption or table. Re-run `code/0809_patch_mra_manuscript.py`'s verification after any hand edit in Word.

**The marked-up manuscript is now producible:** Word → Review → Compare, original `documents/2026-08-08_mra_revision/manuscript_submitted.docx` against the revised file. Check the result before uploading — the editorial office wants every change highlighted, no matter how minor, and the comparison must be made after the working note and highlighting are removed.

Checklist before submitting:

- 8-10-2 read count reconciled with SRR39379360 — blocks 2.2, the only hard blocker left
- Cesar confirms the selection rationale in 1.2 and the tagmentation correction (A.1)
- Optional: one-line confirmation from Plasmidsaurus on the library prep and the flow cell part number
- Word count re-measured on the final file: abstract ≤ 50, Announcement ≤ 500
- Every accession in Table 1 clicked and confirmed to retrieve its full public record
- **In the .docx: delete the highlighted AUTHOR WORKING NOTE at the top, and clear the yellow highlighting** from the library-prep clause and the three 8-10-2 cells
- Marked-up manuscript produced (Word → Review → Compare, `documents/2026-08-08_mra_revision/manuscript_submitted.docx` vs the revised file), after the note and highlighting are removed
- Three files uploaded separately: Response to Reviewers, Marked-Up Manuscript (no figures), clean .docx
- In the .docx: delete the 🛑 box above section 2.2 (it is highlighted yellow; the internal notes are already excluded)
- Everything below the "NOT FOR SUBMISSION" divider deleted, and the 🛑 box above section 2.2 deleted

---

**Word version:** `documents/2026-08-08_mra_revision/response_to_reviewers.docx`, rendered from this file by `code/0809_response_letter_to_docx.py`. It stops at the "NOT FOR SUBMISSION" divider, so the internal notes are not in it — edit this markdown and re-run rather than editing the .docx, or the two will drift apart.

---

*Log: 2026-08-08, revised 2026-08-09 — Single consolidated response letter. 2026-08-09: the tail of this file (closing paragraph and the whole internal section) was found truncated on disk and was restored from the working copy, with the updates below folded in. The revised manuscript was generated as `documents/2026-08-08_mra_revision/manuscript_revised.docx` and the quoted "Change" sentences here were synced word-for-word to what actually went into it — the OD sentence now carries "25% glycerol stocks at -80°C", the Filtlong sentence carries its citation numbers, and a new A.5 covers the data-availability rewording. The word-budget paragraph was corrected: the cuts actually taken were the sampling-tool sentence, the amendment phrasing, the two plating steps, the overnight LB step and the Table 1 pointer — the media recipes were **not** cut, contrary to the earlier draft's claim, because reference [2] could not be confirmed to contain the PMM composition. Measured result: Announcement 494/500, abstract 47/50. Table 1 row 10 (N50 relabel) was deliberately left unchanged to keep letter and manuscript in sync.*
