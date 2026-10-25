# Video assets — presentation video, iGEM 2026 Claremont-CA

Every figure the presentation video draws on, in one place, so the
design system has them as assets and an animation prompt can name one
instead of describing it.

Two kinds:

- **reference** — the animator looks at it and draws something new.
  A rendered protein surface never goes on screen as a PNG, but the
  animated shape has to have its proportions.
- **on-screen** — real data that must appear as itself. Gels, spot
  tests, phylogenies, matrices. Redrawing one of these in a nicer
  hand would be misrepresenting a result, and the judges score
  exactly that.

Longest edge capped at 2000 px. Rebuild with
`python code/1025_video_assets/pack_assets.py`.

| file | kind | beat | what it is | source |
| --- | --- | --- | --- | --- |
| `01-virion-to-scale.png` | reference | Act I — what a phage is | Our phage rendered at true relative scale. Use for the proportions of head, collar and tail; the animated phage must not have a fat head. | `code/output/1018_construct_structures/panels/virion_to_scale.png` |
| `02-virion-assembly.png` | reference | Act I — what a phage is | How the tail module assembles. Shows where the spike sits. | `code/output/1018_construct_structures/panels/virion_assembly.png` |
| `03-phage-tail-module.png` | reference | Act I — what a phage is | The tail gene module. Source for the spike's shape and its neighbours. | `code/output/0729_prof_figures/fig_phage_tail_module.png` |
| `04-phage-genome-map.png` | on-screen | Act I — the genome we sequenced | 9-2-1 Phi8, 62 kb, 80 CDS. Real annotation — goes on screen as itself. | `code/output/0729_prof_figures/fig_phage_genome_map.png` |
| `05-bacterial-genomes.png` | on-screen | Act I — the three hosts | The three Pseudomonas isolates. Establishes that strains differ. | `code/output/0729_prof_figures/fig_bacterial_genomes.png` |
| `06-circos-9-2-1.png` | reference | Act I — the three hosts | Circular genome view. Reference for the look of a genome diagram. | `code/output/0729_prof_figures/panels/circos_9-2-1.png` |
| `07-iptm-matrix.png` | on-screen | Cycle 1 — the screen | The 7,182-pair interface-score matrix. This IS the thing that was retired; the animated matrix of cells is drawn from its shape. | `code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap.png` |
| `08-control-validation.png` | on-screen | Cycle 1 — the control gate | The controls that did not separate. The decisive figure of Act I. | `code/output/0703_phage_host_matrix/fold/control_validation.png` |
| `09-binding-controls-comparison.png` | on-screen | Cycle 1 — the control gate | Known binder vs scrambled vs mismatched, two tools. The same answer twice, which is why the method was retired and not retried. | `documents/2026-07-13_binding_controls_comparison.png` |
| `10-fold-comparison.png` | reference | Cycle 1 — folds | Fold types side by side. Reference for how a beta-helix differs from an alpha-helix and a sandwich at a glance. | `code/output/0712_phage_rbp_detect/structure/fig_fold_comparison.png` |
| `11-cds11-trimer-domains.png` | reference | Cycle 2 — the tail spike | CDS_0011 as a trimer, domains coloured. The long beta-helix body is the shape the rung-period test identified. | `code/output/0729_prof_figures/panels/cds0011_trimer_domains.png` |
| `12-cds11-body-side.png` | reference | Cycle 2 — the beta-helix | Side view: the coiled prism. The animated prism is drawn from this — match the number of visible coils and the taper. | `code/output/0729_prof_figures/panels/cds0011_body_side.png` |
| `13-cds11-body-axial.png` | reference | Cycle 2 — the beta-helix | Down the axis: the triangular cross-section. Use when showing why the rungs stack in register. | `code/output/0729_prof_figures/panels/cds0011_body_axial.png` |
| `14-cds12-gh5.png` | reference | Cycle 2 — the other enzyme | CDS_0012, a TIM barrel matched to endoglucanase 1ECE. A DIFFERENT protein from CDS_0011 and a different substrate — never merge the two. | `code/output/0729_prof_figures/panels/cds0012_gh5.png` |
| `15-cds12-family-overlay.png` | reference | Cycle 3 — the ancestors | CDS_0012 and its three reconstructed ancestors superposed. The fold is conserved; the surface is not. | `code/output/1018_construct_structures/panels/cds12_family_overlay.png` |
| `16-o-antigen-loci.png` | on-screen | Cycle 2 — the cassette | The O-antigen locus in each strain: same slot, same flanks, unrelated cargo. Source for the animated gene row — gene counts must match. | `code/output/0727_o_antigen_comparison/o_antigen_loci_comparison.png` |
| `17-cassette-o-antigen.png` | on-screen | Cycle 2 — the cassette | The cassette again, in the mutant comparison. Shows the O-antigen is untouched in the resistant mutant. | `code/output/1010_resistant_mutant_comparison/fig_cassette_o_antigen.png` |
| `18-gh5-tree-phylogram.png` | on-screen | Cycle 3 — ancestral reconstruction | The GH5 phylogeny with the reconstructed nodes marked. The animated tree is a simplification of this one — keep the node order. | `code/output/1020_zymctrl_figure/fig-gh5-tree-phylogram.png` |
| `19-zymctrl-perplexity.png` | on-screen | Cycle 3 — scoring the designs | ZymCTRL perplexity for each candidate. How we chose what to order. | `code/output/1020_zymctrl_figure/fig_zymctrl_perplexity.png` |
| `20-cds12-wt.png` | reference | Cycle 3 — the constructs | Present-day CDS_0012. | `code/output/1018_construct_structures/panels/CDS12_WT.png` |
| `21-cds12-anc-node1.png` | reference | Cycle 3 — the constructs | Reconstructed ancestor, Node 1. | `code/output/1018_construct_structures/panels/CDS12_ANC_Node1.png` |
| `22-cds12-anc-node40.png` | reference | Cycle 3 — the constructs | Reconstructed ancestor, Node 40. | `code/output/1018_construct_structures/panels/CDS12_ANC_Node40.png` |
| `23-cds12-anc-node281.png` | reference | Cycle 3 — the constructs | Reconstructed ancestor, Node 281. | `code/output/1018_construct_structures/panels/CDS12_ANC_Node281.png` |
| `24-constructs-overview.png` | on-screen | Cycle 3 — what we ordered | All six constructs with their masses. The table behind the gels. | `code/output/1018_construct_structures/fig_constructs_overview.png` |
| `25-gel-0929.png` | on-screen | Cycle 3 — expression | 29 Sept gel. CDS12 IPTG-only band at 40-43 kDa, e1 at 45-50 kDa. | `code/output/0929_gel_annotation/cds12-cds11_annotated_flattened_color.jpg` |
| `26-gel-1010-nta.png` | on-screen | Cycle 3 — the nickel column | 10 Oct Ni-NTA fractions. Elutions blank, flow-through looks like the load. This is the failure the column animation explains. | `code/output/1010_gel_annotation/nta-fractions_annotated_flattened_color.jpg` |
| `27-dotblot.png` | on-screen | Cycle 3 — the cheap assay | Anti-His dot blot. The flow-through is 2.9x the negative control — the protein was there, capture failed. | `code/output/1019_dotblot/fig_dotblot_annotated.png` |
| `28-spot-test-normalised.png` | on-screen | Cycle 4 — does it still kill | 16 Oct spot test, normalised to the PBS control: 12 percent. | `code/output/1016_spot_test_result/fig_spot_test_normalised.png` |
| `29-spot-test-hostrange.png` | on-screen | Cycle 4 — host range | The same test grouped by host range. | `code/output/1016_spot_test_result/fig_spot_test_hostrange.png` |
| `30-mutation-read-level.png` | on-screen | Cycle 4 — the one mutation | 9-6-2 r1, Stealth CR3 F126L, at read level: 263 of 264 reads. The animated read-support bars are drawn from these numbers. | `code/output/1010_resistant_mutant_comparison/fig_mutation_962_mut_4643730.png` |
| `31-read-support-heatmap.png` | on-screen | Cycle 4 — the other sixteen | All 17 candidate differences checked against raw reads. Sixteen fall. | `code/output/1010_resistant_mutant_comparison/fig_read_support_heatmap.png` |
| `32-circos-parent-vs-mutants.png` | reference | Cycle 4 — the resistant mutants | Parent against both resistant mutants. Reference for the scale of the comparison: almost nothing differs. | `code/output/1010_resistant_mutant_comparison/fig_circos_parent_vs_mutants.png` |

## Not here yet

- California Botanic Garden interview clips and site photographs —
  footage, not figures; they come from Alex.
- Team and credits material for the closing card.

## One thing to get right

`14-cds12-gh5` and `11-cds11-trimer-domains` are two different
proteins. CDS_0012 is a TIM barrel matched to endoglucanase 1ECE,
with a different substrate from the O-antigen the CDS_0011 tail
spike reads. All three reconstructed ancestors are CDS_0012's.
Never draw them as domains of one protein.

_Log: assembled 32 assets, 0 source(s) missing._
