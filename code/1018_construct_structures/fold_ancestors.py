#!/usr/bin/env python3
"""Fold the expressed-construct proteins with ESMFold (transformers, local).

Inputs : data/expressed_proteins/*.faa  (mature construct incl. pET-28a leader)
Outputs: code/output/1018_construct_structures/esmfold/<name>.pdb  (+ pLDDT in B-factor)
         and <name>_plddt.json

ESMFold is run on CPU in float32 (MPS lacks some ops used by the folding trunk);
chunk_size is set low to keep peak memory inside a 8 GB laptop.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import torch
from Bio import SeqIO
from transformers import AutoTokenizer, EsmForProteinFolding

ROOT = Path(__file__).resolve().parents[2]
FAA = ROOT / "data/expressed_proteins"
OUT = ROOT / "code/output/1018_construct_structures/esmfold"

# the 21 aa pET-28a leader is disordered and only adds noise to the fold
LEADER = "MGSSHHHHHHSSGLVPRGSHM"


def rescale_bfactors(pdb: str) -> str:
    """transformers writes pLDDT on a 0-1 scale; everything downstream (PyMOL
    colouring, the AF3 comparison) assumes AlphaFold's 0-100 scale."""
    lines = []
    for line in pdb.splitlines():
        if line.startswith(("ATOM", "HETATM")):
            line = f"{line[:60]}{float(line[60:66]) * 100:6.2f}{line[66:]}"
        lines.append(line)
    return "\n".join(lines) + "\n"


def main(names: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    tok = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
    model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", low_cpu_mem_usage=True)
    model.esm = model.esm.float()
    model.eval()
    model.trunk.set_chunk_size(64)

    for name in names:
        rec = next(SeqIO.parse(FAA / f"{name}.faa", "fasta"))
        seq = str(rec.seq)
        seq = seq[len(LEADER):] if seq.startswith(LEADER) else seq
        print(f"[fold] {name} {len(seq)} aa", flush=True)
        with torch.no_grad():
            out = model.infer_pdb(seq)
        out = rescale_bfactors(out)
        (OUT / f"{name}.pdb").write_text(out)
        # out has already been rescaled to AlphaFold's 0-100 pLDDT scale
        plddt = [float(l[60:66]) for l in out.splitlines()
                 if l.startswith("ATOM") and l[12:16].strip() == "CA"]
        (OUT / f"{name}_plddt.json").write_text(json.dumps(
            {"name": name, "length": len(seq), "plddt": plddt,
             "mean_plddt": sum(plddt) / len(plddt)}))
        print(f"[done] {name} mean pLDDT {sum(plddt)/len(plddt):.1f}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or ["CDS12_ANC_Node1", "CDS12_ANC_Node40", "CDS12_ANC_Node281"])
