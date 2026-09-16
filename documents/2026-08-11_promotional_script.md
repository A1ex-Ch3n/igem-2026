# Project Promotion Video — 2026

## 0. 狀態

- **死線 = 2026-08-12 15:00 UTC = 台北 8/12 23:00 = Claremont 8/12 08:00 PDT。** 來源：`GET https://api.igem.org/v1/competitions/58a7e73a-1e25-457f-9f59-36c47b3f652a/deliverables`，`video-project-promotion` 的 `closeTime`，`phase: open`。（工作機在 UTC+8，兩邊時間都寫出來避免再讀錯。）
- **不計入評分**（2026-08-11 Alex 確認）。策略：先蓋能上傳的地板，再往上加。
- **`completeStatus: ["published", "submitted"]` —— submitted 就算完成。** 審核不必在 08:00 前跑完，只要上傳完成。
- **製作方式：全動畫，Remotion。** 隊伍為 non-profit，適用 Remotion 免費層（2026-08-11 Alex 確認）。專案在 `code/0811_promo_video/`。
- **旁白：ElevenLabs AI 語音。配樂：Suno。**（2026-08-12 Alex 定）兩者都是 AI 生成 —— iGEM 允許，但要求「工具條款允許發布」+ 片尾具名 + 登記 Attributions Form。**待確認：兩個帳號都要是付費方案。** ElevenLabs 免費層是非商用且要求署名；Suno 免費層產出的曲子不含商用授權。上傳到 iGEM Video Universe 算發布。
- **名單（2026-08-12 Alex 提供）**：Chun-Yu (Alex) Chen、Yan (Olivia) Yan、Xiaokuan (Carol) Wang、Yuhui (Sarah) Liu、Maggie Chou；PI：J. Cesar Ignacio Espinoza。已填入 `src/components/Credits.tsx`。

---

## 1. 2026 官方要求

來源：`teams.igem.org` 前端 bundle（`videoPaths-f8uu4GJ8.js`、`VideoDeliverable-nvhtwYVy.js`），2026-08-11 抓取。網站是 SPA，WebFetch / WebSearch / Chrome extension 當天全部不可用，故直接從 JS chunk 取原文。

### 技術規格

| 項目 | 規格 |
|---|---|
| 長度 | **≤ 2 分鐘**（不含 iGEM Intro；`duration: 120`） |
| 檔案大小 | **≤ 500MB** |
| 格式 | **.mp4** |
| 解析度 | **1080p 或 4K，橫向（landscape）** |
| 縮圖 | 另傳圖檔，≤ 4MB |
| 字幕 | **.vtt，必須另傳，不可燒進畫面** |

- iGEM Intro 由系統在審核通過後自動插入 —— **不要自己做片頭**。
- 上傳器檢查 MP4 內部 brand label。QuickTime / iPhone / iPad 匯出的檔常被擋。修法：HandBrake 用 `Fast 1080p30` preset 重匯，或 `ffmpeg -i input.mp4 -c copy fixed.mp4`（不重編碼、不掉品質）。
- **標題與描述都是必填**，且只能在上傳完成後才能存檔。**描述沒有長度上限**（6 行文字框）。**標題約 80 字元** —— iGEM 把它包成 `Phagenomics: <標題> (2026) - Project Promotion` 當作 PeerTube 影片名，整串上限 120，前後綴佔 40，超過會被截成 `...`（原始碼 `videoPaths` 的 `Ee()`）。
- 自動字幕會有錯：下載 → 修正 → 重傳。teams 站上有 VTT validator 分頁可貼上檢查。

### 內容規則

- **旁白必須英文。** 系統做語言比對（欄位 `falseEnglishSubmission`，錯誤訊息 "The automatically generated captions do not match the submission language"）。其他語言字幕可額外上傳。
- **版權素材禁止。** 只能用 CC0 / CC BY / 明確允許「改作 + 公開發布」的 stock 授權。含 `NoDerivatives` 條件的授權**不能**剪進影片。授權不清楚就換素材。
- **全部素材都要具名**，即使該授權免署名。片尾字卡列 title / creator / licence，**畫面停留 ≥ 2 秒**，並登記到 Attributions Form。
- **外部素材沒有固定比例上限**，原則是「idea 與 effort 主要來自本隊，借來的素材是支撐不是主體」。
- **AI 生成素材可以**，條件：自己下 prompt 生成、工具條款允許發布、片尾具名工具、登記 Attributions Form。
- **出鏡者需知情同意**；未滿 18 歲需監護人／法定代理人同意。
- **禁國旗** —— 原文 "Country flags are not permitted in any form"。
- 禁止項目：仇恨言論、騷擾或騷擾情節、**扮演病人或障礙者**、刻板印象／文化曲解、對競爭者或具名機構或真實人物的不實指涉。
- 避免快速閃爍、頻閃、強烈運動特效（光敏／前庭症狀觀眾）。
- **不得把虛構影像呈現成本隊真實實驗結果。**

---

## 2. 稿子（改版）

**244 字 / 18 句 / 旁白約 108 秒**（135 wpm），1:48 之後 7 秒給片尾字卡。

字數配速說明：

- **120 秒是 iGEM 機器強制上限**（`duration: 120`，上傳器直接擋）。
- 原稿頂端的 260–320 字是我方自訂目標，不是 iGEM 規則。244 字低於該目標是刻意的 —— 272 字版本以 130 wpm 念要 126 秒，會被退件。**寧可低於自訂字數，不可超過 120 秒。**
- 每段配速已個別驗算，全部落在 112–136 wpm。不要只看總長平均：個別段落超速只會在錄音當下才被發現。

**時間軸的唯一正本是 `code/0811_promo_video/src/timeline.ts`。** 下表是它的鏡像；改時間改那個檔，場景長度、字幕、影片總長全部從它推導。

| 段落 | 字 | 秒 | wpm |
|---|---|---|---|
| 0:00–0:07 Hook | 15 | 7 | 129 |
| 0:07–0:26 Stakes | 43 | 19 | 136 |
| 0:26–0:45 Gap | 43 | 19 | 136 |
| 0:45–0:58 Team | 29 | 13 | 134 |
| 0:58–1:13 Method | 34 | 15 | 136 |
| 1:13–1:30 Wet lab | 39 | 17 | 138 |
| 1:30–1:36 ML loop | 14 | 6 | 140 |
| 1:36–1:48 Close | 27 | 12 | 135 |
| 1:48–1:55 片尾字卡 | — | 7 | — |

總長 **115 秒**（硬上限 120，留 5 秒餘裕）。旁白 135 wpm。

### 連續稿（**唯一正本** —— 配音與 .vtt 都以此為準）

```
Phages are viruses that hunt bacteria. They have been doing it for billions of years.

That matters right now. Antibiotic resistance is rising, and infections we could once cure are becoming untreatable. Phages are one way to fight back, but only if a phage can infect the exact bacterium making someone sick. Most of the time, it cannot.

That decision is made in the first seconds of contact, by the tail spike proteins that grip the bacterial surface. We do not know which parts of them set the host range, and we cannot yet aim a phage at a new host.

We are Phagenomics, a team from Claremont, California. We collected our phages from the water and soil around us, along with the bacteria they infect, and sequenced them ourselves.

We treat host range as an evolutionary question. We take the receptor binding protein, the part that makes first contact, and reconstruct its ancestors, versions that existed long before the strains on our bench.

We build those ancestral proteins in the lab and measure how tightly each one binds its target. Evolution already ran this experiment. The ancestral sequences are its notes, recording which changes opened a host range and which closed it.

Those measurements train our model, and the model tells us what to change next.

So this is a time machine. We go backward to find out what evolution learned, and we run it forward to design the next generation of phages.
```

改稿只改上面這一份。下面分鏡表只寫限制，不重複台詞，避免兩份稿子走鐘。

### 畫面紅線

分鏡本身寫在 `code/0811_promo_video/src/scenes.tsx`（程式即分鏡），這裡只留不能違反的限制：

- **Wet lab 那拍是紅線所在。** 不要放結構渲染圖、docking pose、或結合親和力曲線 —— RBP×OMP ipTM 篩選已退役（對照組兩次失敗、兩套工具），docking 尚未執行。放上去就直接命中「虛構影像被誤認為真實實驗結果」。目前該拍放的是真實 CDS 座標 + 真實訂購構築（CDS_0011 res 305–941、N 端 His6），系統發生樹標明 schematic。
- **ML loop 不要假的 loss curve 或假的預測分數。**
- **Stakes 不可以讓隊員扮演病人**，也不要用「殺菌」畫面 —— 那句旁白講的是「大多數時候做不到」，畫面殺菌會把語意反過來。
- **禁國旗**，包含地圖上的旗標。
- 任何示意圖都要看得出是示意。全片線稿無填色，天生讀成 diagram。
- **片尾字卡 ≥ 2 秒**：隊員 + 所有外部素材（title / creator / licence）+ 所有 AI 工具名稱。同一份清單同步進 Attributions Form。

---

## 3. 相對原稿改了什麼

| 原稿 | 問題 | 處理 |
|---|---|---|
| （無） | 缺利害關係，全篇只講知識空缺 | 新增 [0:08–0:27] 抗藥性段落 |
| `evolute over billions of years` | 非英文字 | `have been doing it for billions of years` |
| `advance bioinformatic algorithms` | 形容詞形式 | 該句整體改寫 |
| `phage organ of tail spike` | 非術語 | `tail spike proteins` / `receptor binding protein` |
| `infect a bacteria` | 單複數 | `infect the exact bacterium` |
| `Phage kills bacteria and live on...` | 主謂不一致 | `Phages are viruses that hunt bacteria` |
| `We build ancestral tree` | 缺冠詞、非正式術語 | `reconstruct its ancestors`（ancestral sequence reconstruction） |
| `input this results` | 單複數 | `Those measurements train our model` |
| Inspired by University of Toronto 2025 | 120 秒裡佔約 10 字 | 移出旁白，保留在 Attributions Form 與片尾字卡 |
| `with the power of artificial intelligence` | 空泛 | 換成具體：ancestral reconstruction + 結合測定 → 模型 |

---

## 4. 剩餘工作

**剩餘時間：約 24 小時**（2026-08-11 23:00 台北 → 08-12 23:00 台北）。

已完成：

- [x] Remotion 專案 `code/0811_promo_video/`，8 拍場景 + 片尾字卡骨架
- [x] 全片渲染驗證通過：**115.05 s / 1920×1080 / h264 / ~12 MB / `ftypisom`** —— 長度、解析度、格式、大小、容器 brand 五項全過
- [x] **噬菌體改畫成 podovirus**：原本畫長尾 + 三根纖維，那是 myovirus（T4）的形狀。我們自己的 synteny 分析（`code/0730_synteny_group_d/`）確認 9-2-1 Φ8 是 podovirus —— 短的、不可收縮的尾巴。衣殼改成真的二十面體（12 頂點 / 30 邊，逐幀旋轉正投影，背面的邊調暗）
- [x] **吸附畫成真實機制**：tail spike (CDS_0011) 是 β-helix depolymerase、受體是 LPS O-antigen 醣，所以是 spike 張開、切斷醣鏈、顆粒沉到膜面 —— 不是「降落」
- [x] **配色兩版**（`src/theme.ts` 的 `PALETTE` 切換）：`morandi`（照隊徽：鼠尾草底、珊瑚色重點、淡藍衣殼）與 `blueprint`（深底技術版）
- [x] **視覺風格定為線稿**（2026-08-11 Alex 選）：可見網格、1.5px 純描邊、無填色，每個形狀自己描出來。圖示素材若要用，走開放授權集（Servier Medical Art CC BY 4.0 / BioIcons 逐圖授權 / SciDraw）—— 目前全片程式繪製，**沒有任何第三方素材**
- [x] 基因體圖改為**資料驅動**：`scripts/export_cds.py` 把真實 80 CDS Pharokka 註解匯出成 `src/data/cds.json`，由 `GenomeTrack.tsx` 直接畫 SVG。可縮放、可換視窗、可逐個描出來，而且仍是我們自己的資料。原本「matplotlib 出圖再貼進影片」的做法已廢棄（19 吋 300 dpi 的標籤縮進 1080p 會糊，副標還帶內部語言「the PI is cloning」）
- [x] BioRender **暫不使用**：需先確認方案是否含 publication licence、是否涵蓋影片、能否匯出 SVG
- [x] `.vtt` 產生器 `scripts/make_vtt.mjs`，未加 `--retimed` 會拒絕執行（避免有人在最後關頭上傳規劃時間碼版本）

未做：

- [x] 影片標題 + 描述 —— 定稿見 §5
- [ ] UNDONE：`.vtt` —— **以實際錄音的時間軸打，不要用上面的規劃時間碼**（規劃時間是配速驗算用，實錄一定會偏）。流程：先平順錄一次 → 量測真實段落時間 → 依連續稿正本寫 .vtt → 貼進 teams 站 validator 檢查
- [ ] UNDONE：縮圖（≤ 4MB）
- [ ] UNDONE：確認 ElevenLabs / Suno 帳號是付費方案（免費層不含發布授權）
- [x] 片尾字卡名單已填（隊員 + PI + ElevenLabs/Suno 揭露 + 工具 + 資料來源）；同一份仍要抄進 Attributions Form
- [x] 出鏡者知情同意：**不適用** —— 全動畫、無真人出鏡。若之後補拍實驗室畫面，這條會回來
- [ ] UNDONE：匯出檢查 —— .mp4 / ≤500MB / 1080p 或 4K / 橫向；若上傳被拒，跑 `ffmpeg -i input.mp4 -c copy fixed.mp4`

---

## 5. 上傳欄位（標題／描述）

兩個都是必填，且只能在影片上傳完成後才能存檔。

**標題上限約 80 字元。** iGEM 把它包成 PeerTube 影片名 `Phagenomics: <標題> (2026) - Project Promotion`，整串上限 120，前後綴佔 40。超過會被截成 `...`。**描述沒有長度上限。**

### 標題（正選）

```
Rebuilding the ancestors of a phage tail spike
```

46 字元，包起來 86/120。備選：

- `A time machine for host range: reconstructing an ancestral tail spike`（69 字元 / 109）
- `Ancestral reconstruction of a phage receptor-binding protein`（60 字元 / 100）

### 描述

```
A phage can only kill the bacteria it can recognise, and that recognition is
settled in the first seconds of contact by the tail spike. We do not yet know
which parts of that protein set host range, or how to aim a phage at a new host.

We isolated and sequenced our own phage — 9-2-1 Φ8, a novel ~62 kb podovirus
collected from water and soil around Claremont, California — and we treat host
range as an evolutionary question. We reconstruct the ancestors of its
receptor-binding protein, build them in the lab, measure how tightly each one
binds, and feed those measurements back into a model that tells us what to
change next.

Every genome figure in this video is drawn from our own assembly and
annotation. The narration and music are AI-generated by the team and credited
on the end card.

Phagenomics — iGEM 2026, Claremont, California.
```

最後一段的 AI 揭露是額外加的 —— iGEM 只要求片尾字卡與 Attributions Form。不想寫在公開描述裡就刪那一句，不影響合規。

---

## Log

- 2026-08-11 初稿（bullet 形式，199 字）
- 2026-08-11 加入 2026 官方要求（從 teams.igem.org JS bundle 取原文）、死線、改寫稿、分鏡限制、未完成清單
- 2026-08-11 逐段配速驗算後修訂：272 → 244 字。原版收尾段 38 字塞在 8 秒 = 285 wpm，不可能念完；且 272 字以 130 wpm 是 126 秒，超過 120 秒硬上限。刪掉重複的收尾句、精簡 Stakes/Gap/Wet lab，重排時間碼
- 2026-08-11 建 Remotion 專案並跑通全片渲染；時間軸改為 135 wpm / 總長 115 秒，正本移至 `code/0811_promo_video/src/timeline.ts`
- 2026-08-11 檢查渲染出來的畫面（不只檢查容器）：Method 拍的基因體圖標籤糊掉、且兩張圖帶內部語言副標，改用螢幕版重出
- 2026-08-11 Blueprint 線稿改版：基因體圖改資料驅動（cds.json + GenomeTrack.tsx）；Stakes 拍原本劃掉 7 個細菌，語意讀成「噬菌體殺菌」，與旁白「大多數時候做不到」相反，改為標出單一目標菌；Team 拍「from the water and soil around us」無法佐證採樣點在 Claremont 附近，改為「from water and soil we sampled」
- 2026-08-11 噬菌體形態修正（podovirus 非 myovirus）、二十面體衣殼、O-antigen 吸附序列；加入莫蘭迪配色（照隊徽）與深色 blueprint 兩版可切換。Manim 評估後不採用 —— 矢量化的收益來自 cds.json + SVG，不是來自 Manim；24 小時內整套重寫風險大於收益
- 2026-08-12 採樣點確認在校園附近，Team 那句改回 `from the water and soil around us`
- 2026-08-12 修 1:17 的 bug：系統發生樹末端用原生 `<circle>`，不吃場景時鐘，整段一開始就在畫面上。改用會依 delay 淡入的 `Dot`
- 2026-08-12 吸附場景改成透視 3D 地面（`Membrane3D.tsx`）—— 旋轉的二十面體站在 2D 直線上會違和，現在整個場景在同一個空間裡：膜面收斂到地平線、醣鏈隨深度縮小、顆粒依自己的 z 縮放
- 2026-08-12 加演示動畫（非文字動畫）：Stakes 掃描線找出目標菌；Team 改成完整的 plaque assay（菌苔鋪滿 → 噬菌體落下 → 溶菌圈長出來）；系統發生樹改成由末端往回合併到祖先（真實的重建方向）；ML loop 加一顆繞行的量測 token
- 2026-08-12 尾部也改成 3D：管、噴嘴錐、六根 spike 全部在與衣殼相同的旋轉空間裡（共用 `TILT`），背面的線調暗；線寬隨 scale 縮放，避免大尺寸時變髮絲。配樂 brief 另開 [`2026-08-12_promo_video_audio_brief.md`](2026-08-12_promo_video_audio_brief.md)
- 2026-08-12 噬菌體改成單一網格（`components/mesh.ts`）：衣殼 20 面、尾管、噴嘴錐、六根 spike 全部是同一份多邊形清單，走同一條管線。先試了 lambert 明暗版，Alex 要線稿，改成**隱線消除的線稿**：面用背景色填滿只負責遮擋，只描輪廓邊（剪影邊，以及衣殼的切面稜線）。所以 spike 是有錐度的實體管、有量體，但不會變成一堆接縫。管段共用頂點且兩端封口，否則接縫會被當成開放邊界畫出來。取消自轉，改固定四分之三視角 —— 轉動的線框讀起來像玩具
- 2026-08-12 填入真實名單與 AI 工具揭露；更正欄位限制 —— 描述無長度上限，受限的是標題（約 80 字元，因為 iGEM 把它包進 120 字元的 PeerTube 影片名）
- 2026-08-12 名單加入 Maggie Chou；標題與描述定稿存入 §5
