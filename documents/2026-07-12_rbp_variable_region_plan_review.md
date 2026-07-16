# RBP 變異區 → 結合特異性 計劃審視(文獻 + 科學嚴謹性)

> **用途**:在投入 coding 之前,對「用 MGnify 高相似序列 + MSA 統計找 RBP 保守/變異區,再連結到 amino-acid level 的結合特異性」這個計劃,做前人文獻盤點 + 科學邏輯壓力測試。
> **結論先講**:核心生物學前提**成立且文獻扎實**;但計劃裡有**一個中心方法學謬誤**(變異區 ≠ 特異性決定位)和**一個致命的資料斷點**(MGnify 序列沒有宿主/受體標註,無法從純序列跨到「結合什麼」的因果)。附一份修正後、仍具新穎性的版本。
> **語言**:中文為主,工具/術語保留英文。

---

## 0. 需要你先拍板的三個模糊點(先擺前面)

1. **這個分析的「查詢序列」是哪一條 RBP?** 是你已定序的 9-2-1 Φ8 的 tailspike/tail fiber(`code/0708_rbp_analysis/`,CDS_0015–0018),還是 literature database 裡的某群 Pseudomonas RBP?**兩者的可行性差很多**(見 §4)。
2. **最終「結合什麼」的 ground truth 從哪來?** 你要宣稱 amino-acid level 的因果,就必須有「這條 RBP 結合這個受體 / 這個宿主」的標籤來源。目前 repo 裡唯一能提供標籤的是 literature DB(Boeckaerts by-host、Moriniere by-receptor)+ 你的 OMP 分類(0620)。**MGnify 提供不了。**
3. **驗證這條腿要不要修?** 你的 co-fold ipTM 篩選(0703)ESMFold 版**對照組沒能分開陽/陰性 → 判定 non-informative**。純序列統計是相關性證據,要觸及「因果」必須靠結構或突變驗證——而這條腿現在是壞的。要不要先修(Boltz-2/AF-Multimer + 正確對照)?

---

## 1. 你的計劃拆解(我怎麼理解)

| 階段 | 你的描述 | 本質 |
|---|---|---|
| A | MGnify 找 100–500 個高相似序列(設 lower bound)→ 打包 aligned FASTA → 統計找 highly similar vs highly varying region | 描述性序列分析 |
| B | 分析原本的 phage 和宿主,找有意思的 pattern | 探索性關聯分析 |
| C | 用可靠 annotation 工具看不同 domain/region 在做什麼 → 理解 affinity 邏輯,細到 amino acid,知道什麼導致 bind / 不 bind | 想跨到機制/因果(你認為的學術創新點) |

---

## 2. 前人文獻:這件事別人做到哪(結論:概念不新,但你的應用切角可以新)

### 2.1 「保守骨架 + 高變遠端 tip」典範——**牢固成立**
RBP(tail fiber / tailspike)是「N 端保守錨定 + C 端/遠端高變、決定宿主特異性」的模組化結構,跨所有主要 RBP 類別都被結構生物學反覆證實:
- **Bartual et al. 2010, PNAS** — T4 長尾纖維 gp37 遠端 tip 結構。
- **Garcia-Doval & van Raaij 2012, PNAS** — T7 gp17,保守 stem + C 端 β-propeller tip 接觸 LPS。
- **Steinbacher et al. 1996/1997, PNAS / JMB** — P22 tailspike:保守 head-binding domain vs C 端 β-helix 上的 O-antigen 結合溝(定位到 Asp392/Asp395/Glu359)。
- **Trojet et al. 2011, GBE** — gp38 adhesin:**四段 hypervariable segments (HVSs)** 被保守 glycine-rich motifs 隔開——變異區概念最清楚的遺傳學陳述。
- **命名坑**:T4 本身遠端 tip 是 gp37,gp38 只是組裝 chaperone;「gp38 = adhesin」是 T2/T6 型親戚的情況。別搞混。

→ **你「RBP 有可辨識的保守 vs 變異區」這個前提是對的。**

### 2.2 特異性確實可細到胺基酸/loop——但目前是「改」不是「預測」
- **Meyer et al. 2012, Science** — λ 的 J 蛋白**四個點突變**就能新增利用 OmpF 受體。自然界胺基酸解析度的最強例子。
- **Yehl et al. 2019, Cell** — T3 gp17 尾纖維**四個遠端 loop(即 HRDRs,Host-Range-Determining Regions)**做定點隨機化("phagebodies"),改宿主範圍並抑制抗性。
- **Dunne et al. 2019, Cell Reports** — 結構導引把 Listeria phage RBP 的 head/neck/shoulder 子域互換,切換血清型特異性。
- **Ando et al. 2015, Cell Systems** — 整段 tail-fiber 模組互換,重導 E. coli phage 到 Yersinia/Klebsiella。

→ 胺基酸級的結合決定子**存在且可操作**。但文獻現況是**組合式篩選 / 改造**,**正向(從序列預測哪個 residue 給哪個宿主)仍不成熟**——這正是你想切入的縫隙,但也說明它「難」。

### 2.3 DGR:變異區作為「可程式化 cassette」的生物範例
- **Liu 2002, Science / Doulatov 2004, Nature** — Bordetella phage BPP-1 用反轉錄酶把 template repeat 抄進 mtd 的 variable repeat,腺嘌呤特異性突變,單一 VR 可產生 ~10¹³ 變體。
- **McMahon 2005, NSMB** — Mtd 的 C-type lectin fold 是耐突變的支架,把變異位點排成受體結合面。

→ 這是「一條 RBP 的一個變異區可被大規模多樣化、而保守核心不塌」的自然證明。對你理解「哪些位點是可變 cassette」很有參考價值。

### 2.4 用序列預測宿主(你 DB 的來源,也是你最直接的「前人」)
- **Boeckaerts 2021, Sci Rep** — RBP 序列 ML 預測宿主,identity <75% 時勝過 BLAST(PR-AUC 0.74–0.94)。
- **Boeckaerts 2022, Viruses (PhageRBPdetect)** — 你 0701 用的偵測器。
- **Boeckaerts 2024, Nat Commun (PhageHostLearn)** — RBP × Klebsiella K-locus 配對預測,strain level ROC-AUC ~0.82,有 wet-lab 驗證。
- **Krusche 2025, Cell Reports** — S. aureus phage,RBP 相似度 → WTA 醣基化特異性;很多 phage 帶**兩條** RBP,特異性不同。
- ⚠️ **"Moriniere" 這篇文獻查不到獨立出處**,可能是 Ghent Phage RBP DB 的資料貢獻者而非獨立論文。**正式引用前務必核實 author/year/DOI。**

### 2.5 主要 review(要引就引這幾篇)
Nobrega 2018 (Nat Rev Microbiol);de Jonge 2019 (Trends Microbiol);Dunne 2021 (Curr Opin Biotechnol,最貼近工程改造);Taslem Mourosi 2022 (IJMS)。

**§2 小結**:整個「找變異區 + 連結宿主特異性」的**大概念不新**——結構生物學 + Boeckaerts ML + 改造論文已鋪得很滿。你要主張創新,必須**收窄到具體、別人沒做的切角**(見 §6)。

---

## 3. 方法學核心謬誤:**「變異區 ≠ 特異性決定位」**(這是最重要的一點)

你計劃的隱含等式是「highly varying region = 決定結合的區域」。文獻對此很明確:**原始 column 變異度是特異性最弱的訊號之一。**

- **真正對應你目標的訊號不是「變異」,而是 SDP(Specificity-Determining Positions):在功能亞群 *內* 保守、亞群 *間* 不同的位點。** 它在全局 column 上往往只是「中度變異」,單純 Shannon entropy / JSD 看不到這種「被功能結構化的變異」。
- **高變 column 大多是中性漂變(drift),不是特異性選擇。** 不加區分地挑高變區 = 把雜訊當訊號。
- **反過來,強保守 residue 可能正是真正的結合接觸點**(因為要接觸受體保守部位而不變)。純挑變異區會把真正的接觸 residue 丟掉。
- **Capra & Singh 2007 自己的結果**:保守度預測催化/配體位點不錯,但**在蛋白–蛋白介面明顯較弱**——而 RBP–受體正是蛋白–蛋白(或蛋白–醣)介面。

**對應的正確方法階梯**(從你提的往文獻實際用的升級):
1. **保守度(相位感知)**:ConSurf / Rate4Site(比 raw entropy 好,因為校正了系譜非獨立性)。JSD(Capra & Singh 2007)。
2. **SDP 方法(真正對口)**:SDPpred(MI)、Sequence Harmony / multi-Harmony、S3det/Xdet(**S3det 可非監督地同時發現亞群與 SDP**,你若還不知道有幾群特異性,這個最合適)、GroupSim。Review:Chakraborty & Chakrabarti 2015。
3. **共演化 / covariation**:DCA(EVcouplings)、SCA(pySCA)、MSA Transformer——抓「成對」耦合 residue 與介面接觸,單 column 掃不到。
   - ⚠️ **DCA 很吃資料**:通常要**上千條有效(去冗餘後)序列**。你「100–500 條高相似」在單一 clade 下**嚴重不足**,couplings 會被系譜假訊號淹沒。

**但注意**:SDP 與共演化都**需要功能標籤(把序列分成 by-host / by-receptor 亞群)才能跑**。這把問題直接推到 §4 的資料斷點。

---

## 4. 致命資料斷點:MGnify 序列**沒有宿主/受體標註**

這是整個計劃邏輯上最脆的一環。

- **MGnify = 巨量(>24 億條)metagenome 預測蛋白,但**:
  - **無可靠宿主/來源生物歸屬**——metagenome contig 的來源菌通常未知。一條 MGnify RBP hit **不會告訴你它感染哪個菌**。
  - **片段化 / frameshift**:低覆蓋組裝常截斷基因,而**被截斷的往往正是決定特異性的變異 tip**。
  - **註解是同源轉移、非實驗驗證**;冗餘極高。
- **後果**:MGnify 能給你「這個 RBP 序列家族長什麼樣」,**給不了「這條 RBP 結合什麼」**。沒有標籤 → 跑不了 SDP(§3),只能跑最弱的純保守度 → 而純保守度對介面本就弱,且**是相關性,不是因果**。

**「100–500 高相似」這個設計本身還踩了統計最大雷**:
- 「高相似」+ 多半來自少數 clade = **系譜/取樣偏差把假保守度灌大**(共同祖先而非選擇),也讓共演化方法幻覺出耦合。這是你這個設計的**一階風險**。
- **緩解**:序列去冗餘 / reweighting(down-weight >X% identical)、用相位感知的 Rate4Site/ConSurf 而非 raw entropy、並**刻意納入更廣的多樣性而非只要「高相似」**。
- 先過**長度/覆蓋度過濾**再算,擋掉 metagenome 片段假訊號。

---

## 5. 因果宣稱的邊界:純序列統計到不了「什麼導致 bind」

你最終想要的「細到 amino acid,知道什麼導致 bind / 不 bind」是**因果宣稱**。要誠實地標清楚:

- 保守度 / SDP / 共演化分數都是**假設產生器(hypothesis generators)**。一個保守或耦合的 residue 只是**與**功能*相關*,不等於「突變它會改變結合」。
- **只有擾動能建立因果**:定點突變 + 結合/plaque assay、深度突變掃描(DMS),或**結構共摺疊**(把 residue 對到實際介面接觸)。
- 你 repo 裡**本來就有這條機制腿**——co-fold ipTM(0703)。這正是序列相關性分析的因果補件,也是你相對於「純 bioinformatics」論文的**獨特優勢**。
- **但這條腿現在是壞的**:ESMFold 版對照(3 陽 6 陰)沒分開 → non-informative。**先修好**(Boltz-2 或 AF-Multimer,配正確陽/陰對照,對膜蛋白只取 β-barrel、手動剔除與膜區衝突的預測——見文獻的 gp38/OMP loop 做法 PMC12032242),它才能當「因果驗證」用。

**收斂邏輯(這才是可發表的強度)**:一個 residue 若**同時**被(a)序列 SDP 標到、(b)結構共摺疊標為介面接觸、(c)理想上有一兩個突變體 plaque assay 佐證 → 才是三角驗證、接近因果的主張。單靠 §A 的 MSA 統計**遠不到**這個強度。

---

## 6. 修正後、仍有新穎性的版本(建議採納)

把計劃從「找變異 column」重寫成「**多亞群 SDP + 結構共摺疊 + 收斂驗證**」:

1. **標籤來源換掉**:用**有宿主/受體資訊**的來源建 RBP 亞群——你的 literature DB(Boeckaerts by-host、Moriniere by-receptor)+ 你的 OMP 分類(0620)+ INPHARED/RefSeq 的 host 欄位。**MGnify 只用來加深 MSA / 擴大結構搜尋空間,不用來指派宿主。**
2. **序列側**:對「同受體類 / 同宿主」亞群跑 **SDP(S3det/SDPpred/Sequence Harmony)**,不是挑高變 column。先去冗餘、相位校正、長度過濾。
3. **結構側**:先**修好 co-fold**(正確對照),對 RBP tip × 特定 Pseudomonas OMP β-barrel 共摺疊,取介面接觸 residue。醣類受體(LPS/CPS)則需 Boltz-2 的 affinity 模組 + 實驗,別信 AF3 的醣構型分數。
4. **收斂**:序列 SDP ∩ 結構介面 residue = 候選特異性決定子短名單。
5. **(iGEM 加分)** 挑 1–3 個候選做定點突變 + plaque/adsorption assay,把「相關」推向「因果」。哪怕只驗一兩個,論述強度天差地別。

**這樣的新穎點怎麼誠實地講**(避免 overclaim):
- ❌ 不是「我們發現了 amino-acid level 什麼導致結合」(這個層級別人已有 λ-J、phagebody)。
- ✅ 而是「我們對**無現成模型的 Pseudomonas phage RBP–OMP 系統**,建了一條**序列 SDP × 結構共摺疊 × 自產 phage 基因體/metagenome RBP 目錄**三方整合、並以小規模 wet-lab 收斂驗證的 pipeline」。切角具體、資料是你自己的、系統沒人做過——這才站得住。

---

## 7. 關於階段 B(phage + 宿主 pattern):可做,但要防混淆

- 探索性關聯分析對「產生假設」有價值,值得做。
- **主要陷阱 = 系譜混淆(Simpson's paradox 家族)**:phage 彼此有親緣、宿主也有親緣,所以「RBP 越像 → 宿主越像」很可能**只是共同祖先驅動,不是 RBP 機制驅動**。要用系譜校正 / partial correlation,別把它當因果。
- 定位成**描述性 / 假設生成**,不要下因果結論。

---

## 8. 建議的執行順序 + Go/No-Go 檢查點

| 步驟 | 產出 | Go/No-Go |
|---|---|---|
| 0 | 拍板 §0 三個模糊點 | 標籤來源確定前不要開 code |
| 1 | 修 co-fold 對照(Boltz-2,3 陽性 + ≥6 陰性) | **陽陰分不開就不要往下用結構當因果** |
| 2 | 用有標籤來源建 RBP by-receptor 亞群 + 去冗餘 MSA | 每亞群 ≥ ~20–30 條有效序列才有統計力 |
| 3 | SDP 分析(S3det 起手) | SDP 是否落在已知變異 tip 區?(sanity check) |
| 4 | co-fold 交集介面 residue | SDP ∩ 介面 有無交集 |
| 5 | 1–3 個突變體 wet-lab | 驗證/證偽 |

MGnify 的角色**限縮**在:步驟 2 加深 MSA、步驟 1 擴大結構搜尋空間。不承擔宿主指派。

---

## 9. 一句話總評

**生物學前提對、方法方向可行,但不能照原樣做**:把「挑高變區」換成「SDP + 共演化」,把「MGnify 當資料主幹」換成「有標籤來源當主幹、MGnify 只加深 MSA」,並且**先修好結構這條因果腿**。純 §A 的 MSA 統計是相關性、且踩系譜偏差雷,**單獨無法支撐你想要的胺基酸級因果宣稱**。修正後版本(§6)仍然新穎且是你獨有資料能撐起的——但創新點要誠實收窄到「Pseudomonas 系統 + 三方整合 + 小驗證」,而不是「發現了結合的胺基酸密碼」。

---

*Log*
- 2026-07-12 建立。文獻由 4 個並行 agent 掃(結構生物學 / MSA 方法學 / MGnify+host prediction / repo 盤點);引用多數已核實,標 ⚠️ 者(Moriniere、Müller Sf6 2008、部分頁碼)正式引用前需再核。advisor 工具本次不可用,以 scientific-critical-thinking 框架自審。
- 待辦:Alex 拍板 §0 三問後,再決定是否開 coding。
