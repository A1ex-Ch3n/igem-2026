"""Render the narration script as a double-spaced, line-numbered PDF for mark-up.

Reads the spoken lines out of documents/2026-10-24_presentation_video_script.md and
lays them out with a wide right margin to write in. Line numbers run continuously,
so edits can be sent back as "line 212: ...". The Chinese director notes stay in the
markdown; the PDF carries a short English stage direction per section instead, since
the local TeX install has no CJK support.

    python code/1024_script_pdf/make_script_pdf.py
"""
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "documents/2026-10-24_presentation_video_script.md"
PDF = ROOT / "documents/2026-10-24_presentation_video_script.pdf"
WPM = 140

# key -> (English heading, on-screen note)
SECTIONS = {
    "COLD": ("Cold open", "Plaque assay animation; then the same drop on two other strains, no effect."),
    "I.1": ("Act I.1 \\textbar{} Our system",
            "Sampling map (check: no flags), bacterial genomes, phage genome. "
            "Credit the phage assembly to the PI."),
    "I.2": ("Act I.2 \\textbar{} The first clue",
            "The three O-antigen loci side by side, labelled "
            "\\texttt{prediction --- not yet tested}. This figure returns at the end of Act II."),
    "I.3": ("Act I.3 \\textbar{} The textbook",
            "Lock and key. First appearance of the beta-helix tail spike render, labelled "
            "\\texttt{the key?}"),
    "II.1": ("Act II.1 \\textbar{} Why a computer",
             "114 $\\times$ 63 = 7,182 matrix; then an interface score bar from 0 to 1."),
    "II.2": ("Act II.2 \\textbar{} The controls",
             "Control design, then the controls comparison figure. "
             "Hold 0.137 and 0.136 large on screen."),
    "II.3": ("Act II.3 \\textbar{} What was going wrong",
             "Two confidence bars: on scrambling the left collapses 0.55 to 0.17, the right "
             "barely moves. Then paired-MSA diagram: two circles that never intersect."),
    "II.4": ("Act II.4 \\textbar{} The fold tells the truth",
             "Beta-helix render returns, H-bond period marked, caption "
             "\\texttt{CDS\\_0011 res 540--941}. Ends by replaying the Act I.2 figure."),
    "II.5": ("Act II.5 \\textbar{} The hypothesis forms", "Attribution has to be exact here."),
    "III.1": ("Act III.1 \\textbar{} The hypothesis",
              "One-sentence hypothesis box on white, held. Credited to the PI."),
    "III.2": ("Act III.2 \\textbar{} The targets",
              "Phage genome zoomed to the tail module. Canonical CDS numbering."),
    "III.3": ("Act III.3 \\textbar{} Resurrecting the ancestor",
              "Tree collapsing back to ancestors, the three nodes, identity matrix, perplexity "
              "trend. Phylogeny, ASR and scoring credited to the PI. RMSD values stay on screen, "
              "unspoken."),
    "III.4": ("Act III.4 \\textbar{} The constructs",
              "Six constructs. Put res 305--941 and res 540--941 on one axis so the overlap is visible."),
    "III.5": ("Act III.5 \\textbar{} The bench",
              "Gel with the target boxed in red. On screen: \\texttt{IPTG -/+ : present} \\textbar{} "
              "\\texttt{empty-vector control: RUNNING NOW} \\textbar{} \\texttt{n = 1}"),
    "III.6": ("Act III.6 \\textbar{} One clean result, and safety",
              "Read pileup with F126L marked; sugar locus \\texttt{unchanged}; "
              "\\texttt{0 VFDB / 0 CARD} and IBC approval."),
    "CODA": ("Coda \\textbar{} Where we are",
             "Three columns fading in: Established / Predicted, not tested / Open."),
}

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage{fontspec}
\usepackage[a4paper,left=2.2cm,right=5.6cm,top=2.2cm,bottom=2.4cm]{geometry}
\usepackage{setspace}
\usepackage{lineno}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{fancyhdr}
\setmainfont{Charter}
\definecolor{note}{gray}{0.45}
\definecolor{rule}{gray}{0.8}
\titleformat{\section}{\normalfont\large\bfseries}{}{0pt}{}
\titlespacing{\section}{0pt}{20pt}{4pt}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\color{note}\footnotesize\thepage}
\renewcommand\linenumberfont{\normalfont\footnotesize\color{note}}
\setlength{\linenumbersep}{16pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\begin{document}
\linenumbers
"""


def esc(text):
    text = text.replace("\\", "\x00")
    for char in "&%$#_{}":
        text = text.replace(char, "\\" + char)
    text = text.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}")
    text = text.replace("—", "---").replace("–", "--")
    text = text.replace("“", "``").replace("”", "''").replace("‘", "`").replace("’", "'")
    text = text.replace("×", r"$\times$").replace("−", "-")
    text = text.replace("Φ", r"$\Phi$").replace("β", r"$\beta$").replace("Å", r"\AA{}")
    return text.replace("\x00", r"\textbackslash{}")


def inline(text):
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*(.+?)\*", r"\\textit{\1}", text)
    text = re.sub(r"`(.+?)`", r"\\texttt{\1}", text)
    return text


CJK = re.compile(r"[\u3000-\u9fff\uff00-\uffef]")


def spoken_lines(chunk):
    """Spoken narration only: ASCII-leading lines with no CJK anywhere in them."""
    out = []
    for line in chunk.split("\n")[1:]:
        if not line.startswith("> "):
            continue
        content = line[2:].strip()
        if not content or CJK.search(content):
            continue
        if content[0].isascii() and content[0].isalpha():
            out.append(content)
    return out


def main():
    md = SRC.read_text()
    body = md.split("## COLD OPEN", 1)[1]
    body = "## COLD OPEN" + body.split("## 累計時間表", 1)[0]

    out = [PREAMBLE]
    out.append(
        r"{\LARGE\bfseries Presentation Video --- narration, v1}\\[5pt]"
        r"{\color{note}iGEM Claremont-CA 2026 \quad\textbar\quad draft of 2026-10-24}\\[3pt]"
        r"{\color{note}Timecodes assume " + str(WPM) + r" words per minute; the uploaded "
        r"file has a hard limit of 15:00.}\\[3pt]"
        r"{\color{note}Line numbers run continuously --- send edits back as "
        r"\textit{line 212: \ldots}}\\[12pt]{\color{rule}\hrule}" + "\n"
    )

    total = 0
    for chunk in re.split(r"\n(?=#{2,3} )", body):
        raw = re.sub(r"^#{2,3} ", "", chunk.split("\n")[0]).strip()
        key = raw.split(" ")[0].replace("COLD", "COLD").replace("CODA", "CODA")
        if key not in SECTIONS:
            continue
        title, onscreen = SECTIONS[key]
        lines = spoken_lines(chunk)
        words = sum(len(s.split()) for s in lines)
        total += words
        stamp = total / WPM * 60
        out.append(
            f"\\section*{{{title} \\normalsize\\mdseries\\color{{note}}\\hfill "
            f"{words} words \\quad ends {int(stamp)//60}:{int(stamp)%60:02d}}}"
        )
        out.append(r"{\singlespacing\footnotesize\color{note}ON SCREEN --- " + onscreen + r"\par}")
        out.append(r"\begin{spacing}{2.0}")
        out.extend(inline(s) + r"\par" for s in lines)
        out.append(r"\end{spacing}")

    end = total / WPM * 60 + 38
    out.append(
        r"\vspace{14pt}{\color{rule}\hrule}\vspace{6pt}"
        r"{\color{note}\footnotesize " + f"{total} spoken words. With three act cards and a "
        r"30-second credit card, the finished file runs about "
        f"{int(end)//60}:{int(end)%60:02d} at {WPM} words per minute." + r"\par}"
    )
    out.append(r"\end{document}")

    with tempfile.TemporaryDirectory() as tmp:
        tex = Path(tmp) / "script.tex"
        tex.write_text("\n".join(out))
        for _ in range(2):
            proc = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                cwd=tmp, capture_output=True, text=True,
            )
        if proc.returncode:
            print(proc.stdout[-2500:])
            raise SystemExit("xelatex failed")
        PDF.write_bytes((Path(tmp) / "script.pdf").read_bytes())

    print(f"{total} spoken words -> {PDF.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
