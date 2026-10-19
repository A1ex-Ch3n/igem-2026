# 2026-10-18 — Code inventory for the Best Software entry

Every piece of code this team wrote, what it does, and what it would take to release it
publicly on `gitlab.igem.org`. Criteria and the winners we are benchmarking against:
[`2026-10-18_igem_special_prize_benchmark.md`](2026-10-18_igem_special_prize_benchmark.md).

**Totals (non-blank lines; notebooks counted by code cells only, vendored and generated code
excluded):** 14,516 lines across 126 files — Python scripts 6,515 (60 files), notebook code
4,654 (25), TypeScript/TSX for the promo video 2,329 (17), shell + SLURM 630 (21),
JavaScript 388 (3). Python is 77 % of the total. 23 of the ~30 code directories already carry
a README, which is unusually good; what is missing is everything *around* the code.

---

## 1. Inventory

Reusability verdict is strict: **tool** = another team could run it on their own data,
**project** = sound but tied to this project, **glue** = one-off.

| Date | Unit | Purpose | Runs on | Verdict |
|---|---|---|---|---|
| 06-05 · 06-08 · 06-22 · 06-29 · 07-10 · 09-04 | `code/0*_quantification.ipynb` (6) | Qubit standard curve + sample concentrations | Mac | glue (×6, see §3) |
| 06-16 | `code/0616_binding_screen_fold_plan.md` | planning doc, not code | — | — |
| 06-17 | `code/0617_receptor_similarity_heatmaps.ipynb` | receptor-set similarity between the 3 isolates (MMseqs2) | Mac | project |
| 06-17 | `code/0617_receptor_venn.ipynb` | shared vs strain-unique receptors | Mac | project |
| 06-19 | `code/0619_literature_rbp_database/` | 1,673 unique RBP sequences aggregated from 3 papers | Mac | **tool** (dataset) |
| 06-20 | `code/0620_receptor_classification.{ipynb,py}` | classify *Pseudomonas* OMPs into Morinière classes by homology to 13 *E. coli* refs | Mac | project (notebook and script are 93 % identical) |
| 06-23 | `code/0623_metagenome_rbp/` | metagenome RBP pipeline: ANI/16S host ID → receptor FASTAs → NCBI surrogate-host search | Mac | mixed; `receptor_fasta.py` reusable |
| 06-24 · 06-25 ×2 | `code/06*_od600_phage*.ipynb` (3) | OD600 lysis time-courses | Mac | project |
| 06-26 | `code/0626_genome_comparison.ipynb` | 5-isolate ANI / CheckM / ONT comparison | Mac | project |
| 06-27 | `code/0627_unique_strain_table.ipynb` | the 3 ANI-distinct representatives table | Mac | glue |
| 07-01 | `code/0701_phagerbp_metagenome/` | PhageRBPdetect v4 (ESM-2) over 1.36 M metagenome proteins → 1,293 RBPs | **Laguna GPU** | good wrapper around a third-party model |
| 07-01 | `code/0701_pharbp_query/` | PharBP API client + BLASTP of our RBPs against it | Mac | project |
| 07-03 | `code/0703_phage_host_matrix/` | the PI's phage–host matrix, 6 steps; plus `fold/` = 3 folding back-ends | Mac + Laguna | steps project; **`fold/` retired** |
| 07-08 | `code/0708_phage_assembly/` | fastp → host removal → bbnorm → SPAdes → Pharokka/CheckV for Φ8; `check_terminal_redundancy.py` | **Laguna CPU** | pipeline template; **DTR script is a tool** |
| 07-08 | `code/0708_phage_genome_analysis.ipynb` | phage genome overview, NCBI searches, 5 figures (bilingual) | Mac | project |
| 07-08 | `code/0708_rbp_analysis/` | writeup + extracted RBP FASTAs (no executable code) | — | data/doc |
| 07-12 | `code/0712_phage_rbp_detect/` | RBP Detect on the 80 Φ8 CDS, union with Pharokka; `beta_helix_analysis.py`; `fold_binding/` | Mac + Laguna | union + β-helix scripts are tools; **`fold_binding/` retired** |
| 07-13 | `code/0713_espinoza_structural_mapping/` | **Prof. Espinoza's own** Colab notebook + his Pharokka run | Colab | not ours — attribution/permission |
| 07-16 | `code/0716_espinoza_fiber_construct/` | domain-map the AF3 folds, choose the orderable construct | Mac | project |
| 07-27 | `code/0727_o_antigen_comparison/` | extract and compare the O-antigen locus across annotated genomes | Mac | **tool** |
| 07-29 | `code/0729_prof_figures/` | circular genome diagram, phage map, 3D domain renders | Mac | project (figures) |
| 07-29 | `code/0729_t4gp10_check/` | does CDS_0010 carry a T4gp10 fragment? (no) | Mac | glue |
| 07-30 | `code/0730_synteny_group_d/` | synteny + RBH orthology vs T7/φKMV/KP32 | Mac | near-tool |
| 08-09 | `code/0809_patch_mra_manuscript.py`, `code/0809_response_letter_to_docx.py` | MRA revision paperwork | Mac | glue, absolute paths |
| 08-11 | `code/0811_promo_video/` | Remotion (React/TS) promo video, 17 files | Mac (node) | project; the only unit with a dependency manifest |
| 09-10 | `code/0910_construct_protein_mw.ipynb` | Twist `.gb` → expressed-protein MW/pI for the 6 constructs | Mac | reusable |
| 09-15 · 09-29 · 10-10 | `code/*_gel_annotation.ipynb` (3) | SDS-PAGE ladder calibration, lane densitometry, annotated overlays | Mac | **tool** (re-typed 3×) |
| 10-10 | `code/1010_resistant_mutant_comparison/` | resistant picks vs parents: mapping, variant calls, read-level confirmation, circos | Mac | **tool** |
| 10-15 | `code/1015_spot_test_dilution.ipynb` | Bradford curve → spot-test dilution table | Mac | project |
| 10-18 | `code/1018_construct_structures/` | ESMFold + PyMOL + comparison tables for the 6 expressed parts | Mac | project |
| 07-01 | `data/processed_genome/binding_screen/` | the first RBP×receptor ColabFold screen | Laguna GPU | **retired, and misfiled under `data/`** |
| 07-13 · 08-21 · 09-24 | `documents/2026-07-13_fig_binding_controls.py`, `2026-08-21_talk_slides/build.sh`, `2026-09-24_paris_travel_reimbursement/build_docx.js` | one figure; LaTeX build; reimbursement .docx | Mac | glue (the last is administrative — exclude) |

`archived/` contains no code (two superseded protocol drafts and a PDF). `code/output/`
is generated results, not a code unit.

## 2. What we should actually submit as our software

**Ranked candidates.**

1. **SDS-PAGE gel annotation and densitometry** (`0915` → `0929` → `1010`). Strongest, exactly
   *because* we re-typed it three times: ladder calibration → lane detection → densitometry →
   apparent-MW estimate → annotated overlay. Every wet-lab iGEM team needs this; the
   lightweight open alternatives are poor. Dependencies are only PIL/scipy/numpy. Consolidate
   into one library + CLI taking an image, a ladder spec and lane labels.
2. **`0727_o_antigen_comparison/`** — O-antigen locus extractor and cross-genome comparator.
   The existing serotyping tools are all species-bound (PAst is *P. aeruginosa*-only, Kaptive
   has no *Pseudomonas* DB); ours works from any Bakta/Prokka annotation. Move the locus
   keyword list into a config and it is publishable.
3. **`1010_resistant_mutant_comparison/`** — phage-resistant mutant vs parent workflow, and the
   only one that does **read-level confirmation of every candidate variant**, which is the step
   that killed this project's own false positives.
4. **Small "phage genome sanity checks" toolkit** —
   `0708_phage_assembly/check_terminal_redundancy.py` (DTR vs circularity from coverage shape,
   66 lines, stdlib; on Φ8 it returned *circular*, which is the topology we now report — it
   did **not** "correct" a circular call to linear, see
   [`2026-10-18_genome_topology_conflict.md`](2026-10-18_genome_topology_conflict.md) §4) plus
   `0712_phage_rbp_detect/fold_structure/beta_helix_analysis.py` (DB-free β-helix classification
   from a PDB).

**Second tier, with work:** the 1,673-sequence literature RBP database (the *dataset* is the
contribution — blocked on the source papers' redistribution terms and on removing the vendored
`raw/PhARIS/` notebook); `0623/receptor_fasta.py`; `0730_synteny_group_d/`;
`0701_phagerbp_metagenome/run_rbp_inference.py` (a well-built batched, resumable wrapper around
someone else's model — infrastructure, not our tool).

**Do not submit the RBP × OMP binding screen** in any of its three incarnations
(`data/processed_genome/binding_screen/`, `0703/fold/`, `0712/fold_binding/`). The method was
retired: controls failed twice across two independent tools, cross-kingdom pairs have no paired
MSA, and the receptor is an LPS sugar, not a protein. It is the largest single block of code we
wrote, and shipping it would mean shipping a method that failed its own validation.
**Submit it as a documented negative result instead** —
[`2026-07-13_why_protein_protein_binding_fails.qmd`](2026-07-13_why_protein_protein_binding_fails.qmd)
already does this well, and the 2026 rubric explicitly credits *"test data, or benchmarking"*.
That honest benchmark is a better Best Software story than a fourth copy of a failed screen.

## 3. Duplication to clean up before release

- `0620_receptor_classification.ipynb` ↔ `.py`: **93 % identical**. Keep one.
- **The binding screen, three times** (07-01 → 07-03 → 07-12): the same five stages rewritten,
  not copied (`collect_results.py` 0.62 similarity, the sbatch pair 0.59).
- **Three folding back-ends in one unit** (`0703/fold/`: ColabFold, Boltz-2, ESMFold), each with
  its own setup/split/sbatch/collect — a parameterised runner would have replaced ~15 files.
- **Qubit quantification ×6** (peak similarity 0.71), **gel annotation ×3**, **OD600 ×3**.
- **"Which proteins are receptors" implemented three times** (`0620`, `0623/receptor_fasta.py`,
  `0703/step2_host_receptors.py`) and **RBP identification four ways**.
- **Hand-rolled MMseqs2 `subprocess` calls in at least 6 units**, each re-specifying thresholds
  and each working around the space in the repo path.

## 4. Release checklist

**Blockers**

- [x] **Licence — DONE 2026-10-19.** The root `LICENSE` is CC BY 4.0 for content, and
      `software/LICENSE` is **MIT** (OSI-approved) for the packaged code; `software/README.md`
      and the root `README.md` both state the split. **The earlier claim that the CC BY 4.0
      licence blocks Best Software was wrong.** The one remaining Best Software blocker is that
      the code has not been uploaded to `gitlab.igem.org` (the deliverable reads "No
      Submissions"). Also replace the
      placeholder holder string "iGEM 2026 team" with the real team name.
- [ ] **Dependency manifest.** There is none — no `environment.yml`, no `requirements.txt`, no
      `pyproject.toml` anywhere, while four READMEs tell the reader to `conda activate igem2026`,
      an environment that exists only on one laptop. Write a top-level `environment.yml` (pandas,
      numpy, matplotlib, seaborn, scipy, biopython, pyfastani, pycirclize, pygenomeviz,
      matplotlib-venn, openpyxl, python-docx, pillow, py3Dmol, torch, transformers,
      pymol-open-source) plus the bioconda CLIs the scripts shell out to (mmseqs2, blast,
      minimap2, samtools, fastp, bowtie2, bbmap, spades, pharokka, checkv, ncbi-datasets-cli).
- [ ] **Tests.** None exist anywhere — the `run_smoke*.sh` files are manual GPU timing runs, not
      tests. The rubric scores validation; the four Tier-1 candidates each need unit tests on a
      tiny fixture.
- [ ] **One install-and-run page**, covering: the conda env; that **the repo path contains a
      space (`iGEM 26`) which breaks MMseqs2** (already worked around ad hoc in
      `0730_synteny_group_d/run_mmseqs.sh`); and that `0623/receptor_ncbi_search.py` needs an
      **`NCBI_API_KEY`** environment variable.
- [ ] **Architecture diagram** — named explicitly in the rubric, and we have none.

**Parameterise**

- [ ] Absolute `/Users/alexy/...` paths in `0809_patch_mra_manuscript.py`,
      `0809_response_letter_to_docx.py`, `0729_t4gp10_check/check_t4gp10_similarity.py`.
- [ ] The SLURM account string `jespinoza@kgi.edu_1541` appears in ~15 files — not a secret, but
      an allocation ID tied to a named person. Replace with `$SLURM_ACCOUNT`.

**No credentials are committed.** A sweep for API keys, tokens, private keys and cloud
credentials across the full history returned only false positives (protein sequences). The one
secret in use, `NCBI_API_KEY`, is read from the environment.

**Must NOT go in the public repo** (decide each deliberately, do not bulk-push):

| Path | Why |
|---|---|
| `documents/2026-09-24_paris_travel_reimbursement/` | personal travel and financial paperwork; `.gitignore` excludes `receipts/` but 4 files in the directory are tracked |
| `documents/2026-10-18_attribution_form_DRAFT.md` | named individuals' contribution statements, pre-submission |
| `documents/2026-08-08_mra_revision/` and `code/0809_*.py` | confidential peer-review correspondence (the paper itself is public: doi 10.1128/mra.00793-26) |
| `code/0713_espinoza_structural_mapping/`, `code/0716_espinoza_fiber_construct/`, `data/phage_genome/9-2-1/folds_espinoza/` | **Prof. Espinoza's own notebook, Pharokka run and AF3 folds** — third-party unpublished work; needs his permission and attribution |
| `data/phage_genome/9-2-1/` | the novel, unpublished 62 kb Φ8 genome — releasing it before deposition scoops our own paper |
| `data/bacteria_genome/*/resistant_r1_SBYK6W/` | unpublished resistant-mutant genomes (the CR3 F126L finding) |
| `data/metagenomes/` | vendor-delivered soil metagenomes — confirm the sequencing agreement allows release |
| `code/0619_literature_rbp_database/raw/` | copyrighted paper PDFs and supplementary files committed into the repo, plus a vendored clone of someone else's repository |
| `documents/2026-07-27_twist_construct_order/`, `documents/2026-09-10_..._second_set/` | vendor paperwork (the construct *sequences* are fine — they belong on the Parts pages) |
| `documents/2026-07-29_pi_conversation/` | verbatim transcript of a conversation with the PI |

Safe to publish: the three MRA isolates (8-5-2 / 9-2-1 / 8-10-2) — accessions are live and the
paper is out. Note that `.gitattributes` routes `*.JPG`, `lab_notebook/**/*.png` and two PDFs
through **git-LFS**; the GitLab mirror must have LFS enabled or those files arrive as pointer
stubs.

## 5. Suggested shape of the GitLab release

```
igem-2026-claremont-software/
  README.md            what each tool is, install, quickstart, the "Judging" block
  LICENSE              MIT or Apache-2.0 for code  (CC BY 4.0 stays for docs/figures)
  environment.yml
  docs/architecture.md + architecture diagram
  gelquant/            tool 1 — SDS-PAGE densitometry      (+ tests, sample gel)
  olocus/              tool 2 — O-antigen locus comparator (+ tests, sample annotation)
  phageresist/         tool 3 — resistant-mutant workflow  (+ tests, tiny BAM fixture)
  phagecheck/          tool 4 — DTR / β-helix sanity checks(+ tests, tiny fixture)
  benchmarks/          the retired binding screen as a documented negative control
  examples/            one runnable example per tool, with expected output
```

---
*Log — 2026-10-18: compiled by sweeping every code unit in the repo. Line counts are non-blank
lines, notebooks counted by code cells only. Companion documents:
[`2026-10-18_igem_special_prize_benchmark.md`](2026-10-18_igem_special_prize_benchmark.md),
[`2026-10-18_parts_structure_comparison.md`](2026-10-18_parts_structure_comparison.md).*
