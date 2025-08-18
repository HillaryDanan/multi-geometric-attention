#!/bin/bash
# Git Repository Professional Cleanup for NeurReps 2025
# Makes everything look clean and organized

echo "🧹 Cleaning up repository for NeurReps 2025..."
echo "=============================================="

# 1. Rename old neurips2025 folder to backup
echo "📦 Backing up old neurips2025 folder..."
git mv neurips2025 archive_neurreps2025_early_drafts
git commit -m "Archive early NeurReps drafts and extended theory"

# 2. Rename new submission folder to proper name
echo "✨ Renaming submission folder..."
git mv neurips2025_submission neurreps2025_submission
git commit -m "Rename to NeurReps 2025 official submission"

# 3. Update the main README to be professional
echo "📝 Creating professional README..."
cat > README.md << 'EOF'
# Empirical Phase Patterns in Large Language Models

## NeurReps 2025 Workshop Submission

**Paper**: Empirical Phase Patterns in GPT-3.5: A 9.7% Transformation Bottleneck  
**Author**: Hillary Danan  
**Workshop**: [NeurReps 2025](https://www.neurreps.org/) - Neural Representations: Composition & Decomposition

### Key Finding

Analysis of 1,000 GPT-3.5 responses reveals a statistically significant phase distribution with a notable **9.7% transformation bottleneck** (χ² = 120.24, p < 0.0001).

### Repository Structure

```
neurreps2025_submission/    # Official workshop submission
├── paper.md                # Main paper (8 pages)
├── supplementary.md        # Supplementary material
├── code/                   # Analysis and visualization code
├── figures/                # Paper figures
└── requirements.txt        # Dependencies

core/                       # Core implementation
├── mgat_framework.py       # Phase analysis framework
└── mgat_enhanced_core.py   # Extended framework

empirical_findings/         # Detailed empirical results
theoretical_framework/      # Geometric hypothesis (proposed interpretation)
extensions/                 # Extended theoretical explorations
archive_neurreps2025_early_drafts/  # Early drafts and extended material
```

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run phase analysis
python core/mgat_framework.py

# Generate figures
python visualization.py
```

### Main Contribution

1. **Empirical Discovery**: Statistically significant phase patterns in GPT-3.5
2. **9.7% Bottleneck**: Consistent limitation in transformation capacity
3. **Geometric Hypothesis**: Proposed interpretation through attention geometry
4. **Testable Predictions**: Framework for validating hypothesis

### Citation

```bibtex
@inproceedings{danan2025phase,
  title={Empirical Phase Patterns in GPT-3.5: A 9.7\% Transformation Bottleneck},
  author={Danan, Hillary},
  booktitle={NeurReps 2025: Neural Representations Workshop},
  year={2025}
}
```

### Links

- Workshop: [NeurReps 2025](https://www.neurreps.org/)
- Contact: hillarydanan@gmail.com

---

*This repository contains both the focused workshop submission and extended theoretical frameworks for future development.*
EOF

# 4. Create a professional .gitignore if missing
echo "🔧 Ensuring .gitignore is complete..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/
.env
.DS_Store

# Jupyter
.ipynb_checkpoints/

# IDE
.vscode/
.idea/
*.swp

# Data
*.h5
*.pkl
data/raw/
data/processed/

# Logs
*.log
logs/

# Temporary
*.tmp
*.bak
reorg.py
EOF

# 5. Add and commit all changes
echo "💾 Committing all changes..."
git add .
git commit -m "Professional repository structure for NeurReps 2025

- Clean submission in neurreps2025_submission/
- Archived early drafts and extended theory
- Updated README with clear structure
- Ready for public viewing"

# 6. Push to GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "=============================================="
echo "✅ Repository cleaned and organized!"
echo "=============================================="
echo ""
echo "Your repo now looks professional with:"
echo "  📁 neurreps2025_submission/ - Your clean submission"
echo "  📁 archive_neurreps2025_early_drafts/ - Preserved early work"
echo "  📄 Professional README.md"
echo ""
echo "Ready for NeurReps reviewers to see!"
echo "🌟 https://github.com/HillaryDanan/multi-geometric-attention"