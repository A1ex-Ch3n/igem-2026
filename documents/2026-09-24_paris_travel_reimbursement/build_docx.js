const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, ExternalHyperlink,
  HeadingLevel, BorderStyle, WidthType, ShadingType, VerticalAlign,
  PageNumber, PageBreak,
} = require("docx");

const OUT = process.argv[2];

// ---- palette ---------------------------------------------------------------
const GREEN = "00A651";      // iGEM green, used for fills and accent text
const GREEN_DK = "007C3D";   // darker green for small text on white
const GREY_BG = "F2F2F2";
const GREY_LN = "D9D9D9";
const BLACK = "1A1A1A";

const CONTENT = 9360;        // US Letter, 1in margins

// ---- inline formatting -----------------------------------------------------
// Handles **bold**, *italic*, `code`; converts straight apostrophes to curly.
function runs(text, base = {}) {
  const out = [];
  const parts = String(text).split(/(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g);
  for (const part of parts) {
    if (!part) continue;
    let opts = Object.assign({}, base);
    let t = part;
    if (/^\*\*[^*]+\*\*$/.test(part)) { t = part.slice(2, -2); opts.bold = true; }
    else if (/^\*[^*]+\*$/.test(part)) { t = part.slice(1, -1); opts.italics = true; }
    else if (/^`[^`]+`$/.test(part)) { t = part.slice(1, -1); opts.font = "Consolas"; opts.size = (base.size || 22) - 2; }
    t = t.replace(/(\w)'(\w)/g, "$1’$2").replace(/'/g, "’");
    out.push(new TextRun(Object.assign({ text: t }, opts)));
  }
  return out.length ? out : [new TextRun(Object.assign({ text: "" }, base))];
}

const body = (text, opts = {}) => new Paragraph({
  children: runs(text, { size: opts.size || 22, color: opts.color || BLACK }),
  spacing: { after: opts.after === undefined ? 160 : opts.after, line: 276 },
  alignment: opts.align,
});

const bullet = (text) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  children: runs(text, { size: 22, color: BLACK }),
  spacing: { after: 100, line: 276 },
});

// Section heading: black, bold, with a green rule under it.
const h1 = (text) => new Paragraph({
  children: runs(text, { size: 30, bold: true, color: BLACK }),
  spacing: { before: 360, after: 180 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GREEN, space: 6 } },
});

const h2 = (text) => new Paragraph({
  children: runs(text, { size: 24, bold: true, color: GREEN_DK }),
  spacing: { before: 260, after: 120 },
});

// ---- tables ----------------------------------------------------------------
const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: GREY_LN };
const cellBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };
const CELL_MARGINS = { top: 70, bottom: 70, left: 110, right: 110 };

function cell(content, w, opts = {}) {
  const size = opts.size || 18;
  const paras = (Array.isArray(content) ? content : [content]).map((c) =>
    c instanceof Paragraph ? c : new Paragraph({
      children: runs(c, { size, bold: opts.bold, color: opts.color || BLACK }),
      alignment: opts.align,
      spacing: { after: 0, line: 240 },
    })
  );
  return new TableCell({
    borders: cellBorders,
    width: { size: w, type: WidthType.DXA },
    margins: CELL_MARGINS,
    verticalAlign: VerticalAlign.TOP,
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR } : undefined,
    columnSpan: opts.span,
    children: paras,
  });
}

// rows: array of arrays of strings/Paragraphs. opts.header => first row green.
function table(widths, rows, opts = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const trs = rows.map((cells, i) => {
    const isHead = opts.header && i === 0;
    const isLast = opts.totalRow && i === rows.length - 1;
    const zebra = !isHead && !isLast && opts.zebra && i % 2 === 0;
    return new TableRow({
      tableHeader: isHead,
      children: cells.map((c, j) => {
        // support {text, span, align, bold}
        const spec = (c && typeof c === "object" && !(c instanceof Paragraph) && "text" in c) ? c : { text: c };
        const w = widths[j] === undefined ? widths[widths.length - 1] : widths[j];
        return cell(spec.text, spec.span ? widths.slice(j, j + spec.span).reduce((a, b) => a + b, 0) : w, {
          fill: isHead ? GREEN : (isLast ? GREY_BG : (zebra ? "FAFAFA" : undefined)),
          color: isHead ? "FFFFFF" : BLACK,
          bold: isHead || isLast || spec.bold,
          align: spec.align || (opts.align && opts.align[j]),
          size: opts.size || 18,
          span: spec.span,
        });
      }),
    });
  });
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: trs,
  });
}

const R = AlignmentType.RIGHT;
const C = AlignmentType.CENTER;

// ---- cover -----------------------------------------------------------------
const cover = [
  new Paragraph({ spacing: { before: 2200, after: 0 }, children: [
    new TextRun({ text: "iGEM Claremont", size: 30, bold: true, color: GREEN }),
  ]}),
  new Paragraph({ spacing: { before: 200, after: 0 }, children: [
    new TextRun({ text: "2026 Grand Jamboree, Paris", size: 56, bold: true, color: BLACK }),
  ]}),
  new Paragraph({
    spacing: { before: 60, after: 400 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GREEN, space: 14 } },
    children: [new TextRun({ text: "Travel Reimbursement Request", size: 36, bold: true, color: GREEN })],
  }),
  table([2100, 7260], [
    ["Submitted by", "Chun-Yu (Alex) Chen, Co-Founder and Team Lead, iGEM Claremont · Lu (Lucy) Shi, Co-Founder, iGEM Claremont"],
    ["Faculty advisors", "Professor J. Cesar Ignacio-Espinoza (Principal Investigator, Keck Graduate Institute) · Professor Ran Libeskind-Hadas (Founding Chair, Kravis Department of Integrated Sciences, Claremont McKenna College)"],
    ["Event", "iGEM 2026 Grand Jamboree, 13–16 November 2026, Paris Convention Centre, Paris, France"],
    ["Date of request", "24 September 2026"],
  ], { size: 20 }),
  new Paragraph({ children: [new PageBreak()] }),
];

// ---- section 1 -------------------------------------------------------------
const s1 = [
  h1("1.  The Request"),
  body("iGEM Claremont is a student research team competing in the 2026 International Genetically Engineered Machine (iGEM) competition. Our results are judged at a single venue — the Grand Jamboree in Paris — and only teams present in person are eligible to be judged."),
  body("Several registration and travel costs fell due before any institutional funding was in place, and team members paid them personally so that the team would not lose its place in the competition. This document requests reimbursement of those out-of-pocket payments."),
  new Paragraph({ spacing: { after: 120 }, children: [] }),
  table([4200, 5160], [
    [{ text: "**Reimbursement requested — travel and competition fees**" }, { text: "**$11,298.02**" }],
    ["Team materials, listed separately in §6.1b", "$160.46"],
    [{ text: "**Combined**" }, { text: "**$11,458.48**" }],
    [{ text: "**Paid by**" }, "Chun-Yu Chen $8,705.02 · Yan Yan $2,593.00"],
    [{ text: "**Students travelling**" }, "4 of 10 team members"],
    [{ text: "**Event dates**" }, "13–16 November 2026"],
    [{ text: "**Location**" }, "Paris Convention Centre, Paris, France"],
    [{ text: "**Delegation travel window**" }, "12–17 November 2026; one booked itinerary runs 11–21 November"],
    [{ text: "**Receipts**" }, "Attached; itemised in §6"],
  ], { size: 20, zebra: true }),
  new Paragraph({ spacing: { after: 140 }, children: [] }),
  body("Every line claimed in §6.1 is supported by an attached receipt and is stated at the amount that actually posted to the payer’s card. Costs that are committed but not yet charged, and the estimated cost of the remaining delegation, are set out in §6.2 and §6.3 for planning purposes and are **not** claimed here."),
];

// ---- section 2 -------------------------------------------------------------
const s2 = [
  h1("2.  What iGEM Is, and Why Paris"),
  body("**iGEM is the largest synthetic biology competition in the world.** It was founded at MIT and is now run by the iGEM Foundation. Each year several hundred university teams spend a full year designing and building an original biological project, then present that work at the Grand Jamboree, where it is judged on its science, its engineering, and the responsibility with which it was carried out. It is one of the few venues where undergraduate research is held to a professional standard and evaluated by external judges."),
  body("An iGEM project is required to span three disciplines at once:"),
  bullet("**Wet lab** — the physical experimental work, from culturing organisms to engineering and testing biological parts."),
  bullet("**Dry lab** — the computational side: genome analysis, structural prediction, and modelling that direct what happens at the bench."),
  bullet("**Human practices** — the bridge to society, ensuring the project is safe, ethical, and addresses a real problem."),
  new Paragraph({ spacing: { after: 80 }, children: [] }),
  body("Teams are also required to work through the “Design, Build, Test, Learn” engineering cycle rather than pursuing a single result, and to publish their methods, parts, and data for other teams to reuse."),
  body("**The Grand Jamboree is not an optional conference.** It is the competition’s only judging session. Teams deliver their presentation and poster to judging panels in person over four days; medals, village awards, and special prizes are all decided there. A team that completes a year of research but does not attend receives no evaluation and no award. Attendance is therefore a condition of the work counting at all, which is why registration and travel are budgeted as part of the project rather than as a trip."),
  body("The competition charges fees in three stages, all payable to the iGEM Foundation in euros: a team registration fee, a team finalization fee, and a separate Jamboree ticket for each attending team member. The deadlines for these fall across the year and well before the November event, which is why the payments in §6 were already made."),
];

// ---- section 3 -------------------------------------------------------------
const s3 = [
  h1("3.  iGEM Claremont"),
  body("iGEM Claremont was founded by Claremont McKenna College students and is led by a CMC undergraduate. The team is ten students, registered for the 2026 season. Our experimental work is supervised by Professor J. Cesar Ignacio-Espinoza of Keck Graduate Institute, a specialist in virus–host interactions and viral genomics, and our computational work is advised by Professor Ran Libeskind-Hadas, Founding Chair of the Kravis Department of Integrated Sciences at CMC."),
  body("The team runs on student initiative. There is at present no standing budget line, no departmental home, and no institutional account from which competition fees can be paid — which is the direct reason those fees were paid personally and why this request exists."),
];

// ---- section 4 -------------------------------------------------------------
const doiCell = new Paragraph({
  spacing: { after: 0, line: 240 },
  children: [new ExternalHyperlink({
    link: "https://doi.org/10.1128/mra.00793-26",
    children: [new TextRun({ text: "doi.org/10.1128/mra.00793-26", size: 18, color: "0563C1", underline: {} })],
  })],
});

const s4 = [
  h1("4.  The 2026 Project"),
  h2("The problem"),
  body("Antibiotics kill bacteria indiscriminately, and resistance to them is rising. Bacteriophages — viruses that infect only bacteria and are harmless to humans — are one of the few routes to an antibacterial agent that destroys a single target strain and leaves the rest of a patient’s microbial community intact. The obstacle is specificity itself: each phage kills only a narrow set of strains, and determining which phage matches which bacterium is still done largely by trial and error."),
  body("Our project asks what decides that match, at the level of a single protein."),
  h2("What we did"),
  body("We collected topsoil from ten sites at the California Botanic Garden in Claremont, isolated *Pseudomonas* bacteria from those samples, and isolated a bacteriophage capable of killing one of the strains we had recovered. We then sequenced both sides of that pairing — the bacterial hosts and the phage — and analysed the phage protein that makes first contact with the bacterial surface."),
  h2("Milestones reached this season"),
  body("None of the following existed in May. Each one is verifiable by a third party today, at the identifier given in the last column."),
  table([460, 4200, 1100, 3600], [
    ["", "Milestone", { text: "Reached", align: C }, "Verifiable at"],
    [{ text: "**1**", align: C }, "**Peer-reviewed publication** in *Microbiology Resource Announcements*, a journal of the American Society for Microbiology, with a CMC undergraduate as first author", { text: "4 Sep 2026", align: C }, doiCell],
    [{ text: "**2**", align: C }, "**Three complete bacterial genomes** deposited in the public sequence archives", { text: "Aug 2026", align: C }, "GCA_059295255.1  ·  GCA_059295275.1  ·  GCA_059295235.1 (BioProject PRJNA1482863)"],
    [{ text: "**3**", align: C }, "**Complete genome of a bacteriophage that matches nothing in the public databases** — 62,338 bp, 80 genes", { text: "Jul 2026", align: C }, "Assembly and annotation held by the team; deposition in progress"],
    [{ text: "**4**", align: C }, "**Safety screen clear** — zero virulence genes, zero antibiotic-resistance genes", { text: "Jul 2026", align: C }, "Screened against the VFDB and CARD reference databases"],
    [{ text: "**5**", align: C }, "**Six engineered protein constructs** designed, ordered, and now in expression testing at the bench", { text: "Sep 2026", align: C }, "Commercial synthesis orders, Jul and Sep 2026"],
  ], { header: true, zebra: true }),
  new Paragraph({ spacing: { after: 160 }, children: [] }),
  body("Milestones 1 and 2 are the ones an outside reader can check in a browser in under a minute: a published paper in an American Society for Microbiology journal, written by undergraduates, and three genome assemblies that anyone in the world can now download."),
  h2("What those milestones mean"),
  body("**The publication.** *Microbiology Resource Announcements* is a peer-reviewed ASM journal. Publishing there means the three bacterial genomes we sequenced have been checked by external reviewers and released as a permanent public resource. The first author is a CMC undergraduate."),
  body("**The phage genome.** Searching those 80 genes against the public databases returns no match to anything previously described. The most likely reading is that the team has recovered and sequenced a bacteriophage that no one has characterised before, found in soil a few miles from campus."),
  body("**The safety screen.** Before a phage project may proceed, iGEM requires evidence that the organism carries no genes that would make it dangerous to work with or to release. Screening our genome against the standard virulence-factor and antibiotic-resistance reference databases returned nothing on either. That result is what permits the rest of the project."),
  body("**A change of direction that came from the computational work.** The team had spent weeks assuming the phage recognises a *protein* on the bacterial surface and had built a computational screen to find which one. When the three-dimensional structure of the phage’s tail spike was predicted, it was not the compact shape of a protein-binding protein but a long right-handed helix — the geometry of an enzyme that cuts sugar chains. The phage does not grip a protein handle; it digests the bacterium’s sugar coat. That result retired the original screen and redefined the target of the whole project. We also demonstrated, using known-interacting control pairs, *why* the abandoned screen could not have worked — a negative result worth reporting to other teams."),
  body("**Six engineered protein constructs, now in expression testing.** Guided by that structure, six protein constructs were designed and ordered from a commercial DNA synthesis company. They are at the bench now, being tested for expression, so that the sugar-cutting prediction can be checked experimentally."),
  h2("What is still open"),
  body("The prediction that differences in the bacterial sugar coat explain which strains this phage can and cannot kill remains a prediction: the assay has been run, but the readout is not yet in our hands. The protein constructs are in expression testing and have not yet been confirmed as expressed. A second phage remains to be sequenced. These are the questions the team carries into the Jamboree."),
];

// ---- section 5 -------------------------------------------------------------
const s5 = [
  h1("5.  The Paris Delegation"),
  body("Four members of the team will travel to Paris. Three of the four are co-authors of the published *Microbiology Resource Announcements* paper described in §4, and three have competed at an iGEM Grand Jamboree before — each of them returning with a Gold Medal."),
  table([1500, 1300, 3400, 3160], [
    ["Name", "College", "Role in the 2026 project", "Previous iGEM record"],
    ["**Chun-Yu (Alex) Chen**", "Claremont McKenna College", "Co-founder and team lead; computational lead. First author of the MRA paper. Assembled and annotated the phage genome and produced the tail-spike structure prediction that redirected the project", "2023 Taipei-KCISLK-V1 — Gold Medal; nominated Best Presentation, Best Wiki · 2025 Taipei-KCISLK-V3 — Gold Medal; nominated Best Presentation, Best Wiki"],
    ["**Yan (Olivia) Yan**", "Harvey Mudd College", "Co-author of the MRA paper. Worked at the bench through the summer", "2024 TestDaily-I-Beijing — Gold Medal · 2025 UPrize-I — Gold Medal; 1st Runner-Up; Best Village Project; Safety and Security Award; iGEMers Prize; nominated Best Measurement, Best Presentation, Best Wiki, Best Integrated Human Practices"],
    ["**Xiaokuan (Carol) Wang**", "Harvey Mudd College", "Co-author of the MRA paper. Worked at the bench through the summer, and is currently researching bacteria–bacteriophage relationships in the Espinoza Lab at Keck Graduate Institute", "First Jamboree. Prior research: Champer Lab, Peking University (gene-drive project, PCR and gel electrophoresis); lake-eutrophication modelling with a dissolved-oxygen control device; HMC Molecular Biology Lab (engineered the aeBlue gene into *E. coli*)"],
    ["**Yuhui (Sarah) Liu**", "Harvey Mudd College", "Shaped the experimental design in the project’s early phase and has advised the team throughout the season", "2022 BNDS-China — Gold Medal"],
  ], { header: true, zebra: true }),
  new Paragraph({ spacing: { after: 160 }, children: [] }),
  body("Two further members contributed to the work but are not travelling. **Camille Dahlgren** (Scripps College) helped design the experiments in the project’s early phase, and competed in 2024 with IEA, taking a Silver Medal and Best Model with a nomination for Best Integrated Human Practices. **Lu (Lucy) Shi**, co-founder of iGEM Claremont, is a signatory to this request."),
  body("The four travellers share two twin rooms, which is how the accommodation figure in §6.3 is costed."),
];

// ---- section 6 -------------------------------------------------------------
const s6 = [
  h1("6.  Expenses"),
  body("This section separates what has already left students’ bank accounts from what has been committed but not yet charged, and from what is still an estimate. Only §6.1 is the subject of this reimbursement request."),
  body("**Currency.** Fees payable to the iGEM Foundation are invoiced in euros. The dollar figures below are the amounts that actually posted to the payer’s card, not a computed conversion, so they are the amounts to reimburse."),

  h2("6.1  Paid out of pocket — reimbursement requested"),
  table([380, 2750, 940, 1650, 820, 1060, 1760], [
    [{ text: "#", align: C }, "Item", { text: "Date paid", align: C }, "Paid by", { text: "Invoiced", align: C }, { text: "Amount (USD)", align: R }, "Receipt"],
    [{ text: "1", align: C }, "iGEM Program Fee — Stage I (Registration), invoice #1OLSWB8M", { text: "2026-04-01", align: C }, "Chun-Yu Chen", { text: "€5,450", align: C }, { text: "**6,337.00**", align: R }, "stage1_registration.pdf"],
    [{ text: "2", align: C }, "iGEM Program Fee — Stage II (Finalization), invoice #ERF3ML2B", { text: "2026-04-23", align: C }, "Yan Yan $2,500.00 Chun-Yu Chen $704.29", { text: "€2,750", align: C }, { text: "**3,204.29**", align: R }, "stage2_registration.pdf"],
    [{ text: "3", align: C }, "Grand Jamboree Universal Pass, early rate, invoice #X8PGCX5S", { text: "2026-05-01", align: C }, "Chun-Yu Chen", { text: "€525", align: C }, { text: "**597.00** *", align: R }, "jamboree_ticket.pdf"],
    [{ text: "4", align: C }, "French visa appointment service fees, TLScontact receipt visa-fr-usLAX2fr-0008361601", { text: "2026-09-11", align: C }, "Yan Yan", { text: "USD", align: C }, { text: "**93.00**", align: R }, "visa_for_chinese_students.pdf"],
    [{ text: "5", align: C }, "Airfare LAX–CDG round trip, Chase Travel trip 1029560276, 1 traveller", { text: "2026-09-18", align: C }, "Chun-Yu Chen", { text: "USD", align: C }, { text: "**1,066.73**", align: R }, "flight.pdf"],
    ["", { text: "Travel subtotal", span: 4, align: R }, "", "", "", { text: "**11,298.02**", align: R }, ""],
  ], { header: true, totalRow: true, zebra: true }),
  new Paragraph({ spacing: { before: 120, after: 140 }, children: runs("* Row 3 is the only line the iGEM Foundation invoiced in euros without a dollar figure. The amount shown is €525 converted at the rate on the date of payment; the card statement line can be supplied on request.", { size: 18, color: "595959" }) }),
  body("**By payer.** Chun-Yu Chen **$8,705.02** · Yan Yan **$2,593.00**."),
  body("Note on row 1: Professor Ignacio-Espinoza advanced the Stage I payment on the day it fell due, and Chun-Yu Chen repaid him in full in eight transfers between 1 and 12 April 2026. Reimbursement for this line is therefore owed to Chen, not to the Professor, who is square."),

  h2("6.1b  Project costs that are not travel"),
  body("Listed separately so they can be considered or struck on their own merits."),
  table([380, 2500, 1100, 1500, 1320, 2560], [
    [{ text: "#", align: C }, "Item", { text: "Date paid", align: C }, "Paid by", { text: "Amount (USD)", align: R }, "Receipt"],
    [{ text: "6", align: C }, "Team uniforms", { text: "2026-08-18", align: C }, "Yan Yan", { text: "**85.54**", align: R }, "Ledger entry; receipt to follow"],
    [{ text: "7", align: C }, "Team mascot", { text: "2026-08-19", align: C }, "Yan Yan", { text: "**7.87**", align: R }, "Ledger entry; receipt to follow"],
    [{ text: "8", align: C }, "Stickers", { text: "2026-08-19", align: C }, "Yan Yan", { text: "**67.05**", align: R }, "Ledger entry; receipt to follow"],
    ["", { text: "Subtotal", span: 3, align: R }, "", "", { text: "**160.46**", align: R }, ""],
  ], { header: true, totalRow: true, zebra: true }),
  new Paragraph({ spacing: { before: 160, after: 160 }, children: runs("Combined total, §6.1 and §6.1b: $11,458.48.", { size: 22, bold: true, color: BLACK }) }),

  h2("6.2  Committed, not yet charged"),
  table([4200, 1100, 1200, 1200, 1660], [
    ["Item", { text: "Charges on", align: C }, "Paid by", { text: "Amount (USD)", align: R }, "Receipt"],
    ["Accommodation — Motel One Paris – Porte de Versailles, Agoda booking 1048778414. One Queen room, five nights, 12–17 November 2026, sleeps two", { text: "2026-11-10", align: C }, "Yan Yan", { text: "785.31", align: R }, "hotel_for2.pdf"],
  ], { header: true }),
  new Paragraph({ spacing: { before: 140, after: 160 }, children: runs("A further city tax of approximately $64.20 is payable at the property on departure and is not included in the figure above.", { size: 22, color: BLACK }) }),

  h2("6.3  Estimated cost of the trip, full delegation"),
  body("The team’s planning figures for the four travellers named in §5, over 12–17 November. These are estimates, not claims."),
  table([2600, 1400, 5360], [
    ["Item", { text: "Per student (USD)", align: R }, "Basis"],
    ["Airfare", { text: "1,100.00", align: R }, "LAX–CDG round trip"],
    ["Accommodation", { text: "367.50", align: R }, "$147 per night, two sharing a room, five nights"],
    ["Grand Jamboree pass", { text: "665.29", align: R }, "Blended: two passes already bought at the early rate of €525 (~$597), two still to buy at the current late rate of €645 (~$733.58)"],
    ["Meals", { text: "450.00", align: R }, "Midpoint of $65–85 per day over six days"],
    ["**Subtotal per student**", { text: "**2,582.79**", align: R }, ""],
    ["**Delegation of four**", { text: "**10,331.16**", align: R }, "Excluding visa fees"],
    ["French visa service fees", { text: "93.00", align: R }, "Per traveller, Chinese passport holders only"],
  ], { header: true, zebra: true }),
  new Paragraph({ spacing: { before: 160, after: 160 }, children: runs("**This total is not additional to §6.1 and §6.2 — it contains them.** The delegation figure covers all four travellers’ airfare, rooms, passes and meals for the trip, including the airfare already paid, the room already booked, and the passes already bought. Anything already settled must be subtracted from it, never added to it.", { size: 22, color: BLACK }) }),
  body("Two notes on the estimate. The nightly hotel rate is quoted as of 24 September 2026 and is subject to change. Passes bought from now on are charged at the late rate, which is €120 (~$137) per person more than the early rate two members secured in May."),

  h2("Note on the booked itinerary"),
  body("The airfare in row 5 covers 11–21 November, which is wider than both the Jamboree itself, 13–16 November, and the booked accommodation, 12–17 November. The extra days are a deliberate buffer against transatlantic delay on the way in, and personal time in Paris at the end."),
  body("That itinerary is a single round-trip fare. The price is set by the route and the booking date, not by the length of stay, and a narrower itinerary would not have been cheaper. **No accommodation, meals, or ground costs are claimed for the personal days**, and the only hotel in this document, §6.2, ends on 17 November."),
];

// ---- appendix --------------------------------------------------------------
const appendix = [
  h1("Appendix A.  Contacts"),
  table([5600, 3760], [
    ["**Chun-Yu (Alex) Chen** — Co-Founder and Team Lead, iGEM Claremont", "cchen29@cmc.edu"],
    ["**Lu (Lucy) Shi** — Co-Founder, iGEM Claremont", "lshi29@students.claremontmckenna.edu"],
    ["**Prof. J. Cesar Ignacio-Espinoza** — Principal Investigator, Keck Graduate Institute", "cesar_espinoza@kgi.edu"],
    ["**Prof. Ran Libeskind-Hadas** — Faculty Advisor, Kravis Department of Integrated Sciences, CMC", "ran.libeskind-hadas@claremontmckenna.edu"],
  ], { size: 20, zebra: true }),
];

// ---- document --------------------------------------------------------------
const doc = new Document({
  styles: { default: { document: { run: { font: "Arial", size: 22, color: BLACK } } } },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 460, hanging: 260 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1260, left: 1440 },
      },
      titlePage: true,
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 120 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GREEN, space: 4 } },
        children: [new TextRun({ text: "iGEM Claremont · 2026 Grand Jamboree Travel Reimbursement", size: 16, color: "808080" })],
      })] }),
      first: new Header({ children: [new Paragraph({ children: [] })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "808080" })],
      })] }),
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
    },
    children: [...cover, ...s1, ...s2, ...s3, ...s4, ...s5, ...s6, ...appendix],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log("wrote", OUT, buf.length, "bytes");
});
