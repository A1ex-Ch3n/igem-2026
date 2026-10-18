# phageresist — resistant isolate vs parent, with read-level confirmation  *(port in progress)*

**Source:** `code/1010_resistant_mutant_comparison/` — `map_reads.sh` (minimap2 + samtools, 38 L)
and `resistant_vs_parent.ipynb` (631 L: assembly QC, variant calling, read-level confirmation,
allele table, circos and synteny plots). The best-documented analysis in the project repository.

**What it does.** Given a phage-resistant isolate and its sensitive parent, maps both read sets to
one reference frame, calls candidate differences, and then — the step that matters — **goes back
to the reads at every candidate position** and reports the supporting depth, so that assembly
artefacts are separated from real mutations.

**Why it is worth packaging.** Isolating phage-resistant mutants is one of the most common
phage-therapy experiments there is, and the usual pipeline (assemble both, diff the assemblies)
produces false positives that look exactly like results. In our own run, read-level confirmation
reduced a list of candidate differences to **one** confirmed change (a capsule-type-cluster
missense), with the rest explained as assembly noise.

## What must change before release

1. Split the notebook into a library (`map`, `call`, `confirm`, `report`) plus a thin notebook that
   only tells the story.
2. Reference paths, sample names and the ENA accession used for comparison are hard-coded.
3. `map_reads.sh` assumes minimap2 and samtools on `PATH` and writes BAMs next to the inputs;
   make the output directory an argument.
4. Tests need a tiny fixture: a 2 kb reference, a parent and a mutant read set with one known
   substitution, so that both the call and the read-level confirmation have a known answer.
5. Keep the honest reporting of the negative case — "no confirmed mutation in this isolate" is a
   result the tool must be willing to print.
