# 五分鐘報告 —— 結構、紅線、時間分配

> **逐字稿的正本在 [`2026-08-21_talk_slides/slides.tex`](2026-08-21_talk_slides/slides.tex) 每頁的 `\note{}`（英文），
> 印出來是 `slides_notes.pdf`。這份文件只留骨架、紅線與排練檢查，不放第二份逐字稿。**

狀態基準：`documents/2026-07-29_results_synthesis_EN.qmd`（2026-07-29）＋
`documents/2026-07-30_graphical_abstract_design.md`（誠實標示規則）。
投影片：[`2026-08-21_talk_slides/slides.pdf`](2026-08-21_talk_slides/slides.pdf)。
CDS 編號一律用 PI 的 `UUAIURNK_`。

---

## 0. 主線句

> 因為**噬菌體只吃一株菌、而現在配對只能試錯**，所以我們要**改造決定宿主的那顆蛋白**；
> 要改造它，得先知道**是哪個基因**和**它要抓什麼**——我們發現**尾突 CDS_0011 是 β-helix depolymerase（抓的是糖，不是蛋白）**，
> 而**三株菌在同一個保守槽裡帶三套非同源的 O-antigen**，所以三株就是三個不同的靶。
> 接下來用**演化**提供變體：**尾突決定「誰被認出來」，depolymerase 決定「什麼能被切開」**，
> 所以 PI 正在建 **GH5（CDS_0012）全序列的樹並做 ancestral state reconstruction**，
> 表達祖先酵素、和 fiber **in trans** 一起挑戰三株菌。
> （另外 CDS_0011 有 15,775 條序列的比對，但那撐的是**保守度剖面**，不是祖先重建。）

**台上那句問題（第 3 頁放大，第 6 頁用同樣的字回答）：**

> Before you can redesign the targeting part: **which gene is it, and what must it recognise?**

---

## 1. 六頁的角色與秒數（英文正本 652 字）

| 頁 | 角色 | 字 | 秒 @125wpm |
|:--|:--|--:|--:|
| 1 | 標題：我們在做「改造零件」 | 36 | 17 |
| 2 | Context：為什麼要改造、我們自己採樣定序 | 106 | 51 |
| 3 | **Design loop**：pick gene → define target → GH5 祖先酵素 → build → in trans test（含誠實標示） | 150 | 72 |
| 4 | Step 1–2 的結果：尾突是 depolymerase，靶是糖（含失敗的 docking 對照） | 116 | 56 |
| 5 | 靶在三株之間不同 —— 這就是可以轉的把手 | 112 | 54 |
| 6 | Loop 現況 + limitation + 未來三個月 | 132 | 63 |
| **合計** | | **652** | **313** |

135 wpm 約 290 秒。超時先砍：第 3 頁「step two」那句、第 1 頁副標那句。

**誠實標示（跟 graphical abstract 同一套）**：實線＝有資料；虛線＝進行中／提案。
第 3 頁的 loop 只有前兩格是實線。

---

## 2. 台上不能講的話（紅線）

| 不要說 | 要說 |
|:---|:---|
| 「我們用 metagenome 的 variable region 找出決定專一性的位點」 | 「variable ≠ specificity-determining；MGnify 沒有宿主標籤，那條路走不通。15,775 條序列支撐的只有保守度剖面」 |
| 「我們做了 ancestral reconstruction」 | 「**PI 正在建樹，還沒有結果**」（虛線） |
| 「祖先重建是對尾突 CDS_0011 做的」 | 「祖先重建是對 **GH5 / CDS_0012** 全序列做的；15,775 條的比對是 CDS_0011 的，用途是保守度剖面」 |
| 只講 affinity 會變 | 「這條線建立在 **affinity ~ binding ~ infection** 的假設上，要講出來」（PI 自己標的 caveat） |
| 「三個構築已經測過」 | 「7/27 送 Twist，還沒表達」 |
| 「O-antigen 差異解釋了我們觀察到的宿主範圍」 | 「這是預測；7/4 的實驗已經做了，讀值待回」 |
| 「Strain 1 是 O-type X」 | 「這個 taxon 沒有 serotype 架構，我們比的是座位結構」 |
| 「這是 T7-like / Autographiviridae」 | 「virion 模組像 podovirus；跟 T7 的 ortholog 幾乎是 0，『T7-like』只是組織上的類比」 |
| 「β-helix 屬於 X 家族」 | 「幾何上是 depolymerase 的 β-helix；還沒 foldseek/DALI 命名」 |
| 「Strain 1 沒有 flippase 和 polymerase」 | 「那兩個基因的家族歸屬待 InterProScan」 |
| 舊編號 `FHABPWTM_` / 舊的 0708 基因體圖 | PI 的 `UUAIURNK_` 編號 + App B1/B2 |

---

## 3. 備用頁（投影片第 8–14 頁）

1. 基因挑選與構築（結構模組順序、CDS_0024 是 Pharokka 漏掉的第二個 depolymerase、CDS_0012 = GH5、三個構築的殘基範圍、CDS_0010 是未知蛋白）
2. 座位怎麼抓、orthology 怎麼判（ihfB 錨點、MMseqs2 30%/50%、為什麼不能用產物名稱；跨 strain best-hit 為何不與 45/4 對得上）
3. cluster 矩陣（45 × 3）
4. limitation 全表（含 variable ≠ specificity）
5. 三株細菌基因體
6. 噬菌體 tail / RBP 模組
7. 酶結構全圖（D 是 CDS_0012，另一個蛋白）

---

## 4. 排練檢查

- 計時三次取最慢一次；第一次通常比正式短 15%。
- 第 3 頁單獨計時，超過 65 秒就砍 step two 那句。
- 每頁開頭不要「那麼我們接下來看一下」。
- 講不到的箭頭和字，全刪。

---

## UNDONE / 需要你補的

- **UNDONE**：第 2 頁的抗藥性數字＋出處（紅字 `[AMR figure + source — Alex]` 會投出來）。
- **UNDONE**：確認第 3 頁那句問題的英文用字——第 6 頁要用同樣的字回答。
- **UNDONE**：GH5 ancestral tree 的進度要跟 PI 對一次（`documents/2026-07-29_pi_conversation/README.md` P2 = in progress），才知道台上能講到多細、以及 in trans 挑戰誰來做。

---

### 文件記錄

- 2026-08-21 建立；同日改為英文並改寫敘事主線。
- **敘事主線＝改造噬菌體零件（DBTL loop）**，不是以糖為開場；糖是 step 2 的答案，不是故事的起點。
- 內容依據 `2026-07-29_results_synthesis_EN.qmd`（§2 材料、§3 結果表 A9/B1–B3/C1–C5/F1/F5、§4 O-antigen 座位比較、§5 next steps）與 `2026-07-30_graphical_abstract_design.md`（DBTL 分區與實線／虛線規則）。
- 第 4 頁 = C1+C2（+F1 當反面對照）；第 5 頁 = A9/§4（+§4.4 clone pair 對照）；第 3 頁 step 3–5 全部是提案／進行中。
