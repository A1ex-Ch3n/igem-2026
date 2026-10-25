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

SECTIONS = {
    "OPENING": ("Opening", "Team logo, a team photo, then the title card."),
    "I.1": ("Act I.1 \textbar{} The bottleneck",
            "Plaque assay animation; then the same drop on two other strains, no effect."),
    "I.2": ("Act I.2 \textbar{} Adsorption and the sugar coat",
            "Cross-section of a cell: membrane, wall, O-antigen, capsule. Mark which layer "
            "the phage meets first."),
    "I.3": ("Act I.3 \textbar{} Where the project came from",
            "Team photo with Prof. Libeskind-Hadas, captioned as an early conversation."),
    "I.4": ("Act I.4 \textbar{} Our system, and the first clue",
            "Sampling at the California Botanic Garden, the genomes, then the three O-antigen "
            "cassettes side by side. Label the last one a hypothesis, not a prediction."),
    "II.1": ("Cycle 1 \textbar{} Design", "DBTL bar with DESIGN lit. Lock and key."),
    "II.2": ("Cycle 1 \textbar{} Build",
             "BUILD lit. Funnel from 441 to 178 to 114 $\times$ 63. Three tools and why each "
             "one stalled."),
    "II.3": ("Cycle 1 \textbar{} Test",
             "TEST lit. The ranking first, so it looks reasonable; then the control figure. "
             "Hold 0.137 and 0.136 large."),
    "II.4": ("Cycle 1 \textbar{} Learn",
             "LEARN lit. Two confidence bars: on scrambling the left collapses 0.55 to 0.17, "
             "the right does not move. Then two circles that never intersect."),
    "III.1": ("Cycle 2 \textbar{} Design and Build",
              "PhageRBPdetect over 80 proteins, 8 candidates, rung-period diagram."),
    "III.2": ("Cycle 2 \textbar{} Test and Learn",
              "Fold table, eight proteins and four verdicts --- the method discriminates. "
              "Then the beta-helix render and a sugar-cutting animation."),
    "III.3": ("Cycle 2 \textbar{} The hypothesis",
              "One-sentence hypothesis box on white, held. Credited jointly with the PI."),
    "IV.1": ("Cycle 3 \textbar{} Design and Build",
             "Shaft versus body rigidity, the six constructs, the tree collapsing to three nodes."),
    "IV.2": ("Cycle 3 \textbar{} Test",
             "Four test rounds; the 9-29 gel; the 10-10 nickel column with blank elutions."),
    "IV.3": ("Cycle 3 \textbar{} Learn: an outside view changed a result",
             "The strongest human-practices beat in the video. Tolstorukov's email, then the "
             "10-19 dot blot with 2.9$\times$ marked."),
    "IV.4": ("Cycle 3 \textbar{} What we still owe",
             "Honest list. Caption: fifth consecutive assay with no empty-vector lane."),
    "V.1": ("Cycle 4 \textbar{} Design and Test",
            "Colonies from the plaque zone, whole-genome sequencing, F126L inside a 30 kb "
            "capsular cluster."),
    "V.2": ("Cycle 4 \textbar{} Learn",
            "Diagram of a capsule hiding an intact O-antigen --- how both conclusions hold."),
    "C.1": ("Coda \textbar{} The garden",
            "Interview clips, at least 20 seconds. Credit both hosts and note permission."),
    "C.2": ("Coda \textbar{} Safety",
            "The IBC letter, 0 VFDB / 0 CARD, and the open condition quoted."),
    "C.3": ("Coda \textbar{} Where we are",
            "Three columns fading in: Established / Predicted / Open."),
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
    body = md.split("## OPENING", 1)[1]
    body = "## OPENING" + body.split("## 對照評分表", 1)[0]

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
        key = raw.split(" ")[0]
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

    end = total / WPM * 60 + 45
    out.append(
        r"\vspace{14pt}{\color{rule}\hrule}\vspace{6pt}"
        r"{\color{note}\footnotesize " + f"{total} spoken words. With six act cards and a "
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
