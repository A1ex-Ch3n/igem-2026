# iGEM 2026 deliverables — what is actually still missing

Checked against the live competition API and the 2026 awards text on 2026-10-18,
not from memory. Team **Claremont CA**, #6317, wiki slug `claremont-ca`.

Sources: `https://api.igem.org/v1/competitions/58a7e73a-1e25-457f-9f59-36c47b3f652a/deliverables`
and `/awards`; criteria prose extracted from the frontend chunks
`competition.igem.org/assets/Awards-hgBAJo9D.js` and `deliverablesData-hBZblRe6.js`,
because the pages themselves are a JS SPA.

## Three findings that change the plan

1. **The Judging Form is required, freezes with everything else on 2026-10-21,
   and no document in this repository mentions it.** It carries the project
   title, the project abstract, the medal-criteria declarations with their
   standard URLs, and the special-award self-nominations.
2. ~~`/contribution` returns 404~~ — **corrected 2026-10-19: it now returns 200**,
   as does `/software`. Both were created after this report was written. The
   Bronze blocker is cleared. Still 404: `/safety` and `/measurement`.
3. **Gold changed in 2026.** It is no longer judged directly. Gold is decided by
   the three Special Awards you name on the Judging Form, so the Judging Form is
   now the single document that determines the medal ceiling.

## The deliverable table, as the API returns it

| closes (UTC) | | type | state |
|---|---|---|---|
| 2026-10-07 | required | `safety-project-form` | **closed already** — settled, not our problem now |
| 2026-10-21 15:00 | required · freeze | `judging-form` | **nothing written** |
| 2026-10-21 15:00 | required · freeze | `parts` | drafts written, upload in progress elsewhere |
| 2026-10-21 15:00 | required · freeze | `attribution-form` | saved, a few PI answers outstanding |
| 2026-10-21 15:00 | required · freeze | `wiki` | live, gaps below |
| 2026-10-21 15:00 | optional · freeze | `software` | wiki page 404s; licence blocker |
| 2026-10-28 15:00 | required | `video-team-presentation` | **nothing written** |
| 2026-11-15 15:00 | required | `judging-session` | **nothing written** |

Earlier deliverables (village selection, promotion video, safety check-in,
animal use, booth, live stage talk) are all closed.

## Medal criteria, 2026 text

Each criterion is a yes/no vote per judge, decided by majority, ties going to the
team. A team gets the highest medal for which every criterion at that level and
below is yes.

**Bronze** — all three:
1. *Competition Deliverables* — Safety Forms, Wiki, **Judging Form**,
   **Presentation Video**, **Judging Session**. Three of those five are the ones
   with nothing written.
2. *Project Attributions* — the Attributions Form, complete and accurate.
3. *Contribution* — "make a useful contribution for future iGEM teams", documented
   at `2026.igem.wiki/claremont-ca/contribution`, **which does not exist**.

**Silver** — Bronze plus:
4. *Engineering Success* — at least one full turn of the design cycle, at
   `/engineering` (exists).
5. *Human Practices* — "explain how you have determined that your work is
   responsible and good for the world", at `/human-practices` (exists, thinnest
   page on the wiki, being rewritten tonight).

**Gold** — Bronze and Silver plus:
6. *Excellence in Synthetic Biology* — demonstrate excellence toward **three
   Special Awards of your choice**, named on the Judging Form. Judges do not cast
   a separate Gold vote; each judge's rubric score for those three awards is
   converted to a yes/no, and **all three must pass**. At least one must come from
   each list below; the third is free. Naming fewer than three is allowed and
   forfeits Gold.

| General Bio Engineering (pick ≥1) | Specializations (pick ≥1) |
|---|---|
| Best Measurement · Best Model · Best New Basic Part · Best New Composite Part · Best New Improved Part · Best Part Collection | Best Education · Best Entrepreneurship · Best Hardware · Inclusivity · Best Integrated Human Practices · Best Alternative Platform · Safety and Security · Best Software · Best Sustainable Development Impact |

### Which three we can actually evidence

This is the team's decision, not mine. What the repository supports:

- **Best New Basic Part** — strongest. Six documented part drafts, three of them
  computationally designed ancestral sequences that exist nowhere in nature, with
  structure predictions and an explicit design rationale.
- **Best Part Collection** — the same six as one toolbox. Needs the collection
  page that is still unwritten.
- **Best Model** — defensible. AlphaFold/ESMFold structures, the ZymCTRL
  perplexity series across the ancestral nodes, the Foldseek structural taxonomy,
  and a modelling result that genuinely redirected the project. Requires `/model`
  to tell that story as *what we learned*, which was precisely the PI's note.
- **Best Software** — blocked twice over: `/software` 404s, and the repository
  licence (CC BY 4.0) is not OSI-approved, which the criteria require. Fixable,
  but it is two fixes, not one.
- **Best Integrated Human Practices** — depends entirely on tonight's rewrite.
- **Best Measurement** — would need `/measurement`, which 404s. Not realistic in
  three days.

A combination that needs no new wiki page beyond what is already planned:
**Best New Basic Part + Best Model + (Best Part Collection or Integrated Human
Practices)**.

## Wiki pages — live status

Re-checked by HTTP on 2026-10-19. Present with real content: `/`,
`/description`, `/engineering` (13.1 kB), `/human-practices` (6.5 kB, thinnest),
`/results`, `/model` (11.7 kB), `/parts` (16.9 kB, largest), `/notebook`,
`/team`, **`/contribution` (6.9 kB)** and **`/software` (6.4 kB)**.
**Still 404: `/measurement`, `/safety`.**

Neither of the remaining two is a medal standard URL. `/measurement` would only
be needed if Best Measurement were nominated. `/safety` appears in the wiki's own
navigation, so it is probably served under a different slug — worth checking, but
it costs nothing at judging.

## What is owed, in order

1. **Judging Form** — project title, abstract, medal declarations with standard
   URLs, three special-award nominations. Freezes 10/21.
2. **Decide the three special awards.** Everything about Gold follows from it.
4. **Human practices rewrite** — Silver criterion, in hand for tonight.
5. **Parts upload and the collection page** — in hand elsewhere.
6. **Presentation Video** — required, 2026-10-28, nothing started. One week after
   the freeze, which is easy to forget once the 21st passes.
7. **Judging Session** — required, 2026-11-15, 25 minutes with a 5-minute project
   overview.
8. *Optional:* `/software` plus an OSI-approved licence, if Best Software is to be
   nominated at all.

---

**Log**

- 2026-10-18 — compiled from the live deliverables and awards APIs plus HTTP
  checks of every standard URL on the team wiki.
