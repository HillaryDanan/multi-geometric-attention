#!/bin/bash
# Compile NeurReps 2025 Paper with PMLR/JMLR template

echo "🔧 Compiling NeurReps 2025 Paper..."
echo "=================================="

# Clean up old files first
echo "🧹 Cleaning up old compilation files..."
rm -f pmlr-sample.aux pmlr-sample.bbl pmlr-sample.blg pmlr-sample.log pmlr-sample.out

# Check if required files exist
echo "📝 Checking required files..."
if [ ! -f "pmlr-sample.tex" ]; then
    echo "❌ ERROR: pmlr-sample.tex not found!"
    echo "Please save the pmlr-sample.tex file first."
    exit 1
fi

if [ ! -f "references.bib" ]; then
    echo "❌ ERROR: references.bib not found!"
    exit 1
fi

# Check for JMLR class files
if [ ! -f "jmlr.cls" ]; then
    echo "⚠️  WARNING: jmlr.cls not found!"
    echo "Download the NeurReps style files and extract them here."
fi

# Compile with pdflatex and bibtex
echo "🚀 Starting LaTeX compilation..."
echo ""

# First pass
echo "📄 First pdflatex pass..."
pdflatex -interaction=nonstopmode pmlr-sample.tex > compile.log 2>&1
if [ $? -ne 0 ]; then
    echo "❌ First pdflatex pass failed. Check compile.log for errors."
    tail -20 compile.log
    exit 1
fi

# BibTeX
echo "📚 Running BibTeX..."
bibtex pmlr-sample >> compile.log 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️  BibTeX had warnings/errors. Continuing anyway..."
fi

# Second pass
echo "📄 Second pdflatex pass..."
pdflatex -interaction=nonstopmode pmlr-sample.tex >> compile.log 2>&1
if [ $? -ne 0 ]; then
    echo "❌ Second pdflatex pass failed. Check compile.log for errors."
    tail -20 compile.log
    exit 1
fi

# Third pass (for references)
echo "📄 Final pdflatex pass..."
pdflatex -interaction=nonstopmode pmlr-sample.tex >> compile.log 2>&1
if [ $? -ne 0 ]; then
    echo "❌ Final pdflatex pass failed. Check compile.log for errors."
    tail -20 compile.log
    exit 1
fi

echo ""
echo "=================================="

# Check if PDF was created
if [ -f "pmlr-sample.pdf" ]; then
    echo "✅ pmlr-sample.pdf created successfully!"
    
    # Get file size
    filesize=$(ls -lh pmlr-sample.pdf | awk '{print $5}')
    echo "📄 File size: $filesize"
    
    # Count pages (Mac/Linux compatible)
    if command -v pdfinfo &> /dev/null; then
        pages=$(pdfinfo pmlr-sample.pdf | grep Pages | awk '{print $2}')
        echo "📄 Page count: $pages"
        if [ "$pages" -gt 9 ]; then
            echo "⚠️  WARNING: Paper has $pages pages (max 9 for proceedings track)"
        fi
    fi
    
    # Open the PDF (Mac)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open pmlr-sample.pdf
    fi
else
    echo "❌ Something went wrong. PDF not created."
    echo "Check compile.log for detailed error messages."
    exit 1
fi

echo ""
echo "📋 NEURREPS 2025 SUBMISSION CHECKLIST:"
echo "  ✓ Using PMLR/JMLR template"
echo "  ✓ Proceedings track (mlmain)"
echo "  ✓ Anonymous submission"
echo "  [ ] Under 9 pages (excluding references)"
echo "  [ ] Keywords included"
echo "  [ ] Abstract within limits"
echo "  [ ] References properly formatted"
echo "  [ ] Upload to OpenReview by Aug 22, 2025"
echo ""
echo "🎉 Paper ready for NeurReps 2025!"
echo "=================================="