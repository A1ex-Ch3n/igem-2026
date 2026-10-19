# iGEM 2026 — *Pseudomonas* Phage Discovery & Characterization

> Wet-lab notebook, protocols, scheme documents, and analysis code for the iGEM 2026 project on isolating and sequencing *Pseudomonas*-targeting bacteriophages from soil samples collected at the California Botanic Garden.

## Project at a glance

- **Goal:** discover novel *Pseudomonas* phages from local soil; sequence both the bacterial hosts and the recovered phages; build a host-range matrix.
- **Three parallel sequencing tracks** + an iterative plaque assay — see [`scheme/2026-06-04_confirmed_scheme_CLAUDE.md`](scheme/2026-06-04_confirmed_scheme_CLAUDE.md) for the dated, sample-by-sample record + pipeline overview, or [`scheme/2026-06-04_confirmed_scheme.md`](scheme/2026-06-04_confirmed_scheme.md) for Alex's original short version.
- **Active dates so far:** 2026-05-18 (kickoff) → ongoing. See [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md) for the chronological table of contents.
- **Where the science stands:** the 9-2-1 Φ8 phage is assembled and annotated ([`code/0708_phage_assembly/`](code/0708_phage_assembly/)); its receptor-binding protein is a **β-helix depolymerase**, so the receptor is **LPS sugar, not a protein** — which is why the protein–protein binding screen was retired ([`documents/2026-07-13_why_protein_protein_binding_fails.qmd`](documents/2026-07-13_why_protein_protein_binding_fails.qmd)). The fiber to clone is **CDS_0011** ([`code/0716_espinoza_fiber_construct/`](code/0716_espinoza_fiber_construct/)).

## ⚠️ Two conventions worth knowing before you read anything

**1. Phage CDS numbering — use Prof. Espinoza's `UUAIURNK_` index.** The 9-2-1 Φ8 genome was
annotated twice, and the two assemblies are **reverse-oriented**, so the CDS numbers run opposite
(77/80 are the same protein, just renumbered). **His index is canonical as of 2026-07-16**; our old
`FHABPWTM_` numbers are deprecated. Convert via
[`code/0713_espinoza_structural_mapping/cds_lookup.tsv`](code/0713_espinoza_structural_mapping/cds_lookup.tsv).
Anything written before 2026-07-16 may still use the old numbers.

**2. File naming.**

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
│       └── 2026-MM-DD_*.md    ← 14 entries (2026-05-18 → 2026-06-05)
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
│   └── output/                     ← every result, mirroring the dir names above
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
│   ├── assays/                      ← OD/phage growth data (0529 OD, 0624/0625 od600)
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

1. **For the WHY + WHAT (per day)** — start with [`scheme/2026-06-04_confirmed_scheme_CLAUDE.md`](scheme/2026-06-04_confirmed_scheme_CLAUDE.md). Detailed timeline with samples + decisions + pipeline overview of each track.
2. **For the HOW (per procedure)** — [`protocol/md/README.md`](protocol/md/README.md). 23 protocols organized as media / techniques / workflows.
3. **For raw notebook entries** — [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md). One markdown file per dated entry.
4. **For the dry-lab story** — read these in order; each analysis dir's own `README.md` has the detail:
   - [`documents/2026-07-05_essential_evidence_map.md`](documents/2026-07-05_essential_evidence_map.md) — what we actually know vs. assume
   - [`documents/2026-07-13_why_protein_protein_binding_fails.qmd`](documents/2026-07-13_why_protein_protein_binding_fails.qmd) — **why the RBP × receptor folding screen was retired.** It was run (7,182 pairs) and a 9-fold control test showed the score reads protein size, not binding. Don't re-attempt it; see [`code/0703_phage_host_matrix/`](code/0703_phage_host_matrix/)
   - [`code/0712_phage_rbp_detect/README.md`](code/0712_phage_rbp_detect/README.md) — the tail spikes are β-helix depolymerases → the receptor is LPS **sugar**
   - [`code/0716_espinoza_fiber_construct/README.md`](code/0716_espinoza_fiber_construct/README.md) — the current front line: which piece of CDS_0011 goes into plasmid #1
5. **For a specific assay** — `code/<MMDD>_<topic>.ipynb`, e.g. [`code/0605_quantification.ipynb`](code/0605_quantification.ipynb) (Qubit DNA quant).

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