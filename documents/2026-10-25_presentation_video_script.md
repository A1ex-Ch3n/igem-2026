# Presentation Video — English narration script (v4)

故事見 [`2026-10-24_presentation_video_story.md`](2026-10-24_presentation_video_story.md)、
條件總表見 [`2026-10-24_presentation_video_plan.md`](2026-10-24_presentation_video_plan.md) §3B。
v1–v3 在 `2026-10-24_presentation_video_script.md`（已停用）。

**v4 = 逐句對照 wiki 科學細節後的版本。** 每一個數字都回到線上 wiki 查過，對照表在文末 §FC。

## v4 修掉的實質錯誤

Alex 2026-10-25 問 GH5 分解的是不是另一種糖 —— **是，而且我前三版把兩個酵素混在一起了。**

| # | v3 寫的 | 實際（wiki） |
|---|---|---|
| 1 | 祖先序列讀起來像是尾刺 CDS_0011 的 | **祖先全部是 CDS_0012 的。CDS_0012 是獨立的蛋白，不是 CDS_0011 的結構域** |
| 2 | 沒提 CDS_0012 的預測受質 | **TIM barrel，結構上對到 endoglucanase 1ECE（綁 cellotetraose）；ZymCTRL 最低 perplexity 是 EC 3.2.1.4 endo-1,4-β-glucanase。不是 O-antigen** |
| 3 | 「八個蛋白，四種判定」 | **8 個預測結構涵蓋 7 個蛋白**（我們的註解把尾刺切成兩段，PI 的併成 CDS_0011）；**三種判定** |
| 4 | 「10/01 e1 沖提成功，其他五個沒東西」就停住 | 同時 **CDS_0011 沖提出的帶比預測的 72 kDa 短 29 kDa** |
| 5 | 12% 抑制沒講保留 | **那次 spot test 用的 1:10 稀釋在 dot blot 上都在背景以下** —— 液滴裡有沒有蛋白從未被證明 |
| 6 | 「預測未驗證／部分驗證」講得含糊 | 2026-07-04 測過，方向吻合，但**無 no-phage 對照、8-5-2 未計分、07-15 與 07-16 的讀數從未寫下** |
| 7 | 「nine control folds」與「ten」混用 | **nine-fold control validation**（3 對 × 3 條件） |
| 8 | CDS_0011 pLDDT 93.2 單獨引用 | 它被切成**兩個重疊片段**模擬，兩者不一致：**93.2 對 64.7** |
| 9 | 抗性突變只說「一個胺基酸改變」 | **F126L，read 支持 263/264，對照 0/176、0/60、0/422；另一株 9-2-1 R1 完全沒有確認突變** |

**Alex 2026-10-25 補充的設計理由**（wiki 上沒寫，但 judge 會問）：選 CDS_0012 做祖先重建，
除了它有上千個同源序列可以建樹之外，還因為**蛋白小、比較好表達**，以及**要在 Twist 贊助的額度內**，
短的建構體才做得出四個。已寫進 C3.B。

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

> 🎬 採樣照 → 五株分離株收斂成三個菌株 → Φ8 環狀基因體圖，tail spike 標紅
> 畫面標 `California Botanic Garden · 19 May 2026`、`Pseudomonas_E sp013179515`、MRA doi

> Soil from the California Botanic Garden, on the nineteenth of May. Out of it came five *Pseudomonas* isolates, whole-genome sequenced, all five closing into complete circular genomes. They collapse into three strains: two of them the same species, the third a different one.
>
> That leaves two pairs of near-identical isolates, and those pairs do real work for the rest of the project. They're our internal control — any difference we report between strains has to be bigger than the difference we can measure within one.
>
> And one phage, Phi-8, which infects exactly one of the three strains. Sixty-two thousand, three hundred and thirty-nine base pairs, circular, eighty genes, no match in the phage database, and effectively no genes in common with T7 or anything else characterised. The architecture is familiar. The sequence isn't.

**137 字**

### I.5 第一條線索

> 🎬 三株的 O-antigen 基因座並排（Results Fig 4 上半）→ 45 群的 presence/absence 矩陣（下半）
> 畫面標 `ihfB-anchored · MMseqs2 ≥30% id` ｜ `23 / 15 / 25 genes` ｜ `4 of 45 clusters shared`

> Then we went to the locus that builds their sugar coat, anchored on the gene that flanks it in *Pseudomonas*, and compared all three.
>
> The cassette sits in the same slot in every strain. The contents are unrelated: twenty-three genes in one strain, fifteen in another, twenty-five in the third, and of forty-five gene clusters across the three, only four are shared by all of them — all four generic sugar chemistry. No shared flippase, no shared polymerase, no shared chain-length regulator. Meanwhile the near-identical pairs inside each strain are a hundred percent identical across every cassette gene. Within a strain, zero variation. Between strains, almost total.
>
> We also found that nobody could have told us this from a database: there is no serotype scheme for this group of species at all. The two standard tools are built for other organisms.
>
> Three strains, three different sugar coats, one phage that kills one of them. So our first hypothesis: the sugar coat might be one of the main things setting what Phi-8 can attack.

**178 字**

---

## CYCLE 1 — THE WRONG QUESTION

> 🎬 幕卡 ＋ DBTL 進度條。四輪共用，當前步驟亮起。

### C1.D Design

> 🎬 `DESIGN` 亮。鎖與鑰匙。

> But that isn't the hypothesis we tested first.
>
> The textbook picture of attachment is a receptor-binding protein on the tail meeting a protein on the bacterial surface. Lock and key. If that's what you assume, the obvious move is to work out which binding protein fits which receptor.
>
> If we'd known the receptor was a sugar we'd never have run this. We thought it was a protein, so we went looking for a protein.

**76 字**

### C1.B Build

> 🎬 `BUILD` 亮。441 → 144 clusters → 114 × 63 漏斗。替代宿主取捨用兩欄對比。
> 畫面標 `Laguna HPC · L40S`

> First we needed to know what was on the surface. We annotated four hundred and forty-one candidate surface receptors across all five isolates and collapsed them into a hundred and forty-four clusters.
>
> Then we needed a reference set of phages, which meant choosing a surrogate host — a relative of our strains that people have already characterised phages on. The closest match by receptor content had twelve phages on record. A slightly more distant relative had two hundred and twenty-seven binding-protein entries across seventy-one phages. We took the one with the literature rather than the one with the best identity, because a receptor shared with a strain nobody has studied tells you nothing.
>
> That gave us a hundred and fourteen binding proteins against sixty-three receptors — seven thousand, one hundred and eighty-two pairs — each folded as a complex on our university's GPU cluster and ranked by the interface score.
>
> Getting it to run took three tools: ColabFold throttled by its alignment server, Boltz-2 blocked by the cluster's CUDA version, and finally ESMFold, which was the one that ran.

**176 字**

### C1.T Test

> 🎬 `TEST` 亮。排名熱圖 → 分數 vs 蛋白長度散點 → 對照組表（Results Table 4）。
> **0.137 / 0.136 要大，停在畫面上。**

> Six thousand, three hundred and fifty-eight pairs came back with a score; the rest were too long for the model. And the ranking looked fine, which is the trouble with this kind of output — it always looks fine.
>
> So before building anything on it, we ran nine control folds: three phage-receptor pairs known to bind, two of them with solved co-structures, each rerun with the receptor scrambled and mismatched against the wrong phage protein.
>
> T5's pb-five with FhuA scored zero point one three seven. The same receptor scrambled scored zero point one three six. The other two pairs behaved the same way. None of the real binders separated from the controls.
>
> And the scores tracked protein length, correlation of plus nought point six. The screen was ranking proteins by size.
>
> We assumed that was the tool, so we rebuilt it with real evolutionary alignments. It got worse — under that one the mismatched pair outscored the genuine binders.

**157 字**

### C1.L Learn

> 🎬 `LEARN` 亮。pTM 與 ipTM 兩條柱（打亂後 0.55→0.17 vs 幾乎不動）→ paired MSA 兩個不相交的圈。

> Two tools, two control gates, both failed. One failure is about your run; two independent failures are about the method.
>
> The diagnostic is this. These models report two confidences: one for the shape of the molecule, one for how two molecules sit together. On the scrambled receptors the shape score collapsed, from zero point five five to zero point one seven — the model could plainly tell the sequence was scrambled. The interface score barely moved. It had never been reading an interface at all.
>
> The reason is that these models don't simulate two proteins touching. They read evolution — looking across thousands of species for positions that change in step. If a residue on one side mutates and one on the other mutates to match, those two are probably in contact.
>
> That signal only exists where two proteins have a shared history of co-adaptation. A phage protein and a bacterial protein have never co-adapted as a pair, so there's no history to read and the interface score returns noise.
>
> So this was never a result about our proteins. It's a property of the method, and more compute doesn't fix it. Nine control folds decided the fate of seven thousand, and we never ran the real screen.

**213 字**

---

## CYCLE 2 — ASK THE PROTEIN WHAT IT IS

> 🎬 幕卡 ＋ DBTL 條。

### C2.DB Design → Build

> 🎬 PhageRBPdetect 掃 80 → 候選 → rung period 示意（β-helix 的階梯間距）
> 畫面標 `PhageRBPdetect v4 (ESM-2), open source` ｜ `phagecheck.betahelix — no database`

> If we couldn't ask what the tail spike binds, we could ask what it is.
>
> Two independent readouts, and they don't share a method. An open-source sequence classifier over all eighty Phi-8 proteins. And then geometry: a right-handed beta-helix is a chain coiled into a long prism with the coils hydrogen-bonded in register, so if you measure how far apart in sequence each backbone hydrogen bond reaches and histogram it, a beta-helix peaks at its coil period, somewhere between sixteen and twenty-six residues. An alpha-helix peaks at four. A beta-sandwich has no peak at all.
>
> We chose that test rather than fell back on it. On a genome with no close relatives, a database can't contain the answer — and homology annotation had already missed something here.

**128 字**

### C2.TL Test → Learn

> 🎬 Engineering Table 2 的七個蛋白判定表（**強調它會說「不是」**）→ β-helix 渲染 ＋ 切糖動畫
> 畫面標 `CDS_0011 · classifier 0.997 · rung period 16–17` ｜ `CDS_0024 · 0.998 · period 23`

> Eight predicted structures covering seven proteins, each classified from its own backbone geometry. Five of the seven were turned down — and the periods they return aren't noise: an alpha-helical fibre lands at six, close to where an alpha-helix should be. The method says no, which is what makes it worth believing when it says yes.
>
> It said yes twice. CDS 11, the tail spike, at classifier confidence nought point nine nine seven and a rung period of sixteen to seventeen: a right-handed beta-helix. And CDS 24, which the annotation had filed as a hypothetical protein, at nought point nine nine eight on a different period — a second depolymerase that homology-based annotation had missed entirely on this novel genome.
>
> That fold is a signature. Enzymes that chew through long sugar chains look like this, because a sugar chain is a thread and you need something that holds it straight while you cut. You can recognise a wood plane by its shape without being told what it cuts.
>
> So the tail spike isn't a key. It's a blade — and the lock we'd spent months looking for doesn't exist.
>
> That reading arrived from two directions at once: our classifier flagged it, and our PI reached the same conclusion from his own structural search. Between us we turned it into a hypothesis.

**223 字**

### C2.H 假說

> 🎬 一句話假說框，白底，停久。畫面標 `Hypothesis — developed jointly with Prof. J. Cesar Ignacio Espinoza`

> In bacteria that wrap themselves in sugar, the ceiling on host range is set by what the depolymerase can digest — not by which protein the tail binds. And the narrow specificity we see now is a narrowed-down version of something broader further back.

**43 字**

### C2.P 可否證的預測，以及它的檢驗

> 🎬 18 宿主矩陣 → 三個定序菌株那幾列。**保留條件要同時上畫面**：
> `no no-phage control` ｜ `8-5-2 not scored` ｜ `07-15 and 07-16 readouts never recorded`

> That hypothesis makes a prediction you can falsify: if the tail spike reads Strain 2's sugar, Phi-8 should fail on the other two strains.
>
> We ran it in July, eighteen host isolates against two pooled lysates. The Strain 1 and Strain 3 representatives scored negative against both. That is the direction the prediction makes.
>
> We're not calling it confirmed, and the reasons are from our own notebook, not from a reviewer. The assay carried no no-phage control — there's a margin note on the page that just says *need control*. One isolate wasn't scored. And two follow-up readouts that would have settled it were never written down. The result is consistent with the prediction and nothing contradicts it, but the clean experiment hasn't been done.

**133 字**

---

## CYCLE 3 — BUILD THE ENZYMES

> 🎬 幕卡 ＋ DBTL 條。
> **這一輪有兩條線，畫面要從頭到尾分開。左：CDS_0011 受體線。右：CDS_0012 祖先線。**

### C3.D1 第一條線：讀受體的那個酵素

> 🎬 CDS_0011 結構域圖：1–110 anchor、111–300 shaft（飄）、301–941 rigid body（0.44–0.99 Å）
> 畫面標 `BBa_26DKNAEC · res 305–941 · 638 aa · CC0`

> If the depolymerase sets the ceiling, the test is whether that domain, on its own, can cut the sugar.
>
> CDS 11 is nine hundred and forty-one residues and most of it isn't the enzyme. The first hundred and ten anchor it to the virion. The next two hundred are a shaft that moves between every model we ran. The rigid trimeric body — from residue three hundred to the end, agreeing between models to within one ångström — is the part that carries the chemistry. That's the fragment we designed, expressed, and submitted to the Registry.

**104 字**

### C3.D2 第二條線：為什麼祖先做在另一個酵素上

> 🎬 **這一段是防守 judge 必問的那一題。** 並排兩個蛋白：
> 左 CDS_0011 β-helix 941 aa；右 CDS_0012 TIM barrel 362 aa，標 `endoglucanase 1ECE, cellotetraose bound`
> 畫面標 `a separate protein — not a domain of CDS_0011`

> The ancestors are a different protein, and it's worth being clear about that.
>
> Phi-8 also carries CDS 12, a glycoside hydrolase from family five. It's a TIM barrel, not a beta-helix, and its closest structural match is an endoglucanase caught with a short cellulose chain in its active site. It is a separate protein — not a domain of the tail spike — and what it does inside the phage is not something we have established.
>
> So why reconstruct ancestors of that one, and not of the tail spike we've just spent five minutes on? Three reasons, and none of them is that we got confused. CDS 12 has a thousand homologues in the sequence databases, which is what you need to build a tree and reconstruct along it; the tail spike is novel enough that there isn't one. CDS 12 is a third of the size, so it was by far the better bet to express. And we were working inside a sponsored synthesis allowance, where four short constructs were affordable and four long ones were not.
>
> It means the ancestral panel tests the shape of the hypothesis — does an ancestral glycoside hydrolase have a broader substrate range than its descendant — on an enzyme we can actually build, rather than on the one that reads the receptor. That's a real limitation and it's ours, not a reviewer's.

**236 字**

### C3.B Build

> 🎬 系統發生樹往回合併 → 三個節點 → 六個 part 的 Registry 卡片。
> 畫面標 `ASR run by Prof. Espinoza on sequences the team prepared` ｜ `998 nodes reconstructed`

> We worked out the direction with our PI; he ran the alignment, the tree and the reconstruction on sequences we prepared. Every node on the path from CDS 12 back to the root was reconstructed, and the three we picked were ordered as DNA.
>
> Six constructs in all, in pET-28a with an N-terminal His-tag, synthesised by Twist across two orders — and all six are now published basic parts on the iGEM Registry under a CC0 licence. Three of the six are those reconstructed ancestors: protein sequences that exist nowhere in nature. That route to new parts is reusable by any team working on an enzyme family, so we wrote the method out in full.
>
> One warning we'd pass on, because it cost us. Our first order was codon-optimised and our second wasn't — the second set carries a mammalian-like codon bias, which in an *E. coli* host is the first thing to suspect when a band doesn't appear.

**161 字**

### C3.M 模型先說了什麼，以及它自己的對照

> 🎬 ZymCTRL perplexity 圖（Model Fig 6B）→ 把「21/24 類別都下降」的對照疊上去。
> 畫面標 `perplexity is not activity`

> Before any of them reached a bench, we asked a protein language model what the reconstructions looked like. Scored against twenty-four glycoside-hydrolase classes, the one it likes best is endo-one-four-beta-glucanase — the same chemistry the structure points at. And along the path to the root the score improves steadily, which read on its own is the hypothesis coming true.
>
> Except that it doesn't survive its own control. A reconstructed ancestor is consensus-like by construction, so it scores better under almost any label — and it does: the score improves in twenty-one of the twenty-four classes. Direction alone proves nothing. What survives is that the improvement is largest under the two labels the structure points at, and even that is less clean than one number would suggest.
>
> And perplexity isn't activity. Nothing in that analysis measures substrate range, which is the whole point of the panel.

**145 字**

### C3.T Test

> 🎬 四輪測試時間軸 → 9-15 兩張膠 → 9-29 CDS_0012 的帶 → 10-01（e1 成功 / CDS_0011 短 29 kDa）→ 10-10
> 畫面標 `empty-vector BL21 lane: absent in all eight assays`

> Four rounds at the bench, and they didn't line up neatly.
>
> September the fifteenth: two gels, four constructs, induced against uninduced. No detectable induction on either. The tail spike lane was essentially blank, which points at lysis or loading rather than at expression.
>
> September the twenty-ninth: CDS 12 gave the first induction-dependent band at the right size.
>
> October the first: nickel columns on six constructs, and one of them worked — the first ancestor eluted at its predicted mass, the only construct that did. The tail spike eluted something, but twenty-nine kilodaltons short of what it should be.
>
> October the tenth: the same column on a second ancestor, and both elutions came off blank while the load and the flow-through carried the same band. We read that as a purification we'd botched, and were about to spend another week on it.

**155 字**

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

### C3.A 活性測定，以及它能撐住多少

> 🎬 10/16 spot test → 菌落計數歸一化長條圖。**三個保留條件同時上畫面**：
> `carry-over control: not run` ｜ `spot-test dilutions read at or below the blot's floor` ｜ `n = 1`

> And then the assay the whole project points at: does an enzyme, on its own, do anything to the sugar?
>
> We read it on October the sixteenth. No visible lysis on any plate — including Phi-8 on its own hosts, so the assay wasn't reading clearing at all. But counting colonies inside the drops gives a number. Under the first ancestor, across seven strains, colony counts fall to a median of twelve percent of the plate's PBS control. Phi-8's own median is zero.
>
> Our PI reads that suppression as enzyme activity. We'd want more before we call it that ourselves, and there are two specific gaps. The control that separates protein activity from phage carried over into the preparation was not run. And the dilutions used in that spot test later read at or below the detection floor of our own dot blot — so the protein in those drops was never actually shown to be there.
>
> It's the strongest activity signal we have, and it is one plate.

**174 字**

### C3.G 還欠什麼

> 🎬 誠實清單。

> And the gap that runs through all of it: eight protein assays now — seven gels and a dot blot — and not one of them carries a lane of untransformed BL21. Every round was designed around a different variable instead. That control is on the bench now.

**48 字**

---

## CYCLE 4 — LET THE BACTERIA ANSWER

> 🎬 幕卡 ＋ DBTL 條。

### C4.DT Design → Test

> 🎬 從噬菌斑區挑菌落 → WGS → read 層級驗證（70 個候選點 → 1 個）→ F126L 在 30 kb 莢膜簇
> 畫面標 `263 of 264 mutant reads · 0 of 176 · 0 of 60 · 0 of 422`

> Three cycles in, every guess about the receptor had come from the phage's side. So for the fourth we let the bacteria answer.
>
> In July we picked colonies from inside the plaque zone — cells still growing where the phage should have killed them — and in October sequenced one from each host against its parent. No structure prediction anywhere in this loop.
>
> Both picks turned out to be the parent strain, intact, with no phage sequence in them, so neither had simply become a lysogen. A naive assembly comparison gives sixteen to twenty-one differing sites, which means nothing on its own — two sequencing runs of the same clone already differ by more than that. So every candidate went back to the raw reads: seventy sites examined, against the parent's reads and an independent read set with completely different chemistry.
>
> Exactly one survived. A missense change in a Stealth-family sugar phosphotransferase, carried by two hundred and sixty-three of two hundred and sixty-four mutant reads and none of the parent's. It sits inside a thirty-kilobase cluster that builds and exports capsular polysaccharide. The other pick has no confirmed mutation at all.

**198 字**

### C4.L Learn

> 🎬 莢膜遮住底下完好 O-antigen 的示意圖。

> That disagrees with Cycle 2, which is the whole reason for doing it this way round. Cycle 2 said the receptor is a sugar. Cycle 4 agrees it's a sugar and disagrees about which one — it points at the capsule, with the O-antigen cassette intact.
>
> Both can be true at once, because a capsule sits on top and can hide an intact O-antigen underneath it. We don't know which surface Phi-8 reads, so where the distinction matters this project says *surface polysaccharide* and leaves it there.
>
> And the honest gap: those colonies were never confirmed resistant. They were colonies in a plaque zone, which is suggestive and isn't the same thing.

**115 字**

---

## WHAT WE'RE LEAVING BEHIND

> 🎬 幕卡：`WHAT WE'RE LEAVING BEHIND`。工具終端畫面 → GitLab → 六個 part → 負面結果

> Four things, and one of them is a failure.
>
> Two packaged tools, MIT licensed, on iGEM's GitLab. One does ladder calibration and densitometry on a gel photograph — we re-typed that code three times across three gel days before admitting we should generalise it. The other is the fold test from Cycle 2, which takes a single predicted structure and returns a call with no database behind it; it also tells a terminal repeat from a circular join by the shape of the read coverage, and that changed our own answer. This wiki used to say the genome was linear. The check said circular, and circular is what we report. Two more tools are staged with porting notes.
>
> Six parts on the Registry, three of them sequences that never existed.
>
> A benchmark: on a genome with no close relatives, a machine-learning classifier found a depolymerase that homology-based annotation had filed as hypothetical. Our recommendation for novel phage genomes is to run both and reconcile the disagreements.
>
> And the screen that failed — published with the controls that caught it and the reason it could never have worked. Don't use interface scores to screen phage-host protein pairs, and run a positive control with a solved co-structure before you scale to thousands.

**213 字**

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
> Phi-8 carries no virulence factors and no resistance genes across all eighty coding sequences, and our constructs are protein fragments in lab *E. coli* — nothing here is a modified phage. But understanding what sets the ceiling on host range is the same as knowing what would have to change to raise it, so we treat this as dual-use rather than arguing our way to a clean no.

**126 字**

### CO.3 收尾

> 🎬 三欄：`Established` / `Partly tested` / `Open`，逐欄淡入。

> So, where we actually are.
>
> Established: five bacterial genomes and a novel circular phage genome; three unrelated sugar cassettes in the same locus, with no serotype scheme in existence to have told us; a tail spike that is a sugar-cutting enzyme by two independent methods; a controlled negative result about interface prediction; and one resistance mutation verified in the reads.
>
> Partly tested: that Phi-8 won't infect the other two strains — the July assay pointed the right way and carried no control. And the enzyme panel: one ancestor purified at its predicted mass, colony counts under it fall to twelve percent of control, and we won't call that activity without the control that separates it from carried-over phage.
>
> Open: a clean expression round with the lane we keep not running; whether the tail spike fragment is even full length; which sugar layer the phage reads; whether Phi-8 is temperate; and depositing the genome, which we haven't done.
>
> Four cycles, three of them wrong, each wrong in a way that told us where to go next. If there's one thing we'd pass on: put the cheap control in front of the expensive experiment. Nine folds told us what seven thousand couldn't, and one afternoon's dot blot told us what a week on a column hadn't.

**221 字**

---

## CREDITS

> 🎬 無旁白，30 秒。隊員、PI、Prof. Libeskind-Hadas、Prof. Tolstorukov、Monjima Ghosh、
> Maggie Chou、California Botanic Garden（Ashley Armstrong、James Manifold）、Twist、
> Artlist 曲名／作者／授權、工具（Bakta、Pharokka、PhageRBPdetect、ESMFold、ColabFold、
> Boltz-2、MMseqs2、IQ-TREE、PhyML、ZymCTRL、Foldseek、Autocycler、AlphaFold3、PyMOL、
> BioRender、Claude）。**停留 ≥ 2 秒。**

---

## FC. 逐項對照表

每一句有數字的話都回到 wiki 查過。來源頁面縮寫：R=Results、D=Design、P=Parts、
M=Model、E=Engineering、PC=Proof of Concept、C=Contribution、HP=Human Practices、
S=Software、DE=Description。

| 稿中說法 | wiki | 頁 |
|---|---|---|
| 五株分離株、三個菌株、兩株同種一株異種 | ✅ Strain 1 = 8-5-2/10-10-2，Strain 2 = 9-2-1/9-6-2，Strain 3 = 8-10-2（*P. capeferrum*） | R |
| clone pair 當內部對照 | ✅ 原文「any difference we report between strains has to be larger than the difference we measure within one」 | R |
| 62,339 bp、circular、80 CDS | ✅ 77 bp 等於最大 k-mer，覆蓋度無尖峰 | R, DE |
| 採樣 2026-05-19，California Botanic Garden | ✅ | DE |
| 無 MASH hit、與 T7 幾乎零 ortholog | ✅ | R |
| cassette 23 / 15 / 25 genes；45 群中 4 群共有 | ✅ 26.5 / 17.0 / 38.2 kb | R |
| 無共有 flippase／polymerase／chain-length regulator | ✅ | R |
| clone pair 在 cassette 基因上 100.0% 一致 | ✅ | R |
| 此類群無 serotype scheme（PAst、Kaptive 都不適用） | ✅ | R |
| 441 候選 → 144 clusters | ✅ | M |
| 替代宿主：12 phages vs 227 RBP／71 phages | ✅ | M |
| 7,182 對、6,358 有分數、824 太長 | ✅ | M, R |
| nine-fold control validation | ✅ 3 對 × 3 條件 | R |
| pb5×FhuA 0.137 / scrambled 0.136 | ✅ 另兩對 0.112/0.102、0.159/0.129 | R |
| r = +0.60 | ✅ | R |
| 真 MSA 那輪錯配贏過正對照 | ✅ 原文「under AlphaFold2 with real MSAs the mismatch outscores the positives」 | R |
| pTM 0.55 → 0.17，ipTM 不動 | ✅ | R |
| 無共演化史 → 界面分數是雜訊 | ✅ | R |
| 8 個預測結構、7 個蛋白、5 個被判否 | ✅ Engineering Table 2 | E |
| α-helical fiber 落在 6 | ✅ | E |
| CDS_0011 confidence 0.997、period 16–17 | ✅ | E, R |
| CDS_0024 confidence 0.998、period 23、Pharokka 標 hypothetical | ✅ | E, R |
| **CDS_0012 = GH5 TIM barrel，對到 endoglucanase 1ECE（cellotetraose）** | ✅ **原文「a distinct protein, not a domain of CDS_0011」** | R, D, P |
| CDS_0011 domain 1–110 / 111–300 / 301–941，0.44–0.99 Å | ✅ part 從 305 起 | R, D, P |
| 六個 part 已發表、CC0、三個是祖先 | ✅ BBa_26DKNAEC 等 | P |
| 998 個節點重建 | ✅ | M |
| ZymCTRL 最佳是 EC 3.2.1.4 endoglucanase | ✅ 中位 perplexity 8.61 | M |
| 24 類中 21 類 perplexity 都下降（對照） | ✅ 原文「Direction alone therefore proves nothing」 | M |
| perplexity 不是活性 | ✅ 原文「Nothing here measures substrate range」 | M |
| 第一批 codon-optimised、第二批沒有 | ✅ | P |
| 9-15 兩張膠、四個建構、無誘導差異 | ✅ CDS_0011 預測 72.0 kDa，空白 | PC |
| 9-29 CDS_0012 首次誘導依賴帶 | ✅ | PC |
| **10-01 e1 在預測分子量沖提，唯一成功；CDS_0011 短 29 kDa** | ✅ PC 說 e1 唯一；D 說 CDS_0011 短 29 kDa | PC, D |
| 10-10 Node281 沖提空白、flow-through = load | ✅ | PC, HP |
| Tolstorukov 2026-10-13 | ✅ | HP |
| dot blot e281 flow-through 2.9× | ✅ e1 lysate 2.4×、WT 1.1× | HP, PC |
| **spot test 的 1:10 稀釋在 blot 的偵測底線以下** | ✅ 原文「the protein in those drops was never shown to be there」 | PC |
| e1 中位 12%、Φ8 中位 0%、七株 | ✅ carry-over 對照未跑 | PC |
| 八次蛋白測定無 BL21 空載體道 | ✅ 七張膠 ＋ 一次 dot blot | C, HP |
| 兩株 pick 都是親本、非溶原 | ✅ 99.7–99.95% reads 回貼親本 | R |
| 70 個候選點回到 reads 檢查 | ✅ | R |
| F126L，263/264 vs 0/176、0/60、0/422 | ✅ OHPLIO_04215，4,643,730 T>C | R |
| 30 kb 莢膜多醣簇（4.64–4.67 Mb） | ✅ ABC export system、TagD、CapA | R |
| 9-2-1 R1 無確認突變 | ✅ | R |
| 兩個已打包 MIT 工具在 GitLab | ✅ `gelquant`、`phagecheck` | S, C |
| phagecheck 改掉了拓撲的結論 | ✅ | S |
| 植物園 86 acres／8 staff／copper 每 4–5 天 | ✅ 從未驗出 Pseudomonas | HP |
| IBC 有條件核准，條件是 host range | ✅ 0 VFDB / 0 CARD | HP, R |
| 基因體尚未寄存 | ✅ | C |

### 稿中刻意**不**講的（wiki 有但不適合口述）

- CDS_0011 兩個重疊片段的 pLDDT 93.2 對 64.7 不一致 —— 引單一數字會是 cherry-pick，所以整句不用。
- 07-04 那次有五株非定序菌株在 1:3000 呈陽性但稀釋後消失（可能污染或 prophage induction）。
- ZymCTRL 的 perplexity 絕對值約 7，遠高於模型自己說的 1.75 門檻。
- Strain 3 是 *P. capeferrum*，與另兩株 87.4–87.7% ANI。

**以上四點若 judge 在 Judging Session 問到，要答得出來。**

---

## 時間表

重建 PDF：`python code/1024_script_pdf/make_script_pdf.py`
（生成器的 `SRC` 需指向本檔。）

v4 仍是寫滿的版本，長度等這一輪科學細節確認後再一起砍。

---

## 念法備註

| 寫法 | 念法 |
|---|---|
| Phi-8 | *fye-eight* |
| pb-five × FhuA | *pee-bee-five* ／ *foo-ay* |
| beta-helix | *bay-ta* |
| CDS 11 / 12 / 24 | *C-D-S eleven* |
| endo-one-four-beta-glucanase | 逐段念，不要念 EC 編號 |
| *Pseudomonas* | *soo-doh-MOH-nas* |
| Tolstorukov | *tol-sto-ROO-kov* |
| ångström | *ANG-strom* |

---

## Log

- 2026-10-24 — v1 三幕；v2 四輪 DBTL ＋ HP；v3 依 wiki 補滿
- 2026-10-25 — **v4：逐句對照 wiki 科學細節。** 最大的修正是把 **CDS_0011（讀受體的 β-helix 尾刺）**
  與 **CDS_0012（做祖先重建的 GH5，TIM barrel，預測受質是 endoglucanase 的受質）** 徹底分開，
  並新增 C3.D2 回答「為什麼祖先做在另一個酵素上」（同源序列夠、蛋白小好表達、Twist 額度）。
  另修 8 結構/7 蛋白、CDS_0011 沖提短 29 kDa、spot test 稀釋在偵測底線以下、
  07-04 預測檢驗的三項保留、nine-fold 對照。加 §FC 逐項對照表
