# CDS11_WT — BBa_26DKNAEC  (bba-26dknaec)

Live snapshot from registry.igem.org. status=draft

## Functional Description

Residues 305-941 of CDS\_0011 of bacteriophage 9-2-1 Phi8: the trimeric, right-handed beta-helix (beta-solenoid) body of the phage tail spike, plus the C-terminal foldon that carries the trimer contacts. Expressed on its own, away from the virion, it is expected to act as a polysaccharide depolymerase on the host's surface sugar, most likely the LPS O-antigen of soil Pseudomonas. The depolymerase assignment rests on the fold, not on a named homolog, and is stated as a hypothesis. The virion-attachment anchor (residues 1-110) and the shaft (111-300) are deliberately left out, so this part cannot assemble into a virion. The sequence is a coding sequence with its own ATG and stop codon; it does not include the pET-28a leader or the GGSGGGGS-His6-ENLYFQ-GGGGSGGGGS purification linker used in our own construct.

## design

**title:** Domain map, construct boundary at residue 305, and the depolymerase claim

CDS\_0011 is the tail spike of phage 9-2-1 Phi8: a structural protein of the virion and the protein that contacts the host surface. Its 941 aa fold has three modules. Residues 1-110 are a Calx-beta sandwich, the virion-attachment anchor, and all four AlphaFold3 templates (3US9, 3EAD, 2FWU, 2KLT) map there. Residues 111-300 are a shaft that AlphaFold3 cannot place: across five models it lands 41-52 Angstrom apart. Residues 301-941 are a rigid right-handed beta-helix (beta-solenoid) body and receptor-binding region at pLDDT 88-94, with the five models superposing at 0.44-0.99 Angstrom, ending in a foldon (921-941) that carries the trimer contacts.

Construct boundary. The part is residues 305-941: the rigid body plus the foldon, with the unplaceable shaft and the anchor removed. The boundary came from superposing the PI's five AlphaFold3 models and keeping what is rigid across all of them. The body is self-trimerising and self-contained; everything N-terminal of about residue 301 is a floppy appendage.

What kind of enzyme this is, and how strong the claim is. A right-handed beta-helix is the canonical fold of a phage depolymerase, an enzyme that cleaves the host surface polysaccharide rather than merely binding it. We call this a depolymerase on fold evidence alone: AlphaFold3 has no template for residues 111-941, and the beta-helix was identified from the sequence offset period of its backbone hydrogen bonds, not from a named homolog.

This is a different claim, with different evidence, from CDS\_0012. CDS\_0012 is a template-confirmed GH5 glycoside hydrolase and a separate protein, not a domain of this tail spike. There is no evidence that this spike contains a GH5.

Relationship to CDS\_0010. The two fibers share the same N-terminal Calx-beta attachment module: 42 percent identity over 107 aa, and superposing the two anchors gives 0.50 Angstrom RMSD over 446 atoms. They look like paralogous fibers built on a common attachment part.

Tag and linker. Our own plasmid adds the pET-28a N-terminal His6 leader plus a designed GGSGGGGS-His6-ENLYFQ (TEV) linker for Ni-NTA purification and tag removal. The insert ends in its own stop codon, so the vector's C-terminal His6 is never translated: despite the construct filename, this protein has no C-terminal tag. Neither the leader nor the linker is part of the submitted sequence.

Models. AlphaFold3 Server trimer, pTM 0.66 and ipTM 0.64, mean pLDDT 90.3 inside the cloned region. The low ipTM reflects the floppy N-terminal appendage rather than a bad interface; the inter-chain PAE minimum is about 2 Angstrom. The AlphaFold3 folds are Prof. J. Espinoza's work.

## experiment

**title:** Cloning and three expression attempts; no band yet

Cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist Bioscience (order of 2026-07-27). Host E. coli BL21(DE3), kanamycin selection, IPTG induction at 16-20 C. The expressed construct carries the pET-28a leader and the designed GGSGGGGS-His6-ENLYFQ-GGGGSGGGGS linker, giving a predicted mass of 72.0 kDa; neither is part of this part's sequence.

Status: expression not yet demonstrated. Across three SDS-PAGE sessions (2026-09-15, 2026-09-29, 2026-10-10) no band was seen at the expected 72.0 kDa. On 2026-09-29 no undiluted lane was run for this construct, so that absence is not interpretable. The untransformed BL21(DE3) control lane is still outstanding, so no band on these gels can be assigned either way.

Practical notes for anyone repeating this: 72 kDa of trimeric beta-solenoid is a hard expression target. A lower induction temperature, a longer induction and a soluble-versus-pellet fractionation are the next things we would try, together with a codon-optimised synthesis, since the ordered insert was not codon optimised for E. coli.

## characterisation

**title:** No characterisation yet, and the assay this part still needs

None. No confirmed expression (see the Experiment entry), no purified protein, and therefore no activity assay.

The readout this part needs is a spot assay on a host lawn: a halo from purified protein where the buffer control gives none would be direct evidence of depolymerase activity. Controls fixed in advance: imidazole vehicle, PBS, a phage-positive spot, and the sensitive parent strain from the same batch. A first spot test was run on 2026-10-16, but it covered only the three ancestral GH5 variants — this part was not in it.

Until that assay exists, the depolymerase assignment for this part is a structural hypothesis, not a measured activity.

## application

**title:** Targeting and surface-stripping module, and the O-antigen prediction

Intended as the targeting and surface-stripping module of a phage-derived antibacterial toolkit against soil Pseudomonas. A free depolymerase strips the polysaccharide barrier without an infective virion, which is why the body is expressed separately from the phage.

Context from the project: the three ANI-distinct host strains carry three non-homologous O-antigen cassettes in the same ihfB-flanked slot, sharing only 4 of 45 ortholog clusters. Since the receptor is that sugar, host range is predicted to track the cassette. This is a prediction, not a result.

Reusable part of the work: the construct-boundary method. Superpose several predicted models, keep what is rigid across all of them, and cut where the models disagree. Here that turned an ambiguous 941 aa protein into a self-contained 637 aa trimer.

## discussion

**title:** Limitations of a fold-level enzyme claim, and what we would do next

Limitations. The depolymerase assignment is fold-level, with no named homolog and no template for residues 111-941. Treat it as a hypothesis until an activity assay exists. The cut at residue 305 removes the virion anchor by design, so this part cannot assemble into a virion and is not meant to. Expression has not been demonstrated.

Comparison with the other two parts. CDS\_0012 is the better-evidenced enzyme, a template-confirmed GH5, but it is a separate, soluble protein with no host-recognition function. This part carries the targeting, the trimeric beta-helix and the putative enzyme activity in one chain, at the cost of a far weaker enzymatic claim and a much harder expression problem. CDS\_0010 shares this protein's Calx-beta anchor but has no function assigned.

Next steps. Establish expression with a control lane and a soluble-versus-pellet fractionation, purify, then run the spot assay on sensitive and Phi8-resistant lawns. An activity result either way would be the single most informative experiment for this part.
