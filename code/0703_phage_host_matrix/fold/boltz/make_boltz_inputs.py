#!/usr/bin/env python3
"""
Build Boltz-2 YAML inputs for the RBP × receptor fold (MSA-free / single-sequence).

Reads probes.fasta + receptors_panel.fasta (co-located in this workspace) and writes one
YAML per pair into boltz_input/<RBP>__<REC>.yaml (two protein chains, `msa: empty`), plus a
6-pair smoke set in smoke_input/. The YAML stem <RBP>__<REC> becomes the Boltz output name,
so collect_boltz.py can decode it.

Run from the workspace (where probes.fasta + receptors_panel.fasta live):
  python3 make_boltz_inputs.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
YAML = """version: 1
sequences:
  - protein:
      id: A
      sequence: {rbp}
      msa: empty
  - protein:
      id: B
      sequence: {rec}
      msa: empty
"""


def read_fasta(path):
    name, buf = None, []
    for line in open(path):
        if line.startswith(">"):
            if name:
                yield name, "".join(buf)
            name, buf = line[1:].split()[0], []
        else:
            buf.append(line.strip())
    if name:
        yield name, "".join(buf)


def main():
    probes = dict(read_fasta(os.path.join(HERE, "probes.fasta")))
    recs = dict(read_fasta(os.path.join(HERE, "receptors_panel.fasta")))
    indir = os.path.join(HERE, "boltz_input")
    smoke = os.path.join(HERE, "smoke_input")
    os.makedirs(indir, exist_ok=True)
    os.makedirs(smoke, exist_ok=True)

    n = 0
    for r, rs in probes.items():
        for c, cs in recs.items():
            with open(os.path.join(indir, f"{r}__{c}.yaml"), "w") as fh:
                fh.write(YAML.format(rbp=rs, rec=cs))
            n += 1
    # smoke: first 3 RBP × first 2 receptors
    for r in list(probes)[:3]:
        for c in list(recs)[:2]:
            with open(os.path.join(smoke, f"{r}__{c}.yaml"), "w") as fh:
                fh.write(YAML.format(rbp=probes[r], rec=recs[c]))
    print(f"{len(probes)} RBP × {len(recs)} receptor = {n} YAMLs -> boltz_input/ | smoke_input/: 6")


if __name__ == "__main__":
    main()
