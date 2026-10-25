"""Assemble the Phagenomics deck.

    python code/1025_presentation_deck/build_deck.py

Writes documents/2026-10-25_presentation_deck.pptx. Every slide carries its
narration in the speaker notes, so it can be recorded straight from the deck.
"""
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

from deck_base import (CONTENT_W, CREAM, DIM, DISPLAY, H, INK, LIGHT, MARGIN,
                       MUTED, OUT, PALE, PALE_RUST, PAPER, RULE, RUST, ROOT,
                       TEAL, W, WHITE, Deck, cards, figure, frame, panel,
                       picture, prose, run, statement, text, notes, eyebrow,
                       FRAMES, FIGS)

N = {}   # narration, keyed by slide


def cover(d):
    s = d.new(bg=INK, number=False)
    text(s, "iGEM CLAREMONT-CA · 2026", MARGIN, Inches(1.45), CONTENT_W,
         Inches(0.3), size=13, color=LIGHT, bold=True)
    text(s, "Phagenomics", MARGIN, Inches(2.0), CONTENT_W, Inches(1.8), size=68,
         color=CREAM, font=DISPLAY, spacing=1.0)
    text(s, "What decides which bacteria a phage can kill —\nand what happened the "
            "four times we asked.", MARGIN, Inches(3.75), Inches(9), Inches(1.6),
         size=23, color=DIM, spacing=1.32)
    text(s, "Bacteriophage Φ8  ·  Pseudomonas  ·  California Botanic Garden soil",
         MARGIN, Inches(6.35), CONTENT_W, Inches(0.4), size=13, color=LIGHT)
    notes(s, "We're iGEM Claremont-CA, a first-year team in California, and this is "
             "Phagenomics.\n\nWe work on one question: what decides which bacteria a "
             "phage can kill?")


def act_one(d):
    prose(d, "The gap we work in",
          "Phage therapy's bottleneck is host range — and nobody can design it",
          "Pseudomonas causes serious infections in immunocompromised patients and "
          "persistent crop disease in agriculture, and phage therapy is one of the "
          "alternatives people are betting on.\n\nEach phage binds a specific receptor "
          "on a specific strain, and nobody can design that specificity yet, because "
          "we don't understand how a phage recognises its target in the first place.\n\n"
          "So we didn't try to build a therapeutic. We tried to understand the "
          "recognition step any therapeutic would depend on.",
          note="Pseudomonas causes serious infections in immunocompromised patients "
               "and persistent crop disease in agriculture, and phage therapy is one "
               "of the alternatives to antibiotics people are betting on. Its "
               "bottleneck is host range. Each phage binds a specific receptor on a "
               "specific strain, and nobody can design that specificity yet, because "
               "we don't understand how a phage recognises its target in the first "
               "place.\n\nSo we didn't try to build a therapeutic. We tried to "
               "understand the recognition step that any therapeutic would depend on. "
               "We went at it four times this season. Three of those four failed, and "
               "the failures are the useful part.")

    run(d, "adsorption",
        ["01-surface", "02-arrive", "03-contact", "04-cut", "05-reach", "06-inject"],
        "How a phage gets in",
        note="It gets decided at the very first step, before any DNA moves: the phage "
             "has to recognise the outside of the cell and stick to it.\n\nAnd many "
             "bacteria don't present a bare protein surface. They wrap themselves in "
             "sugar — long chains called the O-antigen, and above those, in some "
             "species, a capsule. So the first thing a phage touches is a forest of "
             "sugar.\n\nThe tail spike is a depolymerase. It digests the sugar in "
             "front of it, opens a channel, reaches the membrane and injects.")
    frame(d, "adsorption", "07-other-strain", "A different strain", accent=RUST,
          note="Change the sugar, and the same phage never gets through. That is host "
               "range, and it is decided before infection even begins.")

    statement(d, "so", "Host range is decided at the sugar,\nbefore infection begins.",
              "Everything after the channel is ordinary infection. Everything before "
              "it is the question we worked on.",
              note="Everything after this point is ordinary infection. Everything "
                   "before it is host range.")

    prose(d, "Where the project came from",
          "An idea we dropped, and the abstraction we kept",
          "Early on we talked to Professor Ran Libeskind-Hadas at Claremont McKenna, "
          "one of our advisors. He suggested we reconstruct an ancestral phage — a "
          "whole organism, inferred from its relatives.\n\nWe couldn't build one. But "
          "scale that down to a single enzyme and you can order it from a synthesis "
          "company.\n\nThat is what this project became.",
          note="One thing belongs at the start, because it's why half of this project "
               "exists.\n\nEarly on we talked to Professor Ran Libeskind-Hadas at "
               "Claremont McKenna, one of our advisors. He suggested we reconstruct an "
               "ancestral phage — a whole organism, inferred from its relatives. We "
               "couldn't build one. But we realised that if we scaled the idea down "
               "from an organism to a single enzyme, we could order it from a "
               "synthesis company. That is what this project became.")

    s = d.new()
    eyebrow(s, "California Botanic Garden · 19 May 2026")
    text(s, "Five isolates, three strains, two built-in controls", MARGIN,
         Inches(0.98), CONTENT_W, Inches(0.9), size=29, color=INK, font=DISPLAY)
    rows = [("Strain 1", "8-5-2 · 10-10-2", "99.997 % ANI", WHITE),
            ("Strain 2", "9-2-1 · 9-6-2", "100.000 % ANI — the Φ8 host", PALE),
            ("Strain 3", "8-10-2", "a different species", WHITE)]
    y = Inches(2.3)
    for a, b, c, fill in rows:
        panel(s, MARGIN, y, Inches(6.3), Inches(0.72), fill=fill, line=RULE,
              radius=0.02)
        for txt, dx, w_, col in ((a, 0.26, 1.5, INK), (b, 1.9, 2.1, MUTED),
                                 (c, 4.1, 2.1, MUTED)):
            text(s, txt, MARGIN + Inches(dx), y + Inches(0.22), Inches(w_),
                 Inches(0.5), size=15, color=col, bold=(col == INK))
        y += Inches(0.8)
    text(s, "Any difference we report between strains has to be bigger than the "
            "difference we can measure within one.", MARGIN, y + Inches(0.3),
         Inches(6.3), Inches(1.2), size=17, color=MUTED, spacing=1.35)
    picture(s, FIGS / "bactgenomes.png", MARGIN + Inches(6.9), Inches(2.1),
            Inches(4.9), Inches(3.9))
    text(s, "Genomes published in Microbiology Resource Announcements · "
            "doi 10.1128/mra.00793-26", MARGIN, H - Inches(0.6),
         CONTENT_W - Inches(0.9), Inches(0.4), size=12, color=MUTED)
    notes(s, "We collected soil from the California Botanic Garden on the nineteenth "
             "of May. From it we isolated five Pseudomonas strains, and we sequenced "
             "all five genomes — every one of them closed into a complete circle.\n\n"
             "Those five collapse into three distinct strains. That leaves us with two "
             "pairs of near-identical isolates, and we use those pairs as an internal "
             "control all the way through.")

    figure(d, "The phage", "One phage, Φ8, that infects exactly one of the three",
           "phagemap",
           "62,339 bp · circular · 80 coding sequences · no match in the phage "
           "database · effectively no genes in common with T7",
           note="We also isolated a phage, which we call Phi-8, and it infects exactly "
                "one of the three strains. Sixty-two thousand, three hundred and "
                "thirty-nine base pairs, circular, eighty genes. No match anywhere in "
                "the phage database, and essentially no genes in common with T7. The "
                "architecture is familiar. The sequence isn't.")

    run(d, "cassette", ["01-slot", "02-strain", "03-strain", "04-strain", "05-verdict"],
        "The first clue",
        note="Then we went looking at the locus that builds the sugar coat. We "
             "anchored on the gene that flanks it in Pseudomonas, pulled the cassette "
             "out of all three strains, and clustered every protein in it.\n\nWe found "
             "the cassette sitting in the same slot in all three. The contents are "
             "unrelated: twenty-three genes in one strain, fifteen in another, "
             "twenty-five in the third, and of forty-five gene clusters only four are "
             "shared by every strain — all four generic sugar chemistry.")

    figure(d, "The first clue", "The real cassettes, side by side", "oantigen",
           "Located with ihfB as the upstream anchor; cassette proteins clustered with "
           "MMseqs2 at ≥ 30 % identity, ≥ 50 % coverage",
           note="The near-identical pairs inside each strain match at a hundred "
                "percent across every cassette gene. Within a strain, zero variation. "
                "Between strains, almost total.\n\nWe also found that no database "
                "could have told us any of this. There is no serotype scheme for this "
                "group of species at all.")

    statement(d, "first hypothesis",
              "Three strains, three different sugar coats,\none phage that kills one "
              "of them.",
              "So the sugar coat might be one of the main things setting what Φ8 can "
              "attack.",
              note="So: three strains, three different sugar coats, one phage that "
                   "kills one of them. That gave us our first hypothesis — that the "
                   "sugar coat might be one of the main things setting what Phi-8 can "
                   "attack.")


def cycle_one(d):
    frame(d, "wheel", "01-cycle", "Cycle 1 of four", morph=False,
          note="Cycle one — the wrong question. A full design, build, test and learn "
               "loop, retired by its own controls.")

    prose(d, "Cycle 1 · Design", "We designed it around the wrong assumption",
          "The textbook picture of attachment is a receptor-binding protein on the "
          "phage tail meeting a protein on the bacterial surface. Lock and key.\n\n"
          "If you assume that, the obvious move is to work out which binding protein "
          "fits which receptor. So that is what we set out to predict.\n\nIf we had "
          "known the receptor was a sugar, we would never have run this.",
          figkey="virion",
          note="We designed the first cycle around the wrong assumption, and it's "
               "worth saying why it was the reasonable one.\n\nThe textbook picture of "
               "attachment is a receptor-binding protein on the phage tail meeting a "
               "protein on the bacterial surface. Lock and key. If you assume that, "
               "the obvious move is to work out which binding protein fits which "
               "receptor — so that is what we set out to predict.\n\nIf we had known "
               "the receptor was a sugar, we would never have run this. We thought it "
               "was a protein, so we went looking for a protein.")

    run(d, "screen", ["01-matrix", "02-scored", "03-controls-in", "04-no-separation",
                      "05-retired"],
        "Cycle 1 · Build and test",
        note="What we built was a screen. Four hundred and forty-one candidate "
             "receptors across all five isolates, collapsed into a hundred and "
             "forty-four clusters, then a hundred and fourteen binding proteins "
             "against sixty-three receptors — seven thousand, one hundred and "
             "eighty-two pairs, each folded as a complex and ranked by the interface "
             "score.\n\nAnd the ranking looked perfectly reasonable. That's the "
             "trouble with this kind of output. It always looks reasonable.\n\nSo "
             "before we built anything on it, we ran nine control folds. T5's pb-five "
             "with FhuA scored zero point one three seven. The same receptor, "
             "scrambled, scored zero point one three six. None of our real binders "
             "separated from the controls.")

    figure(d, "Cycle 1 · Test", "The controls, in both tools", "controls",
           "Under AlphaFold2 with real alignments the mismatched pair outscores every "
           "genuine binder. Scores tracked protein length at r = +0.60.",
           accent=RUST,
           note="We also plotted score against protein length, and found a correlation "
                "of plus nought point six. The screen was ranking proteins by size.\n\n"
                "We assumed the tool was at fault, so we rebuilt the whole thing with "
                "real evolutionary alignments. It got worse. Under that one, the "
                "mismatched pair outscored the genuine binders.")

    run(d, "interface", ["01-question", "02-species", "03-covary", "04-fingerprint",
                         "05-separate", "06-never-written"],
        "Cycle 1 · Learn — why it cannot work", accent=RUST,
        note="What we learned is that the method cannot answer this question at all — "
             "and we can say exactly why.\n\nThese models don't simulate two proteins "
             "touching. They read evolution. They look across thousands of species for "
             "positions that change in step: if a residue on one side mutates, and a "
             "residue on the other mutates to match, those two are probably in "
             "contact.\n\nAnd that signal only exists where two proteins have a shared "
             "history of co-adaptation. A phage protein and a bacterial protein have "
             "never co-adapted as a pair, so there is no history to read, and the "
             "interface score returns noise.")

    statement(d, "cycle 1 · learn",
              "This was never a result about our proteins.\nIt is a property of the "
              "method.",
              "Nine control folds decided the fate of seven thousand. We never ran the "
              "real screen.", bg=RUST,
              note="So this was never a result about our proteins. It's a property of "
                   "the method, and more compute doesn't fix it. Nine control folds "
                   "decided the fate of seven thousand, and we never ran the real "
                   "screen.")


def cycle_two(d):
    frame(d, "wheel", "02-cycle", "Cycle 2 of four", morph=False,
          note="Cycle two — ask the protein what it is. Geometry instead of docking.")

    run(d, "rung", ["01-prism", "02-bonds", "03-histogram", "04-three-folds"],
        "Cycle 2 · A fold test with no database",
        note="For the second cycle we changed the question. If we couldn't ask what "
             "the tail spike binds, we could ask what it is.\n\nA right-handed "
             "beta-helix is a chain coiled into a long prism, with its coils "
             "hydrogen-bonded in register. So if you take every backbone hydrogen "
             "bond, measure how far apart in sequence its two partners sit, and "
             "histogram those offsets, a beta-helix peaks at its coil period, "
             "somewhere between sixteen and twenty-six residues. An alpha-helix peaks "
             "at four. A beta-sandwich has no peak at all.\n\nWe chose that test "
             "rather than fell back on it. On a genome with no close relatives, a "
             "database can't contain the answer.")

    figure(d, "Cycle 2 · Test",
           "Eight predicted structures, seven proteins — five of them turned down",
           "folds",
           "CDS 11, the tail spike: classifier confidence 0.997, coil period 16–17. "
           "CDS 24, filed as “hypothetical”: 0.998 on a different period — a second "
           "depolymerase homology annotation had missed.",
           note="What we tested was eight predicted structures covering seven "
                "proteins, and we classified each from its own backbone geometry.\n\n"
                "Five of the seven came back negative, and the numbers they returned "
                "aren't noise: an alpha-helical fibre lands at six. The method says "
                "no, which is what makes it worth believing when it says yes.\n\nIt "
                "said yes twice.")

    for i, (key, label_, blurb) in enumerate((
            ("trimer", "The tail spike, whole",
             "CDS 11 is 941 residues, and it hangs off the virion base."),
            ("body-side", "Most of it isn't the enzyme",
             "The first 110 residues anchor it. The next 200 are a shaft that moves "
             "between every model we ran."),
            ("body-axial", "The rigid trimeric body",
             "From residue 300 to the end, agreeing between models to within one "
             "ångström. Submitted as BBa_26DKNAEC, residues 305–941."))):
        s = d.new(morph=(i > 0))
        eyebrow(s, "Cycle 2 · The same protein, three ways")
        picture(s, FIGS / f"{key}.png", MARGIN, Inches(1.0), Inches(6.2),
                Inches(5.9), name="!!spine")
        text(s, label_, MARGIN + Inches(7.0), Inches(2.5), Inches(5.2), Inches(1.1),
             size=28, color=INK, font=DISPLAY, spacing=1.15)
        text(s, blurb, MARGIN + Inches(7.0), Inches(3.7), Inches(5.0), Inches(2.0),
             size=18, color=MUTED, spacing=1.4)
        if i == 0:
            notes(s, "CDS 11 is nine hundred and forty-one residues and most of it "
                     "isn't the enzyme. The first hundred and ten anchor it to the "
                     "virion, and the next two hundred are a shaft that moves between "
                     "every model we ran. The rigid trimeric body — from residue three "
                     "hundred to the end — is the part that carries the chemistry. "
                     "That's the fragment we expressed, and the one we submitted to "
                     "the Registry.")

    statement(d, "cycle 2 · learn",
              "The tail spike isn't a key.\nIt's a blade.",
              "Enzymes that chew through long sugar chains look like this. You can "
              "recognise a wood plane by its shape without being told what it cuts — "
              "and the lock we had spent months looking for doesn't exist.",
              note="That shape is a signature. Enzymes that chew through long sugar "
                   "chains look like this, because a sugar chain is a thread and you "
                   "need something that holds it straight while you cut. You can "
                   "recognise a wood plane by its shape without being told what it "
                   "cuts.\n\nSo the tail spike isn't a key. It's a blade — and the "
                   "lock we had spent months looking for doesn't exist.\n\nWe weren't "
                   "the only ones reading it that way. Our classifier flagged it, and "
                   "our PI reached the same conclusion from his own structural search. "
                   "Between us, we turned it into a hypothesis.")

    statement(d, "the central hypothesis",
              "In bacteria that wrap themselves in sugar, the ceiling\non host range "
              "is set by what the depolymerase can digest —\nnot by which protein the "
              "tail binds.",
              "And the narrow specificity we see today is a narrowed-down version of "
              "something broader further back.    ·    Developed jointly with "
              "Prof. J. Cesar Ignacio Espinoza", size=30,
              note="In bacteria that wrap themselves in sugar, the ceiling on host "
                   "range is set by what the depolymerase can digest — not by which "
                   "protein the tail binds. And the narrow specificity we see today is "
                   "a narrowed-down version of something broader further back.")

    s = d.new()
    eyebrow(s, "A prediction we can falsify")
    text(s, "If the tail spike reads Strain 2's sugar, Φ8 should fail on the other two",
         MARGIN, Inches(0.98), CONTENT_W, Inches(0.9), size=27, color=INK, font=DISPLAY)
    rows = [("9-2-1 · 9-6-2", "Strain 2", "hosts of record", PALE),
            ("10-10-2", "Strain 1", "no plaques", WHITE),
            ("8-10-2", "Strain 3", "no plaques", WHITE)]
    y = Inches(2.3)
    for a, b, c, fill in rows:
        panel(s, MARGIN, y, Inches(6.6), Inches(0.7), fill=fill, line=RULE, radius=0.02)
        for txt, dx, w_, col in ((a, 0.26, 2.0, INK), (b, 2.4, 1.6, MUTED),
                                 (c, 4.3, 2.1, MUTED)):
            text(s, txt, MARGIN + Inches(dx), y + Inches(0.21), Inches(w_),
                 Inches(0.5), size=15, color=col, bold=(col == INK))
        y += Inches(0.78)
    text(s, "Eighteen host isolates spotted against two pooled lysates, July 2026.\n"
            "That is the direction the prediction makes.", MARGIN, y + Inches(0.3),
         Inches(6.6), Inches(1.0), size=17, color=MUTED, spacing=1.35)
    panel(s, MARGIN + Inches(7.2), Inches(2.3), Inches(4.6), Inches(3.1),
          fill=PALE_RUST)
    text(s, "Why we aren't calling it confirmed", MARGIN + Inches(7.5), Inches(2.56),
         Inches(4.0), Inches(0.62), size=16, color=RUST, bold=True)
    text(s, "No no-phage control — a margin note on the page says only “need "
            "control”.\n\nOne isolate was never scored.\n\nTwo follow-up readouts were "
            "never written down.", MARGIN + Inches(7.5), Inches(3.1), Inches(4.0),
         Inches(2.1), size=15, color=INK, spacing=1.35)
    notes(s, "That hypothesis makes a prediction we can falsify. We tested that in "
             "July. We spotted eighteen host isolates against two pooled lysates, and "
             "the Strain 1 and Strain 3 representatives came back negative against "
             "both.\n\nWe're not calling it confirmed, and the reasons come from our "
             "own notebook rather than from a reviewer. The result is consistent with "
             "the prediction, and nothing contradicts it, but we haven't done the "
             "clean experiment.")


def cycle_three(d):
    frame(d, "wheel", "03-cycle", "Cycle 3 of four", morph=False,
          note="Cycle three — build the enzymes. Two lines run through it, and they "
               "are two different proteins.")

    for i in range(2):
        s = d.new(morph=(i > 0))
        eyebrow(s, "Cycle 3 · Two lines, two proteins")
        if i == 0:
            picture(s, FIGS / "body-side.png", MARGIN + Inches(3.4), Inches(1.1),
                    Inches(5.0), Inches(5.0), name="!!left")
            text(s, "CDS 11 — the tail spike", MARGIN + Inches(3.4), Inches(6.25),
                 Inches(5.0), Inches(0.4), size=20, color=TEAL, bold=True,
                 align=PP_ALIGN.CENTER)
        else:
            picture(s, FIGS / "body-side.png", MARGIN + Inches(0.2), Inches(1.1),
                    Inches(4.4), Inches(4.3), name="!!left")
            text(s, "CDS 11 — the tail spike", MARGIN + Inches(0.2), Inches(5.5),
                 Inches(4.4), Inches(0.4), size=18, color=TEAL, bold=True,
                 align=PP_ALIGN.CENTER)
            text(s, "A right-handed β-helix, 941 residues.\nThis is the one that reads "
                    "the host surface.", MARGIN + Inches(0.2), Inches(5.95),
                 Inches(4.4), Inches(1.0), size=14, color=MUTED,
                 align=PP_ALIGN.CENTER, spacing=1.35)
            picture(s, FIGS / "gh5.png", MARGIN + Inches(6.3), Inches(1.6),
                    Inches(5.3), Inches(3.3), name="!!right")
            text(s, "CDS 12 — a GH5 hydrolase", MARGIN + Inches(6.3), Inches(5.1),
                 Inches(5.3), Inches(0.4), size=18, color=RUST, bold=True,
                 align=PP_ALIGN.CENTER)
            text(s, "A TIM barrel, not a β-helix. Its closest structural match is an "
                    "endoglucanase caught with a short cellulose chain.\nA separate "
                    "protein — not a domain of the tail spike.",
                 MARGIN + Inches(6.3), Inches(5.55), Inches(5.3), Inches(1.4),
                 size=14, color=MUTED, align=PP_ALIGN.CENTER, spacing=1.35)
            notes(s, "Two enzymes sit in the tail module. CDS 11, the beta-helix, is "
                     "the one that reads the host surface. And next to it CDS 12, a "
                     "glycoside hydrolase from family five — a TIM barrel, not a "
                     "beta-helix, whose closest structural match is an endoglucanase "
                     "caught with a short cellulose chain. It is a separate protein, "
                     "not a domain of the tail spike, and we have not established what "
                     "it does inside the phage.")

    cards(d, "The question a judge will ask",
          "So why reconstruct ancestors of that one, and not of the tail spike?",
          [("A tree to reconstruct along",
            "CDS 12 has a thousand homologues. The tail spike is novel enough that we "
            "had no such tree.", TEAL, WHITE),
           ("A third of the size",
            "362 residues against 941. We judged it the far better bet to express.",
            TEAL, WHITE),
           ("A synthesis allowance",
            "Four short constructs were affordable inside our sponsored allowance. "
            "Four long ones were not.", TEAL, WHITE)],
          accent=RUST, height=Inches(2.3),
          note="So why did we reconstruct ancestors of that one, rather than of the "
               "tail spike we've just spent five minutes on? Three reasons, and none "
               "of them is that we got confused. CDS 12 has a thousand homologues in "
               "the databases, which is what you need to build a tree and reconstruct "
               "along it. CDS 12 is a third of the size, so we judged it the far "
               "better bet to express. And we were working inside a sponsored "
               "synthesis allowance, where four short constructs were affordable and "
               "four long ones were not.")

    statement(d, "and what that costs us",
              "The ancestral panel tests the shape of the hypothesis\non an enzyme we "
              "could actually build — not on the one\nthat reads the receptor.",
              "That's a real limitation, and it's ours, not a reviewer's.", bg=RUST,
              size=29,
              note="So our ancestral panel tests the shape of the hypothesis — whether "
                   "an ancestral glycoside hydrolase has a broader substrate range "
                   "than its descendant — on an enzyme we could actually build, rather "
                   "than on the one that reads the receptor. That's a real limitation, "
                   "and it's ours, not a reviewer's.")

    run(d, "tree", ["01-node", "02-node", "03-node", "04-node", "05-three"],
        "Cycle 3 · Build — walking back up the tree",
        note="We worked out the direction with our PI, and he ran the alignment, the "
             "tree and the reconstruction on sequences we prepared. He reconstructed "
             "every node on the path from CDS 12 back to the root, nine hundred and "
             "ninety-eight of them, and we picked three to order as DNA.")

    prose(d, "Cycle 3 · Build", "All four fold to the same TIM barrel",
          "Six constructs in pET-28a with an N-terminal His-tag, from Twist — and all "
          "six are now published basic parts on the iGEM Registry, under CC0.\n\n"
          "Three of them are sequences that exist nowhere in nature.\n\nOne warning: "
          "our first order was codon-optimised and our second wasn't. In an E. coli "
          "host, that bias is the first thing to suspect when a band doesn't appear.",
          figkey="cds12-family",
          note="All six went into pET-28a with an N-terminal His-tag and were "
               "synthesised by Twist across two orders, and all six are now published "
               "basic parts on the iGEM Registry under a CC0 licence. Three of the six "
               "are those reconstructed ancestors — protein sequences that exist "
               "nowhere in nature. We think any team working on an enzyme family could "
               "take the same route to new parts, so we wrote the method out in full."
               "\n\nOne warning we'd pass on, because it cost us: our first order was "
               "codon-optimised and our second wasn't.")

    prose(d, "Cycle 3 · What the model said, and its own control",
          "Along the path to the root, the score improves steadily",
          "The label it likes best is endo-1,4-β-glucanase — the same chemistry the "
          "structure points at.\n\nExcept it doesn't survive its own control. A "
          "reconstructed ancestor is consensus-like by construction, so it scores "
          "better under almost any label — and it does, in 21 of 24 classes.\n\n"
          "Direction alone proves nothing. And perplexity isn't activity.",
          figkey="zymctrl",
          note="Before any of them reached a bench, we asked a model what it thought. "
               "The label it likes best is endo-one-four-beta-glucanase — the same "
               "chemistry the structure points at. And along the path to the root the "
               "score improves steadily, which, read on its own, is our hypothesis "
               "coming true.\n\nExcept that it doesn't survive its own control. A "
               "reconstructed ancestor is consensus-like by construction, so it scores "
               "better under almost any label — and it does, in twenty-one of the "
               "twenty-four classes. Direction alone proves nothing.\n\nAnd perplexity "
               "isn't activity.")

    s = d.new()
    eyebrow(s, "Cycle 3 · Test")
    text(s, "Four rounds at the bench, and they didn't line up neatly", MARGIN,
         Inches(0.98), CONTENT_W, Inches(0.8), size=28, color=INK, font=DISPLAY)
    rounds = [("15 Sep", "Two gels, four constructs, induced against uninduced — no "
               "detectable induction on either.", WHITE),
              ("29 Sep", "CDS 12 gives the first induction-dependent band at the right "
               "size.", PALE),
              ("1 Oct", "Nickel columns on six constructs. The first ancestor eluted "
               "at its predicted mass — the only one that did. The tail spike eluted "
               "something, 29 kDa short.", PALE),
              ("10 Oct", "Same column, second ancestor. Both elutions blank; the load "
               "and the flow-through carried the same band.", PALE_RUST)]
    y = Inches(2.2)
    for when, what, fill in rounds:
        panel(s, MARGIN, y, Inches(6.6), Inches(0.98), fill=fill, line=RULE,
              radius=0.02)
        text(s, when, MARGIN + Inches(0.26), y + Inches(0.3), Inches(1.1),
             Inches(0.36), size=15, color=INK, bold=True)
        text(s, what, MARGIN + Inches(1.5), y + Inches(0.16), Inches(4.9),
             Inches(0.8), size=13, color=MUTED, spacing=1.3)
        y += Inches(1.06)
    picture(s, FIGS / "gel0929.png", MARGIN + Inches(7.2), Inches(2.2), Inches(4.6),
            Inches(1.9))
    picture(s, FIGS / "gel1010.png", MARGIN + Inches(7.2), Inches(4.3), Inches(4.6),
            Inches(1.9))
    text(s, "Empty-vector BL21 lane: absent in all eight protein assays", MARGIN,
         H - Inches(0.6), CONTENT_W - Inches(0.9), Inches(0.4), size=12, color=RUST)
    notes(s, "We tested expression four times, and the rounds didn't line up neatly."
             "\n\nOn October the first we ran nickel columns on six constructs, and "
             "one of them worked: the first ancestor eluted at its predicted mass, the "
             "only construct that did. The tail spike eluted something too, but "
             "twenty-nine kilodaltons short.\n\nOn October the tenth both elutions came "
             "off blank. We read that as a purification we had botched, and we were "
             "about to spend another week on it.")

    run(d, "nickel", ["01-load", "02-through", "03-flowthrough", "04-elution-empty"],
        "Cycle 3 · Where the column actually failed", accent=RUST,
        note="A nickel column is supposed to hold a His-tagged protein on the resin "
             "while everything else washes past. Ours didn't hold it: the load and the "
             "flow-through carried the same band, and both elutions came off blank.")

    run(d, "indistinguishable",
        ["01-three-cases", "02-same-lane", "03-cannot", "04-dotblot-splits"],
        "Cycle 3 · Why a gel could not tell us", accent=RUST,
        note="And this is the trap. Three completely different things — no protein "
             "made, protein made but insoluble, protein made and missed by the column "
             "— all give you the same blank lane. A gel cannot separate them.")

    prose(d, "Cycle 3 · Learn — an outside view changed a result",
          "What stopped us wasn't an experiment. It was a conversation.",
          "On 13 October we took it to Prof. Ilya Tolstorukov at Keck Graduate "
          "Institute. He wrote back before we met to say expression was his field and "
          "purification wasn't — and met us anyway.\n\nHe changed the question. Not "
          "why is nothing eluting, but is there anything there to elute.\n\nSix days "
          "later the flow-through read 2.9× the negative control. The run had failed "
          "at capture, not at expression.",
          frame_sub="nickel", frame_name="05-dotblot", accent=RUST,
          note="What stopped us wasn't an experiment. It was a conversation.\n\nOn "
               "October the thirteenth we took the problem to Professor Ilya "
               "Tolstorukov at Keck Graduate Institute, who works on protein "
               "expression. He wrote back before we met to say he wasn't sure he was "
               "the right person — expression is his field, purification isn't — and "
               "he met us anyway. That turned out to be the point.\n\nHe changed the "
               "question. Not why is nothing eluting, but is there anything there to "
               "elute. He told us to check whether the protein was being made at all, "
               "with a dot blot against an anti-His antibody, before we touched the "
               "column again.\n\nSix days later we ran that blot, and the flow-through "
               "from the second ancestor read two point nine times the negative "
               "control. So what we learned is that the protein had been there all "
               "along. It was made, it came off in the flow-through, and the run had "
               "failed at capture — not at expression.\n\nWe had spent a week "
               "debugging the last step of a workflow without checking that the first "
               "step worked, because the last step was the one visibly failing. That's "
               "the generalisable mistake, and one meeting fixed it.")

    prose(d, "Cycle 3 · The assay the whole project points at",
          "Does an enzyme, on its own, do anything to the sugar?",
          "No visible lysis anywhere — including Φ8 on its own hosts — so the assay "
          "never read clearing. But counting colonies inside the drops gives a number: "
          "under the first ancestor, across seven strains, they fall to a median of "
          "12 % of the plate's PBS control. Φ8's own median is 0 %.\n\nOur PI reads "
          "that as activity. Before we do: the carry-over control was not run, and "
          "those dilutions later read at or below our dot blot's floor.\n\nIt is one "
          "plate.",
          figkey="spottest",
          note="Then we ran the assay the whole project points at: does an enzyme, on "
               "its own, do anything to the sugar?\n\nWe read it on October the "
               "sixteenth. Under the first ancestor, across seven strains, colony "
               "counts fall to a median of twelve percent of the plate's PBS control. "
               "Phi-8's own median is zero.\n\nOur PI reads that suppression as enzyme "
               "activity. We'd want more before we call it that ourselves, and there "
               "are two specific gaps.\n\nIt's the strongest activity signal we have, "
               "and it is one plate.")

    statement(d, "one gap runs through all of it",
              "Eight protein assays — seven gels and a dot blot —\nand not one of them "
              "carries a lane of untransformed BL21.",
              "We designed every round around a different variable instead. That "
              "control is on the bench now.", bg=RUST, size=30,
              note="And one gap runs through all of it. We have now run eight protein "
                   "assays — seven gels and a dot blot — and not one of them carries a "
                   "lane of untransformed BL21. We designed every round around a "
                   "different variable instead. That control is on the bench now.")


def cycle_four(d):
    frame(d, "wheel", "04-cycle", "Cycle 4 of four", morph=False,
          note="Cycle four — let the bacteria answer. Selection instead of "
               "prediction. Three cycles in, every guess about the receptor had come "
               "from the phage's side.")

    run(d, "reads", ["01-candidates", "02-filtered", "03-support"],
        "Cycle 4 · Test — checked at read level",
        note="In July we picked colonies from inside the plaque zone — cells still "
             "growing where the phage should have killed them — and in October we "
             "sequenced one from each host against its parent. There's no structure "
             "prediction anywhere in this loop.\n\nA naive assembly comparison gave us "
             "sixteen to twenty-one differing sites, which means nothing on its own. "
             "So we took every candidate back to the raw reads: seventy sites, checked "
             "against the parent's reads and against an independent read set with "
             "completely different chemistry.\n\nExactly one survived — carried by two "
             "hundred and sixty-three of two hundred and sixty-four mutant reads and "
             "by none of the parent's.")

    figure(d, "Cycle 4 · Test", "The one mutation, at read level", "mutation",
           "A missense change in a Stealth-family sugar phosphotransferase, inside a "
           "30 kb cluster that builds and exports capsular polysaccharide. The other "
           "pick has no confirmed mutation at all.",
           note="It sits inside a thirty-kilobase cluster that builds and exports "
                "capsular polysaccharide. The other pick has no confirmed mutation at "
                "all.")

    run(d, "masking", ["01-oantigen", "02-capsule", "03-both"],
        "Cycle 4 · Learn", accent=RUST,
        note="What we learned disagrees with Cycle 2 — which is the whole reason we "
             "did it this way round. Cycle 2 told us the receptor is a sugar. Cycle 4 "
             "agrees it's a sugar, and disagrees about which one: it points at the "
             "capsule, with the O-antigen cassette intact.\n\nBoth can be true at "
             "once, because a capsule sits on top and can hide an intact O-antigen "
             "underneath it. We don't know which surface Phi-8 reads, so wherever the "
             "distinction matters we say surface polysaccharide and leave it there."
             "\n\nAnd the honest gap: we never confirmed those colonies were "
             "resistant. They were colonies in a plaque zone, which is suggestive and "
             "isn't the same thing.")


def closing(d):
    cards(d, "Contribution", "Four things we're leaving behind — one is a failure",
          [("Two packaged tools",
            "MIT licensed, on iGEM's GitLab. Gel densitometry, and the fold test from "
            "Cycle 2 — which also told a terminal repeat from a circular join, and "
            "changed our own answer about the genome.", TEAL, WHITE),
           ("Six registered parts",
            "Published under CC0 — three of them sequences that never existed, "
            "reconstructed from an alignment and a tree.", TEAL, WHITE),
           ("A benchmark",
            "A machine-learning classifier found a depolymerase that homology "
            "annotation had filed as hypothetical. Run both, and reconcile the "
            "disagreements.", TEAL, WHITE),
           ("The screen that failed",
            "Published with the controls that caught it. Don't use interface scores to "
            "screen phage–host protein pairs.", CREAM, RUST)],
          top=Inches(2.4), height=Inches(3.2),
          note="We're leaving four things behind, and one of them is a failure.")

    cards(d, "Human practices · California Botanic Garden · 19 October 2026",
          "We went back and asked. Most of what we'd assumed was wrong.",
          [("We expected to argue for biological control",
            "We didn't have to. They already suppress soil fungi by mulching.",
            MUTED, WHITE),
           ("We expected the objection to be ecological risk",
            "It was whether the thing works. Copper on every blossom every four or "
            "five days, 86 acres, eight staff. The objection is arithmetic.",
            MUTED, WHITE),
           ("The finding that costs us most",
            "They have never had a sample come back positive for Pseudomonas. We "
            "isolated a soil phage and its environmental host — not a treatment for a "
            "disease this stakeholder has.", CREAM, RUST)],
          top=Inches(2.3), height=Inches(2.5),
          note="Two days before our wiki froze, we went back to the garden the soil "
               "came from, and asked the people who manage it whether a treatment as "
               "strain-specific as ours would be any use to them.\n\nWe found that "
               "most of what we had assumed was wrong.\n\nAnd here's the finding that "
               "costs us most. They have never had a sample come back positive for "
               "Pseudomonas.\n\n[PLACE THE INTERVIEW CLIPS HERE — at least 20 seconds, "
               "as promised on the recording.]")

    statement(d, "and what they do need",
              "Something for bacteria inside the vascular system,\nwhere nothing they "
              "have reaches.",
              "Our strain doesn't solve that. But the question we worked on is the one "
              "you'd have to answer first. The strain is local. The question isn't.",
              size=31,
              note="What they do need is something for bacteria inside the vascular "
                   "system, where nothing they have reaches. Our strain doesn't solve "
                   "that. But the question we worked on — what a tail spike reads on a "
                   "cell surface, and how far you can predict that from a genome — is "
                   "the one you'd have to answer first. The strain is local. The "
                   "question isn't.")

    cards(d, "Safety and security",
          "One condition is still open — and it is host range, the subject of the "
          "whole project",
          [("What the committee asked",
            "To show our reasoning that the work won't alter host range, virulence, or "
            "antibiotic resistance. We don't have full approval. The revision is being "
            "written.", RUST, PALE_RUST),
           ("What we can say",
            "Φ8 carries no virulence factors and no resistance genes across all eighty "
            "coding sequences. Our constructs are protein fragments in laboratory "
            "E. coli. Nothing here is a modified phage.", TEAL, WHITE),
           ("Why we treat it as dual use",
            "Understanding what sets the ceiling on host range is the same as knowing "
            "what would have to change to raise it.", CREAM, INK)],
          top=Inches(2.5), height=Inches(2.7),
          note="On safety: our institutional biosafety committee gave us conditional "
               "approval with one condition still open, and that condition is a "
               "question about host range — the subject of this entire project.\n\nBut "
               "understanding what sets the ceiling on host range is the same as "
               "knowing what would have to change to raise it, so we treat this as "
               "dual-use rather than arguing our way to a clean no.")

    s = d.new()
    eyebrow(s, "Where we are")
    text(s, "Established · partly tested · open", MARGIN, Inches(0.98), CONTENT_W,
         Inches(0.8), size=29, color=INK, font=DISPLAY)
    cols = [("Established", TEAL,
             "Five bacterial genomes and a novel circular phage genome\n"
             "Three unrelated sugar cassettes in one locus — with no serotype scheme "
             "in existence that could have told us\n"
             "A tail spike that is a sugar-cutting enzyme, by two independent methods\n"
             "A controlled negative result about interface prediction\n"
             "One resistance mutation verified in the reads"),
            ("Partly tested", RGBColor_gold(),
             "That Φ8 won't infect the other two strains — the July assay pointed the "
             "right way, and carried no control\n"
             "One ancestor purified at its predicted mass\n"
             "Colony counts under it fall to 12 % of control — which our PI reads as "
             "activity, and we won't, until the carry-over control is run"),
            ("Open", RUST,
             "A clean expression round, with the lane we keep not running\n"
             "Whether the tail spike fragment is even full length\n"
             "Which sugar layer the phage reads\n"
             "Whether Φ8 is temperate\n"
             "Depositing the genome, which we haven't done")]
    cw = int((CONTENT_W - Inches(0.6)) / 3)
    for i, (t, colour, body) in enumerate(cols):
        x = int(MARGIN + (cw + Inches(0.3)) * i)
        panel(s, x, Inches(2.3), cw, Inches(0.05), fill=colour, radius=0.0)
        text(s, t, x, Inches(2.5), cw, Inches(0.5), size=20, color=colour, bold=True)
        text(s, body, x, Inches(3.05), cw, Inches(3.6), size=14, color=INK,
             spacing=1.5)
    notes(s, "So let us say plainly where we are.\n\nWe have established five "
             "bacterial genomes and a novel circular phage genome; three unrelated "
             "sugar cassettes in the same locus; a tail spike that is a sugar-cutting "
             "enzyme by two independent methods; a controlled negative result; and one "
             "resistance mutation verified in the reads.\n\nWe have partly tested two "
             "things.\n\nAnd we have left plenty open.")

    s = d.new(bg=INK)
    text(s, "FOUR CYCLES, THREE OF THEM WRONG", MARGIN, Inches(1.5), CONTENT_W,
         Inches(0.3), size=13, color=LIGHT, bold=True)
    text(s, "Each one was wrong in a way that\ntold us where to go next.", MARGIN,
         Inches(2.05), CONTENT_W, Inches(1.8), size=42, color=CREAM, font=DISPLAY,
         spacing=1.18)
    panel(s, MARGIN, Inches(4.15), CONTENT_W, Inches(1.9), fill=TEAL)
    text(s, "If we could pass on one thing: put the cheap control\nin front of the "
            "expensive experiment.", MARGIN + Inches(0.45), Inches(4.42),
         CONTENT_W - Inches(0.9), Inches(1.0), size=25, color=CREAM, font=DISPLAY,
         spacing=1.2)
    text(s, "Nine folds told us what seven thousand couldn't, and one afternoon's dot "
            "blot told us what a week on a column hadn't.", MARGIN + Inches(0.45),
         Inches(5.5), CONTENT_W - Inches(0.9), Inches(0.5), size=15, color=DIM)
    text(s, "iGEM Claremont-CA 2026 · Phagenomics · 2026.igem.wiki/claremont-ca",
         MARGIN, H - Inches(0.6), CONTENT_W, Inches(0.3), size=12, color=LIGHT)
    notes(s, "Four cycles, three of them wrong, and each one wrong in a way that told "
             "us where to go next. If we could pass on one thing, it's this: put the "
             "cheap control in front of the expensive experiment. Nine folds told us "
             "what seven thousand couldn't, and one afternoon's dot blot told us what "
             "a week on a column hadn't.\n\n[CREDITS CARD FOLLOWS — 30 seconds, no "
             "narration.]")


def RGBColor_gold():
    from pptx.dml.color import RGBColor as _R
    return _R(0xC9, 0xA2, 0x27)


if __name__ == "__main__":
    deck = Deck()
    cover(deck)
    act_one(deck)
    cycle_one(deck)
    cycle_two(deck)
    cycle_three(deck)
    cycle_four(deck)
    closing(deck)
    print(f"{deck.save()} slides -> {OUT.relative_to(ROOT)}")
