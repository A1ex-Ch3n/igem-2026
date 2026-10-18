# Attributions Form — entered and saved (iGEM Claremont 2026, team #6317)

Form: https://teams.igem.org/6317/deliverables/attributions/edit · freeze **2026-10-21 08:00 PDT** · status **Saved / Received** as of 2026-10-18.
Save only, no separate Submit — whatever is saved at the freeze is the final submission, so this can still be edited.
No word or character limit (checked the page text, the field attributes and the form's own validation rules). The FAQ asks for the form "(1) Task — what was done; (2) …" and calls out vague entries.

Companion file: `2026-10-18_pi_contribution_questionnaire.md` — sent to the PI 2026-10-18.

## Still to do before the freeze

1. **PI questionnaire** — awaiting his reply. His entry is entered now with the ancestral-sequence design as the lead item; revise it from his own words when they arrive.
2. **The stakeholder interview is on 2026-10-19** — Weitao wrote the guide and conducts it. Afterwards, add the interviewee to External Contributions (name, institution, what they contributed).
3. **"Actual time worked"** per phase is an estimate — adjust if the numbers look wrong.

---

## 1. Team Members

Task options: Analysis · Conceptualization · Background Research · Investigation · Data Curation · Notebook/record keeping · Project Administration · Fundraising · Public Engagement · Entrepreneurship · Hardware · Software · Wiki Coding · Visualization · Writing · Safety · Other

### J. Cesar Ignacio-Espinoza — Primary PI
Tasks: Software · Conceptualization · Analysis · Project Administration · Fundraising · Writing · Safety
> (1) Software — designed the ancestral enzyme variants himself. This is his work, not the students': the GH5 phylogenetic inference, the ancestral-state reconstruction that produced the Node1, Node40 and Node281 sequences we went on to express, and the protein-language-model scoring used to judge how well each designed sequence fits the enzyme class. He also produced the reference assembly and Pharokka annotation of phage 9-2-1 Φ8, which the team adopted as its canonical CDS numbering on 2026-07-16 in place of its own, and the AlphaFold and foldseek structural annotation of the virion together with the AlphaFold3 tail-cluster models that determined which fragment of CDS_0011 we cloned.
> (2) Conceptualization — set the scientific direction throughout: the GH5 depolymerase ancestral-reconstruction hypothesis, the reading of the phage receptor as an LPS sugar rather than a protein, the T7-like podophage classification and the requirement that we justify it by synteny, the design of all six expression constructs, and the withdrawal of an earlier glycosidase call on CDS_0010.
> (3) Analysis — supplied the approach for a large share of the analyses the students then implemented, including the genome assembly and annotation strategy, the RBP detection and receptor classification work, the judgement that our RBP-receptor folding screen was not informative, and the O-antigen and resistant-mutant comparisons; reviewed and validated the students' computational results.
> (4) Project Administration — hosted the team in his laboratory at KGI, supervised all wet-lab work under BSL-2, provided reagents and the HPC allocation our entire computational workload ran on.
> (5) Fundraising — arranged the Twist sponsorship that supplied every plasmid, and placed the synthesis and sequencing orders.
> (6) Writing — senior author of the genome announcement (doi 10.1128/mra.00793-26) and reviewer of its revision.
> (7) Safety — final review and submission of the Project Safety Form.

### Chun-Yu (Alex) Chen — Student Leader
Tasks: Conceptualization · Investigation · Analysis · Software · Data Curation · Notebook/record keeping · Project Administration · Fundraising · Visualization · Writing · Wiki Coding
> Project administration (co-founded the team, led planning and scheduling, coordinated with the PI and iGEM); investigation (soil sampling through to the autumn protein work, with Yan Yan and Xiaokuan Wang); software and analysis (all of the team's analysis code); data curation (1,673-sequence RBP database, notebook pages 1–81); writing (first author of the genome announcement, the revision and the reviewer response); visualization; fundraising; wiki.

### Yan (Olivia) Yan — Student
Tasks: Investigation · Notebook/record keeping · Writing · Wiki Coding · Public Engagement · Project Administration · Fundraising · Data Curation
> Summer bench work and the autumn protein work with Alex and Carol; ~20 notebook entries; co-author of the genome announcement; built the wiki framework and coordinated deliverables; organised the stakeholder interview; team photograph and judging presentation; personally covered part of the competition fees.

### Xiaokuan (Carol) Wang — Student
Tasks: Investigation · Notebook/record keeping · Writing · Data Curation · Analysis
> The largest share of the bench work, summer and autumn; recorded most of the summer experiments; co-author of the genome announcement; now also researches in the Ignacio-Espinoza Lab at KGI.

### Yuhui (Sarah) Liu — Student
Tasks: Conceptualization · Investigation · Analysis
> Helped design the experimental plan early on; DNA extraction and soil enrichment on 2026-05-20; and served as the team's standing technical adviser — she has prior research experience and we consulted her whenever an experiment failed or behaved unexpectedly. Much of this was advice rather than recorded bench days, so the notebook under-represents it.

### Weitao Ke — Student
Tasks: Public Engagement · Conceptualization · Investigation
> Led human practices: wrote the interview guide for our stakeholder interview and conducted the interview himself, and worked through how our results should be presented to an audience outside the laboratory. PMM agar plates on 2026-05-21. Early project discussions.

### Ryan — Student
Tasks: Conceptualization · Analysis
> Took part in the early, exploratory phase during the spring semester while the team was developing its dry-lab pipeline. He joined within two months of our first meeting with the PI and followed the analysis work as it was designed. He studies at a different institution, so his availability was limited and the pipeline as implemented contains no discrete component that is his; we record the participation rather than claim a deliverable for it. **Not the same person as Ryon Schmidt in External Contributions** — different school.

### Former: Camille Dahlgren — Student
Tasks: Conceptualization · Background Research
> Helped design the experimental plan early on, before leaving the roster.

### Former: Christan P — Student
Tasks: Visualization
> Graphic design work for the team.

---

## 2. AI Tool Use

| Tool | Tasks | Entered |
|---|---|---|
| Claude (Anthropic), via Claude Code | Software · Analysis · Writing · Visualization · Wiki Coding · Data Curation | Programming and writing assistant: analysis notebooks (assembly and annotation wrappers, RBP detection, resistant-mutant comparison, gel and assay quantification), HPC job scripts, drafting and editing, wiki structure. Accounts held by Yan Yan and Xiaokuan Wang. **Review:** every computational result was checked by a student against the underlying data — mutation calls confirmed at the level of the sequencing reads, and the protein-binding screen tested against a control set, which is how we found it uninformative and retired it. Code run and read by the student who owned the analysis, text edited by team members, scientific claims reviewed by the PI. |
| ElevenLabs | Visualization | AI narration for the promotional video; script written by the team. Checked line by line against the script. |
| Suno | Visualization | AI background music for the promotional video. |

No other AI tools were used.

## 3. iGEM & Partner Offers

| Offer | Used | Entered |
|---|---|---|
| **Twist** | Yes | Every plasmid in this project came from Twist. All six pET-28a constructs, two orders (2026-07-27, 2026-09-10): the CDS_0011 tail-fibre fragment (res. 305–941, N-terminal His6), the CDS_0012 GH5 depolymerase, three ancestral variants of CDS_0012 designed by the PI, and CDS_0010. Delivered as sequence-verified clones with glycerol stocks, transformed into BL21 for all expression, purification and activity work. The entire protein arm rests on this offer. |
| **Anthropic** | Yes | Yan Yan and Xiaokuan Wang held the accounts and used Claude as described above; every result checked by a student against the data. |
| Distribution Kit | No | Not relevant to our project — phages and isolates we collected from soil, constructs synthesised from those genomes, no standard registry parts. |
| IDT | No | Used another provider instead + did not need this type of support (all synthesis through Twist). |
| GenScript | No | Same. |

## 4. External Contributions

| # | Name | Institution | Relationship | Tasks |
|---|---|---|---|---|
| 1 | Rafael Escobar | Academic (KGI) | Collaborator | Investigation, Writing — PhD candidate in the PI's lab; selected the ten host isolates on 2026-06-11; PMM recipe from his notebook; bench guidance; co-author of the genome announcement |
| 2 | Maggie Chou | Academic (high school, Claremont) | Collaborator | Investigation, Notebook — bench work 2026-06-16 to 07-16 |
| 3 | Lu (Lucy) Shi | Academic (CMC) | Collaborator | Project Administration, Fundraising — co-founder of iGEM Claremont, co-signed the funding and travel requests |
| 4 | Prof. Ran Libeskind-Hadas | Academic (CMC) | External Advisor | Conceptualization, Project Administration — Chair of KDIS; early conceptualisation and administrative support |
| 5 | Ashley Armstrong | Nonprofit (California Botanic Garden) | Collaborator | Investigation, Public Engagement — Director of Horticulture; hosted us and took us into the grounds for the 2026-05-19 sampling |
| 6 | Plasmidsaurus | Industry | Contractor | Investigation — all sequencing: ONT WGS of the isolates and the two resistant clones, and the Illumina run on phage 9-2-1 Φ8 |
| 7 | California Botanic Garden | Nonprofit | Other | Other — granted access for the soil sampling |
| 8 | Ryon Schmidt | Academic (CMC) | Collaborator | Fundraising — approached potential sponsors and donors; the effort did not bring in meaningful funding, but the work was done |
| 9 | Hudson Nguyen | Academic (CMC) | Collaborator | Fundraising — same |

## 5. Project Timeline

| Phase | Start | End | Calendar wks | Actual wks |
|---|---|---|---|---|
| Recruit | 2025-12-01 | 2026-02-15 | 11 | 6 |
| Project development | 2025-12-15 | 2026-05-18 | 22 | 10 |
| Wet lab | 2026-05-18 | 2026-10-21 | 22 | 18 |
| Dry lab | 2026-06-05 | 2026-10-21 | 20 | 18 |
| Wiki | 2026-09-01 | 2026-10-21 | 7 | 5 |

Anchors: team founded winter 2025 · first meeting with the PI and start of the collaboration 2025-12-15 · the remaining members including Ryan joined within the following two months · general proposal 2026-05-07 · lab kickoff at KGI and first notebook page 2026-05-18 · soil sampling 2026-05-19 · first analysis notebook `0605_quantification.ipynb` · repository initialised 2026-06-08 · last notebook page 2026-07-16 · freeze 2026-10-21.

---
Log: 2026-10-18 built from a repository sweep and the live form, filled in from the team lead's answers, entered into the form at teams.igem.org and saved (status Saved / Received). Note: the form persisted its contents while stepping between sections, before the explicit Save.
