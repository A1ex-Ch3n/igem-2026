# Presentation Video — 故事

全片的敘事正本。拍子表與素材對應見 [`2026-10-24_presentation_video_outline.md`](2026-10-24_presentation_video_outline.md)，
規格與評分依據見 [`2026-10-24_presentation_video_plan.md`](2026-10-24_presentation_video_plan.md)。

格式：**中文是結構與導演註記，`>` 引用的英文是旁白的語氣樣本**，不是最終逐字稿。
寫英文完整稿時以這份的順序與因果為準。

---

## 開場

一滴噬菌體落在鋪滿細菌的培養皿上。幾小時後，一個清澈的圓出現了——那裡的細菌全死了。

把同一滴液體移到隔壁的皿上。同一支噬菌體，另一株細菌。什麼都沒發生。

> Phages are the most precise killers we know of. That precision is also the problem.
> To treat an infection with a phage, you need a phage that matches the patient's strain.
> Most of the time, no such phage is on the shelf.

決定配不配得上的是**吸附**：噬菌體必須先認得細菌表面、黏上去，才談得上注入 DNA。而對那些把自己裹在多醣裡的細菌——莢膜、O-antigen——噬菌體碰到的表面根本不是蛋白質，是一層厚糖。

所以問題變成：噬菌體的尾巴，到底認得什麼？

---

## ACT I — The Bottleneck

> We went and found our own system. Water and soil from around campus.

三株 *Pseudomonas*，彼此在 ANI 上互相區分。一支噬菌體 Φ8，只感染其中一株。約 62 kb，和已知噬菌體幾乎不共享 ortholog——是新的。

**署名**：三株細菌的基因體是我們定序、組裝、發表的（MRA）；噬菌體的基因體由 PI 從 metagenomic reads 組裝註解。

然後出現了一個後來證明很重要的細節。我們把三株菌的 O-antigen 基因座排在一起：**同一個槽位，同一個基因側翼，裡面裝的是三套完全不同源的 cassette。**45 個 ortholog cluster，只有 4 個共享。

三株菌，三件不同的糖外衣。而噬菌體只殺得死其中一株。

> The prediction is sitting right there: whatever Φ8 recognises, it is that sugar.

但我們沒有跟著糖走。我們跟著教科書走。教科書說：receptor-binding protein 對上外膜蛋白，鎖與鑰匙，蛋白對蛋白。只要預測哪條 RBP 結合哪個受體，就預測了宿主範圍。

> 🎬 **伏筆**。三套糖 cassette 的圖在這裡出現，Act II 結尾原圖再放一次回收。

---

## ACT II — The Wrong Key

> 🎬 這一幕是全片的賣點，也是最容易讓非專業觀眾掉隊的地方。
> 節奏：**先讓方法看起來完全合理** → 對照組推翻它 → **解釋為什麼** → 摺疊給出真答案。
> 每一個專有名詞出現時，當場用一句日常語言解釋，不要留到後面。

### II.1 為什麼要用電腦

我們有 114 條 receptor-binding protein 和 63 個候選受體，**7,182 種組合**。在實驗台上一組一組測，是好幾年的工作。所以我們做了這個領域都在做的事：問電腦。

> Programs like AlphaFold predict what shape a protein folds into.
> Give them two proteins, and they will also try to predict **how the two fit together**,
> and hand you a number between 0 and 1 — an interface score.
> High means: I am confident these two dock, like this.

計畫是把 7,182 組都打分，讓排在最前面的那幾組告訴我們，實驗該從哪裡開始。

幾個月花在讓它「跑得動」：GPU 驅動、MSA 伺服器、換了一個又一個工具。

### II.2 對照組

然後，很晚——**太晚了**——我們才加上對照組。

> A control here is simple. Before you trust a method on questions whose answers you do not know,
> you give it questions whose answers you do.

我們挑了三組**已知會結合**的噬菌體—受體配對，已知到它們的結構被實驗解出來、一個原子一個原子擺好。然後我們做假的：同一個受體，把序列打亂成亂碼；以及故意配錯的組合。

> If the method can tell binding from non-binding, the real pairs have to beat the fakes.
> That is the only bar it has to clear.

結果：

> The best-characterised pair we had — T5's pb5 with FhuA, a complex that has been co-crystallised —
> scored **0.137**.
> The same receptor, with its sequence shuffled into gibberish, scored **0.136**.

差千分之一。**那個方法分不出一個解過結構的真複合物和一團亂碼。**

我們以為是工具的問題。所以換了另一套程式、改用真實的演化資料重建一次。結果更糟：一組**故意配錯**的組合拿到 **0.50**，高過每一個真結合對。

### II.3 到底哪裡出錯（機制）

> 🎬 **這一小段是全片解釋力的核心。** 如果觀眾只聽懂一段，要是這一段。

有一個細節說明了問題在哪。這些程式會回報**兩個分開的信心分數**：一個是「這個分子本身長成這樣，我有多確定」，另一個是「這兩塊這樣拼在一起，我有多確定」。

把序列打亂之後：

- 第一個分數**崩掉了**——0.55 掉到 0.17。模型注意到了，它知道那串亂碼不是真的蛋白質。
- 第二個分數——也就是「怎麼拼」——**幾乎沒動**。

> So the model was not fooled by the fake. It simply never had an opinion about the fit —
> not for the fake, and not for the real one either.
> It had been handing us a number that looked like an answer and wasn't.

**為什麼？**

> When AlphaFold predicts how two proteins touch, it is not simulating physics.
> It is reading evolutionary history.

它的做法是：跨越幾千個物種，在每個物種裡同時找到這兩個蛋白，然後問一個問題——**當 A 蛋白的這個位置變了，B 蛋白的那個位置有沒有跟著變？**

兩個表面如果必須一直互相貼合，它們就會一起改變。那個「一起改變」的模式，就是接觸的指紋，而那正是模型在讀的東西。

> But that record only exists if the two proteins have been inherited **together**,
> in the same genome, for millions of years.

而噬菌體蛋白的親戚住在別的噬菌體裡，細菌蛋白的親戚住在別的細菌裡。**它們從來不在同一個基因組裡，從來沒有被一起遺傳過。**

對這一類配對來說，那份接觸的演化紀錄不是我們沒找到——**是從來沒有被寫下來過。**

> Which means this was never a result about our proteins.
> It is a limit of the method, and it applies to any phage-and-host pair —
> and to host-and-pathogen pairs across kingdoms generally.
> No amount of compute gets around it.

**十個對照折疊，決定了 7,182 組的命運。那場正式篩選，我們從來沒有跑。**

### II.4 摺疊說了實話

於是我們不再問「這個 tail spike 跟什麼結合」，改問「**這個 tail spike 是什麼**」。我們把它單獨折出來。

它回來是一個**右手 β-helix**：一根細長的三角柱，側面有一道溝槽貫穿整個長度。

> That shape is a signature.
> Enzymes that cut long sugar chains look like this, and they look like this for a reason:
> a sugar chain is a long thread, and to cut it you need something that holds it straight
> and feeds it through.
> You can recognise a wood plane by its shape without being told what it cuts.

我們的 tail spike 不是一把鑰匙。**它是一把刀。一把切糖的刀。**

這把整個問題翻過來了。如果 tail spike 是一個切糖的酵素，那噬菌體認的就是那層糖外衣——而**我們花了好幾個月在找的那把蛋白質的鎖，根本不存在。**

> The identity of the receptor did not come from the docking. It came from the shape.

> 🎬 **伏筆回收**：這裡把 Act I 那張三套糖 cassette 的圖**原樣再放一次**。
> 三株菌、三件不同的糖外衣、一支只殺得死其中一株的噬菌體。

### II.5 假說成形

> 🎬 署名要準確。這是 §3B 的 B5／C9，而出處標註是過去兩年最弱的一題。

我們自己跑的 RBP 偵測模型，已經把這個蛋白指向 depolymerase 或相近的已知酵素。幾乎在同一時間，PI 從他自己的結構搜尋得到同樣的判讀。

> We and our PI arrived at the same reading of the protein at about the same time —
> ours from the RBP-detection model and the fold, his from his own structural search.
> Together we turned that observation into something you can test.

**PI 加上的那一步，是把一個觀察變成一個可以測的假說。**

---

## ACT III — The Enzyme

> In capsulated bacteria, the ceiling on host range is set by the **substrate range of the
> depolymerase** — not by the identity of the RBP.
> And the narrow specificity we see today is derived from a broader ancestral activity.

這個假說可以測，而且它改變了**該測什麼**。不是結合，是**受質範圍**。而如果今天的窄專一性是從更廣的祖先活性窄化來的，那最有意思的實驗，是往樹上回溯。

目標是 CDS_0012，Φ8 尾部模組裡一個 GH5 家族的醣苷水解酶。旁邊 CDS_0011 是 tail fibre。還有 CDS_0010，到現在仍是未知功能蛋白——我們把它一起表達，就是為了弄清楚它是什麼。

**署名**：PI 對齊同源序列、建樹，沿著從 CDS_0012 回到根部的每一個節點重建祖先序列，再用蛋白質語言模型打分。**越祖先的節點，perplexity 越低。**

我們挑了三個節點送合成。一個對野生型 77.8% 相同；另外兩個對野生型大約 51% 和 53%，但彼此 87%——所以這組是野生型、一個近親、加一對較遠的姊妹序列。

在進實驗室之前，我們先問：這些被復活的序列，還折得出同一個酵素嗎？三個都落在同一個 TIM barrel 上，半個 Å 以內。我們也用兩種不同方法折同一條野生型，彼此差 0.28 Å——這告訴我們比較本身是可靠的。

六個建構，全部帶 N 端 His-tag，由 Twist 合成。

然後是實驗台。**我們現在就在這裡。**

> 🎬 語氣：向前看，不自我鞭打。照 EPFL 的句型 —— 假說 → 做了什麼 → 結果 → 下一步。

誘導 CDS_0012 之後，我們在正確的大小範圍看到一條帶。要把那條帶和宿主背景分開，需要空載體對照——**那個對照此刻正在跑**。其中一個祖先的 Ni-NTA 純化失敗了：沖提道是空的，流穿看起來和上樣一樣，蛋白根本沒結上管柱——我們正在改結合條件重做。

有一條線確實做出了乾淨的結果。我們篩出對 Φ8 產生抗性的突變株並定序，其中一株帶有莢膜型別基因上的單一胺基酸改變，在 reads 層級確認。而 O-antigen 基因座本身沒有變動。

安全方面：Φ8 的基因體裡沒有任何毒力因子、沒有任何抗藥基因——兩個資料庫都是零命中——而這項工作有 IBC 核准。

---

## CODA — Where We Are

**已確立**：三株細菌和一支新噬菌體的基因體、三套互不同源的糖 cassette、depolymerase 的摺疊、那個有對照把關的負面結果、一個經 reads 確認的抗性突變。

**預測但未驗證**：Φ8 不會感染另外兩株；祖先酵素的受質範圍比較廣。

**仍未解決**：乾淨的表達與純化、酵素活性測定、基因體拓撲。

最便宜的下一步是那個對照——正在跑。決定性的一步是 O-antigen 剔除的吸附實驗。

> Gate your in-silico screen on controls before you trust it.
> Ten folds told us the truth that seven thousand could not.

---

## 時間預算警告

Act II 為了對非專業觀眾解釋清楚，從 3:40 增加到約 **4:30**，全片會來到約 **14:50**，
超過成品檔 13:30–14:30 的目標（900 秒是上傳器硬上限）。

要拿回約 40 秒，建議從這兩處擇一或並用：

1. **Act I 的基因體段壓縮**（約 −25 秒）：62 kb、novel、MRA 一句話帶過，不展開 ortholog 統計。
2. **Act III 的結構檢查段壓縮**（約 −20 秒）：三個 RMSD 數字留在畫面上，旁白只講「三個都折回同一個酵素」，不逐一念數字。

不建議動 Act II 的解釋段落——那是這支片的賣點。

---

## Log

- 2026-10-24 — 初稿（口述版，先貼在對話中未存檔）
- 2026-10-24 — 建檔。依 Alex 回饋修訂三處：Act II 重寫，為非專業觀眾補上「為什麼要用電腦」「什麼是對照組」「兩個信心分數的差別」「共演化紀錄為何不存在」「β-helix 為何指向糖」五段解釋；PI 的角色改為**同時判讀、共同提出假說**，而非我們帶結果去找他；BL21 空載體對照改為「正在跑」。加入時間預算警告與兩個壓縮方案
