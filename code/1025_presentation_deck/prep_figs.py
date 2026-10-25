"""Thumbnail the figures the deck uses into the repo, so a rebuild needs nothing else.

    python code/1025_presentation_deck/prep_figs.py
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/1025_presentation_deck/figs"

SOURCES = {
    "trimer": "code/output/0729_prof_figures/panels/cds0011_trimer_domains.png",
    "body-side": "code/output/0729_prof_figures/panels/cds0011_body_side.png",
    "body-axial": "code/output/0729_prof_figures/panels/cds0011_body_axial.png",
    "gh5": "code/output/0729_prof_figures/panels/cds0012_gh5.png",
    "cds12-family": "code/output/1018_construct_structures/panels/cds12_family_overlay.png",
    "virion": "code/output/1018_construct_structures/panels/virion_to_scale.png",
    "controls": "documents/2026-07-13_binding_controls_comparison.png",
    "oantigen": "code/output/0727_o_antigen_comparison/o_antigen_loci_comparison.png",
    "zymctrl": "code/output/1020_zymctrl_figure/fig_zymctrl_perplexity.png",
    "gel0929": "code/output/0929_gel_annotation/cds12-cds11_annotated_flattened_color.jpg",
    "gel1010": "code/output/1010_gel_annotation/nta-fractions_annotated_flattened_color.jpg",
    "spottest": "code/output/1016_spot_test_result/fig_spot_test_normalised.png",
    "mutation": "code/output/1010_resistant_mutant_comparison/fig_mutation_962_mut_4643730.png",
    "phagemap": "code/output/0729_prof_figures/fig_phage_genome_map.png",
    "bactgenomes": "code/output/0729_prof_figures/fig_bacterial_genomes.png",
    "folds": "code/output/0712_phage_rbp_detect/structure/fig_fold_comparison.png",
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, rel in SOURCES.items():
        im = Image.open(ROOT / rel)
        im.thumbnail((1600, 1600), Image.LANCZOS)
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
        im.save(OUT / f"{name}.png")
        print(f"{name:14s} {im.size[0]:4d}x{im.size[1]}")
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
