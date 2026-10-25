"""Slide primitives for the Phagenomics deck.

Picture first. A mechanism slide carries one rendered frame and a short eyebrow
label — nothing else — so there is no text to collide with anything. The prose
that summarises a mechanism waits for a slide of its own once the build has run.
Movement between the frames of a build comes from Morph transitions.
"""
from pathlib import Path

from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[2]
FRAMES = ROOT / "code/output/1025_presentation_deck"
FIGS = ROOT / "code/output/1025_presentation_deck/figs"
OUT = ROOT / "documents/2026-10-25_presentation_deck.pptx"

W, H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.72)
CONTENT_W = W - 2 * MARGIN

INK = RGBColor(0x24, 0x38, 0x3A)
TEAL = RGBColor(0x2D, 0x6A, 0x6A)
RUST = RGBColor(0xB4, 0x54, 0x2E)
MUTED = RGBColor(0x6B, 0x76, 0x74)
RULE = RGBColor(0xDC, 0xD8, 0xD0)
PALE = RGBColor(0xEA, 0xF0, 0xEE)
PALE_RUST = RGBColor(0xF6, 0xE7, 0xE0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PAPER = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT = RGBColor(0x8F, 0xB3, 0xAE)
CREAM = RGBColor(0xF7, 0xF4, 0xEE)
DIM = RGBColor(0xC8, 0xD8, 0xD4)

DISPLAY = "Georgia"
BODY = "Avenir Next"

MORPH = (
    '<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">'
    '<mc:Choice xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" Requires="p14">'
    '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
    ' spd="slow" p14:dur="800"><p159:morph'
    ' xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"'
    ' option="byObject"/></p:transition></mc:Choice><mc:Fallback>'
    '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
    ' spd="med"><p:fade/></p:transition></mc:Fallback></mc:AlternateContent>'
)
FADE = ('<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
        ' spd="med"><p:fade/></p:transition>')


def transition(slide, xml):
    sld = slide._element
    node = etree.fromstring(xml)
    clr = sld.find("{http://schemas.openxmlformats.org/presentationml/2006/main}clrMapOvr")
    (sld.append if clr is None else clr.addnext)(node)


class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = W, H
        self.blank = self.prs.slide_layouts[6]
        self.n = 0

    def new(self, bg=PAPER, morph=False, number=True):
        s = self.prs.slides.add_slide(self.blank)
        fill = s.background.fill
        fill.solid()
        fill.fore_color.rgb = bg
        transition(s, MORPH if morph else FADE)
        self.n += 1
        if number:
            text(s, str(self.n), W - MARGIN - Inches(0.6), H - Inches(0.46),
                 Inches(0.6), Inches(0.24), size=10, align=PP_ALIGN.RIGHT,
                 color=LIGHT if bg != PAPER else RGBColor(0xA8, 0xB0, 0xAE))
        return s

    def save(self):
        self.prs.save(OUT)
        return self.n


def text(slide, body, left, top, width, height=None, size=18, color=INK, bold=False,
         font=BODY, align=PP_ALIGN.LEFT, italic=False, spacing=1.3,
         anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(left, top, width, height or Inches(0.9))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(body.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment, p.line_spacing = align, spacing
        run = p.add_run()
        run.text = line
        f = run.font
        f.name, f.size, f.bold, f.italic = font, Pt(size), bold, italic
        f.color.rgb = color
    return box


def panel(slide, left, top, width, height, fill=None, line=None, radius=0.06):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    sh.adjustments[0] = radius
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
        sh.line.width = Pt(1)
    sh.shadow.inherit = False
    sh.text_frame.word_wrap = True
    return sh


def picture(slide, path, left, top, max_w, max_h, name=None):
    iw, ih = Image.open(path).size
    scale = min(max_w / iw, max_h / ih)
    w, h = int(iw * scale), int(ih * scale)
    pic = slide.shapes.add_picture(str(path), int(left + (max_w - w) / 2),
                                   int(top + (max_h - h) / 2), w, h)
    if name:
        pic.name = name
    return pic


def notes(slide, body):
    slide.notes_slide.notes_text_frame.text = body


def eyebrow(slide, label, accent=TEAL):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, MARGIN, Inches(0.42),
                                 Inches(0.13), Inches(0.28))
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent
    bar.line.fill.background()
    bar.shadow.inherit = False
    text(slide, label.upper(), MARGIN + Inches(0.3), Inches(0.44), Inches(10.5),
         Inches(0.3), size=12, color=accent, bold=True)


def frame(d, sub, name, label, note="", morph=True, accent=TEAL):
    """One rendered frame, nearly full bleed, with a single eyebrow label."""
    s = d.new(morph=morph)
    eyebrow(s, label, accent)
    picture(s, FRAMES / sub / f"{name}.png", MARGIN, Inches(0.92),
            CONTENT_W, Inches(6.15), name="!!frame")
    if note:
        notes(s, note)
    return s


def run(d, sub, names, label, note="", accent=TEAL):
    """A build. The narration sits on every frame so it is there whichever one
    is on screen while it is being read."""
    for i, n in enumerate(names):
        frame(d, sub, n, label, note, morph=(i > 0), accent=accent)


def statement(d, kicker, body, sub="", bg=TEAL, note="", size=34):
    s = d.new(bg=bg)
    fg = CREAM if bg != PAPER else INK
    sub_fg = DIM if bg != PAPER else MUTED
    text(s, kicker.upper(), MARGIN, Inches(1.45), CONTENT_W, Inches(0.3), size=12,
         color=sub_fg, bold=True)
    text(s, body, MARGIN, Inches(2.05), CONTENT_W, Inches(3.3), size=size, color=fg,
         font=DISPLAY, spacing=1.2)
    if sub:
        text(s, sub, MARGIN, Inches(5.45), Inches(10.6), Inches(1.3), size=19,
             color=sub_fg, spacing=1.35)
    if note:
        notes(s, note)
    return s


def prose(d, label, head, body, accent=TEAL, note="", figkey=None, frame_sub=None,
          frame_name=None):
    """The text that lands after a mechanism has been shown."""
    s = d.new()
    eyebrow(s, label, accent)
    text(s, head, MARGIN, Inches(0.98), CONTENT_W, Inches(1.25), size=29,
         color=INK, font=DISPLAY, spacing=1.12)
    src = None
    if figkey:
        src = FIGS / f"{figkey}.png"
    elif frame_sub:
        src = FRAMES / frame_sub / f"{frame_name}.png"
    if src:
        picture(s, src, MARGIN, Inches(2.5), Inches(6.5), Inches(4.1))
        text(s, body, MARGIN + Inches(7.0), Inches(2.45), Inches(5.1), Inches(4.4),
             size=16, color=MUTED, spacing=1.38)
    else:
        text(s, body, MARGIN, Inches(2.4), Inches(10.6), Inches(4.4), size=20,
             color=MUTED, spacing=1.45)
    if note:
        notes(s, note)
    return s


def figure(d, label, head, figkey, caption="", accent=TEAL, note=""):
    s = d.new()
    eyebrow(s, label, accent)
    text(s, head, MARGIN, Inches(0.92), CONTENT_W, Inches(0.85), size=25, color=INK,
         font=DISPLAY, spacing=1.12)
    picture(s, FIGS / f"{figkey}.png", MARGIN, Inches(1.95), CONTENT_W, Inches(4.75))
    if caption:
        text(s, caption, MARGIN, H - Inches(0.6), CONTENT_W - Inches(0.9),
             Inches(0.4), size=12, color=MUTED, spacing=1.2)
    if note:
        notes(s, note)
    return s


def cards(d, label, head, items, accent=TEAL, note="", top=Inches(2.4),
          height=Inches(2.0)):
    s = d.new()
    eyebrow(s, label, accent)
    text(s, head, MARGIN, Inches(0.98), CONTENT_W, Inches(1.2), size=29, color=INK,
         font=DISPLAY, spacing=1.12)
    n = len(items)
    gap = Inches(0.32)
    cw = int((CONTENT_W - gap * (n - 1)) / n)
    for i, (title, body, colour, fill) in enumerate(items):
        x = int(MARGIN + (cw + gap) * i)
        panel(s, x, top, cw, height, fill=fill,
              line=RULE if fill == WHITE else None)
        text(s, title, x + Inches(0.3), top + Inches(0.24), cw - Inches(0.6),
             Inches(0.66), size=15, color=colour, bold=True, spacing=1.2)
        text(s, body, x + Inches(0.3), top + Inches(0.9), cw - Inches(0.6),
             height - Inches(1.15), size=13,
             color=MUTED if fill == WHITE else CREAM, spacing=1.35)
    if note:
        notes(s, note)
    return s
