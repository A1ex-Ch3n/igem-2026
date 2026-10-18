# Architecture

Four independent tools, no shared service, no database. Each is a Python package with a library
API and a CLI; the only coupling is that they consume the same file formats.

```
            ┌─────────────── wet lab ───────────────┐
            │  phage lysate      gel image           │
            │      │                 │               │
    Illumina reads │                 │ photo         │
            ▼      ▼                 ▼               │
   ┌────────────────────┐   ┌──────────────────┐      │
   │ assembler (SPAdes) │   │   gelquant       │      │
   └─────────┬──────────┘   │ ladder calibrate │      │
             │ contig.fasta │ lane densitometry│      │
             │ + reads      └────────┬─────────┘      │
             ▼                       │ bands.tsv      │
   ┌────────────────────┐            ▼                │
   │ phagecheck.dtr     │     apparent MW, lane totals│
   │ k-mer coverage     │                             │
   └─────────┬──────────┘                             │
             │ LINEAR+DTR | CIRCULAR                  │
             ▼                                        │
   ┌────────────────────┐   ┌──────────────────┐      │
   │ annotation         │   │ structure        │      │
   │ (Pharokka/Bakta)   │   │ prediction       │      │
   └────┬──────────┬────┘   └────────┬─────────┘      │
        │          │                 │ fold.pdb       │
        │          ▼                 ▼                │
        │  ┌──────────────┐  ┌──────────────────┐     │
        │  │   olocus     │  │phagecheck.beta-  │     │
        │  │ locus extract│  │helix  H-bond     │     │
        │  │ + compare    │  │period signature  │     │
        │  └──────┬───────┘  └────────┬─────────┘     │
        │         │ locus_table.tsv   │ fold_calls.tsv│
        │         │ figure            │               │
        ▼         ▼                   ▼               │
   ┌──────────────────────────────────────────┐       │
   │ phageresist                              │◄──────┘
   │ map reads → call variants → confirm at   │  resistant isolate
   │ read level → report vs parent            │
   └──────────────────────────────────────────┘
```

## Data flow in one line each

| Tool | In | Out |
|---|---|---|
| `phagecheck.dtr` | contig FASTA + FASTQ reads | verdict + the coverage runs that justify it |
| `phagecheck.betahelix` | predicted structure PDB | fold call + H-bond period, core span, elongation, pLDDT |
| `olocus` | Bakta/Prokka annotation directories | per-gene locus table, per-strain FASTAs, comparison figure |
| `gelquant` | gel photo + ladder spec + lane labels | per-band apparent MW, per-lane optical density, annotated overlay |
| `phageresist` | resistant and parent reads/assemblies | candidate variants, read-level confirmation, allele table |

## Design rules

- **No network at run time.** Sequences stay on the machine.
- **Library first, CLI second.** Every CLI is a thin wrapper over functions that return
  dataclasses or data frames, so the tools compose in a notebook.
- **Thresholds are named arguments, not magic numbers** (`k`, `threshold`, `min_length`,
  `PERIOD_RANGE`, `HBOND_CUTOFF`), because every one of them is a scientific judgement a reuser
  may need to change.
- **Tests carry the fixtures with them.** `phagecheck`'s tests build their own genomes and reads,
  so they run in under two seconds with no data download.
