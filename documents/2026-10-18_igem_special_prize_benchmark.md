# 2026-10-18 — What past iGEM winners did: Parts and Best Software

Benchmarking pass over the 2025 results before preparing our **Parts** submission and our
**Best Software** entry. Everything here is sourced; where a source could not be reached it
says so.

Source of the results table: the public API behind `competition.igem.org/results/2025`
(the page itself is a JS SPA — see the house note on igem.org being unscrapeable):
`https://api.igem.org/v1/competitions/d615db72-738d-47c0-a929-fbdeb4882fc0/awards/results`.
Criteria text was extracted from the awards-page JS chunk
`https://competition.igem.org/assets/Awards-hgBAJo9D.js` and from
`https://api.igem.org/v1/competitions/58a7e73a-1e25-457f-9f59-36c47b3f652a/awards` (2026).

---

## 1. The rules we are actually graded against (2026 text)

**Best Software** (renamed from 2025's "Best Software Tool"):

- "Your software must be documented and released under an **OSI-approved open-source
  license**."
- "The source code must be hosted on the **dedicated repository in iGEM**"
  → `https://teams.igem.org/go/deliverables/software`, i.e. our `gitlab.igem.org` repo.
- Software & AI Village teams are **not eligible** — we are not in that village, so we are fine.
- Wiki page expected at `/software`.
- Six judging aspects: synbio-standards compatibility (SBOL, RFCs, data formats) · how well
  validated (2026 adds *"test data, or benchmarking"*) · usefulness to other projects ·
  integrability (APIs, packages) · user-friendliness · how well written and documented for
  future groups (code documentation, comments, performance evaluation, **architecture
  diagrams**, installation and execution scripts).

**Best New Basic Part**: one genetic component, documented on the Registry
(`https://teams.igem.org/go/deliverables/registry`). 2026 exemplars: `BBa_25IQCJ3B`,
`BBa_25MBHXUL`, `BBa_252FW60D`.

**Best Part Collection**, quoted: *"your collection must be registered in the iGEM Registry
and document the ensemble as a whole. Collection documentation is not the same as part
documentation: each part still has its own Registry page covering sequence, function,
characterization, and usage, while the collection page sits on top and explains how the parts
were designed to work together, what the system does as a whole, and how other teams can reuse
the collection or pick individual parts from it."* Wiki deliverable: **none — judges read the
Registry.** Exemplar collections: NRPieceS
`https://registry.igem.org/collections/97504ebf-0622-44d4-9cf2-fc050ae97eb4`, PHOENICS
`https://registry.igem.org/collections/23f3bf6b-fee1-4f6f-9924-bbe397fddb09`.

Registry part documentation is a fixed set of typed Markdown sections — **design, experiment,
characterisation, application, discussion** (public API:
`https://api.registry.igem.org/v1/parts/slugs/<slug>` → `/v1/parts/<uuid>/documentation`).

---

## 2. 2025 winners (abridged)

| Award | HS | Undergrad | Overgrad |
|---|---|---|---|
| Best Software Tool | Lambert-GA (CASPER) | BIT-China (FABRIC), EPFL (Pyronix) | Marburg (mATChmaker), Munich (MESA Designer) |
| Best New Basic Part | GEC-Guangzhou | NJTECH-CHINA-A | Freiburg (CONCAVE) |
| Best New Composite Part | Hongwen School | XJTLU-Science-China | Tianjin |
| Best Part Collection | BNDS-China | IZJU-China (FoCas) | Heidelberg (PHOENICS), Marburg (NRPieceS) |
| Best Model | GreatBay-SCIE | Peking | Heidelberg |
| Best Measurement | BNDS-China | EPFL | Aalto-Helsinki |

Wikis follow `https://2025.igem.wiki/<team-slug>`. Closest project to ours among the nominees:
**Toronto, "Mystiphage: a generative phage bank"** (Best Model nominee).

## 3. How the software winners packaged their work

**Munich — MESA Designer** (`https://2025.igem.wiki/munich/software`) is the fullest template.
Wiki: Usage → Programmatic Access (REST API with embedded OpenAPI reference + Python package)
→ Validation (expert consult + wet-lab validation of two designed receptors) → Development
(a **FAIR4RS compliance table**, architecture diagrams, roadmap) → Installation
(Docker/compose, local, PyPI, hardware requirements) → Conclusion → References.
Distribution: GitLab `gitlab.igem.org/2025/software-tools/munich`, GitHub mirror
`github.com/igem-munich/MESA-Designer`, PyPI `mesa-designer`, DockerHub image. Repo carries
4 Dockerfiles, `api/`, `app/`, a Python package with 4 pytest files, two PDF guides, JSON
resource databases and 5 CI workflows. ⚠️ their licence is CC-BY-4.0, which is **not**
OSI-approved — they won anyway, but copying that would risk our eligibility.

**Marburg — mATChmaker** (`https://2025.igem.wiki/marburg/software`): per-tool wiki skeleton
(Key Points → Abstract → Introduction → pipeline → Results → Outlook → References), Colab link,
Zenodo DOI for the data (`https://zenodo.org/records/17274407`). Repo: README with
Repository Structure / Installation / Usage, Dockerfile, one-click `run_*.sh` and `.bat`,
a developers' guide, sample inputs and outputs. **No LICENSE file in the mirror.**

**Lambert-GA — CASPER** (`https://2025.igem.wiki/lambert-ga/software`): short, and the one
trick worth stealing outright — a **"Judging" section that answers each of the six rubric
questions one by one**, with evidence. Three interfaces (web app, Python package, CLI),
FASTA in / CSV out, in-silico ranking agreement plus a wet-lab-ordered de novo design.

> Not verified: `gitlab.igem.org/2025/software-tools/*` is login-gated for logged-out users,
> so the repo internals above come from the public GitHub mirrors. EPFL and BIT-China software
> pages are client-rendered and returned no text.

## 4. How the parts winners characterised, and where 3D structure sat

- `BBa_25IQCJ3B` (repebody) uses AlphaFold in the **design** section only — a PyMOL figure with
  the mutated residues highlighted, arguing they sit on the non-binding face. No pLDDT/PAE
  numbers. Every characterisation section is wet-lab (expression, binding, far-western, BACTH).
- **PHOENICS** (`experiment` section) is the model for structure-heavy documentation: a
  **Tool | Input | Output table** (BindCraft i_pTM ranking, AlphaFold3 with pLDDT, GROMACS
  umbrella sampling, PRODIGY ΔG/K_D, PyMOL RMSD), then a numbered protocol, then an explicit
  acceptance criterion — *"binders with low predicted K_D and minimal structural drift
  (< 2 Å RMSD)"* — then the cell-free two-hybrid wet-lab readout that closes the loop.
- **NRPieceS** is wet-lab-first (LC-MS on 27 constructs), with structure prediction kept on
  the software page rather than in the collection text.

**Predicted structure alone never carried a winning characterisation section.** It appears in
*design*, paired with a threshold and a wet-lab readout.

---

## 5. What this means for us

1. **A "Judging" block on our `/software` page**, answering the six rubric aspects one by one.
   Cheapest high-signal change available.
2. **OSI-approved licence** (MIT / Apache-2.0 / BSD / GPL) in the repo root and named on the
   wiki. This is the one hard eligibility line.
3. **Mirror and package**: GitLab (required) + GitHub mirror + an installable package + a
   Dockerfile + sample inputs + a one-command run script. More than one interface.
4. **Validation is our strength, and 2026 explicitly accepts benchmarking**: the honest
   negative-control failure of the retired RBP×OMP ipTM screen, and the PhageRBPdetect-vs-
   homology union comparison, are both benchmarks we already own.
5. **Speak the standards language**: FASTA / GenBank / PDB / CSV in and out, an SBOL mapping
   statement, a FAIR4RS table, an architecture diagram.
6. **Parts are Registry-first.** The collection has no wiki deliverable in 2026. Budget time to
   fill all five typed sections per part.
7. **Write the GH5 + three ancestors as a collection, not a list** — one targeting/lysis
   toolbox, a variant → predicted-metric → measured-activity table, and explicit reuse guidance.
8. **Structure prediction goes in *design*, in a tool table, with numbers and a cutoff**, each
   model paired with the wet-lab readout we have (or an honest statement that it is pending).

---
*Log — 2026-10-18: compiled from the 2025 results API and the 2026 awards text. Companion
documents: [`2026-10-18_parts_structure_comparison.md`](2026-10-18_parts_structure_comparison.md)
(the Parts side) and [`2026-10-18_software_inventory.md`](2026-10-18_software_inventory.md)
(the Best Software side).*
