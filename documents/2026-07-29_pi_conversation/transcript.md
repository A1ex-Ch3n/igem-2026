# 逐字稿 — 2026-07-29 10:50–11:17

原始對話，未編輯。摘要與判讀見 [`README.md`](README.md)。

⚠️ 標記 `[截斷]` 的幾則在貼上時就是不完整的，內容未知。

---

**10:50:53 Alex** — 1. The three Twist constructs — one thing I want to confirm before they're synthesized.

I translated the three plasmids to check what will be expressed, and the filenames and the sequences don't quite agree. `CDS11_WT_CTERM_HIS6TAG` actually carries two N-terminal His6 tags (pET-28a's own leader plus the designed GGSGGGGS-His6-TEV cassette) and no C-terminal His6 — the insert ends in its own stop codon, so the vector's C-terminal tag is never translated. The two NOTAG constructs also carry pET-28a's N-terminal His6.

I think the sequences are what we want: res 305–941 is the clean self-contained β-helix body, and an N-terminal tag is the safer choice anyway because res 921–941 looks like a trimerization foldon. So this may just be a naming thing, in which case I'll fix o… `[截斷]`

**10:50:54 Cesar** — I have placed the order for the first 3 constructs

**10:51:30 Alex** — I've saw the email, thank you so much for reaching Twist out!

**10:52:03 Cesar** — `[截斷]` g on any of them

**10:52:51 Alex** — `[截斷]` illustration in few minutes.

**10:53:14 Cesar** — `[截斷]` er group soon

**10:53:19 Alex** — 2. Host range test of Φ8, July 4th.

Could I get the full table from that entry? Specifically Φ8 against 8-5-2 / 10-10-2 / 8-10-2.

This is the direct test of whether the tail spike (CDS_0011) reads the host O-antigen. We just found that the three strains carry three non-homologous O-antigen gene clusters sitting in the same genomic slot — so if Φ8 lyses only 9-2-1/9-6-2, that closes the mechanism. If it also lyses the others, then the second depolymerase we found (CDS_0024, which the annotation had missed) is doing something, and that's a more interesting result. Either way it's the key piece.

**10:54:32 Cesar** — Yes I can go to the lab this week and send the host rang table, but I will need help identifying the date

**10:55:18 Alex** — Sounds good, thank you soooo much! I will digitize all the entries once I land in Ontario.

**10:55:52 Cesar** — My current hypothesis (and this is how science works, directional changes ocurr)

**10:56:38 Cesar** — is that CDS_12 (depolymerase) could improve host range by breaking different glycans

**10:57:00 Cesar** — SO I am building a tree with all GH5 sequences and reconstruct acestrtal states to express them

**10:57:19 Alex** — wow

**10:57:24 Cesar** — if we challenge the affinity of the tail fiber and the differetn depolymerases in trans

**10:57:31 Alex** — That sounds really really cool.

**10:57:32 Cesar** — maybe there affinity changes

**10:57:55 Alex** — I have no idea how to make that happen, but I am more than happy to learn and try it out.

**10:58:11 Cesar** — all of this is under the caveat that the affinity ~ biding ~ infection

**10:58:20 Cesar** — whihc is a safe assumption and we can make it clear

**10:58:41 Alex** — gotcha.

**10:58:47 Alex** — Here's the third question.

**10:58:54 Cesar** — Also to get you inspired "https://www.phagos.com/"

**10:59:19 Alex** — I'm not 100% sure about the variable region part you asked earlier last week.

3. I'd like to check what you have in mind before I build it, because I think there are two quite different versions and they need different data.

What we have on the metagenome side is a set of predicted RBPs from MG08/MG09 (632 and 661 sequences). They have never been aligned against CDS_0011, and more importantly the metagenome contigs carry no host information — we don't know which bacterium any of them infects. So we can show where the fiber varies across environmental relatives, but not which of those variable positions decide what it binds. `[截斷]`

**10:59:32 Alex** — an AI + phage website, interesting

**10:59:37 Alex** — company\*

**11:00:04 Cesar** — basically what we are trying to do

**11:00:29 Cesar** — The metagenome side doesnt matter if they are not associated to any host

**11:00:39 Alex** — I will look into their work and publication if possible

**11:00:42 Cesar** — I was looking earlier and I think we can go bigger

**11:00:47 Cesar** — and I did MGnify

**11:01:02 Alex** — I see, expanding our data beyond the MG sequence we have

**11:01:02 Cesar** — to search for more sequences

**11:01:07 Cesar** — yes

**11:01:26 Alex** — did you find anything specifically interesting

**11:01:33 Alex** — or something we should be aware of?

**11:02:31 Alex** — Here're the last two questions I have:

4. CDS_0010 as a glycosidase — could I see your evidence?

In the AF3 folds you sent, the only template hit on the CDS_0010 body is a weak IspD match over res 361–456; the other ~460 aa have no template at all. CDS_0012 is unambiguous by comparison (all four templates are GH5 endoglucanases, one with cellotetraose bound). If you have a foldseek hit table for CDS_0010 I'd like to add it, since it's one of the three constructs we've ordered.

5. When you say "our three isolates" — which three?

We sequenced five, and by ANI they collapse to three distinct str… `[截斷]`

**11:02:34 Cesar** — a lot of sequences! have not been able to digest

**11:02:59 Cesar** — Yeah I dont know what CDS 10 is

**11:04:17 Cesar** — I thought it was a hydrolyase but not sure

**11:04:29 Alex** — got it, let's assume unknown protein

**11:04:39 Cesar** — I am expressing so maybe we can characterize it

**11:04:46 Cesar** — but for now the cofus \[focus] is CDS11 and 12

**11:05:44 Cesar** — Our phage is a T7-like podophage

**11:06:11 Cesar** — Basically looks similar to group D,

**11:06:37 Cesar** — the long one is the tail (CDS 11) and short one (at least one) is the depolymerase

**11:06:49 Cesar** — You can draw a similar cartoon to that

**11:06:57 Alex** — I see, this helps a lot.

**11:07:06 Cesar** — you need to justify this with synteny

**11:07:11 Cesar** — and similarity

**11:07:22 Alex** — I didn't have this picture in my brain, and it really tells "what it look"

**11:07:35 Cesar** — yeah I wanted to ask

**11:07:38 Alex** — that will be on my todo list

**11:07:46 Cesar** — if its expensive to print 3d figures

**11:07:51 Alex** — no

**11:07:53 Alex** — I will pay for it

**11:07:58 Cesar** — we could print the proteins and assemble it

**11:07:58 Alex** — what's your fav color prof

**11:08:07 Cesar** — its up to you

**11:08:14 Alex** — haha I will do baby blue then

**11:08:38 Cesar** — the funnel and base place \[plate] fibers and depolymerase

**11:09:01 Alex** — noted!

**11:09:52 Cesar** — basically CDS 20, 08, 09, 13, 14

**11:10:04 Cesar** — maybe not 20

**11:10:49 Alex** — I was also folding something similar based on your AF3 results

**11:11:01 Cesar** — yeah perfect.

**11:11:35 Cesar** — 20, 8, 9, 13, 14 really tell (without TEM) that it is a podo/t7 like

**11:12:12 Cesar** — by syntenic assumptions (10,11,12) are the ones that hang from the base and recognize the host

**11:12:17 Alex** — will try to fold it on my side and turned into a printable object as well

**11:12:32 Cesar** — 12 is a depolymerase but we dont know what 10 is

**11:13:20 Cesar** — the cartoon above comes from here "https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.02649/full"

**11:14:16 Alex** — sounds good, I will note that down.

**11:14:22 Alex** — This is really really helpful.

**11:14:31 Alex** — I'm super exciting, espeically for printing them out.

**11:14:41 Alex** — I felt like this is the best use of my printer so far haha.

**11:14:58 Cesar** — remember we are going to print a fluorometer

**11:15:14 Alex** — of course, that's also super cool.

**11:15:46 Alex** — Will try to see the list of parts to order later.

**11:16:38 Cesar** — I can order everything when you are back

**11:17:10 Alex** — amazing, I will organize a shortlist of todos later, and will update some graph and summary for you to check.

*（此處附上兩張圖片，見 `images/`）*

---

*Log — 2026-07-29：貼入原始對話。三則訊息在來源就已截斷，標記為 `[截斷]`；
少數明顯的打字錯誤在方括號中補正，其餘保留原樣。*
