# olocus — O-antigen locus extractor and comparator  *(port in progress)*

**Source:** `code/0727_o_antigen_comparison/` in the project repository —
`extract_o_antigen_loci.py` (171 L), `compare_loci.py` (141 L), `plot_loci.py` (163 L),
`plot_summary_figs.py` (109 L). Working code with its own README; it produced the O-antigen
result in the 2026 synthesis documents.

**Why it is worth packaging.** Every in-silico O-polysaccharide typer is species-bound — PAst
covers *P. aeruginosa* only, Kaptive has no *Pseudomonas* database, and no reference serotype
scheme exists for *Pseudomonas_E* sp013179515. So for most non-model organisms the question
"what is the O-antigen here, and does it differ between my strains?" has **no** available tool.
This one answers it structurally instead of by serotype: it locates the cassette by its conserved
flanks and compares loci directly.

Finding it reproduces: three ANI-distinct strains carry three **non-homologous** O-antigen
cassettes in the same `ihfB`-flanked slot, sharing only 4 of 45 ortholog clusters.

## What must change before release

1. **Anchor genes are hard-coded** for the *Pseudomonas* OSA cluster (30S S1 → `ihfB` →
   LPS assembly protein A → MBL fold metallo-hydrolase). Move them to a YAML config with one
   named profile per organism, so a reuser can supply their own flanks.
2. **Strain paths are hard-coded** to `data/bacteria_genome/<strain>/annotation/`. Take an input
   directory and a sample sheet instead.
3. **Cassette-end detection keywords** (the polysaccharide-biosynthesis gene list and `GAP`
   tolerance) belong in the same config.
4. Split the four scripts into `extract` / `compare` / `plot` modules behind one CLI
   (`python -m olocus extract ...`), and add tests on a miniature two-contig annotation fixture.
5. Keep the written rationale from the source README — the explanation of *why* an anchor-based
   extraction beats fixed coordinates is the part a reuser needs.
