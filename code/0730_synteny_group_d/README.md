# 0730 — Synteny + similarity: is 9-2-1 Φ8 a T7-like podophage, group D?

Answers the PI's 2026-07-29 ask: *justify the "T7-like podophage, looks like
group D" call **with synteny and similarity**, and confirm the structural-module
identity of CDS_20/08/09/13/14* (transcript in
[`../../documents/2026-07-29_pi_conversation/`](../../documents/2026-07-29_pi_conversation/)).

## TL;DR

**Podovirus, yes — by organization. Autographiviridae/T7 *sensu stricto*, no.
Group-D-*like*, not group D.**

1. **The virion module is a canonical podovirus module in canonical order.** On
   the minus strand, 5′→3′: **portal (CDS_0020) → major capsid (0017) → head/tail
   adaptor structural (0016/0014/0013) → tail spike (0011) → tail (0010) → tail
   fiber (0009) → internal virion / ejection protein (0008)**. This is the PI's
   point — CDS_20/08/09/13/14 tell you it is a podo/T7-like particle **without
   TEM**. See `tables/synteny_similarity.tsv`.
2. **But it shares ~0 detectable orthologs with cultured T7-likes.** Reciprocal
   best hits: T7↔KP32 = 40, T7↔φKMV = 6, φKMV↔KP32 = 6, but **9-2-1 Φ8 ↔ any = 0**
   (one spurious 82-aa hit on the 7.5 kb DarB antirestriction gene). Positive
   controls pass (see below), so the absence is real. `tables/ortholog_matrix.tsv`.
3. **It is a novel, large (62 kb), likely-temperate podovirus.** ~62 kb is far
   above the ~40 kb of T7/φKMV/KP32, and it carries a large
   replication/recombination + **excisionase/lysogeny** module (RecE/RecT-like,
   Erf, Holliday-junction resolvase, 2× excisionase, DNA MTase) — consistent with
   the "possibly temperate" note in the genome-sequencing record. So **"T7-like"
   is an organizational analogy of the virion module, not a phylogenetic
   placement.**
4. **The tail is group-D-*like*, not group D.** Latka & Briers 2019 define KP32virus
   **group D** by a first RBP that is a **T4gp10-like anchor without an enzymatic
   domain**, plus a second depolymerase RBP. Our tail has the *arrangement* — an
   anchor-position fiber (CDS_0010, function unknown) + a depolymerase tail spike
   (CDS_0011) + a second GH5 depolymerase (CDS_0012) — **but CDS_0010 carries no
   T4gp10 segment** (checked, negative: [`../0729_t4gp10_check/`](../0729_t4gp10_check/)).
   The T4gp10 hallmark that *defines* group D is absent, so **group-D-like**.
   Cross-genus RBP sequence similarity to KP32viruses is undetectable, as
   expected for hypervariable RBPs.

## The figure

`code/output/0730_synteny_group_d/fig_synteny_4genome.{png,svg}` — four genome
tracks (9-2-1 Φ8 on top, then φKMV / T7 / KP32), genes coloured by functional
class, grey ribbons = RBH orthologs between adjacent tracks. Reads at a glance:
the three cultured T7-likes are tied together by a conserved core; 9-2-1 Φ8 has
**no ribbons** (novel) yet keeps the podovirus virion-module block (bracketed).

## Method

Reference proteomes from RefSeq GenBank: **T7** `NC_001604` (Autographiviridae
type), **φKMV** `NC_005045` (*Pseudomonas* T7-like, host-matched), **KP32**
`NC_013647` (Latka's KP32virus genus). Our proteome is the PI's canonical
`UUAIURNK_` Pharokka run (numbering adopted repo-wide 0716). Orthology by
`mmseqs easy-rbh`; our-vs-ref also re-checked with sensitive `easy-search -s 7.5`.

- `extract_proteomes.py` — parse the four genomes → `work/*.faa` + `*.tsv`
- `run_mmseqs.sh` — RBH + sensitive search (run in a **no-space** dir; mmseqs
  breaks on this repo's path space — see memory `local_env_gotchas`)
- `analyze_and_plot.py` — tables + figure

**Positive controls (pipeline is sound):** φKMV↔T7 recovers 6 orthologs at
25–33 % id (DNA pol, terminase, portal, capsid…); self-search hits 80/80. So the
9-2-1 Φ8 zero is a true negative, not a broken search.

## The group-D exemplar was not downloaded

Latka's group-D reference (Klebsiella phage 2044-307w) has no clean RefSeq
accession, and cross-genus RBP similarity would be undetectable anyway. The
group-D-*like* comparison therefore rests on the architecture (Latka's textual
definition) + our own tail-module map, not on a pairwise RBP alignment. **UNDONE**
if we ever want the alignment: pull 2044-307w from the paper's supplement.

---
*Log — 2026-07-30: built for the PI's C3/C4 (2026-07-29 conversation). Core
finding — 9-2-1 Φ8 is a novel ~62 kb podovirus: podovirus virion synteny is
clear and confirms the CDS_20/08/09/13/14 module (C4), but it shares no
detectable orthologs with T7/φKMV/KP32 and carries a lysogeny/recombination
module, so "T7-like" is organizational only. Tail is group-D-like (anchor fiber +
depolymerase spike) but lacks the defining T4gp10 anchor (C5), so not group D
sensu stricto. Group-D exemplar 2044-307w left UNDONE (no accession).*
