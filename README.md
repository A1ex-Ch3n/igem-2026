# iGEM 2026 — *Pseudomonas* Phage Discovery & Characterization

> Wet-lab notebook, protocols, scheme documents, and analysis code for the iGEM 2026 project on isolating and sequencing *Pseudomonas*-targeting bacteriophages from soil samples collected at the California Botanic Garden.

## Project at a glance

- **Goal:** discover novel *Pseudomonas* phages from local soil; sequence both the bacterial hosts and the recovered phages; build a host-range matrix.
- **Three parallel sequencing tracks** + an iterative plaque assay — see [`scheme/20260605_clean_scheme.md`](scheme/20260605_clean_scheme.md) for the project's underlying logic, or [`scheme/20260604_confirmed_scheme_CLAUDE.md`](scheme/20260604_confirmed_scheme_CLAUDE.md) for the dated, sample-by-sample record.
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
│   ├── 0604/ … 0605/          ← per-day source photos (LFS for big PNGs)
│   └── digitalized/           ← one .md file per dated entry + page images
│       ├── README.md          ← chronological TOC
│       ├── typos.md           ← cataloged handwritten corrections
│       ├── images/            ← extracted page images (LFS for big PNGs)
│       └── 2026-MM-DD_*.md    ← 14 entries
│
├── scheme/                    ← project-level "what we did + why" docs
│   ├── 20260604_confirmed_scheme.md           ← Alex's original
│   ├── 20260604_confirmed_scheme_CLAUDE.md    ← detailed + dated
│   ├── 20260605_clean_scheme.md               ← high-level rationale (EN)
│   └── 20260605_clean_scheme_cn.md            ← high-level rationale (繁體中文)
│
├── protocol/                  ← lab protocols
│   ├── PMM_ProtocoL (1).docx                  ← source: prof's PMM recipe
│   ├── PseudomonasClassAppendixes.pdf         ← source: JMBE 2014 (CC-BY)
│   ├── Genomic_And_Phage_Work.docx            ← source: PI's protocol
│   ├── _d3024_d3025_quick-dna_miniprep_kit.pdf ← source: Zymo kit datasheet
│   ├── protocol-for-portelite-…-OFFcC.pdf     ← source: AAT Bioquest kit
│   └── md/                                    ← team's markdown protocols
│       ├── README.md          ← index of 23 active protocols + 2 archived
│       ├── _TEMPLATE.md       ← protocol authoring template
│       ├── media/             ← 7 reusable media / buffer / kit references
│       ├── techniques/        ← 4 reusable techniques
│       └── workflows/         ← 12 end-to-end workflows
│
├── archived/                  ← deprecated protocols (preserved as historical reference)
│   ├── README.md
│   ├── phage_amplification.md ← deprecated 2026-06-06
│   └── spot_testing.md        ← deprecated 2026-06-06
│
├── code/                      ← analysis notebooks
│   ├── 0605_quantification.ipynb     ← Qubit standard-curve fit + concentrations
│   ├── 0605_quantification.pdf
│   ├── 0605_quantification_report.pdf
│   └── output/                       ← plots (standard curve, per-sample bars)
│
├── data/                      ← raw datasets
│   └── 0529_OD.xlsx                  ← Optical density measurements from 5-29
│
└── photos/                    ← raw lab photos (LFS for *.JPG)
    ├── 0529/                  ← 37 camera photos from 5-29 OD/stock session
    └── 0605/                  ← 5 phone photos from 6-5 lab walk
```

## How to read this repo

1. **For the WHY** — start with [`scheme/20260605_clean_scheme.md`](scheme/20260605_clean_scheme.md). High-level rationale, no dates or sample IDs.
2. **For the WHAT (per day)** — [`scheme/20260604_confirmed_scheme_CLAUDE.md`](scheme/20260604_confirmed_scheme_CLAUDE.md). Detailed timeline with samples + decisions.
3. **For the HOW (per procedure)** — [`protocol/md/README.md`](protocol/md/README.md). 23 protocols organized as media / techniques / workflows.
4. **For raw notebook entries** — [`lab_notebook/digitalized/README.md`](lab_notebook/digitalized/README.md). One markdown file per dated entry.
5. **For analysis** — [`code/0605_quantification.ipynb`](code/0605_quantification.ipynb) (Qubit DNA quant).

## Git LFS

Large binary files (raw camera photos, scanned lab notebook PDF, scanned notebook page PNGs) are tracked via **Git LFS** so cloning is fast and the repo stays manageable. Tracked patterns are in [`.gitattributes`](.gitattributes).

To clone with the LFS files:

```bash
git lfs install                                 # one-time, per machine
git clone <this-repo-url>
cd <repo>
git lfs pull                                    # fetch the LFS-tracked binaries
```

Without `git lfs pull`, the LFS files appear as small text pointers instead of real binaries.

## Attribution — third-party source materials in this repo

The team's own original content (lab notebook .md files, scheme docs, protocol .md files, analysis code, photos taken by team members) is licensed **CC BY 4.0** — see [LICENSE](LICENSE).

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

This repo follows several conventions captured during the project's setup:

- **Preserve all versions:** when sources disagree on a procedure value (team's as-run vs prof's spec vs kit default), all variants are kept side-by-side in tables; readers pick which to use. See any modified protocol for examples.
- **Obsidian callouts** are used for visual emphasis: `> [!tip]` for team practice annotations, `> [!failure] DEPRECATED` for retired content, `> [!note]` for status.
- **Wiki-links** (`[[protocol_name]]`) are used between protocol files. Obsidian resolves these across the vault.
- **`[TBD: …]`** markers flag missing values awaiting team input. Tracked in [`protocol/md/README.md`](protocol/md/README.md) "Pending team decisions" section.
- **`==CONFIRM: …==`** markers flag inline questions for team verification.
- **Per-doc `## Log` footer** records edit history with dated entries.

## Contact

Team contact: see iGEM 2026 team page (link TBD).
