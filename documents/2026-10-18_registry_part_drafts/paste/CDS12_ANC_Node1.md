# CDS12_ANC_Node1 - BBa_26TWEX42  (bba-26twex42)

Paste-ready. Live registry text as of 2026-10-19 with the 2026-10-19 dot blot merged in. status=draft

## Functional Description

A reconstructed ancestor of the phage GH5 glycoside hydrolase CDS\_0012, designed to test whether an ancestral enzyme has a broader substrate range than its modern, specialised descendant. The sequence is computationally designed and does not exist in nature. It is 77.8 percent identical to the modern enzyme, the closest of the three ancestral nodes we submit, and it is expected to fold into the same (beta/alpha)8 GH5 TIM barrel and to retain the acid/base glutamate in the conserved NEP motif. The part is a coding sequence with its own ATG and stop codon and does not include the pET-28a His6 leader used in our own expression construct. An anti-His dot blot on 2026-10-19 gave a positive signal for this construct's induced lysate, at 2.4 times the negative control; the product has not been assigned by size. See the documentation entries.

## design

**title:** Ancestral reconstruction, sequence identities, and the conserved NEP motif

**Hypothesis.** Modern phage depolymerases are specialists: each is tuned to the surface sugar of its own host, which is why phage therapy fails once a host changes that sugar. Reconstructed ancestors of enzyme families are repeatedly found to be more promiscuous than their modern descendants. An ancestral form of our GH5 may therefore cleave polysaccharides the wild-type enzyme cannot, including on phage-resistant mutants. The three ancestral nodes we submit (node 1, node 40, node 281) are that test, and they only make sense as a set.

Where this sequence sits, as percent identity over the 361 aa mature insert: node 1 is 77.8 percent identical to the modern enzyme CDS\_0012, 61.8 percent to node 40 and 57.1 percent to node 281. Node 40 and node 281 are 87.3 percent identical to each other and only about 52 percent to the modern enzyme. So the panel is the wild type, one close ancestor and a distant pair, not three equally spaced points.

We deliberately do not describe this node by tree depth. Until the PI states where node 1 sits on his tree, the identities above are all we can honestly say.

**Structure.** ESMFold v1, single sequence, no MSA, no template: mean pLDDT 90.0, with 95.8 percent of residues above 70, the most confident of the three ancestral models. Superposed on the ESMFold model of CDS12\_WT it gives 0.28 Angstrom backbone RMSD, well inside the 2 Angstrom equivalence criterion. The reconstruction changes the surface, not the fold.

**Method validation.** The wild type folded with the same single-sequence method superposes on the AlphaFold3 model of the same region at 0.28 Angstrom over 2139 atoms, so these ancestral models are not an artefact of the single-sequence method.

**Catalytic machinery.** The GH5 acid/base glutamate sits in the conserved NEP motif, IGADLYNEPHQ at insert position 166, with a conserved SPHEY block downstream. Same fold, same catalytic residues, different surface: the structural precondition for an active enzyme with altered specificity.

**Relationship to the other parts.** This is a variant of CDS12\_WT, the template-confirmed GH5 - a free, standalone enzyme. It is not related to the tail spike CDS\_0011, whose depolymerase assignment is fold-level only, and not to CDS\_0010, whose function is unknown.

## experiment

**title:** Cloning, induction, and an unassigned 45-50 kDa band

Cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist Bioscience; order sheet filed 2026-09-10. Host E. coli BL21(DE3), kanamycin selection, IPTG induction at ~30 C. Predicted mass of the tagged protein 41.9 kDa.

Codon usage warning. The insert was ordered with Codon Optimized set to No and carries a mammalian-like codon bias (CCC, GGG, GCC heavy) rather than an E. coli bias. This is the first thing to suspect behind a missing band; Rosetta or BL21-CodonPlus are the obvious alternative hosts.

SDS-PAGE, 2026-09-29. A strong, clean band at 45-50 kDa appeared in all four lanes, induced and uninduced alike, 7-19 percent above the predicted 41.9 kDa. It is unassigned. It cannot simply be called the product, because CDS12\_WT, which has essentially the same mass, ran on the predicted mass in the same experiment. A host protein fits the data equally well, and the untransformed BL21(DE3) control lane that would settle it has still not been run.

Anti-His dot blot, 2026-10-19. Eleven samples were spotted directly onto membrane and probed with a single-step anti-His HRP conjugate; the positive control reached about 18 times the negative control, so the detection chemistry worked. A dot blot reports the His tag, not size or activity, and this membrane's detection floor is high: every 1:10 dilution on it fell to background, so an absent signal here is weak evidence of absence.

This construct's induced rough lysate was His-positive at 2.4 times the negative control, the third strongest signal on the membrane. That supports expression of a tagged product, but because a dot blot carries no size information it cannot distinguish full-length protein from a truncation or from free tag, and so does not on its own assign the unexplained 45-50 kDa band.

## characterisation

**title:** First activity data: a positive signal that is not yet attributed

First activity data, 2026-10-16. A positive but preliminary signal.

Spot test. Seven Pseudomonas strains were grown as double-layer lawns, 200 microlitres of culture in 3 millilitres of soft agar. Each plate received five 7 microlitre drops: phage Phi8 stock as the positive control, sterile 1x PBS as the negative control, and the e1, e40 and e281 preparations, each diluted 1 in 10 in that same sterile PBS. Spotted 12 October, read 16 October.

No drop produced a clear lysis zone, Phi8 included. The readout was colony growth inside the drop: sterile PBS drops reproducibly developed discrete colonies, a median of 14 per drop, which is the baseline for a liquid drop landing on these lawns. Every plate carried its own PBS drop and that baseline varied between plates, from 7 to 17 colonies, so the comparable figure is each drop as a percentage of the PBS drop on the same plate. On that scale the medians are Phi8 0 percent, e1 12 percent, e281 53 percent, e40 67 percent.

The e1 preparation suppressed colony growth almost completely, as did the phage, on six of the seven strains. The e1 drop was 90 percent the same sterile PBS, so the difference comes from the e1 preparation itself.

What this does and does not establish.

This is the first evidence that the e1 preparation carries an activity against Pseudomonas, and the strongest signal of the three ancestral variants.

It does not identify the active agent as this protein. Expression now has positive evidence, the induced lysate being His-positive at 2.4 times the negative control on the 2026-10-19 dot blot, but a His tag in the lysate does not make this protein the active species, and the elution buffer the preparation sits in, imidazole included, was not spotted on its own.

The largest remaining confound is phage carried over from the Phi8 stock. Across the seven strains e1 tracks the phage almost exactly: both fall below 40 percent on six strains, and the single strain where the phage failed, 9-1-1 at 157 percent, is also the one where e1 failed, at 114 percent. An infectious contaminant would produce precisely that agreement. The deciding experiment is a plaque assay of the e1 preparation itself on a sensitive lawn, and it has not been done. Suppression in this assay does not require infection either, since Phi8 cleared colonies on two of the three strains it cannot plaque, so the fact that e1 works on non-hosts does not resolve this.

The wild-type enzyme CDS12\_WT was not spotted in this run, so the ancestor-versus-modern comparison the design asks for has not been made yet.

One concentration, one plate per strain, colonies counted by automated image segmentation. No replicates and no statistics.

No clearing means no halo, so this is not depolymerase activity in the classical sense.

This part cannot be distinguished from CDS12\_WT or the other two ancestors by SDS-PAGE: all four are within 0.43 kDa, 1.0 percent, of each other. Identification needs sequencing or intact-mass MS.

Planned next, in order: a plaque assay of the e1 preparation on a sensitive lawn; an elution-buffer-only drop; a dilution series of e1; and the same plate run with CDS12\_WT alongside.

## application

**title:** The conservative arm of an ancestral-versus-modern enzyme panel

Intended as the broad-spectrum arm of a phage-derived antibacterial toolkit: an enzyme that may clear surface polysaccharides the modern enzyme cannot, on hosts that have escaped the phage by changing that sugar.

Within our panel this node is the conservative test. At 77.8 percent identity to the modern enzyme it is the closest ancestor we submit, so if even this one behaves differently from CDS12\_WT the effect is unlikely to be an artefact of sequence distance alone. Nodes 40 and 281 probe much further out.

Reusable by any team that wants a matched ancestral-versus-modern depolymerase pair, which is a cheap internal control for substrate-range experiments: same fold, same catalytic residues, different surface.

## discussion

**title:** Limitations of a reconstructed sequence, and its role in the set

Limitations. A reconstructed sequence is a hypothesis about a protein that no longer exists; it is not evidence about any real ancestral phage. Expression is supported by anti-His signal, but the product has never been assigned by size: the 45-50 kDa band remains unexplained, and a dot blot cannot tell full-length protein from a truncation or from free tag. The non-optimised, mammalian-like codon usage is a live expression risk. The structural evidence is a single-sequence model: it says the fold survives the reconstruction, not that the enzyme works.

Role in the set. At 77.8 percent identity to the wild type this is the conservative node. Nodes 40 and 281 sit about 52 percent from the wild type and 87.3 percent from each other, so they act as a near-duplicate pair at the far end while this one anchors the near end.

Attribution note. The sequence of this part is Prof. J. Espinoza's design: the GH5 phylogeny, the ancestral-state reconstruction and the choice of nodes are his. The students contributed the structural comparison of the variants, the cloning, the expression trials and the gel densitometry.
