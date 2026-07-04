# Folding-tool odyssey — RBP × receptor 那一折的坎坷

> 這份文件記錄「把候選 phage RBP × 我們的 receptor 折成複合物、取結合分數」這條線在 Laguna 上
> 換了三個工具、踩了六個坑的完整過程,方便日後 debug、不重蹈覆轍。結論:**最後落在 ESMFold**。

## 目標
7,182 對(114 RBP families × 63 receptors)各折一個 RBP–receptor 複合物 → 每對一個界面分數
→ RBP × receptor 熱圖。硬體:Laguna 的 **NVIDIA L40S(CUDA 12.4 驅動)**,共用 10k GPU-hr 額度。
需求(user):要一張**幾小時內能出的 proof-of-concept 熱圖**,分數可以不精準,之後再對亮點細跑。

## 時間線 / 踩過的坑

### 工具 1 — ColabFold / AlphaFold2-multimer
- **坑 1:遠端 MSA 伺服器瓶頸**。ColabFold 預設打 UGent 的 MMseqs2 MSA 伺服器,rate-limited、
  一天只幾千個、還讓 GPU 空等(log 卡在 `Sleeping... RUNNING`)。7,182 對不可能這樣跑。
- **坑 2:改 `--msa-mode single_sequence` 後精度崩**。離線是離線了,但沒有 MSA → pLDDT ≈ 28(垃圾),
  而且每個長度都重編譯 → **~3.5 min/折**。430 GPU-hr 換一堆雜訊。放棄。

### 工具 2 — Boltz-2(AF3-like、MSA-free)
換 Boltz-2:MSA-free 也堪用、預期 ~30s/折。結果為了讓它在這台驅動上跑,連環三坑:
- **坑 3:torch 對驅動太新**。`pip install boltz[cuda]` 帶的 torch 是給更新 CUDA 編的 →
  `NVIDIA driver too old (found version 12040)`。改裝 **cu124 build 的 torch**。
- **坑 4:`--no-deps` 漏了 CUDA 函式庫**。第一次修用 `--force-reinstall --no-deps` 換 torch,結果
  漏裝 torch bundle 的 CUDA runtime → `libcudart.so.12: cannot open shared object file`,torch 連
  import 都掛。修法:重建 env、**含 deps** 裝 cu124 torch。torch 這才能 import + 抓到 L40S。
- **坑 5:cuequivariance kernel 撞 cuBLAS 符號**。Boltz 的優化 kernel `libcue_ops.so` 要
  `cublasGemmGroupedBatchedEx`(cuBLAS 12.5+ 才有),但 cu124 torch 帶 cuBLAS 12.4 → 缺符號。
  想升 cuBLAS 又會撞回「驅動太舊」。試過 `LD_PRELOAD` 塞 `~/.local` 的 12.6 cuBLAS,torch 仍載自己
  bundle 的 12.4,沒解。
- **坑 6:`--no_kernels` 能跑但太慢**。用 Boltz 的 `--no_kernels`(純 PyTorch 三角更新)繞過 kernel →
  **能折了,但 403s/折**(比帶 kernel 的 ~30s 慢 ~13×,`sys` time 爆表)。全矩陣 %8 ≈ 100h wall。
  不符合「幾小時」。放棄 Boltz。

### 工具 3 — ESMFold(現行方案)
user 拍板:**簡單粗暴用 ESMFold**。理由:HuggingFace `transformers` 版的 ESMFold 是
**純 PyTorch、無 MSA、無 cuequivariance / 無 CUDA kernel**(openfold 工具是 vendored 進去的),
一次躲開坑 5+6 那整類地雷;而且**重用 boltz env 那顆已經能跑的 cu124 torch**,不用再碰坑 3+4。
- 做法:每對 `RBP + (25×G linker) + receptor` 折成一條 → 從**跨鏈 PAE** 算 pseudo-ipTM 當粗分數。
- 代價:ESMFold 本是單鏈模型,拼複合物是 hack,分數是**粗排序、非定論**;之後對高分區塊再細折。
- 速度:多數對(中位長 ~1066 aa)幾秒~十幾秒 → 全矩陣 %8/%16 幾小時內出圖。~2.5% 過長(>2000 aa)標記
  `SKIP_TOOLONG`,不靜默丟。

## 教訓
1. **驅動版本是天花板**:Laguna 是 CUDA 12.4 驅動,任何要 cuBLAS 12.5+ / 更新 CUDA runtime 的預編 kernel
   都會卡。要嘛用能在 12.4 上跑的 build,要嘛用不依賴這些 kernel 的純 PyTorch 工具。
2. **換 torch build 千萬別 `--no-deps`**:會漏掉 bundle 的 CUDA runtime 函式庫。
3. **MSA-free 是 7k 對規模的硬需求**:遠端 MSA 伺服器擋死,單序列 AF2 又是垃圾;要嘛 Boltz/ESMFold 這種
   本來就 MSA-free 的模型。
4. **proof-of-concept 先求「能在幾小時內填滿整個矩陣」**,精度之後對亮點補;工具選型要服從這個約束。

## 程式碼位置
- ColabFold 版(備援):`code/0703_phage_host_matrix/fold/`(`rbp_receptor.sbatch` 等)
- Boltz-2 版(封存,坑 3–6):`code/0703_phage_host_matrix/fold/boltz/`
- **ESMFold 版(現行)**:`code/0703_phage_host_matrix/fold/esmfold/` — 見該資料夾 `GUIDE.md`

---
*Log — 2026-07-04:ColabFold→Boltz-2→ESMFold 三跳、六坑全記錄。Boltz 卡在 L40S CUDA 12.4 驅動 ×
cuequivariance kernel 需 cuBLAS 12.5+;`--no_kernels` 能跑但 403s/折。轉 ESMFold(純 PyTorch、
重用 boltz env 的 cu124 torch),pipeline 寫在 `fold/esmfold/`,待 smoke 驗證每折時間。*
