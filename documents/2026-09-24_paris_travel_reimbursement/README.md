# 2026 Grand Jamboree travel reimbursement

Reimbursement request to the CMC student affairs / travel grant office for
registration and travel costs that team members paid out of pocket.
English deliverable; a formatted `.docx` follows once the content is approved.

| File | What it is |
|:--|:--|
| `iGEM_Claremont_Paris_Reimbursement_Request.docx` | **What goes to the office.** Built from `request.md`, minus the log footers |
| `request.md` | The source of truth for the content, and the only place the provenance log lives |
| `build_docx.js` | Generator for the `.docx`. Provenance only — it rebuilds the file from scratch, so re-running it discards any hand edit made in Word |
| `receipts/` | The six receipts plus the team's cost spreadsheet. Both documents cite these filenames directly. **Not in git** — they carry passport numbers, booking references and payment details, and git history is permanent. They live on disk and are attached to the email separately |

**Editing after this point:** change `request.md` and re-run the generator
(`node build_docx.js <output.docx>`, with `npm install docx` somewhere on the path),
or edit the `.docx` in Word and stop using the generator. Doing both loses work.

**Requested: $11,298.02** in travel and competition fees, plus $160.46 of team
materials listed separately. Paid by Chun-Yu Chen ($8,705.02) and Yan Yan
($2,593.00). Five students travel 12–17 November.

## Still needed before this goes out

Nothing. The document is complete and internally consistent.

Note that `receipts/iGEM_2026_Grand_Jamboree.xlsx` still budgets for five travellers
and is now **superseded** by §6.3, which is recomputed for four. The spreadsheet is
kept as the receipt of record for what was paid, not as the current travel estimate.

## Loose ends, not blocking

Alex judged these low priority on 2026-09-24. The document is written so none of
them stops it being submitted.

- **The Jamboree pass in USD.** The iGEM invoice is euros only; $597.00 is the
  team's conversion. A footnote under §6.1 says so and offers the card statement on
  request, so the claim stands as written.
- **The second early-rate pass.** `receipts/iGEM_2026_Grand_Jamboree.xlsx` records
  two members buying at €525 in May; only one invoice is on file. That second pass is
  simply not claimed, so nothing in §6.1 depends on finding it.
- **Receipts for uniforms, mascot and stickers.** §6.1b marks them "Ledger entry;
  receipt to follow" and keeps them out of the travel subtotal, so the office can
  approve the travel claim without them.

## Open questions

- **This is not purely a reimbursement.** The receipts show three states: $11,458.48
  already paid, a hotel booking Agoda does not charge until 10 November, and
  estimates for the rest of the delegation. §6 splits these into 6.1, 6.2 and 6.3 and
  claims only 6.1. If the office also funds forward costs, 6.2 and 6.3 are already
  written to become a second ask.
- **Does the office have its own form?** If so, this document is the *attachment*
  supplying justification and itemisation. Send the form and §6 will be realigned.
- **Two payers, probably two claims.** Most offices require one claim per person.
  §6.1 carries a per-payer subtotal so it can be split without rewriting.
- **Prof. Espinoza is square.** He advanced the Stage I fee on 1 April; Alex repaid
  him in full by 12 April. §6.1 says so explicitly so the office does not pay him
  instead of Alex.
- **"iGEM Claremont" at a CMC office.** The delegation is CMC, Harvey Mudd and
  Scripps while the ask is to CMC. Same question flagged in
  `../2026-09-20_president_dudley_email_DRAFT.md`. §3 answers it implicitly, founded
  and led by CMC students, but expect it asked directly.
- **Alex's title.** This document says Co-Founder and Team Lead; the president email
  draft says "I founded and currently lead". Pick one and make them agree.

---

*Log: 2026-09-24 — Folder created after four framing answers: recipient = CMC student
affairs / travel grant office, language = English, nature = reimbursement of payments
already made, output = markdown first then a designed Word file.
`Proposal_General.pdf` supplied section order and tone only; its science is from the
retired* Xanthomonas *project and none of it was carried over. Same day: §4 gained a
milestone table; Lucy Shi added to the submission byline as Co-Founder; §5 and §6
filled from the receipts.*

*2026-09-24, later — the receipts folder was moved in from the repo root, where it
was untracked and named `reciepts : costs`, to `receipts/` here, and every citation
in `request.md` repointed. Three flagged items were downgraded from blockers to loose
ends at Alex's call, and §6's "Open items" list was replaced: the euro-only pass
became a footnote, the missing second pass and the missing merchandise receipts moved
here, and the airfare question was answered rather than left open. Alex explained the
11–21 November booking as delay buffer plus personal time, so §6 now states that the
fare is a single round-trip price independent of length of stay and that no lodging,
meals or ground costs are claimed for the personal days.*

*2026-09-25 — §5 roles and Lucy Shi's contact details filled in. Camille Dahlgren
then turned out not to be travelling, so the confirmed delegation dropped to four and
§1, §5 and §6.3 were recounted around it.*

*2026-09-25 — Word version built with `build_docx.js` (docx-js, US Letter, Arial,
iGEM green `#00A651` on headings, table header rows and the cover rule). It carries a
cover page, running header and page numbers from page two, and **omits the provenance
log footers**, which are internal. Validated with the docx skill's checker: 253
paragraphs, all checks passed, and every figure in the tables was confirmed present by
re-extracting the file with pandoc. **No visual proof exists** — LibreOffice is not
installed on this machine, so the file could not be rendered to PDF or images. Open it
in Word before sending.*

*2026-09-25 — §6.3 recomputed for four travellers instead of carrying an unassigned
fifth seat. Pass blend is now two early plus two late, so the per-student figure is
$2,582.79 and the delegation total is $10,331.16 excluding visas. §6.3 gained an
explicit warning that this total contains §6.1 and §6.2 rather than sitting beside
them. `build_docx.js` was patched to match and the `.docx` rebuilt: 257 paragraphs,
validation passed, and pandoc re-extraction confirms the new figures are present and
the superseded ones ($678.95, $2,596.45) are gone. The superseded figures survive only
in the provenance log at the end of `request.md`, which is deliberate and does not
appear in the Word file. Still no visual render — LibreOffice remains unavailable.*
