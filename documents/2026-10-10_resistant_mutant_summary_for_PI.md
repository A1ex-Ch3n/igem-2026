# Φ8-resistant picks — genome result (for Prof. Espinoza)

**Subject:** WGS of the Φ8-resistant picks (9-2-1 R1, 9-6-2 R1) — one mutation, in a capsule-type polysaccharide cluster

Hi Prof. Espinoza,

The Plasmidsaurus genomes of the two Φ8-resistant picks (9-2-1 R1 and 9-6-2 R1) are back and analysed.

**Bottom line:** 9-6-2 R1 carries one confirmed mutation, a missense change (F126L) in a Stealth-family
sugar-phosphotransferase inside a capsule-type polysaccharide biosynthesis cluster. 9-2-1 R1 has no confirmed
mutation. In both picks the O-antigen cassette and the LPS core genes are unchanged.

**What we did**
- Aligned each resistant genome to its parent, then checked every difference against the raw reads.
- The ONT parent reads (SRR39379361) served as a baseline with the same chemistry. 9-2-1 host reads from the Φ8
  Illumina run (71× coverage) gave a check that is independent of ONT.

**Findings**
1. **Both picks are the parental strain and are intact.**
   - 99.7–99.95 % of reads map to the parent.
   - Each is one closed chromosome, colinear with the parent, with no structural change.
   - There is no Φ8 sequence in either genome, so they are not lysogens.
2. **Most assembly-level differences are sequencing noise.**
   - Two ONT assemblies of the same clone already differ at 11–48 sites, which matches the 16–21 sites between
     each mutant and its parent.
   - About 30 sites per lineage are ONT systematic errors: 30–50 % of reads carry the alternative base in every ONT
     read set, the parent included, but 0 % of the Illumina reads do.
3. **9-6-2 R1 has one real mutation: 4,643,730 T>C, Stealth protein CR3 (OHPLIO_04215), F126L.**
   - Read support: 263 of 264 mutant reads, versus 0 of 176 parent ONT reads, 0 of 60 parent Illumina reads and
     0 of 422 reads from 9-2-1 R1.
   - The gene sits in a 30 kb cluster (4.64–4.67 Mb) with an ABC polysaccharide export system (permease,
     ATP-binding protein, outer-membrane export protein) followed by sugar- and glycerol-phosphate enzymes (TagD,
     CDP-glycerol glycerophosphotransferase, CapA). Stealth proteins are predicted to build phosphodiester-linked
     capsule/EPS polymers (Sperisen et al. 2005).
4. **9-2-1 R1 has no confirmed mutation.** Three low-frequency calls (~30 % of reads) look like ONT errors.
5. **The O-antigen cassette (1.41 Mb) and the LPS core *waa* genes are untouched in both picks.**

**Interpretation and caveats**
- The one resistance-associated change points to a capsule-type polysaccharide rather than the O-antigen. This
  does not rule out the O-antigen as Φ8's receptor, because a capsule could also mask it.
- The picks were never phenotyped as resistant, and we have only one clone per host.

**Proposed next steps**
1. PCR and Sanger sequencing of OHPLIO_04215 in all six picks (9-2-1 R1–R3 and 9-6-2 R1–R3). This confirms the
   mutation independently and shows whether other picks hit the same gene.
2. A spot/EOP test of Φ8 on the sequenced R1 clones.
3. If 1 and 2 hold: compare polysaccharide or Φ8 adsorption between 9-6-2 R1 and the parent.

Figures (circular genome map, cassette comparisons, read evidence) and the full notebook:
`code/1010_resistant_mutant_comparison/`.

Best,
Alex

---
*Log — 2026-10-10: drafted from `code/1010_resistant_mutant_comparison/resistant_vs_parent.ipynb`.*
