#!/usr/bin/env python3
"""
Q6 -- 3D models of the enzymatic domains associated with the tail spike.

Source: Prof. Espinoza's AlphaFold3 Server folds (2026-07-14/15), model_0 of each
job, in data/phage_genome/9-2-1/folds_espinoza/ (gitignored bulk data).

A note on scope, because the PI's wording is ambiguous.  He asked for "the
enzymatic domains *within* the tail spike protein", but the confirmed glycoside
hydrolase (GH5) is CDS_0012 -- a SEPARATE protein, not a domain of CDS_0011.
So this renders both, labelled for what they actually are:
  * CDS_0011 res 301-941  -- the beta-helix depolymerase body, genuinely inside
    the tail spike.  Fold called by H-bond rung period, no named homolog yet.
  * CDS_0012 res 118-475  -- the GH5 TIM barrel, template-confirmed (1ECE with
    cellotetraose bound, 1VRX, 4TUF, 2ZUM), but its own protein.
CDS_0010 is deliberately NOT drawn as an enzyme: its glycosidase assignment is
unsupported (one weak IspD hit; ~460 aa with no template).

PyMOL renders the panels; matplotlib assembles them with a colour key.

Outputs -> code/output/0729_prof_figures/
    fig_enzymatic_domains.{png,svg}   assembled 4-panel figure
    panels/*.png                      individual PyMOL renders
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from PIL import Image, ImageChops
from pymol import cmd

ROOT = Path(__file__).resolve().parents[2]
FOLDS = ROOT / "data/phage_genome/9-2-1/folds_espinoza"
OUT = ROOT / "code/output/0729_prof_figures"
PANELS = OUT / "panels"

# domain boundaries from code/0716_espinoza_fiber_construct/
CALX = (1, 110)        # Calx-beta Ca2+-binding beta-sandwich; capsid-base anchor
SHAFT = (111, 300)     # unplaced across AF3 models (RMSD 41-52 A)
BODY = (301, 941)      # rigid trimeric beta-helix depolymerase + RBD
FOLDON = (921, 941)    # helical, heavy trimer contacts -> keep intact
CONSTRUCT = 305        # what actually went to Twist: res 305-941

GH5_CBM = (1, 117)     # no template
GH5_BARREL = (118, 475)  # 4/4 AF3 templates are GH5 endoglucanases

C = {
    "calx": "#2980b9",
    "shaft": "#b2bec3",
    "body": "#16a085",
    "foldon": "#c0392b",
    "cbm": "#e67e22",
    "barrel": "#8e44ad",
}

RAY = (1500, 1250)

# extra shades used only for distinguishing the three chains
CHAIN_SHADES = ["#16a085", "#1abc9c", "#7fd4c1"]


def _hex2rgb(h: str) -> list[float]:
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def register_colors() -> None:
    """PyMOL's cmd.color takes named colours, not hex -- register ours."""
    for key, hexval in C.items():
        cmd.set_color(f"pg_{key}", _hex2rgb(hexval))
    for i, hexval in enumerate(CHAIN_SHADES):
        cmd.set_color(f"pg_chain{i}", _hex2rgb(hexval))


def setup() -> None:
    cmd.reinitialize()
    cmd.bg_color("white")
    cmd.set("ray_opaque_background", 1)
    cmd.set("antialias", 2)
    cmd.set("cartoon_transparency", 0.0)
    cmd.set("ray_shadows", 0)
    cmd.set("specular", 0.15)
    cmd.set("cartoon_sampling", 10)
    register_colors()


def snap(name: str) -> Path:
    p = PANELS / f"{name}.png"
    cmd.ray(*RAY)
    cmd.png(str(p), dpi=300)
    _crop_white(p)
    return p


def _crop_white(path: Path, pad: int = 24) -> None:
    """PyMOL centres the molecule in the canvas, leaving wide white margins that
    waste half the panel once these are tiled.  Trim to the ink."""
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bbox = ImageChops.difference(im, bg).getbbox()
    if not bbox:
        return
    l, t, r, b = bbox
    l, t = max(0, l - pad), max(0, t - pad)
    r, b = min(im.width, r + pad), min(im.height, b + pad)
    im.crop((l, t, r, b)).save(path)


def rng(obj: str, lo: int, hi: int) -> str:
    return f"{obj} and resi {lo}-{hi}"


def panel_trimer_domains() -> Path:
    """Whole CDS_0011 trimer, coloured by domain."""
    setup()
    cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "t11")
    cmd.hide("everything")
    cmd.show("cartoon", "t11")
    cmd.color("pg_shaft", "t11")
    cmd.color("pg_calx", rng("t11", *CALX))
    cmd.color("pg_body", rng("t11", *BODY))
    cmd.color("pg_foldon", rng("t11", *FOLDON))
    cmd.orient("t11")
    cmd.turn("z", 90)
    cmd.zoom("t11", 3)
    return snap("cds0011_trimer_domains")


def panel_body_side() -> Path:
    """The depolymerase body alone, side view -- the solenoid."""
    setup()
    cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "t11")
    cmd.create("body", rng("t11", *BODY))
    cmd.delete("t11")
    cmd.hide("everything")
    cmd.show("cartoon", "body")
    for i, ch in enumerate("ABC"):
        cmd.color(f"pg_chain{i}", f"body and chain {ch}")
    cmd.orient("body")
    cmd.turn("z", 90)
    cmd.zoom("body", 2)
    return snap("cds0011_body_side")


def panel_body_axial() -> Path:
    """Down the 3-fold axis -- shows the triangular beta-helix prism."""
    setup()
    cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "t11")
    cmd.create("body", rng("t11", *BODY))
    cmd.delete("t11")
    cmd.hide("everything")
    cmd.show("cartoon", "body")
    for i, ch in enumerate("ABC"):
        cmd.color(f"pg_chain{i}", f"body and chain {ch}")
    cmd.orient("body")
    cmd.turn("y", 90)          # end-on: after orient() the long axis lies on x
    cmd.zoom("body", 2)
    return snap("cds0011_body_axial")


def panel_gh5() -> Path:
    """CDS_0012 -- CBM + GH5 TIM barrel."""
    setup()
    cmd.load(FOLDS / "fold_cds_0012/fold_cds_0012_model_0.cif", "m12")
    cmd.hide("everything")
    cmd.show("cartoon", "m12")
    cmd.color("pg_cbm", rng("m12", *GH5_CBM))
    cmd.color("pg_barrel", rng("m12", *GH5_BARREL))
    cmd.orient("m12")
    cmd.zoom("m12", 3)
    return snap("cds0012_gh5")


def assemble(paths: dict[str, Path]) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12.5, 11.2))
    spec = [
        ("cds0011_trimer_domains",
         "A  CDS_0011 tail spike — full trimer (941 aa × 3)",
         "Calx-β anchor 1–110 · shaft 111–300 (AF3 cannot place it) ·\n"
         "β-helix depolymerase body 301–941 · foldon 921–941"),
        ("cds0011_body_side",
         "B  the enzymatic body alone, res 301–941",
         "right-handed β-helix / β-solenoid — the depolymerase.\n"
         "Rigid across all 5 AF3 models (RMSD 0.44–0.99 Å)"),
        ("cds0011_body_axial",
         "C  same body, down the 3-fold axis",
         "the three chains interdigitate into a triangular prism;\n"
         "res 321–941 carry the trimer contacts"),
        ("cds0012_gh5",
         "D  CDS_0012 — GH5 glycoside hydrolase (a separate protein)",
         "CBM 1–117 · GH5 TIM barrel 118–475, pLDDT 95–98.\n"
         "All 4 AF3 templates are GH5 endoglucanases (1ECE, 1VRX, 4TUF, 2ZUM)"),
    ]
    for ax, (key, title, sub) in zip(axes.ravel(), spec):
        ax.imshow(mpimg.imread(paths[key]))
        ax.axis("off")
        # subtitle sits just above the image; the title is padded clear of it
        ax.set_title(title, fontsize=12, fontweight="bold", loc="left", pad=36)
        ax.text(0, 1.012, sub, transform=ax.transAxes, fontsize=8.8,
                va="bottom", ha="left", color="#555", linespacing=1.4)

    handles = [
        Patch(fc=C["calx"], label="Calx-β anchor (joins capsid base)"),
        Patch(fc=C["shaft"], label="shaft — unplaced by AF3"),
        Patch(fc=C["body"], label="β-helix depolymerase body"),
        Patch(fc=C["foldon"], label="C-term trimerization foldon"),
        Patch(fc=C["cbm"], label="CBM (no template)"),
        Patch(fc=C["barrel"], label="GH5 TIM barrel"),
    ]
    fig.legend(handles=handles, loc="lower center", ncols=3, fontsize=10,
               frameon=False, bbox_to_anchor=(0.5, -0.015))
    fig.suptitle(
        "9-2-1 Φ8 — enzymatic domains of the tail-spike module\n"
        "Prof. Espinoza's AlphaFold3 folds  ·  numbering = UUAIURNK_  ·  "
        f"ordered construct = CDS_0011 res {CONSTRUCT}–941",
        fontsize=14, y=0.995)
    fig.tight_layout(rect=(0, 0.02, 1, 0.955))
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig_enzymatic_domains.{ext}", dpi=200,
                    bbox_inches="tight")
    print(f"wrote fig_enzymatic_domains.png|svg")


def main() -> None:
    PANELS.mkdir(parents=True, exist_ok=True)
    paths = {
        "cds0011_trimer_domains": panel_trimer_domains(),
        "cds0011_body_side": panel_body_side(),
        "cds0011_body_axial": panel_body_axial(),
        "cds0012_gh5": panel_gh5(),
    }
    for k, v in paths.items():
        print(f"  rendered {k} -> {v.name}")
    assemble(paths)


if __name__ == "__main__":
    main()
