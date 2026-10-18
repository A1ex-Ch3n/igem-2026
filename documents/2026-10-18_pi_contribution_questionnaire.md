# Attributions — questions for Prof. Ignacio-Espinoza

**Why we need this.** iGEM's Attributions Form is the formal record of who did what. It is graded on honesty and specificity, and it is where we draw the line between student work and everything that came from outside the student roster. Several of the most important computational results this season — the GH5 phylogeny, the ancestral-state reconstruction, the protein-language-model scoring of the designed variants, the reference annotation of 9-2-1 Φ8, and the AlphaFold/foldseek structural work — are yours, not ours, and the analyses the students did run were shaped by your direction. We would rather over-credit you than have the form say "the team did it."

**What we need from you.** Written answers in this file, in your own words. Length is not limited — the form has no word limit, and vague entries ("helped with the project") are explicitly called out by iGEM as inadequate. Short, concrete sentences naming tools, files, and what you concluded are ideal.

**Deadline.** The form freezes **2026-10-21, 08:00 PDT**. If you can get us anything by **10/20 evening**, we can still enter it carefully.

**How to answer.** Type under each question, or reply by email and we will transcribe. Please do not worry about formatting.

---

## A. Software and computational work you did yourself

iGEM's own definition of the "Software" task is: *developing, implementing, and/or testing computer programs and code for the project.* Related task labels we can also tick for you are **Analysis**, **Data Curation**, and **Visualization**.

**A1. Ancestral sequence reconstruction and the language-model scoring.**
This is the part we most need in your words, because the team did not do it. Please describe:
- the alignment and the phylogenetic inference (which sequences went in, which program, which model);
- the ancestral-state reconstruction (program, which nodes you reconstructed — we received Node1, Node40, Node281);
- the protein language model you used to score how well each designed sequence fits the enzyme class, and what the scores told you;
- anything you tried that did not work.

> *Your answer:*

**A2. Reference genome annotation of 9-2-1 Φ8.**
You produced the assembly and the Pharokka annotation with locus prefix `UUAIURNK_`, which we adopted as the canonical CDS numbering on 2026-07-16 and used for everything afterwards, replacing our own. Please confirm and describe the assembly and annotation steps, including how the 77 bp direct terminal repeat / linear topology was established.

> *Your answer:*

**A3. Structural annotation of the virion.**
Your Colab notebook (`2026-07-13_espinoza_capsid_tube_foldseek.ipynb`) ran AlphaFold plus foldseek against Ralstonia phage GP4 structures, and your AlphaFold3 Server runs on the tail cluster (2026-07-14/15, including a ~15,775-sequence MSA for CDS_0011) are what told us which fragment of CDS_0011 to clone. Please describe what you ran and what you concluded.

> *Your answer:*

**A4. Anything else you wrote or ran.**
Other scripts, notebooks, database queries, or pipelines for this project that we may not know about.

> *Your answer:*

**A5. Compute and software resources you provided.**
The Laguna allocation (`jespinoza_1541`) carried our entire GPU workload — assembly, protein folding, RBP detection. Anything else: licenses, accounts, servers, storage?

> *Your answer:*

---

## B. Your intellectual contribution to the students' analyses

This is the section we are most likely to under-report if you do not write it, because in the repository these analyses appear under a student's name even when the idea, the method, or the interpretation was yours.

**B1. Where did you supply the approach and a student implemented it?**
For each, a sentence on what you proposed is enough. Analyses to consider:
- phage genome assembly and annotation;
- RBP (receptor-binding protein) detection on the metagenomes;
- the receptor-side classification of Pseudomonas outer-membrane proteins;
- the RBP × receptor folding screen — including your judgement that it was not informative, and the reasoning that the receptor is an LPS sugar rather than a protein;
- the taxonomic call (T7-like podophage, Latka group D) and your request that we justify it by synteny;
- the O-antigen / LPS comparison and the resistant-mutant versus parent genome comparison;
- the expression constructs: which fragment, which tag, which variants.

> *Your answer:*

**B2. Where was the student's work their own design?**
Equally useful to us — it tells the judges which parts are genuinely student-led.

> *Your answer:*

**B3. Which computational results did you personally check or validate?**
For example the assembly, the genome topology, the resistant-mutant variant calls, the gel quantification.

> *Your answer:*

**B4. Scientific direction.**
The GH5 depolymerase ancestral-reconstruction hypothesis, withdrawing the CDS_0010 glycosidase call, the virion cartoon, the fluorometer idea, the seven figure requests of 2026-07-27. Please add anything we have missed, and correct anything we have wrong.

> *Your answer:*

---

## C. People in your lab who are not on our roster

iGEM requires everyone who is not on the 2026 student roster to be listed separately as an external contributor, no matter how close they were to the project. We currently plan to list:

- **Rafael Escobar** — selected the ten host isolates on 2026-06-11; the PMM recipe came from his notebook; lab guidance; co-author on the MRA genome announcement.

**C1.** Is that description right, and is his affiliation "graduate student, Ignacio-Espinoza Lab, Keck Graduate Institute"?

> *Your answer:*

**C2.** Did anyone else in your lab — students, postdocs, technicians, collaborators — contribute to this project, including writing or running code? Names, roles, and what they did.

> *Your answer:*

**C3.** Was **Phoebe** a contributor we should list? You mentioned her on 2026-10-05 but we have no record of what she did.

> *Your answer:*

---

## D. Services, sponsors, and orders

**D1. Twist Bioscience.** All of our plasmids were ordered from Twist — the six pET-28a constructs (the CDS_0011 tail-fiber fragment, CDS_0012 and its three ancestral variants, CDS_0010), in two orders on 2026-07-27 and 2026-09-10. We would like to describe the sponsorship accurately: was it the iGEM–Twist partner offer, a separate sponsorship, or a purchase? Is there a contact or an agreement we should name?

> *Your answer:*

**D2. Sequencing.** We have the Plasmidsaurus orders for the bacterial isolates and for the two Φ8-resistant clones (order SBYK6W). Who performed the Illumina phage sequencing run **3NKSC3**? We never recorded the provider.

> *Your answer:*

**D3. Other offers.** Did the project use **IDT**, **GenScript**, the **iGEM Distribution Kit**, or **Anthropic** credits through iGEM? The form asks us to answer for each one, and to give a reason when we did not use it.

> *Your answer:*

**D4. Other sponsors, donors, or institutional support** we should credit, including the donor named in the summer sponsor report.

> *Your answer:*

---

## E. Two short administrative items

**E1. Safety.** For the Project Safety Form we still need the name of the KGI biosafety officer or IBC contact, and an approval number if there is one.

> *Your answer:*

**E2. Anything we have missed.** If any statement in this document misrepresents your contribution, please correct it directly — we will enter whatever you write.

> *Your answer:*

---

*Prepared by Chun-Yu Chen for iGEM Claremont (team #6317), 2026-10-18. Answers feed the Attributions Form at teams.igem.org, which freezes 2026-10-21 08:00 PDT.*
