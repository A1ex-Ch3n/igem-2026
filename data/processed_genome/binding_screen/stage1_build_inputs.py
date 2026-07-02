#!/usr/bin/env python3
"""
Stage 1 — finalize binding-screen inputs (local, no GPU).

Scope (decided 2026-06-16):
  Phage probes : 36 dereplicated Pseudomonas-phage RBPs (pseudomonas_phage_RBP_probes_strict.fasta)
  Receptors    : per-strain surface phage-receptor PANEL (~60) — TonB-dependent receptors,
                 porins, type IV pili/fimbriae, flagellin, autotransporters
  Matrix       : per strain, probe x receptor

Outputs (under binding_screen/):
  phage_probes/probes.fasta        clean-ID probe sequences for ColabFold job names
  phage_probes/probe_map.tsv       clean_id, accession, source_phage, length, product
  receptors_panel/<strain>_receptors.fasta
  manifest/pairs_36x60.csv         strain, phage_id, receptor_id, receptor_product
"""
import re, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent

STRAINS = {
    "10-10-2": "10-10-2_potential_receptors.fasta",
    "9-2-1":   "9-2-1_potential_receptors.fasta",
    "9-6-2":   "9-6-2_potential_receptors.fasta",
}
PROBE_SRC = ROOT / "pseudomonas_phage_RBP_probes_strict.fasta"

# ---- receptor panel: keep genuine surface phage receptors ----
PANEL = re.compile(
    r"TonB-dependent|siderophore|ferrichrome|ferri|Fpv|Fpt|Fox[A-Z]|Fiu|Fhu[A-Z]|Fep[A-Z]|Btu[A-Z]|"
    r"porin|Opr[A-Z]|Omp[A-Z]|pilus|pil[AQ]\b|fimbri|type IV|flagell|FliC|FliD|"
    r"autotransporter|adhesin|hemagglutinin",
    re.I,
)
EXCLUDE = re.compile(
    r"assembly factor|Bam[ABCDE]\b|LptD|LolB|insertase|"
    r"efflux|membrane fusion|\bMFP\b|TolC|RND|HlyD|"
    r"Energy transducer TonB|ExbB|ExbD|TolQ|TolR|MotA|"
    r"permease|ABC transporter|biosynthesis",
    re.I,
)

def read_fasta(path):
    out, name, seq = [], None, []
    for line in open(path):
        if line.startswith(">"):
            if name: out.append((name, "".join(seq)))
            name = line[1:].rstrip("\n"); seq = []
        else:
            seq.append(line.strip())
    if name: out.append((name, "".join(seq)))
    return out

def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")

def main():
    (ROOT / "phage_probes").mkdir(exist_ok=True)
    (ROOT / "receptors_panel").mkdir(exist_ok=True)
    (ROOT / "manifest").mkdir(exist_ok=True)

    # ---- probes: clean IDs ----
    probes = []  # (clean_id, seq, acc, phage, product)
    for h, s in read_fasta(PROBE_SRC):
        acc = h.split(":")[0].split()[0]
        m = re.search(r"organism=([^\]]+)", h)
        phage = m.group(1).replace("Pseudomonas phage", "").strip() if m else "phage"
        product = re.sub(r"\[organism=.*?\]", "", h.split(" ", 1)[1] if " " in h else "").strip()
        cid = f"{slug(phage)}_{slug(acc)}"
        probes.append((cid, s, acc, phage, product))
    with open(ROOT / "phage_probes/probes.fasta", "w") as fh:
        for cid, s, *_ in probes:
            fh.write(f">{cid}\n{s}\n")
    with open(ROOT / "phage_probes/probe_map.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["clean_id", "accession", "source_phage", "length", "product"])
        for cid, s, acc, phage, product in probes:
            w.writerow([cid, acc, phage, len(s), product])
    print(f"probes: {len(probes)} (-> phage_probes/probes.fasta)")

    # ---- receptors: per-strain panel ----
    panel = {}
    for strain, fa in STRAINS.items():
        kept = [(h, s) for h, s in read_fasta(DATA / fa)
                if PANEL.search(h) and not EXCLUDE.search(h)]
        panel[strain] = kept
        with open(ROOT / f"receptors_panel/{strain}_receptors.fasta", "w") as fh:
            for h, s in kept:
                fh.write(f">{h}\n{s}\n")
        print(f"  {strain}: {len(kept)} receptors")

    # ---- manifest ----
    n = 0
    with open(ROOT / "manifest/pairs_36x60.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["strain", "phage_id", "receptor_id", "receptor_product"])
        for strain in STRAINS:
            for cid, *_ in probes:
                for h, _ in panel[strain]:
                    locus = h.split()[0]
                    product = " ".join(h.split()[1:])
                    w.writerow([strain, cid, locus, product]); n += 1
    print(f"manifest: {n:,} pairs (-> manifest/pairs_36x60.csv)")

if __name__ == "__main__":
    main()
