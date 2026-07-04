# RBP × Receptor Binding Screen — Folding-Tool Recommendation (7,182 pairs, <24 h, Laguna L40S / CUDA 12.4)

*Decision doc for `code/0703_phage_host_matrix/fold/`. Supersedes the tool-selection notes in `fold/GUIDE.md`, `fold/boltz/GUIDE.md`, and `fold/esmfold/GUIDE.md`. Companion to `documents/2026-07-04_folding_tool_odyssey.md` (the CUDA-driver history). Produced by a 21-agent research workflow (survey → deep-dive → synthesize → adversarial critique → finalize).*

## 0. This is grounded in what you've already built

The ESMFold track is **not hypothetical — it is coded and matches the intended plan almost exactly.** `fold/esmfold/esmfold_run.py` already folds each RBP + `"G"*25` + receptor as one chain, derives a pseudo-ipTM from the cross-chain PAE block (`iptm_from_pae`), runs the ESM2 stem in fp16, exposes `--chunk-size`/`--max-len`, appends one resumable row per pair, and tags `OOM`/`SKIP_TOOLONG` instead of dying. The sbatch, splitter, collector, and smoke script all exist. **This recommendation is therefore mostly "commit the array you've built, with four specific parameter/scheduling fixes and one mandatory addition (controls)" — not "adopt a new tool."**

## 1. Bottom line

**Run the ESMFold track you already built. Do not switch tools to hit the deadline.** It is the only path empirically proven to install and run on this exact L40S / CUDA-12.4 box with zero kernel compilation (Boltz's `cuequivariance`/cuBLAS-12.5 wall and ColabFold's rate-limited remote MSA both killed those tracks — see the odyssey doc). Four fixes make the <24 h target robust, and one addition decides whether the heatmap means anything:

1. **Concurrency is the whole ballgame — raise `%8` → `%16` if the allocation allows.** At `%8` (your sbatch's current default) the plan is on a knife's edge; at `%16` it is comfortable. This single number, not tool choice, controls the deadline.
2. **Attack the long tail by truncation, not by a second slow array.** Lower `--max-len` from 2000 to ~1600. The tail is where wall-time concentrates and where scores are least reliable; those pairs are already flagged `SKIP_TOOLONG` and re-foldable later.
3. **Domain-aware truncation for the ~4–6 largest RBPs** (>~1200 aa) so they actually get scored instead of silently dropped — keep the **C-terminal** receptor-binding domain.
4. **Order the queue by a cheap pre-rank** (optional insurance) so plausible pairs finish first — but for a heatmap, **order, don't gate** (gating leaves holes in the matrix).
5. **MANDATORY: run a positive/negative control set through the identical pipeline before trusting any of the 7,182 numbers.** MSA-free single-sequence folding of cross-kingdom phage×OMP pairs can produce a beautifully-formatted matrix that ranks ~randomly. Controls are the single highest-value thing to add, and they cost ~10 folds.

**Chai-1 is not a general upgrade — reserve it for re-folding the top ~20–50 hits as true homotrimer + receptor.** MSA-free Chai-1 shares ESMFold's coevolution-blindness on these novel pairs; what it adds is a genuine `per_chain_pair_iptm` and correct trimeric geometry, which matters only for the shortlist, not for all 7,182 cells.

## 2. The real numbers (computed from your actual FASTAs, not estimates)

From `fold/probes.fasta` (114 RBPs) × `fold/receptors_panel.fasta` (63 receptors) = **7,182 pairs**. Construct length = RBP + 25 (linker) + receptor:

| stat | combined length (aa) |
|---|---|
| median | **1,085** |
| mean | 1,119 |
| p75 / p90 / p95 / p99 | 1,379 / 1,624 / 1,734 / 2,229 |
| max | 3,119 |

Fraction of pairs above each cap (this sets your truncation lever):

| cap | pairs over | % |
|---|---|---|
| >1200 | 2,920 | 40.7% |
| >1400 | 1,685 | 23.5% |
| **>1600** | **824** | **11.5%** |
| >1800 | 291 | 4.1% |
| >2000 (current skip) | ~179 | ~2.5% |

RBP-side problem is **small and localized**: only **6 RBPs are >1000 aa and 4 are >1300 aa** (max 1,922). Under the current `--max-len 2000`, those 4 biggest RBPs paired with *any* receptor exceed the cap and get **skipped entirely — they'd have zero row in the matrix.** That's the concrete cost of not doing domain-aware truncation (Section 7).

## 3. Ranked comparison

| Rank | Tool | Status in repo | Est. speed/pair on L40S | All 7,182 <24 h? | CUDA-12.4 install risk | Score type | Verdict |
|---|---|---|---|---|---|---|---|
| **1** | **ESMFold** (HF `EsmForProteinFolding`, G25 linker) | **Built & wired** (`esmfold_run.py`) | ~45–60 s median (≈45 s/1000 aa anchor); tail 150–350 s | **Yes at %16; borderline at %8** — see §5 | **None — proven working** | cross-chain-PAE pseudo-ipTM (proxy) | **ADOPT — commit the array** |
| 2 | **Chai-1** (`chai_lab`, no-MSA + ESM2 emb.) | Not built | ~60–150 s est. (UNVERIFIED on L40S) | For top-hits only, trivially | **Low** (no cuequivariance/trifast/triton — verified) | native `per_chain_pair_iptm` | **TOP-HITS RE-FOLD ONLY** (§9) |
| 3 | **MEGADOCK-GPU** (FFT dock on pre-folded monomers) | Not built | ~15 s blended | Yes | Low-med (cuFFT only; needs `sm_89` + header patch) | rPSC shape (size-biased, not ipTM) | **FALLBACK** — but needs OMP topology first (§8) |
| 4 | **Boltz-2** (`--no_kernels`) | Built (`boltz/`) | **~403 s** (pure-PyTorch triangle) | **No — ~13× too slow** | High (kernel path blocked by cuBLAS-12.5) | native ipTM | **Deprecated — keep for top-hits re-fold at most** |
| 5 | **LocalColabFold** (AF2-multimer, single_seq) | Built (`GUIDE.md`) | ~3.5 min + garbage single_seq (pLDDT≈28) | No, and low quality | Low (JAX never touches cuBLAS-12.5) but heavy DB infra | native ipTM | **Deprecated** |
| 6 | **Seq-only PPI** (D-SCRIPT / SENSE-PPI) | Not built | ~ms/pair after one embed | Trivially (minutes on 1 GPU) | Low | interaction prob (0–1), off-distribution for phage×OMP | **Queue-ORDER insurance only, never gate** |

## 4. Stay on ESMFold? — Yes.

**Switching tools now would replace a working, wired, resumable pipeline with fresh CUDA-driver risk, to chase a score that is *format*-better but *signal*-equivalent on these MSA-free cross-kingdom pairs.** ESMFold clears the deadline at `%16` and plausibly at `%8` with tail truncation, installs with no kernels, and already emits a defensible ranking readout. The honest caveats — monomer×monomer (RBPs are homotrimers; the true binding tip is the trimer apex), a G25-linker docking hack with ~44–57% DockQ interface recovery on *general* heterodimers (Linker-Tuning, arXiv:2312.01186) — make this a **ranking signal, not a binding call**, exactly matching your stated "coarse but well-ranked, refine top hits later" bar. Do not switch to *escape* ESMFold. Probe Chai-1 only to *re-score the shortlist* (§9).

## 5. #1 pick: concrete plan to hit <24 h

**Install / run** — already documented in `fold/esmfold/GUIDE.md` (reuse the working `boltz` cu124-torch env, `pip install transformers accelerate`, pre-cache the ~2.5 GB `facebook/esmfold_v1` weights on a login node since compute nodes lack egress). No changes needed there. The load-bearing edits are below.

**Timeline math, grounded in the real data.** Anchor: plain ESMFold ≈45 s at 1000 aa on a modern GPU (BioLM; the 15.8 s ESMFold2 figure uses custom Triton kernels — *do not* pursue, that is the compilation trap). Correcting the draft's record: the ~14 s/384 aa figure is **A10G, not V100**, and its recycle count is unstated; and **L40S has GDDR6 ~864 GB/s vs A100's HBM ~1.5–2 TB/s**, so on the 1,400–1,700 aa tail L40S runs ~1.5–2× slower than an A100. Net expectation: **median ~50–60 s, tail (p90–p99) ~150–350 s, blended mean ~80–110 s** — *to be confirmed by the smoke test, which is the real gate.* Wall-time by concurrency at a blended 90 s/pair:

- **`%16` → 7,182 × 90 / 16 ≈ 11 h** (17 h at a pessimistic 140 s). **Safe.**
- **`%8` → 7,182 × 90 / 8 ≈ 22.4 h** (30 h at 140 s). **On the edge; misses if the mean is >~96 s.**

**Edit 1 — concurrency (decisive).** Confirm you can actually hold ~16 L40S on the shared `gpu` partition. If yes, submit `--array=0-119%16` instead of the GUIDE's `%8`. If the allocation realistically caps you at 8 concurrent, you *must* also do Edit 2, and treat the smoke number as pass/fail against the `%8` line above.

**Edit 2 — attack the tail by truncation, not scheduling.** Run `esmfold_run.py --max-len 1600` (down from 2000). This drops the most expensive **11.5%** of folds — which are also the most OOM-prone and least reliable — cutting the blended mean substantially because O(L²)-ish cost is concentrated there. Skipped pairs are tagged `SKIP_TOOLONG` (already implemented), stay in the matrix as blanks, and are re-folded later with domain trimming or Chai-1. **Note: your actual `esmfold_run.py` runs one flat array with a length skip — keep the single-array design; just lower the cap.**

**Edit 3 — resumability discipline.** The script already skips pairs present in the out CSV, so a preempted array task is safe to resubmit. Keep chunks small (`split_esm.py 60` → 120 chunks) so a killed task loses little. Verify one full forward on the longest *kept* pair (~1600 aa) fits 48 GB at `--chunk-size 64`; drop to 32 if it OOMs.

**Then:** `collect_esm.py results binding_matrix.csv` → `fold_heatmap.py` → commit the matrix + heatmap on Laguna (Step 8 of the ESMFold GUIDE). Structures stay on Laguna; only the CSV + PNG return.

## 6. MANDATORY — controls (do this before trusting the matrix)

This is the top omission the tool debate hides. ESMFold is MSA-free single-sequence; for **cross-kingdom phage RBP × bacterial OMP** pairs there is *no* coevolutionary signal, so the linker heterodimer can dock the two domains arbitrarily and the interface-PAE can be ~uniform → **ranking ≈ random.** The cited DockQ 44–57% is on general heterodimers with training-set homologs — it is **not evidence the method ranks novel phage×OMP binders.** You cannot tell "coarse but ranked" from "coarse and unranked" without controls.

**Add a tiny calibration set and run it through the identical `esmfold_run.py`:**
- **Positives:** 2–4 characterized *Pseudomonas* (or close) phage RBP–receptor pairs from the literature with a known cognate receptor (e.g., a documented tail-fiber/tailspike whose OMP/LPS-proximal receptor is established). Pull sequences from the papers/NCBI.
- **Negatives:** the *same* positive RBPs paired with a deliberately mismatched receptor, plus 2–3 sequence-scrambled receptors (preserve length/composition, shuffle order).
- **Decision rule:** if the pseudo-ipTM (and `interchain_pae_min`) do **not** separate positives from negatives, the full heatmap is noise — report it as such and pivot the shortlist to Chai-1/Boltz re-folds or a MEGADOCK triage, rather than shipping a random-ranked matrix. If they *do* separate, you have an empirical threshold to draw on the heatmap legend instead of the ad-hoc "smoke ipTM ~0.25–0.41" range.

This is ~10 extra folds — cheaper than any other item here and it governs the interpretation of all 7,182.

## 7. Long tail + truncation (biology, not just speed)

The 1,922 aa max RBP exceeds any sane cap by itself. Tailspike/tail-fiber **receptor-binding domains are C-terminal**; naive keep-the-front truncation deletes the site you are scoring. Fix, for the **6 RBPs >~1000 aa** (only 4 are truly problematic at >1300):
- In `make_esm_pairs.py`, for those RBP sequences substitute the **C-terminal ~700–900 aa** (the RBD-bearing region) in place of the full sequence, so RBP+linker+receptor lands under `--max-len` and the pair actually gets a score.
- Flag those rows (e.g., a `truncated` column) as **low-confidence** in the matrix.
- Everything ≤~1000 aa RBP (108 of 114) is untouched — this is a 4–6-RBP surgical fix, not a global operation.

## 8. Named fallback

**If the ESMFold tail OOMs/straggles even after truncation, or if controls show the pseudo-ipTM doesn't separate: MEGADOCK-GPU** on ESMFold-folded monomers (fold the ~177 unique chains once, then FFT-dock all pairs; cuFFT-only, sidesteps the cuBLAS wall; ~15 s/pair blended → whole matrix in single-digit hours). **Two real prerequisites the tool choice hides:** (a) you have **no OMP topology annotation** for the 63 receptors — MEGADOCK should dock the **trimmed extracellular loops**, not the full β-barrel, so you must add a topology/boundary step first; (b) the rPSC score is **size-biased — z-score within each receptor column before ranking, never compare raw scores across differently-sized proteins.** Build the `sm_89` + cuda-samples header patch once. This is a bigger project than "fold monomers, FFT-dock," so treat it as a genuine fallback, not a co-primary.

## 9. Chai-1 — reframed as top-hits re-fold

**Verified:** `chai_lab`'s deps are pure torch/Python (torch ≥2.3.1; **no cuequivariance, trifast, flash-attn, or triton**) — the exact profile Boltz-2 *lacked*, so it structurally clears the cuBLAS-12.5 wall, and L40S 48 GB is on Chai's recommended-hardware list. But **MSA-free Chai (`use_msa_server=False`) is AF3-without-MSA — it shares ESMFold's coevolution-blindness on these novel pairs.** So it upgrades the *metric* (real `per_chain_pair_iptm` + correct geometry), not the *signal*, for the general screen. Its real value: **re-fold the top ~20–50 ESMFold hits as true homotrimer (3× RBP chains) + receptor**, where trimeric geometry and a calibrated interface score genuinely matter.
- Install: `pip install torch==2.5.1 --index-url .../cu124` **first**, then `pip install chai_lab` (confirm the pinned version's deps still match the clean profile above; the repo README covers 2.3.1–2.7.1).
- **Weights come from chaiassets.com (Cloudflare R2)** — a compute node with no egress fails hard; **pre-warm `CHAI_DOWNLOADS_DIR` and `HF_HOME` on a login node**, then set `HF_HUB_OFFLINE=1`. License is **non-commercial** (fine for iGEM; note it).
- Run: `use_msa_server=False, num_diffn_samples=2, num_trunk_recycles=3, low_memory=True`; read `max(np.load(f)['iptm'])` over `scores.model_idx_*.npz`. Folding the true trimer triples tokens → 3–8× slower + OOM risk, which is exactly why this is shortlist-only.

## 10. Smoke-test checklist (do these on Laguna *before* the full array)

1. **Measure real per-pair time on L40S** across your true range: fold ~8 pairs spanning short / median (~1,085 aa) / p95 (~1,734) / a truncated big-RBP case, at your actual recycle setting. Report **median AND p95**, and size the array width from p95, not median. This single measurement validates or breaks the <24 h claim.
2. **Confirm concurrency.** Verify you can actually hold ~16 concurrent L40S on `gpu`. If only ~8, apply Edit 2 (max-len 1600) and re-check the smoke number against the `%8` line (needs blended mean <~96 s).
3. **Run the control set (§6) through `esmfold_run.py`** and check positive-vs-negative score separation. Gate the whole interpretation on this.
4. **Confirm the longest *kept* pair (~1,600 aa, chunk 64/32) fits 48 GB** without OOM.
5. **Verify output fields** in the installed transformers: `out.predicted_aligned_error` shape `[L,L]` and `out.ptm`/`out.plddt` on one fold (the script already reads these; just confirm the version matches).
6. **Apply domain-aware truncation** to the 4–6 RBPs >~1000 aa in `make_esm_pairs.py` so they aren't silently skipped; flag them `truncated`.
7. **fp16 on the ESM stem only** — the script does `model.esm = model.esm.half()` and never `.half()`s the trunk. Keep it that way (a half trunk NaNs the scores).
8. **Legend the biology tradeoff on the heatmap:** monomer-vs-homotrimer + G25-linker hack ⇒ ranking signal, not a binding call; re-fold top ~20–50 as trimer+receptor (Chai-1) for the shortlist.

---

*Log: 2026-07-04 — synthesized from a 21-agent research workflow (survey → deep-dive → synthesize → adversarial critique → finalize), re-grounded in the actual `fold/` scaffolding and the real length distribution of `probes.fasta`/`receptors_panel.fasta`. Advisor tool unavailable at write time. Key deltas vs. the draft: (a) <24 h reframed as concurrency-conditional (sbatch defaults to `%8`, where the plan is borderline); (b) tail handled by lowering `--max-len` in the existing single array, not a second slow array; (c) controls elevated to mandatory pre-flight; (d) Chai-1 demoted to top-hits re-fold; (e) confirmed only 4–6 RBPs need domain-aware truncation; (f) corrected the speed anchor (A10G not V100; L40S bandwidth-limited vs A100 on the tail).*
