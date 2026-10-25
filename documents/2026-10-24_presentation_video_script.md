# Presentation Video — English narration script (v2)

故事見 [`2026-10-24_presentation_video_story.md`](2026-10-24_presentation_video_story.md)、
條件總表見 [`2026-10-24_presentation_video_plan.md`](2026-10-24_presentation_video_plan.md) §3B。

**v2 相對 v1 的改動**（依 Alex 在 PDF 上的批註 ＋ 重讀 wiki 的 Engineering 與 Human Practices 頁）：

1. **改成四個 DBTL cycle 講**（批註「Explain in cycles!」）。wiki 的 Engineering 頁本來就有四輪，
   v1 只講到兩輪半，而且把 Cycle 4 縮成一句話。
2. **補上 Human Practices**（批註「Where are all the human practice?」）。v1 完全沒有。
   現在有四段，全部來自 wiki HP 頁，而且**每一段都綁在它改變的那個決定上**。
3. **修正 Ni-NTA 那段 —— v1 寫錯了。** 真相是：10-13 請教 Prof. Tolstorukov → 他把問題從
   「為什麼沖提不出來」換成「到底有沒有表達」→ 10-19 anti-His dot blot → Node281 flow-through
   是陰性對照的 **2.9×**。**蛋白有表達，是管柱沒抓住。** 這是全專案最強的 HP→結果鏈。
4. **修正「預測尚未驗證」** —— 其實 2026-07-04 的 18 宿主矩陣測過了，方向吻合，但沒有對照所以不宣稱確認。
5. 開場加「我們是誰、這支片要講什麼」。
6. 採樣地點改為 **California Botanic Garden**；噬菌體基因體組裝改記為團隊。
7. 解釋什麼是 sugar coat；把第一幕的預測語氣放軟。
8. 補上實作細節（ColabFold / Boltz-2 / ESMFold、Laguna、PhageRBPdetect）。
9. 不再解釋「什麼是對照組」；Cycle 1 改成「先覺得不對勁 → 才做對照 → 找到真正的問題」。
10. 語氣整體重寫，減少對仗句與格言式收尾。

---

## ⚠️ 兩件要先決定的事

**(1) 植物園的訪談片段。** wiki 的 HP 頁寫著，我們在錄音裡對 Ashley Armstrong 和 James Manifold
說過**會把片段剪進這支 presentation video**，他們同意了。那是一個已經做出的承諾。
「v1 不要真人出鏡」指的是隊員，但這是利害關係人素材，而且我們答應過。
**建議至少放兩段共 20 秒。** 如果這版不放，要是有意識地決定，不要是忘記。

**(2) 長度。** 本版比 v1 長。130 wpm 會超過 15:00 硬上限，**必須用 140 wpm**，或照文末建議刪。

---

## OPENING

> 🎬 隊徽 → 隊員合照（靜照，不算真人出鏡）→ 片名。

> We're iGEM Claremont-CA, a first-year team in California. This is Phagenomics.
>
> Our question is what decides which bacteria a phage can kill. We went at it four times this season. Three of those attempts failed, and the failures are the useful part — so that's how this video is organised.
>
> Our project is about one question: what decides which bacteria a given phage can kill? We went after that question four times over the season. Three of those attempts failed, and the failures turned out to be the most useful thing we have — so this video is built around them rather than around a result.

**67 字**

---

## ACT I — THE BOTTLENECK

> 🎬 幕卡：`ACT I — THE BOTTLENECK` ／ *Why one phage only kills one host*

### I.1 問題

> 🎬 promo 的 plaque assay 動畫 → 同一滴滴到另外兩株，什麼都沒發生。

> A drop of phage goes onto a lawn of bacteria, and a few hours later there's a clear circle where the bacteria used to be. Move the same drop to the next plate and nothing happens.
>
> Same phage, different strain. Phages are fussy, and that fussiness is the bottleneck for using them as medicine: you need one that matches the strain in front of you, and usually there isn't one.

**80 字**

### I.2 吸附與糖衣

> 🎬 **Alex 批註要的圖**：細菌剖面 —— 細胞膜 → 細胞壁 → O-antigen → 莢膜。
> 標出「噬菌體最先碰到的是哪一層」。

> It gets decided at the first step, before any DNA moves: the phage has to recognise the outside of the cell and stick to it.
>
> And many bacteria aren't presenting a bare protein surface. They're wrapped in sugar — long chains called the O-antigen, and above that, in some species, a capsule. The first thing a phage touches is a forest of sugar.

**95 字**

### I.3 這個專案從哪來

> 🎬 HP 頁 Fig 1：團隊與 Prof. Libeskind-Hadas 的合照。
> 畫面標 `Prof. Ran Libeskind-Hadas, CMC — early conversation`

> One thing belongs at the start, because it's why half this project exists.
>
> Early on, Professor Ran Libeskind-Hadas at Claremont McKenna suggested reconstructing an ancestral phage — a whole organism, inferred from its relatives.
>
> We couldn't build one. But scale that down to a single enzyme and you can order it from a synthesis company. That is what this project became.

**120 字**

### I.4 我們的系統與第一條線索

> 🎬 California Botanic Garden 採樣照 → 三株細菌基因體 → Φ8 基因體圖 → 三套 O-antigen cassette 並排。
> 畫面標 `California Botanic Garden · 2026-05-19`、MRA doi、`hypothesis`

> Our soil came from the California Botanic Garden in May. Out of it we got three distinct strains of *Pseudomonas* and a phage, Phi-8, that infects exactly one of them. The bacterial genomes are published; our team assembled and annotated the phage.
>
> Then we lined the three strains up at the locus that builds their sugar coat. Same position, same flanking gene — and inside, three cassettes with no homology to each other.
>
> Three strains, three different sugar coats, one phage that kills one of them. So our first hypothesis: the sugar coat might be one of the main things setting what Phi-8 can attack.

**147 字**

---

## ACT II — CYCLE 1: THE WRONG QUESTION

> 🎬 幕卡：`CYCLE 1 — THE WRONG QUESTION`
> 之後四輪都用同一條 DBTL 進度條，當前步驟亮起。這是「explain in cycles」的視覺骨架。

### II.1 Design

> 🎬 DBTL 條，`DESIGN` 亮。鎖與鑰匙示意。

> But that isn't the hypothesis we tested first.
>
> The textbook picture of attachment is a receptor-binding protein on the tail meeting a protein on the bacterial surface. Lock and key. If that's what you assume, the obvious move is to work out which binding protein fits which receptor.
>
> If we'd known the receptor was a sugar we'd never have run this. We thought it was a protein, so we went looking for a protein.

**98 字**

### II.2 Build

> 🎬 `BUILD` 亮。441 → 178 → 114 × 63 = 7,182 的漏斗。右側列三個工具與各自撞牆的原因。
> 畫面標 `Laguna HPC · L40S`

> Four hundred and forty-one candidate receptors, clustered and narrowed to a hundred and fourteen binding proteins against sixty-three receptors — seven thousand, one hundred and eighty-two pairs, each folded as a complex on our university's GPU cluster and ranked by the interface score.
>
> Getting it to run took three tools — ColabFold throttled by its alignment server, Boltz-2 blocked by the cluster's CUDA version — and we ended up on ESMFold because it was the one that ran.

**120 字**

### II.3 Test

> 🎬 `TEST` 亮。先放「排名看起來很合理」的熱圖，再切對照組圖。
> **0.137 和 0.136 要大，停在畫面上。**

> And we got a ranking. It looked fine — which is the trouble with this kind of output. It always looks fine.
>
> What made us uneasy was that the scores tracked protein length more than anything else. So we ran the method against pairs where the answer was already known — complexes solved experimentally, against the same receptors shuffled into nonsense.
>
> T5's pb-five with FhuA, a real co-crystallised complex, scored zero point one three seven. The same receptor shuffled scored zero point one three six.
>
> We assumed that was the tool, so we rebuilt it with real evolutionary alignments. It got worse: a deliberately mismatched pair came out at zero point five, above every genuine binder.

**146 字**

### II.4 Learn

> 🎬 `LEARN` 亮。兩條信心柱（打亂後左邊 0.55→0.17，右邊不動）→ paired MSA 兩個永不相交的圈。

> Two tools, two control gates, both failed. One failure is about your run; two independent failures are about the method.
>
> These models report two confidences: one for the shape of the molecule, one for how two molecules sit together. When we shuffled a sequence, the shape confidence collapsed from zero point five five to zero point one seven — the model could tell it was nonsense. But the interface number barely moved. It had never been reading an interface at all.
>
> The reason is that these models don't simulate two proteins touching. They read evolution — looking across thousands of species for positions that change in step. If a residue on one side mutates and one on the other mutates to match, those two are probably in contact.
>
> That only exists if the two proteins have been inherited together, in one genome, for a long time. A phage protein's relatives are in other phages; a bacterial protein's are in other bacteria. They're never in the same genome, so the record of that interface doesn't exist. Not hidden — never written.
>
> So this was never a result about our proteins. It's a property of the method for any phage-and-host pair, and more compute doesn't help. Ten control folds decided the fate of seven thousand, and we never ran the real screen.

**264 字**

---

## ACT III — CYCLE 2: ASK THE PROTEIN WHAT IT IS

> 🎬 幕卡：`CYCLE 2 — ASK THE PROTEIN WHAT IT IS`

### III.1 Design → Build

> 🎬 PhageRBPdetect 掃 80 個蛋白 → 8 個候選 → rung period 示意（β-helix 的階梯間距）
> 畫面標 `PhageRBPdetect v4 (ESM-2), open source`

> If we couldn't ask what the tail spike binds, we could ask what it is.
>
> We ran an open-source classifier across all eighty Phi-8 proteins, folded the eight candidates, and classified the folds by the spacing of their backbone hydrogen bonds — which needs no structure database at all.

**79 字**

### III.2 Test → Learn

> 🎬 八個蛋白的摺疊分類表，四種判定。**強調這個方法會分辨，不是只會附和我們**
> （CDS_0012 被判 α-rich，與它是 GH5 TIM barrel 一致）。然後 β-helix 渲染圖 ＋ 切糖動畫。
> 畫面標 `CDS 11 · rung period 16–17 · confidence 0.997`

> Eight proteins, four different verdicts — so the method discriminates rather than agreeing with us. CDS 11, the tail spike, came back a right-handed beta-helix: a long triangular prism. And CDS 24, which the annotation had written off as hypothetical, came back as a second one.
>
> That fold is a signature. Enzymes that chew through long sugar chains look like this, because a sugar chain is a thread and you need something that holds it straight while you cut. You can recognise a wood plane by its shape without being told what it cuts.
>
> So the tail spike isn't a key. It's a blade — and the lock we'd spent months looking for doesn't exist.
>
> That reading arrived from two directions at once: our classifier flagged it as a depolymerase, and our PI reached the same conclusion from his own structural search. Between us we turned it into a hypothesis.

**181 字**

### III.3 假說

> 🎬 一句話假說框，白底，停久一點。
> 畫面標 `Hypothesis — developed jointly with Prof. J. Cesar Ignacio Espinoza`

> In bacteria that wrap themselves in sugar, the ceiling on host range is set by what the depolymerase can digest — not by which protein the tail binds. And the narrow specificity we see now is a narrowed-down version of something broader further back.
>
> That tells you what to measure — substrate range, not binding — and where to look for the broader version: back up the tree.

**76 字**

---

## ACT IV — CYCLE 3: BUILD THE ENZYMES

> 🎬 幕卡：`CYCLE 3 — BUILD THE ENZYMES`

### IV.1 Design → Build

> 🎬 CDS_0011 軸桿 vs 本體的剛性比較 → 六個建構體 → 系統發生樹往回合併 → 三個節點
> 畫面標 `ASR executed by Prof. Espinoza, on sequences prepared by the team`

> Two enzymes sit in the tail module: CDS 11, the beta-helix, and next to it CDS 12, a glycoside hydrolase. CDS 10 is still unknown, so we expressed that one too.
>
> For the tail spike we took residues three-oh-five to nine-four-one, because the shaft drifts between models while the body stays rigid.
>
> Then the ancestors — the part that came out of that first conversation. We worked out the direction with our PI; he ran the tree and the reconstruction on sequences we prepared.
>
> We picked three nodes. Six constructs in all, His-tagged, from Twist. The ancestors are exactly the same length as the wild type, which makes them indistinguishable on a gel — we should have thought about that before ordering.

**192 字**

### IV.2 Test

> 🎬 四輪測試時間軸 → 9-29 的膠（CDS 12 的 IPTG 依賴帶）→ 10-10 的 Ni-NTA（沖提道空白）
> 畫面標 `empty-vector BL21 lane: still absent`

> Four rounds at the bench. On September the twenty-ninth, CDS 12 gave an IPTG-dependent band at the right size while the tail spike gave nothing. On October the tenth we ran a nickel column on one ancestor, and both elutions came off blank — while the load and the flow-through carried the same band.
>
> We read that as a purification we'd botched, and were about to spend another week on the column.

**87 字**

### IV.3 Learn — 外部意見改變了一個結果

> 🎬 **全片最強的 HP 段落。** Tolstorukov 的 email 引文 → 10-19 dot blot → 2.9× 標出來。
> 畫面標 `Prof. Ilya Tolstorukov, Keck Graduate Institute · 2026-10-13`

> What stopped us was a conversation.
>
> On October the thirteenth we took it to Professor Ilya Tolstorukov at Keck Graduate Institute, who works on protein expression. He wrote back before we met to say he wasn't sure he was the right person — expression is his field, purification isn't — and met us anyway. That turned out to be the point.
>
> He changed the question. Not *why is nothing eluting*, but *is there anything there to elute*. Check whether the protein is being made at all — a dot blot against an anti-His antibody — before touching the column again.
>
> Six days later we ran that blot. The flow-through from the ancestor read two point nine times the negative control.
>
> So the protein was there. It had been made, it came off in the flow-through, and the run failed at capture — not at expression. A gel can't tell those apart; all three look identical. One cheap assay separates them, and it pointed the fix at the column instead of the construct.
>
> We'd spent a week debugging the last step of a workflow without checking the first step worked, because the last step was the one visibly failing. That's the generalisable mistake, and one meeting fixed it.

**252 字**

### IV.4 還欠什麼

> 🎬 誠實清單。畫面標 `fifth consecutive assay with no empty-vector lane`

> One thing we still owe: we've run five protein assays without an empty-vector BL21 lane, the control that separates our bands from host background. That one is on the bench now.

**69 字**

---

## ACT V — CYCLE 4: LET THE BACTERIA ANSWER

> 🎬 幕卡：`CYCLE 4 — LET THE BACTERIA ANSWER`

### V.1 Design → Test

> 🎬 從噬菌斑區挑菌落 → WGS → read 層級驗證 → F126L 落在 30 kb 莢膜簇裡
> 畫面標 `every difference verified back to raw reads, against two independent baselines`

> Three cycles in, every guess about the receptor had come from the phage's side. So for the fourth we let the bacteria answer.
>
> In July we picked colonies from inside the plaque zone — cells still growing where the phage should have killed them — and sequenced them against their parents.
>
> Every difference was checked back against the raw reads. Exactly one survived: a single amino-acid change in a sugar phosphotransferase, inside a thirty-kilobase capsule cluster. The O-antigen cassette was untouched.

**114 字**

### V.2 Learn

> 🎬 莢膜遮住底下完好 O-antigen 的示意圖 —— 兩個結論如何同時成立。

> That disagrees with Cycle 2, which is the whole reason for doing it this way round. Cycle 2 said the receptor is a sugar; Cycle 4 agrees it's a sugar and disagrees about which one. It points at the capsule, not the O-antigen underneath.
>
> Both can be true at once, because a capsule can hide an intact O-antigen underneath it. We don't yet know which surface Phi-8 reads.
>
> And the honest gap: those colonies were never confirmed resistant. They were colonies in a plaque zone, which is suggestive and isn't the same thing.

**117 字**

---

## CODA

> 🎬 幕卡：`WHAT IT IS FOR, AND WHAT WE GOT WRONG`

### C.1 植物園

> 🎬 **植物園訪談片段（建議 ≥ 20 秒）。** 見文件開頭待決定事項 (1)。
> 畫面標 `Ashley Armstrong & James Manifold, California Botanic Garden · 2026-10-19 · used with permission`

> Two days before our wiki froze we went back to the garden the soil came from, and asked whether a treatment as strain-specific as ours would be any use to them.
>
> Most of what we'd assumed was wrong.
>
> We expected to argue for biological control against a chemical default, and didn't have to — they already suppress soil fungi by mulching. We expected the objection to be ecological risk. It wasn't; it was whether the thing works. Copper is the only chemistry they have for bacterial disease, it goes onto every blossom every four or five days, and they have eighty-six acres and eight staff. The objection is arithmetic.
>
> And the finding that costs us most: they've never had a sample come back positive for *Pseudomonas*. We isolated a soil phage and its environmental host — not a treatment for a disease this stakeholder has.
>
> What they do need is something for bacteria inside the vascular system, where nothing they have reaches. Our strain doesn't solve that.

**190 字**

### C.2 安全

> 🎬 IBC 信件 → `0 VFDB / 0 CARD` → 開放中的那一條原文

> On safety: our biosafety committee gave conditional approval with one condition still open — and that condition is a question about host range, which is the subject of this entire project. We don't have full approval; the revision is being written.
>
> Phi-8 carries no virulence factors and no resistance genes, and our constructs are protein fragments in lab *E. coli* — nothing here is a modified phage. But understanding what sets the ceiling on host range is the same as knowing what would have to change to raise it, so we treat this as dual-use rather than arguing our way to a clean no.

**136 字**

### C.3 收尾

> 🎬 三欄：`Established` / `Predicted` / `Open`，逐欄淡入。

> So, where we actually are.
>
> Established: the genomes, three unrelated sugar cassettes in one locus, a tail spike that turns out to be a sugar-cutting enzyme, a controlled negative result about interface prediction, and one mutation verified in the reads.
>
> Predicted and partly tested: that Phi-8 won't infect the other two strains. A host-range matrix in July pointed the right way, but carried no no-phage control, so we won't call it confirmed.
>
> Still open: clean expression, an activity assay, which sugar layer the phage reads, and whether Phi-8 is temperate.
>
> Four cycles, three of them wrong, each wrong in a way that told us where to go next. If there's one thing we'd pass on: put the cheap control in front of the expensive experiment. Ten folds told us what seven thousand couldn't, and one afternoon's dot blot told us what a week on a column hadn't.

**177 字**

---

## CREDITS

> 🎬 無旁白，30 秒。隊員、PI、Prof. Libeskind-Hadas、Prof. Tolstorukov、Monjima Ghosh、
> Maggie Chou、California Botanic Garden（Ashley Armstrong、James Manifold）、Twist、
> Artlist 曲名／作者／授權、工具（Pharokka、PhageRBPdetect、ESMFold、ColabFold、Boltz-2、
> IQ-TREE、ZymCTRL、Foldseek、PyMOL、Claude）。**停留 ≥ 2 秒。**

---

## 對照評分表

| 條件 | 在哪 |
|---|---|
| B1 目標／設計／結果 | OPENING 一句話定題；C.3 三欄回扣 |
| B2 技術數據 | 對照組數字、八蛋白分類表、2.9× dot blot、F126L reads |
| B3 視覺設計 | DBTL 進度條貫穿四輪；β-helix 渲染圖；分幕配色 |
| B4 engaging | 四輪結構；Cycle 1 與 Cycle 4 兩次翻轉 |
| B5 出處 | PI 三處署名、Libeskind-Hadas、Tolstorukov、植物園、工具全列 |
| **C1 DBTL** | **四輪各自完整，每輪都有 Learn** |
| C2 標準元件 | IV.1 六個 pET-28a 建構 |
| C3 會不會成功 | C.3 三欄 |
| C4 數據支持 claim | 畫面寫出缺的對照；預測只說「方向吻合」 |
| C5 影響 | C.1 植物園說出真正的缺口 |
| **C6 HP 影響設計** | **I.3 專案起源、IV.3 改變了一個結果、C.1 改變了定位** |
| C7 責任與安全 | C.2 |
| C9 學生主導 | 署名精確；ASR 寫成「方向共同決定、PI 執行、我們備料」 |

---

## 時間表 —— 必讀

字數由 `code/1024_script_pdf/make_script_pdf.py` 實測：**2,184 字**。

| 語速 | 旁白 | ＋幕卡與片尾 45 秒 |
|---|---|---|
| 140 wpm | 15:36 | **16:21 ✗ 超過** |
| 150 wpm | 14:33 | 15:18 ✗ 超過 |
| 155 wpm | 14:05 | 14:50 ⚠️ 剛好 |
| 160 wpm | 13:39 | 14:24 ✓ |

**坦白講：你要求補的東西（四輪 DBTL ＋ 四段 HP ＋ 安全 ＋ 對非專業觀眾解釋清楚），
照正常語速塞不進 15 分鐘。** 我已經把每一段都壓過一輪，從 2,803 字壓到 2,184，
再壓下去就是砍內容，而砍哪一塊是你的決定不是我的。

### 各段字數（決定要砍哪裡時看這張）

| 字數 | 段落 |
|---|---|
| 220 | II.4 Cycle 1 Learn —— 機制解釋 |
| 207 | IV.3 Cycle 3 Learn —— Tolstorukov |
| 167 | C.1 植物園 |
| 150 | III.2 Cycle 2 Test→Learn |
| 147 | C.3 收尾 |
| 122 | IV.1 Cycle 3 Design→Build |
| 116 | II.3 Cycle 1 Test |
| 106 | OPENING |
| 105 | I.4 系統與第一條線索 |
| 104 | C.2 安全 |
| 93 | V.2 Cycle 4 Learn |
| 81 | V.1 Cycle 4 Design→Test |
| 78 | II.2 Cycle 1 Build |
| 74 | II.1 Cycle 1 Design |
| 72 | IV.2 Cycle 3 Test |
| 70 | I.1 問題 |
| 68 | III.3 假說 |
| 63 | I.2 糖衣 |
| 61 | I.3 專案從哪來 |
| 49 | III.1 Cycle 2 Design→Build |
| 31 | IV.4 還欠什麼 |

### 三個選項

**A. 念快一點（160 wpm）—— 不砍任何東西。** 14:24 過關。
代價是語速偏快，而 ballot 有一題是 engaging。紀錄片旁白通常 140–150。

**B. 砍幕卡，念 150。** 六張幕卡改成左下角的 lower-third 標籤，省 15 秒，片尾留 30 秒
→ 15:03。還是太貼，不建議單用。

**C. 砍約 250 字到 1,930，用 150 wpm → 13:52 ＋ 45 秒 ＝ 14:37。安全。**
我建議砍這三處，理由是它們在 wiki 上都講得更完整，judge 會去看：
- **C.2 安全 104 → 45**（−59）。留「有條件核准、條件就是宿主範圍、我們當 dual-use 處理」三句。
- **I.3 專案從哪來 61 → 0**（−61），把 Libeskind-Hadas 併進 IV.1 的一個從句。
- **C.1 植物園 167 → 110**（−57）。保留「我們以為的全錯了」「他們沒有 Pseudomonas」
  「真正的缺口在維管束」三個重點，刪銅劑的細節。
- **III.2 150 → 115**（−35）。刨刀的比喻留著，壓縮前面。

**我的建議是 C。** 但 I.3 那段是 ASR 的來源故事，砍掉有點可惜 —— 如果你想留，
就改成砍 II.3 和 V.2 各 30 字。


## 念法備註

| 寫法 | 念法 |
|---|---|
| Phi-8 | *fye-eight* |
| pb-five × FhuA | *pee-bee-five* ／ *foo-ay* |
| beta-helix | *bay-ta* |
| CDS 11 / 12 / 24 | *C-D-S eleven*，不要念成 zero-zero-one-one |
| nought point nine nine seven | 一個數字一個數字念 |
| *Pseudomonas* | *soo-doh-MOH-nas* |
| Tolstorukov | *tol-sto-ROO-kov* |

---

## Log

- 2026-10-24 — v1 初稿，1,802 字，三幕
- 2026-10-24 — v2 大改。依 Alex 的 PDF 批註與重讀 wiki 的 Engineering／Human Practices：
  改成四個 DBTL cycle；補上四段 Human Practices；**修正 Ni-NTA 段落**（實際結論是 capture failure，
  由 Tolstorukov 建議的 anti-His dot blot 證實，2.9× 陰性對照）；修正「預測未驗證」為「已測、方向吻合、
  無對照」；加開場自我介紹；採樣地點改為 California Botanic Garden；噬菌體基因體組裝改記為團隊；
  加 sugar coat 解釋圖；放軟第一幕預測語氣；補實作細節（三個摺疊工具、Laguna、PhageRBPdetect）；
  全篇重寫語氣
