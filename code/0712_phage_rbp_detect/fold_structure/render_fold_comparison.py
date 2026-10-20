#!/usr/bin/env python3
"""Side-by-side renders of the folds behind beta_helix_analysis.tsv.

The point of the figure is to show what the rung period is measuring. The
classifier calls four different verdicts across eight structures, and the
shapes are obviously different once you put them next to each other: a long
prism with a sustained ~23-residue H-bond period, a thin coiled-coil rod at
period 6, and a TIM barrel at period 34, which is the classifier saying "not a
solenoid" rather than "mostly helix".

Everything is coloured by pLDDT, ColabFold's own confidence, on AlphaFold's
scale. That is deliberate: it exposes that the CDS_0011 monomer model is the
weak one at 64.7, next to CDS_0012 at 92.5.

Numbering: the panels carry the PI's CDS numbers, which are the canonical ones
(see code/0713_espinoza_structural_mapping/cds_lookup.tsv). Our own numbering
from the 0708 annotation is printed underneath in grey, because the PDB files
on disk are named with it. Our CDS_0015 and CDS_0016 are two halves of the PI's
CDS_0011, so that protein has two rows in the TSV and two panels here.

Input  : code/output/0712_phage_rbp_detect/structure/pdb/*_unrelaxed_rank_001_*.pdb
         code/output/0712_phage_rbp_detect/structure/beta_helix_analysis.tsv
Output : code/output/0712_phage_rbp_detect/structure/panels/*.png
         code/output/0712_phage_rbp_detect/structure/fig_fold_comparison.{png,svg}

Run with PyMOL's python, the same way render_constructs.py is run.
"""
from __future__ import annotations

import csv
import glob
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from PIL import Image, ImageChops
from pymol import cmd

ROOT = Path(__file__).resolve().parents[3]
STRUCT = ROOT / "code/output/0712_phage_rbp_detect/structure"
PDBDIR = STRUCT / "pdb"
PANELS = STRUCT / "panels"

RAY = (1500, 1250)

# pLDDT bands, AlphaFold's own scale. Same hex values as
# code/1018_construct_structures/render_constructs.py so the two figures read
# as one system.
C = {
    "plddt_vhigh": "#0053d6",
    "plddt_high": "#65cbf3",
    "plddt_low": "#ffdb13",
    "plddt_vlow": "#ff7d45",
}

# our CDS id (how the PDB is named) -> PI CDS id, and the Pharokka annotation
# the PI's table carries. Verified against cds_lookup.tsv on 2026-10-20.
MAP = {
    "CDS_0002": ("CDS_0024", "hypothetical protein"),
    "CDS_0016": ("CDS_0011 fragment", "tail spike protein"),
    "CDS_0015": ("CDS_0011 fragment", "tail spike protein"),
    "CDS_0014": ("CDS_0012", "hypothetical protein"),
    "CDS_0017": ("CDS_0010", "tail protein"),
    "CDS_0018": ("CDS_0009", "tail fiber protein"),
    "CDS_0019": ("CDS_0008", "internal virion protein"),
    "CDS_0020": ("CDS_0007", "virion structural protein"),
}

# Reading order: the three folds the period is meant to separate first, then the
# rest. Both halves of the PI's CDS_0011 are shown, side by side, because they
# are two separate models of one protein and they do not agree on confidence --
# 93.2 against 64.7. Hiding the weak one would be the dishonest version of this
# figure, and it is also where the table's "16-17" comes from.
FIGURE_ORDER = ["CDS_0002", "CDS_0016", "CDS_0015", "CDS_0014",
                "CDS_0020", "CDS_0017", "CDS_0018", "CDS_0019"]

VERDICT_LABEL = {
    "beta-helix": "β-helix",
    "alpha-rich": "α-rich",
    "beta-other": "β-other",
    "alpha-fiber": "α-fiber",
}


def _hex2rgb(h: str) -> list[float]:
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def setup() -> None:
    cmd.reinitialize()
    cmd.bg_color("white")
    cmd.set("ray_opaque_background", 1)
    cmd.set("antialias", 2)
    cmd.set("ray_shadows", 0)
    cmd.set("specular", 0.15)
    cmd.set("cartoon_sampling", 10)
    for key, hexval in C.items():
        cmd.set_color(f"pg_{key}", _hex2rgb(hexval))


def _crop_white(path: Path, pad: int = 24) -> None:
    im = Image.open(path).convert("RGB")
    bbox = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).getbbox()
    if not bbox:
        return
    l, t, r, b = bbox
    im.crop((max(0, l - pad), max(0, t - pad),
             min(im.width, r + pad), min(im.height, b + pad))).save(path)


def snap(name: str) -> Path:
    PANELS.mkdir(parents=True, exist_ok=True)
    p = PANELS / f"{name}.png"
    cmd.ray(*RAY)
    cmd.png(str(p), dpi=300)
    _crop_white(p)
    return p


def color_by_plddt(obj: str) -> None:
    """ColabFold writes pLDDT into the B-factor column, 0-100."""
    cmd.color("pg_plddt_vlow", f"{obj} and b < 50")
    cmd.color("pg_plddt_low", f"{obj} and b > 50 and b < 70")
    cmd.color("pg_plddt_high", f"{obj} and b > 70 and b < 90")
    cmd.color("pg_plddt_vhigh", f"{obj} and b > 90")


def read_analysis() -> dict[str, dict[str, str]]:
    """monomer rows of beta_helix_analysis.tsv, keyed by our CDS id."""
    rows: dict[str, dict[str, str]] = {}
    with open(STRUCT / "beta_helix_analysis.tsv", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            name = row["structure"]
            if not name.endswith("__monomer"):
                continue
            rows[name.split("__")[0]] = row
    return rows


def find_pdb(our_cds: str) -> Path | None:
    hits = sorted(glob.glob(str(PDBDIR / f"*{our_cds}__monomer_unrelaxed_rank_001*.pdb")))
    return Path(hits[0]) if hits else None


def panel(our_cds: str) -> Path | None:
    pdb = find_pdb(our_cds)
    if pdb is None:
        print(f"[skip] no monomer PDB for {our_cds}")
        return None
    setup()
    cmd.load(pdb, our_cds)
    cmd.hide("everything")
    cmd.show("cartoon", our_cds)
    color_by_plddt(our_cds)
    cmd.orient(our_cds)
    # Solenoids and fibres read far better along their long axis than in
    # PyMOL's default orientation, which puts the prism end-on.
    cmd.turn("z", 90)
    cmd.zoom(our_cds, 3)
    return snap(our_cds)


def assemble(paths: dict[str, Path], rows: dict[str, dict[str, str]]) -> None:
    keys = [k for k in FIGURE_ORDER if k in paths]
    if not keys:
        print("[skip] nothing rendered, no figure written")
        return

    ncol = 4
    nrow = -(-len(keys) // ncol)
    fig = plt.figure(figsize=(4.1 * ncol, 5.6 * nrow))
    grid = fig.add_gridspec(nrow * 2, ncol, height_ratios=[1.0, 0.34] * nrow,
                            hspace=0.10, wspace=0.05)

    for i, key in enumerate(keys):
        row_i, col = divmod(i, ncol)
        r = rows.get(key, {})
        pi_id, annot = MAP[key]
        verdict = VERDICT_LABEL.get(r.get("verdict", ""), r.get("verdict", "?"))

        ax = fig.add_subplot(grid[row_i * 2, col])
        ax.imshow(mpimg.imread(paths[key]))
        ax.set_title(f"{chr(65 + i)}  {pi_id} — {verdict}",
                     fontsize=11, fontweight="bold", loc="left", pad=8)
        ax.axis("off")

        cap = fig.add_subplot(grid[row_i * 2 + 1, col])
        cap.axis("off")
        sub = (f"Pharokka: {annot}\n"
               f"rung period {r.get('period', '?')} · pLDDT {r.get('plddt', '?')}\n"
               f"{r.get('n', '?')} aa · β {r.get('beta', '?')} / helix {r.get('helix', '?')}\n"
               f"(our {key})")
        cap.text(0, 1, sub, fontsize=8.5, color="#2d3436", va="top", ha="left",
                 linespacing=1.45, transform=cap.transAxes)

    key_items = [
        Patch(facecolor=C["plddt_vhigh"], label="pLDDT > 90"),
        Patch(facecolor=C["plddt_high"], label="pLDDT 70–90"),
        Patch(facecolor=C["plddt_low"], label="pLDDT 50–70"),
        Patch(facecolor=C["plddt_vlow"], label="pLDDT < 50"),
    ]
    fig.legend(handles=key_items, loc="lower center", ncol=4, frameon=False, fontsize=9)
    fig.suptitle("What the rung period measures — eight Φ8 structures, four verdicts, "
                 "no structure database",
                 fontsize=14, fontweight="bold")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.07)
    for ext in ("png", "svg"):
        fig.savefig(STRUCT / f"fig_fold_comparison.{ext}", dpi=220)
    plt.close(fig)
    print(f"[ok] {STRUCT / 'fig_fold_comparison.png'}")


def main() -> None:
    rows = read_analysis()
    paths: dict[str, Path] = {}
    for our_cds in MAP:
        p = panel(our_cds)
        if p:
            paths[our_cds] = p
            print(f"[ok] {p}")
    assemble(paths, rows)


if __name__ == "__main__":
    main()
