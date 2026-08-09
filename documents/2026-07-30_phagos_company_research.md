# Phagos（phagos.com）公司研究：運作模式與核心科學技術
# Phagos company research: how they operate and their core science

**日期 / Date:** 2026-07-30　|　**分支 / Branch:** `results-synthesis-0729`　|　**來源 / Sources:** 官網、Series A 新聞稿原文 PDF、創辦人受訪、Nature Microbiology 論文（見文末清單）

> 所有 **> 引號區塊** 都是**原文逐字引用**（英/法文不翻譯，以免失真）；中文為我的解讀，兩者分開放。

---

## 一句話結論 / Bottom line

**中文：** Phagos 是 2021 年成立的法國公司（巴黎近郊 Suresnes），把**噬菌體療法賣進畜牧業**，核心賣點不是某一支噬菌體，而是**一套「平台」拿到了法規許可**——他們自稱是全世界第一家被允許販售「個人化（客製化配方）」噬菌體獸藥的公司。科學上他們的主張是：**用 AI 讀完整的噬菌體基因體與細菌基因體，直接預測交互作用（誰能殺誰）**，不做結構對接，因此可在 2 個月內為單一農場配出新藥。但**他們沒有任何同行審查論文、專利也還沒公開**（我查了 Crossref / Europe PMC / Google Patents，見「證據缺口」）；技術可信度目前主要靠**共同創辦人 Adèle James 博士的學術出身**（Roscoff 站 Le Roux 實驗室，Piel et al. 2022 *Nature Microbiology*，81,926 組 host–phage 交叉感染矩陣）來支撐。

**EN:** Phagos (founded 2021, Suresnes/Paris) sells phage therapy into livestock farming. Their moat is
regulatory, not a single phage: they claim the world's first authorization to market *personalized*
phage-based veterinary drugs. Scientific claim: an AI that reads **whole genomes of phages and
bacteria and predicts their interactions** — no structural docking — enabling a farm-specific drug in
2 months. Caveat: **zero peer-reviewed output attributable to the company, patent filed but not yet
published.** Their technical credibility traces to co-founder Dr Adèle James's PhD work on natural
Vibrio–phage populations (Piel et al. 2022, *Nature Microbiology*).

---

## 1. 公司基本資料 / Company facts

| 項目 | 內容 | 證據 |
|---|---|---|
| 成立 | 2021 | 新聞稿："Founded in 2021 by Alexandros Pantalis and Dr. Adèle James" |
| 地點 | 5 Rue Gardenat Lapostol, 92150 Suresnes, France | 官網頁尾 |
| 創辦人 | Alexandros Pantalis（CEO）、Dr Adèle James（共同創辦人 & CTO） | 新聞稿 + James 的 LinkedIn 職稱 |
| 產品名 | **Alphagos**（官網另見 "Alphagos™"） | 官網 platform 頁 |
| 目標市場 | chicken, cattle, swine, shrimp farms | 官網首頁 |
| 目標病原 | Salmonella、E. coli（另有報導提 Enterococcus cecorum） | 新聞稿 "(Salmonella, E. coli…)" |
| Series A | €25m（美版新聞稿寫 $30m），2025-10-08 | 兩份新聞稿 PDF |
| 投資人 | co-leads: CapAgro, Hoxton Ventures, CapHorn, Demeter；另有 Acurio Ventures, Citizen Capital, Entrepreneur First, Founders Capital, Station F | 新聞稿 |
| 團隊 | 50 人，90% 科學/技術背景 | 新聞稿："50 employees, 90% of whom have scientific and technical backgrounds (microbiology, computer science, R&D, data, AI)" |
| 官網計數器 | 50 EMPLOYEES / 23 NATIONALITIES / 11 CLINICAL TRIALS / €30M FUNDING / 68-32 F/M RATIO / 1M+ ANIMALS TREATED | about-us 頁的數字計數器（數字由前端動畫呈現，文字標籤逐字如下方引用） |

官網 about-us 的計數器標籤原文（數字本身是動畫，標籤是靜態文字）：

> "CLINICAL TRIALS — demonstrating efficacy and safety of our AI-powered phage treatments."
>
> "ANIMALS TREATED — so far on the field, contributing to a healthier food chain, less reliant on antibiotics."

⚠️ 注意：官網 FUNDING 計數器顯示 €30M，但 Series A 新聞稿是 €25M；合理解讀是 €30M＝累計募資（含種子輪），但**官網沒說清楚**。

---

## 2. 他們怎麼運作 / How they operate

### 2.1 五步流程：Alphagos 平台

官網把運作拆成五步，原文：

> "01.DIAGNOSE　02.IDENTIFY　03.DESIGN　04.TEST　05.DEPLOY"
>
> "We receive your isolated bacterial strain and environmental samples to design your treatment and monitor the evolution of the bacteria."
>
> "The Alphagos platform combines our expertise in microbiology and AI to design ultra targeted bacterial treatments using phages. Treatments are continuously updated to ensure animals stay healthy without contributing to antimicrobial resistance (AMR)."

**中文解讀：** 這是「送檢體 → 定序/比對 → AI 配 cocktail → 驗證 → 出貨」的**服務型（service）模式**，不是賣固定成分的藥。農場的菌株變了，配方就跟著改——這也是他們為什麼一定要「平台級」法規許可，而不是單一產品許可。

交付與速度（原文）：

> "We can design and deploy a personalized cure in only 2 months"
>
> "New medicines tailored to your farm can be designed in as little as 2 months using our AI models."
>
> "Non-invasive administration — Easy application through water, feed, or spray provides convenient, stress-free delivery that ensures animal comfort and welfare."
>
> "Regulatory compliant — Meets food safety standards without withdrawal periods, ensuring continuous production and high-quality products for consumers."

Pantalis 在法國農業媒體 Agra 的受訪補了**產能與物流**細節（法文原文）：

> "nous arrivons grâce à notre technologie de caractérisation d'un phage, à un résultat en quelques minutes et parfois même quelques secondes"
>
> "en deux mois seulement, nous sommes capables de mettre à disposition un nouveau médicament vétérinaire"
>
> "Chaque phage est efficace contre un certain nombre de souches, parfois une, parfois plusieurs"
>
> "notre solution est personnalisée et qu'elle doit le rester, parce que les souches peuvent elles aussi évoluer"

同篇報導整理的營運數字：實驗室約 **100 m²**，月產能可處理**數千萬隻動物**；劑型是**液體、稀釋於飲水**；畜種為豬、蛋雞/肉雞、乳牛/肉牛。

### 2.2 真正的護城河：法規許可（這一段要小心讀）

公司主張（新聞稿原文）：

> "Phagos has become the world's first company authorized to market personalized phage-based veterinary drugs — a groundbreaking regulatory milestone marking a major turning point in how bacterial infections are fought."
>
> 法文版："Phagos devient la première entreprise au monde autorisée à commercialiser des médicaments vétérinaires sur-mesure à base de phages"

官網時間軸把它寫成**平台許可**：

> "2025 — Alphagos receives world's first **phage platform authorization** for use in animal farming."

Pantalis 自己的說法（Agra 受訪，法文原文）最關鍵：

> "il s'agit d'une première mondiale, aucun pays n'ayant réglementé les phages de cette manière-là"
>
> "**Il s'agit d'une autorisation de notre plateforme**"

**各方說法並存（我不擅自挑一個）：**

| 來源 | 說的是什麼許可 | 機關 |
|---|---|---|
| Phagos 新聞稿 | "first authorization to market personalized veterinary phage-based treatments **on EU soil**" | 未指名 |
| Pantalis（Agra） | 「**我們平台**的許可」，並稱是世界首例（無任何國家這樣管理過噬菌體）；**確切核准日期在受訪中沒講**（該報導日期為 2025-10-08，勿當成核准日） | ANMV（法國獸藥署，隸屬 Anses） |
| Process Alimentaire（法媒） | "Depuis mai 2025, l'entreprise figure dans la liste des **établissements préparateurs de médicaments vétérinaires autorisés en France**." | ANMV 的**製藥廠/調製機構名冊** |
| Protein Signals（產業分析） | 歸因於 EMA 與 EU Regulation 2019/6 框架（"created a specific pathway for veterinary phage therapies with variable composition"），並提到 EMA 2023-10 指引與 European Pharmacopoeia 的 phage 專章 | EMA/EU 框架 |

**中文解讀（重要）：** 「列入法國獸藥調製機構名冊」和「取得某個產品的上市許可（AMM）」**不是同一件事**。目前公開證據最扎實的是**法國 ANMV 層級**、且性質偏向**平台/機構級**的授權，再由公司包裝成「歐盟第一」。EMA 那條線是產業分析者的框架推論，不是官方文件。我試著直接查 ANMV 的 `etavet` 機構名冊做獨立驗證，但那是 ASP 表單站、無法程式化查詢，**未能獨立確認**。要跟教授報告時建議這樣說：**「平台級、法國核准、公司自稱歐盟首例；產品級 AMM 未見公開文件。」**

### 2.3 商業階段

> "Field deployment has already begun with leading industry players, marking an important milestone toward the adoption of phage therapy."（新聞稿）
>
> "only for use on farms by prescription of a veterinarian."（官網，處方藥定位）

資金用途三條（新聞稿原文）：

> "Objectives: deploy veterinary treatments in the field, develop the next generation of patented AI technology for phage discovery, and accelerate international expansion."

法文版把 AI 的用途講得更精確——**是用來「表徵噬菌體」**：

> "développer la nouvelle génération de son IA brevetée [pour la caractérisation des phages]"

---

## 3. 主要科學技術 / Core science and technology

### 3.1 核心技術主張：全基因體 → 交互作用預測

新聞稿（最明確的一句技術描述）：

> "The company has also filed a patent for its AI technology, **capable of analyzing the full genomes of both phages and bacteria to predict their interactions** and make phage therapy a scalable, targeted, and effective solution."
>
> 法文版："Elle a également déposé un brevet sur sa technologie d'IA, capable d'analyser **l'intégralité des génomes de phages et de bactéries** pour prédire leurs interactions"

二手報導的補充描述（非公司原話，標記為二手）：

> "analyzes complete genomes of both bacteriophages and target bacteria to predict which phage strains will successfully lyse which bacterial variants" — Protein Signals
>
> "generates treatment recommendations in minutes rather than the 28 to 386 days historically required to match phages to patient isolates" — Protein Signals
>
> "Its AI platform simulates millions of interactions virtually, predicting the most effective combinations instantly" — AgNavigator
>
> "With training data from public databases and its own lab-generated data, Phagos's AI models will predict which phages are the most effective against any given infection" — AWS case study
>
> "a platform that uses **generative AI** to match bacterial strains with effective phages" — AWS case study

官網自己對「為什麼一定要 AI」的說法：

> "The complexity of genomic interactions between phages and bacteria creates infinite potential combinations. **Only artificial intelligence can decode these biological relationships fast enough** to allow phage therapy to scale."

**中文解讀：** 技術路線是 **sequence/genome-level 的 ML 預測 host range**，明確**不是**結構生物學路線（沒有任何 RBP–receptor docking、結構預測的字眼）。這一點對我們很有參考價值——見第 5 節。

### 3.2 噬菌體庫（wet lab 那一半）

> "One of the world's largest characterized phage collections"
>
> "Our phages target the bacterial strains hitting farms the hardest. **Each phage's DNA is fully sequenced and characterized** to advance our product development and R&D efforts."
>
> "We grow our collection every year through ongoing environmental sampling to stay ahead of emerging threats."

只用溶菌性噬菌體（官網 Phage 101）：

> "Phage therapy only uses lytic phages for their ability to eliminate bacteria quickly."
>
> "TEMPERATE — Temperate phages lie dormant inside bacterial DNA for varying amounts of time before eventually destroying the bacteria through cell lysis."

⚠️ **庫的規模沒有數字**：「世界最大之一」但不給 N（幾百？幾千？）。官網也沒有菌株庫規模、預測準確率、驗證資料。

### 3.3 科學根源：CTO 的博士工作（這是最硬的證據）

Phagos 自己沒有論文，但 CTO Adèle James 的學術出身有。她博士期間在 Roscoff 海洋站（Le Roux 團隊）做**天然族群裡的 Vibrio–噬菌體共演化**，是這篇的作者之一：

**Piel D, Bruto M, Labreuche Y, …, James A, …, Le Roux F. "Phage–host coevolution in natural populations." *Nature Microbiology*, 2022. PMID 35760840, doi:10.1038/s41564-022-01157-1**

摘要原文（關鍵句逐字）：

> "we isolated **195 Vibrio crassostreae strains and 243 vibriophages** during a 5-month time series from an oyster farm"
>
> "**Cross-infection studies of 81,926 host–phage pairs** delineated a modular network where phages are best at infecting co-occurring hosts, indicating local adaptation."
>
> "Successful propagation of phage is restricted by the ability to **adsorb to closely related bacteria** and further constrained by **strain-specific defence systems**. These defences are highly diverse and predominantly located on mobile genetic elements"
>
> "epigenetic and genomic modifications enable phage to adapt to bacterial defences and **alter host range**"

AWS 報導提到她最早的概念驗證（二手）：

> "James managed to use phages to demonstrate a **40% reduction in mortality in infected oysters**"

**中文解讀：** 這解釋了 Alphagos 的思想來源。她的博士研究產出的正是「**菌株層級的大規模 host-range 矩陣**」（8 萬多組配對）+「**吸附能力 + 菌株特異防禦系統決定成敗**」這兩個結論。把這種矩陣當標註資料（labels）、把雙方基因體當特徵（features）去訓練模型，就是 Alphagos 的原型。也就是說：**他們的「AI」很可能是 supervised host-range 預測（基因體特徵 → 感染成敗），而非從機制出發的模擬**。

### 3.4 抗性管理的說法

> "Resistance-proof — Alphagos' evolving formulation means it keeps up with bacterial resistance. **AMR will never be an issue again.**"
>
> "Adaptive precision approach — Our formulation continuously evolves to stay ahead of bacterial resistance."

**中文解讀：** 「AMR will never be an issue again」是**行銷過頭的一句**。Piel et al.（他們自家 CTO 的論文！）證明的正好是細菌防禦系統多樣、且位於可移動遺傳元件上、會快速交換——所以正確講法是「**用更新配方追著抗性跑**」（軍備競賽），不是「抗性不再是問題」。這句話跟他們自己的科學基礎有張力，值得在報告裡點出來。

---

## 4. 證據缺口 / What is NOT public（我實際查過的負面證據）

| 查詢 | 結果 |
|---|---|
| Crossref `query.affiliation=Phagos` | **0 筆** |
| Europe PMC `AFF:"Phagos"` | 1 筆，且是 2023 年 flavivirus NS5 論文，與本公司**無關**（字串誤中） |
| Google Patents `assignee=Phagos` | **0 筆已公開**（與「已提交申請」一致：申請後 18 個月才公開，2025 才申請的話正常還看不到） |
| 官網/新聞稿的模型細節 | 無模型架構、無訓練資料規模、無準確率、無 benchmark |
| 田野試驗資料 | 只有計數器數字（11 clinical trials、1M+ animals treated），**沒有任何試驗報告或 endpoint 數據** |
| 噬菌體庫規模 | 只有 "one of the world's largest"，無 N |

**中文解讀：** 以「科學證據」的標準看，Phagos 目前是**零同行審查產出**的公司；能引用的一手材料只有官網、新聞稿、創辦人受訪。這不代表技術不成立（法規許可是硬證據，需要提交 dossier 才拿得到），但**任何效能數字目前都無法獨立驗證**。跟教授討論時這點務必講清楚。

---

## 5. 對我們專案的意義 / Why this matters for our iGEM project

1. **他們選的路線正好是我們證明走不通的那條的反面。** 我們 0713 的結論是 9-2-1 Φ8 的 tail spike 是 β-helix depolymerase、受體是 LPS O-antigen，因此 **RBP × OMP 的蛋白–蛋白 docking 無效**（見 `2026-07-13_phage_rbp_depolymerase_findings.md`）。Phagos 完全不碰結構，直接做 **genome → host range 的 supervised 預測**。這是對我們「別再嘗試結構對接」判斷的一個**產業側佐證**。
2. **他們的訓練資料形狀值得我們抄。** Piel et al. 的 81,926 組交叉感染矩陣＝「菌株 × 噬菌體」的密集標註。我們手上的 1673 條文獻 RBP 序列（`build_rbp_database.ipynb`）是**特徵側**，缺的是**標註側**（誰能感染誰）。若要做預測，缺口在濕實驗 host-range 矩陣，不在序列數量。
3. **「菌株特異的防禦系統」是我們沒納入的變數。** 他們 CTO 的論文明講成敗受**吸附 + 菌株特異防禦（多在 MGE 上）**雙重限制。我們目前的思考只到受體（吸附）這一層。
4. **法規/安全敘事可直接借用。** 只用 lytic phage、不用 temperate phage 的理由、獸醫處方定位、免疫系統自然清除的說法，都是寫 safety form 時好用的公開先例框架（可對照 `2026-06-30_safety_check-in_phage_DRAFT.md`）。我們自己的 9-2-1 Φ8 **可能是 temperate**（見 phage genome sequencing 記錄），按 Phagos 的產業標準，這種噬菌體是不會進治療產品的——這對我們的敘事是個要面對的點。
5. **可提的問題（如果教授要接觸他們）：** 訓練標註是怎麼取得的（規模、是否 quantitative host range）？模型是 sequence-based classifier 還是 embedding + 交互作用預測？受體層級的資訊（O-antigen 血清型）有沒有進 feature？平台許可的法源條文是哪一條？

---

## 6. 來源清單 / Sources

一手 / Primary
- 官網首頁、platform、how-it-works、about-us：https://www.phagos.com/ ・/platform ・/how-it-works ・/about-us
- Series A 新聞稿（英文，EU 版）PDF、美版 $30m PDF、法文 COMMUNIQUÉ DE PRESSE PDF — 公司 Media Kit（Google Drive，官網頁尾 "Media Kit" 連結）；2025-10-08，Paris
- Series A 頁面：https://www.phagos.com/resources/series-a-fundraising
- Pantalis 受訪（法文，最具體的營運/法規細節）：https://www.agra.fr/agra-innovation/alexandros-pantalis-phagos-nous-allons-deployer-nos-traitements-base-de-bacteriophages-usage
- Piel et al. 2022, *Nature Microbiology*（CTO 為共同作者）：https://doi.org/10.1038/s41564-022-01157-1 ・PMID 35760840

二手 / Secondary（標記過的推論來源）
- AWS 案例報導（generative AI、訓練資料、牡蠣 40% 概念驗證）：https://www.aboutamazon.com/news/aws/aws-phagos-ai-antibiotic-resistance-bacteria-phage-therapy
- Protein Signals 產業分析（EMA / Reg 2019/6 框架、28–386 天對比）：https://proteinsignals.com/p/phagos-series-a-why-phage-therapy-s-fourth-attempt-may-finally-work
- AgNavigator（法規與平台描述）：https://www.agnavigator.com/Article/2025/10/14/is-phagos-investor-backing-and-regulatory-greenlight-the-turning-point-for-phage-therapy-in-the-eu/
- AgFunderNews（創辦人引言、已申請專利、四大畜種）：https://agfundernews.com/france-based-phagos-lands-29m-to-further-develop-its-antibiotic-alternative-for-livestock
- Process Alimentaire（ANMV 機構名冊，2025 年 5 月起）：https://www.processalimentaire.com/qualite/antibioresistance-phagos-leve-25-meu-pour-mettre-fin-aux-maladies-bacteriennes
- Microbiome Times / The Phage / EU-Startups：新聞稿轉載，數字一致

未能取得 / UNDONE
- ANMV `etavet` 機構名冊的獨立查核（ASP 表單站，無法程式化查詢）→ 建議人工到 https://anmv.anses.fr 查「Phagos」
- 專利全文（尚未公開；2026 年下半年後可再查 Espacenet / Google Patents，關鍵字 assignee=Phagos）
- 任何 peer-reviewed 效能數據（目前不存在）

---

*Log — 2026-07-30：依教授提到的公司做背景研究。方法：官網四頁逐字擷取 + Media Kit 新聞稿 PDF 原文（英/美/法三版）+ 創辦人法文受訪 + Crossref/Europe PMC/Google Patents 反向查證。三個要點：(1) 護城河是**平台級法規許可**（法國 ANMV；「歐盟第一」是公司自稱，產品級 AMM 未見文件，各方說法已並列保留）；(2) 技術是**全基因體 → host range 的 ML 預測**，完全不走結構對接，與我們 0713 放棄 docking 的結論方向一致；(3) **零同行審查論文、專利未公開**，可信度目前靠 CTO 的 Piel et al. 2022（81,926 組交叉感染矩陣）支撐。ANMV 名冊查核與專利全文列為 UNDONE。*
