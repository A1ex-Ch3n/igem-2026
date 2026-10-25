"""Build the Phagenomics presentation deck as a PowerPoint file.

The deck is built the way Hamburg 2023's winning presentation was: a white page,
a coloured title bar, and the same protein renders carried through the talk and
re-annotated rather than replaced. Movement comes from Morph transitions between
near-identical slides, so a build is a short run of slides and PowerPoint tweens
the shapes that share a name.

    python code/1025_presentation_deck/build_deck.py

Writes documents/2026-10-25_presentation_deck.pptx.
"""
from copy import deepcopy
from pathlib import Path

from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parents[2]
ASSETS = Path(
    "/private/tmp/claude-501/-Users-alexy-Desktop-iGEM-26/"
    "77c93b6d-bdc5-452e-8971-b54893d1cd43/scratchpad/pptx_assets"
)
OUT = ROOT / "documents/2026-10-25_presentation_deck.pptx"

W, H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.78)
CONTENT_W = W - 2 * MARGIN

DARK = RGBColor(0x1C, 0x2B, 0x2B)
TEAL = RGBColor(0x2D, 0x6A, 0x6A)
RUST = RGBColor(0xB4, 0x54, 0x2E)
MUTED = RGBColor(0x55, 0x60, 0x5F)
RULE = RGBColor(0xDC, 0xD8, 0xD0)
PALE = RGBColor(0xEA, 0xF0, 0xEE)
PALE_RUST = RGBColor(0xF6, 0xE7, 0xE0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_TEAL = RGBColor(0x8F, 0xB3, 0xAE)

DISPLAY = "Georgia"
BODY = "Avenir Next"

MORPH = (
    '<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">'
    '<mc:Choice xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" Requires="p14">'
    '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
    ' spd="slow" p14:dur="900">'
    '<p159:morph xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"'
    ' option="byObject"/>'
    "</p:transition></mc:Choice><mc:Fallback>"
    '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med">'
    "<p:fade/></p:transition></mc:Fallback></mc:AlternateContent>"
)
FADE = (
    '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med">'
    "<p:fade/></p:transition>"
)


def transition(slide, xml):
    """Attach a slide transition; it must follow clrMapOvr in the slide element."""
    sld = slide._element
    for existing in sld.findall(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}transition"
    ):
        sld.remove(existing)
    node = etree.fromstring(xml)
    clr = sld.find("{http://schemas.openxmlformats.org/presentationml/2006/main}clrMapOvr")
    if clr is None:
        sld.append(node)
    else:
        clr.addnext(node)


class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = W, H
        self.blank = self.prs.slide_layouts[6]
        self.n = 0

    def slide(self, morph=False, bg=WHITE, number=True):
        s = self.prs.slides.add_slide(self.blank)
        bgfill = s.background.fill
        bgfill.solid()
        bgfill.fore_color.rgb = bg
        transition(s, MORPH if morph else FADE)
        self.n += 1
        if number:
            page(s, self.n, bg)
        return s

    def save(self):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        self.prs.save(OUT)
        return self.n


def text(slide, body, left, top, width, height=None, size=20, color=DARK,
         bold=False, font=BODY, align=PP_ALIGN.LEFT, italic=False, spacing=1.25,
         anchor=MSO_ANCHOR.TOP, name=None):
    height = height if height is not None else Inches(1)
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(body.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        run = p.add_run()
        run.text = line
        f = run.font
        f.name, f.size, f.bold, f.italic = font, Pt(size), bold, italic
        f.color.rgb = color
    if name:
        box.name = name
    return box


def rich(slide, parts, left, top, width, height=None, size=20, align=PP_ALIGN.LEFT,
         spacing=1.25, font=BODY, name=None):
    """parts: list of (text, color, bold, italic) on one paragraph."""
    height = height if height is not None else Inches(1)
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment, p.line_spacing = align, spacing
    for body, color, bold, italic in parts:
        run = p.add_run()
        run.text = body
        f = run.font
        f.name, f.size, f.bold, f.italic = font, Pt(size), bold, italic
        f.color.rgb = color
    if name:
        box.name = name
    return box


def box(slide, left, top, width, height, fill=None, line=None, radius=True,
        line_w=Pt(1), name=None, shape=None):
    kind = shape or (MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE)
    sh = slide.shapes.add_shape(kind, left, top, width, height)
    if radius and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = 0.06
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
        sh.line.width = line_w
    sh.shadow.inherit = False
    if name:
        sh.name = name
    tf = sh.text_frame
    tf.margin_left = tf.margin_right = Inches(0.28)
    tf.margin_top = tf.margin_bottom = Inches(0.2)
    tf.word_wrap = True
    return sh


def card(slide, left, top, width, height, title, body, accent=TEAL, fill=WHITE,
         title_size=17, body_size=15, title_color=None):
    box(slide, left, top, width, height, fill=fill, line=RULE)
    text(slide, title, left + Inches(0.3), top + Inches(0.24), width - Inches(0.6),
         size=title_size, color=title_color or accent, bold=True)
    text(slide, body, left + Inches(0.3), top + Inches(0.74), width - Inches(0.6),
         size=body_size, color=MUTED, spacing=1.3)


def title_bar(slide, label, heading, accent=TEAL, heading_size=31, width=None):
    """Hamburg's move: a coloured eyebrow bar, then the heading under it."""
    w = width or CONTENT_W
    bar = box(slide, MARGIN, Inches(0.52), Inches(0.16), Inches(0.34),
              fill=accent, radius=False)
    bar.name = "!!bar"
    text(slide, label.upper(), MARGIN + Inches(0.34), Inches(0.54), w - Inches(0.34),
         size=13, color=accent, bold=True, name="!!eyebrow")
    text(slide, heading, MARGIN, Inches(1.02), w, size=heading_size, color=DARK,
         font=DISPLAY, spacing=1.08, name="!!heading")


def page(slide, n, bg):
    colour = RGBColor(0x8A, 0x93, 0x91) if bg == WHITE else LIGHT_TEAL
    text(slide, str(n), W - MARGIN - Inches(0.6), H - Inches(0.52), Inches(0.6),
         height=Inches(0.26), size=11, color=colour, align=PP_ALIGN.RIGHT)


def footer(slide, body, color=None):
    text(slide, body, MARGIN, H - Inches(0.62), CONTENT_W - Inches(0.8),
         height=Inches(0.46), size=12, color=color or RGBColor(0x8A, 0x93, 0x91),
         spacing=1.15)


def picture(slide, key, left, top, max_w, max_h, name=None):
    """Place an image scaled to fit the box, centred in it."""
    path = ASSETS / f"{key}.png"
    iw, ih = Image.open(path).size
    scale = min(max_w / iw, max_h / ih)
    w, h = int(iw * scale), int(ih * scale)
    pic = slide.shapes.add_picture(
        str(path), int(left + (max_w - w) / 2), int(top + (max_h - h) / 2), w, h
    )
    if name:
        pic.name = name
    return pic


def notes(slide, body):
    slide.notes_slide.notes_text_frame.text = body


# --------------------------------------------------------------------------- #
# The bacterial envelope, drawn in native shapes so a build can morph through it
# --------------------------------------------------------------------------- #

def envelope(slide, stage, left, top, w, h):
    """stage 1 membrane · 2 + O-antigen · 3 + capsule · 4 + an approaching phage."""
    base = top + h
    mem_h = Inches(0.17)
    box(slide, left, base - mem_h, w, mem_h, fill=RGBColor(0x8F, 0xA7, 0xA4),
        radius=False, name="!!mem-outer")
    box(slide, left, base - mem_h * 2 - Inches(0.05), w, mem_h,
        fill=RGBColor(0xC2, 0xCF, 0xC6), radius=False, name="!!mem-wall")
    box(slide, left, base - mem_h * 3 - Inches(0.1), w, mem_h,
        fill=RGBColor(0x8F, 0xA7, 0xA4), radius=False, name="!!mem-inner")
    chain_top = base - mem_h * 3 - Inches(0.1)

    if stage >= 2:
        n = 11
        step = (w - Inches(0.5)) / (n - 1)
        for i in range(n):
            x = left + Inches(0.25) + step * i
            length = Inches(1.05) + Inches(0.12) * ((i * 7) % 3)
            box(slide, int(x), int(chain_top - length), Inches(0.055), int(length),
                fill=TEAL, radius=False, name=f"!!chain{i}")
            box(slide, int(x - Inches(0.035)), int(chain_top - length - Inches(0.09)),
                Inches(0.125), Inches(0.125), fill=TEAL,
                shape=MSO_SHAPE.OVAL, name=f"!!cap{i}")
    if stage >= 3:
        cap = box(slide, left, int(chain_top - Inches(2.1)), w, Inches(0.62),
                  fill=RUST, name="!!capsule")
        cap.fill.fore_color.rgb = RUST
        cap.adjustments[0] = 0.5
        from pptx.oxml.ns import qn
        solid = cap.fill._xPr.find(qn("a:solidFill"))
        alpha = etree.SubElement(solid.find(qn("a:srgbClr")), qn("a:alpha"))
        alpha.set("val", "38000")
    if stage >= 4:
        box(slide, int(left + w / 2 - Inches(0.05)), int(top), Inches(0.1),
            Inches(0.9), fill=DARK, radius=False, name="!!tail")
        box(slide, int(left + w / 2 - Inches(0.19)), int(top + Inches(0.88)),
            Inches(0.38), Inches(0.55), fill=DARK,
            shape=MSO_SHAPE.ISOSCELES_TRIANGLE, name="!!spike")
        sp = slide.shapes[-1]
        sp.rotation = 180


def label(slide, body, left, top, width, color, size=15):
    text(slide, body, left, top, width, size=size, color=color, bold=True)


# --------------------------------------------------------------------------- #
# The deck
# --------------------------------------------------------------------------- #

def build():
    d = Deck()

    # ---- cover -----------------------------------------------------------
    s = d.slide(bg=DARK, number=False)
    text(s, "iGEM CLAREMONT-CA · 2026", MARGIN, Inches(1.5), CONTENT_W,
         size=15, color=LIGHT_TEAL, bold=True)
    text(s, "Phagenomics", MARGIN, Inches(2.1), CONTENT_W, size=72,
         color=RGBColor(0xF7, 0xF4, 0xEE), font=DISPLAY, spacing=1.0)
    text(s, "What decides which bacteria a phage can kill —\nand what happened the four times we asked.",
         MARGIN, Inches(3.65), Inches(9), size=24,
         color=RGBColor(0xC8, 0xD8, 0xD4), spacing=1.3)
    text(s, "Bacteriophage Φ8  ·  Pseudomonas  ·  California Botanic Garden soil",
         MARGIN, Inches(6.3), CONTENT_W, size=14, color=LIGHT_TEAL)
    notes(s, "We're iGEM Claremont-CA, a first-year team in California, and this is "
             "Phagenomics.\n\nWe work on one question: what decides which bacteria a "
             "phage can kill?")

    # ---- the gap ---------------------------------------------------------
    s = d.slide()
    title_bar(s, "The gap we work in",
              "Phage therapy's bottleneck is host range — and nobody can design\n"
              "host range, because nobody can say how a phage finds its target.")
    y = Inches(2.9)
    card(s, MARGIN, y, Inches(5.7), Inches(1.6), "What we did not do",
         "Build a therapeutic.", accent=MUTED)
    card(s, MARGIN + Inches(6.13), y, Inches(5.7), Inches(1.6), "What we did",
         "Work on the recognition step that any therapeutic would depend on —\n"
         "four times, three of them wrong.")
    text(s, "Pseudomonas causes serious infections in immunocompromised patients and "
            "persistent crop disease in agriculture.", MARGIN, Inches(5.05), CONTENT_W,
         size=16, color=MUTED, italic=True)
    notes(s, "Pseudomonas causes serious infections in immunocompromised patients and "
             "persistent crop disease in agriculture, and phage therapy is one of the "
             "alternatives to antibiotics people are betting on. Its bottleneck is host "
             "range. Each phage binds a specific receptor on a specific strain, and "
             "nobody can design that specificity yet, because we don't understand how a "
             "phage recognises its target in the first place.\n\nSo we didn't try to "
             "build a therapeutic. We tried to understand the recognition step that any "
             "therapeutic would depend on. We went at it four times this season. Three "
             "of those four failed, and the failures are the useful part.")

    # ---- the problem in one image ---------------------------------------
    s = d.slide()
    title_bar(s, "The problem, in one image",
              "Same phage, different strain.")
    bw, bh = Inches(5.3), Inches(2.5)
    left1, left2 = MARGIN + Inches(0.4), MARGIN + Inches(6.4)
    yy = Inches(2.45)
    box(s, left1, yy, bw, bh, fill=RGBColor(0xC9, 0xD6, 0xCE), radius=False)
    box(s, int(left1 + bw / 2 - Inches(0.85)), int(yy + bh / 2 - Inches(0.85)),
        Inches(1.7), Inches(1.7), fill=WHITE, line=TEAL, line_w=Pt(2.5),
        shape=MSO_SHAPE.OVAL)
    box(s, left2, yy, bw, bh, fill=RGBColor(0xC9, 0xD6, 0xCE), radius=False)
    ring = box(s, int(left2 + bw / 2 - Inches(0.85)), int(yy + bh / 2 - Inches(0.85)),
               Inches(1.7), Inches(1.7), fill=None, line=RUST, line_w=Pt(2.5),
               shape=MSO_SHAPE.OVAL)
    ring.line.dash_style = 4
    label(s, "Its own host — a clear circle where the bacteria used to be",
          left1, yy + bh + Inches(0.22), bw, TEAL)
    label(s, "The next plate — nothing happens", left2, yy + bh + Inches(0.22), bw, RUST)
    text(s, "To treat an infection you need a phage that matches the strain in front of "
            "you, and usually there isn't one.", MARGIN, Inches(6.0), CONTENT_W,
         size=19, color=DARK)
    notes(s, "Here is the problem in one image. We put a drop of phage onto a lawn of "
             "bacteria, and a few hours later there's a clear circle where the bacteria "
             "used to be. We move the same drop to the next plate, and nothing happens. "
             "Same phage, different strain.\n\nPhages are fussy about what they kill, and "
             "that fussiness is the bottleneck.")

    # ---- BUILD: the sugar coat ------------------------------------------
    env_l, env_t, env_w, env_h = MARGIN + Inches(0.6), Inches(2.25), Inches(6.6), Inches(4.0)
    stages = [
        ("The envelope",
         "Outer membrane, wall, inner membrane — and the proteins a textbook would "
         "have the phage bind.", MUTED),
        ("O-antigen",
         "But many bacteria don't present a bare protein surface. Long sugar chains "
         "are anchored in the outer membrane.", TEAL),
        ("Capsule",
         "And above those, in some species, a second polysaccharide layer sits over "
         "everything below.", RUST),
        ("What the phage touches",
         "So the first thing a phage meets is not protein. It is a forest of sugar.", DARK),
    ]
    for i, (head, blurb, colour) in enumerate(stages, start=1):
        s = d.slide(morph=(i > 1))
        title_bar(s, "Adsorption decides everything",
                  "It gets decided before any DNA moves")
        envelope(s, i, env_l, env_t, env_w, env_h)
        text(s, head, MARGIN + Inches(7.9), Inches(2.5), Inches(4.0), size=24,
             color=colour, font=DISPLAY, name="!!stage-head")
        text(s, blurb, MARGIN + Inches(7.9), Inches(3.15), Inches(4.0), size=17,
             color=MUTED, spacing=1.35, name="!!stage-body")
        notes(s, "It gets decided at the very first step, before any DNA moves: the "
                 "phage has to recognise the outside of the cell and stick to it.\n\n"
                 "And many bacteria don't present a bare protein surface. They wrap "
                 "themselves in sugar — long chains called the O-antigen, and above "
                 "those, in some species, a capsule. So the first thing a phage touches "
                 "is a forest of sugar.")

    act_one(d)
    cycle_one(d)
    cycle_two(d)
    cycle_three(d)
    cycle_four(d)
    closing_act(d)
    return d



def act_one(d):
    s = d.slide()
    title_bar(s, "California Botanic Garden · 19 May 2026",
              "Five isolates, three strains, two built-in controls")
    rows = [("Strain 1", "8-5-2 · 10-10-2", "99.997 % ANI"),
            ("Strain 2", "9-2-1 · 9-6-2", "100.000 % ANI — the Φ8 host"),
            ("Strain 3", "8-10-2", "a different species")]
    y = Inches(2.35)
    for i, (a, b, c) in enumerate(rows):
        fill = PALE if i == 1 else WHITE
        box(s, MARGIN, y, Inches(6.5), Inches(0.72), fill=fill, line=RULE, radius=False)
        text(s, a, MARGIN + Inches(0.26), y + Inches(0.22), Inches(1.5), size=16,
             color=DARK, bold=True)
        text(s, b, MARGIN + Inches(2.0), y + Inches(0.22), Inches(2.2), size=16, color=MUTED)
        text(s, c, MARGIN + Inches(4.3), y + Inches(0.22), Inches(2.4), size=16, color=MUTED)
        y += Inches(0.78)
    text(s, "Any difference we report between strains has to be bigger than the "
            "difference we can measure within one.",
         MARGIN, y + Inches(0.25), Inches(6.5), size=17, color=DARK, spacing=1.3)
    picture(s, "bactgenomes", MARGIN + Inches(7.0), Inches(2.2), Inches(4.9), Inches(3.6))
    footer(s, "Genomes published in Microbiology Resource Announcements · doi 10.1128/mra.00793-26")
    notes(s, "We collected soil from the California Botanic Garden on the nineteenth of "
             "May. From it we isolated five Pseudomonas strains, and we sequenced all "
             "five genomes — every one of them closed into a complete circle.\n\nThose "
             "five collapse into three distinct strains. That leaves us with two pairs "
             "of near-identical isolates, and we use those pairs as an internal control "
             "all the way through.")

    s = d.slide()
    title_bar(s, "The phage", "And one phage, Φ8, that infects exactly one of the three")
    picture(s, "phagemap", MARGIN, Inches(2.15), CONTENT_W, Inches(2.4))
    stats = [("62,339 bp", "circular"), ("80", "coding sequences"),
             ("no match", "in the phage database"), ("~0", "genes shared with T7")]
    cw = CONTENT_W / 4
    for i, (big, small) in enumerate(stats):
        x = MARGIN + cw * i
        box(s, int(x), Inches(4.85), int(cw - Inches(0.2)), Inches(0.04),
            fill=TEAL, radius=False)
        text(s, big, int(x), Inches(5.0), int(cw - Inches(0.2)), size=26,
             color=TEAL, bold=True)
        text(s, small, int(x), Inches(5.5), int(cw - Inches(0.2)), size=14, color=MUTED)
    text(s, "The architecture is familiar. The sequence isn't.", MARGIN, Inches(6.15),
         CONTENT_W, size=20, color=DARK, font=DISPLAY)
    notes(s, "We also isolated a phage, which we call Phi-8, and it infects exactly one "
             "of the three strains. Sixty-two thousand, three hundred and thirty-nine "
             "base pairs, circular, eighty genes. No match anywhere in the phage "
             "database, and essentially no genes in common with T7. The architecture is "
             "familiar. The sequence isn't.")

    s = d.slide()
    title_bar(s, "The first clue", "The same slot in the genome. Three unrelated cargoes.")
    picture(s, "oantigen", MARGIN, Inches(2.1), CONTENT_W, Inches(2.75))
    trio = [("Strain 1", "15 genes · 17.0 kb", RULE), ("Strain 2 — the host",
             "23 genes · 26.5 kb", TEAL), ("Strain 3", "25 genes · 38.2 kb", RULE)]
    cw2 = (CONTENT_W - Inches(0.6)) / 3
    for i, (t, b, edge) in enumerate(trio):
        x = MARGIN + (cw2 + Inches(0.3)) * i
        box(s, int(x), Inches(5.1), int(cw2), Inches(1.0), fill=WHITE, line=edge)
        text(s, t, int(x + Inches(0.28)), Inches(5.28), int(cw2 - Inches(0.5)),
             size=16, color=TEAL if edge == TEAL else DARK, bold=True)
        text(s, b, int(x + Inches(0.28)), Inches(5.66), int(cw2 - Inches(0.5)),
             size=15, color=MUTED)
    footer(s, "Located with ihfB as the upstream anchor; cassette proteins clustered with "
              "MMseqs2 at ≥ 30 % identity, ≥ 50 % coverage")
    notes(s, "Then we went looking at the locus that builds the sugar coat. We anchored "
             "on the gene that flanks it in Pseudomonas, pulled the cassette out of all "
             "three strains, and clustered every protein in it.\n\nWe found the cassette "
             "sitting in the same slot in all three. The contents are unrelated.")

    s = d.slide()
    title_bar(s, "The first clue",
              "Within a strain, zero variation. Between strains, almost total.")
    picture(s, "clusters", MARGIN, Inches(2.2), Inches(7.0), Inches(3.1))
    bx = MARGIN + Inches(7.5)
    text(s, "4 of 45", bx, Inches(2.3), Inches(4.3), size=40, color=TEAL,
         bold=True, font=DISPLAY)
    text(s, "ortholog clusters shared by all three strains — and all four are generic "
            "sugar chemistry.", bx, Inches(3.0), Inches(4.3), size=16, color=MUTED,
         spacing=1.3)
    box(s, bx, Inches(3.95), Inches(4.3), Inches(0.03), fill=RULE, radius=False)
    text(s, "No shared flippase. No shared polymerase. No shared chain-length regulator.\n"
            "The near-identical pairs inside each strain match at 100 % across every "
            "cassette gene.", bx, Inches(4.15), Inches(4.3), size=16, color=MUTED,
         spacing=1.3)
    text(s, "No database could have told us this: there is no serotype scheme for this "
            "group of species at all.", bx, Inches(5.45), Inches(4.3), size=16,
         color=RUST, bold=True, spacing=1.3)
    notes(s, "Across all three we found forty-five gene clusters — of which only four "
             "are shared by every strain, and all four are generic sugar chemistry. "
             "Meanwhile the near-identical pairs inside each strain match at a hundred "
             "percent.\n\nWe also found that no database could have told us any of this.")

    s = d.slide(bg=TEAL, number=True)
    text(s, "FIRST HYPOTHESIS", MARGIN, Inches(1.9), CONTENT_W, size=14,
         color=RGBColor(0xBF, 0xD8, 0xD5), bold=True)
    text(s, "Three strains, three different sugar coats,\none phage that kills one of "
            "them — so the sugar coat\nmight be one of the main things setting\nwhat Φ8 "
            "can attack.", MARGIN, Inches(2.5), CONTENT_W, size=38,
         color=RGBColor(0xF7, 0xF4, 0xEE), font=DISPLAY, spacing=1.18)
    notes(s, "So: three strains, three different sugar coats, one phage that kills one "
             "of them. That gave us our first hypothesis — that the sugar coat might be "
             "one of the main things setting what Phi-8 can attack.")

def cycle_card(d, n, heading, blurb, note):
    s = d.slide(bg=DARK)
    text(s, f"CYCLE {n} OF 4", MARGIN, Inches(1.75), CONTENT_W, size=14,
         color=LIGHT_TEAL, bold=True)
    text(s, heading, MARGIN, Inches(2.3), CONTENT_W, size=58,
         color=RGBColor(0xF7, 0xF4, 0xEE), font=DISPLAY, spacing=1.05)
    x = MARGIN
    for step in ("Design", "Build", "Test", "Learn"):
        chip = box(s, int(x), Inches(4.25), Inches(1.5), Inches(0.5),
                   fill=RGBColor(0xC8, 0xD8, 0xD4))
        tf = chip.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = step
        r.font.name, r.font.size, r.font.bold = BODY, Pt(15), True
        r.font.color.rgb = TEAL
        x += Inches(1.68)
    text(s, blurb, MARGIN, Inches(5.3), Inches(9.5), size=20,
         color=RGBColor(0xC8, 0xD8, 0xD4), spacing=1.3)
    notes(s, note)


def cycle_one(d):
    cycle_card(d, 1, "The wrong question",
               "We looked for a protein lock. Nine control folds decided the fate of "
               "seven thousand pairs.",
               "Cycle 1 — the wrong question. Retired by its own controls.")

    s = d.slide()
    title_bar(s, "Cycle 1 · Design", "We designed it around the wrong assumption")
    text(s, "The textbook picture of attachment is a receptor-binding protein on the "
            "phage tail meeting a protein on the bacterial surface. Lock and key.",
         MARGIN, Inches(2.5), Inches(6.4), size=20, color=DARK, spacing=1.35)
    text(s, "If you assume that, the obvious move is to work out which binding protein "
            "fits which receptor. So that is what we set out to predict.",
         MARGIN, Inches(3.75), Inches(6.4), size=19, color=MUTED, spacing=1.35)
    box(s, MARGIN, Inches(5.1), Inches(0.05), Inches(1.0), fill=RUST, radius=False)
    text(s, "If we had known the receptor was a sugar,\nwe would never have run this.",
         MARGIN + Inches(0.3), Inches(5.15), Inches(6.1), size=19, color=RUST,
         bold=True, spacing=1.3)
    picture(s, "virion", MARGIN + Inches(7.1), Inches(2.3), Inches(4.5), Inches(3.9))
    footer(s, "Φ8 virion, to scale — AlphaFold3 models run by Prof. J. Cesar Ignacio Espinoza")
    notes(s, "We designed the first cycle around the wrong assumption, and it's worth "
             "saying why it was the reasonable one.\n\nIf we had known the receptor was "
             "a sugar, we would never have run this. We thought it was a protein, so we "
             "went looking for a protein.")

    # BUILD: the funnel
    steps = [
        [("441", "candidate surface receptors annotated across all five isolates")],
        [("441", "candidate surface receptors"),
         ("144", "clusters, after collapsing them")],
        [("441", "candidate surface receptors"),
         ("144", "clusters, after collapsing them"),
         ("114 × 63", "binding proteins against receptors")],
        [("441", "candidate surface receptors"),
         ("144", "clusters, after collapsing them"),
         ("114 × 63", "binding proteins against receptors"),
         ("7,182", "pairs, each folded as a complex and ranked by interface score")],
    ]
    for i, rows in enumerate(steps):
        s = d.slide(morph=(i > 0))
        title_bar(s, "Cycle 1 · Build", "What we built was a screen")
        y = Inches(2.4)
        for j, (big, small) in enumerate(rows):
            last = (j == len(rows) - 1 and i == len(steps) - 1)
            box(s, MARGIN, y, Inches(7.3), Inches(0.92),
                fill=TEAL if last else PALE, radius=True, name=f"!!row{j}")
            text(s, big, MARGIN + Inches(0.4), y + Inches(0.2), Inches(2.3), size=26,
                 color=WHITE if last else TEAL, bold=True, name=f"!!big{j}")
            text(s, small, MARGIN + Inches(3.0), y + Inches(0.3), Inches(4.0), size=15,
                 color=RGBColor(0xC8, 0xD8, 0xD4) if last else MUTED,
                 name=f"!!small{j}")
            y += Inches(1.05)
        if i == len(steps) - 1:
            card(s, MARGIN + Inches(7.9), Inches(2.4), Inches(4.0), Inches(1.95),
                 "Choosing a surrogate host",
                 "The closest match by receptor content had 12 phages on record. A more "
                 "distant relative had 227 entries across 71 phages. We took the one "
                 "with the literature.")
            card(s, MARGIN + Inches(7.9), Inches(4.5), Inches(4.0), Inches(1.75),
                 "Three tools to get it running",
                 "ColabFold — throttled by its alignment server.\n"
                 "Boltz-2 — blocked by the cluster's CUDA version.\n"
                 "ESMFold — the one that ran.")
        notes(s, "What we built was a screen. Four hundred and forty-one candidate "
                 "receptors across all five isolates, collapsed into a hundred and "
                 "forty-four clusters. A hundred and fourteen binding proteins against "
                 "sixty-three receptors — seven thousand, one hundred and eighty-two "
                 "pairs, each folded as a complex on our university's GPU cluster.")

    # BUILD: the controls
    ctrl = [
        ("0.137", "T5's pb-five with FhuA — a real, co-crystallised complex", False),
        ("0.136", "the same receptor, with its sequence scrambled into nonsense", False),
        ("", "", True),
    ]
    for i, (num, blurb, final) in enumerate(ctrl):
        s = d.slide(morph=(i > 0))
        title_bar(s, "Cycle 1 · Test",
                  "We didn't test the screen. We tested whether it could tell\nthe "
                  "difference.", heading_size=28)
        box(s, MARGIN, Inches(2.7), Inches(3.3), Inches(1.9), fill=PALE, name="!!n1")
        text(s, "0.137", MARGIN + Inches(0.3), Inches(3.0), Inches(2.7), size=44,
             color=TEAL, bold=True, font=DISPLAY, name="!!v1")
        text(s, "a real, co-crystallised complex", MARGIN + Inches(0.3), Inches(3.9),
             Inches(2.7), size=14, color=MUTED, name="!!l1")
        if i >= 1:
            box(s, MARGIN + Inches(3.7), Inches(2.7), Inches(3.3), Inches(1.9),
                fill=PALE_RUST, name="!!n2")
            text(s, "0.136", MARGIN + Inches(4.0), Inches(3.0), Inches(2.7), size=44,
                 color=RUST, bold=True, font=DISPLAY, name="!!v2")
            text(s, "the same receptor, scrambled", MARGIN + Inches(4.0), Inches(3.9),
                 Inches(2.7), size=14, color=MUTED, name="!!l2")
        if i >= 2:
            text(s, "One thousandth apart.", MARGIN, Inches(4.95), Inches(7.0),
                 size=28, color=DARK, font=DISPLAY, name="!!gap")
            text(s, "Nine control folds: three pairs known to bind, each rerun "
                    "scrambled and mismatched. None of the real binders separated from "
                    "the controls — and the scores tracked protein length at r = +0.60.",
                 MARGIN, Inches(5.55), Inches(7.0), size=16, color=MUTED, spacing=1.3,
                 name="!!gapbody")
            picture(s, "controls", MARGIN + Inches(7.5), Inches(2.7), Inches(4.3),
                    Inches(3.2), name="!!ctrlfig")
        notes(s, "What we tested wasn't the screen. It was whether the screen could "
                 "tell the difference.\n\nT5's pb-five with FhuA scored zero point one "
                 "three seven. The same receptor, scrambled, scored zero point one "
                 "three six. One thousandth apart.\n\nWe assumed the tool was at fault, "
                 "so we rebuilt it with real evolutionary alignments. It got worse.")

    s = d.slide()
    title_bar(s, "Cycle 1 · Learn",
              "The method cannot answer this question — and we can say why", accent=RUST)
    box(s, MARGIN, Inches(2.3), Inches(6.1), Inches(3.5), fill=WHITE, line=RULE)
    text(s, "On a scrambled receptor", MARGIN + Inches(0.4), Inches(2.6), Inches(5.3),
         size=18, color=DARK, bold=True)
    bars = [("shape score", 0.55, 0.17, TEAL), ("interface score", 0.14, 0.14, RUST)]
    bx = MARGIN + Inches(0.5)
    for name_, before, after, colour in bars:
        for k, val in enumerate((before, after)):
            hgt = Inches(1.6) * val / 0.55
            box(s, int(bx), int(Inches(5.2) - hgt), Inches(0.62), int(hgt),
                fill=colour if k == 0 else RGBColor(0xB8, 0xC9, 0xC6), radius=False)
            text(s, f"{val:.2f}", int(bx - Inches(0.08)), int(Inches(5.2) - hgt - Inches(0.3)),
                 Inches(0.78), size=12, color=DARK, align=PP_ALIGN.CENTER)
            bx += Inches(0.72)
        text(s, name_, int(bx - Inches(1.52)), Inches(5.3), Inches(1.6), size=12,
             color=MUTED, align=PP_ALIGN.CENTER)
        bx += Inches(0.9)
    text(s, "The model could plainly tell the sequence was nonsense. The interface "
            "number barely moved — it had never been reading an interface at all.",
         MARGIN + Inches(0.4), Inches(5.65), Inches(5.3), size=15, color=MUTED,
         spacing=1.3)
    rx = MARGIN + Inches(6.6)
    text(s, "These models don't simulate two proteins touching. They read evolution — "
            "looking across thousands of species for positions that change in step.",
         rx, Inches(2.35), Inches(5.2), size=19, color=DARK, spacing=1.35)
    text(s, "That signal only exists where two proteins have a shared history of "
            "co-adaptation. A phage protein and a bacterial protein have never "
            "co-adapted as a pair.", rx, Inches(3.5), Inches(5.2), size=18,
         color=MUTED, spacing=1.35)
    box(s, rx, Inches(4.75), Inches(5.2), Inches(1.4), fill=RUST)
    text(s, "There is no history to read, so the interface score returns noise.\n"
            "More compute doesn't fix it.", rx + Inches(0.32), Inches(4.98),
         Inches(4.56), size=18, color=RGBColor(0xFB, 0xF3, 0xEE), spacing=1.3)
    footer(s, "Nine control folds decided the fate of seven thousand. We never ran the "
              "real screen.", RUST)
    notes(s, "Two tools, two control gates, both failed. One failure is about your run; "
             "two independent failures are about the method.\n\nWhen we scrambled a "
             "receptor, the shape score collapsed from zero point five five to zero "
             "point one seven. But the interface score barely moved. It had never been "
             "reading an interface at all.\n\nThese models read evolution. That signal "
             "only exists where two proteins have co-adapted. A phage protein and a "
             "bacterial protein never have.")

def cycle_two(d):
    cycle_card(d, 2, "Ask the protein what it is",
               "If we couldn't ask what the tail spike binds, we could ask what it is.",
               "Cycle 2 — geometry instead of docking.")

    s = d.slide()
    title_bar(s, "Cycle 2 · Design and Build",
              "Two readouts that don't share a method")
    card(s, MARGIN, Inches(2.35), Inches(5.7), Inches(1.55), "1 · Sequence",
         "An open-source classifier over all eighty Φ8 proteins, to pick out the "
         "receptor-binding candidates.")
    card(s, MARGIN + Inches(6.13), Inches(2.35), Inches(5.7), Inches(1.55),
         "2 · Geometry",
         "Take every backbone hydrogen bond, measure how far apart in sequence its two "
         "partners sit, and histogram the offsets.")
    trio = [("16–26", "a β-helix peaks at its coil period"),
            ("4", "an α-helix peaks here"),
            ("none", "a β-sandwich has no peak at all")]
    cw = (CONTENT_W - Inches(0.6)) / 3
    for i, (big, small) in enumerate(trio):
        x = MARGIN + (cw + Inches(0.3)) * i
        box(s, int(x), Inches(4.2), int(cw), Inches(1.15), fill=PALE)
        text(s, big, int(x + Inches(0.32)), Inches(4.42), int(cw - Inches(0.6)),
             size=26, color=TEAL, bold=True, font=DISPLAY)
        text(s, small, int(x + Inches(0.32)), Inches(4.9), int(cw - Inches(0.6)),
             size=14, color=MUTED)
    text(s, "We chose that test rather than fell back on it. On a genome with no close "
            "relatives, a database can't contain the answer — and homology annotation "
            "had already missed something here.", MARGIN, Inches(5.65), CONTENT_W,
         size=18, color=DARK, spacing=1.3)
    footer(s, "PhageRBPdetect v4 (ESM-2), open source · the geometry test ships as "
              "phagecheck.betahelix, no database required")
    notes(s, "For the second cycle we changed the question. We built that on two "
             "readouts that don't share a method: an open-source sequence classifier "
             "over all eighty proteins, and then geometry measured directly.\n\n"
             "We chose that test rather than fell back on it.")

    s = d.slide()
    title_bar(s, "Cycle 2 · Test",
              "Eight predicted structures, seven proteins — and the method says no five times",
              heading_size=27)
    picture(s, "folds", MARGIN, Inches(2.0), CONTENT_W, Inches(3.55))
    trio2 = [("CDS 11 — the tail spike",
              "Confidence 0.997, coil period 16–17. A right-handed β-helix.", TEAL),
             ("CDS 24 — filed as “hypothetical”",
              "Confidence 0.998 on a different period. A second depolymerase the "
              "annotation had missed.", TEAL),
             ("Five turned down",
              "An α-helical fibre lands at six. The method says no — which is what "
              "makes it worth believing when it says yes.", RUST)]
    cw2 = (CONTENT_W - Inches(0.6)) / 3
    for i, (t, b, colour) in enumerate(trio2):
        x = MARGIN + (cw2 + Inches(0.3)) * i
        box(s, int(x), Inches(5.75), int(cw2 - Inches(0.2)), Inches(0.035),
            fill=colour, radius=False)
        text(s, t, int(x), Inches(5.88), int(cw2 - Inches(0.2)), size=15,
             color=colour, bold=True)
        text(s, b, int(x), Inches(6.25), int(cw2 - Inches(0.2)), size=13,
             color=MUTED, spacing=1.25)
    notes(s, "What we tested was eight predicted structures covering seven proteins, "
             "and we classified each from its own backbone geometry.\n\nFive of the "
             "seven came back negative. The method says no, which is what makes it "
             "worth believing when it says yes.\n\nIt said yes twice: the tail spike, "
             "and CDS 24, which the annotation had filed as hypothetical.")

    # BUILD: strip the tail spike down to the enzyme
    strip = [
        ("trimer", "The tail spike, whole",
         "CDS 11 is nine hundred and forty-one residues, and it hangs off the virion "
         "base.", None),
        ("trimer", "Most of it isn't the enzyme",
         "The first hundred and ten residues anchor it. The next two hundred are a "
         "shaft that moves between every model we ran.", "anchor"),
        ("body-side", "The rigid trimeric body",
         "From residue three hundred to the end — agreeing between models to within "
         "one ångström. This is the part that carries the chemistry.", None),
        ("body-axial", "Down the three-fold axis",
         "A long triangular prism with a groove running its length: the signature of "
         "an enzyme that cuts a sugar chain.", "part"),
    ]
    for i, (img, head, blurb, flag) in enumerate(strip):
        s = d.slide(morph=(i > 0))
        title_bar(s, "Cycle 2 · What the fold is",
                  "The same protein, looked at four ways")
        picture(s, img, MARGIN + Inches(0.6), Inches(2.05), Inches(4.6), Inches(4.5),
                name="!!spine")
        tx = MARGIN + Inches(6.0)
        text(s, head, tx, Inches(2.5), Inches(5.8), size=28, color=DARK,
             font=DISPLAY, name="!!spine-head")
        text(s, blurb, tx, Inches(3.3), Inches(5.6), size=19, color=MUTED,
             spacing=1.35, name="!!spine-body")
        if flag == "anchor":
            box(s, tx, Inches(4.7), Inches(0.05), Inches(0.95), fill=RUST, radius=False)
            text(s, "Calx-β anchor · residues 1–110\nShaft · residues 111–300",
                 tx + Inches(0.3), Inches(4.75), Inches(5.3), size=17, color=RUST,
                 spacing=1.3)
        if flag == "part":
            box(s, tx, Inches(4.9), Inches(5.6), Inches(1.15), fill=PALE)
            text(s, "Residues 305–941 → BBa_26DKNAEC", tx + Inches(0.32), Inches(5.1),
                 Inches(5.0), size=18, color=TEAL, bold=True)
            text(s, "The fragment we expressed, and the one we submitted to the Registry.",
                 tx + Inches(0.32), Inches(5.52), Inches(5.0), size=14, color=MUTED)
        notes(s, "CDS 11 is nine hundred and forty-one residues and most of it isn't "
                 "the enzyme. The first hundred and ten anchor it to the virion, and "
                 "the next two hundred are a shaft that moves between every model we "
                 "ran. The rigid trimeric body — from residue three hundred to the end "
                 "— is the part that carries the chemistry.")

    s = d.slide()
    title_bar(s, "Cycle 2 · Learn", "The fold is a signature, and it names the receptor",
              accent=RUST)
    picture(s, "body-axial", MARGIN + Inches(0.4), Inches(2.1), Inches(4.2), Inches(4.1))
    tx = MARGIN + Inches(5.4)
    text(s, "Enzymes that chew through long sugar chains look like this, because a "
            "sugar chain is a thread and you need something that holds it straight "
            "while you cut.", tx, Inches(2.3), Inches(6.4), size=20, color=DARK,
         spacing=1.35)
    text(s, "You can recognise a wood plane by its shape without being told what it cuts.",
         tx, Inches(3.65), Inches(6.4), size=19, color=MUTED, spacing=1.35)
    box(s, tx, Inches(4.5), Inches(6.4), Inches(1.6), fill=TEAL)
    text(s, "So the tail spike isn't a key. It's a blade.", tx + Inches(0.35),
         Inches(4.75), Inches(5.7), size=25, color=RGBColor(0xF7, 0xF4, 0xEE),
         font=DISPLAY)
    text(s, "And the lock we had spent months looking for doesn't exist.",
         tx + Inches(0.35), Inches(5.42), Inches(5.7), size=16,
         color=RGBColor(0xC8, 0xD8, 0xD4))
    footer(s, "Our classifier flagged it, and our PI reached the same conclusion from "
              "his own structural search. Between us, we turned it into a hypothesis.")
    notes(s, "That shape is a signature. Enzymes that chew through long sugar chains "
             "look like this. You can recognise a wood plane by its shape without being "
             "told what it cuts.\n\nSo the tail spike isn't a key. It's a blade — and "
             "the lock we had spent months looking for doesn't exist.")

    s = d.slide(bg=TEAL)
    text(s, "THE CENTRAL HYPOTHESIS", MARGIN, Inches(1.55), CONTENT_W, size=14,
         color=RGBColor(0xBF, 0xD8, 0xD5), bold=True)
    text(s, "In bacteria that wrap themselves in sugar, the ceiling\non host range is "
            "set by what the depolymerase can digest —\nnot by which protein the tail "
            "binds.", MARGIN, Inches(2.15), CONTENT_W, size=34,
         color=RGBColor(0xF7, 0xF4, 0xEE), font=DISPLAY, spacing=1.2)
    text(s, "And the narrow specificity we see today is a narrowed-down version of "
            "something broader further back.", MARGIN, Inches(4.5), Inches(10.5),
         size=22, color=RGBColor(0xC8, 0xD8, 0xD4), spacing=1.3)
    footer(s, "Developed jointly with Prof. J. Cesar Ignacio Espinoza",
           RGBColor(0xBF, 0xD8, 0xD5))
    notes(s, "In bacteria that wrap themselves in sugar, the ceiling on host range is "
             "set by what the depolymerase can digest — not by which protein the tail "
             "binds. And the narrow specificity we see today is a narrowed-down version "
             "of something broader further back.")

    s = d.slide()
    title_bar(s, "A prediction we can falsify",
              "If the tail spike reads Strain 2's sugar, Φ8 should fail on the other two")
    rows = [("9-2-1 · 9-6-2", "Strain 2", "hosts of record", "infects", True),
            ("10-10-2", "Strain 1", "no plaques", "does not infect", False),
            ("8-10-2", "Strain 3", "no plaques", "does not infect", False)]
    y = Inches(2.45)
    for a, b, c, e, hi in rows:
        box(s, MARGIN, y, Inches(7.1), Inches(0.68), fill=PALE if hi else WHITE,
            line=RULE, radius=False)
        for txt, dx, w_ in ((a, 0.26, 2.0), (b, 2.3, 1.5), (c, 3.9, 1.9), (e, 5.6, 1.6)):
            text(s, txt, MARGIN + Inches(dx), y + Inches(0.2), Inches(w_), size=15,
                 color=DARK if txt in (a,) else MUTED)
        y += Inches(0.74)
    text(s, "Eighteen host isolates spotted against two pooled lysates, July 2026. "
            "That is the direction the prediction makes.", MARGIN, y + Inches(0.2),
         Inches(7.1), size=16, color=MUTED, spacing=1.3)
    box(s, MARGIN + Inches(7.6), Inches(2.45), Inches(4.2), Inches(3.0), fill=PALE_RUST)
    text(s, "Why we aren't calling it confirmed", MARGIN + Inches(7.95), Inches(2.72),
         Inches(3.5), size=17, color=RUST, bold=True)
    text(s, "No no-phage control — a margin note on the page says only “need control”.\n"
            "One isolate was never scored.\n"
            "Two follow-up readouts were never written down.",
         MARGIN + Inches(7.95), Inches(3.25), Inches(3.5), size=15, color=DARK,
         spacing=1.35)
    text(s, "All three come from our own notebook, not from a reviewer.",
         MARGIN + Inches(7.95), Inches(4.85), Inches(3.5), size=14, color=MUTED)
    notes(s, "That hypothesis makes a prediction we can falsify. We tested that in "
             "July. The Strain 1 and Strain 3 representatives came back negative "
             "against both lysates.\n\nWe're not calling it confirmed, and the reasons "
             "come from our own notebook rather than from a reviewer.")

def cycle_three(d):
    cycle_card(d, 3, "Build the enzymes",
               "Two lines run through this cycle, and they are two different proteins.",
               "Cycle 3 — build the enzymes. Two lines.")

    # BUILD: the two enzymes side by side
    for i in range(2):
        s = d.slide(morph=(i > 0))
        title_bar(s, "Cycle 3 · Two lines, two proteins",
                  "The enzyme that reads the receptor — and the one we rebuilt ancestors of",
                  heading_size=27)
        if i == 0:
            picture(s, "body-side", MARGIN + Inches(3.6), Inches(2.1), Inches(4.6),
                    Inches(4.2), name="!!left")
            text(s, "CDS 11 — the tail spike", MARGIN + Inches(3.6), Inches(6.35),
                 Inches(4.6), size=20, color=TEAL, bold=True, align=PP_ALIGN.CENTER,
                 name="!!leftlab")
        else:
            picture(s, "body-side", MARGIN + Inches(0.3), Inches(2.1), Inches(4.2),
                    Inches(3.5), name="!!left")
            text(s, "CDS 11 — the tail spike", MARGIN + Inches(0.3), Inches(5.7),
                 Inches(4.2), size=18, color=TEAL, bold=True, align=PP_ALIGN.CENTER,
                 name="!!leftlab")
            text(s, "A right-handed β-helix, 941 residues, attached to the virion.\n"
                    "This is the one that reads the host surface.",
                 MARGIN + Inches(0.3), Inches(6.1), Inches(4.2), size=14, color=MUTED,
                 align=PP_ALIGN.CENTER, spacing=1.3)
            picture(s, "gh5", MARGIN + Inches(6.3), Inches(2.4), Inches(4.8),
                    Inches(2.9), name="!!right")
            text(s, "CDS 12 — a GH5 hydrolase", MARGIN + Inches(6.3), Inches(5.5),
                 Inches(4.8), size=18, color=RUST, bold=True, align=PP_ALIGN.CENTER)
            text(s, "A TIM barrel, not a β-helix. Its closest structural match is an "
                    "endoglucanase caught with a short cellulose chain.\n"
                    "A separate protein — not a domain of the tail spike.",
                 MARGIN + Inches(6.3), Inches(5.9), Inches(4.8), size=14, color=MUTED,
                 align=PP_ALIGN.CENTER, spacing=1.3)
        notes(s, "Two enzymes sit in the tail module. CDS 11, the beta-helix, is the "
                 "one that reads the host surface. And next to it CDS 12, a glycoside "
                 "hydrolase from family five — a TIM barrel, not a beta-helix, whose "
                 "closest structural match is an endoglucanase caught with a short "
                 "cellulose chain. It is a separate protein, not a domain of the tail "
                 "spike, and we have not established what it does inside the phage.")

    s = d.slide()
    title_bar(s, "The question a judge will ask",
              "So why reconstruct ancestors of that one, and not of the tail spike?",
              accent=RUST)
    reasons = [("A tree to reconstruct along",
                "CDS 12 has a thousand homologues in the databases. The tail spike is "
                "novel enough that we had no such tree."),
               ("A third of the size",
                "362 residues against 941. We judged it the far better bet to express."),
               ("A synthesis allowance",
                "Four short constructs were affordable inside our sponsored allowance. "
                "Four long ones were not.")]
    cw = (CONTENT_W - Inches(0.6)) / 3
    for i, (t, b) in enumerate(reasons):
        x = MARGIN + (cw + Inches(0.3)) * i
        card(s, int(x), Inches(2.4), int(cw), Inches(1.85), t, b)
    box(s, MARGIN, Inches(4.6), CONTENT_W, Inches(1.95), fill=RUST)
    text(s, "So the ancestral panel tests the shape of the hypothesis — whether an "
            "ancestral glycoside hydrolase has a broader substrate range than its "
            "descendant — on an enzyme we could actually build, rather than on the one "
            "that reads the receptor.", MARGIN + Inches(0.4), Inches(4.85),
         CONTENT_W - Inches(0.8), size=19, color=RGBColor(0xFB, 0xF3, 0xEE), spacing=1.3)
    text(s, "That's a real limitation, and it's ours, not a reviewer's.",
         MARGIN + Inches(0.4), Inches(6.05), CONTENT_W - Inches(0.8), size=17,
         color=RGBColor(0xF3, 0xD6, 0xC8))
    notes(s, "So why did we reconstruct ancestors of that one, rather than of the tail "
             "spike? Three reasons, and none of them is that we got confused. CDS 12 "
             "has a thousand homologues in the databases. CDS 12 is a third of the "
             "size. And we were working inside a sponsored synthesis allowance, where "
             "four short constructs were affordable and four long ones were not.\n\n"
             "That's a real limitation, and it's ours, not a reviewer's.")

    # BUILD: the ancestors appear one at a time
    anc = [("anc-wt", "CDS 12, the modern enzyme", "The GH5 as Φ8 carries it today."),
           ("anc-n1", "Node 1", "78 % identical to the modern enzyme — the closest of the three."),
           ("anc-n40", "Node 40", "53 % identical to the modern enzyme, 87 % to Node 281."),
           ("anc-n281", "Node 281", "51 % identical to the modern enzyme, 87 % to Node 40.")]
    slots = [(MARGIN + Inches(0.1), Inches(2.3)), (MARGIN + Inches(3.1), Inches(2.3)),
             (MARGIN + Inches(6.1), Inches(2.3)), (MARGIN + Inches(9.1), Inches(2.3))]
    for i in range(4):
        s = d.slide(morph=(i > 0))
        title_bar(s, "Cycle 3 · Build",
                  "Walking back up the tree, one node at a time")
        for j in range(i + 1):
            key, head, blurb = anc[j]
            x, y = slots[j]
            picture(s, key, int(x), int(y), Inches(2.75), Inches(2.0), name=f"!!anc{j}")
            text(s, head, int(x), Inches(4.45), Inches(2.75), size=16,
                 color=TEAL if j else DARK, bold=True, align=PP_ALIGN.CENTER,
                 name=f"!!anchead{j}")
            text(s, blurb, int(x), Inches(4.82), Inches(2.75), size=13, color=MUTED,
                 align=PP_ALIGN.CENTER, spacing=1.3, name=f"!!ancbody{j}")
        if i == 3:
            text(s, "Our PI ran the alignment, the tree and the reconstruction on "
                    "sequences we prepared — every node on the path from CDS 12 back "
                    "to the root, 998 of them. We picked three to order as DNA.",
                 MARGIN, Inches(6.0), CONTENT_W, size=18, color=DARK, spacing=1.3)
        notes(s, "We worked out the direction with our PI, and he ran the alignment, "
                 "the tree and the reconstruction on sequences we prepared. He "
                 "reconstructed every node on the path from CDS 12 back to the root, "
                 "and we picked three of them to order as DNA.")

    s = d.slide(morph=True)
    title_bar(s, "Cycle 3 · Build", "All four fold to the same TIM barrel")
    picture(s, "anc-overlay", MARGIN + Inches(0.4), Inches(2.1), Inches(5.6),
            Inches(4.2), name="!!anc0")
    tx = MARGIN + Inches(6.6)
    trio = [("6", "parts published on the Registry, under CC0"),
            ("3", "of them reconstructed ancestors — sequences that exist nowhere in nature"),
            ("998", "nodes reconstructed in total")]
    y = Inches(2.3)
    for big, small in trio:
        box(s, tx, y, Inches(5.2), Inches(0.95), fill=PALE)
        text(s, big, tx + Inches(0.32), y + Inches(0.22), Inches(1.1), size=26,
             color=TEAL, bold=True, font=DISPLAY)
        text(s, small, tx + Inches(1.6), y + Inches(0.26), Inches(3.3), size=14,
             color=MUTED, spacing=1.25)
        y += Inches(1.08)
    box(s, tx, Inches(5.65), Inches(5.2), Inches(1.15), fill=PALE_RUST)
    text(s, "One warning we'd pass on: our first order was codon-optimised and our "
            "second wasn't. In an E. coli host that bias is the first thing to suspect "
            "when a band doesn't appear.", tx + Inches(0.32), Inches(5.85),
         Inches(4.56), size=14, color=DARK, spacing=1.3)
    notes(s, "All six went into pET-28a with an N-terminal His-tag and were "
             "synthesised by Twist across two orders, and all six are now published "
             "basic parts on the iGEM Registry under a CC0 licence. Three of the six "
             "are those reconstructed ancestors — protein sequences that exist nowhere "
             "in nature.\n\nOne warning we'd pass on, because it cost us: our first "
             "order was codon-optimised and our second wasn't.")

    s = d.slide()
    title_bar(s, "Cycle 3 · What the model said, and its own control",
              "Along the path to the root, the score improves steadily",
              heading_size=28)
    picture(s, "zymctrl", MARGIN, Inches(2.15), Inches(6.8), Inches(3.9))
    tx = MARGIN + Inches(7.3)
    text(s, "Scored against twenty-four glycoside-hydrolase classes, the label the "
            "model likes best is endo-1,4-β-glucanase — the same chemistry the "
            "structure points at.", tx, Inches(2.25), Inches(4.5), size=17,
         color=DARK, spacing=1.35)
    box(s, tx, Inches(3.6), Inches(4.5), Inches(2.1), fill=PALE_RUST)
    text(s, "Except it doesn't survive its own control", tx + Inches(0.3), Inches(3.8),
         Inches(3.9), size=16, color=RUST, bold=True)
    text(s, "A reconstructed ancestor is consensus-like by construction, so it scores "
            "better under almost any label — and it does, in 21 of the 24 classes. "
            "Direction alone proves nothing.", tx + Inches(0.3), Inches(4.2),
         Inches(3.9), size=14, color=DARK, spacing=1.3)
    text(s, "And perplexity isn't activity. Nothing here measures substrate range — "
            "which is the whole point of the panel.", tx, Inches(5.95), Inches(4.5),
         size=16, color=DARK, bold=True, spacing=1.3)
    notes(s, "Before any of them reached a bench, we asked a model what it thought. "
             "The label it likes best is endo-one-four-beta-glucanase — the same "
             "chemistry the structure points at. And along the path to the root the "
             "score improves steadily.\n\nExcept that it doesn't survive its own "
             "control. A reconstructed ancestor is consensus-like by construction, so "
             "it scores better under almost any label — and it does, in twenty-one of "
             "the twenty-four classes. Direction alone proves nothing.\n\nAnd "
             "perplexity isn't activity.")

    s = d.slide()
    title_bar(s, "Cycle 3 · Test", "Four rounds at the bench, and they didn't line up neatly")
    rounds = [("15 Sep", "Two gels, four constructs, induced against uninduced — no "
               "detectable induction on either. The tail spike lane essentially blank.", WHITE),
              ("29 Sep", "CDS 12 gives the first induction-dependent band at the right size.", PALE),
              ("1 Oct", "Nickel columns on six constructs. The first ancestor eluted at "
               "its predicted mass — the only construct that did. The tail spike eluted "
               "something, 29 kDa short.", PALE),
              ("10 Oct", "Same column, second ancestor. Both elutions blank; the load "
               "and the flow-through carried the same band.", PALE_RUST)]
    y = Inches(2.3)
    for when, what, fill in rounds:
        box(s, MARGIN, y, Inches(7.0), Inches(0.92), fill=fill, line=RULE, radius=False)
        text(s, when, MARGIN + Inches(0.26), y + Inches(0.28), Inches(1.1), size=15,
             color=DARK, bold=True)
        text(s, what, MARGIN + Inches(1.5), y + Inches(0.16), Inches(5.3), size=13,
             color=MUTED, spacing=1.25)
        y += Inches(0.98)
    picture(s, "gel0929", MARGIN + Inches(7.5), Inches(2.3), Inches(4.3), Inches(1.75))
    picture(s, "gel1010", MARGIN + Inches(7.5), Inches(4.2), Inches(4.3), Inches(1.75))
    footer(s, "Empty-vector BL21 lane: absent in all eight protein assays", RUST)
    notes(s, "We tested expression four times, and the rounds didn't line up neatly.\n\n"
             "On October the first we ran nickel columns on six constructs, and one of "
             "them worked: the first ancestor eluted at its predicted mass, the only "
             "construct that did. The tail spike eluted something too, but twenty-nine "
             "kilodaltons short.\n\nOn October the tenth both elutions came off blank. "
             "We read that as a purification we had botched, and we were about to spend "
             "another week on it.")

    s = d.slide()
    title_bar(s, "Cycle 3 · Learn — human practices",
              "What stopped us wasn't an experiment. It was a conversation.", accent=RUST)
    box(s, MARGIN, Inches(2.3), Inches(0.06), Inches(1.55), fill=TEAL, radius=False)
    text(s, "He changed the question. Not why is nothing eluting, but is there anything "
            "there to elute.", MARGIN + Inches(0.35), Inches(2.4), Inches(6.3),
         size=20, color=DARK, italic=True, spacing=1.3)
    text(s, "Prof. Ilya Tolstorukov, Keck Graduate Institute · 13 October 2026. He wrote "
            "back before we met to say expression was his field and purification wasn't "
            "— and met us anyway.", MARGIN + Inches(0.35), Inches(3.3), Inches(6.3),
         size=14, color=MUTED, spacing=1.3)
    text(s, "Check whether the protein is being made at all — an anti-His dot blot — "
            "before touching the column again. Run uninduced controls. Standardise what "
            "goes onto a membrane before comparing spots on it.",
         MARGIN, Inches(4.2), Inches(6.6), size=16, color=DARK, spacing=1.35)
    box(s, MARGIN, Inches(5.4), Inches(6.6), Inches(1.3), fill=TEAL)
    text(s, "Six days later: the flow-through read 2.9× the negative control.",
         MARGIN + Inches(0.35), Inches(5.6), Inches(5.9), size=19,
         color=RGBColor(0xF7, 0xF4, 0xEE), spacing=1.25)
    text(s, "The protein had been there all along. The run failed at capture — not at "
            "expression.", MARGIN + Inches(0.35), Inches(6.18), Inches(5.9), size=14,
         color=RGBColor(0xC8, 0xD8, 0xD4))
    picture(s, "dotblot", MARGIN + Inches(7.1), Inches(2.4), Inches(4.7), Inches(2.3))
    text(s, "A gel can't tell them apart: no expression, insoluble protein, and a "
            "column that didn't bind all look identical. One cheap assay separates "
            "them — and pointed our fix at the column instead of the construct.",
         MARGIN + Inches(7.1), Inches(4.9), Inches(4.7), size=15, color=MUTED,
         spacing=1.3)
    footer(s, "We debugged the last step of a workflow for a week without checking the "
              "first step worked. One meeting fixed it.")
    notes(s, "What stopped us wasn't an experiment. It was a conversation.\n\nHe "
             "changed the question. Not why is nothing eluting, but is there anything "
             "there to elute.\n\nSix days later we ran that blot, and the flow-through "
             "from the second ancestor read two point nine times the negative control. "
             "The protein had been there all along. The run had failed at capture — not "
             "at expression.\n\nWe had spent a week debugging the last step of a "
             "workflow without checking that the first step worked. That's the "
             "generalisable mistake, and one meeting fixed it.")

    s = d.slide()
    title_bar(s, "Cycle 3 · The assay the whole project points at",
              "Does an enzyme, on its own, do anything to the sugar?")
    picture(s, "spottest", MARGIN, Inches(2.2), Inches(6.5), Inches(3.4))
    tx = MARGIN + Inches(7.1)
    for i, (big, small) in enumerate([("12 %", "median colony count under the first "
                                       "ancestor, against the plate's PBS control"),
                                      ("0 %", "Φ8's own median, over the same seven strains")]):
        x = tx + Inches(2.45) * i
        box(s, int(x), Inches(2.25), Inches(2.25), Inches(1.5), fill=PALE)
        text(s, big, int(x + Inches(0.28)), Inches(2.45), Inches(1.7), size=28,
             color=TEAL, bold=True, font=DISPLAY)
        text(s, small, int(x + Inches(0.28)), Inches(2.95), Inches(1.7), size=12,
             color=MUTED, spacing=1.25)
    text(s, "No visible lysis on any plate — including Φ8 on its own hosts — so the "
            "assay was never reading clearing. Counting colonies inside the drops gives "
            "a number.", tx, Inches(3.95), Inches(4.7), size=15, color=MUTED, spacing=1.3)
    box(s, tx, Inches(4.9), Inches(4.7), Inches(1.65), fill=PALE_RUST)
    text(s, "Our PI reads that as enzyme activity. Before we call it that ourselves:",
         tx + Inches(0.3), Inches(5.08), Inches(4.1), size=14, color=RUST, bold=True)
    text(s, "The carry-over control was not run.\nThose dilutions later read at or below "
            "our own dot blot's detection floor.", tx + Inches(0.3), Inches(5.5),
         Inches(4.1), size=13, color=DARK, spacing=1.3)
    footer(s, "The strongest activity signal we have — and it is one plate.")
    notes(s, "Then we ran the assay the whole project points at: does an enzyme, on its "
             "own, do anything to the sugar?\n\nUnder the first ancestor, across seven "
             "strains, colony counts fall to a median of twelve percent of the plate's "
             "PBS control. Phi-8's own median is zero.\n\nOur PI reads that suppression "
             "as enzyme activity. We'd want more before we call it that ourselves, and "
             "there are two specific gaps.\n\nIt's the strongest activity signal we "
             "have, and it is one plate.")

    s = d.slide(bg=RUST)
    text(s, "ONE GAP RUNS THROUGH ALL OF IT", MARGIN, Inches(2.0), CONTENT_W, size=14,
         color=RGBColor(0xF3, 0xD6, 0xC8), bold=True)
    text(s, "Eight protein assays — seven gels and a dot blot —\nand not one of them "
            "carries a lane of untransformed BL21.", MARGIN, Inches(2.6), CONTENT_W,
         size=36, color=RGBColor(0xFB, 0xF3, 0xEE), font=DISPLAY, spacing=1.2)
    text(s, "We designed every round around a different variable instead.\nThat control "
            "is on the bench now.", MARGIN, Inches(4.7), Inches(10), size=20,
         color=RGBColor(0xF3, 0xD6, 0xC8), spacing=1.3)
    notes(s, "And one gap runs through all of it. We have now run eight protein assays "
             "— seven gels and a dot blot — and not one of them carries a lane of "
             "untransformed BL21. We designed every round around a different variable "
             "instead. That control is on the bench now.")

def cycle_four(d):
    cycle_card(d, 4, "Let the bacteria answer",
               "Three cycles in, every guess about the receptor had come from the "
               "phage's side. No structure prediction anywhere in this loop.",
               "Cycle 4 — selection instead of prediction.")

    s = d.slide()
    title_bar(s, "Cycle 4 · Design and Test",
              "Seventy candidate sites, checked against the raw reads. One survived.")
    text(s, "In July we picked colonies from inside the plaque zone — cells still "
            "growing where the phage should have killed them — and in October we "
            "sequenced one from each host against its parent.",
         MARGIN, Inches(2.35), Inches(6.7), size=18, color=DARK, spacing=1.35)
    text(s, "Both picks were the parent strain, intact, with no phage sequence in them, "
            "so neither had simply become a lysogen. A naive assembly comparison gave "
            "sixteen to twenty-one differing sites — which means nothing on its own, "
            "because two sequencing runs of the same clone already differ by more.",
         MARGIN, Inches(3.6), Inches(6.7), size=16, color=MUTED, spacing=1.35)
    for i, (big, small) in enumerate([("263 / 264", "mutant reads carry the change"),
                                      ("0 / 658", "parent and other-pick reads do")]):
        x = MARGIN + Inches(3.5) * i
        box(s, int(x), Inches(5.1), Inches(3.2), Inches(1.0), fill=PALE)
        text(s, big, int(x + Inches(0.3)), Inches(5.28), Inches(2.6), size=24,
             color=TEAL, bold=True, font=DISPLAY)
        text(s, small, int(x + Inches(0.3)), Inches(5.72), Inches(2.6), size=13,
             color=MUTED)
    text(s, "A missense change in a Stealth-family sugar phosphotransferase, inside a "
            "30 kb cluster that builds and exports capsular polysaccharide. The other "
            "pick has no confirmed mutation at all.", MARGIN, Inches(6.3),
         Inches(6.7), size=15, color=DARK, spacing=1.3)
    picture(s, "mutation", MARGIN + Inches(7.2), Inches(2.9), Inches(4.6), Inches(3.0))
    notes(s, "For the fourth cycle we stopped asking the phage, and asked the "
             "bacteria.\n\nWe took every candidate back to the raw reads: seventy "
             "sites, checked against the parent's reads and against an independent read "
             "set with completely different chemistry.\n\nExactly one survived. A "
             "missense change in a Stealth-family sugar phosphotransferase, inside a "
             "thirty-kilobase cluster that builds and exports capsular polysaccharide.")

    # BUILD: the capsule hides an intact O-antigen
    mask = [("Cycle 2 said the receptor is a sugar",
             "The tail spike's fold points at the O-antigen — the long chains anchored "
             "in the outer membrane.", 2),
            ("Cycle 4 agrees, and disagrees about which one",
             "The one confirmed mutation sits in the capsule cluster, with the "
             "O-antigen cassette intact.", 3),
            ("Both can be true at once",
             "A capsule sits on top and can hide an intact O-antigen underneath it. We "
             "don't know which surface Φ8 reads — so wherever the distinction matters "
             "we say surface polysaccharide and leave it there.", 3)]
    for i, (head, blurb, stage) in enumerate(mask):
        s = d.slide(morph=(i > 0))
        title_bar(s, "Cycle 4 · Learn",
                  "It disagrees with Cycle 2 — which is the whole reason we did it this "
                  "way round", accent=RUST, heading_size=28)
        envelope(s, stage, MARGIN + Inches(0.5), Inches(2.3), Inches(6.2), Inches(3.7))
        tx = MARGIN + Inches(7.5)
        text(s, head, tx, Inches(2.6), Inches(4.4), size=24, color=DARK,
             font=DISPLAY, spacing=1.15, name="!!mask-head")
        text(s, blurb, tx, Inches(3.9), Inches(4.4), size=17, color=MUTED,
             spacing=1.35, name="!!mask-body")
        if i == 2:
            footer(s, "The honest gap: we never confirmed those colonies were "
                      "resistant. They were colonies in a plaque zone, which is "
                      "suggestive and isn't the same thing.", RUST)
        notes(s, "What we learned disagrees with Cycle 2 — which is the whole reason "
                 "we did it this way round. Cycle 2 told us the receptor is a sugar. "
                 "Cycle 4 agrees it's a sugar, and disagrees about which one: it points "
                 "at the capsule, with the O-antigen cassette intact.\n\nBoth can be "
                 "true at once, because a capsule sits on top and can hide an intact "
                 "O-antigen underneath it.\n\nAnd the honest gap: we never confirmed "
                 "those colonies were resistant.")


def closing_act(d):
    s = d.slide()
    title_bar(s, "Contribution",
              "Four things we're leaving behind — one of them is a failure")
    items = [("Two packaged tools",
              "MIT licensed, on iGEM's GitLab. Gel densitometry — we re-typed that code "
              "three times before generalising it. And the fold test from Cycle 2, "
              "which also told a terminal repeat from a circular join and changed our "
              "own answer: this wiki used to say the genome was linear.", TEAL, WHITE),
             ("Six registered parts",
              "Published under CC0 — three of them sequences that never existed, "
              "reconstructed from an alignment and a tree and ordered as DNA.", TEAL, WHITE),
             ("A benchmark",
              "On a genome with no close relatives, a machine-learning classifier found "
              "a depolymerase that homology annotation had filed as hypothetical. For "
              "novel phage genomes: run both, and reconcile the disagreements.", TEAL, WHITE),
             ("The screen that failed",
              "Published with the controls that caught it and the reason it could never "
              "have worked. Don't use interface scores to screen phage–host protein "
              "pairs, and run a positive control with a solved co-structure before you "
              "scale to thousands.", RGBColor(0xF3, 0xD6, 0xC8), RUST)]
    cw = (CONTENT_W - Inches(0.4)) / 2
    for i, (t, b, tc, fill) in enumerate(items):
        x = MARGIN + (cw + Inches(0.4)) * (i % 2)
        y = Inches(2.3) + Inches(2.15) * (i // 2)
        box(s, int(x), int(y), int(cw), Inches(1.95), fill=fill,
            line=RULE if fill == WHITE else None)
        text(s, t, int(x + Inches(0.34)), int(y + Inches(0.24)), int(cw - Inches(0.7)),
             size=18, color=tc, bold=True)
        text(s, b, int(x + Inches(0.34)), int(y + Inches(0.68)), int(cw - Inches(0.7)),
             size=13, color=MUTED if fill == WHITE else RGBColor(0xFB, 0xF3, 0xEE),
             spacing=1.3)
    notes(s, "We're leaving four things behind, and one of them is a failure.\n\n"
             "Two packaged tools, MIT licensed, on iGEM's GitLab. Six parts on the "
             "Registry, three of them sequences that never existed. A benchmark. And "
             "the screen that failed, published with the controls that caught it.")

    s = d.slide()
    title_bar(s, "Human practices · California Botanic Garden · 19 October 2026",
              "We went back and asked whether any of this would be useful.\nMost of "
              "what we'd assumed was wrong.", heading_size=28)
    panels = [("We expected to argue for biological control",
               "We didn't have to. They already suppress soil fungi by mulching.",
               WHITE, MUTED, DARK),
              ("We expected the objection to be ecological risk",
               "It was whether the thing works. Copper on every blossom every four or "
               "five days, 86 acres, eight staff. The objection is arithmetic.",
               WHITE, MUTED, DARK),
              ("The finding that costs us most",
               "They have never had a sample come back positive for Pseudomonas. We "
               "isolated a soil phage and its environmental host — not a treatment for "
               "a disease this stakeholder has.",
               RUST, RGBColor(0xF3, 0xD6, 0xC8), RGBColor(0xFB, 0xF3, 0xEE))]
    cw = (CONTENT_W - Inches(0.6)) / 3
    for i, (t, b, fill, tc, bc) in enumerate(panels):
        x = MARGIN + (cw + Inches(0.3)) * i
        box(s, int(x), Inches(2.75), int(cw), Inches(2.3), fill=fill,
            line=RULE if fill == WHITE else None)
        text(s, t, int(x + Inches(0.3)), Inches(2.98), int(cw - Inches(0.6)), size=15,
             color=tc, bold=True, spacing=1.25)
        text(s, b, int(x + Inches(0.3)), Inches(3.68), int(cw - Inches(0.6)), size=14,
             color=bc, spacing=1.3)
    text(s, "What they do need is something for bacteria inside the vascular system, "
            "where nothing they have reaches. Our strain doesn't solve that — but the "
            "question we worked on is the one you'd have to answer first.",
         MARGIN, Inches(5.35), CONTENT_W, size=18, color=DARK, spacing=1.3)
    text(s, "The strain is local. The question isn't.", MARGIN, Inches(6.25),
         CONTENT_W, size=22, color=TEAL, font=DISPLAY)
    footer(s, "Ashley Armstrong and James Manifold · recorded and used with permission · "
              "INTERVIEW CLIPS GO HERE")
    notes(s, "Two days before our wiki froze, we went back to the garden the soil came "
             "from, and asked the people who manage it whether a treatment as "
             "strain-specific as ours would be any use to them.\n\nWe found that most "
             "of what we had assumed was wrong.\n\nAnd here's the finding that costs us "
             "most. They have never had a sample come back positive for Pseudomonas.\n\n"
             "[PLACE THE INTERVIEW CLIPS HERE — at least 20 seconds, as promised on the "
             "recording.]")

    s = d.slide()
    title_bar(s, "Safety and security",
              "One condition is still open — and the condition is host range,\nthe "
              "subject of this entire project", heading_size=28)
    cols = [("What the committee asked",
             "To show our reasoning that the work won't alter host range, virulence, or "
             "antibiotic resistance. We don't have full approval. The revision is being "
             "written.", PALE_RUST, RUST, DARK),
            ("What we can say",
             "Φ8 carries no virulence factors and no resistance genes across all eighty "
             "coding sequences. Our constructs are protein fragments in laboratory "
             "E. coli. Nothing here is a modified phage.", WHITE, TEAL, MUTED),
            ("Why we treat it as dual use",
             "Understanding what sets the ceiling on host range is the same as knowing "
             "what would have to change to raise it — so we treat this as dual-use "
             "rather than arguing our way to a clean no.", DARK, LIGHT_TEAL,
             RGBColor(0xF2, 0xEF, 0xE9))]
    cw = (CONTENT_W - Inches(0.6)) / 3
    for i, (t, b, fill, tc, bc) in enumerate(cols):
        x = MARGIN + (cw + Inches(0.3)) * i
        box(s, int(x), Inches(2.9), int(cw), Inches(2.5), fill=fill,
            line=RULE if fill == WHITE else None)
        text(s, t, int(x + Inches(0.3)), Inches(3.14), int(cw - Inches(0.6)), size=16,
             color=tc, bold=True)
        text(s, b, int(x + Inches(0.3)), Inches(3.62), int(cw - Inches(0.6)), size=14,
             color=bc, spacing=1.3)
    footer(s, "Institutional Biosafety Committee, Keck Graduate Institute · conditional "
              "approval, 15 October 2026")
    notes(s, "On safety: our institutional biosafety committee gave us conditional "
             "approval with one condition still open, and that condition is a question "
             "about host range — the subject of this entire project.\n\nBut "
             "understanding what sets the ceiling on host range is the same as knowing "
             "what would have to change to raise it, so we treat this as dual-use "
             "rather than arguing our way to a clean no.")

    s = d.slide()
    title_bar(s, "Where we are", "Established · partly tested · open")
    cols = [("Established", TEAL,
             "Five bacterial genomes and a novel circular phage genome\n"
             "Three unrelated sugar cassettes in the same locus — with no serotype "
             "scheme in existence that could have told us\n"
             "A tail spike that is a sugar-cutting enzyme, by two independent methods\n"
             "A controlled negative result about interface prediction\n"
             "One resistance mutation verified in the reads"),
            ("Partly tested", RGBColor(0xC9, 0xA2, 0x27),
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
    cw = (CONTENT_W - Inches(0.6)) / 3
    for i, (t, colour, b) in enumerate(cols):
        x = MARGIN + (cw + Inches(0.3)) * i
        box(s, int(x), Inches(2.4), int(cw), Inches(0.05), fill=colour, radius=False)
        text(s, t, int(x), Inches(2.6), int(cw), size=20, color=colour, bold=True)
        text(s, b, int(x), Inches(3.15), int(cw), size=14, color=DARK, spacing=1.45)
    notes(s, "So let us say plainly where we are.\n\nWe have established five bacterial "
             "genomes and a novel circular phage genome; three unrelated sugar "
             "cassettes in the same locus; a tail spike that is a sugar-cutting enzyme "
             "by two independent methods; a controlled negative result; and one "
             "resistance mutation verified in the reads.\n\nWe have partly tested two "
             "things.\n\nAnd we have left plenty open.")

    s = d.slide(bg=DARK)
    text(s, "FOUR CYCLES, THREE OF THEM WRONG", MARGIN, Inches(1.6), CONTENT_W,
         size=14, color=LIGHT_TEAL, bold=True)
    text(s, "Each one was wrong in a way that\ntold us where to go next.", MARGIN,
         Inches(2.15), CONTENT_W, size=44, color=RGBColor(0xF7, 0xF4, 0xEE),
         font=DISPLAY, spacing=1.18)
    box(s, MARGIN, Inches(4.2), CONTENT_W, Inches(1.85), fill=TEAL)
    text(s, "If we could pass on one thing: put the cheap control\nin front of the "
            "expensive experiment.", MARGIN + Inches(0.45), Inches(4.45),
         CONTENT_W - Inches(0.9), size=26, color=RGBColor(0xF7, 0xF4, 0xEE),
         font=DISPLAY, spacing=1.2)
    text(s, "Nine folds told us what seven thousand couldn't, and one afternoon's dot "
            "blot told us what a week on a column hadn't.", MARGIN + Inches(0.45),
         Inches(5.55), CONTENT_W - Inches(0.9), size=16,
         color=RGBColor(0xC8, 0xD8, 0xD4))
    text(s, "iGEM Claremont-CA 2026 · Phagenomics · 2026.igem.wiki/claremont-ca",
         MARGIN, H - Inches(0.62), CONTENT_W, height=Inches(0.3), size=12,
         color=LIGHT_TEAL)
    notes(s, "Four cycles, three of them wrong, and each one wrong in a way that told "
             "us where to go next. If we could pass on one thing, it's this: put the "
             "cheap control in front of the expensive experiment. Nine folds told us "
             "what seven thousand couldn't, and one afternoon's dot blot told us what a "
             "week on a column hadn't.\n\n[CREDITS CARD FOLLOWS — 30 seconds, no "
             "narration.]")


if __name__ == "__main__":
    deck = build()
    count = deck.save()
    print(f"{count} slides -> {OUT.relative_to(ROOT)}")
