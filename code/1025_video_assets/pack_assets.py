"""Collect every figure the presentation video draws on into one upload folder.

Two kinds of asset land here, and the README says which is which:

  reference — the animator looks at it and draws something new from it. A
              rendered protein surface is a reference: it never goes on screen
              as a PNG, but the animated blob has to have its proportions.
  on-screen — real data that must appear as itself. A gel, a spot test, a
              phylogeny. Redrawing these would be misrepresenting a result.

    python code/1025_video_assets/pack_assets.py
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "documents/2026-10-25_video_assets"
MAXPX = 2000

# (number, slug, source, kind, beat, what it is / what to draw from it)
ASSETS = [
    # ---- Act I: the organism, the genome, the question ---------------------
    ("01", "virion-to-scale",
     "code/output/1018_construct_structures/panels/virion_to_scale.png",
     "reference", "Act I — what a phage is",
     "Our phage rendered at true relative scale. Use for the proportions of "
     "head, collar and tail; the animated phage must not have a fat head."),
    ("02", "virion-assembly",
     "code/output/1018_construct_structures/panels/virion_assembly.png",
     "reference", "Act I — what a phage is",
     "How the tail module assembles. Shows where the spike sits."),
    ("03", "phage-tail-module",
     "code/output/0729_prof_figures/fig_phage_tail_module.png",
     "reference", "Act I — what a phage is",
     "The tail gene module. Source for the spike's shape and its neighbours."),
    ("04", "phage-genome-map",
     "code/output/0729_prof_figures/fig_phage_genome_map.png",
     "on-screen", "Act I — the genome we sequenced",
     "9-2-1 Phi8, 62 kb, 80 CDS. Real annotation — goes on screen as itself."),
    ("05", "bacterial-genomes",
     "code/output/0729_prof_figures/fig_bacterial_genomes.png",
     "on-screen", "Act I — the three hosts",
     "The three Pseudomonas isolates. Establishes that strains differ."),
    ("06", "circos-9-2-1",
     "code/output/0729_prof_figures/panels/circos_9-2-1.png",
     "reference", "Act I — the three hosts",
     "Circular genome view. Reference for the look of a genome diagram."),

    # ---- Cycle 1: the wrong question ---------------------------------------
    ("07", "iptm-matrix",
     "code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap.png",
     "on-screen", "Cycle 1 — the screen",
     "The 7,182-pair interface-score matrix. This IS the thing that was "
     "retired; the animated matrix of cells is drawn from its shape."),
    ("08", "control-validation",
     "code/output/0703_phage_host_matrix/fold/control_validation.png",
     "on-screen", "Cycle 1 — the control gate",
     "The controls that did not separate. The decisive figure of Act I."),
    ("09", "binding-controls-comparison",
     "documents/2026-07-13_binding_controls_comparison.png",
     "on-screen", "Cycle 1 — the control gate",
     "Known binder vs scrambled vs mismatched, two tools. The same answer "
     "twice, which is why the method was retired and not retried."),
    ("10", "fold-comparison",
     "code/output/0712_phage_rbp_detect/structure/fig_fold_comparison.png",
     "reference", "Cycle 1 — folds",
     "Fold types side by side. Reference for how a beta-helix differs from "
     "an alpha-helix and a sandwich at a glance."),

    # ---- Cycle 2: ask the protein what it is -------------------------------
    ("11", "cds11-trimer-domains",
     "code/output/0729_prof_figures/panels/cds0011_trimer_domains.png",
     "reference", "Cycle 2 — the tail spike",
     "CDS_0011 as a trimer, domains coloured. The long beta-helix body is "
     "the shape the rung-period test identified."),
    ("12", "cds11-body-side",
     "code/output/0729_prof_figures/panels/cds0011_body_side.png",
     "reference", "Cycle 2 — the beta-helix",
     "Side view: the coiled prism. The animated prism is drawn from this — "
     "match the number of visible coils and the taper."),
    ("13", "cds11-body-axial",
     "code/output/0729_prof_figures/panels/cds0011_body_axial.png",
     "reference", "Cycle 2 — the beta-helix",
     "Down the axis: the triangular cross-section. Use when showing why the "
     "rungs stack in register."),
    ("14", "cds12-gh5",
     "code/output/0729_prof_figures/panels/cds0012_gh5.png",
     "reference", "Cycle 2 — the other enzyme",
     "CDS_0012, a TIM barrel matched to endoglucanase 1ECE. A DIFFERENT "
     "protein from CDS_0011 and a different substrate — never merge the two."),
    ("15", "cds12-family-overlay",
     "code/output/1018_construct_structures/panels/cds12_family_overlay.png",
     "reference", "Cycle 3 — the ancestors",
     "CDS_0012 and its three reconstructed ancestors superposed. The fold is "
     "conserved; the surface is not."),
    ("16", "o-antigen-loci",
     "code/output/0727_o_antigen_comparison/o_antigen_loci_comparison.png",
     "on-screen", "Cycle 2 — the cassette",
     "The O-antigen locus in each strain: same slot, same flanks, unrelated "
     "cargo. Source for the animated gene row — gene counts must match."),
    ("17", "cassette-o-antigen",
     "code/output/1010_resistant_mutant_comparison/fig_cassette_o_antigen.png",
     "on-screen", "Cycle 2 — the cassette",
     "The cassette again, in the mutant comparison. Shows the O-antigen is "
     "untouched in the resistant mutant."),

    # ---- Cycle 3: build the enzymes ----------------------------------------
    ("18", "gh5-tree-phylogram",
     "code/output/1020_zymctrl_figure/fig-gh5-tree-phylogram.png",
     "on-screen", "Cycle 3 — ancestral reconstruction",
     "The GH5 phylogeny with the reconstructed nodes marked. The animated "
     "tree is a simplification of this one — keep the node order."),
    ("19", "zymctrl-perplexity",
     "code/output/1020_zymctrl_figure/fig_zymctrl_perplexity.png",
     "on-screen", "Cycle 3 — scoring the designs",
     "ZymCTRL perplexity for each candidate. How we chose what to order."),
    ("20", "cds12-wt",
     "code/output/1018_construct_structures/panels/CDS12_WT.png",
     "reference", "Cycle 3 — the constructs", "Present-day CDS_0012."),
    ("21", "cds12-anc-node1",
     "code/output/1018_construct_structures/panels/CDS12_ANC_Node1.png",
     "reference", "Cycle 3 — the constructs", "Reconstructed ancestor, Node 1."),
    ("22", "cds12-anc-node40",
     "code/output/1018_construct_structures/panels/CDS12_ANC_Node40.png",
     "reference", "Cycle 3 — the constructs", "Reconstructed ancestor, Node 40."),
    ("23", "cds12-anc-node281",
     "code/output/1018_construct_structures/panels/CDS12_ANC_Node281.png",
     "reference", "Cycle 3 — the constructs", "Reconstructed ancestor, Node 281."),
    ("24", "constructs-overview",
     "code/output/1018_construct_structures/fig_constructs_overview.png",
     "on-screen", "Cycle 3 — what we ordered",
     "All six constructs with their masses. The table behind the gels."),
    ("25", "gel-0929",
     "code/output/0929_gel_annotation/cds12-cds11_annotated_flattened_color.jpg",
     "on-screen", "Cycle 3 — expression",
     "29 Sept gel. CDS12 IPTG-only band at 40-43 kDa, e1 at 45-50 kDa."),
    ("26", "gel-1010-nta",
     "code/output/1010_gel_annotation/nta-fractions_annotated_flattened_color.jpg",
     "on-screen", "Cycle 3 — the nickel column",
     "10 Oct Ni-NTA fractions. Elutions blank, flow-through looks like the "
     "load. This is the failure the column animation explains."),
    ("27", "dotblot",
     "code/output/1019_dotblot/fig_dotblot_annotated.png",
     "on-screen", "Cycle 3 — the cheap assay",
     "Anti-His dot blot. The flow-through is 2.9x the negative control — the "
     "protein was there, capture failed."),

    # ---- Cycle 4: let the bacteria answer ----------------------------------
    ("28", "spot-test-normalised",
     "code/output/1016_spot_test_result/fig_spot_test_normalised.png",
     "on-screen", "Cycle 4 — does it still kill",
     "16 Oct spot test, normalised to the PBS control: 12 percent."),
    ("29", "spot-test-hostrange",
     "code/output/1016_spot_test_result/fig_spot_test_hostrange.png",
     "on-screen", "Cycle 4 — host range",
     "The same test grouped by host range."),
    ("30", "mutation-read-level",
     "code/output/1010_resistant_mutant_comparison/fig_mutation_962_mut_4643730.png",
     "on-screen", "Cycle 4 — the one mutation",
     "9-6-2 r1, Stealth CR3 F126L, at read level: 263 of 264 reads. The "
     "animated read-support bars are drawn from these numbers."),
    ("31", "read-support-heatmap",
     "code/output/1010_resistant_mutant_comparison/fig_read_support_heatmap.png",
     "on-screen", "Cycle 4 — the other sixteen",
     "All 17 candidate differences checked against raw reads. Sixteen fall."),
    ("32", "circos-parent-vs-mutants",
     "code/output/1010_resistant_mutant_comparison/fig_circos_parent_vs_mutants.png",
     "reference", "Cycle 4 — the resistant mutants",
     "Parent against both resistant mutants. Reference for the scale of the "
     "comparison: almost nothing differs."),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows, missing = [], []
    for num, slug, rel, kind, beat, note in ASSETS:
        src = ROOT / rel
        if not src.exists():
            missing.append(rel)
            continue
        im = Image.open(src)
        before = im.size
        im.thumbnail((MAXPX, MAXPX), Image.LANCZOS)
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
        elif im.mode != "RGB":
            im = im.convert("RGB")
        dst = OUT / f"{num}-{slug}.png"
        im.save(dst)
        rows.append((dst.name, kind, beat, note, rel, before, im.size))
        print(f"{dst.name:34s} {before[0]:5d}x{before[1]:<5d} -> "
              f"{im.size[0]}x{im.size[1]}  [{kind}]")

    readme = [
        "# Video assets — presentation video, iGEM 2026 Claremont-CA",
        "",
        "Every figure the presentation video draws on, in one place, so the",
        "design system has them as assets and an animation prompt can name one",
        "instead of describing it.",
        "",
        "Two kinds:",
        "",
        "- **reference** — the animator looks at it and draws something new.",
        "  A rendered protein surface never goes on screen as a PNG, but the",
        "  animated shape has to have its proportions.",
        "- **on-screen** — real data that must appear as itself. Gels, spot",
        "  tests, phylogenies, matrices. Redrawing one of these in a nicer",
        "  hand would be misrepresenting a result, and the judges score",
        "  exactly that.",
        "",
        f"Longest edge capped at {MAXPX} px. Rebuild with",
        "`python code/1025_video_assets/pack_assets.py`.",
        "",
        "| file | kind | beat | what it is | source |",
        "| --- | --- | --- | --- | --- |",
    ]
    for name, kind, beat, note, rel, _b, _a in rows:
        readme.append(f"| `{name}` | {kind} | {beat} | {note} | `{rel}` |")
    readme += [
        "",
        "## Not here yet",
        "",
        "- California Botanic Garden interview clips and site photographs —",
        "  footage, not figures; they come from Alex.",
        "- Team and credits material for the closing card.",
        "",
        "## One thing to get right",
        "",
        "`14-cds12-gh5` and `11-cds11-trimer-domains` are two different",
        "proteins. CDS_0012 is a TIM barrel matched to endoglucanase 1ECE,",
        "with a different substrate from the O-antigen the CDS_0011 tail",
        "spike reads. All three reconstructed ancestors are CDS_0012's.",
        "Never draw them as domains of one protein.",
        "",
        f"_Log: assembled {len(rows)} assets, "
        f"{len(missing)} source(s) missing._",
    ]
    (OUT / "README.md").write_text("\n".join(readme) + "\n")

    if missing:
        print("\nMISSING:")
        for m in missing:
            print(f"  {m}")
    print(f"\n{len(rows)} assets -> {OUT}")


if __name__ == "__main__":
    main()
