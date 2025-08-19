#!/bin/bash
# Simple compile without bibtex hassle

echo "🚀 Compiling paper (simple version)..."

# Just compile twice (references are inline now)
pdflatex paper.tex
pdflatex paper.tex

echo "✅ Done! Check paper.pdf"

# Open it
open paper.pdf