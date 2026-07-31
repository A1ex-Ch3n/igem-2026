# Graphical abstract —— 設計規格（第 2 題）中文版

對應 `2026-07-30_graphical_abstract_design.md` 的中文版本，內容同步（同結構、同決策）。
這是教授 2026-07-27 信件第 2 題 *"a graphical abstract that summarizes the overall
project"* 的設計。2026-07-30 與 Alex 腦力激盪後鎖定。

這份文件同時是**「設計」+「開工前要確認哪些資訊」的清單** —— 圖還沒做，有三項輸入在等（見 §6）。

> 先攤開歧義：專案結果偏**表徵型**，但 graphical abstract 需要一個**工程主軸**。這個主軸
> （見下）是**前瞻性**的 —— 中央流程多半是**提議／進行中**，不是已示範。誠實度機制（§4）
> 就是為了不讓圖被讀成「已完成」。

## 1. 主軸（一句話）

**可程式化、糖專一的噬菌體：讀 O-antigen，重新導向這隻 phage 能殺哪些菌。** 這是**工程平台**
故事，不是「我們描述了一隻噬菌體」。走**結構／機制知情**路線，刻意對照 Phagos 的純基因體
宿主範圍預測（見 `2026-07-30_phagos_company_research.md`）。

## 2. 受眾／版位

**一張母版、寬幅、可 reflow → 導出三種裁切：** iGEM wiki hero（寬）、論文 graphical abstract
（約 1:1 或直式）、簡報（16:9）。邏輯設計一次；母版必須能優雅退化（寬＝一列、方＝兩列）。
必須在手機寬度與灰階下都讀得懂。

## 3. 版面 —— 方案 A，水平 DBTL pipeline（左 → 右）

```
Zone 0  ── 標題帶：一句話主軸 ──────────────────────────────────────────
┌── Zone 1：地基（✅ 實線）──────┐  ┌─ Zone 2：工程迴圈（提議）──┐  ┌ Zone 3：產出 ┐
│ 新穎 ~62 kb Pseudomonas         │  │  Learn  →  Test   →  Build  │  │ 平台：       │
│ podovirus 9-2-1 Φ8              │  │  GH5      in trans   模組    │  │ 序列 → 預測  │
│ tail spike CDS_0011 =           │  │  祖先樹   混搭挑戰   depol   │  │ 讀哪種糖     │
│ β-helix DEPOLYMERASE            │  │  (→規律)  (量affinity) 交換  │  │ → 重新導向   │
│ 受體 = 菌株專一 O-ANTIGEN       │  │                      (宿主   │  │              │
│ 糖（不是蛋白）                  │  │                      範圍     │  │ 可程式化     │
│ 三株 × 三套非同源 O-antigen     │  │                      on       │  │ 精準         │
│ 卡匣（同一 ihfB slot）→ 為何    │  │                      demand)  │  │ antibacterial│
│ 一隻 phage 殺不完、為何可當把手 │  │                              │  │ 平台         │
│ (輔) 第二個 depolymerase        │  │                              │  │              │
│ CDS_0024                        │  │                              │  │              │
└─────────────────────────────────┘  └──────────────────────────────┘  └──────────────┘
```

- **閱讀方向：** 左→右敘事。寬版＝這一列；方版＝Zone 1 在上、Zone 2–3 在下。
- **Zone 1** 是已確認的地基；**Zone 2** 是 DBTL 工程迴圈（Learn→Test→Build）；**Zone 3** 是
  交付物 —— **平台/方法本身**（設計規律 + 預測），模組交換是它的終極應用。

## 4. 誠實度機制（不可妥協）

一個 legend，全圖一致：

- **實線外框／飽和色 = 已完成、有資料。**
- **虛線外框／淡化 = 進行中或提議。**

| 元素 | 狀態 | 畫法 |
|---|---|---|
| podovirus 基因體、β-helix depolymerase、O-antigen 受體、三卡匣、CDS_0024 | ✅ 有資料 | **實線** |
| 重組蛋白 CDS_0011 / CDS_0012 | 已下單、未表現 | 半虛線 |
| host-range assay | 已做 2026-07-04、**資料未到手** | 半虛線 |
| GH5 祖先樹（Learn） | 教授建構中 | 半虛線 |
| in-trans 測試（Test）、模組交換（Build）、預測平台（Output） | 提議／概念 | **虛線** |

應用 framing（Zone 3）：**不鎖定應用**的「可程式化精準 antibacterial 平台」，*在環境型
Pseudomonas 上示範*。**不得暗示臨床用途** —— 菌株是 *Pseudomonas_E* sp013179515 與
*P. capeferrum*，不是臨床的 *P. aeruginosa*。

## 5. 風格

- 盡量沿用 synthesis 圖既有的顏色語言：tail spike / depolymerase 用 CDS_0011 已用的紅色系；
  O-antigen 卡匣用細菌圖上的紅色。小而克制的調色盤（≤5 色），灰階下仍可辨。
- baby blue 當次要 accent（Alex 選的 3D 列印顏色 —— 一條把 abstract 連到實體 tail-spike 列印
  的淡線索）。
- 用 icon 不用照片；「O-antigen」全圖共用同一個糖鏈 glyph。
- **用可編輯向量（SVG）製作。** 這是設計型示意圖，不是資料驅動的 plot，所以**不是** matplotlib
  圖 —— 手寫或腳本生成、且能持續編輯以做 reflow 裁切的 SVG。工具在製作時決定（Inkscape /
  drawsvg / 手寫 SVG）。詳細工具評估見本文件末的補充。

## 6. 開工前要確認的資訊（你要的清單）

**已鎖定（2026-07-30 與 Alex）：** 主軸 · 版面 A · Learn→Test→Build 流程 · 交付物＝平台/方法 ·
版位＝母版→導出 · 應用＝不鎖定的平台。

**仍待確認 —— 多半在教授手上：**

1. **host-range 讀出** —— 等教授 2026-07-04 的 notebook。決定「一隻 phage 殺不完」那格能放真
   資料還是維持預測。
2. **GH5 祖先樹產出** —— 教授建構中；需要它才能具體畫出 *Learn* 格。
3. **in-trans 實驗設計** —— 需要它才能具體畫出 *Test* 格。
4. （次要）跟教授確認一句話主軸的確切措辭。

在 1–3 到手前，中央迴圈維持 schematic／虛線。圖現在可先用 placeholder 打草稿，各輸入到齊後
逐格定稿。

## 7. 工具 —— 怎麼做出來（用「Claude 能迭代」篩選）

篩選條件（Alex 定）：工具必須讓 Claude 能**執行*且*迭代**，不是丟回一張一次性圖。

| 工具 | Claude 能驅動？ | 媒材適配 | 判定 |
|---|---|---|---|
| **Claude 手寫/腳本 SVG**（drawsvg 寫、cairosvg 轉點陣讓 Claude *看到*並自我修正） | ✅ 完整迴圈 —— 寫 → 渲染 → 看 → 改 | 向量、可 reflow、wiki + 論文皆可用 | **主力** |
| **HTML + inline SVG 當 claude.ai Artifact** | ✅ 產出 + 重新發布；你在同一 URL 看它即時更新 | 同一份 SVG、即時可分享預覽 | **輔助**（你的即時預覽） |
| **PaperBanana**（`paperbanana.me` —— 你用過的那個；文字→圖、五 agent、**可導出可編輯 SVG**） | ⚠️ 否 —— 網頁 GUI，Claude 無法驅動 | 快、漂亮的第一版 | **可選 seeder**：在那生草稿 → 導出 SVG → Claude 接手細修 |
| **matplotlib**（已安裝） | ✅ 但媒材不對 | 資料 plot，不是設計型插畫 | 僅備援 |
| **BioRender / Inkscape / Canva** | ❌ GUI，Claude 無法驅動（不過篩選） | 你手動做的話 icon 庫最好 | 不適合 Claude 驅動迴圈 |

**建議：** 主力＝**Claude 手寫 SVG**（`drawsvg` + `cairosvg` 自我檢查 —— 只需一次
`python -m pip install drawsvg cairosvg`，唯一設定），搭配 **HTML/SVG Artifact** 讓你有即時預覽。
PaperBanana 只當 *seeder* 有用，因為它導出可編輯 SVG、Claude 能接手 —— Claude 沒法在它裡面迭代。

---
*Log — 2026-07-30：與 Alex 腦力激盪後建立為 `2026-07-30_graphical_abstract_design.md` 的中文
版本，兩份同步。鎖定主軸（工程化宿主範圍平台）、版面 A（水平 DBTL）、GH5-Learn → in-trans-Test
→ 模組交換-Build 流程、交付物＝平台/方法、母版→導出版位、不鎖定應用（非臨床、環境型
Pseudomonas）。誠實度機制固定（實線＝已做、虛線＝提議）。圖尚未製作：三項輸入在等，皆來自
教授（host-range 讀出、GH5 樹、in-trans 設計）。對應結果 synthesis 的第 2 題。*
