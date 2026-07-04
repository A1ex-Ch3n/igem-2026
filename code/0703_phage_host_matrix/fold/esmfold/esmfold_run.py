#!/usr/bin/env python3
"""
ESMFold RBP x receptor complex screen (MSA-free, CUDA-kernel-free).

For each RBP-family x receptor pair, fold a 2-chain complex with HuggingFace ESMFold
(facebook/esmfold_v1): concatenate rbp + a glycine linker + receptor, fold as one input,
then score the interface from the cross-chain block of the predicted-aligned-error (PAE)
matrix with a PAE-derived pseudo-ipTM. One row per pair is appended to <out.csv>; the run
is resumable (pairs already present in <out.csv> are skipped).

NOT a true AlphaFold ipTM: ESMFold is a single-sequence monomer model repurposed for
complexes via a linker, so the score is a COARSE proof-of-concept ranking, not a calibrated
binding affinity. High scorers are wet-lab candidates to re-fold with a complex-native model.

Usage:
  python3 esmfold_run.py <pairs.tsv> <out.csv> [--linker 25] [--chunk-size 64] [--max-len 2000]

pairs.tsv (tab, with header): rbp_id  rec_id  rbp_seq  rec_seq
out.csv columns: rbp_id,rec_id,iptm,ptm,interchain_pae_min,interchain_pae_mean,plddt_mean,len,status
"""
import argparse
import csv
import os

import numpy as np


def iptm_from_pae(pae, idxA, idxB):
    """Interface-pTM proxy from PAE: for each residue, mean TM-weight to the OTHER chain;
    take the best residue. TM weight = 1/(1+(pae/d0)^2), d0 from the two-chain length."""
    n = len(idxA) + len(idxB)
    d0 = max(1.24 * (n - 15) ** (1.0 / 3.0) - 1.8, 0.5)
    w = 1.0 / (1.0 + (pae / d0) ** 2)
    per_A = w[np.ix_(idxA, idxB)].mean(axis=1)   # each A residue -> all B
    per_B = w[np.ix_(idxB, idxA)].mean(axis=1)   # each B residue -> all A
    return float(max(per_A.max(), per_B.max()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs")
    ap.add_argument("out")
    ap.add_argument("--linker", type=int, default=25, help="glycine linker length between chains")
    ap.add_argument("--chunk-size", type=int, default=64, help="ESMFold trunk chunk size (lower = less VRAM)")
    ap.add_argument("--max-len", type=int, default=1600, help="skip pairs whose total length exceeds this "
                    "(1600 drops the most expensive/least-reliable ~11.5%% as SKIP_TOOLONG, re-foldable later)")
    a = ap.parse_args()

    import torch
    from transformers import AutoTokenizer, EsmForProteinFolding

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f">> device={dev}; loading facebook/esmfold_v1 (first run downloads ~2.5GB) ...", flush=True)
    tok = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
    model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", low_cpu_mem_usage=True)
    model = model.to(dev).eval()
    if dev == "cuda":
        model.esm = model.esm.half()                    # half-precision LM stem: faster, less VRAM
        torch.backends.cuda.matmul.allow_tf32 = True
    model.trunk.set_chunk_size(a.chunk_size)

    # resume: collect pairs already scored
    done = set()
    existed = os.path.exists(a.out)
    if existed:
        for r in csv.DictReader(open(a.out)):
            done.add((r["rbp_id"], r["rec_id"]))
    fh = open(a.out, "a", newline="")
    w = csv.writer(fh)
    cols = ["rbp_id", "rec_id", "iptm", "ptm", "interchain_pae_min",
            "interchain_pae_mean", "plddt_mean", "len", "status"]
    if not existed:
        w.writerow(cols); fh.flush()

    linker = "G" * a.linker
    rows = list(csv.DictReader(open(a.pairs), delimiter="\t"))
    todo = [r for r in rows if (r["rbp_id"], r["rec_id"]) not in done]
    print(f">> {len(rows)} pairs, {len(done)} already done, {len(todo)} to fold", flush=True)

    for i, r in enumerate(todo, 1):
        A, B = r["rbp_seq"].strip(), r["rec_seq"].strip()
        LA, LB = len(A), len(B)
        L = LA + a.linker + LB
        if L > a.max_len:
            w.writerow([r["rbp_id"], r["rec_id"], "", "", "", "", "", L, "SKIP_TOOLONG"]); fh.flush()
            print(f"   [{i}/{len(todo)}] {r['rbp_id']}x{r['rec_id']} SKIP len={L}>{a.max_len}", flush=True)
            continue
        seq = A + linker + B
        try:
            ids = tok([seq], return_tensors="pt", add_special_tokens=False)["input_ids"].to(dev)
            with torch.no_grad():
                out = model(ids)
            pae = out.predicted_aligned_error[0].float().cpu().numpy()   # [L, L]
            ptm = float(out.ptm)
            plddt_mean = float(out.plddt.float().mean())
            idxA = np.arange(0, LA)
            idxB = np.arange(LA + a.linker, L)
            ic = pae[np.ix_(idxA, idxB)]
            iptm = iptm_from_pae(pae, idxA, idxB)
            w.writerow([r["rbp_id"], r["rec_id"], f"{iptm:.4f}", f"{ptm:.4f}",
                        f"{ic.min():.2f}", f"{ic.mean():.2f}", f"{plddt_mean:.2f}", L, "OK"]); fh.flush()
            if i % 5 == 0 or i == 1:
                print(f"   [{i}/{len(todo)}] {r['rbp_id']}x{r['rec_id']} iptm={iptm:.3f} pae_min={ic.min():.1f} len={L}", flush=True)
        except RuntimeError as e:
            status = "OOM" if "out of memory" in str(e).lower() else "ERR"
            if dev == "cuda":
                torch.cuda.empty_cache()
            w.writerow([r["rbp_id"], r["rec_id"], "", "", "", "", "", L, status]); fh.flush()
            print(f"   [{i}/{len(todo)}] {r['rbp_id']}x{r['rec_id']} {status}: {str(e)[:100]}", flush=True)

    fh.close()
    print(">> done", flush=True)


if __name__ == "__main__":
    main()
