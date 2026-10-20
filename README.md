# iGEM 2026 — *Pseudomonas* Phage Discovery & Characterization

> Wet-lab notebook, protocols, scheme documents, and analysis code for the iGEM 2026 project on isolating and sequencing *Pseudomonas*-targeting bacteriophages from soil samples collected at the California Botanic Garden.

## Project at a glance

- **Goal:** discover novel *Pseudomonas* phages from local soil; sequence both the bacterial hosts
  and the recovered phages; work out what sets the phage's host range.
- **Central hypothesis, in the PI's words:** in capsulated bacteria the **depolymerase substrate
  range**, not RBP identity, sets the ceiling on host range, and today's narrow specificity is
  derived from a broader ancestral activity. This is why the project moved from a protein–protein
  binding screen to ancestral reconstruction of the phage's GH5 enzyme.
- **Active dates:** 2026-05-18 (kickoff) → **2026-10-19 (final bench day)**. 63 digitized notebook
  entries; see [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md).
- **Published:** the three host genomes are announced in *Microbiology Resource Announcements*,
  **doi [10.1128/mra.00793-26](https://doi.org/10.1128/mra.00793-26)** (published 2026-09-04,
  undergraduate first author). Isolates 8-5-2 / 9-2-1 / 8-10-2; assemblies GCA_059295255.1,
  GCA_059295275.1, GCA_059295235.1 (BioProject PRJNA1482863); reads under PRJNA1483221.

**Where the science stands.** The 9-2-1 Φ8 phage is assembled and annotated
([`code/0708_phage_assembly/`](code/0708_phage_assembly/)): ~62 kb, 80 CDS, no database match,
zero virulence and zero antibiotic-resistance genes. Its receptor-binding apparatus is a
**β-helix depolymerase**, so the receptor is **LPS sugar, not a protein** — which is why the
protein–protein binding screen was retired
([`documents/2026-07-13_why_protein_protein_binding_fails.qmd`](documents/2026-07-13_why_protein_protein_binding_fails.qmd)).
Six proteins were cloned into pET-28a and expressed in *E. coli*: three wild-type phage proteins
and three computationally reconstructed ancestors of the GH5 enzyme. Expression is **partly
evidenced and not yet confirmed by size** — the 2026-10-19 anti-His dot blot
([`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`](lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md))
is the furthest the wet lab got.

## ⚠️ Three conventions worth knowing before you read anything

**1. Phage CDS numbering — use Prof. Espinoza's `UUAIURNK_` index.** The 9-2-1 Φ8 genome was
annotated twice, and the two assemblies are **reverse-oriented**, so the CDS numbers run opposite
(77/80 are the same protein, just renumbered). **His index is canonical as of 2026-07-16**; our old
`FHABPWTM_` numbers are deprecated. Convert via
[`code/0713_espinoza_structural_mapping/cds_lookup.tsv`](code/0713_espinoza_structural_mapping/cds_lookup.tsv).
Anything written before 2026-07-16 may still use the old numbers.

**2. Phage genome topology — report it as circular.** Our own assembly reads as linear with a
77 bp direct terminal repeat; the PI's reads as circular. On **2026-10-18** it was settled that
the PI's assembly governs for anything outward-facing: **circular, 62,339 bp** (62,416 bp before
the 77 bp overhang is trimmed). Documents written before that date still say linear and carry a
dated footer saying so. The evidence on both sides, and what was never tested, is in
[`documents/2026-10-18_genome_topology_conflict.md`](documents/2026-10-18_genome_topology_conflict.md).

**3. File naming.**

| where | pattern | example |
|---|---|---|
| `code/` | `MMDD_snake_case` — a notebook/dir **is named after its output dir** | `0708_phage_genome_analysis.ipynb` → `code/output/0708_phage_genome_analysis/` |
| `documents/`, `scheme/`, `lab_notebook/digitalized/` | `YYYY-MM-DD_slug` | `2026-07-13_why_protein_protein_binding_fails.qmd` |

Analysis code goes in `code/<MMDD_topic>/`, everything it writes goes in `code/output/<same name>/`
— never beside the code. Write-ups for humans go in `documents/`. Each analysis dir carries its own
`README.md` ending in a dated **log footer**; open questions are marked **UNDONE**.

## Repository structure

```
iGEM 26/
├── README.md                  ← you are here
├── LICENSE                    ← CC BY 4.0 for the team's original content
├── .gitignore
├── .gitattributes             ← Git LFS pattern rules
│
├── lab_notebook/              ← physical lab notebook + digitized markdown copies
│   ├── pre_0604.pdf           ← scanned notebook pages 1-28 (LFS)
│   ├── 0604/                  ← per-day source photos (2 jpg)
│   ├── 0605/                  ← per-day source photos (3 png, LFS)
│   └── digitalized/           ← one .md file per dated entry + page images
│       ├── README.md          ← chronological TOC
│       ├── typos.md           ← cataloged handwritten corrections
│       ├── images/            ← extracted page images (LFS for big PNGs)
│       └── 2026-MM-DD_*.md    ← 63 entries (2026-05-18 → 2026-10-19)
│
├── scheme/                    ← project-level "what we did + why" docs
│   ├── 2026-06-04_confirmed_scheme.md         ← Alex's original short version
│   └── 2026-06-04_confirmed_scheme_CLAUDE.md  ← detailed + dated + pipeline overview
│
├── protocol/                  ← lab protocols
│   ├── md/                                    ← 23 protocols: media / techniques / workflows
│   ├── PMM_ProtocoL (1).docx                  ← source: PI's PMM recipe
│   ├── PseudomonasClassAppendixes.pdf         ← source: JMBE 2014 (CC-BY)
│   └── Genomic_And_Phage_Work.docx            ← source: PI's protocol
│
├── code/                      ← analysis, one dir/notebook per dated task (MMDD_topic)
│   ├── 0605–0710_quantification, 0624/0625_od600_phage   ← wet-lab assay analysis
│   ├── 0617–0620_receptor_*        ← host-side: Pseudomonas surface OMPs → receptor classes
│   ├── 0619_literature_rbp_database/, 0623_metagenome_rbp/, 0701_*  ← RBP discovery tracks
│   ├── 0703_phage_host_matrix/     ← the RBP × receptor folding screen (retired — see below)
│   ├── 0708_phage_assembly/        ← 9-2-1 Φ8 assembly + Pharokka annotation (Laguna)
│   ├── 0712_phage_rbp_detect/      ← RBP Detect + fold: the tail spikes are β-helix depolymerases
│   ├── 0713_espinoza_structural_mapping/   ← PI's virion map + the CDS-numbering conversion table
│   ├── 0716_espinoza_fiber_construct/      ← which piece of CDS_0011 to clone (plasmid #1)
│   ├── 0727_o_antigen_comparison/  ← three strains, three non-homologous O-antigen cassettes
│   ├── 0729_prof_figures/, 0730_synteny_group_d/  ← figures for the PI; novel podovirus, group-D-like
│   ├── 0915/0929/1010_gel_annotation.ipynb  ← SDS-PAGE densitometry across the expression rounds
│   ├── 1010_resistant_mutant_comparison/    ← WGS of two Φ8-resistant picks vs their parents
│   ├── 1015/1016_spot_test*        ← dilution series and the first activity readout
│   ├── 1018_construct_structures/  ← ESMFold + PyMOL comparison of the six expressed parts
│   ├── 1018_prof_asr_zymctrl/      ← the PI's ancestral reconstruction and ZymCTRL scoring
│   ├── 1019_dotblot/               ← the final experiment: anti-His dot blot quantification
│   └── output/                     ← every result, mirroring the dir names above
│
├── software/                  ← the packaged, reusable tools (MIT; see software/README.md)
│   ├── phagecheck/            ← DTR-vs-circularity from read coverage; β-helix call from a PDB
│   ├── gelquant/, olocus/, phageresist/   ← gel densitometry, O-antigen locus comparison,
│   │                                        resistant-mutant workflow
│   └── benchmarks/            ← includes the retired binding screen, published as a negative result
│
├── documents/                 ← write-ups for humans (YYYY-MM-DD_slug): findings, safety
│                                 drafts, PI notes, rendered .qmd → .html/.pdf reports
│
├── data/                      ← datasets, organized by category
│   ├── bacteria_genome/             ← vendor genome bundles per strain (9-2-1, 9-6-2, 10-10-2, 8-5-2, 8-10-2)
│   ├── phage_genome/                ← per host site. 9-2-1 Φ8: raw reads (3NKSC3) + assembly +
│   │                                  the PI's AlphaFold3 folds (bulk files on disk, not in git)
│   ├── processed_genome/            ← extracted receptors + phage-binding screen
│   ├── metagenomes/                 ← MG08 / MG09 predicted proteomes
│   ├── assays/                      ← OD/growth data plus every protein assay: 0915/0929/1001/1010
│   │                                  SDS-PAGE, 1015 Bradford, 1016 spot test, 1019 dot blot
│   ├── expressed_proteins/          ← the six pET-28a constructs as ordered
│   ├── dna_extraction_inventory.md  ← bacteria/phage/DNA storage inventory
│   └── week_3_bacteria_list.md      ← strains queued for week 3
│
├── archived/                  ← superseded protocols, kept for provenance
│
└── photos/                    ← raw lab photos (LFS)
    ├── 0529/                  ← 37 camera photos from 5-29 OD/stock session
    └── 0605/                  ← 5 phone photos from 6-5 lab walk
```

**Not in git:** raw reads, metagenome proteomes, the PI's AlphaFold3 folds (51 MB zipped → 460 MB
of MSAs and PAE matrices), and other bulky vendor/intermediate data — they live on disk and are
listed in [`.gitignore`](.gitignore). Git keeps the scripts plus the compact derived results, so
every `code/output/` deliverable is reproducible by re-running its script over the local data.

## How to read this repo

**Start here.** The canonical, cross-linked index of every result is the pair of synthesis
documents — same numbers, same figures, one in Traditional Chinese and one in English:

- [`documents/2026-07-28_results_synthesis.qmd`](documents/2026-07-28_results_synthesis.qmd) (中文)
- [`documents/2026-07-29_results_synthesis_EN.qmd`](documents/2026-07-29_results_synthesis_EN.qmd) (English)

They carry a 53-row results table with an evidence grade on every row, the full O-antigen
analysis, and a "how each figure was made" note. Read one of those before re-deriving anything.
Both predate 2026-10-18 and carry dated footers where later work superseded them.

Then, by what you need:

1. **The WHY + WHAT, per day** — [`scheme/2026-06-04_confirmed_scheme_CLAUDE.md`](scheme/2026-06-04_confirmed_scheme_CLAUDE.md).
   Timeline with samples, decisions and a pipeline overview of each track.
2. **The HOW, per procedure** — [`protocol/md/README.md`](protocol/md/README.md). 23 protocols as
   media / techniques / workflows.
3. **Raw notebook entries** — [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md).
   One markdown file per dated entry; open questions are marked `==CONFIRM==` / `==UNDONE==`.
4. **The dry-lab story**, in order:
   - [`documents/2026-07-05_essential_evidence_map.md`](documents/2026-07-05_essential_evidence_map.md) — what we know vs. assume
   - [`documents/2026-07-13_why_protein_protein_binding_fails.qmd`](documents/2026-07-13_why_protein_protein_binding_fails.qmd) — **why the RBP × receptor folding screen was retired.** It ran over 7,182 pairs and a 9-fold control test showed the score reads protein size, not binding. Do not re-attempt it
   - [`code/0712_phage_rbp_detect/README.md`](code/0712_phage_rbp_detect/README.md) — the tail spikes are β-helix depolymerases, so the receptor is LPS **sugar**
   - [`code/0727_o_antigen_comparison/`](code/0727_o_antigen_comparison/) — three ANI-distinct strains carry three non-homologous O-antigen cassettes in the same `ihfB`-flanked slot
   - [`code/1018_prof_asr_zymctrl/`](code/1018_prof_asr_zymctrl/) — the ancestral GH5 reconstruction the expression work is built on
5. **The protein work and what it does and does not show** — the gels in
   `code/*_gel_annotation.ipynb` (9/15 inconclusive, 9/29 two unassigned bands, 10/10 Ni-NTA
   failed), then [`code/1016_spot_test_result.ipynb`](code/1016_spot_test_result.ipynb) and
   finally [`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`](lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md).
   **No construct has been confirmed by size**, and there is still no untransformed BL21(DE3)
   control lane anywhere in the protein work.
6. **The Registry parts** — [`documents/2026-10-18_registry_part_drafts/`](documents/2026-10-18_registry_part_drafts/).
   `paste/` holds the exact ASCII text that went onto registry.igem.org,
   `live_snapshot_1019/` the verbatim state before the last edit round, and
   [`REGISTRY_APPLIED.md`](documents/2026-10-18_registry_part_drafts/REGISTRY_APPLIED.md) records
   what is applied and what is still outstanding.
7. **A specific assay** — `code/<MMDD>_<topic>.ipynb`, e.g.
   [`code/0605_quantification.ipynb`](code/0605_quantification.ipynb) (Qubit DNA quant).

## State at the 2026-10-21 freeze

**Done:** the MRA paper is published; six Registry parts exist with full documentation; the wiki
is live; the Attributions Form is submitted; `software/` is packaged under MIT with tests.

**Known-outstanding**, recorded rather than hidden:

- Two Registry **Functional Descriptions** still need editing, and the parts are still in
  **Draft** — see `REGISTRY_APPLIED.md`. Sequence, authorship and licence lock permanently at
  *Send for Screening*.
- The **Judging Form** has not been saved; its abstract needs the species correction described in
  [`documents/2026-10-18_judging_form_draft.md`](documents/2026-10-18_judging_form_draft.md).
- **Induction temperature** is recorded as ~30 °C on the part pages, but the notebook says 37 °C
  for 2026-09-10 and nothing for the 09-15 and 09-27 rounds. Unreconciled on purpose.
- Never done: **CheckV**, formal phage taxonomy (`terL` unannotated), and the **9-6-2 Φ8** genome.
- The 2026-10-16 spot test did **not** settle R1 resistance — Φ8 gave no clearing even on the
  parent strains.

## Git LFS

Large binary files (raw camera photos, scanned lab notebook PDF, scanned notebook page PNGs) are tracked via **Git LFS** so cloning is fast and the repo stays manageable. Tracked patterns are in [`.gitattributes`](.gitattributes):

- `*.JPG` — camera photos in `photos/`
- `lab_notebook/**/*.png` — scanned notebook pages
- `lab_notebook/pre_0604.pdf` — the 71 MB notebook scan

To clone with the LFS files:

```bash
git lfs install                                 # one-time, per machine
git clone <this-repo-url>
cd <repo>
git lfs pull                                    # fetch the LFS-tracked binaries
```

Without `git lfs pull`, the LFS files appear as small text pointers instead of real binaries.

## Attribution — third-party source materials in this repo

The team's own original content (lab notebook `.md` files, scheme docs, protocol `.md` files, the
analysis notebooks under `code/`, photos taken by team members) is licensed **CC BY 4.0** — see
[LICENSE](LICENSE).

**The packaged software under [`software/`](software/) is MIT instead** — see
[`software/LICENSE`](software/LICENSE). The split is deliberate: CC BY 4.0 is a content licence
and is not OSI-approved, and iGEM's Best Software rules require an OSI-approved licence for the
code.

The following files in this repo were **authored by third parties** and are included under fair-use / educational-use assumptions:

| File | Authorship | Original use |
|---|---|---|
| `protocol/Genomic_And_Phage_Work.docx` | Project PI | Course / teaching protocol |
| `protocol/PMM_ProtocoL (1).docx` | Project PI | Course / teaching protocol |
| `protocol/PseudomonasClassAppendixes.pdf` | Sandman & Ecker, JMBE 2014 | Open-access journal article (CC-BY 4.0) |
| `protocol/_d3024_d3025_quick-dna_miniprep_kit.pdf` | Zymo Research | Publicly-distributed product datasheet |
| `protocol/protocol-for-portelite-…-OFFcC.pdf` | AAT Bioquest | Publicly-distributed product datasheet |

If you are one of the authors of the PI's documents and would prefer they be removed from this repository, please open an issue.

---
*Log — 2026-06: scheme section points at `_CLAUDE.md` for project logic (the clean-scheme summaries
were deleted); Git LFS patterns listed inline; "PI" used throughout instead of "prof".*
*Log — 2026-07-16: repo-wide tidy. Adopted the PI's `UUAIURNK_` CDS numbering as canonical and
documented it up front. Normalized naming — `scheme/` `YYYYMMDD` → `YYYY-MM-DD`;
`code/0619_literature_database/` → `0619_literature_rbp_database/` (match its output dir); dropped
parentheses/spaces from the two `0625_od600_phage` notebooks; `0616_binding-screen-fold-plan.md` →
underscores; the two `0605_quantification` PDFs moved into `code/output/0605_quantification/`;
`documents/fig_binding_controls.py` → date-prefixed. Structure tree rewritten — it was missing
`code/`, `documents/` and `archived/` entirely and claimed `protocol/` still held the 0605 PDF and
an `output/` dir (both had moved to `code/` long ago). Added "how to read the dry-lab story" so the
retired binding screen isn't re-attempted.*