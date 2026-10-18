#!/usr/bin/env python3
"""3D renders of the six expressed constructs, for the iGEM Parts pages.

Two structure sources, kept visibly separate because they are not equivalent
evidence:
  * AlphaFold3 Server (Prof. Espinoza, 2026-07-14/15) for the three wild-type
    parents CDS_0010 / CDS_0011 (trimer) / CDS_0012 -- real MSA + templates.
    data/phage_genome/9-2-1/folds_espinoza/ (gitignored bulk data)
  * ESMFold v1, run locally by code/1018_construct_structures/fold_ancestors.py,
    for the three CDS_0012 ancestral reconstructions, which have no AF3 job.
    A single-sequence language-model fold -- weaker evidence, so the ancestral
    panels are coloured by pLDDT rather than by domain.

The AF3 jobs are the FULL-LENGTH proteins; the constructs that went to Twist are
truncations, so each wild-type panel greys out what is not in the plasmid.

Outputs -> code/output/1018_construct_structures/
    panels/*.png                 individual renders
    fig_constructs_overview.{png,svg}   6-panel figure, one per construct
    fig_cds12_family.{png,svg}          WT vs the three ancestors + overlay
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
OUT = ROOT / "code/output/1018_construct_structures"
ESM = OUT / "esmfold"
PANELS = OUT / "panels"

RAY = (1500, 1250)

# domain boundaries, parent-protein numbering (code/0716_espinoza_fiber_construct/)
CALX = (1, 110)          # Calx-beta Ca2+-binding sandwich, shared by CDS_0010/0011
SHAFT = (111, 300)       # unplaced across AF3 models
BODY = (301, 941)        # trimeric beta-helix depolymerase body
FOLDON = (921, 941)
GH5_CBM = (1, 117)
GH5_BARREL = (118, 475)

# what is actually in each plasmid, parent numbering
CONSTRUCT_RANGE = {"CDS10_WT": (105, 917), "CDS11_WT": (305, 941), "CDS12_WT": (117, 477)}

C = {
    "calx": "#2980b9",
    "shaft": "#b2bec3",
    "body": "#16a085",
    "foldon": "#c0392b",
    "cbm": "#e67e22",
    "barrel": "#8e44ad",
    "unknown": "#34495e",
    "excluded": "#dfe6e9",   # present in the fold, absent from the construct
    "calx_excluded": "#a9cce3",   # Calx-β, but outside the construct
    # pLDDT bands, AlphaFold's own scale
    "plddt_vhigh": "#0053d6",
    "plddt_high": "#65cbf3",
    "plddt_low": "#ffdb13",
    "plddt_vlow": "#ff7d45",
}
ANCESTORS = ["CDS12_ANC_Node1", "CDS12_ANC_Node40", "CDS12_ANC_Node281"]


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


def rng(obj: str, lo: int, hi: int) -> str:
    return f"{obj} and resi {lo}-{hi}"


def color_by_plddt(obj: str) -> None:
    """ESMFold writes pLDDT into the B-factor column, same 0-100 scale as AF."""
    cmd.color("pg_plddt_vlow", f"{obj} and b < 50")
    cmd.color("pg_plddt_low", f"{obj} and b > 50 and b < 70")
    cmd.color("pg_plddt_high", f"{obj} and b > 70 and b < 90")
    cmd.color("pg_plddt_vhigh", f"{obj} and b > 90")


# --------------------------------------------------------------------------- #
# wild-type panels, from the AF3 folds
# --------------------------------------------------------------------------- #
def panel_cds10() -> Path:
    setup()
    cmd.load(FOLDS / "fold_cds_0010/fold_cds_0010_model_0.cif", "m10")
    cmd.hide("everything")
    cmd.show("cartoon", "m10")
    cmd.color("pg_excluded", "m10")
    lo, hi = CONSTRUCT_RANGE["CDS10_WT"]
    cmd.color("pg_unknown", rng("m10", lo, hi))
    # the Calx-β anchor is almost entirely upstream of the construct start (res 105)
    cmd.color("pg_calx_excluded", rng("m10", CALX[0], lo - 1))
    cmd.color("pg_calx", rng("m10", lo, CALX[1]))
    cmd.orient("m10")
    cmd.zoom("m10", 3)
    return snap("CDS10_WT")


def panel_cds11() -> Path:
    setup()
    cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "t11")
    cmd.hide("everything")
    cmd.show("cartoon", "t11")
    cmd.color("pg_excluded", "t11")
    cmd.color("pg_body", rng("t11", *BODY))
    cmd.color("pg_foldon", rng("t11", *FOLDON))
    cmd.color("pg_calx", rng("t11", *CALX))
    cmd.orient("t11")
    cmd.turn("z", 90)
    cmd.zoom("t11", 3)
    return snap("CDS11_WT")


def panel_cds12() -> Path:
    setup()
    cmd.load(FOLDS / "fold_cds_0012/fold_cds_0012_model_0.cif", "m12")
    cmd.hide("everything")
    cmd.show("cartoon", "m12")
    cmd.color("pg_excluded", "m12")
    cmd.color("pg_barrel", rng("m12", *GH5_BARREL))
    cmd.color("pg_cbm", rng("m12", GH5_CBM[0] + 116, GH5_CBM[1]))  # 117 only
    cmd.orient("m12")
    cmd.zoom("m12", 3)
    return snap("CDS12_WT")


# --------------------------------------------------------------------------- #
# ancestral panels, from the local ESMFold models
# --------------------------------------------------------------------------- #
def panel_ancestor(name: str) -> Path | None:
    pdb = ESM / f"{name}.pdb"
    if not pdb.exists():
        print(f"[skip] {pdb} missing -- run fold_ancestors.py first")
        return None
    setup()
    cmd.load(pdb, name)
    cmd.hide("everything")
    cmd.show("cartoon", name)
    color_by_plddt(name)
    cmd.orient(name)
    cmd.zoom(name, 3)
    return snap(name)


def panel_overlay() -> Path | None:
    """All four CDS_0012-family ESMFold models superposed on the WT."""
    have = [n for n in ["CDS12_WT", *ANCESTORS] if (ESM / f"{n}.pdb").exists()]
    if len(have) < 2:
        print("[skip] overlay needs the ESMFold CDS12_WT model as reference")
        return None
    setup()
    shades = {"CDS12_WT": "#2d3436", "CDS12_ANC_Node1": "#e17055",
              "CDS12_ANC_Node40": "#00b894", "CDS12_ANC_Node281": "#0984e3"}
    for n in have:
        cmd.set_color(f"ov_{n}", _hex2rgb(shades[n]))
        cmd.load(ESM / f"{n}.pdb", n)
        cmd.hide("everything", n)
        cmd.show("cartoon", n)
        cmd.color(f"ov_{n}", n)
        if n != "CDS12_WT":
            cmd.align(n, "CDS12_WT")
    cmd.set("cartoon_transparency", 0.35, "CDS12_WT")
    cmd.orient("CDS12_WT")
    cmd.zoom("CDS12_WT", 3)
    return snap("cds12_family_overlay")


# --------------------------------------------------------------------------- #
def assemble_overview(paths: dict[str, Path]) -> None:
    spec = [
        ("CDS10_WT",
         "A  CDS10_WT — unknown-function fiber (91.6 kDa)",
         "AF3, full-length CDS_0010. Construct = res 105–917 (dark);\n"
         "Calx-β anchor 1–110 in blue is partly outside the plasmid.\n"
         "No enzymatic template support — deliberately not called a glycosidase."),
        ("CDS11_WT",
         "B  CDS11_WT — tail-spike depolymerase (72.0 kDa)",
         "AF3 trimer of full-length CDS_0011. Construct = res 305–941:\n"
         "the β-helix body (teal) + foldon (red). Calx-β (blue) and shaft\n"
         "are pale = removed from the construct."),
        ("CDS12_WT",
         "C  CDS12_WT — GH5 glycoside hydrolase (41.8 kDa)",
         "AF3, full-length CDS_0012. Construct = res 117–477, essentially\n"
         "the whole GH5 TIM barrel (purple, pLDDT 95–98).\n"
         "4/4 AF3 templates are GH5 endoglucanases (1ECE, 1VRX, 4TUF, 2ZUM)."),
        ("CDS12_ANC_Node1",
         "D  CDS12_ANC_Node1 — reconstructed ancestor (41.9 kDa)",
         "ESMFold v1, single sequence, coloured by pLDDT.\n"
         "78 % identical to CDS12_WT — the closest of the three."),
        ("CDS12_ANC_Node40",
         "E  CDS12_ANC_Node40 — reconstructed ancestor (42.2 kDa)",
         "ESMFold v1, single sequence, coloured by pLDDT.\n"
         "53 % identical to CDS12_WT, 87 % to Node281."),
        ("CDS12_ANC_Node281",
         "F  CDS12_ANC_Node281 — reconstructed ancestor (42.3 kDa)",
         "ESMFold v1, single sequence, coloured by pLDDT.\n"
         "51 % identical to CDS12_WT, 87 % to Node40."),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(16.5, 11.5))
    for ax, (key, title, sub) in zip(axes.ravel(), spec):
        if key in paths:
            ax.imshow(mpimg.imread(paths[key]))
        else:
            ax.text(0.5, 0.5, "model not available", ha="center", va="center",
                    transform=ax.transAxes, color="#b2bec3")
        ax.set_title(title, fontsize=11.5, fontweight="bold", loc="left", pad=8)
        ax.set_xlabel(sub, fontsize=8.5, color="#2d3436", loc="left")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    key_items = [
        Patch(facecolor=C["calx"], label="Calx-β anchor (res 1–110)"),
        Patch(facecolor=C["body"], label="β-helix depolymerase body"),
        Patch(facecolor=C["foldon"], label="foldon / trimerization tip"),
        Patch(facecolor=C["barrel"], label="GH5 TIM barrel"),
        Patch(facecolor=C["unknown"], label="unknown function"),
        Patch(facecolor=C["excluded"], label="in the fold, NOT in the construct"),
        Patch(facecolor=C["plddt_vhigh"], label="pLDDT > 90"),
        Patch(facecolor=C["plddt_high"], label="pLDDT 70–90"),
        Patch(facecolor=C["plddt_low"], label="pLDDT 50–70"),
        Patch(facecolor=C["plddt_vlow"], label="pLDDT < 50"),
    ]
    fig.legend(handles=key_items, loc="lower center", ncol=5, frameon=False, fontsize=9)
    fig.suptitle("iGEM 2026 Claremont — 3D models of the six expressed parts",
                 fontsize=14, fontweight="bold")
    fig.tight_layout(rect=(0, 0.07, 1, 0.97))
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig_constructs_overview.{ext}", dpi=220)
    plt.close(fig)


def assemble_family(paths: dict[str, Path]) -> None:
    keys = ["CDS12_WT", *ANCESTORS, "cds12_family_overlay"]
    have = [k for k in keys if k in paths]
    if not have:
        return
    fig, axes = plt.subplots(1, len(have), figsize=(4.2 * len(have), 5.2))
    axes = [axes] if len(have) == 1 else list(axes)
    titles = {
        "CDS12_WT": "CDS12_WT (AF3, full-length)",
        "CDS12_ANC_Node1": "ANC_Node1 (ESMFold)",
        "CDS12_ANC_Node40": "ANC_Node40 (ESMFold)",
        "CDS12_ANC_Node281": "ANC_Node281 (ESMFold)",
        "cds12_family_overlay": "all four superposed",
    }
    for ax, k in zip(axes, have):
        ax.imshow(mpimg.imread(paths[k]))
        ax.set_title(titles[k], fontsize=11, fontweight="bold")
        ax.axis("off")
    fig.suptitle("The CDS_0012 GH5 family — wild type and three reconstructed ancestors",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig_cds12_family.{ext}", dpi=220)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    for fn in (panel_cds10, panel_cds11, panel_cds12):
        p = fn()
        paths[p.stem] = p
    for name in ANCESTORS:
        p = panel_ancestor(name)
        if p:
            paths[p.stem] = p
    p = panel_overlay()
    if p:
        paths[p.stem] = p
    assemble_overview(paths)
    assemble_family(paths)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
