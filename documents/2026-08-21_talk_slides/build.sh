#!/usr/bin/env bash
# Build the deck and the speaker-note printout. XeLaTeX only — no quarto, no xeCJK.
set -euo pipefail
cd "$(dirname "$0")"
xelatex -interaction=nonstopmode -halt-on-error slides.tex >/dev/null
xelatex -interaction=nonstopmode -halt-on-error slides.tex >/dev/null
xelatex -interaction=nonstopmode -halt-on-error -jobname=slides_notes \
  "\def\NOTESONLY{}\input{slides.tex}" >/dev/null
rm -f slides.aux slides.log slides.nav slides.out slides.snm slides.toc \
      slides_notes.aux slides_notes.log slides_notes.nav slides_notes.out slides_notes.snm slides_notes.toc
echo "built: slides.pdf (deck)  slides_notes.pdf (speaker script)"
