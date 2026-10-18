# Documents from Prof. Ignacio-Espinoza — 2026-10-18

Seven files handed over on 2026-10-18. Originals kept here unedited; the
derived/usable material has been filed elsewhere in the repo.

**Read first — three things that conflict with what the repo already records:**

1. `LooseEndsiGEM.docx` A2 describes the Φ8 genome as **circular** ("the assembly
   graph closed into a circle"). The repo's own analysis
   (`code/0708_phage_assembly`, `data/phage_genome`) resolved the topology as
   **linear with a 77 bp direct terminal repeat (DTR)** — same 77 bp, opposite
   interpretation. Do not paste A2 into the wiki or a form until this is settled
   with him. Full evidentiary record, and why our own "resolved" is weaker than
   it looks, in
   [`../2026-10-18_genome_topology_conflict.md`](../2026-10-18_genome_topology_conflict.md).
2. A2 has an unfilled placeholder: "input **XX** ng".
3. A3 has an unfilled placeholder: "AlphaFold **weserver version**", plus
   "all ORFs with were annotated" and "to identify structural" (sentence cut off).

## The files

| File | What it is | Where it plugs in |
|---|---|---|
| `LooseEndsiGEM.docx` | His answers to our Attributions questionnaire (A1–A5, B1–B4, D2, D3, E1, E2) | Transcribed to [`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md); questions are in `../2026-10-18_pi_contribution_questionnaire.md` |
| `IBCReviewLetter.docx` | KGI IBC **conditional approval**, dated 2026-10-15, signed Jasmine Yu (Chair). One revision required; track-changes revision due **Oct 24** | Project Safety Form (E1). See note below |
| `iGEM_main_figure.pdf` | Draft main figure, 4 panels: (A) plaque photo 9-6-2 Φ8 1:256, (B) virion cartoon with CDS_10 / CDS_12 coloured, (C) phage × Pseudomonas EOP susceptibility matrix, (D) ZymCTRL perplexity per EC number, extant → ancestral | Wiki Results / Description figure |
| `phage_groupA.svg` | Vector source of panel B (virion schematic, branched RBP with accessory proteins) | Editable asset for wiki figures |
| `SCRIPTS_DATA.zip` | Archive of the ASR + ZymCTRL work | Extracted to `../../code/1018_prof_asr_zymctrl/` |
| `DepolymeraseMCB.docx` | Grant pre-proposal: "Virion-associated depolymerases as a determinant of phage host range" (3 aims) | Not an iGEM deliverable — background framing. See below |
| `DepolymerasesEEB.docx` | Grant pre-proposal, evolution-framed variant: "The Evolution of Capsule Degradation as a Determinant of Phage Host Range" (3 aims) | Same |

## Why the two grant drafts matter to us

They are the first written statement of the project's **central hypothesis** in
his own words, and both name iGEM 2026 explicitly:

> in capsulated bacteria, the substrate range and biochemistry of phage virion
> depolymerases, and not the RBP identity alone, set a host range ceiling

and the evolutionary half:

> the narrow specificity of extant enzymes is a derived state arising from
> broader ancestral activity

This is the framing our wiki Description/Project Design should use. It also
reconciles the retired RBP×OMP binding screen: the gate is the **polysaccharide
layer and the enzyme that degrades it**, not a protein–protein lock and key.

They also supply usable text for:

- **Preliminary work** — isolates are named as *Pseudomonas capeferrum* and
  *P. putida* from the California Botanic Garden, The Claremont Colleges, with
  Chen et al., 2026 (MRA) as the citation.
- **Depolymerases occur in two forms** in our phage: fused into the RBP *and* as
  independent ORFs (EEB draft) — which is the CDS_10 / CDS_12 distinction in
  figure panel B.
- **Human Practices / training** — 5 undergrads per year, authorship, meetings.

Note the two drafts order the same three aims differently (MCB: biochemistry
first; EEB: phylogeny first). Neither is "the" plan; use whichever framing fits
the audience.

## IBC letter — what it means for the Safety Form

- Conditional approval only, **no approval number yet** (he confirms this in
  `LooseEndsiGEM.docx` E1). The contact name in his answer is "Jasmine **Ju**";
  the letter is signed "Jasmine **Yu**" — the letter is the primary source.
- The outstanding condition (Section IV part 3) is to supply **references or
  scientific rationale that our experiments will not alter phage host range,
  bacterial virulence, or antibiotic resistance**. We already hold evidence that
  bears on exactly this: 0 VFDB and 0 CARD hits in the Φ8 genome
  (`code/0708_phage_assembly`) and the resistant-mutant WGS showing only a single
  host-side capsule-cluster SNP (`documents/2026-10-10_resistant_mutant_summary_for_PI.md`).
  Offering him that material is the single highest-value thing we can do before
  his Oct 24 deadline.

---

**Log**

- 2026-10-18 — received from PI; filed, indexed, conflicts flagged.
