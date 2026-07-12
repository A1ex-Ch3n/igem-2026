"""
Figure for the mini-report "Why protein-protein binding simulation does not work?":
positive vs negative control ipTM for the two binding-screen experiments —
neither separates real binders from scrambled/mismatched negatives.

Data (exact, from the source files):
  ESMFold (2026-07-05, MSA-free): code/output/0703_phage_host_matrix/fold/control_scores.csv
  ColabFold (2026-07-12/13, real MSA): per-class min/mean/max from collect_binding.py (control mode)
Run: python3 documents/fig_binding_controls.py  ->  2026-07-13_binding_controls_comparison.png
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# --- ESMFold (MSA-free): exact per-pair ipTM ---
esm = {
    "positive":  [0.1369, 0.1124, 0.1590],
    "scrambled": [0.1362, 0.1023, 0.1288],
    "mismatch":  [0.1286, 0.1287, 0.1124],
}
# --- ColabFold (real MSA): per-class min / mean / max (n=3 each) ---
cf = {
    "positive":  (0.130, 0.243, 0.310),
    "scrambled": (0.150, 0.173, 0.210),
    "mismatch":  (0.210, 0.320, 0.500),
}

classes = ["positive", "scrambled", "mismatch"]
col = {"positive": "#2a9d5c", "scrambled": "#d9791f", "mismatch": "#c1443c"}
xpos = {c: i for i, c in enumerate(classes)}

fig, ax = plt.subplots(1, 2, figsize=(10, 4.3), sharey=True)

# Panel A — ESMFold (exact dots + mean bar)
for c in classes:
    v = esm[c]; x = xpos[c]
    ax[0].scatter(np.full(len(v), x) + np.random.default_rng(0).uniform(-.06, .06, len(v)),
                  v, s=55, color=col[c], zorder=3, edgecolor="white", linewidth=.6)
    ax[0].hlines(np.mean(v), x - .22, x + .22, color=col[c], lw=2.5, zorder=2)
pmax = max(esm["positive"]); nmin = min(esm["scrambled"] + esm["mismatch"])
ax[0].axhspan(min(pmax, nmin), max(pmax, nmin), color="grey", alpha=.12, zorder=0)
ax[0].set_title("ESMFold — MSA-free (2026-07-05)\nreal 0.137 vs scrambled 0.136  (gap +0.014)", fontsize=10)

# Panel B — ColabFold (mean marker + min-max range)
for c in classes:
    lo, mean, hi = cf[c]; x = xpos[c]
    ax[1].vlines(x, lo, hi, color=col[c], lw=2, zorder=2)
    ax[1].scatter([x, x], [lo, hi], s=30, color=col[c], zorder=3)
    ax[1].scatter([x], [mean], s=90, color=col[c], marker="D", zorder=4,
                  edgecolor="white", linewidth=.8)
pmax = cf["positive"][2]; nmax = cf["mismatch"][2]; pmin = cf["positive"][0]
ax[1].axhspan(pmin, pmax, color="grey", alpha=.12, zorder=0)
ax[1].set_title("ColabFold AF2 — real MSA (2026-07-12/13)\npositives ≤0.31  vs  a mismatch 0.50  (gap −0.37, OVERLAP)", fontsize=10)

for a in ax:
    a.set_xticks(range(len(classes)))
    a.set_xticklabels(["positive\n(known binders)", "scrambled", "mismatch"], fontsize=9)
    a.set_ylim(0, 0.62)
    a.axhline(0.5, ls=":", color="k", lw=.8, alpha=.5)
    a.grid(axis="y", ls=":", alpha=.4)
ax[0].set_ylabel("interface ipTM  (0–1)")
ax[0].text(-0.35, 0.52, "real binders typically 0.5–0.9  ▲", fontsize=8, color="k", alpha=.6, va="bottom", ha="left")
fig.suptitle("Positive controls do NOT separate from negatives — in either run", fontsize=12, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.96])
out = os.path.join(HERE, "2026-07-13_binding_controls_comparison.png")
fig.savefig(out, dpi=150)
print("wrote", out)
