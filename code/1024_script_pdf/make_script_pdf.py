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
    "I.1": ("Act I.1 | The bottleneck",
            "Plaque assay animation; then the same drop on two other strains, no effect."),
    "I.2": ("Act I.2 | Adsorption and the sugar coat",
            "Cross-section of a cell: membrane, wall, O-antigen, capsule. Mark which layer the phage meets first."),
    "I.3": ("Act I.3 | Where the project came from",
            "Team photo with Prof. Libeskind-Hadas, captioned as an early conversation."),
    "I.4": ("Act I.4 | What we isolated",
            "Sampling photo; five isolates collapsing to three strains; the circular phage genome with the tail spike outlined."),
    "I.5": ("Act I.5 | The first clue",
            "The three O-antigen loci side by side, labelled as a hypothesis."),
    "C1.D": ("Cycle 1 | Design", "DBTL bar, DESIGN lit. Lock and key."),
    "C1.B": ("Cycle 1 | Build",
             "BUILD lit. Funnel from 441 to 144 clusters to 114 x 63. The surrogate-host trade-off as two columns. Three tools and why each stalled."),
    "C1.T": ("Cycle 1 | Test",
             "TEST lit. The ranking first so it looks reasonable, then score against protein length, then the control figure. Hold 0.137 and 0.136 large."),
    "C1.L": ("Cycle 1 | Learn",
             "LEARN lit. Two confidence bars: on scrambling the left collapses 0.55 to 0.17, the right does not move. Then two circles that never intersect."),
    "C2.DB": ("Cycle 2 | Design and Build",
              "An open-source classifier over 80 proteins, 8 candidates, rung-period diagram."),
    "C2.TL": ("Cycle 2 | Test and Learn",
              "Fold table: eight proteins, four verdicts, so the method discriminates. Then the beta-helix render and a sugar-cutting animation."),
    "C2.H": ("Cycle 2 | The hypothesis",
             "One-sentence hypothesis box on white, held. Credited jointly with the PI."),
    "C3.D": ("Cycle 3 | Design",
             "Domain map of CDS 11: anchor, flexible shaft, rigid body. Then the tree collapsing to three nodes."),
    "C3.B": ("Cycle 3 | Build",
             "Registry cards for the six parts, published and CC0. Caption: three of the six are sequences that exist nowhere in nature."),
    "C3.T": ("Cycle 3 | Test",
             "Four test rounds. The 9-15 gels, the 9-29 band, the 10-01 elution that worked, the 10-10 column that did not."),
    "C3.L": ("Cycle 3 | Learn: an outside view changed a result",
             "The strongest human-practices beat in the video. Tolstorukov's email, then the 10-19 dot blot with 2.9x marked."),
    "C3.A": ("Cycle 3 | The activity assay",
             "The 10-16 spot test and colony counts normalised to the PBS control. Caption the missing carry-over control."),
    "C3.G": ("Cycle 3 | What we still owe", "Honest list."),
    "C4.DT": ("Cycle 4 | Design and Test",
              "Colonies from the plaque zone, whole-genome sequencing, read-level verification, F126L inside a 30 kb capsule cluster."),
    "C4.L": ("Cycle 4 | Learn",
             "A capsule hiding an intact O-antigen: how both conclusions hold at once."),
    "WHAT": ("What we're leaving behind",
             "Tool terminal output, the GitLab repository, the six parts, the negative result."),
    "CO.1": ("Coda | The garden",
             "Interview clips, at least 20 seconds. Credit both hosts and note permission."),
    "CO.2": ("Coda | Safety",
             "The IBC letter, 0 VFDB / 0 CARD, and the open condition quoted."),
    "CO.3": ("Coda | Where we are",
             "Three columns fading in: Established / Partly tested / Open."),
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


def esc_bar(text):
    """Headings and notes use a plain pipe as a separator; LaTeX needs \textbar."""
    return text.replace("|", r"\textbar{}").replace("x 63", r"$\times$ 63").replace("2.9x", r"2.9$\times$")


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
        probe = content.lstrip("*_`")
        if probe and probe[0].isascii() and probe[0].isalpha():
            out.append(content)
    return out


def main():
    md = SRC.read_text()
    body = md.split("## OPENING", 1)[1]
    body = "## OPENING" + body.split("## 對照評分表", 1)[0]

    out = [PREAMBLE]
    out.append(
        r"{\LARGE\bfseries Presentation Video --- narration, v3}\\[5pt]"
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
            f"\\section*{{{esc_bar(title)} \\normalsize\\mdseries\\color{{note}}\\hfill "
            f"{words} words \\quad ends {int(stamp)//60}:{int(stamp)%60:02d}}}"
        )
        out.append(r"{\singlespacing\footnotesize\color{note}ON SCREEN --- " + esc_bar(onscreen) + r"\par}")
        out.append(r"\begin{spacing}{2.0}")
        out.extend(inline(s) + r"\par" for s in lines)
        out.append(r"\end{spacing}")

    end = total / WPM * 60 + 60
    out.append(
        r"\vspace{14pt}{\color{rule}\hrule}\vspace{6pt}"
        r"{\color{note}\footnotesize " + f"{total} spoken words. With the act cards and a "
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
