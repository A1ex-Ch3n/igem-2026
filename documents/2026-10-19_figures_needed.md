# 还缺的图 — 清单

截至 2026-10-19。冻结 2026-10-21 15:00 UTC。

扫描范围：`wiki/pages/` 全部 18 页的占位框与 todo、`wiki-figures-upload/` 的本地导出、
static.igem.wiki 上的实际文件、以及项目 repo `code/output/` 和 `documents/` 里的分析输出。

每条都标了**来源是否已存在**——绝大多数不需要重做实验或重画，只需要导出和上传。

---

## A. 页面上已有占位框，空着就是空着（4 张）

这四处现在显示的是灰色虚线占位框，判委和访客都看得见。

| # | 图 | 页面 | 位置 | 来源 |
|---|---|---|---|---|
| A1 | Φ8 基因组图，结构模块高亮 | **Results** | Figure 1，`results.html:132` | 已有：`code/output/0729_prof_figures/fig_phage_genome_map.png` |
| A2 | 对照验证图（真实 binder / 打乱对照 / 背景分布） | **Results** | Figure 3，`results.html:284` | 已有：`documents/2026-07-13_binding_controls_comparison.png`，另有 `documents/2026-08-21_talk_slides/fig/binding_controls_af2.png` |
| A3 | O-antigen cassette 三株比较 + 45 簇直系同源矩阵 | **Results** | Figure 4，`results.html:472` | 已有：`code/output/0727_o_antigen_comparison/o_antigen_loci_comparison.svg` 和 `fig2_cluster_presence.png`，需合成一张 |
| A4 | Human Practices 历程图 | **Human Practices** | Figure 1，`human-practices.html:152` | **没有，要新做**。等 10-19 的利益相关方访谈结束后再画，必须反映真实发生的事 |

### A1 有个坑，别直接传原图

线上已经有一个 `figures/fig-phage-genome-map.avif`（1800×564），但它**图里烧死了一行标题**写着
"62,416 bp, linear with 77 bp DTR"——长度是 PI 那版 contig 的数字（我们的是 62,338），而且把拓扑
写死成 linear，我们全站的口径是未定。

我已经把标题裁掉了，裁好的在 `wiki-figures-upload/fig-phage-genome-map.png`（1800×464）。
上传时**务必换个新文件名**（比如 `fig-phage-genome-map-notitle.png`），CloudFront 两年缓存，
同名覆盖等于没传。

---

## B. 本地已导出，但没上传到服务器（2 张）

两张都在 `wiki-figures-upload/`，服务器上查是 403（不存在）。
`results.html:657` 那个 "Two figures still to place" 的 todo 等的就是这两张。

| # | 文件 | 该放哪页 |
|---|---|---|
| B1 | `fig-cassette-lps-core-waa.png` | **Results**，O-antigen cassette 那节 |
| B2 | `fig-pairwise-differences.png` | **Results**，抗性突变体那节 |

---

## C. 已上传，但页面里一次都没引用（3 张）

这三张在服务器上是 200，白传了。要么找个地方放，要么就当没有。

| # | 文件 | 建议位置 |
|---|---|---|
| C1 | `fig-bacterial-genomes.avif` | **Results** §01 细菌基因组，或 **Dry Lab** |
| C2 | `fig-phage-tail-module.avif` | **Results** §02 尾刺，或 **Design** |
| C3 | `fig-synteny-4genome.avif` | **Description** 或 **Results**（四基因组共线性） |

---

## D. 整页一张图都没有，但内容明显需要图

| # | 页面 | 现状 | 该补什么 | 来源 |
|---|---|---|---|---|
| D1 | **Proof of Concept** | **0 张图** | 页面按时间叙述了三个跑胶日（09-29 首次出现诱导依赖条带、10-10 Ni-NTA 柱子没洗下东西、10-15 归一化），每一天都该配那天的胶图 | 已有，带标注和泳道定量：`code/output/0915_gel_annotation/`、`0929_gel_annotation/`、`1010_gel_annotation/`（`*_annotated_flattened_color.jpg` + `*_lane_quant.tsv`） |
| D2 | **Experiments** | 0 张图，`experiments.html:150` 有 "Add figure" todo | 两条生长曲线 | 已有：`code/output/0624_od600_phage/2026-06-24_od600_curves.png`、`code/output/0625_od600_phage/2026-06-25_curves_*.png` |
| D3 | **Parts** | 有 3 张结构图，但 `parts.html:143` 的 todo 要的是表达验证 | 表达验证胶图 | 同 D1 的胶图 |
| D4 | **Engineering** | 0 张图 | 工程循环四节（计算筛选 → 糖受体假说 → 功能验证 → 让细菌告诉我们受体）至少该有一张循环示意图 | 没有，要新做（BioRender） |

**D1 是这份清单里最值得做的一件。** Proof of Concept 是论证"构建体确实表达了"的页面，
而全站唯一的直接实验证据——蛋白胶——一张都没放上去。胶图连标注带定量都现成。

---

## E. `model.html:348` 那个导出清单里有两项做不到

Dry Lab 页列了六张"已存在、待导出"的图，其中两项在 repo 里找不到任何对应文件：

- **CDS_0024 的 3D 结构模型** —— 从来没建过。CDS_0024 是 PhageRBPdetect 找出来的，
  但没有为它跑过结构预测。
- **CDS_0012 GH5 结合位点（带 cellotetraose）** —— 没有任何带配体的模型文件。

这两条建议直接从那个清单里删掉，而不是去追。留着等于承诺了做不到的东西。

---

## 汇总：优先级

| 优先级 | 事项 | 工作量 |
|---|---|---|
| 1 | **D1** Proof of Concept 补三张胶图 | 导出 + 上传，图是现成的 |
| 2 | **A1 / A2 / A3** 填掉 Results 的三个占位框 | A1 重传裁剪版；A2 直接传；A3 要合成 |
| 3 | **B1 / B2** 两张已导出的传上去 | 纯上传 |
| 4 | **D2** Experiments 生长曲线 | 导出 + 上传 |
| 5 | **A4** Human Practices 历程图 | 访谈后新做 |
| 6 | **C1–C3** 给三张孤儿图找位置 | 决定放哪 |
| 7 | **E** 修掉 Dry Lab 那两条做不到的 | 删两行 |
| 8 | **D4** Engineering 循环示意图 | 新做，可选 |

---

## 上传时的两条硬规矩

1. **永远用新文件名**。static.igem.wiki 在 CloudFront 后面，`cache-control: max-age=63072000`
   （两年），同名覆盖之后边缘节点不回源——这次 BioRender 那四张已经踩过一次，
   query string、`no-cache` 头、Range 请求全都绕不过去。
2. **正文插图导出时勾透明底**。图框底色是 `--paper` #FAFAF6 不是纯白，白底图会在框里透出一块亮斑。
   （**header 背景图相反**，必须纯白不透明，那边走 `mix-blend-mode: multiply`。）

传完把 URL 给我，我负责替换占位框、写图注和 alt 文字、调尺寸、build 推送。
