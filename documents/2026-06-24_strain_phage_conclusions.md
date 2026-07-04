# Strain & Phage Conclusions

- Our 3 site isolates (9-6-2, 9-2-1, 10-10-2) are nearly identical to each other (~99.4–100% ANI). They are the same strain.
- They anchor to *Pseudomonas* sp. CM27 (GCA_013179515.1) at ~99.2% ANI. CM27 is the closest known strain.
- They are not close to anything else. The next-nearest public strain drops to ~89% ANI: *P. kurunegalensis* ANKC.G2 (CP127871.1) — a different species.
- They are unlikely to be *P. aeruginosa* PAO1 (GCF_000006765.1, ~80% ANI) or *P. putida* NBRC 14164 (GCF_000412675.1, type strain, ~89% ANI).
- We do not yet know any phage that will infect them.
- So we switched to a protein-wise approach: scanned each genome's Bakta annotation and pulled out only the surface receptor proteins (porins, TonB-dependent receptors, OmpA/W, TolC, LptD, FadL, Tsx, ushers, flagellin, pilin) that a phage could bind. Found **264 receptors** (88 / 88 / 86 per strain) — see `code/0623_metagenome_rbp/out_receptor_fasta/`.
- We then searched those receptors against 395 named NCBI Pseudomonas reference genomes to find **surrogate phage hosts** — named bacteria carrying near-identical receptors that *do* have known phages. The closest relatives (P. hunanensis, fortuita, monteilii, kurunegalensis, ~97–99% id) mostly have **no known phages**. The standout surrogate host is **_P. putida_**: shares **57 receptors at up to 99.4% identity** and has **139 phage records** — its phages are the best candidates to test. Others: P. plecoglossicida, taiwanensis, fulva, parafulva, entomophila (~95–96% id, few phages). See `code/0623_metagenome_rbp/out_receptor_ncbi/surrogate_hosts.md`.
- Caveat: receptor identity is a weak proxy for phage host range (phages read variable surface loops) — these are leads to test, not guarantees.

---
*Log: 2026-06-23 — created. Based on ANI results in `code/0623_metagenome_rbp/out_finding_rbps/ani/`.*
*Log: 2026-06-24 — added receptor-mining conclusion (264 receptors via `code/0623_metagenome_rbp/receptor_fasta.py`).*
*Log: 2026-06-24 — added surrogate-host search (P. putida standout; `receptor_ncbi_search.py`).*
