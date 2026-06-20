#!/usr/bin/env python3
"""
M3 — per-strain ipTM heatmap (local, no GPU).

Reads the pairs manifest + a binding_matrix.csv of Tier-1 results and renders one
heatmap per strain (x = phage RBP, y = receptor, colour = ipTM).

binding_matrix.csv columns: strain, phage_id, receptor_id, iptm   (iPAE optional)

If no results file is given (or it's missing), generates a PLACEHOLDER with random
ipTM so the deliverable format is ready before Tier-1 has run. Swap in the real
binding_matrix.csv later and rerun — nothing else changes.

Usage:
  python3 make_heatmap.py                       # placeholder
  python3 make_heatmap.py binding_matrix.csv    # real results
"""
import sys, csv, math, random
from pathlib import Path
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest/pairs_36x60.csv"
OUTDIR = ROOT / "output"
DATE = "2026-06-16"

def load_manifest():
    by_strain = defaultdict(lambda: {"phages": [], "receptors": []})
    seen = defaultdict(lambda: (set(), set()))
    rows = []
    for r in csv.DictReader(open(MANIFEST)):
        rows.append(r)
    order = {}
    for r in rows:
        s = r["strain"]
        order.setdefault(s, {"p": [], "r": []})
        if r["phage_id"] not in order[s]["p"]:
            order[s]["p"].append(r["phage_id"])
        if r["receptor_id"] not in order[s]["r"]:
            order[s]["r"].append(r["receptor_id"])
    return order

def load_scores(path):
    if not path or not Path(path).exists():
        return None
    sc = {}
    for r in csv.DictReader(open(path)):
        try:
            sc[(r["strain"], r["phage_id"], r["receptor_id"])] = float(r["iptm"])
        except (KeyError, ValueError):
            pass
    return sc

def main():
    OUTDIR.mkdir(exist_ok=True)
    scores_path = sys.argv[1] if len(sys.argv) > 1 else None
    scores = load_scores(scores_path)
    placeholder = scores is None
    if placeholder:
        random.seed(42)
        print("No results file -> PLACEHOLDER heatmaps (random ipTM).")

    order = load_manifest()
    for strain, d in order.items():
        phages, receptors = d["p"], d["r"]
        M = np.full((len(receptors), len(phages)), np.nan)
        for i, rec in enumerate(receptors):
            for j, ph in enumerate(phages):
                if placeholder:
                    M[i, j] = round(random.betavariate(2, 6), 3)  # skewed low, like real ipTM
                else:
                    v = scores.get((strain, ph, rec))
                    if v is not None:
                        M[i, j] = v

        h = max(6, len(receptors) * 0.18)
        w = max(8, len(phages) * 0.30)
        fig, ax = plt.subplots(figsize=(w, h))
        im = ax.imshow(M, aspect="auto", cmap="viridis", vmin=0, vmax=1)
        ax.set_xticks(range(len(phages))); ax.set_xticklabels(phages, rotation=90, fontsize=5)
        ax.set_yticks(range(len(receptors))); ax.set_yticklabels(receptors, fontsize=4)
        ax.set_xlabel("phage RBP"); ax.set_ylabel("receptor (locus)")
        title = f"{strain} — RBP × receptor ipTM"
        if placeholder:
            title += "   [PLACEHOLDER: random data, replace with Tier-1 results]"
        ax.set_title(title, fontsize=9)
        cb = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.01); cb.set_label("ipTM")
        fig.tight_layout()
        out = OUTDIR / f"{DATE}_{strain}_iptm-heatmap.png"
        fig.savefig(out, dpi=150); plt.close(fig)
        print(f"  {strain}: {len(receptors)}x{len(phages)} -> {out.name}")

if __name__ == "__main__":
    main()
