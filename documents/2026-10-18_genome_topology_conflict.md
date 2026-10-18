# 9-2-1 Φ8 topology — circular or linear + 77 bp DTR

The PI's A2 text (2026-10-18) calls the genome **circular**. This repository has
said **linear with a 77 bp direct terminal repeat** since 2026-07-08 and treats
it as resolved. Both versions are kept here side by side.

**The short version: our "RESOLVED" is weaker than it looks, and the one
read-level test we actually ran agreed with the PI.** Nothing here settles the
question. Do not state a topology on the wiki until PhageTerm or CheckV has run.

---

## 1. Why the same 77 bp supports both readings

A de Bruijn assembler reports a contig whose two ends overlap in exactly two
situations, and it reports them identically:

- a genuinely **circular** molecule, linearised for output, leaving a
  **circularisation overlap** of roughly the k-mer length of the graph that built
  the contig; or
- a **linear** genome carrying a **direct terminal repeat**, where the assembler
  collapses the two copies of the repeat into one.

Our own software package states this correctly — `software/README.md:46-48`:
"assemblers report a phage contig as 'circular' whenever the ends overlap, which
is also exactly what a direct terminal repeat on a linear genome looks like."
So the existence of the 77 bp is not evidence for either side. Only something
outside the assembly graph can decide it.

## 2. What each side actually rests on

### The PI's case for circular

From `2026-10-18_pi_questionnaire_answers.md` A2: megahit, default parameters,
~20 M read pairs subsampled to 50,000, one contig of 62,339 bp at 140×.

> The contig terminated in a 77 bp redundancy corresponding to the maximum k-mer
> length used during assembly, indicating that the assembly graph closed into a
> circle.

**One checkable problem with the stated reason.** megahit's default k-list is
21, 29, 39, 59, 79, 99, 119, 141 — its **maximum** k is 141, not 77. So "77 bp
corresponding to the maximum k-mer length" does not hold as written.

**But a weaker version of his argument survives, and it is uncomfortably good.**
77 sits right beside the **k = 79** step: a circular-join overlap out of the k=79
graph would be 78 bp, and the measured length difference between his assembly and
ours is **exactly 78 bp** (62,416 − 62,338). The exact repeat is 77 bp, one off.
That is close enough that "circularisation overlap from an intermediate k" cannot
be dismissed. Ask him which k actually assembled the contig.

### Our case for linear + DTR

From `data/phage_genome/9-2-1/assembly/NOTES.md:41-51` and
`PI_assembly/README.md:18-31`. The test was a string comparison on the PI's FASTA
(`compare_to_PI_assembly.py:26-29`), re-verified independently today:

| | our SPAdes contig | the PI's megahit contig |
|---|---|---|
| length | 62,338 bp | 62,416 bp |
| exact prefix == suffix | **0 bp** | **77 bp** |
| the 77 bp repeat | present **once, internally**, reverse-complemented, at index 17703 | present at **both ends** |
| coverage | 1014× | 140× |

The repeat sequence is
`GGCTGCGCTCGACCACGACGTTTTGCGGCTTACCGCCTTTGACCTTCGGCACGGGCAGTTTCTTGCCCTGGCTGGCC`.
100 % of our 31-mers are found in his assembly, so it is the same genome.

**The problem: this is precisely the ambiguous observation from §1.** "His contig
has an exact terminal repeat" is the thing that looks identical under both
hypotheses. Our conclusion was drawn from a string-identity test on a single
assembled sequence, not from anything outside the graph.

## 3. The part of the record that was overwritten

The repo reached the linear call by reversing an earlier one, and the earlier one
had better evidence behind it.

- commit `8cb197e` — "62kb **circular** novel phage". No topology evidence.
- commit `e10dd9b` — retracted: "no exact terminal redundancy and SPAdes didn't
  flag it circular, so 'circular' was overclaimed."
- commit `ecc164c` — **the only read-level analysis ever run**.
  `check_terminal_redundancy.py`, a 31-mer read-coverage profile along the contig
  from 300k reads: **median ~357×, max/median 1.63×, no qualifying ≥2× spike**.
  Its own verdict line prints `CIRCULAR / no short linear DTR`. The commit reads
  the PI's terminal repeat as "most consistent with a **circularisation
  overlap**".
- commit `efc4c19` — **flipped to linear + DTR purely on the string comparison
  above**, describing the read-level work as "my earlier flip-flopping read-only
  guesses".

So: the string test overrode the coverage test, and the coverage test is the one
that looked outside the assembly graph. The logic of the reversal was that the
PI's assembly is authoritative — but the PI reads his own assembly as circular,
which removes the ground the reversal stood on.

**Why the coverage test matters here.** If the molecule were linear with a DTR,
reads from *both* copies of the repeat map onto the single collapsed copy in our
contig — at index 17703 — giving a ~2× coverage spike there. No such spike was
found. That is a direct argument for circular, and it is the strongest piece of
evidence in the whole record.

Two caveats on it, in fairness: `max/median` came out at **1.63×**, marginally
above the script's hard-coded 1.6× threshold, but no run of ≥15 bp qualified; and
**the saved stdout of that run is not in the repo** — the numbers survive only in
a commit message and a superseded NOTES.md. The check was also never re-run
against the PI's 62,416 bp sequence.

## 4. A documentation error this exposes, which is user-facing

`software/README.md:48-50` and `software/phagecheck/dtr.py:15-16` both say:

> This is the check that corrected our own call on phage 9-2-1 Φ8 — reported as
> circular by the assembler, actually linear with a 77 bp DTR.

and `software/README.md:68-70` calls it "a regression test record: the DTR check
overturned an assembler's circularity call".

**That is backwards.** Per commit `ecc164c`, that check's verdict on this genome
was *circular*. The linear call came from the PI-assembly string comparison in
`efc4c19`. `2026-10-18_software_inventory.md:75-76` repeats the same claim.

This matters beyond tidiness: `software/` is the Best Software entry, and
"corrected our own call" is its headline provenance claim. It should be fixed or
removed before anything is submitted. Not changed here — it is a factual claim
about our own history and needs a decision, not a silent edit.

## 5. What would actually settle it

None of these has been run. The reads are on disk at
`data/phage_genome/9-2-1/3NKSC3_1_9_2_1_ph8_R{1,2}.fastq.gz`.

1. **PhageTerm** — the real answer, recommended in the repo three separate times
   and never executed. It pools read 5′-end positions: a linear DTR genome shows a
   sharp peak of read starts at the terminus, a circularly permuted (headful)
   genome shows none. This distinguishes DTR, headful and circular directly.
2. **CheckV** — reports a `termini` / DTR call and a completeness percentage.
   Never ran; the database download failed on Laguna with an SSL drop three months
   ago and was never retried.
3. **Re-run the coverage profile on the PI's 62,416 bp sequence**, and re-run it
   on ours with the saved output committed this time.
4. **Ask the PI which k assembled the contig** — if it was k = 79, his
   circularisation-overlap reading gains a lot; if the k-list was the megahit
   default and the contig came out of k = 141, his stated reason does not survive.

## 5b. Four further gaps in the record

1. **Neither assembler's graph is in this repository.** No SPAdes
   `assembly_graph.fastg`, `contigs.paths` or `spades.log` was pulled back from
   Laguna, and there is no megahit log or output file at all — the only trace of
   the PI's run is his prose. So the graph-closure state, which is what both
   sides are really arguing about, cannot be inspected here by either party.
   Commit `e10dd9b` had named the assembly-graph check as the way to settle it;
   it was never done.
2. **The PI's own annotation treats the genome as circular, and it shows.**
   `code/0713_espinoza_structural_mapping/README.md:39` records a coordinate
   artefact between his CDS set and ours: "genome-origin split | CDS_0001 +
   CDS_0080 | CDS_0026 (4193 aa) | **circular-genome origin cut differently**".
   A 4193 aa CDS is not a real protein; it is what happens when an origin is cut
   in a different place. This is not evidence about the molecule — but it does
   mean his circular reading is already baked into the CDS numbering we adopted
   as canonical, so if the topology changes, that numbering needs re-checking.
3. **A read-count discrepancy to raise with him.** A2 says Plasmidsaurus
   delivered "approximately 20 M read pairs". `data/phage_genome/README.md:25`
   records **9,933,775** raw pairs in the delivered `3NKSC3` FASTQs, and his D2
   answer confirms `3NKSC3` is the same Plasmidsaurus order. Either two different
   deliveries exist or one of the numbers is wrong.
4. **Our own file calls his assembly authoritative.**
   `PI_assembly/README.md:3` files his sequence as "the **canonical complete
   genome** (it retains the terminal repeat)". That is the assumption the linear
   call rests on, and he reads the same sequence as circular.

The software provenance error in §4 also appears in a third place:
`software/docs/architecture.md:19-22` labels the `phagecheck.dtr` pipeline box
output `LINEAR+DTR | CIRCULAR`.

## 6. What to write in the meantime

On the wiki, in the Judging Form, and in anything shown to the PI:

> One complete contig of 62,338 bp (62,416 bp in the PI's assembly), 80 CDS,
> 62 % GC, with a 77 bp terminal redundancy. Whether that redundancy is a direct
> terminal repeat on a linear genome or an assembly circularisation overlap is
> not yet resolved; PhageTerm on the full read set is the outstanding test.

Saying this is not a weakness. It is a negative-result statement of exactly the
kind the 2026-10-18 meeting said should be on the wiki, and it is defensible in
front of a judge in a way that "linear, resolved" is not.

**Documents that currently assert linear + DTR as settled** and will need
revising if the question goes the other way: `2026-07-29_results_synthesis_EN.qmd`
(lines 162-164, 217, 501-502), `2026-07-28_results_synthesis.qmd` (132, 177),
`2026-08-08_sponsor_summer_report_DRAFT.md:106`,
`2026-08-21_talk_slides/slides.tex:95`, `code/0708_phage_genome_analysis.ipynb`
(cells 0, 4, 5), `data/phage_genome/README.md:50-52`, and
`data/phage_genome/9-2-1/assembly/NOTES.md:41-51,76-78`.

Note also: the genome is **undeposited**, so no GenBank record declares a
topology. The only `linear` strings in tool output are the Pharokka-generated
`LOCUS` lines in both `.gbk` files, which are a Biopython default and carry no
evidence either way.

---

**Log**

- 2026-10-18 — compiled after the PI's A2 answer contradicted the repo. Both
  readings kept; neither adopted.
