# CDS12_WT - BBa_267WQM51  (bba-267wqm51)

Paste-ready. Live registry text as of 2026-10-19 with the 2026-10-19 dot blot merged in. status=draft

## Functional Description

Catalytic region (residues 117-477) of CDS\_0012 of bacteriophage 9-2-1 Phi8: a glycoside hydrolase family 5 (GH5) enzyme. The part is expected to fold into the (beta/alpha)8 TIM barrel of CAZy clan GH-A and to hydrolyse a polysaccharide of the Pseudomonas cell surface, acting as a free, standalone enzyme rather than as a virion-attached structural protein. Catalysis is expected to follow the retaining double-displacement mechanism of GH5, with the acid/base glutamate in the conserved NEP motif. The part is a coding sequence that begins with ATG and ends with a stop codon; it does not include the pET-28a MGSSHHHHHHSSGLVPRGSHM leader we used for expression, so users can add the affinity tag of their choice.

## design

**title:** GH5 assignment, construct boundary and model validation

CDS\_0012 is a glycoside hydrolase family 5 (GH5) enzyme: CAZy clan GH-A, a (beta/alpha)8 TIM barrel with a retaining mechanism and the catalytic glutamates on the C-terminal face of the barrel. GH5 contains the classic bacterial endoglucanases, and in phage genomes GH5-like enzymes act as depolymerases that strip the capsule, EPS or O-antigen standing between the phage and the cell surface. Because it is a soluble enzyme and not a virion component, it can be applied without the phage.

Evidence. All four AlphaFold3 templates over residues 118-475 are GH5 endoglucanases: 1ECE (with cellotetraose bound), 1VRX, 4TUF and 2ZUM, at pLDDT 95-98. AF3 monomer pTM 0.77; mean pLDDT 96.4 inside the cloned region, with 98.9 percent of those residues above 70. The AlphaFold3 folds are Prof. J. Espinoza's work.

This part is a separate protein, not a domain of the tail spike. The tail spike, CDS\_0011, is submitted as its own part: virion-attached, and a depolymerase on fold evidence only (beta-helix periodicity, no template, no named homolog). CDS\_0010 is a third protein, of unknown function. Three proteins, three different evidence grades.

Construct boundary. Residues 117-477 cover essentially the whole TIM barrel; only a short N-terminal extension is left out, so the part is the catalytic unit.

Catalytic machinery. The GH5 acid/base glutamate sits in the conserved NEP motif, IGADLYNEPHL at insert position 165, with the conserved SPH(D/E)Y block downstream. The nucleophile has not yet been assigned structurally by superposition on 1ECE.

Variants. Three reconstructed ancestors of this enzyme are submitted as separate parts of the same collection. Superposed on this protein's model they give 0.28, 0.50 and 0.52 Angstrom backbone RMSD, inside the 2 Angstrom equivalence criterion, although Node40 and Node281 share only about 52 percent sequence identity with it.

Model validation. Folding this sequence with ESMFold (single sequence, no MSA, no template) and superposing it on the AlphaFold3 model of the same region gives 0.28 Angstrom over 2139 atoms. Two independent methods agree, which is what licenses the ESMFold models used for the ancestral variants.

## experiment

**title:** Cloning and expression trial in E. coli BL21(DE3)

Cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist Bioscience (order of 2026-07-27). Expressed in E. coli BL21(DE3) with kanamycin selection, induced with IPTG at ~30 C for 16 h. The construct we expressed carries the vector's N-terminal His6 leader MGSSHHHHHHSSGLVPRGSHM, which is not part of this part's sequence; the predicted mass of the tagged protein is 41.8 kDa.

SDS-PAGE, 2026-09-29. An IPTG-dependent band at 40-43 kDa, on the predicted 41.8 kDa, absent from the uninduced lane even though that lane carried more total protein. This is the first induction-dependent signal in the project, and this construct is first in the purification queue.

Anti-His dot blot, 2026-10-19. Eleven samples were spotted directly onto membrane and probed with a single-step anti-His HRP conjugate; the positive control reached about 18 times the negative control, so the detection chemistry worked. A dot blot reports the His tag, not size or activity, and this membrane's detection floor is high: every 1:10 dilution on it fell to background, so an absent signal here is weak evidence of absence.

This construct was spotted as an induced and uninduced pair, and the two are indistinguishable, at 4.4 against 3.9, a ratio of 1.1 that sits inside the noise. The blot therefore gives no induction-dependent His signal for this construct, on a membrane where the positive control reached about 18 times the negative and two other constructs were positive. It does not overturn the 2026-09-29 band, but it does not support it either, and the two results should be read together.

Ni-NTA purification, 2026-10-01. This construct was one of six purified over NEBExpress Ni spin columns (NEB S1427) in a single session and gave no band in either elution; by Bradford, its E2 fell below the lower limit of quantification. Nothing was recovered, which stands against the induction-dependent band of 2026-09-29 and is unexplained.

Not yet done: an untransformed BL21(DE3) control lane, a size-resolved anti-His western, and a second purification attempt with reworked binding conditions. The codon usage of the synthesised insert was not optimised for E. coli, so Rosetta or BL21-CodonPlus are the obvious alternative hosts if the yield is poor.

## characterisation

**title:** Preliminary and incomplete characterisation

Preliminary and incomplete.

One induction-dependent band at the predicted mass (see the Experiment entry). Not confirmed to be this protein: no western, no mass spectrometry, and the control lane that would exclude a host band is outstanding.

No purified protein was recovered on 2026-10-01, therefore no activity data. This construct was also not included in the 2026-10-16 spot test, so the ancestor-versus-modern comparison the design asks for still has no modern arm.

Note for anyone reusing these parts: this protein and its three ancestral variants differ by at most 0.43 kDa (1.0 percent) and cannot be distinguished by SDS-PAGE. Identity needs sequencing or intact-mass MS.

Not included in the 2026-10-16 spot test. That run compared the three ancestral variants against phage Phi8 and a sterile-PBS control on seven Pseudomonas lawns. The e1 preparation suppressed colony growth inside the drop to a median of 12 percent of the same-plate PBS control, against 0 percent for the phage. This wild-type enzyme is the missing comparator: without it on the same plate, no ancestor-versus-modern claim can be made. Putting CDS12\_WT into that assay is the highest-value next experiment for this part.

The readout it needs is a spot assay on a host lawn, with a halo scored against an elution-buffer control.

## application

**title:** Surface-stripping module of a phage-derived antibacterial toolkit

Intended as the surface-stripping module of a phage-derived antibacterial toolkit against soil Pseudomonas. As a free enzyme it can be applied without an infective virion, which is the route we are pursuing for phage-resistant hosts.

In that toolkit it sits beside the tail spike CDS\_0011 (host recognition and a trimeric beta-helix) and CDS\_0010 (unknown function, sharing the Calx-beta anchor of the spike), and beside its own three reconstructed ancestors, which are tested for a broader substrate range than this modern enzyme.

Reusable by any team that wants a well-templated phage GH5 as a positive control for depolymerase work, or a modern-versus-ancestral enzyme pair. The part is a plain coding sequence with its own ATG and stop codon, so it drops into any expression vector and takes whichever affinity tag the user prefers.

## discussion

**title:** Limitations, comparison with the tail spike, and next steps

Limitations. The GH5 assignment is structural (templates plus fold), not enzymatic: no substrate has been tested, and the natural substrate is assumed to be the host surface polysaccharide rather than cellulose. The expression evidence is a single band at the right size, which is not an identification, and the 2026-10-19 anti-His dot blot did not reproduce an induction-dependent signal for it. The catalytic nucleophile has not been assigned structurally.

Comparison. Against the tail spike CDS\_0011, this protein is the better-evidenced enzyme but the weaker targeting module: the spike carries host recognition and the trimeric beta-helix, while this one is a compact, soluble, monomeric barrel, easier to express, purify and apply. The two should not be read as one protein; the depolymerase claim for CDS\_0011 rests on fold evidence alone.

Future directions. Purify, confirm identity by western blot or mass spectrometry, then assay against the host's purified LPS and against Phi8-resistant mutants, side by side with the three reconstructed ancestors.
