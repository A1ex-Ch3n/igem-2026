# Registry part page 草稿（中文版）

英文正本：[`README.md`](README.md)。**送件時貼英文版**，中文版只是給團隊看懂、討論與校對用。

每個 part 一個檔案，照 Registry 的五個文件區塊寫（**design / experiment / characterisation /
application / discussion**），可以直接貼。流程、截止日與「送出後永久鎖死」的規則看
[`../2026-10-18_registry_submission_guide.md`](../2026-10-18_registry_submission_guide.md)。

| 草稿 | Part | 寫好了嗎 |
|---|---|---|
| [`CDS10_WT.md`](CDS10_WT.md) ／ [中文](CDS10_WT_zh.md) | CDS_0010 res 105–917 — 功能未知的 fiber | ✅ |
| [`CDS11_WT.md`](CDS11_WT.md) ／ [中文](CDS11_WT_zh.md) | CDS_0011 res 305–941 — tail spike 的 β-helix depolymerase body | ✅ |
| [`CDS12_WT.md`](CDS12_WT.md) ／ [中文](CDS12_WT_zh.md) | CDS_0012 res 117–477 — GH5 glycoside hydrolase | ✅ |
| [`CDS12_ANC_Node1.md`](CDS12_ANC_Node1.md) ／ [中文](CDS12_ANC_Node1_zh.md) | 重建祖先 GH5，node 1（`e1`） | ✅ |
| [`CDS12_ANC_Node40.md`](CDS12_ANC_Node40.md) ／ [中文](CDS12_ANC_Node40_zh.md) | 重建祖先 GH5，node 40（`e40`） | ✅ |
| [`CDS12_ANC_Node281.md`](CDS12_ANC_Node281.md) ／ [中文](CDS12_ANC_Node281_zh.md) | 重建祖先 GH5，node 281（`e281`） | ✅ |
| collection 頁 | 六個 part 當成一套工具組 | ⬜ **UNDONE** |

**祖先草稿等的那兩個欄位，教授 2026-10-18 的交付資料都答了**，現在已經補進去。(1) 重建方法：
CDS_0012 對 NCBI nr 取前 1000 hits、SeaView 內 MUSCLE 比對並人工修剪、PhyML 建樹（WAG，p-inv 0.1，
100 bootstrap）、IQ-TREE 以同一矩陣 midpoint-rooted 推祖先。(2) 節點順序：CDS_0012 到樹根這條路徑上
每個節點都重建了，編號是任意識別碼而非深度，順序 1, 2, 38, 39, 40, 42, 267, 277, 281 由最晚近到最古老，
與草稿原本就有的 identity 數字一致。出處：
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md) A1。
那三頁可以直接貼。

## 這些草稿要守住的區分

三個野生型蛋白是**三種不同的東西**，而且這個專案已經混淆過一次（教授問的是「tail spike *裡面*
的酵素 domain」，但確認的酵素其實是另一個獨立的蛋白）。

| | CDS_0010 | CDS_0011 | CDS_0012 |
|---|---|---|---|
| 是什麼 | virion fiber，**功能未知** | **tail spike** — 結構蛋白，附著在病毒顆粒上 | **游離酵素**，不是 virion 的組成 |
| 酵素宣稱 | **沒有** | **β-helix depolymerase** | **GH5 glycoside hydrolase** |
| 證據 | 只有一個涵蓋 96 aa 的微弱 IspD template；其餘約 800 aa 完全沒有 template | **只有摺疊層級**：AF3 對 res 111–941 沒有任何 template，β-helix 是用 H-bond offset 週期判定的，而且沒有具名的同源蛋白 | **全專案最強**：4/4 個 AF3 template 都是 GH5 endoglucanase（1ECE 帶 cellotetraose、1VRX、4TUF、2ZUM），pLDDT 95–98 |
| 寡聚狀態 | AF3 job 裡是單體 | **三聚體**（941 aa × 3，約 238 Å 長） | 單體 |
| 共通處 | Calx-β anchor，與 CDS_0011 有 42% identity／107 aa，兩個 anchor 疊合 **0.50 Å** | 與 CDS_0010 同一個 anchor | — |

所以：**CDS_0011 是 tail spike，它的 body 是 depolymerase；CDS_0012 是 template 確認的 GH5
glycoside hydrolase，而且是另一個獨立的蛋白。** 絕對不要寫成「tail spike 帶有一個 GH5
domain」——我們沒有這個證據，而且這兩個宣稱的證據強度差很多。CDS_0010 一律寫
**unknown function**：教授已於 2026-07-29 撤回 glycosidase 的說法。

## 序列

可直接送件的序列由
[`../../code/1018_construct_structures/registry_sequences.py`](../../code/1018_construct_structures/registry_sequences.py)
產生 → `code/output/1018_construct_structures/registry/registry_parts.{ffn,faa,tsv}`。

Twist 訂單表裡的是 **insert，不是 part**：它有自己的 stop codon，但**沒有起始 codon**（translation
是從 pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` leader 開始），而且 CDS11 的 insert 前面還多一段我們自己
設計的 `GGSGGGGS`-His6-`ENLYFQ`-`GGGGSGGGGS` 純化 linker。因此草稿送出的是
**`ATG` + 蛋白自身的 CDS + stop**，載體 leader 和那段 linker 寫在 *design* 段說明，不放進序列：

| Part | 送件序列 | 蛋白 | 修剪內容 |
|---|---|---|---|
| `CDS10_WT` | 2445 bp | 814 aa | 加上 `ATG` |
| `CDS11_WT` | 1917 bp | 638 aa | 加上 `ATG`，移除 30 aa 純化 linker |
| `CDS12_WT` | 1089 bp | 362 aa | 加上 `ATG` |

⚠️ part 一旦離開 Draft，**序列、作者、授權三者永久鎖死**。在任何人按下 *Send for Screening*
之前，六個 part 的 His6 政策要一次談定。

---
*Log — 2026-10-18：建立。數字來自 `code/output/1018_construct_structures/`；結構宣稱與其證據等級
來自 [`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。*
