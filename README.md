# iGEM 2026 — *Pseudomonas* Phage Discovery & Characterization

> Wet-lab notebook, protocols, scheme documents, and analysis code for the iGEM 2026 project on isolating and sequencing *Pseudomonas*-targeting bacteriophages from soil samples collected at the California Botanic Garden.

## Project at a glance

- **Goal:** discover novel *Pseudomonas* phages from local soil; sequence both the bacterial hosts and the recovered phages; build a host-range matrix.
- **Three parallel sequencing tracks** + an iterative plaque assay — see [`scheme/20260604_confirmed_scheme_CLAUDE.md`](scheme/20260604_confirmed_scheme_CLAUDE.md) for the dated, sample-by-sample record + pipeline overview, or [`scheme/20260604_confirmed_scheme.md`](scheme/20260604_confirmed_scheme.md) for Alex's original short version.
- **Active dates so far:** 2026-05-18 (kickoff) → ongoing. See [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md) for the chronological table of contents.

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
│   ├── 20260604_confirmed_scheme.md           ← Alex's original short version
│   └── 20260604_confirmed_scheme_CLAUDE.md    ← detailed + dated + pipeline overview
│
├── protocol/                  ← lab protocols
│   ├── PMM_ProtocoL (1).docx                  ← source: PI's PMM recipe
│   ├── PseudomonasClassAppendixes.pdf         ← source: JMBE 2014 (CC-BY)
│   ├── Genomic_And_Phage_Work.docx            ← source: PI's protocol
│   ├── 0605_quantification_report.pdf
│   └── output/                       ← plots (standard curve, per-sample bars)
│
├── data/                      ← datasets, organized by category
│   ├── bacteria_genome/             ← vendor genome bundles per strain (9-2-1, 9-6-2, 10-10-2, 8-5-2)
│   ├── processed_genome/            ← extracted receptors + phage-binding screen
│   ├── metagenomes/                 ← MG08 / MG09 predicted proteomes
│   ├── assays/                      ← OD/phage growth data (0529 OD, 0624/0625 od600)
│   ├── dna_extraction_inventory.md  ← bacteria/phage/DNA storage inventory
│   └── week_3_bacteria_list.md      ← strains queued for week 3
│
└── photos/                    ← raw lab photos (LFS)
    ├── 0529/                  ← 37 camera photos from 5-29 OD/stock session
    └── 0605/                  ← 5 phone photos from 6-5 lab walk
```

## How to read this repo

1. **For the WHY + WHAT (per day)** — start with [`scheme/20260604_confirmed_scheme_CLAUDE.md`](scheme/20260604_confirmed_scheme_CLAUDE.md). Detailed timeline with samples + decisions + pipeline overview of each track.
2. **For the HOW (per procedure)** — [`protocol/md/README.md`](protocol/md/README.md). 23 protocols organized as media / techniques / workflows.
3. **For raw notebook entries** — [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md). One markdown file per dated entry.
4. **For analysis** — [`code/0605_quantification.ipynb`](code/0605_quantification.ipynb) (Qubit DNA quant).

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

The team's own original content (lab notebook `.md` files, scheme docs, protocol `.md` files, analysis code, photos taken by team members) is licensed **CC BY 4.0** — see [LICENSE](LICENSE).

The following files in this repo were **authored by third parties** and are included under fair-use / educational-use assumptions:

| File | Authorship | Original use |
|---|---|---|
| `protocol/Genomic_And_Phage_Work.docx` | Project PI | Course / teaching protocol |
| `protocol/PMM_ProtocoL (1).docx` | Project PI | Course / teaching protocol |
| `protocol/PseudomonasClassAppendixes.pdf` | Sandman & Ecker, JMBE 2014 | Open-access journal article (CC-BY 4.0) |
| `protocol/_d3024_d3025_quick-dna_miniprep_kit.pdf` | Zymo Research | Publicly-distributed product datasheet |
| `protocol/protocol-for-portelite-…-OFFcC.pdf` | AAT Bioquest | Publicly-distributed product datasheet |

If you are one of the authors of the PI's documents and would prefer they be removed from this repository, please open an issue.

## Editing conventions
- Scheme section: removed 20260605_clean_scheme.md + 20260605_clean_scheme_cn.md (deleted)
- "Project at a glance": now points to the _CLAUDE.md for project logic (since the clean-scheme summary is gone)
- "How to read this repo": collapsed step 1 (clean scheme) + step 2 (CLAUDE scheme) into a single step 1; renumbered accordingly
- lab_notebook/0604 / 0605: split into separate lines so it's clear what's in each subfolder
- Git LFS section: added the actual tracking patterns inline (was previously "see .gitattributes")
- "PI" terminology used consistently instead of "prof" (more professional for a public repo)