# Unified phage RBP reference database

Receptor-binding proteins (RBPs) aggregated from three literature sources into one
FASTA + metadata table. Built by
[`../../0619_literature_database/build_rbp_database.ipynb`](../../0619_literature_database/build_rbp_database.ipynb).
(中文版:[`README_zh.md`](README_zh.md))

## Files

| File | Rows | What |
|---|---|---|
| `rbp_database.fasta` | **1673** | unique RBP protein sequences (one per 100 %-identity cluster); header = `rbp_id` |
| `rbp_metadata.tsv` | 2447 | one row per source RBP (incl. exact duplicates), full schema + cluster cross-refs |
| `rbp_clusters.tsv` | 2447 | `rbp_id → cluster_rep_100 / cluster_rep_95` (MMseqs2 membership) |
| `pseudomonas_rbp_candidates.fasta` | 115 | *Pseudomonas* slice, for the binding screen (`../../0616_binding-screen-fold-plan.md`) |

## Sources

| `source` | Paper | RBPs (rows / unique) | Annotation key |
|---|---|---|---|
| `boeckaerts2021` | Boeckaerts et al. 2021, *Sci Rep* — host prediction from RBPs | 1232 / 933 | by host (9 species) |
| `krusche_chm` | Krusche et al., *Cell Host & Microbe* (PhARIS) | 575 / 266 | by cluster; all bind WTA; `rbp_type` = main (irreversible) / reversible |
| `moriniere2026` | Moriniere et al. 2026, bioRxiv (GenoPHI) | 640 / 474 | by receptor + class; `confidence` provenance |

Unique-DB host distribution: *E. coli* 792, *S. aureus* 320, *K. pneumoniae* 175,
*P. aeruginosa* 115, *S. enterica* 114, *A. baumannii* 64, *C. difficile* 21,
*E. cloacae* 17, *Shigella* spp. ~17.

## Schema (`rbp_metadata.tsv`)

`rbp_id, source, phage_name, host_species, rbp_type, cluster, receptor,
receptor_class, accession, seq_length, is_pseudomonas, confidence,
protein_sequence, cluster_rep_100, cluster_rep_95`

`confidence` values: `literature_annotated` (Boeckaerts/Krusche — taken as the
papers report them); `experimentally_validated` / `af3_validated` / `kmer_candidate`
(Moriniere, see caveats).

## Cluster membership (`cluster_rep_100`, `cluster_rep_95`)

**MMseqs2** groups sufficiently similar sequences into clusters, each electing one
*representative*. "Cluster membership" records, for every sequence, **which cluster it
belongs to and which sequence is its representative**. Two stringencies are stored:

| Column | Threshold | Purpose |
|---|---|---|
| `cluster_rep_100` | 100 % identical | **dedup** — identical sequences collapse to one; only the rep enters the FASTA |
| `cluster_rep_95` | 95 % similar | **cross-source redundancy** — near-identical (but not identical) sequences grouped |

Reading rule: **a row is a representative iff its `rbp_id` equals its `cluster_rep_100`**
(those are the 1673 that go into `rbp_database.fasta`); otherwise it is a duplicate
absorbed by that representative.

- *Example (100 %):* cluster `krusche_0074` holds **28 identical sequences**
  (different *S. aureus* phages carrying the very same RBP) — all 28 kept in the
  metadata, only `krusche_0074` written to the FASTA. This is the 2447 → 1673 dedup.
- *Example (95 %):* cluster `boeckaerts_0009` (1026-aa *E. coli* RBPs) contains rows
  from **both** Boeckaerts and Moriniere — the two papers independently deposited
  near-identical copies of the same RBP. Their `cluster_rep_100` differ (sequences are
  95 %, not 100 %, identical) so both remain in the FASTA, but `cluster_rep_95` flags
  them as the same RBP. This is the cross-source overlap reported below.

So this lets you trace which sequences are duplicates / near-duplicates of which
representative, without losing any source provenance during dedup.

## How RBPs were extracted

- **Boeckaerts, Krusche** — direct parse of the deposited RBP sets (GitHub).
  Krusche's `RBPs_main/` + `RBPs_rev/` FASTAs already contain every clustered
  per-phage RBP, so no pipeline rerun was needed.
- **Moriniere** — the supplementary data is *feature-centric*: Dataset S6 lists every
  protein carrying a receptor-predictive k-mer (~20 proteins/phage, **not** all RBPs).
  The RBP for each `(phage × receptor)` is the protein carrying the **most predictive
  k-mers** for that receptor, after first assigning each protein to its single
  argmax-feature receptor (so one protein is never smeared across receptors —
  validated: EV240 *gp38* lands only on OmpA, matching the paper). Receptor
  assignments are then tagged with curated provenance.

## Caveats

- **Moriniere RBPs are heuristic.** `experimentally_validated` (66, Tables S8/S9) and
  `af3_validated` (107, Table S5) are paper-curated; `kmer_candidate` (467) are
  inferred and should be treated as candidates. AlphaFold3 validation is **OMP-only**,
  so LPS-core-sugar (Kdo/Hep/Glu) and NGR receptors are never `af3_validated` — the
  same protein-vs-polysaccharide blind spot noted in the binding-screen plan.
- **Coverage vs the papers' own ground truth** (since Dataset S6 is the only sequence
  source, a curated pair is captured only if its RBP carries predictive k-mers there):
  **149/163** AF3-validated pairs and **66/83** experimentally-validated pairs are
  captured; the rest have no recoverable sequence in Dataset S6 and are absent.
- **Boeckaerts** is the *collected* set (pre-dereplication); 1232 rows → 933 unique.
  The paper's final model used 887 after extra length filtering.
- Cross-source 95 %-identity redundancy: 16 clusters Boeckaerts↔Moriniere (*E. coli*),
  6 Boeckaerts↔Krusche (*S. aureus*) — preserved in metadata, collapsed in the FASTA.
- `is_pseudomonas` flags all *Pseudomonas* hosts (115 unique, all *P. aeruginosa*);
  these phages are *P. aeruginosa*, a proxy for the team's environmental *Pseudomonas*.

## Reproducing

Raw deposits are cached in `../../0619_literature_database/raw/` (gitignored). Re-fetch
commands are in the notebook's first cell; then run the notebook (cwd = `code/`'s
notebook dir). Needs `mmseqs`, `pandas`, `openpyxl`.

---
*Log: 2026-06-19 — initial build. 3 sources → 2447 RBP rows → 1673 unique sequences.*
