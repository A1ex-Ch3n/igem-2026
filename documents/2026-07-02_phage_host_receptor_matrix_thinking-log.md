# Phage–host receptor interaction matrix — thinking log

**Started:** 2026-07-02 (PI task) · **Status:** planning + foundation built · **Code:** `code/0703_phage_host_matrix/`

A retrospective record of how we're approaching the PI's "interaction matrix" task — the
reasoning, the dead-ends we ruled out, the data facts we established, and the decisions
made. Purpose: so we (or future related tasks) can reload the thought process quickly.
Builds directly on the PharBP-query task ([`2026-07-01_pharbp_query_report.md`](2026-07-01_pharbp_query_report.md)).

## 1. The PI's initial task (Cesar Espinoza, WhatsApp, 2026-07-02)

Proposed a 4-step workflow:
1. Download all the predicted receptors for known Pseudomonas phages (~6000)
2. Identify all unique hosts (~60)
3. Predict/identify the shared receptors with our genomes (BLAST is fine now)
4. Make a giant interaction table

Follow-up when we flagged the receptor-vs-RBP problem (below), the PI clarified:
> "yes I know, but this would give us good clues … we won't know to which receptor for
> sure, but we know if a particular bacteria has a receptor."

So the PI **accepts a clue-level (presence/homology) analysis** — he is NOT asking for
exact RBP↔receptor binding.

## 2. The core reasoning chain (why the task is shaped this way)

Goal: **which phages could infect our 3 sequenced isolates?** Can't be answered directly
(our isolates are novel, no known phage, absent from every database), so we step back:

```
Q0 which phages infect our strains?           ✗ novel isolates, no known phage
Q1 which phages' RBPs bind receptors WE have?  ✗ no DB stores RBP↔receptor; needs folding
Q2 which phages' HOSTS share receptors with us? ✓ computable by BLAST  ← the PI's clue level
```

Q2 logic: phage P infects host H → P binds *some* receptor on H → if H and we share a
receptor R (high identity) → P may also bind our R → **P is a candidate**. The matrix
systematises this. Cells are **presence + % identity** ("does this phage's host carry a
receptor homologous to ours"), NOT a binding score — because binding needs simulation and
the PI is fine with the weaker clue.

## 3. The key facts we established (from the PharBP-query task + probing)

- **PharBP stores RBP → phage → host *name*. It has NO bacterial-receptor field**, and no
  RBP↔receptor pairing. → the matrix cells cannot be "downloaded"; the receptor side must
  be built ourselves from host genomes (NCBI + annotation).
- **The real Pseudomonas scope in PharBP:** by phage name, ~1,480 phages / **8,227 RBP
  records** / ~57 (messy) host strings (1,911 records have no host). *This* matches the PI's
  "~6000 / ~60" — not the 198/21 we first pulled with the narrow `host_genus=Pseudomonas`
  filter. Dominated by *P. aeruginosa* and *P. syringae*.
- **Receptor-sharing already computed in 0623** (`out_receptor_ncbi/carrier_organisms.tsv`,
  390 organisms): the hosts most similar to us at high identity (hunanensis, alloputida,
  fortuita, capeferrum…) mostly have **0 phages**; the one host that is *both* highly
  similar (99.4% id, 98 shared receptors) *and* phage-rich (**139 phages**) is **P. putida**.
  Secondary: plecoglossicida (95.9%, 7), taiwanensis (95.8%, 4). Meanwhile PharBP's dominant
  aeruginosa/syringae share with us only at 78–87% id (far). → **P. putida is the standout
  surrogate host; its phages are the top candidates.**

## 4. Where the PI's workflow was inefficient, and our corrections

1. **Wrong columns.** "6000 host receptors" is unnecessary — the receptors that matter are
   the ones WE have. Columns collapse to our own ~106–144 receptor groups; no 60-host
   genome download needed just to define columns.
2. **Lookup assumption.** "Make an interaction table" implies the interactions are
   downloadable. They aren't (no RBP↔receptor data). Cells are presence/homology now; a
   fold/ipTM layer is optional, later, only for top candidates.
3. **Redundancy.** Our 3 site isolates (9-6-2/9-2-1/10-10-2) are ~one strain; 8-10-2 is a
   distinct species (capeferrum). Reference is really ~2 receptor sets, not 3–5.

## 5. Decisions made (with the user)

- **Redo the host-receptor overlap fresh, from PharBP** (not just reuse 0623) — for clean
  data provenance and easier debugging. 0623 becomes a cross-check.
- **Self-annotate receptors at scale** (many host genomes) via code kept in the repo,
  runnable **locally or on Laguna**.
- **Keep all 5 sequenced isolates as reference columns** despite redundancy — makes it
  easier to spot clues later (core vs strain-specific receptors).
- **First concrete artifact:** a receptor × strain presence table for our isolates + a
  Markdown repertoire summary (done — see §6).

## 6. Current status

**Done:**
- `code/0703_phage_host_matrix/build_receptor_by_strain.py` — clusters our 441 receptors
  (mmseqs, 90% id / 80% cov) across all 5 isolates.
- `code/output/0703_phage_host_matrix/receptor_by_strain.tsv` — 144 receptor groups ×
  5 strains presence matrix.
- `code/output/0703_phage_host_matrix/receptor_by_strain.md` — repertoire summary
  (43 core groups shared by all 5; 46 capeferrum-specific; per-class counts).

**Next (planned):**
1. Retrieve + clean the full list of Pseudomonas hosts from PharBP (resolve messy host
   strings → downloadable NCBI genomes).
2. Download those host genomes, annotate receptors (same rules as 0623 `receptor_fasta.py`),
   run locally or on Laguna, code in repo.
3. BLAST our receptors vs each host → build the host × our-receptor overlap table
   (cells = % identity), focusing on hosts that are both phage-rich and receptor-similar.
4. Join PharBP RBP sequences for the top hosts; optional fold/ipTM on the shortlist.

## Related files
- PharBP-query report: `documents/2026-07-01_pharbp_query_report.md`
- Our receptors (canonical): `code/0623_metagenome_rbp/out_receptor_fasta/receptors_all.tsv`
- 0623 surrogate-host overlap: `code/0623_metagenome_rbp/out_receptor_ncbi/carrier_organisms.tsv`

---
*Log — 2026-07-02: PI proposed matrix task. 2026-07-03: reasoning worked out (clue-level,
not simulation), PharBP scope corrected (~8k RBP / ~57 hosts), receptor×strain reference
table built. Next = host-receptor overlap from PharBP.*
