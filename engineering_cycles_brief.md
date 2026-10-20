# Engineering Cycles — 現況簡介與圖片需求

給 lab repo 原生 session 的交接文件。
wiki 頁面：`https://2026.igem.wiki/claremont-ca/engineering`
原始碼：`claremont-ca/wiki/pages/engineering.html`

這一頁是 **Silver 判準 1（Engineering Success）的 standard URL**，同時餵養
Best Wiki 和 Best Model 的評分。判準本身只要求走完一輪 DBTL，我們有四輪，
所以**文字已經達標，現在是在加強說服力**。

---

## 一、四個循環在論證什麼

每一輪都有完整的 Design / Build / Test / Learn 四個小標。

### Cycle 1 — Computational RBP–receptor screen
**假設**：Φ8 靠 RBP 和宿主表面蛋白的蛋白質對蛋白質交互作用辨識宿主。
**做了什麼**：441 個候選表面受體收斂成 178 個簇；交叉比對 PharBP 的 6,376 筆
宿主記錄，選出 *P. putida* KT2440 當替代宿主；縮成 114 RBP × 63 受體 = 7,182 對。
光是讓摺疊工具跑起來就換了三個：ColabFold 被遠端 MSA 伺服器的速率限制擋死、
Boltz-2 在 L40S 的 CUDA 12.4 驅動上連撞四次（torch 版本、缺 CUDA runtime、
kernel 要 cuBLAS 12.5+、關掉 kernel 後 403 s/fold），最後落在 ESMFold。
**關鍵**：用**兩個不同工具各做一次對照閘門**。ESMFold 閘門的陽性 0.137 對打亂 0.136，
分數與長度相關 r = +0.58；ColabFold AF2 真實 MSA 閘門更糟，陽性全部 ≤ 0.31
而一個錯配對拿到 0.50，排序直接翻轉。
**結論**：跨界配對沒有 paired MSA，ipTM 回傳的是雜訊。這是方法的性質不是調參問題。
一次失敗是關於我們的 run，兩次獨立失敗是關於這個方法。
**圖：4 張，已完成。**

### Cycle 2 — Carbohydrate receptor hypothesis
**假設**：尾刺是作用在多醣上的酵素，所以受體是糖。
**做了什麼**：PhageRBPdetect v4（ESM-2 分類器）掃全部 80 個 Φ8 蛋白；
ColabFold 真實 MSA 模式折疊 8 個 RBP 候選（單序列模式 pLDDT 約 30，不堪用）；
用主鏈氫鍵的 rung period 判定摺疊，這個方法不需要結構資料庫。
**結論**：CDS_0011 信心 0.997、rung period 15–18，右手 β-helix；
CDS_0024 被 Pharokka 標成 hypothetical，信心 0.998、period 22–24，第二個解聚酶。
由此推出該比較的是 O-antigen 基因座，三株各帶互不同源的 cassette，
45 個直系同源簇只有 4 個三株共有。產生可否證預測：Φ8 不該在 Strain 1 或 3 上形成噬菌斑。
該預測已被 2026-07-04 的 18 宿主矩陣直接測試，10-10-2 與 8-10-2 對兩種溶液皆陰性，
方向吻合但因無對照而不宣稱確認。
**圖：3 張，已完成。**

### Cycle 3 — Functional validation
**設計理由**：取 CDS_0011 殘基 301–941。軸桿區 111–300 在不同模型間飄移，
三聚體本體 301–941 剛性一致（RMSD 0.44–0.99 Å），活性位點在本體內。
**做了什麼**：兩批 Twist 訂單共六個構建體，全部 pET-28a(+) N 端 His6。
第一批 CDS_0011 (305–941)、CDS_0010 (105–917)、CDS_0012 (117–477)；
第二批是 CDS_0012 的三個重建祖先 Node1 / Node40 / Node281，插入長度與構建體長度
與野生型完全相同，所以四者在 SDS-PAGE 上無法分辨。
**四輪測試**：9-15 無結論、9-29 CDS_0012 出現 IPTG 依賴的 40–43 kDa 條帶而
CDS_0011 在 72 kDa 沒東西、10-10 Ni-NTA 什麼都沒抓到、10-15 Bradford 歸一化。
**結論**：擋住這一輪的是一個對照而不是一個實驗。三次跑胶沒有一次有未轉化的
BL21(DE3) 泳道。另外兩個設計改動來自文獻而非我們的數據：誘導應該在 16–20 °C
16 小時（DepoCatalog 的 90 個蛋白沒有一個在 37 °C 誘導），以及平板 halo 測定
比 Coomassie 膠更靈敏，等乾淨的膠再做測定是順序錯了。
**圖：0 張。有兩張表（Table 2 構建體、Table 3 四輪測試）。**

### Cycle 4 — Let the bacteria tell us the receptor
**設計理由**：前三輪都從噬菌體那一側猜受體，這一輪反過來，讓宿主和噬菌體一起長，
留下活下來的再定序，變掉的東西就是候選。迴路裡沒有任何結構預測。
**做了什麼**：2026-07-07 從 9-2-1 與 9-6-2 的 1:1000 盤噬菌斑區內各挑三個菌落，
共六個；7-09 萃取 DNA；10-06 每個宿主的 R1 送 Plasmidsaurus 全基因組定序，
以既有親本組裝為參考。
**結論**：每個差異都拿回原始 reads 驗證，用親本的 Nanopore reads 和一組獨立的
Illumina reads 當兩條基線。只有一個突變通過過濾：Stealth 家族糖磷酸轉移酶的 F126L，
位在 30 kb 莢膜型多醣簇內。兩個 pick 的 O-antigen cassette 與 LPS core 都沒動。
答案與預測不符而那正是這樣做的意義：Cycle 2 說受體是糖，這一輪同意是糖但不同意是哪一種糖，
而兩者都能成立因為莢膜可以遮蔽底下完好的 O-antigen。
**已知缺口**：那些 pick 從未被表型確認為抗性，它們只是噬菌斑區內的菌落。
**圖：0 張。**

### 05 — What we would tell the next team
四條給後人的教訓，不是 DBTL 循環。**圖：0 張。**

---

## 二、我需要什麼

### 已確定要加的（不需要你找，但需要你確認理解無誤）

**8 個候選蛋白的摺疊分類表**，資料來源
`code/output/0712_phage_rbp_detect/structure/beta_helix_analysis.tsv`，
已用 `code/0713_espinoza_structural_mapping/cds_lookup.tsv` 換算成 PI 的編號：

| 蛋白（PI 編號） | Pharokka 標註 | rung period | 判定 |
|---|---|---|---|
| CDS_0024 | hypothetical protein | 23 | β-helix |
| CDS_0011 尾刺 | tail spike protein | 16–17 | β-helix |
| CDS_0012 | hypothetical protein | 34 | α-rich |
| CDS_0010 | tail protein | 7 | α-rich |
| CDS_0009 | tail fiber protein | 12 | β-other |
| CDS_0008 | internal virion protein | 7 | β-other |
| CDS_0007 | virion structural protein | 6 | α-fiber |

（我們舊的 CDS_0015 與 CDS_0016 合併成 PI 的 CDS_0011，period 分別是 17 和 16，
所以表上寫 16–17。）

這張表的用途是證明**這個方法會分辨而不是只會附和**。八個結構四種判定，
而且 CDS_0012 被判成 α-rich 不是 β-helix，與獨立的模板分析說它是 GH5 TIM barrel
一致，也就是**它的否定判斷也是對的**。

**請你確認**：上面的編號換算、period 數字、以及 CDS_0012 的 α-rich 判定與 GH5
的一致性，這三件事有沒有我理解錯的地方。

### 需要你找的東西

**請在 lab repo 既有的 figures 與 assets 裡，為 Cycle 3、Cycle 4 和第 05 節各找
最合適的圖。** 判斷標準是：

1. **每張圖要釘在它所論證的那一個步驟上**（Design / Build / Test / Learn），
   不是裝飾。我在 Cycle 1 和 2 就是這樣排的。
2. **優先選已經上傳到 `static.igem.wiki` 的**，其次是 repo 裡現成但未上傳的，
   最後才是需要重新產生的。
3. **避免與其他頁面重複使用同一張圖超過兩次**。目前 Results 有 9 張、
   Proof of Concept 有 4 張、Parts 有 3 張，Engineering 這邊若借用要改寫圖註成
   循環的角度。
4. **不要用 `fig-phage-genome-map.avif`**，那張把錯誤的標題燒死在圖裡了
   （寫著 62,416 bp, linear with 77 bp DTR，長度和拓撲都和現在的口徑不符）。
   要用的是裁過標題的 `fig-phage-genome-map-notitle-2026-10-19.avif`。

**具體缺口：**

| 位置 | 需要什麼樣的圖 | 我知道可能相關的素材 |
|---|---|---|
| Cycle 3 Design | 為什麼從殘基 305 切：軸桿飄移、本體剛性 | `fig-enzymatic-domains` 的 A 面板（已上傳，但 Cycle 2 已用過整張） |
| Cycle 3 Build | 六個構建體 | `fig-constructs-overview`（已上傳，Parts 在用）、`code/output/1018_construct_structures/panels/` 的單獨面板 |
| Cycle 3 Test | 四輪的胶 | 四張都在 Proof of Concept，重複貼可能不妥，請判斷 |
| Cycle 4 Design/Build | 抗性篩選的概念或流程 | 不確定有沒有 |
| Cycle 4 Test | read 層級驗證 | `fig-read-support-heatmap`、`fig-circos-parent-vs-mutants`（都已上傳，Results 在用） |
| 第 05 節 | 可有可無 | — |

**另外一個具體問題。** 上面那張摺疊分類表裡的八個蛋白，如果能配一張**並排對比不同
摺疊**的圖會非常有力，例如 β-helix 的長稜柱對上 α-fiber 對上 TIM barrel。
我在 repo 裡只找到 CDS_0010、CDS_0011、CDS_0012 加三個祖先的單獨渲染
（`code/output/1018_construct_structures/panels/`），沒看到 CDS_0007、0008、0009、0024
的單獨渲染。**請確認這類渲染是否存在，或是否能從既有的 PDB 產生。**

### 你回覆時請附上的資訊

對每一張你建議的圖：

- **repo 內的完整路徑**，或線上的完整 URL（如果已上傳）
- **像素尺寸**（我要寫進 `<img width height>` 以免版面跳動）
- **這張圖實際畫了什麼**，寫到我能據以寫出準確的 alt text 的程度
- **它應該放在哪一輪的哪一步**
- **數字出處**：圖上如果有數字，它來自哪個分析、哪一天、哪份輸出
- **任何已知的坑**：例如圖上燒死了過期的標題、座標系是舊的、
  或這張圖在別處已經被標為 obsolete

---

## 三、給另一個 session 的 prompt

> 我們在補 iGEM wiki 的 Engineering 頁面，那頁是 Silver 判準 Engineering Success
> 的 standard URL。頁面上有四個完整的 DBTL 循環，Cycle 1 和 Cycle 2 已經配好圖，
> Cycle 3、Cycle 4 和最後的 Lessons 一節目前零張圖。
>
> 四個循環分別是：
> 1. 計算篩選 RBP 對受體，跑了 7,182 對，被兩個不同工具的對照閘門推翻；
> 2. 改問糖，用 rung period 判定尾刺是 β-helix 解聚酶，再比較三株的 O-antigen cassette；
> 3. 功能驗證，把 CDS_0011 的 301–941 和另外五個構建體送 Twist 表達，四輪跑胶卡住；
> 4. 反過來讓抗性細菌自己說受體，R1 全基因組定序找到莢膜簇的 F126L。
>
> 請你在 lab repo 既有的 figures 和 assets 裡，為 Cycle 3、Cycle 4 和 Lessons
> 各找最合適的圖。每張圖必須能釘在某一個 Design / Build / Test / Learn 步驟上，
> 不要裝飾性的圖。優先已上傳到 static.igem.wiki 的，其次 repo 裡現成的。
>
> 另外請確認一件事：`code/output/0712_phage_rbp_detect/structure/beta_helix_analysis.tsv`
> 那張八個蛋白的摺疊判定表，如果要在 wiki 上並排展示不同摺疊的結構圖
> （β-helix 對上 α-fiber 對上 TIM barrel），repo 裡有沒有 CDS_0007、CDS_0008、
> CDS_0009、CDS_0024 的單獨結構渲染？只找到 1018_construct_structures/panels/ 裡的
> 六個表達構建體。
>
> 回覆每張圖時請附上：repo 完整路徑或線上 URL、像素尺寸、圖上實際畫了什麼
> （詳細到能寫 alt text）、該放哪一輪的哪一步、圖上數字的出處、以及任何已知的坑。

---

*Log — 2026-10-20：Cycle 1 與 2 已完成並上線，各 4 張和 3 張圖。
Cycle 3、4 與 Lessons 待補圖。*
