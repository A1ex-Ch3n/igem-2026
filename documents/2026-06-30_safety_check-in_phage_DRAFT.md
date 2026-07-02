# iGEM 2026 Safety Check-In — environmental bacteriophages (DRAFT)

**Team:** Claremont CA — #6317 · **Check-In type:** Whole Organism or Cell Line · **Contact:** Chun-Yu Chen
**Form:** https://teams.igem.org/6317/safety/safety-check-in-form (submit as a **second** Check-In)
**Companion:** this is the phage counterpart to [`2026-06-30_safety_check-in_pseudomonas_DRAFT.md`](2026-06-30_safety_check-in_pseudomonas_DRAFT.md) (the bacterial hosts).

> Copy each **A:** block into the matching field. Same precautionary posture as the bacteria form. A bacteriophage infects only bacteria — no infectivity for humans/animals/plants — so this is intrinsically the lower-risk of the two check-ins, but the phages are wild, unsequenced, and not on the White List, so they get their own review.

---

## ⚠️ Decide these before you submit

1. **Risk Group of a phage (the one genuinely new judgment call).** iGEM assesses a phage's risk through its **host and gene content**, not its (minimal) intrinsic hazard to people. Your host is declared **Risk Group 2** (precautionary) and your phage is **unsequenced** and handled at **BSL-2 on that host**, so the coherent, parity-preserving answer is **Risk Group 2**, matching the host — exactly as the bacteria form does. (Declaring the phage RG1 while handling it at BSL-2 re-introduces the "why the extra containment?" mismatch the bacteria form deliberately avoids, and a reviewer reading both forms would question a bacteria-RG2 / phage-RG1 split.) **Risk Group 1** is defensible *in isolation* — a phage of a non-pathogen is genuinely low-hazard — so it stays as the honest note. **Confirm the final call with your PI / KGI biosafety officer.**
2. **Lifestyle + gene content are unknown until you sequence.** The phages are **not sequenced**, so you cannot yet state whether any are temperate (lysogenic — able to integrate and carry genes) vs strictly lytic, or whether they carry toxin / AMR / virulence genes. The draft **discloses this** and commits to screening the genomes before any application-oriented work. Keep that commitment in.
3. **Unsequenced host in host-range testing.** Φ8 host-range/OD assays included **9-9-2**, one of the not-yet-sequenced "likely *P. aeruginosa*" stocks (see the bacteria form's Decision #1). The draft notes this honestly and cross-references that form. Have your PI sign off on the shared public wording.
4. **BSL-2 / IBC documentation** and **Whole-Organism sub-field mapping** — same two notes as the bacteria form (cite the KGI IBC number if one exists; map the Organism description onto whatever identity fields the Whole-Organism branch shows).

---

## Contact Info

**Q: Who from your team should be contacted about this form?**

**A:** Chun-Yu Chen (Claremont CA, team #6317).

---

## Check In Description

**Q: What kind of Check In are you submitting?**

**A:** ☑ **Whole Organism or Cell Line** — novel environmental bacteriophages isolated by our team from soil.

**Q: How does this organism fit into your project goals? (1–3 sentences)**

**A:** Our project, *Phagenomics*, designs phage receptor-binding proteins (RBPs) to bind a target bacterium's surface receptors, so that phage host-range becomes something we design rather than screen for. These soil phages — isolated from the same site as our *Pseudomonas* hosts — are the empirical other half of that pipeline: they are the actual phages whose host-range we aim to predict, and once sequenced they supply real RBP sequences from phages that infect our own strains, the ground truth our computational designs are benchmarked against.

**Q: Why are you checking in this organism?**

**A:** ☑ **We saw that it's not on the White List.** These are novel, wild bacteriophages we recovered from the environment; they correspond to no White List entry, and they are propagated on the environmental *Pseudomonas* isolates we are also checking in (companion form).

---

## Organism description

*(Map onto the Whole-Organism branch's identity fields.)*

**Identity.** Wild environmental **bacteriophages**, not genetically modified. We prepared **six** soil phage enrichments/filtrates, designated **ϕ3, ϕ5, ϕ6, ϕ8, ϕ9, ϕ10** (named by soil site). The one with **confirmed lytic activity** is **ϕ8**, plaque-purified on our hosts **9-6-2** and **9-2-1** (both among our whole-genome-sequenced, non-pathogenic isolates). The phages **have not been sequenced**, so their family/taxonomy and replication lifestyle are not yet characterised; they are *presumed lytic* — they form clear plaques, which is consistent with but does not prove a lytic lifestyle (lysogeny can only be ruled out by sequence).

**Host range.** The hosts are our own environmental *Pseudomonas* sp. (*P. putida* group; closest reference *Pseudomonas* sp. CM27; ***P. aeruginosa* excluded by ~80% ANI** — see companion bacteria form). Host-range testing (plaque assays + OD₆₀₀ lysis-challenge) has also included some **not-yet-sequenced** stocks, e.g. **9-9-2** — one of the presumptively-labelled "likely *P. aeruginosa*" stocks disclosed in the bacteria form. We have **not** tested these phages against a confirmed pathogen and do not intend to expand their host range toward one.

**Source.** Soil enrichments (1 g California Botanic Garden topsoil + LB broth, sites #3/5/6/8/9/10), propagated on our *Pseudomonas* isolates, then clarified by centrifugation and **0.22 µm filtration**; working lysates stored at 4 °C in phage buffer.

**How it is used.** Plaque assays (soft-agar overlay) and OD₆₀₀ lysis-challenge assays against *Pseudomonas* lawns to detect and map host range; iterative plaque re-isolation to confirm single-phage origin; and (planned) amplification → DNA extraction → whole-genome sequencing to identify each phage and read its RBPs, which then feed the computational pipeline.

**Q: What Risk Group is this organism?**

**A:** ☑ **Risk Group 2** *(see Decision #1)*, matching the host. iGEM assesses a phage's risk through its host and gene content: our phages are **unsequenced** (lifestyle and gene content not yet confirmed) and are propagated at BSL-2 on our environmental *Pseudomonas*, which we declare **Risk Group 2** as a precaution — so the phage tracks the same level. Their intrinsic hazard to people is genuinely minimal (bacteriophages infect only bacteria, and *P. aeruginosa* is excluded by sequencing), which is why **Risk Group 1** is a defensible alternative in isolation. *→ Confirm the final call with your PI / KGI biosafety officer.*

---

## Identifying and managing risks

**Q: What risks have you identified from this organism?**

**A:** A bacteriophage has **no direct infectivity for laboratory workers** — it replicates only in bacteria — and ours are propagated on non-pathogenic environmental *Pseudomonas*, so the baseline hazard is low. The phage-specific risks we take seriously are: (1) **Transduction** — phages can package and transfer host DNA between bacteria, so in principle a phage could move genes (including, hypothetically, resistance or virulence genes) from one strain to another; our hosts' virulence/AMR gene content has **not yet been assessed** (see companion form), and we do not co-culture our phages with any pathogen. (2) **Unknown lifestyle** — because the phages are **not sequenced**, we cannot yet confirm whether any are temperate (lysogenic, able to integrate and carry accessory genes) rather than strictly lytic; we presume lytic (clear plaques) but treat this as unconfirmed. (3) **Unknown gene content** — we have not screened for phage-encoded toxins, integrases, or AMR/virulence determinants. (4) **Host range** — not tested against pathogenic *Pseudomonas*; host-range testing has included some not-yet-species-confirmed stocks (see Decision #3). Standard lab-exposure routes (aerosols/splashes, sharps, contamination) apply to the bacterial cultures used to grow the phages.

**Q: What measures have you put in place to manage the risks?**

**A:** All work is carried out at **Biosafety Level 2** at Keck Graduate Institute under PI **Dr. J. Cesar Ignacio-Espinoza** and KGI institutional biosafety oversight *[confirm IBC approval / registration number]* — the same containment as the bacterial hosts, which govern the phages' handling. Specifically:
- **Propagation only on characterised, non-pathogenic hosts** — our own environmental *Pseudomonas* isolates; the phages are never amplified on a known pathogen.
- **Physical clarification:** phage lysates are 0.22 µm-filtered to remove host cells.
- **Containment & PPE:** aseptic technique in / adjacent to a biosafety cabinet or flame; gloves, lab coat, eye protection.
- **Decontamination & disposal:** all media/agar autoclaved before use; cultures, plates, soft-agar overlays, lysates, filtrates, and contaminated consumables are bleach-treated (~10%) and/or autoclaved before disposal.
- **No genetic modification** of the phages — handled strictly as wild environmental isolates.
- **No host-range expansion** toward pathogens.
- **UNDONE / planned precaution:** whole-genome sequence the phages and screen for a temperate lifestyle (integrases), toxins, and AMR/virulence genes; report the result before any application-oriented work.

**Q: Are there alternative ways to achieve your project goals that would present less risk?**

**A:** The lower-risk alternative is to work only with well-characterised reference *Pseudomonas* phages from a public collection (indeed our *computational* pipeline already uses ~40 NCBI reference *Pseudomonas*-phage genomes and 36 curated phage-RBP probes *in silico*, with no lab handling). We considered this but retained the novel soil phages for the wet lab because the project's aim — predicting and designing host-range **from genome sequence** — needs phages matched to our own sequenced host strains to benchmark predictions against real biology; a generic reference phage on a generic host removes that test. We reduce the added risk rather than avoid the work: propagate only on non-pathogenic hosts, 0.22 µm-filter, contain at BSL-2, keep everything wild-type, and sequence the phages to rule out harmful genes before going further.

**Q: Is there anything else you want to tell us?**

**A:** This check-in is the phage companion to our *Pseudomonas* whole-organism check-in; the two share hosts, lab, and containment. Although our project's aim is to make phage host-range *designable*, we want to be explicit that **no current work engineers phage host range in the lab** — all host-range redesign is computational and hypothetical at this stage, and we do not retarget phages toward new or higher-risk hosts. We have **created no genetically modified organism**, and the therapeutic/agricultural applications in our project description are long-term aspirations, not current work. We will update the committee once the phages are sequenced — in particular to confirm their lytic-vs-temperate lifestyle and the absence of toxin/AMR/virulence genes.

---

## Supporting Documents (optional uploads)

> ⚠️ **Everything on this form — text and uploads — is public and indexable.** Attach only what's safe to publish.

- **Phage evidence (optional):** a plaque-assay photo of ϕ8 on 9-6-2 / 9-2-1 (safe to publish), or just describe it in text.
- **Handling / disposal protocol:** the media-disposal protocol (bleach + PPE) — safe to publish.
- **Do not** upload the genome-announcement manuscript or any file with unpublished co-author data (it concerns the bacteria, not these phages, and shouldn't be posted publicly — see the bacteria form).

---

## Evidence appendix (repo sources)

- Phage isolation + plaque record: `scheme/20260604_confirmed_scheme_CLAUDE.md` (Plaque Assay section); `lab_notebook/digitalized/2026-06-01…`, `…-06-02…`, `…-06-03…`, `…-06-04…`, `…-06-05…`, `…-06-10…`.
- Phage inventory (ϕ8 picks on 9-6-2 / 9-2-1, 4 °C): `data/dna_extraction_inventory.md`.
- Lysis-challenge assays: `data/assays/0624_*`, `0625_*`, `0629_*`.
- Host identity (P. putida group; *P. aeruginosa* excluded): companion bacteria form; `documents/strain_phage_conclusions.md`; ANI matrix `code/0623_metagenome_rbp/out_finding_rbps/ani/ani_matrix.csv`.

---

*Log: 2026-06-30 — Drafted by Alex + Claude as the phage companion to the Pseudomonas check-in. Reused the confirmed framing (trigger = not on White List; BSL-2; KGI oversight; PPE + bleach/autoclave + aseptic/BSC). Phage-specific content: Risk Group set to **RG2 to match the host** and preserve parity with the bacteria form (RG1 kept as the honest in-isolation note), per advisor review; risks lead with transduction / unknown-lifestyle / unknown-gene-content / host-range, all disclosed honestly pending sequencing; unsequenced host 9-9-2 in host-range testing cross-referenced to the bacteria form's Decision #1; added an explicit dual-use line (no lab engineering of phage host range) to pre-empt a biosecurity reviewer.*
