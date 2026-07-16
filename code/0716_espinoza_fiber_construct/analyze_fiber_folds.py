"""
Domain-map Prof. Espinoza's AlphaFold3 folds of the 9-2-1 Phi8 tail cluster, to pin down the
construct he wants to order: "CDS 11, removing the first 300ish bases so everything after the
first long beta-sheet barrel" (2026-07-15).

Numbering is HIS (UUAIURNK_) throughout -- the canonical index for this phage. See ../0713_*/.

Four questions, four answers written to code/output/0716_espinoza_fiber_construct/:

  1. template_hits.tsv   Which PDBs did AF3 find, over which query residues?
                         -> identifies "the first long beta-sheet barrel" and settles whether
                            CDS_0010/0012 are really glycosidases.
  2. domain_map.tsv      Sliding-window pLDDT / %beta / %helix / H-bond period / elongation.
                         Reuses the DB-free beta-helix signature from
                         ../0712_phage_rbp_detect/fold_structure/beta_helix_analysis.py:
                         a sustained H-bond sequence-offset peak at ~16-24 = beta-solenoid rung.
  3. model_rmsd.tsv      Superpose the 5 AF3 models on the body, measure where the N-term lands.
                         -> shows the body is rigid and everything N-terminal of ~301 is floppy.
  4. construct_options.tsv + construct_*.fasta
                         The three candidate cut sites, as protein + DNA ready to order.

Input : data/phage_genome/9-2-1/folds_espinoza/  (gitignored -- unzip the prof's 3 zips there)
Run   : python3 code/0716_espinoza_fiber_construct/analyze_fiber_folds.py
"""

import json
import os
import sys
import urllib.request

import numpy as np
from Bio import SeqIO
from Bio.PDB import MMCIFParser, Superimposer
from Bio.Seq import Seq

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
FOLDS = os.path.join(REPO, "data/phage_genome/9-2-1/folds_espinoza")
FFN = os.path.join(REPO, "code/0713_espinoza_structural_mapping/pharokka_espinoza/phanotate.ffn")
OUT = os.path.join(REPO, "code/output/0716_espinoza_fiber_construct")

# prof CDS -> (fold dir, chain count). CDS_0011 was folded as the trimer he says it forms.
JOBS = {
    "CDS_0010": ("fold_cds_0010", 1),
    "CDS_0011": ("fold_cds_011_trimer", 3),
    "CDS_0012": ("fold_cds_0012", 1),
}
BODY = (301, 941)  # CDS_0011: the high-confidence, self-trimerizing beta-helix body
cif = MMCIFParser(QUIET=True)


def die(msg):
    sys.exit(f"ERROR: {msg}\nUnzip the prof's 3 zips into {FOLDS}/ first.")


def model_path(d, k):
    return os.path.join(FOLDS, d, f"{d}_model_{k}.cif")


# ---------------------------------------------------------------- 1. template hits

def pdb_title(pdb, tries=3):
    """Ask RCSB what a template actually is -- AF3 strips titles from the bundled CIFs."""
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb}"
    for n in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                j = json.load(r)
            return j["struct"]["title"], j.get("struct_keywords", {}).get("pdbx_keywords", "")
        except Exception as e:
            if n == tries - 1:
                return f"<lookup failed: {e}>", ""
    return "", ""


def templates():
    """AF3's query_to_hit `name` is the template CIF's filename; the PDB ID is that file's
    data_ block. Which query residues have a template at all is the key readout."""
    rows = []
    for cds, (d, _) in JOBS.items():
        tdir = os.path.join(FOLDS, d, "templates")
        hits = [f for f in sorted(os.listdir(tdir)) if "query_to_hit" in f]
        j = json.load(open(os.path.join(tdir, hits[0])))
        for e in j:
            with open(os.path.join(tdir, e["name"])) as f:
                pdb = next(l.split("_", 1)[1].strip() for l in f if l.startswith("data_"))
            qi = e["queryIndices"]
            title, kw = pdb_title(pdb)
            rows.append(dict(cds=cds, pdb=pdb.upper(), q_start=min(qi) + 1, q_end=max(qi) + 1,
                             n_aligned=len(qi), keywords=kw, title=title))
    return rows


# ---------------------------------------------------------------- 2. domain map

def backbone(chain):
    N, CA, C, O, pl = [], [], [], [], []
    for r in chain:
        if all(a in r for a in ("N", "CA", "C", "O")):
            N.append(r["N"].coord); CA.append(r["CA"].coord)
            C.append(r["C"].coord); O.append(r["O"].coord); pl.append(r["CA"].bfactor)
    return [np.array(x) for x in (N, CA, C, O, pl)]


def dih(p0, p1, p2, p3):
    b0, b1, b2 = p0 - p1, p2 - p1, p3 - p2
    b1n = b1 / np.linalg.norm(b1)
    v = b0 - np.dot(b0, b1n) * b1n
    w = b2 - np.dot(b2, b1n) * b1n
    return np.degrees(np.arctan2(np.dot(np.cross(b1n, v), w), np.dot(v, w)))


def ss_per_res(N, CA, C):
    out = ["-"] * len(CA)
    for i in range(1, len(CA) - 1):
        phi = dih(C[i - 1], N[i], CA[i], C[i])
        psi = dih(N[i], CA[i], C[i], N[i + 1])
        if -180 <= phi <= -40 and 60 <= psi <= 180:
            out[i] = "b"
        elif -160 <= phi <= -30 and -90 <= psi <= -10:
            out[i] = "h"
    return np.array(out)


def hb_period(N, O, lo, hi):
    """Dominant backbone H-bond sequence-offset >=10 inside [lo,hi). ~16-24 => beta-solenoid rung."""
    offs = []
    for i in range(lo, hi):
        d = np.linalg.norm(O - N[i], axis=1)
        offs += [abs(i - j) for j in np.where(d < 3.5)[0] if abs(i - j) > 2 and lo <= j < hi]
    if not offs:
        return 0, 0
    bc = np.bincount(np.array(offs, int), minlength=41)[:41]
    far = bc[10:].argmax() + 10
    return int(far), int(bc[far])


def elong(CA, lo, hi):
    X = CA[lo:hi] - CA[lo:hi].mean(0)
    ev = np.linalg.svd(X, compute_uv=False)
    return ev[0] / max(ev[1], 1e-6)


def domain_map(win=40):
    rows = []
    for cds, (d, _) in JOBS.items():
        N, CA, C, O, pl = backbone(cif.get_structure("x", model_path(d, 0))[0]["A"])
        ss = ss_per_res(N, CA, C)
        for s in range(0, len(CA), win):
            e = min(s + win, len(CA))
            if e - s < 15:
                continue
            per, pk = hb_period(N, O, s, e)
            rows.append(dict(cds=cds, res_start=s + 1, res_end=e, plddt=round(pl[s:e].mean(), 1),
                             frac_beta=round((ss[s:e] == "b").mean(), 2),
                             frac_helix=round((ss[s:e] == "h").mean(), 2),
                             hb_period=per, hb_peak=pk, elongation=round(elong(CA, s, e), 2)))
    return rows


# ---------------------------------------------------------------- 3. model-to-model RMSD

def rmsd_rows():
    """Superpose models 1-4 on model 0 using the BODY only, then see where each region landed.

    Body RMSD tiny + N-term RMSD huge => AF3 is confident about the body and has no idea where
    the N-terminal domains sit. That is the whole argument for where to cut.
    """
    d = JOBS["CDS_0011"][0]
    chains = [cif.get_structure(f"m{k}", model_path(d, k))[0]["A"] for k in range(5)]

    def at(ch, lo, hi):
        return [r["CA"] for r in ch if "CA" in r and lo <= r.id[1] <= hi]

    def pair_rmsd(a, b, lo, hi):
        f = np.array([x.coord for x in at(a, lo, hi)])
        m = np.array([x.coord for x in at(b, lo, hi)])
        return float(np.sqrt(((f - m) ** 2).sum(1).mean()))

    rows = []
    ref = chains[0]
    for k in range(1, 5):
        mob = chains[k]
        sup = Superimposer()
        sup.set_atoms(at(ref, *BODY), at(mob, *BODY))
        body_rms = sup.rms
        sup.apply([a for r in mob for a in r])
        rows.append(dict(model=k, rmsd_body_301_941=round(body_rms, 2),
                         rmsd_calx_beta_1_110=round(pair_rmsd(ref, mob, 1, 110), 1),
                         rmsd_shaft_111_300=round(pair_rmsd(ref, mob, 111, 300), 1)))
    return rows


# ---------------------------------------------------------------- 4. construct options

CUTS = [
    (111, "prof's words: remove the first ~300 bases = the Calx-beta anchor (res 1-110)"),
    (301, "clean cut: start of the rigid, self-trimerizing beta-helix body"),
    (391, "his 0713 claim: the RBD is 'the C-terminal ~550 aa'"),
]


def constructs():
    rec = {r.id: r for r in SeqIO.parse(FFN, "fasta")}["UUAIURNK_CDS_0011"]
    nt = str(rec.seq)
    aa = str(Seq(nt).translate()).rstrip("*")
    assert len(aa) == 941, f"expected 941 aa, got {len(aa)}"
    rows, fa = [], []
    for start, why in CUTS:
        sub_nt, sub_aa = nt[(start - 1) * 3:], aa[start - 1:]
        rows.append(dict(name=f"CDS_0011_{start}-941", aa_start=start, aa_end=941,
                         n_aa=len(sub_aa), n_bp_incl_stop=len(sub_nt),
                         peptide_starts=sub_aa[:12], rationale=why))
        fa.append((f"CDS_0011_{start}-941 | {len(sub_aa)} aa | {why}", sub_aa, sub_nt))
    return rows, fa


# ---------------------------------------------------------------- write

def write_tsv(path, rows):
    cols = list(rows[0].keys())
    with open(path, "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r[c]) for c in cols) + "\n")
    print(f"  wrote {os.path.relpath(path, REPO)}  ({len(rows)} rows)")


def main():
    for cds, (d, _) in JOBS.items():
        if not os.path.exists(model_path(d, 0)):
            die(f"missing {model_path(d, 0)}")
    os.makedirs(OUT, exist_ok=True)

    print("1. template hits (asking RCSB what each template is)...")
    write_tsv(os.path.join(OUT, "template_hits.tsv"), templates())
    print("2. sliding-window domain map...")
    write_tsv(os.path.join(OUT, "domain_map.tsv"), domain_map())
    print("3. model-to-model RMSD (body-superposed)...")
    write_tsv(os.path.join(OUT, "model_rmsd.tsv"), rmsd_rows())
    print("4. construct options...")
    rows, fa = constructs()
    write_tsv(os.path.join(OUT, "construct_options.tsv"), rows)
    for ext, idx in (("faa", 1), ("ffn", 2)):
        p = os.path.join(OUT, f"construct_options.{ext}")
        with open(p, "w") as f:
            for h, *seq in fa:
                f.write(f">{h}\n")
                s = seq[idx - 1]
                for i in range(0, len(s), 60):
                    f.write(s[i:i + 60] + "\n")
        print(f"  wrote {os.path.relpath(p, REPO)}")


if __name__ == "__main__":
    main()
