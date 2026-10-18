# Attributions — Prof. Ignacio-Espinoza's answers

Source: `2026-10-18_prof_documents/LooseEndsiGEM.docx`, received 2026-10-18.
Questions: `2026-10-18_pi_contribution_questionnaire.md`.
Transcribed verbatim below, his wording preserved including typos, so that the
Attributions and Safety forms can be filled from one place.

**Unanswered: C1, C2, C3 (people in his lab — Weitao's affiliation, Phoebe,
anyone else) and D1 (Twist — sponsorship vs purchase) and D4 (other sponsors).**
These were the questions we most needed for the Attributions form; ask again.

**Do not paste A2 as written** — it calls the genome circular, our analysis says
linear + 77 bp DTR. See `2026-10-18_prof_documents/README.md`.

---

## A. Software and computational work he did himself

**A1. Ancestral sequence reconstruction and the language-model scoring.**

> CDS_12 was used as a query against the NCBI non-redundant (nr) protein
> database, targeting viral and bacterial sequences as well as metagenome-derived
> sequences. The top 1,000 hits were downloaded and aligned with MUSCLE as
> implemented in SeaView. The alignment was then manually curated to retain the
> regions covered by the extant query sequence. The curated alignment was used to
> build a phylogenetic tree with PhyML (WAG substitution matrix, proportion of
> invariant sites fixed at 0.1, branch support from 100 bootstrap replicates).
>
> Ancestral sequence reconstruction was performed in IQ-TREE using the same WAG
> matrix, with the tree rooted at the midpoint. All ancestral nodes along the path
> from CDS_12 to the root were reconstructed. These are referred to by their
> arbitrary labels (Node 1, 2, 38, 39, 40, 42, 267, 277 and 281), ordered from
> most recent to most ancestral.
>
> To evaluate the "carboxylase-likeness" of the reconstructed ancestral
> sequences, we used ZymCTRL (a conditional protein language model, CTRL/GPT-2-style
> decoder trained on ~37 M EC-annotated UniProt enzyme sequences). Each sequence
> was scored against the EC number expected for a carboxylase in this family (full
> list in the Colab notebook). ZymCTRL returns a perplexity value, which reflects
> how canonical a sequence appears relative to the sequences the model was trained
> on, with lower perplexity indicating a more canonical sequence. More ancestral
> nodes returned lower perplexity scores and therefore resemble canonical
> carboxylase sequences more closely. Subject to the caveats below, we interpret
> this as broader sequence conservation and, tentatively, a broader substrate
> range. We note that reconstructed ancestors are consensus-like by construction,
> which may itself lower perplexity independently of any functional signal.

Code and data for this are now at `code/1018_prof_asr_zymctrl/`.
Node labels 1, 2, 38, 39, 40, 42, 267, 277, 281 are the authoritative naming —
reconcile with how the three ancestral constructs we ordered from Twist are named
in `2026-07-27_twist_construct_order` and `2026-09-10_twist_construct_order_second_set`.

**A2. Reference genome annotation / assembly of 9-2-1 Φ8.** — see warning above.

> Phage DNA was sequenced by Plasmidsaurus (input XX ng) using their shotgun
> metagenomic pipeline (Illumina NovaSeq X, 2 × 150 bp paired-end), yielding
> approximately 20 M read pairs. Reads were subsampled to 50000 which were then
> assembled with megahit with default parameters, producing a single contig of
> 62,339 bp at 140 X mean coverage. The contig terminated in a 77 bp redundancy
> corresponding to the maximum k-mer length used during assembly, indicating that
> the assembly graph closed into a circle; the genome is therefore reported as a
> circular contig after removing the redundant overhang.

**A3. Structural annotation of the virion.**

> In the absence of immediate access to a TEM, we inferred virion morphology
> computationally. Protein structures were predicted for all ORFs [that] were
> annotated as structural using AlphaFold [webserver version] and each model was
> queried against the default databases hosted through Foldseek to identify
> structural [homologues]. The closest structural matches across multiple
> structural proteins, including the major capsid protein, portal and tail
> adaptor, were to **Ralstonia phage GP4 (NC_054964)**, a Bcep22-like podovirus of
> the genus *Gervaisevirus*. On this basis we tentatively assign our phage to the
> Bcep22-like lineage of short-tailed (podovirus-morphology) *Caudoviricetes*. We
> note that morphology was not confirmed experimentally, and that major capsid
> proteins across *Caudoviricetes* share the HK97 fold, so capsid-level structural
> similarity alone carries limited phylogenetic signal; the assignment rests
> chiefly on the tail and adaptor proteins. Comparative analysis further suggested
> a **branched architecture for the receptor-binding apparatus**, in which
> accessory proteins are appended to a central RBP scaffold in a grape-like
> cluster. One of these accessory proteins was independently annotated as a
> depolymerase by our blast based annotation, and is the focus of this study.
>
> (Maybe include the foldseek results)

This closes the open taxonomy item in `project_phage_genome_sequencing`: the
assignment is Bcep22-like *Gervaisevirus*-adjacent podovirus, structural not
terL-based, and explicitly tentative. The "grape-like branched RBP" is what
`phage_groupA.svg` / figure panel B draws.

**A4. Anything else.**

> The most important part was the subsampling of the reads from the phage
> metagenome. Not sure if worth writing about it.

**A5. Compute and software resources.** Authorized acknowledgement, use verbatim:

> The authors acknowledge the Center for Advanced Research Computing (CARC) at
> the University of Southern California for providing computing resources that
> have contributed to the research results reported within this publication.
> URL: https://carc.usc.edu.

## B. His intellectual contribution

**B1.**

> J.C.I.E. proposed the central hypothesis of the project: that the substrate
> range of ancestrally reconstructed proteins acts as a driver of extant host
> range. J.C.I.E. also provided initial guidance directing students toward the
> analysis of receptor-binding proteins (RBPs) from metagenomic datasets, phage
> genome assembly and annotation, and the structure of O-antigen cassettes in
> sequenced bacterial genomes.

**B2.**

> Students led the idea of investigating phage RBPs and have continuously
> suggested methods they have come across from the literature for expression and
> validation of protein expression results.

**B3.** Results he personally checked: "Assembly, and phylogenetics."

**B4.** Scientific direction: "Sounds good as is."

## D. Services and sponsors

**D1. Twist.** Not answered — ask again.

**D2. Illumina phage run 3NKSC3.** "Is also plasmidsaurus (see above)."

**D3. Funding, use verbatim:**

> This work was supported by Keck Graduate Institute (KGI) startup funds to
> J.C.I.E. We also acknowledge Claremont McKenna College (CMC) and Harvey Mudd
> College (HMC) for summer internship stipends supporting Y.C., Y.Y., and X.W.

**D4. Other sponsors.** Not answered.

## E. Administrative

**E1. Safety contact.** "Jasmine Ju, we don't have an approval number yet."
The IBC letter of 2026-10-15 is signed **Jasmine Yu, Chair, IBC, Keck Graduate
Institute** — use the letter's spelling. Status is **conditional approval, no
number**, with a revision due Oct 24.

**E2.** "It looks Good."

---

**Log**

- 2026-10-18 — transcribed from `LooseEndsiGEM.docx`; gaps C1–C3/D1/D4 and the
  A2 topology conflict flagged.
