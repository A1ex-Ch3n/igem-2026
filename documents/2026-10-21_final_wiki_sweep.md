# Final pre-freeze sweep of the wiki — 2026-10-21, 02:00–03:00 PDT

Every non-judging page of <https://2026.igem.wiki/claremont-ca/>, checked against
the live site rather than against the repository, because the wiki source lives
only on gitlab.igem.org and there is no local clone.

Scanner: `$CLAUDE_JOB_DIR/tmp/scan/check_wiki.py` (not committed; it is a
throwaway). What it does is reproduced below so the check can be repeated.

## Result

| check | pages | outcome |
|---|---|---|
| HTTP status | 18 | all 200 |
| internal links | 49 distinct | all 200, no dead nav |
| images, srcset, CSS and video sources | 75 distinct | all 200 |
| figure numbering | 10 pages carry figures | sequential, no gaps, every number cited in the prose |
| DOIs | 42 distinct | all registered and resolving (checked against the handle registry, not by following the link — publishers return 403 to anything that is not a browser) |
| unrendered Jinja, TODO, TBD, UNDONE, placeholder text | 18 | none |
| iGEM's own HAR Check, all required pages | 6 | **PASSED**, no external assets |

The 18 pages: index, description, design, engineering, experiments, results,
proof-of-concept, model, software, parts, contribution, notebook, protocols,
human-practices, safety-and-security, team, attributions, achievements.

## Two things were wrong. Both are fixed and verified live.

### 1. The Harvey Mudd sponsor logo was broken on all 18 pages

`wiki/footer.html` pointed at
`sponsor-logo/hmc-logo-288.avif`, which has never existed in the team's upload
area. The bucket holds `hmc-logo-2400.avif` and `hmc-logo-gold.avif`. Every
request for the 288 file returned 403, so the footer rendered a broken image
beside the three sponsor logos that do load — on every page of the site.

Fixed to `hmc-logo-2400.avif`, the dark-panel lockup, which is Harvey Mudd's
version for light backgrounds and therefore the one `.footer-sponsors a`'s
`background: var(--paper)` calls for; this is what the comment at the top of
`footer.html` already specified. gitlab `935a6dd4`.

### 2. Figure 6 on `/model` disagreed with its own page

The panel A title read **"All 997 reconstructed nodes"**. `perp.csv` holds
**998** rows, Node1 through Node998, and the Model page says 998 in three
places — the method paragraph, the ZymCTRL paragraph and the software table —
as does the Attributions reference list. The figure was the one that was wrong:
`plot_perplexity.py` had the count written into the title string by hand.

The title is now computed from the loaded table, so it cannot drift again. The
redrawn figure went up as `models/fig-zymctrl-perplexity-998.avif` — a new
filename, because static.igem.wiki caches by name — and `wiki/pages/model.html`
points at it. gitlab `53112582`, local `eb26645`.

Regenerating also confirmed every number the Model page quotes from this figure:
median perplexity 8.61 under EC 3.2.1.4 and 9.03 under 3.2.1.123, against 14.1
to 17.5 for the other twenty-two classes; Node1 11.55 falling to Node281 6.81,
a drop of 4.74, which is the "~4.7 units" in the panel B title.

## Checked and found already correct

- **`/engineering`'s four numbers**, which were wrong when the hand-off document
  was written, have all been fixed by the other session: 144 ortholog groups
  (not 178), "43 are shared by all five" (not "only twelve"), "7,182 enumerated
  pairs, 6,358 of which returned a score", and "362 aa insert — 382 aa once
  pET-28a's leader is counted". The rung periods 15–18 and 22–24 and the pLDDT
  range 88–94 are gone; it now gives 93.2 against 64.7 and names panel C.
- **144 versus 45** is not a contradiction. 144 is the ortholog-group count
  across the five isolates' proteomes; 45 is the cluster count inside the three
  O-antigen cassettes, of which 4 are shared. Both are used consistently on
  every page that mentions them.
- **0.997 and 0.998** on `/model` are PhageRBPdetect confidences, not node
  counts.
- **`/protocols`'s 37 `<h2>`s** are Bootstrap modal dialog titles carrying
  `aria-labelledby`. That is correct markup; demoting them would break the
  accessibility wiring. No change.
- **`/safety`** is not a dead link. The page is `/safety-and-security` and the
  nav points there.
- Every page has a header image, the team logo and the four sponsor logos; no
  page is missing its banner.

## Not covered by this sweep

- Whether each figure is the *right* figure for its caption. Filenames and
  captions match on every page, but only a human who was at the bench can
  confirm the image is the experiment the caption describes.
- Content that only appears after a click — the protocol modals' bodies, which
  iGEM's HAR Check also excludes by its own statement.
- The Presentation Video, due 2026-10-28, which does not exist yet.

## Repeating the check

```python
# for each page: urlopen, then
#   re.findall(r'(?i)<img[^>]+src="([^"]+)"', html)      -> HEAD each, expect 200
#   re.findall(r'(?i)srcset="([^"]+)"', html)            -> first token of each entry
#   re.findall(r"url\((['\"]?)(https?://[^)'\"]+)\1\)", html)
#   re.findall(r'(?i)href="([^"#?][^"]*)"', html)        -> urljoin, keep same-origin, HEAD
#   re.findall(r'(?is)<figcaption[^>]*>(.*?)</figcaption>', html)
# DOIs: GET https://doi.org/api/handles/<doi> and require responseCode == 1.
# Do not judge a DOI by following it; publishers 403 a non-browser client.
```

---
*Log — 2026-10-21 03:00 PDT, five hours before the freeze. Written after the two
fixes above were deployed and re-verified on the live site. The HMC logo had
been broken since the footer was written; nothing in the repository would have
caught it, because the filename is a string and the file it names lives in
iGEM's upload area, not in the repository.*
