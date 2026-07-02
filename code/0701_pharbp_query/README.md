# 0701 — PharBP query (bacteria receptors ↔ recorded RBP/phage pairs)

Task: on [PharBP](https://pharbp.ugent.be/) (UGent Boeckaerts group, same lab as
PhageRBPdetection) check whether our bacterial receptors appear and whether there are
recorded pairs, via its API.

## Key finding that reshaped the task
**PharBP is a phage-RBP database, not a receptor database.** Each entry maps an RBP
(tail fiber / tailspike) → its **phage** and → its **host bacterium**. There is **no
field for the bacterial receptor** (LPS / a named OMP / pili / flagella), and the only
"pairs" are RBP↔host, mostly *computationally predicted* — not experimentally validated
RBP–receptor pairs. So our 441 bacterial receptors cannot be "looked up" here, and
BLASTing receptor (OMP) sequences against an RBP DB is biologically mismatched.

We therefore run the two things the DB *can* answer (confirmed with the professor's
intent = both):
- **Track A** — pull all Pseudomonas-host RBPs recorded in PharBP (the closest thing to
  "recorded pairs": phage–host, with structures/evidence).
- **Track B** — BLASTP our predicted RBPs (the 1,293 metagenome RBPs from
  `0701_phagerbp_metagenome/`) against PharBP to find catalogued homologs and read off
  their phage/host — i.e. which of *our* RBPs resemble known ones.

## API mechanics (verified live, no auth needed)
- CSV export: `GET /export/results/?host_genus=Pseudomonas&unique=1&download=csv`.
- BLASTP: `GET /blastp/` to obtain the `csrftoken` cookie → `POST /api/blastp/upload/`
  with form field `sequence=` (ONE sequence per call — multi-FASTA is concatenated!),
  sending `X-CSRFToken` header + matching `Referer`; completes synchronously and returns
  a `query_id` → `GET /api/blastp/results/<query_id>/` = `{total, results:[{protein_id,
  phage_name, host_names[], percent_identity, evalue, bit_score, query_coverage, …}]}`.
- FoldSeek (structure search) exists too but we have no structures for these RBPs.

## Scripts
- `pull_pseudomonas_rbps.py` — Track A: export + summarise.
- `blast_rbps_vs_pharbp.py` — Track B: CSRF handshake, per-sequence BLASTP (dedups
  identical sequences, resumable, polite rate-limit), top-N hits per RBP with phage/host.

## Results
**Track A — Pseudomonas RBPs in PharBP:** 198 unique RBP records, 60 phages, 21 host
strains; 22 records have a P. putida-group / non-aeruginosa host (closest to our
*Pseudomonas_E* isolates — most of the DB's Pseudomonas is *P. aeruginosa*).
→ `output/0701_pharbp_query/pseudomonas_rbps.csv` + `_summary.md`.

**Track B — our RBPs vs PharBP:** (full 1,293 run; see `rbp_vs_pharbp_hits.tsv`).
Validation on the first 30 RBPs: only 8/30 had any hit, all at low identity (30–46%) to
*non-Pseudomonas* phages (Salmonella/Cyano/Bacillus-prophage). Preliminary signal: our
soil-metagenome RBPs are largely **novel** relative to catalogued RBPs. Final counts +
host/phage distribution filled in after the full run.

## Outputs (`code/output/0701_pharbp_query/`)
- `pseudomonas_rbps.csv`, `pseudomonas_rbps_summary.md` — Track A.
- `rbp_vs_pharbp_hits.tsv` — Track B: `query_rbp_id, hit_rank, n_hits, protein_id,
  percent_identity, evalue, bit_score, query_coverage, phage_name, host_names`.

## Caveats
- No receptor dimension in PharBP → receptor↔RBP pairing must come from our own in-silico
  fold screen (`data/processed_genome/binding_screen/`), not this DB.
- Host taxonomy match is genus-level only (ours = *Pseudomonas_E* sp013179515 / *P.
  capeferrum*; DB = mostly *P. aeruginosa*).
- PharBP RBPs are largely predicted, not experimentally validated binders.

---
*Log — 2026-07-01: researched PharBP + API; DB has no receptor field so reframed to
Track A (198 Pseudomonas RBPs) + Track B (BLAST our 1,293 RBPs). API/CSRF verified live.*
