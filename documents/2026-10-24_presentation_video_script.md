# Presentation Video — English narration script (v1)

故事正本見 [`2026-10-24_presentation_video_story.md`](2026-10-24_presentation_video_story.md)。
拍子與素材見 [`2026-10-24_presentation_video_outline.md`](2026-10-24_presentation_video_outline.md)。

**怎麼用這份**

- `>` 區塊裡的英文**就是要念的字**。其餘是導演註記，不念。
- 每節標了字數。最後有一張**累計時間表**，130 / 140 wpm 兩種語速都算了。
- 念的時候**當成在跟人講，不是在念稿**（handbook p.14 的評審回饋明講聽得出來）。
  句子寫得短，就是為了讓你可以停。標 `—` 的地方是停頓點。
- 數字**念出來**（`zero point one three seven`），不要念成「零點一三七」的英文直譯。

---

## COLD OPEN

> 🎬 promo 的 plaque assay 動畫。第二顆鏡頭：同一滴液體滴到另外兩株菌上，什麼都沒發生。

> A drop of phage goes onto a lawn of bacteria. A few hours later, there's a clear circle where the bacteria used to be.
>
> Move the same drop to the plate next door. Same phage. Different strain. Nothing.
>
> Phages are the most precise killers we know of — and that precision is the problem. If you want to treat an infection with a phage, you need a phage that matches the patient's strain. Most of the time, there isn't one on the shelf.
>
> What decides the match is the very first step. The phage has to recognise the cell surface and stick to it. And for bacteria that wrap themselves in sugar, that surface isn't protein at all.
>
> So what is the phage's tail actually recognising?

**131 字**

---

## ACT I — THE BOTTLENECK

> 🎬 幕卡 2.5 秒：`ACT I — THE BOTTLENECK` ／ *Why one phage only kills one host*

### I.1 我們的系統

> 🎬 採樣點地圖（**確認無國旗**）→ 細菌基因體圖 → Φ8 基因體圖。
> 畫面標註：MRA doi `10.1128/mra.00793-26`；`Phage genome assembly and annotation: Prof. J. Cesar Ignacio Espinoza`

> We went looking for our own system — water and soil from around our campus.
>
> We came back with three strains of *Pseudomonas*, distinct from one another, and one phage, Phi-8, that infects exactly one of them. About sixty-two kilobases, sharing almost no genes with anything described before. The three bacterial genomes are ours — sequenced, assembled and published. The phage genome was assembled and annotated by our PI.

**78 字**

### I.2 第一條線索

> 🎬 三株菌 O-antigen 基因座並排圖。畫面標 `prediction — not yet tested`。**這張圖 Act II 結尾原樣再出現一次。**

> Then we lined up the three strains at the one locus that builds their sugar coat.
>
> Same position in the genome. Same gene on either side. And inside — three cassettes with no homology to each other at all. Of forty-five gene clusters, four were shared.
>
> Three strains. Three different sugar coats. One phage that kills one of them.
>
> The prediction is sitting right there. Whatever Phi-8 recognises, it's that sugar.

**81 字**

### I.3 教科書

> 🎬 鎖與鑰匙示意。**β-helix tail spike 渲染圖第一次出現**，標 `the key?`

> But we didn't follow the sugar. We followed the textbook.
>
> The textbook says a phage's receptor-binding protein meets a protein on the bacterial surface. Lock and key — protein against protein. Work out which binding protein fits which receptor, and you've worked out host range.
>
> So that's what we set out to do.

**58 字**

---

## ACT II — THE WRONG KEY

> 🎬 幕卡 2.5 秒：`ACT II — THE WRONG KEY` ／ *Ten control folds decided the fate of 7,182*
>
> **這一幕是全片的賣點。** 節奏要穩：先讓方法看起來完全合理，再讓對照組推翻它，然後解釋為什麼。

### II.1 為什麼要用電腦

> 🎬 矩陣示意：114 × 63 = 7,182。接著一個「ipTM 0→1」的分數條示意。

> We had a hundred and fourteen candidate binding proteins, and sixty-three candidate receptors. That's seven thousand, one hundred and eighty-two combinations. Testing those at the bench is years of work.
>
> So we did what the field does. We asked a computer.
>
> Programs like AlphaFold predict the shape a protein folds into. Give them two proteins, and they'll also predict how the two fit together — and hand you back a number between zero and one. An interface score. High means: I'm confident these two dock, like this.
>
> The plan was to score all seven thousand pairs, and let the top of that list tell us where to start in the lab.
>
> Most of the next few months went into getting it to run at all.

**134 字**

### II.2 對照組

> 🎬 對照組設計圖（3 正 / 打亂 / 錯配）→ 切到 `2026-07-13_binding_controls_comparison.png`，紅框框住重疊區。
> **0.137 和 0.136 兩個數字要大，停在畫面上。**

> And then, late — too late — we added controls.
>
> A control here is a simple idea. Before you trust a method on a question you can't check, you give it questions you can.
>
> We picked three phage-receptor pairs that are known to bind. Known well enough that somebody has solved their structures experimentally, atom by atom. Then we built fakes — the same receptor with its sequence shuffled into nonsense, and pairs deliberately mismatched.
>
> If the method can tell binding from non-binding, the real pairs have to beat the fakes. That's the only bar it has to clear.
>
> The best-characterised pair we had was T-five's pb-five with FhuA — a complex that has been co-crystallised. It scored zero point one three seven.
>
> The same receptor, with its sequence shuffled into gibberish, scored zero point one three six.
>
> One thousandth apart.
>
> We assumed the tool was at fault, and rebuilt the whole thing with a different program, using real evolutionary data. It got worse. A deliberately mismatched pair scored zero point five — higher than every true binder in the set.

**186 字**

### II.3 機制

> 🎬 **全片解釋力的核心。** 兩條並排的信心柱：打亂後左邊崩掉（0.55→0.17），右邊幾乎不動。
> 然後 paired MSA 示意：噬菌體的同源都在噬菌體裡，細菌的都在細菌裡，兩個圈永不相交。

> One detail told us what was actually going on.
>
> These programs report two separate confidences. One is about the shape of the molecule itself. The other is about how the two pieces fit together.
>
> When we shuffled the sequence, the first number collapsed — from zero point five five down to zero point one seven. So the model noticed. It knew the shuffled protein wasn't a real protein.
>
> But the second number — the fit — barely moved.
>
> So the model wasn't being fooled by our fake. It had simply never had an opinion about the fit. Not for the fake, and not for the real pair either. It had been handing us a number that looked like an answer and wasn't one.
>
> Here's why.
>
> When AlphaFold predicts how two proteins touch, it isn't simulating physics. It's reading evolutionary history. It looks across thousands of species, finds both proteins in each one, and asks one question: when this spot on protein A changes, does that spot on protein B change to match? Two surfaces that have to keep fitting each other keep changing in step. That pattern is the fingerprint of contact.
>
> But that record only exists if the two proteins have been inherited together — in the same genome, for millions of years.
>
> A phage protein's relatives live in other phages. A bacterial protein's relatives live in other bacteria. They are never in the same genome. They have never been inherited together.
>
> So for a pair like ours, the evolutionary record of that interface isn't hard to find. It was never written.
>
> Which means this was never a result about our proteins. It's a limit of the method — and it holds for any phage and host, and for host and pathogen across kingdoms generally. More compute doesn't fix it.
>
> Ten control folds decided the fate of seven thousand. We never ran the real screen.

**300 字** — 最長的一節，刻意的。

### II.4 摺疊說了實話

> 🎬 **β-helix 渲染圖第二次出現**，標出氫鍵週期。接一個酵素在糖鏈上切開的動畫。
> 畫面小字：`CDS_0011 res 540–941`
> **結尾把 I.2 那張三套糖 cassette 的圖原樣再放一次。**

> So we stopped asking what the tail spike binds, and asked what it is. We folded it on its own.
>
> It came back as a right-handed beta-helix — a long triangular prism with a groove running down the side.
>
> That shape is a signature. Enzymes that cut long sugar chains look like this, and they look like this for a reason. A sugar chain is a long thread, and to cut it you need something that holds it straight and feeds it through. You can recognise a wood plane by its shape without being told what it cuts.
>
> Our tail spike wasn't a key. It was a blade — an enzyme for sugar.
>
> Which turns the whole question over. If the tail spike cuts sugar, then what the phage recognises is the sugar coat, and the protein lock we'd spent months looking for doesn't exist.
>
> The identity of the receptor didn't come from the docking. It came from the shape.
>
> And it points straight back to those three sugar coats.

**168 字**

### II.5 假說成形

> 🎬 署名要準確。B5／C9。

> We weren't the only ones reading it that way. Our own RBP-detection model had already flagged the protein as a depolymerase — and at about the same time, our PI reached the same conclusion from his own structural search.
>
> What he added was the step from an observation to something you can test.

**57 字**

---

## ACT III — THE ENZYME

> 🎬 幕卡 2.5 秒：`ACT III — THE ENZYME` ／ *If the ceiling is set by the enzyme, raise the enzyme*

### III.1 假說

> 🎬 一句話假說框，白底，停久一點。畫面標 `Hypothesis: Prof. J. Cesar Ignacio Espinoza`

> In bacteria that wrap themselves in sugar, the ceiling on a phage's host range is set by the substrate range of its depolymerase — not by the identity of its binding protein. And the narrow specificity we see today is a narrowed-down version of something broader in the past.
>
> That changes what you'd test. Not binding. Substrate range.
>
> And if today's enzymes are narrowed-down descendants, then the interesting experiment is to go back up the tree, and ask what the ancestor could do.

**86 字**

### III.2 目標

> 🎬 Φ8 基因體圖放大到 tail 模組，三個 CDS 標出來。**用正本編號。**

> Phi-8's tail module has two enzymes in it. The tail spike we've just been talking about — CDS eleven, with that beta-helix at its business end. And next to it, CDS twelve, a glycoside hydrolase from family five. There's also CDS ten, which is still an unknown protein. We expressed it to find out what it is.

**62 字**

### III.3 復活祖先

> 🎬 系統發生樹由末端往回合併 → 標出三個節點 → 身分矩陣 → ZymCTRL perplexity 趨勢。
> 整段標題列掛 `Phylogeny, ASR and ZymCTRL scoring: Prof. J. Cesar Ignacio Espinoza`
> ✂️ 三個 RMSD（0.28 / 0.50 / 0.52 Å）留畫面，不念。

> Our PI took CDS twelve, aligned its closest relatives, built a phylogeny, and reconstructed the ancestral sequence at every node on the path back to the root. Then he scored each reconstruction with a protein language model. The further back he went, the better the model liked it.
>
> We picked three of those nodes and had them synthesised. One is seventy-eight percent identical to the modern enzyme. The other two are about half identical to it — but eighty-seven percent identical to each other. So the panel is the modern enzyme, one close relative, and a pair of more distant cousins.
>
> Before any bench work, we asked whether those resurrected sequences still fold into the same enzyme. All three come back as the same TIM barrel.

**131 字**

### III.4 建構

> 🎬 六個建構一覽。**把 CDS_0011 res 305–941 和第二幕的 res 540–941 疊在同一條軸上**，
> 讓觀眾看見「第二幕認出來的那段，就在我們訂的那段裡面」。

> Six constructs, all with an N-terminal histidine tag, synthesised by Twist. The beta-helix piece of the tail spike itself. CDS twelve. Its three ancestors. And the unknown protein.
>
> That first one matters. The fragment we ordered contains exactly the beta-helix domain we'd identified by folding it. What the shape told us to look at is what we put in a tube.

**66 字**

### III.5 實驗台

> 🎬 膠圖，目標位置紅框。畫面標：`IPTG −/+ : present` ｜ `empty-vector control: RUNNING NOW` ｜ `n = 1`

> And then the bench — which is where we are right now.
>
> When we induce CDS twelve, we see a band in the right size range. To separate that band from host background we need an empty-vector control, and that control is on the bench as I'm speaking.
>
> The nickel purification of one ancestor failed. The elutions came off empty, and the flow-through looked like the load — so the protein never bound the column. We're repeating it with the binding conditions changed.
>
> So the enzyme arm is honest work in progress. I'd rather tell you exactly which part is unfinished than show you a cleaner story.

**119 字**

### III.6 乾淨的結果與安全

> 🎬 read pileup 圖，F126L 標出來 → O-antigen 基因座標 `unchanged` → `0 VFDB / 0 CARD` + IBC

> One line did come back clean.
>
> We raised mutants resistant to Phi-8, and sequenced them. One carries a single amino-acid change in a gene that builds the capsule — confirmed down at the level of the sequencing reads. And the sugar locus itself is untouched.
>
> On safety: Phi-8's genome carries no virulence factors and no antibiotic-resistance genes. Zero hits in either database. And the work has approval from our institutional biosafety committee.

**76 字**

---

## CODA — WHERE WE ARE

> 🎬 三欄：`Established` ／ `Predicted, not tested` ／ `Open`。逐欄淡入。

> So, plainly.
>
> Established: the genomes. Three unrelated sugar cassettes in one slot. A tail spike that turns out to be a sugar-cutting enzyme. A controlled negative result about interface prediction. One resistance mutation, confirmed in the reads.
>
> Predicted, but not yet tested: that Phi-8 won't infect the other two strains. That the ancestral enzymes have a broader substrate range.
>
> Still open: clean expression, an activity assay, and the topology of the phage genome.
>
> The cheapest next step is that control — and it's running. The decisive one is knocking out the sugar and watching whether the phage still sticks.
>
> And if there's one thing we'd hand to anyone starting a screen like ours — gate it on controls before you trust it.
>
> Ten folds told us the truth that seven thousand couldn't.

**143 字**

---

## CREDITS

> 🎬 無旁白，30 秒。隊員、PI、advisors、Twist、Artlist 曲名/作者/授權、工具
> （Claude、Pharokka、ESMFold、ColabFold、IQ-TREE、ZymCTRL、Foldseek、PyMOL）。**停留 ≥ 2 秒。**

---

## 累計時間表

旁白總字數 **1,802**（程式實測，已排除導演註記）。

| 段 | 字數 | 累計字 | @130 wpm | @140 wpm |
|---|---|---|---|---|
| Cold open | 126 | 126 | 0:58 | 0:54 |
| I.1 | 69 | 195 | 1:30 | 1:23 |
| I.2 | 71 | 266 | 2:02 | 1:54 |
| I.3 | 53 | 319 | 2:27 | 2:16 |
| II.1 | 125 | 444 | 3:24 | 3:10 |
| II.2 | 181 | 625 | 4:48 | 4:27 |
| II.3 | 316 | 941 | 7:14 | 6:43 |
| II.4 | 170 | 1111 | 8:32 | 7:56 |
| II.5 | 53 | 1164 | 8:57 | 8:18 |
| III.1 | 83 | 1247 | 9:35 | 8:54 |
| III.2 | 57 | 1304 | 10:01 | 9:18 |
| III.3 | 126 | 1430 | 11:00 | 10:12 |
| III.4 | 61 | 1491 | 11:28 | 10:39 |
| III.5 | 107 | 1598 | 12:17 | 11:24 |
| III.6 | 72 | 1670 | 12:50 | 11:55 |
| Coda | 132 | 1802 | 13:51 | 12:52 |
| ＋幕卡與片尾 | — | — | **14:29** | **13:30** |

⚠️ 130 wpm 是 **14:29**，140 wpm 是 **13:30**。兩種語速都在 15:00 以內。

你試念之後：

- 念出來**低於 14:00** → 現在這份直接用，還可以把 story 裡標 ✂️ 的兩段加回來。
- 念出來 **14:00–14:50** → 砍 II.1 的最後一句、III.2 的 CDS 十那句、Coda 的「So, plainly.」，約 −40 字。
- 念出來**超過 14:50** → 告訴我實際秒數，我重配各節預算，優先保 II.3。

---

## 念法備註

| 寫法 | 念法 |
|---|---|
| Phi-8 | *fye-eight* |
| pb-five × FhuA | *pee-bee-five* / *foo-ay* |
| beta-helix | *bay-ta* |
| TIM barrel | *tim barrel* |
| zero point one three seven | 一個數字一個數字念，不要念成 "point one thirty-seven" |
| *Pseudomonas* | *soo-doh-MOH-nas* |
| CDS eleven / twelve / ten | 不要念 "CDS zero zero one one" |

---

## Log

- 2026-10-24 — 初稿。依 story 的三幕結構寫出完整旁白，1,837 字（實測）；附逐節字數與 130/140 wpm 累計時間表；CDS 編號全部改用正本（`UUAIURNK_`），Act II 的 β-helix 標為 `CDS_0011 res 540–941`；加入 III.4「訂的那段包含第二幕認出的結構域」的連結；附念法備註
- 2026-10-24 — 字數改為程式實測值，時間表重算
- 2026-10-24 — 產生可批註 PDF（double space、行號、右側留白）；修正字數統計把中文導演註記誤計為口白的問題，實際口白 1,802 字
