# 噬菌體 RBP–受體 高通量 PPI 篩選 Pipeline 設計

> **用途**:這份文件總結了 pipeline 的選型、架構、各階段運作、加速策略與待驗證實驗。
> 目標是帶進 Claude Code 接著實作與嘗試。
> **場景**:Phagenomics — AI/ML 導引的噬菌體 receptor-binding protein (RBP) 設計,
> 需對「一組 RBP × 一組宿主受體」做高通量結合預測篩選。
> **規模**:幾萬對(數量級 ~10⁴)。**硬體**:L40S GPU 叢集(laguna)。

---

## 0. 決策摘要(TL;DR)

- **模型 = Boltz-2**(不是 AlphaFold3)。唯一決定性理由:**授權**。Boltz 是 MIT,可商用;AF3 權重非商業授權,對 Phagenomics 商業化是死路。
- **篩選分數 = ipTM**(來自 Boltz confidence 模組)。**不算 affinity** — 它的 head 是蛋白–配體訓練的,對蛋白–蛋白不適用。
- **漏斗式**:粗篩(全部幾萬對,低取樣)→ 精算(前幾 %,高取樣)。兩段都用 Boltz-2。
- **MSA 按 unique 蛋白快取,不按對算**。這是成本能否收斂的關鍵。
- **真正的瓶頸不是 MSA**,是 N² 次、無法跨對快取的 **Boltz trunk 三角運算**。
- **現成 turnkey 工具(AlphaPulldown)是 AF 後端**,授權對我們不乾淨;Boltz 版沒人封裝好,需自己拼(但膠水很薄,評分階段可用 AlphaJudge)。

---

## 1. 專案脈絡與目標

- 對兩個 array of protein(baits = RBPs,candidates = 宿主表面受體)做全對或 pulldown 式的結合預測。
- 輸出:每一對的交互作用信心分數(ipTM 為主),用來排序、挑出高信心結合對。
- 下游:高信心對進 wet-lab 驗證 / 進一步結構分析。
- 約束:走向商業化與專利,所以**所有工具的授權必須乾淨(可商用),序列盡量不外流第三方**。

---

## 2. 選型結論與理由

| 候選 | 授權 | 適配度 | 結論 |
|---|---|---|---|
| **Boltz-2** | **MIT(可商用)** | 複合物結構 + ipTM,MIT | ✅ **採用** |
| AlphaFold3 | 權重非商業 | 準確度標竿,但授權卡死 | ❌ 排除 |
| AlphaPulldown2 | — | 成熟 turnkey,但後端是 AF | ❌ 後端授權問題 |
| AF_Cache | — | 解 MSA 瓶頸,但 AF 後端 | ❌ 同上 |

**因為選了 Boltz,漏斗兩段都是 Boltz-2**,只是取樣強度不同(見 §10)。

---

## 3. 整體架構:漏斗 + 雙分區

**兩個關鍵設計原則:**

1. **漏斗**:粗篩排序 → 只對頂部候選做精算,避免對幾萬對都跑高成本設定。
2. **雙分區解耦**:MSA(CPU/大 RAM 或 GPU-MMseqs2)和推論(GPU)拆成不同 SLURM 分區,
   透過 a3m 檔案交接。GPU 不該閒著等 MSA。

```
baits.fasta ┐
            ├─► [0] pair 展開 + unique 蛋白抽取
candidates.fasta ┘        │
                          ▼
              [1] MSA(per-protein 快取,a3m)   ← CPU+大RAM 或 一張 L40S 跑 MMseqs2-GPU
                          │  (檔案交接)
                          ▼
              [2] Boltz-2(結構 + ipTM,跳過 affinity) ← GPU array,一卡一對
                          │
                          ▼
              [3] AlphaJudge(抽 ipTM/pDockQ/PAE → CSV)  ← 輕量 CPU
                          │
                          ▼
              [4] 校準閾值(在已知正/負對上定 cutoff)   ← 手動,一次性
```

---

## 4. Pipeline 各階段詳解

每階段:**算什麼 / 主要算力 / 輸入 → 輸出**。

### [0] Pair 展開(膠水腳本)
- **算什麼**:把 baits × candidates 展開成 pair 清單;抽出所有 unique 蛋白;每對寫一個指向快取 a3m 的 Boltz YAML。
- **算力**:可忽略。
- **I/O**:兩個 FASTA 清單 → unique 蛋白 FASTA + 每對一個 YAML。
- **註**:這就是「Boltz 版 AlphaPulldown」缺的那段膠水,約一天腳本工作量。

### [1] MSA 生成(MMseqs2 引擎 + ColabFold 編排)
- **算什麼**:對每個 unique 蛋白搜同源序列並對齊,產出 unpaired a3m(複合物再選配 paired)。這是把「一條序列」變成「一疊演化證據」。
- **怎麼算**(`colabfold_search` 內部依序呼叫 `mmseqs` 子命令):
  1. `createdb` — query 轉 MMseqs2 格式
  2. `search` vs **UniRef30**,3 輪迭代 profile 搜尋;搜共識序列(~29.3M)而非完整 UniRef100(~277.5M)→ ~10× 加速。每輪內部:prefilter(k-mer / GPU ungapped)→ ungapped 對齊 → gapped(Smith-Waterman)
  3. `expandaln` — 把命中的聚類代表展開成成員序列
  4. 多樣性過濾 — 修剪成多樣但不冗餘(~30 條夠多樣的序列往往就夠)
  5. (可選)`search` vs BFD/MGnify 或 ColabFoldDB 環境庫 ← **condensed 開關**
  6. `result2msa` + `unpackdb` — 輸出每 query 一個 a3m
- **算力**:**CPU 密集 + 巨量 RAM/DB**(或改 MMseqs2-GPU 用一張 L40S)。本質 I/O 受限,不是純算力受限。**整條鏈唯一大量吃 RAM 的階段。**
- **I/O**:unique 蛋白 FASTA → `unpaired/*.a3m`(+ `paired/*.a3m`)。
- **關鍵**:**per-protein 快取** — 40,000 對背後只有幾百個 unique 蛋白,搜幾百次不是幾萬次;算完存起來永遠重用。

### [2] Boltz-2(結構 + confidence)
- **算什麼**:(a) trunk 從兩條序列 + 其 MSA 算成對表徵 `z`;(b) diffusion 模組去噪成 3D 座標;(c) confidence 模組吐 **ipTM / PAE / pLDDT**。
- **怎麼算**:trunk 三角運算跑在 bfloat16 + trifast kernel;結構是擴散去噪(`sampling_steps` / `diffusion_samples` 控制);ipTM 來自 confidence head。
- **算力**:**GPU 密集,一對一張卡**。L40S(48GB)跳過 affinity 後約用 11GB。VRAM 隨總 token 數約 N² 成長。每對數秒~數分鐘。**embarrassingly parallel,靠卡數堆吞吐。**
- **I/O**:YAML(兩序列 + 快取 a3m 路徑 + 取樣參數)→ `.cif` + confidence JSON(含 ipTM)。

### [3] AlphaJudge(評分與聚合)
- **算什麼**:讀每對 Boltz 輸出,抽 ipTM / pDockQ / PAE + 物理界面特徵(接觸、界面面積、能量、靜電),整併成全對 CSV。
- **重點**:**已支援解析 Boltz-2 輸出**,所以「Boltz 輸出 → ipTM 表」這段不用自己寫。
- **算力**:輕量 CPU。
- **I/O**:Boltz 預測資料夾 → 排序用 CSV(+ 驗證 PDF)。

### [4] 校準(手動,不是工具)
- 在已知正/負對上定 ipTM(或 pDockQ)閾值,再套到幾萬對。**沒有現成工具,但必做** — 否則有分數卻不知 cutoff 畫哪。

---

## 5. 關鍵技術決策與理由

### 5.1 MSA 按蛋白快取,不按對算
- MSA 只跟單一序列有關 → 每個 unique 蛋白算一次即可。
- N 個蛋白 all-vs-all → ~N²/2 對,但只有 N 個 unique 蛋白。200×200 = 40,000 對但只有 400 蛋白 → **400 次搜尋 vs 40,000,差 100×**。
- 昂貴的同源搜尋是 per-protein;paired 的配對只是拿快取的 per-protein MSA 做便宜的 taxonomy 後處理。

### 5.2 跳過 affinity,用 ipTM
- Boltz affinity head 是**蛋白–配體(小分子)**訓練的;新版還禁止對 ≥128 原子的配體算 affinity — 蛋白當「配體」遠超上限。
- 有人 fine-tune 的 Boltz-2-PPI 反而**輸給序列法模型**。
- 實作上:YAML **不寫 `properties: affinity` 區塊**,affinity 模組就不執行,順便省 ~7–8GB VRAM。

### 5.3 MSA 是什麼 / 為何需要
- Multiple Sequence Alignment:搜同源序列對齊成疊。模型真正「讀」的是這疊演化資訊,不只單條序列。
- 為何有用:**共演化** — 3D 上接觸的兩個位置,突變會互相補償 → MSA 兩欄相關 → 空間接觸 → 結構約束。

### 5.4 Condensed DB(對付 RAM 天花板)
- ColabFold 是三層可選庫:**UniRef30**(小)/ **BFD/MGnify**(中)/ **ColabFoldDB**(環境庫巨獸,209M reps / 738M members)。
- **Condensed 配方**:只用 UniRef30(+ 視情況 BFD/MGnify),**跳過 ColabFoldDB**;對已表徵蛋白(細菌受體、已知 RBP)宏基因組庫增益邊際。
- 其他省 RAM 手段:刪 `.idx` 檔 → 即時建索引(128GB 可跑,不需 768GB);`--max-seqs` 設淺(粗篩夠用);MMseqs2-GPU 把記憶體從每殘基 ~7 bytes 壓到 1 byte。

### 5.5 Paired vs Unpaired MSA — 先驗證再決定
- **Unpaired 必做**(每鏈各自的演化證據)。
- **Paired 對跨物種(噬菌體 RBP × 宿主受體)前提站不住** — 共演化是拮抗式軍備競賽,且無乾淨的大規模配對基因組庫。很可能貢獻甚微。
- `colabfold_search` 跑複合物時**兩者順便一起產出**,成本不是問題;問題是「要不要餵給 Boltz」。
- **⚠️ 待驗證實驗(見 §12)**:在已知正對上跑 unpaired-only vs unpaired+paired,比 ipTM。沒差就全走 unpaired,省掉配對的坑。

### 5.6 MMseqs2-GPU(用一張 L40S 跑 MSA)
- ColabFold 支援 GPU 加速搜尋:比 CPU 版 ~1.65× 快,MSA 生成本身 ~5.4× 快,記憶體大降、可從 host RAM 串流。
- **策略**:撥一張 L40S 專跑 MSA,而不是搶胖 RAM 的 CPU 節點。
- **兩個提醒**:(1) GPU(ungapped)與 CPU(k-mer)prefilter 產出**不同的 MSA**,下游 ipTM 有差 → **選一種全程統一,別混**;(2) DB 要建成 GPU 相容格式。

---

## 6. 效能與加速:真正的瓶頸

**快取後,MMseqs2 不再是瓶頸。** 對比:
- MSA:N 次、一次性、可平行、算完永久存 → 十幾 CPU-小時。
- Boltz:**N² 次、每對都要重跑** → 數百 GPU-小時。

**為何 Boltz 無法像 MSA 那樣快取掉**:trunk 算的是「兩鏈聯合」的 pairwise `z`,換 partner 就全重算。計算量集中在唯一無法攤銷的地方。

**最耗算力的具體組件**:trunk 的**三角運算(triangle attention/multiplication)**,對 token 數是 **O(N³)**,再乘 recycling 次數。

**加速優先序(按槓桿):**
1. **砍取樣(最大、免費)**:粗篩 recycling 3→1、sampling_steps 20→~10、diffusion_samples=1。直接砍 trunk 重跑次數。
2. **建單體別建三聚體(N³ 槓桿)**:三角運算 O(N³),token ×3 → 計算 ~×27。粗篩用單體 RBP。
3. **cuEquivariance kernel**:疊在 bfloat16+trifast 上,同精度再 ~1.75×(FP32→cuEq BF16 可到 2.5×)。L40S(Ada)支援。
4. **全卡並行攤 N²**:前三項降「每對成本」,但 N² 次數本身砍不掉(若真要全跑)。SLURM array 一卡一對攤到所有 L40S — 這才是壓 wall-clock 的辦法。

**砍不掉的現實**:真要全部 N² 對,次數是本質的,只能靠並行壓時間。減次數唯一辦法是 Boltz 前加序列法預篩 — 但幾萬對不值得,直接全跑更省事。

---

## 7. 硬體:L40S 注意事項

- **官方支援**:L40S 在 Boltz-2 NIM 測試清單;Ada 架構 → **bfloat16 + trifast 原生可用**(不像 V100 要關 trifast)。
- **實測(L40S)**:結構預測 ~11GB、affinity ~7–8GB;每個蛋白–配體預測 ~40–60s;16 卡 ~1000 預測/小時。跳過 affinity 後只需 ~11GB。
- **無 NVLink 不影響**:工作是 embarrassingly parallel,一卡一對,永遠不需多卡跑單一預測。
- **⚠️ 唯一紅線 = VRAM**:48GB 是 Boltz-2 門檻底線,VRAM 隨 token 數約 N²。逼近天花板的情境:
  - **三聚體 RBP**(如 T7 gp17 這類尾絲,功能單位是三聚體)→ token ×3。
  - 大型/多結構域受體或受體複合物。
  - 參考:L40S 低記憶體版跑 2527 殘基 ~12 min、2971 殘基 ~21 min。撞牆可用 **LMI4Boltz**(token 上限再拉 ~66.7%)。
- **多 claim 卡不會給單一預測更多 VRAM**(無跨卡切分)。要吞吐就用單卡 array task 攤開;過度 claim 會拉長自己排隊、傷 fairshare。

---

## 8. 已知的坑(gotchas)

- **Boltz 靜默空 MSA**:若 a3m 第一條序列不是 query 本身,Boltz 會**靜默當空 MSA 跑**,不報錯只給爛結構。批次腳本**務必驗證每個 a3m 首行 = query**。
- **Steering 旗標**:Boltz-2 把旗標改成 `--use_steering`,且**預設可能不開**(Boltz-1 預設開)。確認你這版預設值。
- **GPU/CPU MSA 不一致**:見 §5.6,全程統一一種。
- **公開 MMseqs2 API 會限流/卡住**:幾萬 unique 蛋白**一定本地跑**,別用 `--use_msa_server` 打公開 server。
- **本地結果 ≠ server 結果**:DB 版本/參數差異 → 分數不能假設對得上論文,cutoff 在自己環境重新校準。
- **DB 版本一致性**:整個專案鎖同一版 UniRef30/envdb。
- **I/O**:DB 放節點本地 NVMe,別放慢的共享網路儲存(Lustre/GPFS)。

---

## 9. 現成工具地景

- **AlphaPulldown / AlphaPulldown2**:就是「兩 array → ipTM 表」的成熟 CLI(pulldown / all-vs-all 模式、CPU/GPU 分段、Snakemake、續傳)。**但後端是 AlphaFold** → 授權對我們不乾淨。
- **AlphaFastPPi**:AlphaPulldown 的減取樣 wrapper(5× 快)。AF 後端。
- **AF_Cache**:Nextflow + MSA 快取。AF 後端。
- **OmniFold**:容器化跑 AF3/Chai-1/Boltz-2 ensemble。可設 Boltz-only,但要確認它有無跨對去重 MSA。
- **AlphaJudge**(Kosinski lab):評分/聚合,**已支援 Boltz-2 輸出** → 直接當 §[3]。
- **Boltz 官方 API + SDK**(很新,含 Claude Code 整合)/ **Tamarind、Rowan、BioLM**:託管、可規模化,但**序列外流第三方** → 商業化/機密性顧慮。

**結論**:免費+本地+Boltz 後端的 turnkey 全對篩選器目前是空缺。務實解 = **AlphaPulldown 的設計 + `boltz predict` + AlphaJudge**,中間補一段展開 pair 的膠水。

---

## 10. 調參速查表(漏斗兩段)

| 參數 | 粗篩(全部幾萬對) | 精算(排序後前幾 %) |
|---|---|---|
| `recycling_steps` | 1 | 3–6 |
| `sampling_steps` | ~10 | 50+ |
| `diffusion_samples` | 1 | 3–5 |
| affinity | 關(不寫區塊) | 關 |
| MSA 深度(`--max-seqs`) | 淺 | 完整 |
| DB | condensed(UniRef30) | 完整(+envdb) |
| RBP 建模 | 單體 | 視需要三聚體 |
| 分數 | ipTM | ipTM + 最佳結構 |

---

## 11. 命令與資料流骨架(帶進 Claude Code 細修)

### 資料流
```
FASTA → colabfold_search(內部 mmseqs: createdb→search×3→expandaln→filter→result2msa→unpackdb)
      → unpaired/*.a3m (+ paired/*.a3m)
      → Boltz YAML 的 MSA_PATH 指向 a3m(檔案交接)
      → boltz predict → *.cif + confidence JSON
      → alphajudge → ipTM CSV
```

### 一次性:建庫
```bash
# 只建 UniRef30(condensed);要 envdb 再另下載
setup_databases.sh /path/to/dbs
```

### 階段 1:MSA(CPU 或 GPU-MMseqs2 分區),per-protein 快取
```bash
colabfold_search \
    unique_proteins.fasta \
    /path/to/dbs \
    msa_out/ \
    --mmseqs "$(which mmseqs)" \
    --db-load-mode 2          # index 已在記憶體時省載入
    # condensed:db 目錄只含 UniRef30,跳過環境庫
    # GPU:改用 MMseqs2-GPU 相容 db 與參數
# ⚠️ 之後驗證每個 a3m 首行 == query 序列
```

### 階段 2:Boltz(GPU array,一卡一對,跳過 affinity)
```bash
# 每對一個 YAML,不含 affinity 區塊,MSA 指向快取 a3m
# 粗篩範例參數:
boltz predict pair.yaml \
    --recycling_steps 1 \
    --sampling_steps 10 \
    --diffusion_samples 1 \
    --output_format mmcif
    # 確認 --use_steering 的預設與需求
```

### SLURM array(單卡一 task,限並發當好公民)
```bash
#SBATCH --array=1-40000%20      # 一次最多 20 個並發
#SBATCH --gres=gpu:1            # 一 task 一張卡
#SBATCH --partition=<gpu_part>
# 依 SLURM_ARRAY_TASK_ID 取第 N 個 YAML 跑 boltz predict
```

### 階段 3:評分聚合
```bash
alphajudge out_dir/predictions/ -r -o iptm_summary.csv --models_to_analyse all
```

---

## 12. 待辦與待驗證實驗(TODO)

- [ ] **[實驗] paired 到底有沒有用**:準備一組已知正對,跑 unpaired-only vs unpaired+paired,比 ipTM。沒差就全走 unpaired。
- [ ] **[實驗] cutoff 校準**:準備已知正/負對,畫 ipTM(和 pDockQ)分布,定閾值。**跑幾萬對前必做。**
- [ ] **[決策] RBP 建單體 vs 三聚體**:估 L40S 48GB 下的安全 token/殘基上限,決定粗篩用哪個(直接影響 VRAM 與 N³ 成本)。
- [ ] **[驗證] a3m 首行 == query** 的自動檢查加進膠水腳本。
- [ ] **[決策] MSA 走 CPU 還是 GPU-MMseqs2**:選一種,全程統一。
- [ ] **[基準] 單對計時**:粗篩設定下量一對的 wall-clock 與 VRAM,回推全批 GPU-小時與並發數。
- [ ] **[膠水] pair 展開器**:兩 array → pair 清單 + unique 蛋白抽取 + 每對 YAML(指向快取 a3m)。
- [ ] **[編排] 選 Snakemake 或 Nextflow** 當雙分區薄編排層(CPU-MSA → GPU-Boltz → AlphaJudge)。
- [ ] **[環境] laguna 上確認**:MMseqs2-GPU 可否裝、cuEquivariance 可否裝、DB 放本地 NVMe。

---

## 13. 參考資料

- Boltz 官方:https://boltz.bio/boltz2 ・ 論文:https://jeremywohlwend.com/assets/boltz2.pdf
- Boltz repo(含 MSA/YAML 用法、issues):https://github.com/jwohlwend/boltz
- Boltz-2 FAQ(訓練/誤報率):https://rowansci.com/blog/boltz2-faq
- AlphaPulldown2:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11937959/
- AlphaFastPPi:https://www.biorxiv.org/content/10.1101/2024.06.07.597882
- AlphaJudge(支援 Boltz-2 評分):https://github.com/KosinskiLab/AlphaJudge
- ColabFold 論文:https://www.nature.com/articles/s41592-022-01488-1
- ColabFold DB 下載/RAM 說明:https://colabfold.mmseqs.com/
- MMseqs2:https://github.com/soedinglab/MMseqs2
- MSA 生成/配對深入:https://neurosnap.ai/blog/post/mmseqs2-deep-understanding-of-msa-generation-optimization/6711802c8bedccdda9e14fe4
- DiffPALM(配對優化):https://arxiv.org/pdf/2308.07136

---

*本文件為設計摘要,非最終規格。§12 的實驗結果會回頭修正 §5.5、§7、§10 的決策。*
