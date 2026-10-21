#!/usr/bin/env python3
"""Redraw the PI's ZymCTRL perplexity panel from the scores he sent.

He has the figure only as a raster and its x-axis labels overlap, so this
rebuilds it from `perp.csv` (998 reconstructed nodes x 24 glycoside-hydrolase EC
classes, 2026-10-20) as a vector figure with readable labels.

Two changes from his version, both to make the result legible rather than to
change it:

* EC classes are ordered by median perplexity instead of by his column order, so
  the two classes this protein family actually fits sit at the left.
* A second panel draws the CDS_0012 -> root path on its own, because the
  monotonic fall is the claim being made and it is invisible inside the cloud.

Perplexity is ZymCTRL's, lower = the sequence looks more like what the model
would write under that EC label.

Input  : documents/2026-10-20_prof_zymctrl/perp.csv  (from Prof. Espinoza, 2026-10-20)
Output : code/output/1020_zymctrl_figure/fig_zymctrl_perplexity.{png,svg}
"""
from __future__ import annotations

import csv
import statistics as st
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "documents/2026-10-20_prof_zymctrl/perp.csv"
OUT = ROOT / "code/output/1020_zymctrl_figure"

# the CDS_0012 -> root path, most recent first (the PI's labels are arbitrary
# identifiers, not depths)
PATH = [1, 2, 38, 39, 40, 42, 267, 277, 281]

CLOUD = "#f6c6c6"
HI = "#c0392b"


def load() -> tuple[list[str], dict[str, dict[str, float]]]:
    rows = list(csv.DictReader(open(CSV)))
    ecs = [k for k in rows[0] if k != "name"]
    data = {r["name"]: {e: float(r[e]) for e in ecs} for r in rows}
    return ecs, data


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ecs, data = load()
    order = sorted(ecs, key=lambda e: st.median(v[e] for v in data.values()))
    path_names = [f"Node{n}" for n in PATH]
    shades = plt.cm.Reds(np.linspace(0.35, 0.95, len(PATH)))

    fig = plt.figure(figsize=(14, 8.4))
    grid = fig.add_gridspec(2, 1, height_ratios=[1.75, 1.0], hspace=0.42)

    # ---- all nodes, per EC ------------------------------------------------ #
    ax = fig.add_subplot(grid[0])
    rng = np.random.default_rng(0)
    for i, ec in enumerate(order):
        ys = [v[ec] for v in data.values()]
        ax.scatter(rng.normal(i, 0.11, len(ys)), ys, s=4, c=CLOUD,
                   alpha=0.55, linewidths=0, zorder=1)
        for j, nm in enumerate(path_names):
            ax.scatter(i, data[nm][ec], s=46, color=shades[j],
                       edgecolor="#7b241c", linewidth=0.5, zorder=3)
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels([f"3.2.1.{e[2:]}" for e in order], rotation=45,
                       ha="right", fontsize=9)
    ax.set_ylabel("ZymCTRL perplexity\n(lower = more canonical for that EC)", fontsize=10)
    # Counted from the table rather than written in, so the title cannot drift
    # from the file the way the first version did (it said 997 for 998 rows).
    ax.set_title(f"A   All {len(data)} reconstructed nodes scored against "
                 f"{len(ecs)} glycoside-hydrolase EC classes",
                 fontsize=12, fontweight="bold", loc="left")
    ax.grid(axis="y", alpha=0.25, linewidth=0.6)
    ax.set_axisbelow(True)
    best = order[0]
    ax.annotate(f"3.2.1.{best[2:]} = endoglucanase,\nthe activity the GH5 templates predict",
                xy=(0, st.median(v[best] for v in data.values())),
                xytext=(4.6, 10.6), fontsize=9, color="#7b241c",
                arrowprops=dict(arrowstyle="->", color="#7b241c", lw=1))

    # ---- the path alone --------------------------------------------------- #
    ax2 = fig.add_subplot(grid[1])
    for ec, style, lab in ((order[0], "-o", f"3.2.1.{order[0][2:]}"),
                           (order[1], "-s", f"3.2.1.{order[1][2:]}")):
        ax2.plot(range(len(PATH)), [data[n][ec] for n in path_names], style,
                 color=HI if ec == order[0] else "#e8956f", label=lab, lw=1.6, ms=6)
    med_other = [st.median(data[n][e] for e in order[2:]) for n in path_names]
    ax2.plot(range(len(PATH)), med_other, "--^", color="#95a5a6", lw=1.4, ms=5,
             label="median of the other 22 classes")
    ax2.set_xticks(range(len(PATH)))
    ax2.set_xticklabels([f"Node{n}" for n in PATH], fontsize=9)
    ax2.set_xlabel("CDS_0012  →  root   (left = most recent, right = most ancestral)", fontsize=10)
    ax2.set_ylabel("perplexity", fontsize=10)
    ax2.set_title("B   The same nine nodes on their own: the fall is ~4.7 units in the "
                  "best-fitting class and <1 unit elsewhere",
                  fontsize=12, fontweight="bold", loc="left")
    ax2.grid(axis="y", alpha=0.25, linewidth=0.6)
    ax2.set_axisbelow(True)
    ax2.legend(frameon=False, fontsize=9, loc="center right")

    fig.subplots_adjust(left=0.085, right=0.985, top=0.93, bottom=0.09)
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig_zymctrl_perplexity.{ext}", dpi=200)
    plt.close(fig)
    print(f"[ok] {OUT / 'fig_zymctrl_perplexity.png'}")

    # ---- the numbers the caption quotes ----------------------------------- #
    print("\nmedian perplexity per EC (lowest 4):")
    for e in order[:4]:
        print(f"  3.2.1.{e[2:]:5} {st.median(v[e] for v in data.values()):.3f}")
    print(f"  ... worst: 3.2.1.{order[-1][2:]} "
          f"{st.median(v[order[-1]] for v in data.values()):.3f}")
    d = data["Node1"][order[0]] - data["Node281"][order[0]]
    print(f"\nNode1 -> Node281 under 3.2.1.{order[0][2:]}: "
          f"{data['Node1'][order[0]]:.2f} -> {data['Node281'][order[0]]:.2f}  (drop {d:.2f})")


if __name__ == "__main__":
    main()
