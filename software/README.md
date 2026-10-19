# iGEM 2026 Claremont — software

Four small tools that came out of a phage-therapy project against soil *Pseudomonas*, plus one
documented negative benchmark. Each tool answers a question we hit in the lab and could not find
a usable open tool for.

| Tool | Question it answers | Status |
|---|---|---|
| [`phagecheck/`](phagecheck/) | Is this phage assembly circular, or linear with a terminal repeat? Is this predicted fold a β-helix depolymerase? | **ported, tested** |
| [`olocus/`](olocus/) | Where is the O-antigen locus in these annotated genomes, and how do the loci differ between strains? | port in progress — [see notes](olocus/README.md) |
| [`gelquant/`](gelquant/) | What size is that SDS-PAGE band, and how much is in the lane? | port in progress — [see notes](gelquant/README.md) |
| [`phageresist/`](phageresist/) | Which mutations distinguish a phage-resistant isolate from its parent, confirmed at read level? | port in progress — [see notes](phageresist/README.md) |
| [`benchmarks/`](benchmarks/) | Can protein–protein docking predict phage receptor binding? (No — and here is the control data.) | written up |

**Licence:** code is **MIT** ([`LICENSE`](LICENSE)). The project wiki, figures and written
documentation remain CC BY 4.0, as iGEM requires. Keeping these separate is deliberate: CC BY is
a content licence and is not OSI-approved, and Best Software requires an OSI-approved licence for
the code.

## Install

```bash
conda env create -f environment.yml
conda activate igem2026-software
python -m pytest phagecheck/tests -q      # 11 tests, < 2 s, no external data needed
```

Nothing here needs a GPU, a cluster account or an internet connection at run time.
**Avoid spaces in the checkout path** — MMseqs2, which some tools shell out to, breaks on them.

## Quickstart

```bash
# Is the assembly circular, or linear with a DTR?
python -m phagecheck.dtr contig.fasta reads_R1.fastq.gz reads_R2.fastq.gz

# Is this predicted structure a beta-helix depolymerase?
python -m phagecheck.betahelix fold.pdb --out fold_calls.tsv
```

Both print a table; both take `--help`. `phagecheck` is importable as a library
(`from phagecheck import check, classify`) and returns dataclasses, not printed text.

## Why these tools exist

**`phagecheck.dtr`** — assemblers report a phage contig as "circular" whenever the ends overlap,
which is also exactly what a **direct terminal repeat** on a linear genome looks like. The two
are distinguishable from coverage alone: a collapsed DTR receives reads from both genome ends and
shows a ~2× k-mer coverage spike, while a truly circular genome is flat. On our own phage
9-2-1 Φ8 it returned **`CIRCULAR / no short linear DTR`** (median ~357×, max/median 1.63×, no
qualifying run ≥ 15 bp), against a string-level reading of the contig ends that had been taken as
linear with a 77 bp DTR. The circular call is the one the project now reports, in agreement with
the PI's assembly; the disagreement and what is still untested are written up in
[`2026-10-18_genome_topology_conflict.md`](../documents/2026-10-18_genome_topology_conflict.md).
No aligner, no database, pure Python.

**`phagecheck.betahelix`** — tail-spike depolymerases are built on a right-handed β-helix, and
that fold has a database-free signature: the sequence-offset distribution of backbone hydrogen
bonds peaks at the coil period (~16–26 residues) because adjacent coils bond in register. An
α-helix peaks at offset 4; a β-sandwich has no periodic peak. We used it to call the Φ8 tail spike
a β-helix without Foldseek or a structure database.

## Judging — the six Best Software aspects, answered

*(iGEM's own rubric, answered one by one; this section is for judges.)*

1. **Compatible with synthetic-biology standards?** Inputs and outputs are the formats the field
   already uses: FASTA and FASTQ in, PDB in, TSV/CSV out. No bespoke formats, no database
   required. Nothing is SBOL-encoded — our objects are assemblies and structures, not genetic
   circuits — but every output is a flat table that joins on a part or contig identifier.
2. **How well is it validated?** `phagecheck` ships 11 unit tests, including simulated linear-with-
   DTR and circular genomes where the right answer is known by construction, and a regression test
   on the real Φ8 tail spike. Both tools are also validated against the project's own wet-lab
   record: the DTR check's circular verdict on Φ8 is the topology the project now reports, and
   the β-helix call is consistent with the AlphaFold3 template evidence. `benchmarks/` goes
   further and publishes a method of ours that **failed** its controls, with the control data.
3. **Useful to other projects?** Any team sequencing a phage faces the circular-vs-DTR question,
   and any team predicting a tail fiber faces the fold question. Neither tool contains anything
   specific to our phage or our host.
4. **Integrable?** Importable Python with dataclass returns, plus a CLI per tool. No service, no
   account, no network calls.
5. **User-friendly?** One conda command to install, one command to run, `--help` on everything,
   and defaults that work (k=31, 150 k reads, 1.6× median threshold).
6. **Written and documented for future groups?** Module docstrings explain the *method*, not just
   the API; parameters are named constants, not magic numbers; tests are the executable
   documentation; [`docs/architecture.md`](docs/architecture.md) has the architecture diagram and
   the data flow.

## Provenance

These tools were extracted from the project repository; each module names the analysis directory
it came from. The analyses that produced the science live there, with their own READMEs and dated
logs. Work by our PI (AlphaFold3 folds, the GH5 phylogeny and ancestral reconstruction, his
Pharokka annotation) is **not** included here — it is his, not the team's.

---
*Log — 2026-10-18: created. `phagecheck` ported and tested; the other three staged with porting
notes. See [`../documents/2026-10-18_software_inventory.md`](../documents/2026-10-18_software_inventory.md)
for the full code inventory and the release checklist.*
