# Presentation Video — 2026 討論稿

## 0. 狀態

- **死線：2026-10-28 15:00 UTC**，也就是台北 10/28 23:00、Claremont 10/28 08:00 PDT（美國 11/1 才結束夏令時間，所以還是 PDT）。來源：`GET https://api.igem.org/v1/competitions/58a7e73a-1e25-457f-9f59-36c47b3f652a/deliverables`，`video-team-presentation`，`required: true`，`phase: open`。2026-10-24 抓取。
- **必交**，屬於 Bronze 的必要 deliverable（Wiki、Judging Form、Presentation Video、Judging Session）。Judging Form 上已經勾了「has and will fully complete」，這支片是那個承諾。
- **目前進度：零。** 還沒有稿子、投影片或錄音。
- 這份是討論稿，還不是腳本。先把第 1 節的決定做完，再寫稿。

---

## 1. 待決定（請逐題回答）

**D1. 形式** — ✅ **已定（2026-10-24）：Hamburg 式的投影片主體，加上 TU-Eindhoven 式的真人開場和收尾**（見 §3A）。以下是原本的選項，保留作紀錄。
- (a) 投影片加隊員真人錄音，螢幕錄影或 Keynote/PowerPoint 匯出影片
- (b) 全片 Remotion 動畫，沿用 `code/0811_promo_video/`
- (c) 混合：以投影片加真人錄音為主幹，片頭、吸附機制、plaque assay 等段落直接剪入 promo 的動畫片段

剩 4 天，做 10 分鐘以上的全動畫不實際：promo 只有 115 秒，就做了兩天。**建議 (c)**。

**D2. 誰講、誰出鏡**
- 一人講完，或每段換人講。
- 要不要露臉（例如片頭隊員自我介紹、子母畫面）？出鏡的人都要知情同意，未滿 18 歲的要有監護人同意。

**D3. 配音** — ✅ **已定（2026-10-24）：隊員自己配音。**
- 剪入的 promo 片段只用畫面，不用 ElevenLabs 配音，這樣不會牽涉新的 AI 素材。

**D4. 目標長度** — ⚠️ 原本建議 10–12 分鐘，**看了 2025 數據後需要重談**（見 §3.4）。
- 2025 年 395 支 Team Presentation 的中位數是 **14.5 分鐘**，四支 Best Presentation 得獎片都在 **13.7–15 分鐘**。

**D5. 背景音樂** — ✅ **已定（2026-10-24）：用 Artlist 這類 stock 平台。**
- 規則面沒問題。FAQ 原文：「Material released under CC0, CC BY, or a stock platform licence permitting free reuse is acceptable.」
- **還沒解決：Attributions Form 已在 10/21 凍結**（API：`attribution-form`，`open: false`，`freeze: true`）。FAQ 要求「record every external item on your Attributions Form」，Artlist 的曲子無法補登，表上目前只有 promo 用的 ElevenLabs/Suno。可能的做法：
  - (a) 片尾字卡完整列出 title / creator / Artlist licence，這部分一定要做；
  - (b) 寫信問 iGEM HQ，凍結後能否補登一筆，或只列片尾字卡是否就夠。
- **待確認 Artlist 方案條款**：上傳到 video.igem.org（PeerTube，公開播放）是否在方案的授權範圍內；退訂後已下載的曲子是否仍有授權。

**D6. 分工與時程**
- 誰寫稿、誰做投影片、誰錄音、誰剪接上傳？各自的截止時間？倒推時程草案見第 7 節。

**D7. 和 Judging Session 共用骨架嗎？**
- Judging Session 在 11/13 07:35–08:00 PST，開頭有 5 分鐘 project overview。judge 會先看過這支片再進場。**建議**這支片的投影片當作母版，5 分鐘版本從裡面抽。

---

## 2. 2026 官方要求

來源是以下五個前端 chunk，2026-10-24 抓取（兩個網站都是 SPA，規則文字只存在 JS chunk 裡）：

- `teams.igem.org/assets/videoPaths-FY191FQN.js`
- `teams.igem.org/assets/VideoDeliverable-CFqA-JpH.js`
- `teams.igem.org/assets/EditVideoSubmission-DSPw4XFm.js`
- `competition.igem.org/assets/deliverablesData-CPz8PTSL.js`
- `competition.igem.org/assets/Awards-qHVorymG.js`

### 技術規格

| 項目 | 規格 | 原文 / 程式碼 |
|---|---|---|
| 長度 | **≤ 15 分鐘**（不含 iGEM Intro） | `Up to 15 minutes (excluding iGEM Intro)`，`duration:900` |
| 檔案大小 | **≤ 1 GB** | `Up to 1GB`，`size:1e3` |
| 格式 | **.mp4** | `mimeTypes:["video/mp4"]` |
| 解析度 | **1080p 或 4K，橫向** | `1080p or 4k, Landscape`，`minHeight:1080`，`maxHeight:4e3` |
| 字幕 | **.vtt，另外上傳，不可燒進畫面** | `Do not embed subtitles directly into your video file. Captions must be submitted as a separate .vtt file.` |
| 必填欄位 | 影片檔、標題、描述 | `submissionContent: ["Video File", "Title and Description"]` |

promo 的經驗（見 `2026-08-11_promotional_script.md` §1），這次一樣適用：

- 上傳器會檢查 MP4 內部的 brand label，QuickTime、iPhone、iPad 匯出的檔案常被擋。修法：`ffmpeg -i input.mp4 -c copy fixed.mp4`（不重新編碼），或用 HandBrake 的 `Fast 1080p30` preset。promo 當時就需要 `ClaremontCA_fixed.mp4`。
- **標題**由 iGEM 組成 `<隊名>: <標題> (2026) - <類型>`，全長上限 120 字元，超過會被截成 `...`（`videoPaths` 的 `je()`）。後綴「 (2026) - Team Presentation」和 promo 的「 (2026) - Project Promotion」一樣是 27 字元，所以標題預算和 promo 相同，約 80 字元。隊名前綴的確切字串在上傳頁上確認，不要直接沿用 promo 稿的推測。
- 自動字幕會有錯，要下載、修正、重傳。teams 網站上有 VTT Validator 分頁。

### 流程（和 promo 不同的地方）

- **Presentation video 不會個別審核。** 原文：`Presentation videos aren't individually reviewed — your submission stays here until the deadline, then it's published automatically.`
- **只要在死線前到「Submitted」就算完成**，也就是影片上傳完成、標題和摘要都填好：`Reaching "Submitted" on your side before the deadline is what counts`。
- 後果：**沒有 moderator 幫忙把關。** 如果違規（國旗、未授權音樂、把虛構影像當成實驗結果），影片會原樣公開。檢查只能靠我們自己（見第 8 節）。
- 死線過後自動公開到 video.igem.org。

### 內容範圍

`deliverablesData` 原文：

> A presentation in video format covering your team's entire project — its background, technical and scientific content, design, methodology, results, human practices, etc. Judges review this video ahead of your Judging Session, and it is made publicly available for anyone to watch.

### 內容規則（與 promo 相同）

- `Narration is required to be in English.` 系統會比對自動字幕和提交語言（`The automatically generated captions do not match the submission language.`）。
- `Copyright Material is NOT allowed`：只能用 CC0、CC BY，或授權允許「剪入改作品」和「公開發布」兩者的素材。
- `Please credit everyone who contributed to the video (even people outside of your team) at the end by text on the screen for at least 2 seconds.`
- AI 生成素材可以用，但要自己下 prompt 生成、工具條款允許發布、片尾具名，並登記在 Attributions Form（**已凍結**，見 D3）。
- 出鏡者要知情同意。
- `Country flags are not permitted in any form.`
- 禁止仇恨言論、騷擾、扮演病人或障礙者、刻板印象，以及對競爭者、具名機構或真實人物的未經證實指涉。
- 避免快速閃爍、頻閃和強烈的運動特效。
- 不得把虛構影像呈現成本隊的實驗結果（AI 圖和示意動畫都要標「schematic」）。

---

## 3. 評分標準（討論中）

### 3.1 這支片影響哪些分數

`competition.igem.org/assets/Awards-qHVorymG.js` 原文：

- **主 ballot**：「Project Awards are determined by the weighted scores of the **Project**, **Presentation**, and **Wiki** sections of the ballot, ranked against every other team.」所以 Presentation 是三大區塊之一，會影響 Village Award 和總排名，不只影響單項獎。權重沒有公開。
- 「The Presentation and Wiki sections use the same ballot questions as the Best Presentation and Best Wiki Special Awards.」所以同一組 5 題，一次算兩個地方。
- **Best Presentation**（All Teams）：「A great presentation tells your team's story clearly and presents your data in a concise, visually appealing way to a **scientific and engineering audience**.」，「Standard URL: None. Judges will evaluate your Team Presentation Video.」
- judge 會**先**看這支片，再進 11/13 的 Judging Session（`deliverablesData`：「Judges have already reviewed your Wiki and Presentation Video beforehand」）。主 ballot 的 Project 區塊有一題「How competent was the team, collectively, at answering judge questions?」，所以片子講過的東西，現場會被追問。

### 3.2 計分方式

每題 1–6 分。每題各分數的具體措辭**刻意不公開**（「so that teams stay focused on answering the broader question」），公開的只有通用量表：

| 分 | 通用描述 |
|---|---|
| 1 | Poor work done or completely absent. |
| 2 | Less work done; multiple missing components. |
| 3 | Some work done; incomplete. |
| 4 | Good work; complete. |
| 5 | Great work; complete with some impressive components. |
| 6 | Amazing work; impressive. |

解讀：**4 分的門檻是「complete」**，也就是 `deliverablesData` 列的範圍要全部講到：background、technical and scientific content、design、methodology、results、human practices。少一塊就掉到 3 分。5–6 分才看「impressive」。所以先求完整，再求亮點。

### 3.3 五題逐題拆解

| # | 原文 | judge 實際在看什麼（我們的解讀） | 對形式和剪輯的影響 | 我們的弱點 / 機會 |
|---|---|---|---|---|
| Q1 | How well did the team communicate their project **goals, design, and results** with **convincing evidence**? | 目標清不清楚；設計和目標是否扣在一起；結論有沒有證據撐 | 開場 60–90 秒講清楚中心假說；中途有 roadmap / 章節卡；每個 claim 都配一張證據圖 | 中心假說（depolymerase 受質範圍決定宿主上限）很強，但**直接驗證它的實驗還沒成功**。要把「假說 → 我們做到哪一步 → 下一步」講誠實 |
| Q2 | How well does this presentation convey what the team accomplished through their **technical data or results (either modeled or experimentally measured)**? | 真的數據，不是示意圖；**明確接受 modeled 結果** | 數據圖在畫面上要停夠久，旁白要指著圖講（「左邊這條帶是…」）；軸和標籤在 1080p 下要看得清楚；用高亮或框選引導視線 | 濕實驗弱（Ni-NTA 失敗、spot test inconclusive）。強項在 genomic / 計算結果：MRA 已發表、三套 O-antigen 基因組、resistant mutant WGS（CR3 F126L）、結構預測。**這題的分數主要靠這些** |
| Q3 | Does the **visual design** of the presentation **support the communication of the technical content** (project design, results and data analysis, and conclusions)? | 好看是次要的，重點是設計有沒有幫助理解 | 統一模板、一張一個重點；用動畫依旁白順序逐步出現元素，而不是整頁文字；promo 的機制動畫可以用在「解釋設計」的段落 | promo 已經有一套視覺語言（莫蘭迪配色、吸附 3D、plaque assay），直接加分 |
| Q4 | Did you find the presentation **engaging**? | 15 分鐘能不能撐住 judge 的注意力 | 隊員本人的聲音；有故事線；節奏要有變化（數據段 vs 動畫段 vs 露臉段）；音樂壓在人聲底下 | 「從校園水和土裡挖到一隻新噬菌體」本身就是好故事；負結果也可以講成「我們怎麼發現這條路走不通」 |
| Q5 | Were images, prior work, background information, and supporting data **acknowledged appropriately**? | 引用、圖片來源、他人的工作有沒有標出來 | 每張外部圖角落標來源；文獻在畫面上標作者和年份；片尾字卡 | **PI 的工作（ASR、ZymCTRL、噬菌體組裝、Foldseek）一定要標名**，否則同時扣 Q5 和主 ballot 的「initiated and led by the students」 |

### 3.4 2025 年的參考數據

來源：`api.igem.org/v1/competitions/d615db72-…/awards/results`（得獎名單），以及 `video.igem.org/api/v1/search/videos`（PeerTube，片長），2026-10-24 抓取。

**片長分布**：2025 年 395 支 Team Presentation，中位數 **14.5 分鐘**。

| 長度 | 支數 |
|---|---|
| < 8 分 | 9 |
| 8–10 分 | 9 |
| 10–12 分 | 27 |
| 12–14 分 | 108 |
| 14–15.5 分 | 242 |

（PeerTube 的長度包含 iGEM Intro，所以 15.1 分也算合規。）

**2025 Best Presentation 得獎片**：

| 組別 | 隊伍 | 長度 | 連結 |
|---|---|---|---|
| undergrad | EPFL（Pyronix） | 14.9 分 | https://video.igem.org/w/4AbQTx2JqnHrfGPjFywoGE |
| undergrad | TU-Eindhoven（BRIGHT） | 15.1 分 | https://video.igem.org/w/41E4P31pPxS3hmv6BsyMWi |
| overgrad | Brno Czech Republic | 13.7 分 | https://video.igem.org/w/gfy1XN38pQJffDGhPx7qVo |
| high school | Boston-BOSLab（BloomBusters） | 15.0 分 | https://video.igem.org/w/8QHUT5awxuQNMSDgT23xXP |

**EPFL 的時間分配**（從自動字幕逐分鐘整理；全片約 1,790 字，約 120 wpm）：

| 分鐘 | 內容 |
|---|---|
| 0–1 | Hook（野火數據）→ 現有方案的問題 → 他們的方案總覽 |
| 1–6 | 濕實驗設計逐模組講解，包括失敗和改版（「didn't result in higher levels of…」） |
| 6–9 | 硬體（無人機） |
| 9–10 | 軟體和數據分析 |
| 10–11 | 結果（burn test，含對照組設計） |
| 11–13 | Human Practices：訪談對象 → 每個人的意見如何改變設計 |
| 13–14 | 影響（SDGs）、教育推廣 |

觀察：
- 得獎片幾乎都用滿 15 分鐘。「complete」需要時間。
- EPFL 直接講失敗和改版，沒有隱藏，這對我們的 Ni-NTA 和 spot test 是好的參考。
- HP 段落的寫法是「誰說了什麼 → 我們改了什麼」，和主 ballot 的 HP 題目同一個邏輯。

### 3.5 2026 Judging Handbook 的線索

來源：[`2026-10-24_judge_handbook_2026_v5.pdf`](2026-10-24_judge_handbook_2026_v5.pdf)（原檔名 `2026-judge-handbook-digital-v5.pdf`，108 頁），2026-10-24 讀。頁碼是 handbook 印刷頁碼。

#### (a) 最重要的發現：這支片也被拿來打 **Project 區塊**的分數

p.32 原文：

> We can review presentation videos and wikis to determine what winning teams did to score well on all of the aspects above **except number 4**. How competent was the team, collectively, at answering judge questions? To judge this aspect, judges will primarily use the discussion time during the Judging Session.

「aspects above」指的是 Project 區塊的 10 題（p.31）。所以 judge 會用影片加 wiki 來打 Project 的 9 題，第 4 題（現場答問）除外。而 Project 區塊是「**the main determinant for choosing finalists**」（p.31）。

p.11 也寫明 judge 的準備方式：「In most cases, the Team Wiki and Project Presentation Video (15 minutes each) will be the core materials」，必要時再看 Registry、GitLab、**Attribution Form**、Safety Form。

**影響**：這支片不只要回答 Presentation 的 5 題，Project 的 9 題也都要在片中有對應的段落。對照表：

| Project 題（p.31 原文） | 片中要出現什麼 |
|---|---|
| 1. How well were engineering principles used (e.g., design-build-test cycle, use of standards, modularity, etc.)? | 明確的 DBTL 循環：binding screen → 對照組失敗 → 淘汰 → 轉向 depolymerase |
| 2. Did the team design a project based on synthetic biology and standard components (BioBricks, software, etc.)? | 6 個 pET-28a parts、Registry 編號、軟體 |
| 3. Did the project work or is it likely to work? | 什麼成功了（基因體、O-antigen、resistant mutant）、什麼還沒成功、為什麼仍然可能成功 |
| 5. How well did the team's data (modeled and/or experimentally measured) support their claims? | 每個 claim 配證據；claim 不能超過證據（§4） |
| 6. Is the project likely to have an impact? | 宿主範圍 → 噬菌體療法 / 抗藥性的意義 |
| 7. How well did the team demonstrate that their Human Practices work influenced the design, execution, application…? | HP：誰說了什麼 → 我們改了什麼 |
| 8. To what extent did they convince you that their Human Practices activities helped create a project that is responsible and good for the world? | 安全（IBC、0 VFDB / 0 CARD）、責任 |
| 9. Are the project components well documented on the team's Wiki/Registry pages? | 畫面上指出 wiki 和 Registry 的位置 |
| 10. How much of the project was initiated and led by the students? | 學生主導的部分講清楚，PI 的部分標名（§4） |

#### (b) Presentation 專章（p.85–86）

Summary 原文：

> - The presentation is the chance for a team to tell their story in a concise and visually appealing way.
> - Teams prepare video presentations up to 15 minutes long, which will be viewable to judges before the Grand Jamboree.
> - Excellent presentation videos are **engaging**, **easily understood by a scientific/engineering community**, **balance big-picture ideas with design details**, and **flow smoothly**.
> - Teams should present their work while **thoroughly acknowledging inspiration, background information, prior work and outside support**.
>
> … **Above all, each team should tell a story** as they present their work.

Handbook 舉的兩個得獎範例，judge 稱讚的點：

**TUDelft 2020**（19.2 分；當年上限 20 分鐘）
- 「multiple student team members present the project」：多人講。
- 先清楚講問題，再用「easy-to-follow figures」講基因線路。
- 「**did not oversell their project, nor did they use distracting graphics or flashy elements to advertize their work**」
- 涵蓋 goals、technologies、experimental designs、modeling and laboratory results、synergistic activities、future plans。
- 照片、文字框、影片片段、彩色圖「amplified the team's message and were not distracting」。
- 技術內容以外，也講了 engagement、safety risk assessment、entrepreneurship。

**Hamburg 2023**（14.7 分；這隊同年拿 Grand Prize 和 Best Presentation，p.39）
- 「slides are simple yet effective and informative」
- 「used many illustrations of the protein to guide the audience through the project」：用同一個蛋白質圖像當導覽主線。
- iHP 和 Education 用「simple flow charts」，outlook 用「straightforward slides」。
- 「clear and simple text throughout the video was easy to understand and **complementary to the spoken presentation**」：畫面文字是補充旁白，不是重複旁白。
- 「good contrast color palettes」

#### (c) 失敗和誠實：handbook 一再肯定

- p.16：「success and failure are equally valuable since they both provide answers to the question at hand」，並引用 Petroski：「Failure is central to engineering.」
- p.34（finalist 案例）：「They demonstrated where the project succeeded or failed. **They discussed their failed results.** They used iterative engineering to step back and fix parts of the project that weren't working.」
- p.73（Model 範例）：隊伍承認模型對不上實驗，「it is important and impressive that the team acknowledged what they could and could not accomplish」。
- p.20：「It is better that a team presents and acknowledges limited, qualitative assessments than they attempt to report flawed quantitative measurements.」
- p.22：「Approaching limitations with integrity」

**但有一個陷阱**。p.14 judge 回饋範例：「much of your work under the engineering criterion **reads more like routine troubleshooting than actual design-driven engineering**.」所以失敗要講成「假說 → 設計 → 測試 → 學到什麼 → 改設計」，不能只是列出「這個失敗、那個也失敗」。

#### (d) 旁白

p.14 judge 回饋範例：「Your video was great. I loved the paper artwork and motions. One minor suggestion would be to **try to not read off a script**.」judge 聽得出來在念稿。自己配音要先練到能用講的語氣，不要逐字念。

#### (e) Judging Session（p.11）

「Teams will give a 5-minute short summary of their project using any support they need (video, wiki page, slides). Then you will have 20 minutes to ask questions」。所以 5 分鐘版本可以直接用這支片的投影片剪。

#### (f) 綜合：形式上的結論

1. **一條故事線貫穿全片**，例如 Hamburg 的蛋白質導覽。我們的候選是 Φ8 的尾部或 depolymerase 這個圖像。
2. **簡潔、不浮誇**。動畫只用在能幫助解釋機制的地方；畫面文字補充旁白，不重複旁白。
3. **完整**：Project 的 9 題加上 Presentation 的 5 題都要有對應段落。15 分鐘用得到。
4. **失敗講成 DBTL**，不要講成 troubleshooting 清單。
5. **多人講，不念稿。**
6. **出處和 PI 的工作在畫面上標清楚**，並且和 Attribution Form 一致，因為 judge 可能會對照看。

### 3.6 要討論的問題

1. **長度**：依照 §3.4 改成 13–14.5 分鐘嗎？§3.5(a) 讓理由更充分：這支片要撐起 Project 的 9 題加上 Presentation 的 5 題。代價是稿子從約 1,400 字增加到約 1,700 字，而只剩 4 天。
2. **證據主軸**：results 的重心放在 genomic / 計算結果，濕實驗講成 DBTL 加失敗分析。§3.5(c) 支持這個方向，但要避開「troubleshooting 清單」的陷阱。
3. **故事線的圖像**：用 Φ8 的尾部或 depolymerase，還是用「從校園採樣到新噬菌體」的旅程？
4. **幾個人講**：handbook 稱讚多人講。誰講哪一段？
5. **要露臉嗎？**
6. **PI 的工作怎麼標示**：每張相關投影片的角落都標，還是在章節卡上統一標？

---

## 3A. 正面範本：形式拆解

方法：從 video.igem.org 下載 480p 檔，每 30 秒抽一張畫面，逐張看過；EPFL 另外讀了自動字幕。2026-10-24 做。下面的時間點是抽樣畫面的時間，精度 ±15 秒。縮圖表在 `/private/tmp/claude-501/-Users-alexy-Desktop-iGEM-26/77c93b6d-bdc5-452e-8971-b54893d1cd43/scratchpad/videos/sheets/`（別隊的作品，只放 scratchpad，不進 repo）。

五支片的形式可以分成四種：

| 形式 | 代表 | 製作難度 | 4 天內可行？ |
|---|---|---|---|
| A. 純投影片加旁白 | Hamburg 2023 | 低 | ✅ |
| B. 主播式：講者站著，旁邊彈出圖卡 | TUDelft 2020 | 中 | △，需要乾淨背景加穩定收音 |
| C. 混合：真人開場和收尾，中段是投影片或動畫 | TU-Eindhoven 2025 | 中 | ✅，真人部分只有 2–3 分鐘 |
| D. 紀錄片：多地點實拍、訪談、空拍 | EPFL 2025、Brno 2025 | 高 | ❌ |

### A. Hamburg 2023 — 純投影片加旁白（14.7 分；Grand Prize 加 Best Presentation）

全片除了片頭的 stock 畫面和片尾的照片，**沒有任何人出鏡**。這證明不露臉也能拿 Best Presentation。

| 時間 | 畫面 |
|---|---|
| 0:00–0:30 | stock 實拍：人群、培養皿上疊一個大數字 —— 用一個數據帶出問題 |
| 1:00 | **一句話目標**，放在一個橘色框裡：「Our goal is to synthesize a drug delivery system by using a CPP-Ferritin container…」 |
| 1:30–3:30 | 設計：每張投影片一個元件（Ferritin、CPPs、Loading the Cargo、Nanobodies），**同一個 ferritin 3D 渲染圖反覆出現**，每次加上新元件 |
| 5:00–5:30 | 選殖流程：圖示加箭頭的流程圖（PCR → Ligation → Transformation → Miniprep…） |
| 6:30–7:00 | **真實膠圖**（SDS-PAGE、Western、IEC、SEC），目標條帶用**紅框**框起來 |
| 8:30 | 「**What Did We Accomplish?**」三條勾選清單，對應 1:00 的目標 |
| 9:00 | 「Nomination: Best Composite Part」：質體圖，標出 part 的位置 |
| 9:30–10:00 | Next Steps、Outlook |
| 10:30–11:00 | iHP：**流程圖**，「問題 → 問了哪位專家 → 得到什麼決定」 |
| 11:30 | 「Thank you!」：每位專家都有照片、姓名、所屬機構 logo |
| 12:00–13:30 | Education & Communication：時間軸加活動照片 |
| 14:00 | 字卡：團隊合照、advisors、PI、贊助商、GoFundMe 名單 |

視覺規則：
- 白底。標題列用顏色分章節：綠色 = 設計，藍綠 = 實驗，深藍 = 成果和 HP。
- 每張投影片都有 iGEM logo 和頁碼。
- 畫面文字很少，只有標題加圖。

時間分配：設計約 30%、實驗約 20%、成果和展望約 10%、HP 和教育約 25%。

### B. TUDelft 2020 — 主播式（19.2 分；當年上限 20 分鐘；handbook 範例）

| 時間 | 畫面 |
|---|---|
| 0:00–1:00 | stock 實拍（蝗災、噴藥卡車），**每個鏡頭左下角都有出處**：「[© FAO] [2016] [Biopesticides for Locust Control] [Youtube:FAOVideo]」 |
| 1:30 | 講者站在中間，兩側彈出圖示（Chemical Pesticides vs Biopesticide） |
| 2:00 | 全隊走出大樓的畫面 |
| 3:30–4:00 | 全螢幕動畫講機制（彩色底） |
| 4:30 | 講者在右，左邊彈出文字圖卡「Benefits: …」 |
| 5:00 | **專家視訊子母畫面**，標註姓名和機構（「Omar Lavy, Researcher at Tel Aviv University」） |
| 8:00–13:00 | 換一位講者，**換上實驗衣、在實驗室裡**講濕實驗；機制圖全螢幕、**膠圖放在講者旁邊的圖卡裡** |
| 14:00 | 「Future of PHOCUS — Engagement」圖卡，第三位講者 |

特點：
- **每章換一位講者**，場景配合內容（實驗章節就在實驗室）。
- 圖卡統一用綠框加漸層底。
- 隊服統一。

### C. TU-Eindhoven 2025 — 混合（15.1 分；Best Presentation undergrad）

| 時間 | 畫面 |
|---|---|
| 0:00 | 講者在校園走廊，**下方字條寫姓名和職責**：「Tristan de Haas — Team captain and Hardware」 |
| 0:30 | 講者旁邊彈出簡單示意圖（膽酸循環） |
| 1:30–2:30 | 第二、第三位講者，各在不同戶外地點 |
| 3:00 | 專案名稱「BRIGHT」標題卡，開始進入投影片段 |
| 3:30–5:30 | 深藍底動畫：感測器原理（bioluminescence、BRET），蛋白質卡通圖 |
| 6:00–11:30 | **版本迭代**：BRIGHT-V1 → V2 → V2.1 → V2.3 / V2.4 → V3。每個版本 = 卡通圖（改了哪裡）+ 真實數據（發射光譜、劑量反應曲線、96 孔盤照片） |
| 10:30 | Kd 和 fold change 表格，**附 ± 誤差**，綠色箭頭標示改善方向 |
| 11:00 | Camera vs Phone 檢測對比 |
| 11:30–12:00 | 「BRIGHT-V3 summary」章節卡 |
| 12:30–13:00 | 回到真人：坐在沙發上，旁邊放著硬體實物 |
| 13:30–14:30 | HP 講者、收尾講者 |

特點：
- 真人只出現在**開場約 3 分鐘和收尾約 2.5 分鐘**，中間約 9 分鐘全是投影片和數據。
- **DBTL 直接用版本號呈現**，judge 一看就知道是迭代設計，不是 troubleshooting。
- 隊服統一，所有講者都別小型領夾麥克風。

### D. EPFL 2025、Brno 2025 — 紀錄片（參考用，不建議採用）

- **EPFL**（14.9 分）：
  - 0:00 野火實拍；0:30 黑底大字標語。
  - 1:00、2:30、6:00、9:30 等時間點，講者在不同地點出鏡（鐵道旁、實驗室）。
  - 數據段：黑底加質體圖、螢光顯微、flow cytometry；4:30 的 flow 圖**下方直接列 4 條結論**，5:30 的 Western 下方附完整圖說。
  - 7:30–8:00 講者用**視訊子母畫面**疊在圖上。
  - 9:00 軟體螢幕錄影；10:30 長條圖附顯著性標記。
  - 13:00 SDG 圖示。
- **Brno**（13.7 分）：電影感實拍，有農場、溫室、空拍和利害關係人訪談。引用前人工作時，用**人像照加姓名和頭銜**（「Barbara McClintock — Medicine Nobel Prize Laureate」）。⚠️ 片中有燒進畫面的字幕。**2026 規則禁止燒字幕，不要模仿。**

### 形式結論

- **A（Hamburg）證明不露臉也能贏**，而且最省時。
- **C（TU/e）是最可行的升級**：只要多拍 2–3 分鐘真人，並在每段講者出鏡時加姓名和職責字條，這也順便回答了 Project Q10「initiated and led by the students」。
- 建議：**Hamburg 式的投影片主體 + TU/e 式的真人開場和收尾**。中段可以學 TUDelft，偶爾在講者旁邊放數據圖卡，但不是必要。

---

## 3B. 條件總表（含案例）

這張表取代 §3.3 和 §3.5(a) 的分散清單，是**唯一的檢核依據**。每條都列出依據、得獎片怎麼做，以及我們打算怎麼做。

### A. 硬性條件（違反就無法上傳，或者違規公開）

| # | 條件 | 依據 | 案例 | 我們 |
|---|---|---|---|---|
| A1 | ≤ 15:00（不含 iGEM Intro） | `duration:900` | EPFL 14.9、TU/e 15.1（含 Intro）：都貼著上限 | 目標 13–14.5 分 |
| A2 | .mp4、1080p–4K 橫向、≤ 1 GB | `minHeight:1080`、`size:1e3` | — | 輸出 1080p30，再 `ffmpeg -c copy` remux |
| A3 | 英文旁白 | `Narration is required to be in English.` | — | 自己配音 |
| A4 | 字幕用 .vtt 另外上傳，不燒進畫面 | `Do not embed subtitles directly into your video file.` | ⚠️ 反例：Brno 有燒字幕 | 下載自動字幕，修正後重傳 |
| A5 | 素材有授權，片尾字卡 ≥ 2 秒 | `Copyright Material is NOT allowed`；`at least 2 seconds` | TUDelft 0:00–1:00 **每個 stock 鏡頭角落都標出處**；Hamburg 14:00 字卡 | Artlist 曲名、作者、授權寫在字卡；外部圖在畫面角落標出處 |
| A6 | 出鏡者同意；不出現國旗；不扮演病人；不用強烈閃爍 | FAQ | — | 拍攝前確認背景沒有國旗 |
| A7 | 不得把虛構影像當成實驗結果 | FAQ | EPFL 4:30、5:30 的數據圖都附圖說，和示意動畫區隔 | promo 動畫畫面標「schematic」 |
| A8 | 標題和描述填好，**10/28 15:00 UTC 前**到 Submitted | `Reaching "Submitted"… is what counts` | — | 10/27 上傳 |

### B. Presentation 區塊（5 題，同時是 Best Presentation 的評分題）

| # | 條件 | 案例 | 我們 |
|---|---|---|---|
| B1 | 目標、設計、結果講清楚，並有有力的證據（Q1） | Hamburg 1:00 用**一句話目標框**開場，8:30「What Did We Accomplish?」用三條清單**回扣**這個目標 | 約 1:00 放中心假說的一句話框；結尾放「What we showed / what remains open」回扣 |
| B2 | 呈現技術數據，**modeled 結果也算**（Q2） | Hamburg 6:30 膠圖**用紅框框出目標條帶**；TU/e 10:30 Kd 附 ±；EPFL 5:30 Western 附完整圖說 | 膠圖加紅框（Ni-NTA 的 elution 是空白也照實框出）；CR3 F126L 的 read pileup；O-antigen 基因組比較圖；結構預測 |
| B3 | 視覺設計幫助理解技術內容（Q3） | Hamburg 用**同一個 ferritin 渲染圖**反覆出現當導覽，標題列用顏色分章；TU/e 同一個卡通圖隨版本改動 | 用 Φ8 尾部 / depolymerase 的同一個渲染圖當導覽；沿用 promo 的莫蘭迪配色；章節用顏色區分 |
| B4 | Engaging（Q4） | TU/e 前 3 分鐘有 3 位隊員出鏡；TUDelft 每章換講者、實驗章節在實驗室拍；**Hamburg 不露臉，靠設計乾淨也贏** | 真人開場和收尾；多人配音；不念稿 |
| B5 | 圖片、前人工作、背景、數據都有適當標註（Q5） | TUDelft stock 鏡頭標出處、專家子母畫面標姓名機構；Brno 引用前人時放人像加頭銜；Hamburg 11:30 專家照片加機構 | **PI 的工作有專屬標記**（例如右上角「Analysis: Prof. Espinoza」）；文獻在投影片底部標作者和年份；Twist 等支援寫在字卡 |

### C. Project 區塊（judge 用影片加 wiki 評分，除了現場答問那題；handbook p.32）

| # | Project 題 | 案例 | 我們 |
|---|---|---|---|
| C1 | 工程原則 / DBTL（Q1） | TU/e 6:00–11:30 用 **V1 → V2 → V2.1 → V2.3/V2.4 → V3 版本號**，每版 = 改了什麼 + 數據 + 為什麼進下一版；Hamburg 5:00 選殖流程圖 | 「Cycle 1：RBP×OMP binding screen → 對照組兩次失敗 → 學到受體是醣不是蛋白 → Cycle 2：轉向 depolymerase」；表達實驗 0915 → 0929 → 1010 也用 cycle 編號呈現 |
| C2 | 以合成生物學和標準元件為基礎（Q2） | Hamburg 9:00 用「Nomination: Best Composite Part」質體圖標出 part | 我們的 Registry part（G1）加質體圖加編號 |
| C3 | 專案成功了嗎，或可能成功嗎（Q3） | Hamburg 9:30 Next Steps 三條；TU/e 11:00 用手機就能讀結果 | 成功的部分、還沒成功的部分、為什麼仍然可能成功，三者分開講 |
| C4 | 數據支持 claim（Q5） | EPFL 10:00 先講樣品組（**ablation 對照**），10:30 才放長條圖加顯著性；TU/e 誤差值 | 每張數據圖都放對照組（親代株、WT）；claim 不超過 §4 |
| C5 | 可能產生影響（Q6） | Hamburg 10:00 Outlook：「Higher efficacy → less dosing → saving resources」；EPFL 13:00 SDG 對應具體效益 | 宿主範圍上限 → 對有莢膜病原菌設計噬菌體雞尾酒療法的意義；資料庫和工具的貢獻 |
| C6 | HP 影響了設計（Q7） | Hamburg 10:30 iHP 流程圖（問題 → 專家 → 決定）；EPFL 11:00「FireRain 說 get the physics right → 所以我們做了黏度測試」 | 從 wiki HP 頁挑 2–3 個「誰說了什麼 → 我們改了什麼」 |
| C7 | 負責任、對世界有益（Q8） | TUDelft 1:30 開場就比較化學農藥和生物農藥的安全性 | IBC 核准；0 VFDB / 0 CARD；resistant mutant 的意義 |
| C8 | Wiki 和 Registry 有完整記錄（Q9） | Hamburg 9:00 直接點名 Registry 提名 | 每章底部放 wiki 頁網址字條 |
| C9 | 學生發起和主導（Q10） | TU/e 每位講者出鏡時都有**姓名加職責字條** | 每位講者都加姓名和職責字條；PI 的部分另外標示（B5） |

### D. Handbook 的質性要求

| # | 條件 | 依據 | 案例 | 我們 |
|---|---|---|---|---|
| D1 | 講一個故事 | p.85「Above all, each team should tell a story」 | TUDelft 0:00 蝗災實拍 → 現有方案的問題 → 他們的解法；Hamburg 用「Trojan horse」比喻 | 校園採樣 → 新噬菌體 → 為什麼宿主範圍這麼窄 → depolymerase 假說 |
| D2 | big picture 和設計細節要平衡 | p.85 | Hamburg 1:30 先放 ferritin 全貌，5:00 才放選殖細節 | 每章先放一張全貌，再進細節 |
| D3 | 不浮誇，不用分散注意力的特效 | p.86（TUDelft 的評語） | TUDelft 的圖卡樸素統一；EPFL 和 Brno 的電影感因為服務內容所以沒被扣分，但這不是必要條件 | 動畫只用在解釋機制 |
| D4 | 失敗講成 DBTL，不講成 troubleshooting | p.16、p.34、p.73 正面；p.14 反面 | EPFL 字幕約 3:00：「we redesigned silica and CBD fusions… This change seemed to improve bacterial phenotype… but unfortunately didn't result in higher levels of…」= 假說 → 改設計 → 結果 → 結論 | Ni-NTA 和 spot test 都用同一個句型講 |
| D5 | 不念稿 | p.14 | — | 稿子寫成口語；錄音前先練過 |
| D6 | 畫面文字補充旁白，不重複旁白 | p.86（Hamburg 的評語） | Hamburg：短標題加圖；EPFL 4:30 flow 圖下方列結論，旁白負責解釋過程 | 投影片只放關鍵詞和圖 |
| D7 | 致謝靈感、背景、前人工作、外部支援 | p.85 | 見 B5 | 見 B5 |

### E. 我們自己的限制

| # | 條件 | 依據 |
|---|---|---|
| E1 | 說法不超出已凍結的 wiki | §4 |
| E2 | 數字和 `2026-10-20_engineering_number_consistency.md` 一致 | §4 |
| E3 | PI 的工作要標名，而且和 Attribution Form 一致（judge 可能對照看，p.11） | §4 |
| E4 | Artlist 音樂無法補登 Attributions Form | §1 的 D5 |

---

## 4. 不可超出 wiki 的說法

wiki 已在 10/21 凍結，judge 會兩邊都看，所以片中說法要和 wiki 一致。以下這些不能講過頭：

- **基因體拓撲尚未定論**：不要說「circular」。我們的分析是 linear 加 77 bp DTR，和 PI 的說法衝突（`2026-10-18_genome_topology_conflict.md`）。
- **CDS_0010 = unknown protein**，不是 glycosidase。
- **分類是暫定的**（Bcep22-like / *Gervaisevirus*，根據 Foldseek 結構比對）。「T7-like」只代表基因排列方式相似。
- **Ni-NTA 純化失敗**（1010），**spot test 結果 inconclusive**（1016）。可以講，而且應該誠實講，但不能講成成功。
- 不要把 ancestral nodes 稱為「deep / mid / shallow」。
- 不要把 O-antigen 的預測（Φ8 不會在 Strain 1/3 上形成 plaque）講成已驗證的結果。
- 所有數字都要以 `2026-10-20_engineering_number_consistency.md` 為準。
- RBP×OMP binding screen 只能當作**被淘汰的負結果**來講，不能講成工具。

**學生 vs PI 的貢獻**（Attributions Form §1 原文）：
- ASR、系統發生樹、ZymCTRL perplexity 評分、噬菌體基因體組裝，以及用 Foldseek 推論形態，都是 **PI 做的**。這些內容出現的畫面要寫「Analysis: Prof. J. Cesar Ignacio Espinoza」。
- 學生做的：採樣與分離、細菌基因體與 MRA、O-antigen 比較、RBP 資料庫、resistant-mutant WGS、蛋白質表達與膠圖、wiki、軟體。

---

## 5. 大綱草稿（目標約 11 分鐘，**待 §3.6 第 1 題定案後重排**）

時間是預算，D4 定案後再調。每段標出主要回答哪幾題。

| 段 | 時間 | 內容 | 可用素材 | 回答 |
|---|---|---|---|---|
| 1. Hook | 0:00–0:45 | 有莢膜的細菌，以及為什麼噬菌體的宿主範圍這麼窄 | promo 開場動畫 | Q4 |
| 2. 中心假說 | 0:45–2:00 | 決定宿主範圍上限的是 depolymerase 的受質範圍，而不是 RBP 的身分；現存的窄專一性是由較廣的祖先活性演化來的 | PI grant 原文、wiki Description | Q1 |
| 3. 發現 | 2:00–4:00 | 從校園採樣、分離出三株菌和 Φ8；細菌基因體（MRA 已發表）；同一個 `ihfB` 位置上有三套互不同源的 O-antigen 基因組 | promo plaque assay 動畫、`0729_prof_figures` 細菌基因體圖、`0727` O-antigen 比較圖 | Q1 Q2 |
| 4. 設計 | 4:00–5:45 | Φ8 基因體和尾部模組；CDS_0011 tail fibre、CDS_0012 GH5 depolymerase；三個祖先變體（**PI 的 ASR**）；6 個 pET-28a parts | 噬菌體基因體圖、AF3/ESMFold 結構、`1018_construct_structures` | Q1 Q3 Q5 |
| 5. Engineering | 5:45–7:00 | 設計–建構–測試循環；淘汰的 binding screen（對照組兩次失敗）如何讓我們轉向 depolymerase | wiki Engineering | Q1 |
| 6. Results | 7:00–9:15 | 表達膠圖、Ni-NTA 失敗、spot test、resistant mutant（9-6-2 r1 = Stealth CR3 F126L，有 reads 確認） | 膠圖 notebook、`2026-10-21_spot_test_figures` | Q2 |
| 7. HP 與 Safety | 9:15–10:15 | Human Practices 如何影響設計；IBC 條件式核准；0 VFDB / 0 CARD | wiki HP / Safety | Q1 |
| 8. 貢獻與下一步 | 10:15–10:50 | 軟體、RBP 資料庫、負結果 benchmark；下一個實驗 | wiki Software / Contribution | Q1 |
| 9. 字卡 | 10:50–11:05 | 隊員、PI、協助者、素材出處、授權（≥ 2 秒） | promo `Credits.tsx` | Q5 |

語速以 130–135 wpm 估算：11 分鐘大約 1,400 字稿。

---

## 6. 現有素材

- `documents/2026-07-29_results_synthesis_EN.qmd`：圖和「每張圖怎麼做的」說明
- `code/0729_prof_figures/`：細菌基因體圖、噬菌體基因體圖（tail spike 標色）、酵素結構域 3D
- `code/0727_o_antigen_comparison/`：三株菌的 O-antigen 基因組比較
- `code/1018_construct_structures/`：6 個 construct 的結構和比較表
- `documents/2026-10-21_spot_test_figures/`：spot test 圖和圖說（剛為 PI 的經費申請整理好）
- `code/0811_promo_video/`：Remotion 專案，含配色、片尾字卡元件、plaque assay、吸附 3D、系統發生樹動畫
- wiki 18 頁：可以直接截圖做投影片底稿

---

## 7. 倒推時程草案

目標是 **10/27 就上傳完成**，留一天緩衝給轉檔、修字幕和重傳。

| 日期 | 工作 |
|---|---|
| 10/24（六） | 回答第 1 節；定分工 |
| 10/25（日） | 寫英文稿（約 1,400 字）並對照第 4 節檢查；做投影片 |
| 10/26（一） | 錄音、錄影；剪入 promo 片段 |
| 10/27（二） | 輸出 1080p mp4、remux、上傳、填標題和摘要，達到 **Submitted**；下載自動字幕修正後重傳 |
| 10/28（三） | 緩衝。15:00 UTC（台北 23:00 / PDT 08:00）截止 |

---

## 8. 上傳前自查（因為沒有人工審核）

- [ ] 長度 ≤ 15:00，1920×1080 以上，橫向，.mp4，≤ 1 GB
- [ ] `ffprobe` 確認解析度和長度；做過 `-c copy` remux
- [ ] 全片沒有國旗（地圖、隊員背景、衣服都要看）
- [ ] 每張外部圖或素材都有授權，而且列在片尾字卡
- [ ] 沒有新的 AI 素材超出 Attributions Form 已申報的範圍
- [ ] 示意動畫都有標示，沒有被當成實驗數據
- [ ] 第 4 節逐條對過
- [ ] PI 的工作有在畫面上標示
- [ ] 片尾字卡 ≥ 2 秒
- [ ] 英文旁白；字幕 .vtt 另外上傳並通過 Validator
- [ ] 標題長度在預算內，摘要已填
- [ ] 狀態顯示 **Submitted**

---

## Log

- 2026-10-24 — 初稿：從 iGEM 前端 bundle 和 API 抓取 2026 Presentation Video 規則與 Best Presentation ballot 題目；列出待決定事項、不可超出 wiki 的說法、大綱草稿和時程
- 2026-10-24 — D3 定案（自己配音）、D5 定案（Artlist，附 Attributions Form 凍結的待解問題）；§3 擴寫：主 ballot 權重結構、1–6 量表、五題逐題拆解、2025 片長分布與得獎片時間分配；D4 因 2025 數據改為待重談
- 2026-10-24 — 加入 §3.5，讀 2026 Judging Handbook 的結果：影片也用來打 Project 區塊的 9 題（p.32），附對照表；Presentation 專章與 TUDelft / Hamburg 範例；handbook 對失敗與誠實的立場，以及「troubleshooting」陷阱；不要念稿；討論題改為 §3.6
- 2026-10-24 — 加入 §3A（下載 5 支得獎片，每 30 秒抽一張畫面，拆解四種形式和逐段時間點）與 §3B（條件總表 A–E，每條附得獎片案例和我們的做法，取代分散的清單）
- 2026-10-24 — D1 定案：Hamburg 式投影片主體加 TU/e 式真人開場和收尾；handbook PDF 移到 `documents/2026-10-24_judge_handbook_2026_v5.pdf`
