# CDS12_ANC_Node281 - BBa_26LHLSLW  (bba-26lhlslw)

Paste-ready. Live registry text as of 2026-10-19 with the 2026-10-19 dot blot merged in. status=draft

## Functional Description

A reconstructed ancestor of the phage GH5 glycoside hydrolase CDS\_0012, the most distant of the three ancestral nodes we submit, designed to test whether an ancestral enzyme has a broader substrate range than its modern descendant. The sequence is computationally designed and does not exist in nature. It is 51.0 percent identical to the modern enzyme and 87.3 percent identical to node 40, so the two act as a pair at the far end of the panel. It is expected to fold into the same (beta/alpha)8 GH5 TIM barrel and to retain the acid/base glutamate in the conserved NEP motif. The part is a coding sequence with its own ATG and stop codon and does not include the pET-28a His6 leader used in our own expression construct. Two purification attempts, on 2026-10-01 and 2026-10-10, both recovered nothing, but an anti-His dot blot on 2026-10-19 found the 10-10 flow-through positive at 2.9 times the negative control, indicating the protein was expressed and did not bind the resin. See the documentation entries.

## design

**title:** The most diverged node of the panel, and what survives at 51 percent identity

Hypothesis, shared with the other two ancestral nodes: ancestral enzymes tend to be more promiscuous than their modern specialised descendants, so an ancestral GH5 may cleave surface polysaccharides the wild-type enzyme cannot, including on phage-resistant hosts. The three nodes were designed as one set.

Where this sequence sits, as percent identity over the 361 aa mature insert: node 281 is 51.0 percent identical to the modern enzyme CDS\_0012, the most distant of the three, 57.1 percent to node 1 and 87.3 percent to node 40. Node 40 and node 281 behave as a pair, which gives the panel an internal replicate at the far end.

Node ordering. The node labels are arbitrary identifiers, not tree depths. The reconstructed nodes, ordered from most recent to most ancestral, are 1, 2, 38, 39, 40, 42, 267, 277 and 281, so node 281 is the most ancestral of the three we submit. That ordering agrees with the sequence identities above, which were measured independently of the tree.

Structure. ESMFold v1, single sequence, no MSA, no template: mean pLDDT 85.8, with 88.1 percent of residues above 70. Superposed on the ESMFold model of CDS12\_WT it gives 0.52 Angstrom backbone RMSD. Half the sequence has changed and the GH5 TIM barrel is unmoved; the differences sit in surface loops, which is also where the model is least confident.

Method validation: the wild type folded with the same single-sequence method superposes on the AlphaFold3 model of the same region at 0.28 Angstrom over 2139 atoms.

Catalytic machinery. The acid/base glutamate sits in the conserved NEP motif, IGADLHNEPHG at insert position 166, with a conserved SPHDY block downstream. It shares with node 40 the Tyr to His substitution immediately before the motif, a difference from both node 1 and the wild type, and the obvious first thing to test if these two distant ancestors behave alike.

Reconstruction method. CDS\_0012 was used as a query against the NCBI non-redundant protein database, targeting viral, bacterial and metagenome-derived sequences. The top 1,000 hits were downloaded and aligned with MUSCLE as implemented in SeaView, and the alignment was manually curated to retain the regions covered by the extant query. The curated alignment was used to build a tree with PhyML, WAG substitution matrix, proportion of invariant sites fixed at 0.1, branch support from 100 bootstrap replicates. Ancestral sequence reconstruction was performed in IQ-TREE using the same WAG matrix, with the tree rooted at the midpoint, and every ancestral node on the path from CDS\_0012 to the root was reconstructed. This work is Prof. J. Espinoza's.

## experiment

**title:** Cloning, two Ni-NTA purifications that recovered nothing, and the dot blot that explains them

Cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist Bioscience; order sheet filed 2026-09-10. Host E. coli BL21(DE3), kanamycin selection, IPTG induction at ~30 C. Predicted mass of the tagged protein 42.3 kDa.

Codon usage warning: ordered with Codon Optimized set to No, mammalian-like codon bias. First suspect behind a missing band; Rosetta or BL21-CodonPlus are the alternatives.

This construct has been over a Ni-NTA column twice. On 2026-10-01 it was one of six constructs purified in a single session over NEBExpress Ni spin columns (NEB S1427); it gave no band in either elution, and by Bradford its E2 fell below the lower limit of quantification. The dedicated repeat on 2026-10-10 failed outright as well, and it is the one with quantified lanes: its elutions E1 and E2 were blank gel, peak prominence 0.011 against a measured noise floor of 0.020, with lane totals inside the never-loaded range, and the flow-through was indistinguishable from the load, the same 40-44 kDa band in both. Nothing bound the resin, so that band, although close to the predicted 42.3 kDa, behaves like a host protein rather than a His6-tagged construct. The crude gel of 2026-09-29 had already shown no band at 42.3 kDa for this construct.

The 2026-10-10 gel on its own could not distinguish no expression, an insoluble product and a dead column.

Anti-His dot blot, 2026-10-19. Eleven samples were spotted directly onto membrane and probed with a single-step anti-His HRP conjugate; the positive control reached about 18 times the negative control, so the detection chemistry worked. A dot blot reports the His tag, not size or activity, and this membrane's detection floor is high: every 1:10 dilution on it fell to background, so an absent signal here is weak evidence of absence.

This construct's flow-through was His-positive at 2.9 times the negative control, the second strongest signal on the membrane. That settles the three-way ambiguity above: the protein was expressed and it did not bind the resin. The failure is capture, not expression, so the next move is the binding conditions, meaning imidazole carried into the load, binding time and resin choice, rather than a repeat of the same purification. An untransformed BL21(DE3) control lane and a size-resolved anti-His western are both still outstanding.

## characterisation

**title:** First activity data, and anti-His evidence that the protein was expressed

First activity data, 2026-10-16. Essentially negative for this variant, alongside the failed purification recorded in the Experiment entry.

Spot test. Seven Pseudomonas strains were grown as double-layer lawns, 200 microlitres of culture in 3 millilitres of soft agar. Each plate received five 7 microlitre drops: phage Phi8 stock as the positive control, sterile 1x PBS as the negative control, and the e1, e40 and e281 preparations, each diluted 1 in 10 in that same sterile PBS. Spotted 12 October, read 16 October.

No drop produced a clear lysis zone, Phi8 included. The readout was colony growth inside the drop: sterile PBS drops reproducibly developed discrete colonies, a median of 14 per drop. Every plate carried its own PBS drop and that baseline varied between plates, from 7 to 17 colonies, so the comparable figure is each drop as a percentage of the PBS drop on the same plate. On that scale the medians are Phi8 0 percent, e1 12 percent, e281 53 percent, e40 67 percent. This variant sits at 53 percent, closer to the no-effect line than to the phage.

What this does and does not establish.

The e281 preparation is a crude lysate, not purified protein, so the enzyme is not enriched in it. A weak effect here is not evidence that this variant is inactive: the experiment cannot tell a missing activity from a diluted one. Neither Ni-NTA attempt, on 2026-10-01 or 2026-10-10, recovered anything, so no purified material existed to spot.

Expression is now supported: this construct's flow-through was His-positive on the 2026-10-19 dot blot. That does not rescue this result, because what was spotted here was the 1:10 crude lysate, and every 1:10 dilution on that membrane fell below its detection floor. How much enzyme was in the drop remains unknown.

By contrast the e1 preparation, the only one of the six from which Ni-NTA recovered protein, suppressed colonies almost completely in the same experiment, at 12 percent. That difference tracks the preparation, not necessarily the sequence.

For anyone reading the e1 result beside this one: that activity is not yet attributed to the protein either. e1 tracks phage Phi8 strain by strain, so carry-over of infectious phage from the Phi8 stock remains the leading alternative, and a plaque assay of the preparation is the experiment that would settle it.

The wild-type enzyme CDS12\_WT was not spotted in this run, so the ancestor-versus-modern comparison the design asks for has not been made yet.

One concentration, one plate per strain, colonies counted by automated image segmentation. No replicates and no statistics.

This part cannot be distinguished from CDS12\_WT or the other two ancestors by SDS-PAGE: all four are within 0.43 kDa, 1.0 percent, of each other. Identification needs sequencing or intact-mass MS.

Planned next: fix the capture step now that expression is supported, then purify, equalise protein against the others, and re-spot with an elution-buffer-only control and CDS12\_WT on the same plate.

## application

**title:** The far end of the ancestral panel

With node 40, this part is the far arm of the ancestral panel: the pair furthest from the modern enzyme's specificity, and the most likely of the three to act where the wild type cannot.

The intended application is the same as for the rest of the toolkit: a free depolymerase applied to a phage-resistant soil Pseudomonas, where the modern enzyme has stopped working because the host changed its surface sugar.

For another team the reusable idea is the panel, not this sequence alone: a modern enzyme, one close ancestor and two near-identical distant ancestors, which gives an internal replicate exactly where the design is most speculative.

## discussion

**title:** The strongest test of the promiscuity hypothesis, and the likeliest to fail

Limitations. A reconstructed sequence is a hypothesis about a protein that no longer exists. Two purification attempts recovered nothing, and expression rests on the dot blot rather than on any sized band. The non-optimised codon usage is a real risk. The structural evidence is a single-sequence model.

Role in the set. Being the most diverged of the three, at 51.0 percent identity to the wild type, this node is the strongest test of the promiscuity hypothesis and also the most likely to misfold or express poorly. Its near-twin node 40, 87.3 percent identical to it, is the control for both of those risks.

Attribution note. The sequence is Prof. J. Espinoza's design: the GH5 phylogeny, the ancestral-state reconstruction and the node choice are his. The students contributed the structural comparison, the cloning, the expression trials, the Ni-NTA attempt and the gel densitometry.
