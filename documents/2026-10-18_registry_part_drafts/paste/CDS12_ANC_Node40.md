# CDS12_ANC_Node40 - BBa_26EK89VW  (bba-26ek89vw)

Paste-ready. Live registry text as of 2026-10-19 with the 2026-10-19 dot blot merged in. status=draft

## Functional Description

A reconstructed ancestor of the phage GH5 glycoside hydrolase CDS\_0012, further from the modern enzyme than node 1, designed to test whether an ancestral enzyme has a broader substrate range. The sequence is computationally designed and does not exist in nature. It is 52.6 percent identical to the modern enzyme but 87.3 percent identical to node 281, so the two behave as a pair at the far end of the panel. It is expected to fold into the same (beta/alpha)8 GH5 TIM barrel and to retain the acid/base glutamate in the conserved NEP motif. The part is a coding sequence with its own ATG and stop codon and does not include the pET-28a His6 leader used in our own expression construct. Expression has not been demonstrated: on the 2026-10-19 anti-His dot blot this construct gave no signal on a membrane where two sibling constructs were positive. See the documentation entries.

## design

**title:** A distant ancestor paired with node 281, and a Tyr to His change beside the catalytic motif

Hypothesis, shared with the other two ancestral nodes: ancestral enzymes are repeatedly found to be more promiscuous than their modern, specialised descendants, so an ancestral form of this GH5 may cleave surface polysaccharides the wild-type enzyme cannot, including on phage-resistant hosts. The three nodes are designed as one panel.

Where this sequence sits, as percent identity over the 361 aa mature insert: node 40 is 52.6 percent identical to the modern enzyme CDS\_0012, 61.8 percent to node 1 and 87.3 percent to node 281. So node 40 and node 281 act as a pair. Differences that appear in both of them, and not in node 1, are what this design predicts most strongly; a difference seen only in node 40 needs a separate explanation.

Node ordering. The node labels are arbitrary identifiers, not tree depths. The reconstructed nodes, ordered from most recent to most ancestral, are 1, 2, 38, 39, 40, 42, 267, 277 and 281, so node 40 is the middle of the three we submit. That ordering agrees with the sequence identities above, which were measured independently of the tree.

Structure. ESMFold v1, single sequence, no MSA, no template: mean pLDDT 85.5, with 87.3 percent of residues above 70. Superposed on the ESMFold model of CDS12\_WT it gives 0.50 Angstrom backbone RMSD. Only about half the sequence is shared with the modern enzyme and the GH5 TIM barrel is unchanged; the lower confidence, relative to node 1, is concentrated in surface loops.

Method validation: the wild type folded with the same single-sequence method superposes on the AlphaFold3 model of the same region at 0.28 Angstrom over 2139 atoms.

Catalytic machinery. The acid/base glutamate sits in the conserved NEP motif, IGADLHNEPHG at insert position 166, with a conserved SPHDY block downstream. Note the Tyr to His substitution immediately before the motif relative to node 1 and the wild type, which node 40 shares with node 281. It sits next to the catalytic residue and is the first place to look if these two distant ancestors behave alike.

Reconstruction method. CDS\_0012 was used as a query against the NCBI non-redundant protein database, targeting viral, bacterial and metagenome-derived sequences. The top 1,000 hits were downloaded and aligned with MUSCLE as implemented in SeaView, and the alignment was manually curated to retain the regions covered by the extant query. The curated alignment was used to build a tree with PhyML, WAG substitution matrix, proportion of invariant sites fixed at 0.1, branch support from 100 bootstrap replicates. Ancestral sequence reconstruction was performed in IQ-TREE using the same WAG matrix, with the tree rooted at the midpoint, and every ancestral node on the path from CDS\_0012 to the root was reconstructed. This work is Prof. J. Espinoza's.

## experiment

**title:** Cloned; one barely loaded lane, one purification that recovered nothing, and no anti-His signal

Cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist Bioscience; order sheet filed 2026-09-10. Host E. coli BL21(DE3), kanamycin selection, IPTG induction at ~30 C. Predicted mass of the tagged protein 42.2 kDa.

Codon usage warning: the insert was ordered with Codon Optimized set to No and carries a mammalian-like codon bias. That is the first suspect behind a missing band; Rosetta or BL21-CodonPlus are the alternatives.

SDS-PAGE, 2026-09-15. The lane for this construct on gel 1 was essentially not loaded, so that experiment carries no information about it. In the project's expression plan it sits in batch 2, behind CDS12\_WT and the node 1 ancestor.

Ni-NTA purification, 2026-10-01. This construct was included in the project's one purification session, over NEBExpress Ni spin columns (NEB S1427), and ran on the second of that day's two gels as crude lysate, crude lysate at 1:2, the third wash and both elutions. The crude lanes carry lysate bands; wash 3 and both elutions show nothing at the expected 42.2 kDa. Nothing was recovered. Of the six constructs purified that day, only the node 1 ancestral variant eluted at its predicted size.

Anti-His dot blot, 2026-10-19. Eleven samples were spotted directly onto membrane and probed with a single-step anti-His HRP conjugate; the positive control reached about 18 times the negative control, so the detection chemistry worked. A dot blot reports the His tag, not size or activity, and this membrane's detection floor is high: every 1:10 dilution on it fell to background, so an absent signal here is weak evidence of absence.

This construct was spotted twice, as induced rough lysate and at 1:10, and gave no anti-His signal either time, at -0.2 and 0.7 against a negative control of 3.9. That is a like-for-like negative rather than an isolated one, because on the same membrane the node 1 lysate and the node 281 flow-through were both positive. It is still not proof of absence, for the reasons given above.

## characterisation

**title:** First activity data: essentially negative, and why that is not a verdict

First activity data, 2026-10-16. Essentially negative for this variant.

Spot test. Seven Pseudomonas strains were grown as double-layer lawns, 200 microlitres of culture in 3 millilitres of soft agar. Each plate received five 7 microlitre drops: phage Phi8 stock as the positive control, sterile 1x PBS as the negative control, and the e1, e40 and e281 preparations, each diluted 1 in 10 in that same sterile PBS. Spotted 12 October, read 16 October.

No drop produced a clear lysis zone, Phi8 included. The readout was colony growth inside the drop: sterile PBS drops reproducibly developed discrete colonies, a median of 14 per drop. Every plate carried its own PBS drop and that baseline varied between plates, from 7 to 17 colonies, so the comparable figure is each drop as a percentage of the PBS drop on the same plate. On that scale the medians are Phi8 0 percent, e1 12 percent, e281 53 percent, e40 67 percent. This variant sits at 67 percent, close to the no-effect line.

What this does and does not establish.

The e40 preparation is a crude lysate, not purified protein, so the enzyme is not enriched in it. A weak effect here is not evidence that this variant is inactive: the experiment cannot tell a missing activity from a diluted one.

Expression of this part is still unconfirmed, see the Experiment entry, so there may be no enzyme in the drop at all. On the 2026-10-19 anti-His dot blot this construct gave no signal as induced rough lysate or at 1:10.

By contrast the e1 preparation, the only one of the six from which Ni-NTA recovered protein, suppressed colonies almost completely in the same experiment, at 12 percent. That difference tracks the preparation, not necessarily the sequence.

For anyone reading the e1 result beside this one: that activity is not yet attributed to the protein either. e1 tracks phage Phi8 strain by strain, so carry-over of infectious phage from the Phi8 stock remains the leading alternative, and a plaque assay of the preparation is the experiment that would settle it.

The wild-type enzyme CDS12\_WT was not spotted in this run, so the ancestor-versus-modern comparison the design asks for has not been made yet.

One concentration, one plate per strain, colonies counted by automated image segmentation. No replicates and no statistics.

This part cannot be distinguished from CDS12\_WT or the other two ancestors by SDS-PAGE: all four are within 0.43 kDa, 1.0 percent, of each other. Identification needs sequencing or intact-mass MS.

Planned next: purify this variant, equalise protein against the others, and re-spot with an elution-buffer-only control and CDS12\_WT on the same plate.

## application

**title:** Far arm of the ancestral panel, with node 281 as its replicate

With node 281, this part forms the far arm of the ancestral panel: the pair that probes furthest from the modern enzyme's specificity, and therefore the pair most likely to act on polysaccharides the wild type cannot handle.

The intended application is the same as for the rest of the toolkit: a free depolymerase applied to a phage-resistant Pseudomonas host, where the modern enzyme has stopped working because the host changed its surface sugar.

For another team, the reusable idea is the panel design rather than this single sequence: a modern enzyme, one close ancestor and two near-identical distant ancestors give an internal replicate at the far end, so a surprising result can be checked without a second experiment.

## discussion

**title:** Limitations, and reading node 40 and node 281 as a pair

Limitations. A reconstructed sequence is a hypothesis about a protein that no longer exists. There is no demonstrated expression and no activity: the one usable gel for this construct, on 2026-10-01, shows lysate bands but nothing eluted, and on the 2026-10-19 anti-His dot blot it was the one member of the CDS12 family that gave no signal while the node 1 lysate and the node 281 flow-through were positive on the same membrane. The non-optimised codon usage is a real risk. The structural evidence is a single-sequence model: it shows that the fold survives the reconstruction, not that the enzyme works.

Role in the set. Node 40 and node 281 are 87.3 percent identical to each other and about 52 percent identical to the wild type. Treating them as a pair is the honest reading of this panel and it also makes the experiment easier to interpret: two nearly identical distant ancestors provide an internal replicate that node 1 does not have.

Attribution note. The sequence is Prof. J. Espinoza's design: the GH5 phylogeny, the reconstruction and the node choice are his. The students contributed the structural comparison, the cloning, the expression attempts and the gel analysis.
