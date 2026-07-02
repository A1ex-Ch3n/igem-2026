# iGEM 2026 Project Safety Form (Q6–Q28, Steps 3–6) — DRAFT

**Team:** Claremont CA — #6317 · **Form:** Project Safety Form (Q6–Q28) · **Contact:** Chun-Yu Chen
**Form:** https://teams.igem.org/6317/safety/safety-project-form · Preliminary deadline **Jul 1**.
**Companions:** the two Safety Check-In drafts in this folder (Pseudomonas + phage). Keep all three consistent.

> This covers the **full Project Safety Form — Steps 3–6, Q6–Q28** (Step 4's two harm/hazard follow-ups are unnumbered in the form). Copy each **A:** into the matching field; **☑ / ☐** mark recommended checkbox selections.

---

## ⚠️ Decide before you submit

1. **The scope fork that drives Q7 / Q9 / Q11 (and Protein-Design in Q14).** Does your iGEM wet lab **this cycle**:
   - **(a)** stay **computational design + wild-type characterisation** — *drafted default, and consistent with your Check-In forms* → Q7 **No**, Q9 **No**, Q11 **no synthesised DNA**; or
   - **(b)** also **build & test designed RBP constructs** (synthesise RBP genes, express the proteins, or engineer phages) → Q7 **Yes**, Q9 **Yes**, Q11 **IGSC-member synthesis**, and check **Protein Design** in Q14.

   I drafted **(a)**. If the answer is **(b)**, tell me and I'll flip those four answers. **Confirm with your PI** — this is the single most consequential choice on the form.
2. **Q11 synthesis screening:** if your wet lab orders **any** synthesised DNA this cycle — even PCR primers for 16S species-confirmation — pick the **IGSC-member** option and order from an [IGSC](https://genesynthesisconsortium.org/) member so sequences are screened. Only pick "will not use synthesised DNA/RNA" if you genuinely order none.
3. **Q14 AI categories:** I checked **LLM** + **Protein Structure Prediction** (both definite). Also tick **Protein Design** if you use/plan generative design (RFdiffusion/ProteinMPNN-type), **Genetic Prediction** if you count ML gene-finders (Bakta/Prodigal), and **Data Analysis** if you count LLM-assisted analysis. Tell me which apply.
4. **Institution-specific fill-ins (Steps 4–6), marked *[…]* inline:** the **KGI biosafety-officer / IBC name + email** (Q21), the **KGI biosafety-manual link** (Q22), your **safety-training** specifics (Q24), and which institutional measures you actually have (Q25 — accident reporting / access controls). **Most load-bearing:** confirm whether a **formal IBC/BSO** covers this work — "institutional biosafety oversight / IBC" is cited across all three forms, so if it's PI supervision *without* a formal IBC, soften "IBC" to "institutional biosafety oversight" everywhere. One question to your PI settles it.
5. **Live-form mechanics to check:** (a) **verify the Q22 links resolve** before pasting (BMBL / NIH-OSP / iGEM-policies — generated URLs can be stale); (b) **Q23 may be single-select** — it doesn't say "check all that apply," so if it's a radio button, lead with **"Yes, at the iGEM project stage."**

---

## STEP 3 — About Your Project

### Project Goal

**Q6. Describe the goal of your project: what is your engineered organism (or other synthetic biology product, system, or tool) supposed to do?**

**A:** *Phagenomics* is a computational pipeline — a synthetic-biology **tool**, not an engineered organism — that predicts and designs phage host range from genome sequence. Given a target bacterium's genome, we (1) annotate it and extract the surface-exposed proteins a phage could bind — TonB-dependent receptors, porins (OmpA/OmpW/OprD-family), TolC, LptD, FadL, Tsx, ushers, flagellin, and pilin; (2) fold complexes of candidate phage **receptor-binding proteins** (RBPs — the tail-fibre/spike proteins phages use to recognise a host) against those receptors with AlphaFold2-Multimer/ColabFold, ranking likely receptor–RBP pairs by interface confidence (ipTM / interface-PAE); and (3) benchmark the predictions against phages we isolate from the same soil as the target strains. The aim is to make phage host range something we can **design computationally** rather than find by trial-and-error screening — initially for environmental *Pseudomonas*, with longer-term applications in agriculture and phage therapy.

### Organisms

**Q7. Will you be engineering whole organisms, including viruses and cell lines, in your project?**

**A:** ☑ **No** *(current scope — see Decision #1)*. We do not genetically modify any organism, virus, or cell line. The design half is entirely computational (in-silico structure prediction and ranking of RBP–receptor pairs). The wet-lab half works only with **wild-type** material: we isolate naturally-occurring environmental *Pseudomonas* and naturally-occurring bacteriophages from soil, sequence them, and test which phages lyse which hosts. No cloning, transformation, expression vectors, antibiotic selection, or genome editing is performed.

> *Explain how the project is conducted without engineering an organism:* our contribution is a **prediction/design tool** validated against nature. All novelty is in the computational pipeline (receptor mining → structural binding screen → host-range prediction) and in characterising wild isolates + their natural phages. Designed RBP sequences remain **in silico**; none are built into an organism in the current scope.

**Q8. Will you use any other organisms in your project? List organisms, including genus, species, and strain.**

**A:** All organisms are handled as **wild-type**; none are engineered.
- **Environmental *Pseudomonas* sp.** (*P. putida* group; GTDB *Pseudomonas_E* sp013179515; closest sequenced reference *Pseudomonas* sp. CM27, ~99% ANI) — our own soil isolates: strains **9-2-1, 9-6-2, 10-10-2, 8-5-2** (whole-genome sequenced), **_Pseudomonas capeferrum_ 8-10-2**, and ~23 further unsequenced environmental *Pseudomonas* soil isolates (≈28 banked stocks in total). *Use:* culturing, whole-genome sequencing, and as hosts for phage host-range assays. (*P. aeruginosa* is genomically excluded, ~80% ANI — see our Check-In form.)
- **Novel environmental bacteriophages** ϕ3, ϕ5, ϕ6, ϕ8, ϕ9, ϕ10 (not yet taxonomically identified; ϕ8 confirmed lytic on hosts 9-6-2 and 9-2-1) — isolated from the same soil. *Use:* plaque and OD₆₀₀ lysis host-range assays; planned sequencing.
- **Computational inputs only** (public database sequences, never physically handled): ~40 NCBI reference *Pseudomonas*-phage genomes and curated phage-RBP sequences (e.g. phages phiKZ, KPP10, PPpW-4); literature phage-RBP sets from *E. coli*, *S. aureus*, and *K. pneumoniae* phages; *E. coli* K-12 reference outer-membrane receptor proteins (a classification vocabulary); and soil-metagenome protein sets (MG08/MG09).

### Parts & Synthesis

**Q9. Are you planning to make / have you made new parts or substantively changed existing parts in the Registry?**

**A:** ☑ **No** *(current scope — see Decision #1)*. We are not making or substantively modifying Registry parts. Our designed RBP sequences exist only as **computational designs** at this stage — none have been synthesised, cloned, or deposited as parts.

**Q10. Could any of your parts be hazardous on their own and/or in the context of your project?**

**A:** ☑ **Yes** *(in the project context — see below)*. The parts themselves — phage **receptor-binding proteins** (tail-fibre/spike binding domains) — are **not toxins and not hazardous on their own**. But because our project designs the very part that determines a phage's **host range** (the targeting component of a bacteria-killing agent), host-range-determining parts are **inherently dual-use in the context of the project**, and we treat them that way. We manage this by keeping all RBP redesign **computational and hypothetical** (nothing built into an organism in the current scope), **never retargeting phages toward pathogens** or expanding host range experimentally, and working under PI and institutional biosafety oversight per iGEM's policies. *(If you prefer, this can instead be a qualified **No** — "no parts exist yet (Q9), and RBPs are not hazardous on their own" — but keep this dual-use qualifier so it stays consistent with Q14. Confirm the Yes-vs-qualified-No call with your PI.)*

**Q11. What synthesis screening is done for the DNA/RNA that your team will use?**

**A:** ☑ **We will not use any synthesized DNA/RNA** *(current scope — see Decisions #1 and #2)*. Our wet lab extracts and sequences DNA from wild isolates; it does not order synthesised genes, and the designed RBPs are not synthesised in the current scope.
> **If that changes** (you order PCR primers, gBlocks, or designed RBP genes), switch to **"order our DNA/RNA from a company, member of the IGSC"** and order from an IGSC member so the sequences are screened.

### Experiments & Chemicals

**Q12. What experiments will you do with your organisms and parts?**

**A:** **Wet-lab (all wild-type):**
- Soil sampling at the California Botanic Garden; metagenomic DNA extraction (community DNA → shotgun sequencing of sites #8/#9).
- Selective enrichment and isolation of environmental *Pseudomonas* (*P. putida* group; strains 9-2-1/9-6-2/10-10-2/8-5-2/8-10-2 + further soil isolates) on *Pseudomonas* Minimal Media → *Pseudomonas* Isolation Agar; liquid culture; glycerol banking.
- Genomic DNA extraction and Oxford Nanopore whole-genome sequencing (outsourced to Plasmidsaurus); assembly + annotation.
- Isolation of novel soil bacteriophages (ϕ3/5/6/8/9/10) by enrichment and 0.22 µm filtration; **plaque assays** and **OD₆₀₀ lysis-challenge assays** mapping which phages lyse which *Pseudomonas* hosts; iterative plaque re-isolation.

**Dry-lab / in silico (no physical parts):**
- Mine surface-receptor proteins from annotated genomes; build a literature phage-RBP database; predict RBP–receptor binding with AlphaFold2-Multimer/ColabFold ranked by ipTM.
- RBP sequences taken from other organisms' phages (e.g. phiKZ, KPP10) and *E. coli* reference receptor proteins are used **only as computational inputs** — analysed as database sequences, never synthesised or physically handled.

No experiments involve human/animal cells, pathogens, or genetically modified organisms.

**Q13. Are you using some kind of hazardous chemicals in your project?**

**A:** ☑ **Yes.** As in most microbiology labs, we handle: **sodium hypochlorite (bleach)** for decontamination (corrosive/oxidiser); **ethanol / isopropanol** (flammable) for surface cleaning and nucleic-acid work; the **guanidinium-salt lysis/binding buffers** in the Zymo Quick-DNA kit (harmful — and note the standard incompatibility: guanidinium waste must **never** be combined with bleach, which can release toxic gas); and media components such as **ferric chloride** (PMM). We keep and consult the Safety Data Sheets for these reagents. No highly toxic, explosive, or select-agent chemicals are used.

### AI Tools

**Q14. Is your team using or planning to use an AI tool for the development of your project?** ☑ **Yes.**

**Which category of AI tool(s)?** ☑ **Large Language Models** (e.g. Claude) · ☑ **Protein Structure Prediction Tools** (AlphaFold2-Multimer / ColabFold). *(See Decision #3 for the optional additions: Protein Design, Genetic Prediction, Data Analysis.)*

**What risks do you foresee from these AI tools, and what measures will you take to identify and mitigate them?**

**A:** Our project uses AI in two main ways, each under human oversight:
1. **Large Language Models (e.g. Claude)** — for writing/reviewing analysis code, organising data, and drafting documentation (including these safety forms). *Risk:* LLMs can hallucinate, produce subtly wrong code, or misstate facts. *Mitigation:* every AI output is reviewed by team members and our PI; we verify AI claims against primary data rather than trusting the model (e.g. species identity is decided by ANI/sequencing, not an LLM summary); AI is an assistant, never the authority for any scientific or safety decision.
2. **Protein structure-prediction tools (AlphaFold2-Multimer / ColabFold)** — to predict phage RBP–receptor binding. *Risk:* over-confidence in predicted interactions; the ipTM score is a heuristic, not experimental proof, with known blind spots (e.g. it cannot model protein-vs-polysaccharide receptors). *Mitigation:* predictions are treated as **hypotheses to be tested** by wet-lab plaque/host-range assays; we report confidence scores honestly and never use a prediction as the sole basis for a wet-lab or biosafety decision.

**Dual-use / biosecurity:** AI-assisted design of phage host range is a dual-use capability. *Mitigation:* no wet-lab engineering of phage host range is performed — all redesign is computational and hypothetical; we do not retarget phages toward pathogens or expand host range experimentally; all work is under PI and institutional biosafety oversight, following iGEM's safety policies. **Data:** we use only public sequences and our own environmental isolates — no human or otherwise sensitive data.

---

## STEP 4 — Identifying Risks

**Q15. Are there any hazards presented by the organisms, parts, chemicals, or experiments you described in Part 3?**

**A:** ☑ **Yes.** Our project carries the ordinary hazards of a microbiology + molecular-biology lab. We identify them by category here (the management measures go in Part 6 / are detailed in our Safety Check-In forms):

- **Organisms — environmental *Pseudomonas* isolates (*P. putida* group).** Wild soil bacteria, not fully characterised at the moment of isolation; the genus *Pseudomonas* contains opportunistic pathogens, so we treat all isolates at **BSL-2** as a precaution. Whole-genome sequencing places ours in the non-pathogenic *P. putida* group and **excludes *P. aeruginosa*** (~80% ANI); a subset of banked stocks is not yet species-confirmed and is held at the same precautionary level.
- **Organisms — novel environmental bacteriophages.** Phages infect only bacteria, so direct hazard to people is minimal; the residual points are that they are **unsequenced** (lytic-vs-temperate lifestyle and gene content unconfirmed) and could in principle **transduce** DNA between bacteria. Propagated only on our non-pathogenic hosts.
- **Parts — designed receptor-binding proteins (RBPs).** Not toxins and not hazardous on their own, but **dual-use in the project context** because they determine phage host range; managed by keeping all redesign computational and never retargeting phages toward pathogens (see Q10).
- **Chemicals.** Sodium hypochlorite (bleach; corrosive/oxidiser), ethanol/isopropanol (flammable), the guanidinium-salt buffers in our DNA kit (harmful — and **must never be mixed with bleach**: toxic-gas risk), and media components such as ferric chloride. SDS kept and consulted for each.
- **Experiments.** Routine microbiology exposure routes — aerosols/splashes during culturing and pipetting, sharps, and surface contamination.

No experiments involve human or animal cells, select agents, or genetically modified organisms.

**Q15 (cont.) — For each hazard above, how could harm occur? (1–3 sentences each)** *(unnumbered follow-up to Q15 in the form)*

**A:**
- **Environmental *Pseudomonas* isolates.** A team member could be exposed by aerosol, splash, or contact during culturing or pipetting; although our sequenced isolates are non-pathogenic *P. putida*-group organisms, a not-yet-species-confirmed isolate could in principle be an opportunistic pathogen and cause infection, especially in an immunocompromised person. *(exposure)* A viable culture could also escape on contaminated gloves, glassware, or waste and re-enter the environment — low-consequence here, since the organisms came from local soil, but still an unwanted release of an incompletely-characterised strain. *(release)*
- **Novel bacteriophages.** Phages cannot infect human cells, so the realistic harm is genetic rather than infectious: because they are unsequenced, one could prove temperate or carry an accessory gene, and propagating it could **transduce** or mobilise DNA — in the worst case a resistance or virulence gene — between bacteria. This is mitigated by propagating only on our non-pathogenic hosts, which are not known to carry such genes. *(release / transduction)*
- **Designed receptor-binding proteins (RBPs).** Our computational designs specify the part that sets a phage's host range; if such a design were built and misused, it could **retarget** a phage toward a new or higher-risk host such as a pathogen — turning a precision-targeting tool into a means of directing a bacteria-killing agent at an unintended target. This is why we keep all redesign computational and never retarget toward pathogens. *(dual-use)*
- **Chemicals.** A team member could be harmed by direct contact, splash, or inhalation — bleach causing skin/eye/respiratory irritation, ethanol or isopropanol igniting near an open flame, or, most seriously, the guanidinium-salt DNA-kit waste being mixed with bleach and releasing toxic gas. *(exposure)*
- **Experiments / physical procedures.** The procedures create exposure routes independent of the specific agent: centrifugation, vortexing, and pipetting can generate aerosols; glassware and pipette tips can cause cuts; and inadequate surface decontamination can leave a viable culture that is later touched or ingested. *(exposure)*

**Q15 (cont.) — What hazards are presented? (check all that apply)** *(unnumbered follow-up to Q15)*

**A:**
- ☑ **Human health or safety hazards** — hazardous chemicals (bleach, ethanol/isopropanol, guanidinium-salt buffers) and the BSL-2-handled environmental *Pseudomonas* (opportunistic-pathogen risk from not-yet-species-confirmed isolates).
- ☑ **Environmental hazards** — a viable culture or phage could escape; **low-consequence** (locally-sourced, non-invasive soil organisms — release returns them to their source) but real, and some banked stocks are not yet species-confirmed.
- ☑ **Dual-use hazards** — we design the host-range-determining part of a bacteria-killing agent; the knowledge could be misused to retarget phages (managed by keeping redesign computational, no retargeting toward pathogens).
- ☑ **Other hazards to team members in the lab** — physical/procedural: sharps and glassware cuts, autoclave/flame burns, aerosols from centrifugation/vortexing.
- ☐ *Other hazards beyond the laboratory* — **not checked** (no community deployment; only purified DNA, not live organisms, is shipped to the sequencing vendor; environmental release is box 2, dual-use is box 3).

*Judgment calls: box 2 (Environmental) checked as low-but-real for consistency with the harm pathways above; box 4 (Other-in-lab) checked to flag physical hazards — leave it if you consider those covered by box 1's "safety."*

---

## STEP 5 — Anticipating Future Risks

**Q16. Imagine your project fully developed into a real product. How would people use it? (check all that apply)**

**A:** ☑ **In agriculture / on a farm** · ☑ **To be used in the human body, or in food**
*(Optional: ☑ **In the natural environment** — agricultural phage application is an open field release; check it if you want that explicit. Do **not** check "foundational / no specific application" — you do have applications in mind.)*
> **Describe:** Fully developed, *Phagenomics* is a design platform whose output is custom phages (or phage RBPs) that kill a chosen bacterium on demand. Its two real-world uses follow from our stated aims: **(1) agriculture** — designed phages applied to crops to control *Pseudomonas* and other bacterial plant pathogens (biocontrol); and **(2) phage therapy** — designed phages administered to treat bacterial infections in humans (and potentially animals). The pipeline itself is a foundational method; these downstream applications require the phage-engineering and release steps that are out of scope during the competition.

**Q17. If permitted, would continued development require release beyond containment? (check all that apply)**

**A:** ☑ **Yes, open release in the environment** (agricultural field application) · ☑ **Yes, release into a human or animal body** (phage therapy)
> **Describe:** A fully-developed product would leave containment in two ways: applying designed phages to crops in open fields (open environmental release) and administering them into a human or animal body (therapeutic release). Both need approvals we do not undertake during iGEM — in the US, USDA-APHIS / EPA for agricultural biocontrol and field release, and FDA (IND / biologics) for phage therapeutics, plus institutional biosafety committee (IBC) review and, for clinical work, IRB / ethics approval. All current work stays fully contained in the lab.

**Q18. Has your team discussed how any of the listed bad outcomes relate to your project? (check all that apply)**

**A:** Recommended (discussed through this safety work, and matching the outcomes you identify in Q19 below): ☑ **Harm to human health and safety** · ☑ **Harm to agricultural animals / crops** · ☑ **Harm to the environment (wild plants and animals)** · ☑ **Reducing global, national or health security**.
*Keep **Q18 ⊇ Q19**: identifying an outcome as possible in Q19 **is** a discussion of it, so anything ticked there should be ticked here. Optional (tick only if genuinely discussed): ☐ Breaking norms about engineering biology · ☐ Creating / reinforcing social inequities (e.g. phage-therapy access). Harm to materials/infrastructure — not applicable.*

**Q19. Could your project potentially lead to any of those bad outcomes?**

**A:** ☑ **Yes.** Honestly: our work is dual-use (host-range design), our organisms and phages could be released or spread, and a fully-developed product would act beyond containment — so some risk exists, as it does for virtually all biotechnology. The point (per the form) is that we recognise it and manage it: computational-only redesign, no pathogen retargeting, BSL-2 containment, PI / IBC oversight, and the regulatory steps in Q17 before any real-world use.

**Q19 (cont.) — What bad outcomes could your project potentially lead to? (check all + comment)**

**A:** ☑ **Harm to human health and safety** · ☑ **Harm to agricultural animals / crops** · ☑ **Harm to the environment (wild plants and animals)** · ☑ **Reducing global, national or health security**
*(Optional, team's call: ☐ Breaking norms about engineering biology — host-range modification is a norm-sensitive area; ☐ Creating / reinforcing social inequities — access to phage therapy / ag products. Not applicable: materials/infrastructure; Other.)*
> **Comment:** The headline concern is **security**: our host-range-design capability is dual-use and could be misused to retarget phages toward pathogens or other targets. **Health, agricultural, and environmental** harms could follow from the eventual products rather than the current work — a phage biocontrol agent could have non-target effects on beneficial or crop-associated bacteria, and released, self-replicating phages could perturb environmental bacterial communities. These are properties of a *fully-developed product*; the current computational + wild-type work does not cause them, and we manage them by keeping redesign computational, never retargeting toward pathogens, and gating any real-world use behind the regulatory review in Q17.

**Q19 (cont.) — How might those bad outcomes come to pass? (check all that apply)**

**A:** ☑ **Accidental exposure to a hazardous organism or chemical** (lab exposure to chemicals or the BSL-2 *Pseudomonas*) · ☑ **Accidental release of an organism or part into the environment** (a viable culture or phage escaping) · ☑ **Combining the results of the project with other technologies** (our computational designs become actionable only when combined with DNA synthesis / phage engineering — the main route by which the dual-use risk is realised) · ☑ **Deliberate misuse by someone intending to cause harm** (misusing host-range design to retarget phages)
*(Optional: ☐ Other unintended consequences — e.g. non-target ecological effects, or bacteria evolving phage resistance.)*

**Q20. If fully developed, could any of your engineered organisms or parts spread autonomously in the environment?**

**A:** ☑ **Yes — autonomous environmental spread of one or more of our organisms or parts is possible.** (As in Q16/Q17, this describes the *hypothetical fully-developed product*; current work engineers nothing and is fully contained.) Bacteriophages are self-replicating agents: they amplify on their host bacteria and spread through host populations wherever the host is present, so a fully-developed phage product could spread autonomously. The natural limit is **host specificity** — a phage only replicates on its target bacterium, which is precisely the property our pipeline designs — but any real deployment would still require containment / monitoring and the regulatory review in Q17. (Our designed RBP *parts* alone — proteins — cannot replicate or spread; it is the phage carrying them that can.)

> **Q20 — Describe how this could happen:** A phage could enter the environment accidentally (contaminated waste, equipment, or clothing) or, in a fully-developed product, intentionally (agricultural field application). Once present it replicates on any of its host bacteria in the environment and propagates through that host population, spreading beyond the point of release for as long as susceptible hosts are available. Spread is naturally bounded by **host specificity** (the phage amplifies only on its target bacterium) and, for our current wild phages, by the fact that their hosts are common soil organisms already present locally. We use **no engineered biocontainment** (kill switch / auxotrophy) because the project currently engineers nothing; a real deployment would add containment and monitoring and be gated behind the regulatory review in Q17.

---

## STEP 6 — Managing Risks

**Q21. Who are the experts (other than your supervisors) supporting you in managing risks? Who would you go to if you found a hazard?**

**A:** Beyond our PI, we would turn to:
- The **Keck Graduate Institute (KGI) biosafety officer / Institutional Biosafety Committee (IBC)** — our first point of contact for any biosafety hazard, since our wet-lab work is carried out at KGI. *[Insert the KGI BSO / IBC name + email.]*
- The **iGEM Safety & Security Committee** (safety@igem.org) — for iGEM-specific guidance and the Check-In process we are already using.
- Experienced **KGI microbiology / phage collaborators and co-mentors** (e.g. the co-authors on our genome-sequencing work). *[Insert names / contacts if you wish to list them.]*

*→ The specific KGI biosafety-officer name + email is the one contact iGEM most wants here — please fill it in.*

**Q22. What safety and security rules or guidance cover your work?**

**A:**
- **US / national:** the CDC–NIH *Biosafety in Microbiological and Biomedical Laboratories* (**BMBL**, 6th ed.; https://www.cdc.gov/labs/bmbl/) — the standard reference for our BSL practices; the *NIH Guidelines for Research Involving Recombinant or Synthetic Nucleic Acid Molecules* (https://osp.od.nih.gov/) — noting our current work is non-recombinant; and OSHA laboratory chemical-hygiene standards. Select-agent regulations do not apply (no select agents).
- **Institutional (KGI):** KGI's laboratory biosafety manual, IBC policies, and chemical hygiene plan. *[Insert the KGI biosafety-manual / IBC link.]*
- **iGEM:** the iGEM Safety & Security Policies, including the White List and Check-In process (https://responsibility.igem.org/safety/policies).

**Q23. Will your project need extra support or review? (beyond normal institutional review)**

**A:** ☑ **Yes, at the iGEM project stage** — we are already engaging the iGEM Safety & Security Committee through Check-In forms (for our *Pseudomonas* isolates and our phages) and rely on KGI institutional biosafety review.
☑ **Yes, if developed further for real-world use** — as in Q17, agricultural or therapeutic use would require regulatory review (EPA / USDA-APHIS / FDA), field- or clinical-trial design support, and ethics / IBC review.

**Q24. Have your team members received safety and/or security training?**

**A:** ☑ **Yes, we have already received safety and/or security training** — institutional laboratory-safety / BSL-2 training is required to work in our KGI lab. *[Confirm: name the training (e.g. KGI lab-safety onboarding, BSL-2, chemical hygiene) and that every member has completed it; if some still need it, add "and plan to for remaining members."]*

**Q25. What laboratory biosafety and biosecurity measures are you using? (select all relevant)**

**A:** Confident (evidenced in our work):
- ☑ **Personal Protective Equipment (PPE)** — gloves, lab coat, eye protection.
- ☑ **Waste management system** — media/agar autoclaved; cultures, plates, lysates, and liquid waste bleach-treated and/or autoclaved before disposal.
- ☑ **Inventory controls** — a detailed inventory of every bacterial / phage / DNA item by storage location and status (`data/dna_extraction_inventory.md`).
- ☑ **Additional containment** — we work at **BSL-2** as a precaution for uncharacterised environmental *Pseudomonas*, above the BSL-1 a confirmed non-pathogen would require.

Likely institutional — *confirm with your PI / KGI*: ☑ **Accident reporting** · ☑ **Physical access controls**.

Check only if your lab has them: ☐ Data access controls · ☐ Lone Worker / Out-of-Hours policy · ☐ Medical surveillance (probably unnecessary for RG1-type environmental organisms).

**Q26. What other actions have you taken to manage risks? (select all)**

**A:** Confident:
- ☑ **Other consulting with iGEM** — we are submitting Check-In forms for our *Pseudomonas* isolates and our phages.
- ☑ **Deciding not to do an activity** — we deliberately keep all phage / RBP redesign **computational**: no engineering of organisms, no retargeting of phages toward pathogens or experimental host-range expansion, and no infection experiments.
- ☑ **Consulting with other experts** — KGI biosafety officer / IBC. *[Confirm you've done / will do this.]*
- ☑ **Crafting a responsible communication plan** *(recommended given your dual-use nature)* — because host-range design is dual-use, we are mindful about how we present methods (highlighting biosafety measures; not publishing a turnkey pathogen-retargeting protocol). *[Adopt / confirm.]*

Check if applicable: ☐ Project-specific safety training · ☐ iGEM Values & Risks workshop · ☐ Consulting with stakeholders · ☐ Evaluating countermeasures · ☐ Modifying experimental design.

> **Comment (how these apply):** Our central risk-management choice is to keep the project at the **computational-design + wild-type-characterisation** stage, which removes the engineering, synthesis, and release hazards entirely for now. On top of that: BSL-2 containment, PPE, aseptic technique, and bleach/autoclave waste treatment manage day-to-day exposure and release; the inventory tracks every organism and extract; the iGEM Check-Ins and KGI biosafety oversight give external review of the dual-use and organism-identity questions; and our decision not to engineer or retarget, plus a responsible-communication posture, manages the dual-use risk directly.

**Q27. Summary — how will these actions, expert support, rules, training, and procedures manage your project's risks?**

**A:** We match each identified risk to a concrete control:
- **Biological exposure / uncharacterised-organism risk** → all isolates handled at **BSL-2** under the CDC-NIH BMBL framework, with PPE and aseptic technique, and **whole-genome sequencing** to confirm identity (which placed ours in the non-pathogenic *P. putida* group and excluded *P. aeruginosa*); not-yet-confirmed stocks stay at the precautionary level pending sequencing.
- **Chemical hazards** → SDS on file for bleach, ethanol/isopropanol, and the guanidinium DNA-kit buffers, with the guanidinium–bleach incompatibility explicitly flagged; standard chemical hygiene.
- **Environmental release / autonomous phage spread** → media and waste autoclaved and/or bleach-treated before disposal; organisms are locally-sourced and non-invasive; no engineered biocontainment is claimed because nothing is engineered, and any future release would be gated behind EPA / USDA / FDA review.
- **Dual-use** → all redesign kept computational, no retargeting toward pathogens, iGEM Check-Ins submitted, KGI biosafety oversight, and a responsible-communication posture.
- **Physical lab hazards** → institutional lab-safety training, accident reporting, and standard sharps / flame / autoclave practice.
Together, institutional (KGI IBC / BSO) and iGEM (Safety Committee, Check-Ins) oversight provide external review, while our deliberate scope choice — computational design plus wild-type characterisation, no engineering — keeps the project's real footprint low-risk and fully contained.

**Q28. Is there anything else you would like us to know? (optional)**

**A:** Two things we want to be transparent about: (1) a subset of our banked environmental stocks was **presumptively labelled "likely *P. aeruginosa*"** from selective-media morphology before sequencing; the one such stock we have since sequenced turned out to be *P. capeferrum* (a non-pathogen), and we will species-confirm the rest — we would welcome the committee's guidance on how to declare them in the meantime. (2) Our project is explicitly **dual-use** (making phage host range designable), and we have tried to be forthright about that throughout rather than minimise it; we keep all redesign computational and are glad to discuss our responsible-communication approach. We are submitting companion Check-In forms for the *Pseudomonas* isolates and the phages.

---

*Log: 2026-06-30 — Drafted Step 3 (Q6–Q14) by Alex + Claude from repo sources, consistent with the two Safety Check-In drafts (same organisms; no engineering; BSL-2; P. aeruginosa excluded). Q7/Q9/Q11 answered on the current "computational + wild-type" scope, with the (a)/(b) scope fork flagged as Decision #1. Q10 answered **Yes-with-mitigation** (RBPs not hazardous alone, but host-range-determining parts are dual-use in project context) to stay consistent with Q14, per advisor review; qualified-No offered as the PI's alternative. Q14 discloses LLM (Claude) + AlphaFold/ColabFold use with human-in-the-loop, dual-use, and data-privacy mitigations. Step 4 added — Q15 (hazards Y/N + comment) plus its two **unnumbered** follow-ups (harm pathways; hazard-category checklist). Step 5 (Q16–Q20) added — future use (agriculture + human body), release-beyond-containment (Yes: open-env + human/animal, with US regulatory notes), bad-outcome conversations (health / environment / security recommended), could-lead-to-bad-outcomes = **Yes**, autonomous spread = **Yes** (phages self-replicate, limited by host specificity). Q19 detail added — outcomes = health / ag / environment / security; pathways = accidental exposure / accidental release / combining-with-other-tech / deliberate-misuse — and Q20 "describe how" added (host-specificity limit, no engineered biocontainment, regulatory gating). Q18 aligned to the same four outcomes (Q18 ⊇ Q19). Numbering note: the form's Q16–Q20 are the Step-5 questions, so the Step-4 harm-pathway + hazard-category questions are unnumbered follow-ups to Q15 (relabeled to avoid a clash). Step 6 (Q21–Q28, Managing Risks) added — experts/rules/extra-review/training/measures/summary; containment framed as BSL-2 "additional containment" + the deliberate no-engineering choice (no kill-switch claimed, per advisor); institution-specific items (KGI BSO contact + manual link, training specifics, accident-reporting/access controls) left as clearly-marked placeholders for the team to fill. **The full Project Safety Form (Q6–Q28) is now drafted.**\*
