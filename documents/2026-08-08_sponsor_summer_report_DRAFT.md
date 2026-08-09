# Summer Sponsorship Report — Alex Chen (DRAFT)

**Author:** Alex · **Purpose:** Summer sponsorship / donor report (Overview · Outcomes · Impact · Highlight · Thank You) · **Status:** DRAFT — needs Alex's read-through and four fills before submission

> Drafted from the project docs and lab notebook. Four open items flagged in **⚠️ Needs Alex's input** below — everything else is ready to submit as-is or lightly edited. Written for a **non-technical reader**: no term is used before it is glossed, and every number is one a lay reader can hold. A Traditional Chinese version of all five sections is in `2026-08-08_sponsor_summer_report_DRAFT_zh.md` — the English here is what gets submitted; the Chinese is for reading and reuse.

---

## ⚠️ Needs Alex's input before submitting

1. **Attribution — read this one first.** The draft says "I predicted," "I designed the comparison myself," "the check I built in." How much of the structure prediction, the anchor-based cassette comparison, and the control design was your own work versus work done by Claude under your direction is not something this draft can determine, and it is going to a donor under your name. Go through every first-person claim and adjust to "our team," "I directed," or "I designed and ran" as each case actually warrants. Nobody else can make this call.
2. **The donor's name and what the gift actually funded.** Currently `[DONOR NAME]` and `[what the gift funded — sequencing / reagents / the DNA synthesis order / a stipend]` in the Thank You section. This is the highest-value fill in the document — a donor rarely gets to see the object their gift became, and naming it is most of what the last section does. Consider adding the same line item once in §1's final paragraph, so the report opens and closes on it.
3. **Career target.** The Outcomes section says you want to work at the computation-to-bench interface, which is defensible from the summer's record, but the *destination* is not derivable from the repo: field name, graduate school vs. major vs. further lab work. Placeholder is `[field / next stage]`.
4. **Word limits.** Written long so you can cut rather than pad. If the form caps each answer at 100–150 words — which is what the OCS summer journal used — the sentence-level keeps are marked `[cut for length]` at the end of each section. Those notes are aggressive on purpose; at 150 words per answer you are keeping roughly two sentences per section.

Three smaller judgement calls, flagged rather than decided:

- **Voice.** This is written in a plain, concrete, first-person register inferred from the project documents — not sampled from prose you actually wrote, since most documents in `documents/` are Claude-drafted. Read it aloud; if it does not sound like you, the fastest fix is to rewrite the first sentence of each section in your own words and let the rest follow.
- Whether to name the PI and teammates (currently unnamed).
- Whether to include the tail-spike structure figure with the Highlight section (recommended if the form allows an image). Note also that three alternative Highlight moments were considered — the control passing at 100.0%, placing the DNA order, and catching the mislabelled construct — and the structure-rendering moment was chosen for being visual, instantaneous, and jargon-free. Any of the others can be swapped in if it feels more genuinely yours.

---

## 1. Overview
*What did you do? What was your main role? What was your biggest success or contribution?*

This summer I worked on a wild bacterium and the virus that kills it. My team collected soil from ten sites at a botanic garden in May, isolated *Pseudomonas* bacteria from it, and isolated a bacteriophage — a virus that infects only bacteria and is harmless to people — that could kill one of them. Phages are being developed as precision antibiotics, and the thing that decides whether a given phage can kill a given bacterium is which molecule it recognises on the bacterial surface. Finding out what our phage recognises, and why it kills one of our strains and not the others, was the question I spent the summer on.

My role was the computational side of a wet-lab project. The lab produced samples and raw sequencing data; I turned that into finished genomes and into decisions the team could act on. That came down to three distinct things: assembling and annotating complete genomes from raw sequencing reads, using protein-structure prediction to work out what unnamed phage genes actually do, and writing the synthesis documents that the team and our PI now use as the project's shared reference. I also worked at the bench — DNA quantification standard curves across five batches, and growth-curve experiments where we add phage to a bacterial culture and watch whether the culture collapses.

My biggest contribution was finding that the phage's key fits a sugar lock, not a protein one — and that finding redirected the project. Everyone, including me, had assumed the phage docks onto a protein on the bacterial surface, and we had spent weeks building a computational screen to find out which one. Instead, when I predicted the three-dimensional structure of the phage's tail spike — the part that touches the bacterium first — it came back as a long right-handed spiral, the architecture of an enzyme that chews through sugar chains. The phage does not dock onto a protein handle; it eats its way through the bacterium's sugar coat. That changed the target of the entire project. I then compared the sugar-coat genes across our three bacterial strains and found that all three carry completely unrelated versions of them, sitting in the same slot in the genome — of forty-five gene groups in that region, only four are shared by all three, and none of those four are the machinery that builds the coat. Because the phage's weapon is a sugar-cutting enzyme, that difference predicts directly which strains it should and should not be able to infect. The laboratory test of that prediction has been run but its data has not yet reached me, so for now it remains a prediction rather than a result.

A second contribution was proving that one of our own approaches did not work. Before running the planned 120-pair screen, I built a control test out of protein pairs already known to bind each other — pairs the method had to score highly if it was to be trusted. It failed: the known-good pairs scored *worse* than a pair I had deliberately mismatched. I then worked out why. The method relies on evolutionary signal shared between two partner proteins, and a virus and a bacterium are far too distantly related for that signal to exist. The screen would have produced a full page of confident-looking numbers that meant nothing. Catching it cost a few days; not catching it would have cost the summer, and the finding is worth publishing on its own as a caution to other groups.

What exists now that did not in May: five bacterial genomes sequenced to completion, each a single closed chromosome of roughly six million DNA letters, now known to collapse into three genuinely distinct strains rather than five; the phage's complete genome, 62,338 letters and 80 genes, which matches nothing in the public databases and so appears to be a phage nobody has described before; a safety screen of that genome finding zero virulence genes and zero antibiotic-resistance genes, which is what lets the project proceed responsibly; three protein designs ordered from a commercial DNA synthesis company so the lab can now test the sugar-cutting prediction at the bench; a draft genome-announcement manuscript with my name on it; and a written synthesis of every result in the project, each marked with how strongly it is supported. What is still open: a second phage awaiting sequencing, and the host-range experiment awaiting its readout.

> `[cut for length]` — at 150 words, keep exactly these: sentence 1 of ¶1 ("This summer I worked on a wild bacterium and the virus that kills it"), the phage-as-precision-antibiotic sentence, sentence 1 of ¶2 ("My role was the computational side of a wet-lab project"), and from ¶3 the headline sentence plus "The phage does not dock onto a protein handle; it eats its way through the bacterium's sugar coat." Then close with one sentence of deliverables — the complete phage genome and the three constructs ordered. Everything else goes; the failed screen and the sugar-cassette detail both recur later.

---

## 2. Outcomes
*What were the most important takeaways? How did this influence your future career goals?*

The most important thing I learned is that a method has to be tested against an answer you already know before you can trust it on one you don't. This is not how I instinctively worked at the start of the summer; I learned it by nearly shipping a result that would have been confidently wrong. Any analysis method will happily produce output, and output looks like an answer whether or not it is one. A scale that returns a number for every object is not the same as a scale that returns the right number, and the only way to tell them apart is to weigh something whose weight you already know.

The second is that being wrong quickly is cheaper than being right slowly. Twice this summer I threw away work that had already been done — once when the tail-spike structure killed our protein-binding hypothesis, and once when I realised a planned analysis rested on an assumption that did not hold. My instinct both times was to protect the effort already spent. That instinct is exactly backwards: the sunk work is not recovered by continuing, and the sooner a wrong direction is dropped, the more of the summer is left. The one condition is that you have to understand *why* it failed, or you are not redirecting, you are just quitting.

The third took me by surprise: careful bookkeeping is not clerical work, it is where errors actually get caught. Our phage was annotated twice, in opposite orientations, so two incompatible gene-numbering systems were circulating in the team and the same gene had two different names in different documents. The DNA constructs we ordered came back with filenames that contradicted their own sequences — I found it by translating each sequence by hand instead of trusting the label. In a collaboration where several people generate data over months, ambiguity is a failure mode exactly as real as a failed experiment, and it is a silent one. I now write down not only what a result is, but how strongly it is supported and where it came from, so that anyone reading can tell a confirmed fact from a prediction.

This summer confirmed that I want to work at the point where computation changes what someone does at the bench. The chain that made that concrete for me was: a gene of unknown function, a predicted structure, a hypothesis about what the protein does, a construct designed and ordered, and an experiment the lab can now run. The computation mattered because it ended in a tube. I also learned what I don't want, which is analysis that produces a figure and stops. Concretely, this points me toward `[field / next stage]`.

It also showed me exactly what I cannot do yet, and that is what I want next. I can now take a gene nobody has characterised and predict what it probably does — but I cannot yet express that protein, purify it, and measure whether the prediction was right. That handoff is where my work currently ends and someone else's begins, and closing it is what I want out of the next stage. The pull toward this particular subject is real too: phages are one of the few plausible routes to antibacterials that kill one target and leave everything else alone, and that is what made the work feel worth doing rather than merely interesting.

> `[cut for length]` — at 150 words, keep: "a method has to be tested against an answer you already know before you can trust it on one you don't," the scale analogy, "being wrong quickly is cheaper than being right slowly," and then the whole of ¶4 (the computation-to-bench chain), which is what the question actually asks. Drop ¶3 entirely — it reappears in Impact — and cut ¶5 to its first two sentences.

---

## 3. Impact
*What were your challenges? What did you learn from them? What did you learn about yourself?*

My first challenge was that the tools I needed either would not run or did not exist. The practical version was a stretch of trial and error across several structure-prediction tools, a laptop that could not run any of them, and eventually a shared university computing cluster with its own queueing system, environment setup, and etiquette — where a careless job wastes resources other people are waiting for. Days went into infrastructure that produced no scientific result at all. The harder version came with the sugar-coat comparison: every existing analysis tool for that problem is built around a different bacterial species, and ours is none of them. There was no method to run and no reference scheme to compare against.

What I learned from that is that when no method exists, you build one — and you build its test at the same time. I designed the comparison myself: rather than relying on gene names or genome coordinates, I located the sugar-coat gene cassette by the fixed genes flanking it, and decided which genes counted as equivalents by comparing sequences directly rather than trusting their labels. The part I am most pleased with is the check I built in. Our five bacterial isolates include two pairs that are near-identical duplicates of each other, so if the method was sound, it had to report both pairs' cassettes as identical. It did, at 100.0% for both. Before measuring two things that should differ, I measured two things that should match, and gave the method a chance to prove itself wrong. On the infrastructure side, the lesson was less elegant but just as real: study the setups that already work before writing your own, rather than learning by breaking things on a machine other people share.

My second challenge was that most of what I needed was in other people's hands, and it moved. A key experiment had already been run, but its data had not reached me, so a result I could otherwise state had to stay a prediction. The phage's genes had been numbered twice in opposite directions, so half the project's documents referred to genes by names the other half did not recognise. One protein's identity was withdrawn partway through the summer, after our PI concluded he did not actually know what it was. What I learned was to stop treating incoming information as fixed — to record, for every claim, how strongly it is supported and where it came from, and to ask a senior collaborator one narrow, direct question rather than guessing and then building on the guess.

What I learned about myself is that I over-trust things that produce confident-looking output. My default was to believe a tool that ran without error, a filename that described its file, and a number that came with three decimal places. This summer punctured all three: a prediction method that ran perfectly and produced meaningless scores, ordered DNA whose filenames contradicted their own sequences, and an earlier screen that turned out to be measuring how *large* the proteins were rather than whether they bound. What changed is not that I became cynical, but that I now build the check before the result, and I have learned to notice the specific feeling that should trigger it — the moment a result is convenient. The cost is that I am slower, and I am still working out where the line sits between rigour and stalling.

The other thing I learned about myself is that I have to write something down before I actually understand it. Across the summer I kept producing documents nobody asked for: a running synthesis of every result with its evidence level attached, a note reconstructing exactly why the failed screen failed, a table reconciling the two gene-numbering systems. I started them to keep the team aligned and discovered they were how I think — the contradictions and the gaps only became visible once things sat next to each other on the page. I am, it turns out, more motivated by making a messy thing legible than by generating one more result.

> `[cut for length]` — at 150 words, keep: the first two sentences of ¶1 (tools that would not run, no method that applied), from ¶2 "when no method exists, you build one — and you build its test at the same time" plus the clone-pair check and its 100.0% result, and then ¶4's opening ("I over-trust things that produce confident-looking output") through "the moment a result is convenient." Drop ¶3 and ¶5. If you have room for one more sentence, take ¶5's last line about being motivated by making a messy thing legible.

---

## 4. Highlight
*Share a moment that was particularly meaningful. Why does it stand out?*

The moment was watching the tail spike's predicted structure finish rendering. I had submitted a phage protein of unknown function to a structure-prediction model and waited for it, expecting something like the compact, irregular shape of a protein that grabs onto another protein — because that was what the whole team was looking for. What came back was a long right-handed spiral running down most of the protein's length, some six hundred amino acids of it, repeating with almost mechanical regularity. I did not need to run another analysis to know what I was looking at. That shape belongs to a family of enzymes that chew through sugar chains.

It stands out because the project's central assumption died and its real question appeared in the same image. For weeks we had been asking which bacterial protein the phage recognises. The structure said it does not recognise a protein at all — it recognises the bacterium's sugar coat, and it recognises it by cutting through it. Everything that followed descends from that one picture: the comparison of the sugar-coat genes across our three strains, the prediction about which strains the phage can and cannot kill, and the three protein constructs now ordered so that the lab can test it.

What has stayed with me is not that I found something, but the shape of how it arrived. The thing I was looking for was not there, and something better was in its place — and the only reason I could see it was that I had asked the question in a way that allowed for an answer I had not anticipated. That is the part I would like to be able to do again on purpose.

> Recommended: include the predicted structure figure with this section if the form allows an image. It carries the section on its own.

---

## 5. Thank You
*What would you like to say to the donor? A few words of appreciation.*

Thank you, `[DONOR NAME]`, for `[what the gift funded]`. I want to be specific about what it turned into, because I think a donor rarely gets to see the object their gift became. It became a complete genome for a bacteriophage that, as far as the public databases can tell, nobody had described before — 62,338 letters of DNA, 80 genes, and a screen showing it carries no virulence genes and no antibiotic-resistance genes at all. And it became three protein designs that are now being manufactured, so the lab can test at the bench a prediction that until this summer existed only on a screen.

I also want to thank you for something less tangible: I was trusted with a question that did not have an answer yet. I was not handed an exercise whose result was already known and asked to reproduce it. I was given a real open question — what does this phage recognise, and why does it kill one strain and not another — and allowed to be wrong about it, in public and at a lab's expense, for an entire summer. Students very rarely get that, and it is the reason this summer changed what I want to do rather than simply adding a line to a résumé.

And I want to say the honest thing, which is that some of what you funded was failure. A meaningful part of my summer went into an approach that turned out not to work. The value of that money was not a result; it was knowing, with evidence, that a whole direction is a dead end — so that neither this team nor the next one walks down it. I understand that is a kind of patience most funding does not have, and I am grateful that this did.

What happens next is already in motion. The proteins arrive for expression and testing, the genome-announcement manuscript moves toward submission, and a second phage is still waiting to be sequenced. For my own part, I intend to keep working at the place where an analysis has to end in something someone can actually pick up.

Thank you for funding a summer in which I got to find out I was wrong about something real, and then find out what was actually true. I do not think I could have arranged that for myself.

---

## Evidence appendix (repo sources)

- Five isolates collapsing to three ANI-distinct strains; genome sizes and completeness: `code/0627_unique_strain_table.ipynb`, `code/output/0626_genome_comparison/table1_genome_summary.csv`.
- Phage 9-2-1 Φ8 complete genome (62,338 bp, 80 CDS, linear with 77 bp terminal repeat); novelty (no INPHARED match): `data/phage_genome/9-2-1/assembly/`, `code/0713_espinoza_structural_mapping/pharokka_espinoza/`.
- Safety screen, zero VFDB virulence factors and zero CARD resistance genes: `.../top_hits_{vfdb,card}.tsv`.
- Tail spike CDS_0011 as a right-handed β-helix depolymerase; receptor is the LPS O-antigen: `code/0712_phage_rbp_detect/`, `code/0716_espinoza_fiber_construct/`, `documents/2026-07-13_phage_rbp_depolymerase_findings.md`.
- O-antigen cassette comparison — three non-homologous cassettes in one slot, 4 of 45 ortholog clusters shared, clone pairs 100.0% identical as internal control: `documents/2026-07-29_results_synthesis_EN.qmd` §4.
- Failed protein–protein binding screen, control gate and diagnosis: `documents/2026-07-13_why_protein_protein_binding_fails.qmd`; size-confounded earlier screen: `code/0703_phage_host_matrix/`.
- Structure-prediction tool selection and infrastructure difficulties: `documents/2026-07-04_folding_tool_odyssey.md`, `documents/2026-07-04_folding_tool_recommendation.md`.
- Two coexisting CDS numbering schemes and the crosswalk: `code/0713_espinoza_structural_mapping/cds_lookup.tsv`.
- Three constructs ordered from Twist on 2026-07-27, and the filename/sequence contradiction: `documents/2026-07-27_twist_construct_order/README.md`.
- Draft genome announcement (MRA): `documents/2026-06-27_MRA_Pseudomonas.docx`.
- Bench work — DNA quantification standard curves (5 batches) and OD600 phage-challenge time courses: `code/output/*_quantification/`, `code/0624_od600_phage.ipynb`, `code/0625_od600_phage.ipynb`.
- Host-range experiment run but data not yet in hand: `documents/2026-07-29_results_synthesis_EN.qmd` §3 E4–E5.

---

*Log: 2026-08-08 — Drafted by Claude from the project docs and lab notebook, following the five-section structure of the sponsorship form (Overview · Outcomes · Impact · Highlight · Thank You) and the point outline agreed in conversation. Traditional Chinese version alongside at `2026-08-08_sponsor_summer_report_DRAFT_zh.md`. The failed binding screen appears in three sections by design, each time doing a different job — contribution in §1, method lesson in §2, self-knowledge in §3 — and is stated at full length only in §1. Host range is written as a prediction, not a result, since the 2026-07-04 assay data has not reached us. The Highlight describes the β-helix as running down "most of" CDS_0011 rather than its full 941 aa, per the domain map in `code/0716_espinoza_fiber_construct/domain_map.tsv` (Calx-β 1–110, unplaceable shaft 111–300, rigid β-helix body 301–941) — which is also why the ordered construct starts at residue 305. The §3 control is both clone pairs at 100.0% (A10), not one pair. Four items flagged as needing Alex's input, attribution of first-person claims first among them.*
