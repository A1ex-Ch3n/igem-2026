# Presentation Video — English narration script (v3, full)

故事見 [`2026-10-24_presentation_video_story.md`](2026-10-24_presentation_video_story.md)、
條件總表見 [`2026-10-24_presentation_video_plan.md`](2026-10-24_presentation_video_plan.md) §3B。

**v3 = 先寫滿，不管長度**（Alex 2026-10-24：「內容不是太多，而是太少」）。
來源是線上 wiki 全部 18 頁，2026-10-24 抓取。
（`git@ssh.gitlab.igem.org:2026/claremont-ca.git` 在這台機器上三把 SSH key 都沒註冊，
所以讀的是已發布的 HTML —— 那也正是 judge 會看到的東西。要我改用 GitLab 原始碼的話，
把 key 加到 gitlab.igem.org 就行。）

## v3 比 v2 多補的東西

讀完 wiki 後發現 v2 **漏掉的幾乎全是正面結果**，其中兩個相當關鍵：

1. **10/01 e1（Node1 祖先）在預測分子量沖提出來，是六個建構裡唯一成功的。**
   v2 只寫了失敗那次。
2. **10/16 活性測定有量化結果**：e1 液滴內菌落掉到該盤 PBS 對照的**中位數 12%**，
   Φ8 自己是 0%。PI 判讀為酵素活性；能獨立證明的 carry-over 對照沒跑。
3. **拓撲已定案為 circular**（77 bp 等於組裝的最大 k-mer 長度，覆蓋度無尖峰）。v1/v2 寫成未解決。
4. **五株分離株 → 三個 ANI 相異菌株**，兩對 clone pair 是全專案的內部對照。
5. **Parts**：六個 basic part 已發表、CC0，其中三個是自然界不存在的重建祖先。
6. **Software**：`gelquant` 與 `phagecheck` 已打包測試、MIT、在 iGEM GitLab。
7. **Contribution**：被記錄的失敗模式、RBP Detect 勝過同源註解的 benchmark、
   第二批 Twist 訂單的 codon bias 警告。
8. **Model 的替代宿主取捨**（選有文獻的，不選最相似的）。
9. 蛋白測定缺 BL21 空載體對照的次數是 **八次**，不是五次。

---

## OPENING

> 🎬 隊徽 → 隊員合照 → 片名。

> We're iGEM Claremont-CA, a first-year team in California, and this is Phagenomics.
>
> *Pseudomonas* causes serious infections in immunocompromised patients and persistent crop disease in agriculture, and phage therapy is one of the alternatives to antibiotics people are betting on. Its bottleneck is host range: each phage binds a specific receptor on a specific strain, and we can't design that specificity yet, because we don't understand how a phage recognises its target in the first place.
>
> So we didn't set out to build a therapeutic. We set out to understand the recognition step any therapeutic would depend on. We went at it four times this season. Three of those attempts failed, and the failures turned out to be the useful part.

**122 字**

---

## ACT I — THE BOTTLENECK

> 🎬 幕卡：`ACT I — THE BOTTLENECK`

### I.1 問題

> 🎬 plaque assay 動畫 → 同一滴滴到另外兩株，什麼都沒發生。

> A drop of phage goes onto a lawn of bacteria, and a few hours later there's a clear circle where the bacteria used to be. Move the same drop to the next plate and nothing happens.
>
> Same phage, different strain. That fussiness is the bottleneck: you need a phage that matches the strain in front of you, and usually there isn't one.

**65 字**

### I.2 吸附與糖衣

> 🎬 **細菌剖面圖**：細胞膜 → 細胞壁 → O-antigen → 莢膜。標出噬菌體最先碰到哪一層。

> It gets decided at the first step, before any DNA moves: the phage has to recognise the outside of the cell and stick to it.
>
> And many bacteria aren't presenting a bare protein surface. They're wrapped in sugar — long chains called the O-antigen, and above that, in some species, a capsule. The first thing a phage touches is a forest of sugar.

**69 字**

### I.3 這個專案從哪來

> 🎬 HP Fig 1：團隊與 Prof. Libeskind-Hadas 的合照。

> One thing belongs at the start, because it's why half this project exists.
>
> Early on, Professor Ran Libeskind-Hadas at Claremont McKenna suggested reconstructing an ancestral phage — a whole organism, inferred from its relatives. We couldn't build one. But scale that down to a single enzyme and you can order it from a synthesis company. That is what this project became.

**66 字**

### I.4 我們分離到什麼

> 🎬 採樣照 → 五株分離株收斂成三個菌株的表 → Φ8 環狀基因體圖，tail spike 標紅
> 畫面標 `California Botanic Garden · 19 May 2026`、`Pseudomonas_E sp013179515`、MRA doi

> Soil from the California Botanic Garden, on the nineteenth of May. Out of it came five *Pseudomonas* isolates, whole-genome sequenced, all five closing into complete circular genomes. They collapse into three strains that differ from one another — two of them the same species, the third a different one.
>
> That leaves two pairs of near-identical isolates, and those pairs do real work for the rest of the project. They're our internal control: any difference we report between strains has to be bigger than the difference we can measure within one.
>
> And one phage, Phi-8, which infects exactly one of the three strains. Sixty-two thousand, three hundred and thirty-nine base pairs, circular, eighty genes, no match in the phage database, and effectively no genes in common with T7 or anything else characterised. The architecture is familiar. The sequence isn't.

**137 字**

### I.5 第一條線索

> 🎬 三株的 O-antigen 基因座並排。畫面標 `hypothesis`

> Then we lined the three strains up at the locus that builds their sugar coat. Same position, same flanking gene — and inside, three cassettes with no homology to each other at all.
>
> Three strains, three different sugar coats, one phage that kills one of them. So our first hypothesis: the sugar coat might be one of the main things setting what Phi-8 can attack.

**69 字**

---

## CYCLE 1 — THE WRONG QUESTION

> 🎬 幕卡 ＋ DBTL 進度條。四輪共用同一條，當前步驟亮起。

### C1.D Design

> 🎬 `DESIGN` 亮。鎖與鑰匙。

> But that isn't the hypothesis we tested first.
>
> The textbook picture of attachment is a receptor-binding protein on the tail meeting a protein on the bacterial surface. Lock and key. If that's what you assume, the obvious move is to work out which binding protein fits which receptor.
>
> If we'd known the receptor was a sugar we'd never have run this. We thought it was a protein, so we went looking for a protein.

**76 字**

### C1.B Build

> 🎬 `BUILD` 亮。441 → 144 clusters → 114 × 63 漏斗。替代宿主的取捨用兩欄對比。
> 畫面標 `Laguna HPC · L40S`

> First we needed to know what was actually on the surface. We annotated four hundred and forty-one candidate surface receptors across all five isolates and collapsed them into a hundred and forty-four clusters.
>
> Then we needed a reference set of phages, which meant choosing a surrogate host — a relative of our strains that people have already characterised phages on. The closest match by receptor content had only twelve phages on record. A slightly more distant relative had two hundred and twenty-seven binding-protein entries across seventy-one phages. We took the one with the literature rather than the one with the best identity, because a receptor shared with a strain nobody has studied tells you nothing.
>
> That gave us a hundred and fourteen binding proteins against sixty-three receptors — seven thousand, one hundred and eighty-two pairs — each folded as a complex on our university's GPU cluster and ranked by the interface score.
>
> Getting it to run took three tools: ColabFold throttled by its alignment server, Boltz-2 blocked by the cluster's CUDA version, and finally ESMFold, which was the one that ran.

**178 字**

### C1.T Test

> 🎬 `TEST` 亮。排名熱圖（看起來很合理）→ 分數 vs 蛋白長度散點 → 對照組圖。
> **0.137 / 0.136 要大，停在畫面上。**

> Six thousand, three hundred and fifty-eight pairs came back with a score. And the ranking looked fine, which is the trouble with this kind of output — it always looks fine.
>
> What made us uneasy was that the scores tracked protein length. Correlation of plus nought point six.
>
> So before building anything on it, we ran the method against pairs where the answer was already known: complexes solved experimentally, against the same receptors shuffled into nonsense, and against deliberately wrong pairings.
>
> T5's pb-five with FhuA, a real co-crystallised complex, scored zero point one three seven. The same receptor shuffled scored zero point one three six.
>
> We assumed that was the tool, so we rebuilt it with real evolutionary alignments. It got worse: a deliberately mismatched pair came out at zero point five, above every genuine binder.

**139 字**

### C1.L Learn

> 🎬 `LEARN` 亮。兩條信心柱（打亂後左崩右不動）→ paired MSA 兩個永不相交的圈。

> Two tools, two control gates, both failed. One failure is about your run; two independent failures are about the method.
>
> These models report two confidences: one for the shape of the molecule, one for how two molecules sit together. When we shuffled a sequence, the shape confidence collapsed from zero point five five to zero point one seven — the model could tell it was nonsense. But the interface number barely moved. It had never been reading an interface at all.
>
> The reason is that these models don't simulate two proteins touching. They read evolution — looking across thousands of species for positions that change in step. If a residue on one side mutates and one on the other mutates to match, those two are probably in contact.
>
> That only exists if the two proteins have been inherited together, in one genome, for a long time. A phage protein's relatives are in other phages; a bacterial protein's are in other bacteria. They're never in the same genome, so the record of that interface doesn't exist. Not hidden — never written.
>
> So this was never a result about our proteins. It's a property of the method for any phage-and-host pair, and more compute doesn't help. Nine control folds decided the fate of seven thousand, and we never ran the real screen.

**221 字**

---

## CYCLE 2 — ASK THE PROTEIN WHAT IT IS

> 🎬 幕卡 ＋ DBTL 條。

### C2.DB Design → Build

> 🎬 PhageRBPdetect 掃 80 → 8 候選 → rung period 示意。
> 畫面標 `PhageRBPdetect v4 (ESM-2), open source`

> If we couldn't ask what the tail spike binds, we could ask what it is.
>
> We ran an open-source classifier across all eighty Phi-8 proteins to pick the candidates, folded the eight that came out, and classified their folds by the spacing of the backbone hydrogen bonds — which needs no structure database at all.

**58 字**

### C2.TL Test → Learn

> 🎬 八蛋白分類表，四種判定（**強調它會分辨**：CDS_0012 被判 α-rich，與它是 GH5 TIM barrel 一致）
> → β-helix 渲染 ＋ 切糖動畫。畫面標 `CDS_0011 · confidence 0.997 · pLDDT 93.2 · rung period 16–17`

> Eight proteins, four different verdicts — so the method discriminates rather than just agreeing with us. It even called one of our own targets *not* a beta-helix, which matched an independent read of that protein as a completely different fold.
>
> CDS 11, the tail spike, came back a right-handed beta-helix: a long triangular prism, classifier confidence nought point nine nine seven, fold confidence ninety-three. And CDS 24, which the annotation had written off as a hypothetical protein, came back as a second depolymerase the homology tools had missed.
>
> That fold is a signature. Enzymes that chew through long sugar chains look like this, because a sugar chain is a thread and you need something that holds it straight while you cut. You can recognise a wood plane by its shape without being told what it cuts.
>
> So the tail spike isn't a key. It's a blade — and the lock we'd spent months looking for doesn't exist.
>
> That reading arrived from two directions at once: our classifier flagged it as a depolymerase, and our PI reached the same conclusion from his own structural search. Between us we turned it into a hypothesis.

**196 字**

### C2.H 假說

> 🎬 一句話假說框，白底，停久。畫面標 `Hypothesis — developed jointly with Prof. J. Cesar Ignacio Espinoza`

> In bacteria that wrap themselves in sugar, the ceiling on host range is set by what the depolymerase can digest — not by which protein the tail binds. And the narrow specificity we see now is a narrowed-down version of something broader further back.
>
> That tells you what to measure — substrate range, not binding — and where to look for the broader version: back up the tree.

**72 字**

---

## CYCLE 3 — BUILD THE ENZYMES

> 🎬 幕卡 ＋ DBTL 條。

### C3.D Design

> 🎬 CDS_0011 三段結構域圖：1–110 anchor、111–300 shaft（飄）、301–941 body（剛性 0.44–0.99 Å）

> If the depolymerase is the thing that matters, the test is whether that domain, on its own, can cut the sugar.
>
> CDS 11 is nine hundred and forty-one residues, and most of it isn't the enzyme. The first hundred and ten anchor it to the virion. The next two hundred are a shaft that moves between every model we ran. The rigid trimeric body — residues three-oh-one to nine-four-one, agreeing between models to within one ångström — is the part that carries the active site. That's what we submitted, and what we expressed.
>
> Then the ancestors, which is where that first conversation comes back. We worked out the direction with our PI; he ran the alignment, the tree and the reconstruction on sequences we prepared, and the further back up the tree he went, the better a protein language model scored the result. We picked three nodes.

**152 字**

### C3.B Build

> 🎬 六個 part 的 Registry 卡片（BBa_、CC0、published）。
> 畫面標 `three of the six are sequences that exist nowhere in nature`

> Six constructs, all in pET-28a with an N-terminal His-tag, synthesised by Twist across two orders — and all six are now published basic parts on the iGEM Registry, under a CC0 licence.
>
> Three of those six are the reconstructed ancestors: protein sequences that exist nowhere in nature, inferred from an alignment and a tree and then ordered as DNA. That route to new parts is reusable by any team working on an enzyme family, so we wrote the method out in full.
>
> One warning we'd pass on, because it cost us. Our first Twist order was codon-optimised and our second wasn't — the second set carries a mammalian-like codon bias, which in an *E. coli* host is the first thing to suspect when a band doesn't appear. Anyone reusing those sequences should re-optimise first.

**134 字**

### C3.T Test

> 🎬 四輪測試時間軸 → 9-15 兩張膠 → 9-29 CDS_0012 的帶 → **10-01 e1 沖提成功** → 10-10 Node281 空白
> 畫面標 `empty-vector BL21 lane: absent in all eight assays`

> Four rounds at the bench, and they didn't line up neatly.
>
> September the fifteenth: two gels, four constructs, induced and uninduced — no detectable induction on either. Inconclusive. The tail spike lane was essentially blank, which points at lysis or loading rather than at expression.
>
> September the twenty-ninth: CDS 12 gave the first induction-dependent band at the right size.
>
> October the first: we ran nickel columns on six constructs, and one worked. The first ancestor eluted at its predicted mass — the only construct that did. The other five gave nothing.
>
> October the tenth: the same column on a different ancestor, and both elutions came off blank, while the load and the flow-through carried the same band. We read that as a purification we'd botched, and were about to spend another week on it.

**145 字**

### C3.L Learn — 外部意見改變了一個結果

> 🎬 **全片最強的 HP 段。** Tolstorukov 的 email 引文 → 10-19 dot blot → 2.9× 標出來。
> 畫面標 `Prof. Ilya Tolstorukov, Keck Graduate Institute · 2026-10-13`

> What stopped us was a conversation.
>
> On October the thirteenth we took it to Professor Ilya Tolstorukov at Keck Graduate Institute, who works on protein expression. He wrote back before we met to say he wasn't sure he was the right person — expression is his field, purification isn't — and met us anyway. That turned out to be the point.
>
> He changed the question. Not *why is nothing eluting*, but *is there anything there to elute*. Check whether the protein is being made at all — a dot blot against an anti-His antibody — before touching the column again. He also told us to run uninduced controls, and to standardise how much material goes onto a membrane before comparing spots on it.
>
> Six days later we ran that blot. The flow-through from the second ancestor read two point nine times the negative control.
>
> So the protein was there. It had been made, it came off in the flow-through, and the run failed at capture — not at expression. A gel can't tell those apart: no expression, insoluble protein, and a column that didn't bind all look identical. One cheap assay separates them, and it pointed the fix at the column instead of the construct.
>
> We'd spent a week debugging the last step of a workflow without checking the first step worked, because the last step was the one visibly failing. That's the generalisable mistake, and one meeting fixed it.

**243 字**

### C3.A 活性測定

> 🎬 10/16 spot test 圖 → 菌落計數歸一化到 PBS 對照的長條圖。
> 畫面標 `e1 median 12% of PBS control` ｜ `Φ8 median 0%` ｜ `carry-over control: not run`

> And then the assay the whole project points at: does this enzyme, on its own, do anything to the sugar?
>
> We read it on October the sixteenth. No visible lysis on any plate — including Phi-8 on its own hosts, which tells you the assay wasn't reading clearing. But counting colonies inside the drops gives a number. Under the first ancestor, colony counts fall to a median of twelve percent of the plate's PBS control. Phi-8's own median is zero.
>
> Our PI reads that suppression as enzyme activity. We'd want one more control before we call it that ourselves — the one that separates protein activity from phage carried over into the preparation — and that control wasn't run.

**124 字**

### C3.G 還欠什麼

> 🎬 誠實清單。

> And the gap that runs through all of it: we have now run eight protein assays — seven gels and a dot blot — and not one carries a lane of untransformed BL21. Every round was designed around a different variable instead. That control is on the bench now.

**49 字**

---

## CYCLE 4 — LET THE BACTERIA ANSWER

> 🎬 幕卡 ＋ DBTL 條。

### C4.DT Design → Test

> 🎬 從噬菌斑區挑菌落 → WGS → read 層級驗證 → F126L 落在 30 kb 莢膜簇

> Three cycles in, every guess about the receptor had come from the phage's side. So for the fourth we let the bacteria answer.
>
> In July we picked colonies from inside the plaque zone — cells still growing where the phage should have killed them — and sequenced them against their parents. No structure prediction anywhere in this loop.
>
> Every difference was checked back against the raw reads, which is the step that removed our own false positives. Exactly one mutation survived: a single amino-acid change in a sugar phosphotransferase, inside a thirty-kilobase capsule cluster. The O-antigen cassette was untouched.

**101 字**

### C4.L Learn

> 🎬 莢膜遮住底下完好 O-antigen 的示意圖。

> That disagrees with Cycle 2, which is the whole reason for doing it this way round. Cycle 2 said the receptor is a sugar. Cycle 4 agrees it's a sugar and disagrees about which one — it points at the capsule, not the O-antigen underneath.
>
> Both can be true at once, because a capsule can hide an intact O-antigen underneath it. We don't know yet which surface Phi-8 reads, so where the distinction matters this project says *surface polysaccharide* and leaves it there.
>
> And the honest gap: those colonies were never confirmed resistant. They were colonies in a plaque zone, which is suggestive and isn't the same thing.

**112 字**

---

## WHAT WE'RE LEAVING BEHIND

> 🎬 幕卡：`WHAT WE'RE LEAVING BEHIND`。工具終端畫面 → GitLab repo → 六個 part → 負面結果

> Four things, and one of them is a failure.
>
> Two packaged tools, MIT licensed, on iGEM's GitLab. One does ladder calibration and densitometry on a gel photograph — we re-typed that code three times across three gel days before admitting we should generalise it. The other tells a direct terminal repeat from a circular join by the shape of the read coverage, and that one changed our own answer: this wiki used to say the genome was linear, the check said circular, and circular is what we now report. Two more tools are staged with porting notes.
>
> Six parts on the Registry, three of them sequences that never existed.
>
> A benchmark: a machine-learning classifier found a depolymerase on a novel genome that homology-based annotation had labelled hypothetical.
>
> And the screen that failed — published with the controls that caught it and the reason it could never have worked, so the next team planning one can read it and skip it.

**161 字**

---

## CODA

> 🎬 幕卡：`WHAT IT IS FOR, AND WHAT WE GOT WRONG`

### CO.1 植物園

> 🎬 **植物園訪談片段（建議 ≥ 20 秒）。** 我們在錄音中承諾過會剪進這支片。
> 畫面標 `Ashley Armstrong & James Manifold, California Botanic Garden · 2026-10-19 · used with permission`

> Two days before our wiki froze we went back to the garden the soil came from, and asked whether a treatment as strain-specific as ours would be any use to them.
>
> Most of what we'd assumed was wrong. We expected to argue for biological control against a chemical default, and didn't have to — they already suppress soil fungi by mulching. We expected the objection to be ecological risk. It wasn't; it was whether the thing works. Copper is the only chemistry they have for bacterial disease, it goes onto every blossom every four or five days, and they have eighty-six acres and eight staff. The objection is arithmetic.
>
> And the finding that costs us most: they've never had a sample come back positive for *Pseudomonas*. We isolated a soil phage and its environmental host — not a treatment for a disease this stakeholder has.
>
> What they do need is something for bacteria inside the vascular system, where nothing they have reaches. Our strain doesn't solve that. But the question we worked on — what a tail spike reads on a cell surface, and how far that can be predicted from a genome — is the one you'd have to answer first. The strain is local. The question isn't.

**206 字**

### CO.2 安全

> 🎬 IBC 信件 → `0 VFDB / 0 CARD` → 開放中的那一條原文

> On safety: our institutional biosafety committee gave conditional approval with one condition still open, and that condition is a question about host range — the subject of this entire project. They asked us to show our reasoning that the work won't alter host range, virulence, or antibiotic resistance. We don't have full approval; the revision is being written.
>
> Phi-8 carries no virulence factors and no resistance genes, and our constructs are protein fragments in lab *E. coli* — nothing here is a modified phage. But understanding what sets the ceiling on host range is the same as knowing what would have to change to raise it, so we treat this as dual-use rather than arguing our way to a clean no.

**121 字**

### CO.3 收尾

> 🎬 三欄：`Established` / `Partly tested` / `Open`，逐欄淡入。

> So, where we actually are.
>
> Established: five bacterial genomes and a novel circular phage genome; three unrelated sugar cassettes in one locus; a tail spike that is a sugar-cutting enzyme by two independent methods; a controlled negative result about interface prediction; and one resistance mutation verified in the reads.
>
> Partly tested: that Phi-8 won't infect the other two strains — a host-range matrix in July pointed the right way, but carried no no-phage control. And the enzyme itself: one ancestor purified at its predicted mass, and colony counts under it fall to twelve percent of control, which our PI reads as activity and we won't call that ourselves without the carry-over control.
>
> Open: a clean expression round with the control we keep not running; which sugar layer the phage reads; whether Phi-8 is temperate; and depositing the genome, which we haven't done.
>
> Four cycles, three of them wrong, each wrong in a way that told us where to go next. If there's one thing we'd pass on: put the cheap control in front of the expensive experiment. Nine folds told us what seven thousand couldn't, and one afternoon's dot blot told us what a week on a column hadn't.

**205 字**

---

## CREDITS

> 🎬 無旁白，30 秒。隊員、PI、Prof. Libeskind-Hadas、Prof. Tolstorukov、Monjima Ghosh、
> Maggie Chou、California Botanic Garden（Ashley Armstrong、James Manifold）、Twist、
> Artlist 曲名／作者／授權、工具（Bakta、Pharokka、PhageRBPdetect、ESMFold、ColabFold、
> Boltz-2、IQ-TREE、ZymCTRL、Foldseek、Autocycler、PyMOL、BioRender、Claude）。**停留 ≥ 2 秒。**

---

## 對照評分表

| 條件 | 在哪 |
|---|---|
| B1 目標／設計／結果 | OPENING 定題；CO.3 三欄回扣 |
| B2 技術數據 | 對照組數字、八蛋白分類表、e1 沖提、12% 抑制、2.9× dot blot、F126L reads |
| B3 視覺設計 | DBTL 進度條貫穿四輪；β-helix 渲染圖；分幕配色 |
| B4 engaging | 四輪結構；Cycle 1 與 Cycle 4 兩次翻轉 |
| B5 出處 | PI 三處、Libeskind-Hadas、Tolstorukov、植物園、工具全列 |
| **C1 DBTL** | **四輪各自完整，每輪都有 Learn** |
| **C2 標準元件** | **C3.B：六個 Registry part、CC0、三個是自然界不存在的序列** |
| C3 會不會成功 | CO.3 三欄 |
| C4 數據支持 claim | 畫面寫出缺的對照；12% 那段明講 PI 的判讀與我們的保留 |
| C5 影響 | CO.1 植物園指出真正的缺口 |
| **C6 HP 影響設計** | **I.3 起源、C3.L 改變了一個結果、CO.1 改變了定位** |
| C7 責任與安全 | CO.2 |
| C8 文件化 | 「WHAT WE'RE LEAVING BEHIND」整段 |
| C9 學生主導 | 署名精確；ASR 寫成「方向共同決定、PI 執行、我們備料」 |

---

## 時間表

重建 PDF：`python code/1024_script_pdf/make_script_pdf.py`

v3 刻意寫滿，長度等你看完內容再一起砍。各段字數印在 PDF 的每個段落標題右側。

---

## 念法備註

| 寫法 | 念法 |
|---|---|
| Phi-8 | *fye-eight* |
| pb-five × FhuA | *pee-bee-five* ／ *foo-ay* |
| beta-helix | *bay-ta* |
| CDS 11 / 12 / 24 | *C-D-S eleven* |
| nought point nine nine seven | 一個數字一個數字念 |
| *Pseudomonas* | *soo-doh-MOH-nas* |
| Tolstorukov | *tol-sto-ROO-kov* |
| ångström | *ANG-strom* |

---

## Log

- 2026-10-24 — v1，1,802 字，三幕
- 2026-10-24 — v2，四輪 DBTL ＋ HP；修正 Ni-NTA 段落
- 2026-10-24 — **v3，先寫滿不管長度**（Alex：內容太少不是太多）。讀完線上 wiki 18 頁後補進
  v2 漏掉的正面結果：10/01 e1 在預測分子量沖提成功（六個裡唯一）、10/16 活性測定 e1 壓到
  PBS 對照的 12%（PI 判讀為活性，carry-over 對照未跑）、拓撲定案為 circular、五株分離株
  收斂成三個菌株且 clone pair 是內部對照、六個 Registry part（三個是自然界不存在的序列）、
  兩個已打包的 MIT 工具、RBP Detect 的 benchmark、第二批訂單的 codon bias 警告、
  Model 的替代宿主取捨、蛋白測定缺對照是八次不是五次
