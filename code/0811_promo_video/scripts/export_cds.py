#!/usr/bin/env python3
"""
Export the real CDS coordinates of 9-2-1 Φ8 as JSON for the video.

Reads the same Pharokka table the manuscript figures are drawn from
(code/0713_espinoza_structural_mapping/pharokka_espinoza/), via the loader in
code/0729_prof_figures/plot_phage_genome_map.py — so the genome track on screen
is the team's own annotation, not a decorative approximation.

Drawing happens in Remotion (src/components/GenomeTrack.tsx) rather than
matplotlib: the blueprint style needs stroke-only arrows that draw themselves
on, which a raster/vector export cannot animate.

  python scripts/export_cds.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SRC = ROOT / "code/0729_prof_figures"
OUT = HERE.parent / "src/data/cds.json"

sys.path.insert(0, str(SRC))
import plot_phage_genome_map as m  # noqa: E402

# Only genes the narration or the annotations actually name. Everything else
# is drawn unlabelled — texture that is nonetheless real.
LABEL = {
    "CDS_0009": "tail fiber",
    "CDS_0010": "tail protein",
    "CDS_0011": "TAIL SPIKE",
    "CDS_0012": "glycoside hydrolase",
    "CDS_0017": "major head",
    "CDS_0020": "portal",
    "CDS_0078": "endolysin",
}


def main() -> None:
    df = m.load()
    genes = [
        {
            "cds": r["cds"],
            "s": int(r["s"]),
            "e": int(r["e"]),
            "strand": int(r["strand_i"]),
            "category": r["category"],
            "label": LABEL.get(r["cds"]),
        }
        for _, r in df.iterrows()
    ]

    payload = {
        "genome": "9-2-1 Phi8",
        "length": m.GENOME_LEN,
        "tailZoom": list(m.TAIL_ZOOM),
        "star": m.STAR,
        "source": "Pharokka annotation of the canonical Version_1 assembly",
        "genes": genes,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=1))
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(genes)} CDS, {m.GENOME_LEN} bp)")


if __name__ == "__main__":
    main()
