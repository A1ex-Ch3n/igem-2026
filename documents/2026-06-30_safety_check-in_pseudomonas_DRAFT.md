# iGEM 2026 Safety Check-In — *Pseudomonas* soil isolates (DRAFT)

**Team:** Claremont CA — #6317 · **Check-In type:** Whole Organism or Cell Line · **Contact:** Chun-Yu Chen
**Form:** https://teams.igem.org/6317/safety/safety-check-in-form · **Submission ID:** cut5mxwLDzP6hWtNQdkXC5

> Copy each **A:** block into the matching field of the live iGEM form. Everything here is drawn from the team's own repo (lab notebook, scheme doc, genome data, protocols) — sources are listed in the Evidence appendix. Wording is precautionary on purpose: for a safety reviewer, under-stating risk is the costly error.

---

## ⚠️ Decide these before you submit

1. **The "likely *P. aeruginosa*" stocks (most important).** Some batch-2 glycerol stocks were labelled *"likely P. aeruginosa"* from PIA morphology + OD **before** sequencing, and ~10 were revived / cultured / DNA-extracted (9-9-2 was even phage-challenged). None of *those specific* stocks are species-confirmed. The one stock from that presumptive batch that *was* sequenced (8-10-2) came back ***P. capeferrum***, not aeruginosa. **This draft discloses that subset honestly.** Decide: (a) keep the disclosure as written (recommended — it is the truthful, defensible answer and your BSL-2 handling already covers it), or (b) species-confirm those stocks (16S or WGS) first and update the numbers. Do **not** delete the disclosure. Because this form is **public** and names your PI, have the PI/team sign off on the public wording of this disclosure before submitting — making it public is their call, not just yours.
2. **BSL-2 / IBC documentation.** You told me the work runs at **BSL-2** under **KGI** oversight. If KGI has a written IBC approval or biosafety registration number, cite it in "Measures" and attach it under Supporting Documents. If it's PI supervision without a formal IBC letter, soften "IBC approval" to "institutional biosafety oversight."
3. **Whole-Organism sub-fields.** The PDF you gave me only captured the *Activity* branch of the form. The *Whole Organism* branch will ask its own identity questions (organism name, source, risk group, select-agent status, etc.). Map the **Organism description** block below onto whatever fields it shows.
4. **Phages = separate form.** Per your choice, this check-in covers the **bacteria only**. Your novel soil phages (ϕ3/5/6/8/9/10; Φ8 confirmed lytic on 9-6-2 & 9-2-1) are equally not-on-White-List and can go on a second check-in later — say the word and I'll draft it.

---

## Contact Info

**Q: Who from your team should be contacted about this form?**

**A:** Chun-Yu Chen (Claremont CA, team #6317).

---

## Check In Description

**Q: What kind of Check In are you submitting?**

**A:** ☑ **Whole Organism or Cell Line** — wild-type environmental *Pseudomonas* isolates cultured by our team from soil.

**Q: How does this organism fit into your project goals? (1–3 sentences)**

**A:** Our project, *Phagenomics*, is building a computational pipeline that reads a bacterium's genome, predicts the surface proteins a phage could bind, and designs phage receptor-binding proteins (RBPs) against them — turning phage host-range into something we design rather than screen for by trial and error. These wild *Pseudomonas* strains, isolated and whole-genome-sequenced by our team from local soil, are the real-world target hosts that ground the pipeline: their genomes supply the receptor repertoire we model, and the matched soil phages we recovered on them let us test our predictions against real biology.

**Q: Why are you checking in this organism?**

**A:** ☑ **We saw that it's not on the White List.** These are wild environmental isolates — an unnamed species in the *Pseudomonas putida* group (closest sequenced reference *Pseudomonas* sp. CM27 / GTDB *Pseudomonas_E* sp013179515) — so they correspond to no White List entry and were uncharacterised at the moment of isolation. Because the genus *Pseudomonas* also contains opportunistic pathogens, we are submitting them for review rather than assuming they are exempt.

---

## Organism description

*(Map these onto the Whole-Organism branch's identity fields.)*

**Identity.** Wild-type environmental *Pseudomonas* sp., *P. putida* group. Five isolates have been sequenced to complete, single-contig, circular genomes (Oxford Nanopore, via Plasmidsaurus; assembled with Autocycler/Flye/hifiasm/Plassembler; QC by CheckM ≥99.7% complete; taxonomy by sourmash against GTDB):

| Isolate | Closest species (GTDB)                                                  | ANI    | Genome             |
| ------- | ----------------------------------------------------------------------- | ------ | ------------------ |
| 9-2-1   | *Pseudomonas_E* sp013179515 (≈ *Pseudomonas* sp. CM27, GCA_013179515.1) | 99.53% | 6.18 Mbp, 62.4% GC |
| 9-6-2   | *Pseudomonas_E* sp013179515                                             | 99.53% | 6.18 Mbp, 62.4% GC |
| 10-10-2 | *Pseudomonas_E* sp013179515                                             | 99.75% | 5.93 Mbp, 62.6% GC |
| 8-5-2   | *Pseudomonas_E* sp013179515                                             | 99.75% | 5.93 Mbp, 62.6% GC |
| 8-10-2  | *Pseudomonas_E* **capeferrum**                                          | 98.66% | ≈5.5 Mbp           |

- **Not *P. aeruginosa*.** ANI to *P. aeruginosa* PAO1 is only **~80%** — far below the ~95% species boundary — so *P. aeruginosa* is genomically excluded. ANI to the *P. putida* type strain is ~89% (so not *P. putida* proper either; an unnamed *P. putida*-group species).
- **Not genetically modified.** Every isolate is handled as wild-type. The project involves **no cloning, transformation, plasmids, expression vectors, antibiotic-resistance selection, or any genetic modification** of these bacteria — the work to date is isolation, sequencing, phage host-range testing, and *in silico* design.
- **Not a select agent; not clinical.** Environmental soil isolates, not sourced from a clinical sample or culture collection.

**Q: What Risk Group is this organism?**

**A:** ☑ **Risk Group 2** (precautionary). Our isolates are an uncharacterised environmental species in the *Pseudomonas putida* group (closest reference *Pseudomonas* sp. CM27; isolate 8-10-2 = *P. capeferrum*), for which no official risk-group listing exists. The *P. putida* group is classified **Risk Group 1 in some frameworks (e.g. US / ABSA) and Risk Group 2 in others (several EU national lists)**, and the genus *Pseudomonas* includes opportunistic pathogens. Whole-genome sequencing **excludes *P. aeruginosa*** (~80% ANI to PAO1), so this is a conservative call for an uncharacterised environmental organism, not a suspected pathogen. Because some banked stocks are not yet species-confirmed and all work is handled at BSL-2, we adopt the more conservative **Risk Group 2**. *→ Confirm with your PI / KGI biosafety officer — the Risk Group is ultimately their determination; **Risk Group 1** is a defensible fallback if KGI formally classifies the* P. putida *group as RG1.*

**Source.** Topsoil at the **California Botanic Garden (Claremont, CA)**, collected 2026-05-19 with a T-handle soil probe (sites #2–#10; coordinates ~34°6′N 117°43′W). Enriched in *Pseudomonas* Minimal Media, then selectively isolated on *Pseudomonas* Minimal Agar → *Pseudomonas* Isolation Agar (PIA), banked as glycerol stocks.

**How it is used.** Cultured in LB broth; banked as −80 °C glycerol stocks; grown up for genomic-DNA extraction (Zymo Quick-DNA) and sent out for Nanopore whole-genome sequencing; and grown as bacterial lawns/hosts for plaque and OD-lysis assays against our environmental soil phages. Genomes then feed the computational pipeline (surface-receptor mining, structural RBP–receptor binding screens).

**Characterisation status — full disclosure.** The five isolates above are species-confirmed by WGS. Separately, our team banked ~28 stocks in total, and a **batch-2 subset was presumptively labelled "likely *P. aeruginosa*" from selective-media morphology + OD, before any sequencing.** About ten of those presumptive stocks (e.g. 6-2-1, 6-8-1, 6-8-2, 6-10-2, 8-1-2, 9-1-1, 9-1-2, 9-9-2, 9-10-1, 8-10-2) were revived, cultured, and DNA-extracted, and 9-9-2 was phage-challenged. Of that batch, **only 8-10-2 has been sequenced — and it is *P. capeferrum* (P. putida group), not *P. aeruginosa***, which indicates the presumptive label is unreliable. We treat all such stocks at BSL-2 until species-confirmed (see Measures).

---

## Identifying and managing risks

**Q: What risks have you identified from this organism?**

**A:** The isolates are **wild environmental *Pseudomonas***, and the genus contains opportunistic human, animal, and plant pathogens (most notably *P. aeruginosa*, Risk Group 2). At the moment of isolation an environmental *Pseudomonas* colony is not species-confirmed, so there is an a-priori possibility that a given isolate is an opportunistic pathogen. We have reduced that uncertainty by whole-genome sequencing: all five sequenced isolates fall in the non-pathogenic *P. putida* group (closest reference *Pseudomonas* sp. CM27; isolate 8-10-2 = *P. capeferrum*), and *P. aeruginosa* is genomically excluded (~80% ANI). Two honest limitations remain: (1) a subset of banked stocks was presumptively labelled "likely *P. aeruginosa*" and handled **before** species confirmation (see Organism description) — these are not yet sequenced; and (2) we have **not yet mined the genome annotations for virulence or antimicrobial-resistance genes**, so their virulence/AMR gene content is *not yet assessed* rather than known to be absent. General laboratory-exposure routes apply: aerosols/splashes during culturing and pipetting, sharps, and surface contamination.

**Q: What measures have you put in place to manage the risks?**

**A:** All wet-lab work is carried out at **Biosafety Level 2** at Keck Graduate Institute — a precautionary level chosen precisely because environmental *Pseudomonas* isolates are not fully characterised at the time of handling — under the supervision of PI **Dr. J. Cesar Ignacio-Espinoza** and covered by KGI institutional biosafety oversight *[confirm IBC approval / registration number]*. Specifically:
- **Containment & technique:** aseptic technique, performed in / adjacent to a biosafety cabinet or flame; no aerosol-generating procedures beyond standard pipetting.
- **PPE:** gloves, lab coat, and eye protection for all culture handling.
- **Decontamination & disposal:** all media and agar are autoclaved before use; cultures, plates, and liquid waste are treated with ~10% bleach and/or autoclaved before disposal, per our media-disposal protocol.
- **No genetic modification:** isolates are handled strictly as wild-type — we introduce no resistance, virulence, or foreign genes.
- **Characterisation before scale-up:** isolates are whole-genome-sequenced and taxonomically classified, which is how we confirmed the *P. putida*-group identity and excluded *P. aeruginosa*.
- **UNDONE / planned precautions:** species-confirm the remaining presumptively-labelled batch-2 stocks (16S or WGS); screen the Bakta genome annotations for virulence and AMR determinants and report the result.

**Q: Are there alternative ways to achieve your project goals that would present less risk?**

**A:** The lower-risk alternative would be to work exclusively with a pre-characterised White-List laboratory strain (e.g. *P. putida* KT2440) instead of our own soil isolates. We considered this but retained the environmental isolates because they are central to the project's aim: *Phagenomics* is about predicting and designing phage host-range **from a bacterium's own genome**, so having the actual host strains *and* the matched soil phages we recovered on them is what lets us validate predictions against real biology — a pre-characterised lab strain removes exactly that test. We reduce the added risk rather than avoid the work: (1) containment at BSL-2, (2) whole-genome species-confirmation before any extensive handling, and (3) keeping all bacterial work wild-type with no genetic modification. Note that our *computational* pipeline already leans on White-List / reference material where it can — our surrogate-host analysis explicitly uses named *P. putida* reference genomes (with known phages) as a computational stand-in — but that is an *in silico* surrogate host, not a wet-lab replacement for the target strains.

**Q: Is there anything else you want to tell us?**

**A:** The project is at the discovery + *in silico* design stage: we have **created no genetically modified organism**, and the therapeutic/agricultural applications in our project description are long-term aspirations, not current lab activities. We are filing this check-in for the bacterial isolates now; the novel environmental phages we isolated on these hosts (ϕ3/5/6/8/9/10; Φ8 confirmed lytic on 9-6-2 and 9-2-1, not yet sequenced) can be submitted as a separate check-in on request. We would welcome the committee's guidance on the right way to declare the presumptively-labelled, not-yet-sequenced stocks described above.

---

## Supporting Documents (optional uploads)

> ⚠️ **Everything on this form — text *and* uploads — becomes public and indexable** (the form states this explicitly). Attach only what you are comfortable publishing.
>
> **Do NOT upload `documents/2026-06-27_MRA_Pseudomonas.docx`.** It is an unpublished genome-announcement manuscript with named co-authors and pending GenBank/SRA accessions; posting it to a public form would disclose co-authors' unpublished work and create a prior-public-disclosure footprint before the paper is submitted. The committee needs the *species-ID evidence*, not the manuscript.

Attach only what supports the safety case:
- **Species / ANI evidence (recommended):** a single species-ID figure, or the ANI matrix showing ~80% ANI to *P. aeruginosa* PAO1 and the sp013179515 / CM27 assignment — **or** simply cite those numbers in the Organism description above and attach nothing.
- **Disposal / handling protocol:** the media-disposal protocol listing bleach treatment + PPE (safe to make public).
- **Institutional biosafety approval / IBC letter from KGI** — attach if it exists *(see Decision #2)*.

---

## Evidence appendix (repo sources)

- Species truth: `data/bacteria_genome/*/…_sourmash-genome-species.csv`; ANI matrix `code/0623_metagenome_rbp/out_finding_rbps/ani/ani_matrix.csv`; `documents/2026-06-24_strain_phage_conclusions.md`; genome-announcement drafts `documents/2026-06-26_MRA_Pseudomonas_Annotation.docx`, `documents/2026-06-27_MRA_Pseudomonas.docx`.
- Organism / material inventory incl. the "likely aeruginosa" flags: `data/dna_extraction_inventory.md`, `data/week_3_bacteria_list.md`.
- Wet-lab record: `scheme/20260604_confirmed_scheme_CLAUDE.md`; `lab_notebook/digitalized/2026-*.md`.
- Disposal / PPE: `protocol/md/workflows/media_disposal.md`.
- Project framing: `documents/2026-06-22_village_and_description.md`; `README.md`.

---

*Log: 2026-06-30 — Drafted by Alex + Claude from repo sources. Framing confirmed with Alex: check-in type = Whole Organism; trigger = not on White List; scope = bacteria only (phages deferred); containment = BSL-2; measures = PPE + bleach/autoclave + KGI oversight + aseptic/BSC. Precautionary risk framing per reviewer best-practice; `P. aeruginosa` exclusion stated as fact (ANI), no Risk-Group number asserted. Open decisions logged at top: unsequenced "likely aeruginosa" stocks, IBC documentation, Whole-Organism sub-field mapping.*
