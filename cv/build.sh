#!/usr/bin/env bash
# Builds the CV (needs `tectonic` and `pip install pymupdf`).
set -euo pipefail
cd "$(dirname "$0")"
tectonic Yigit_Sarp_Avci_CV.tex
python3 fix_pdf_text.py Yigit_Sarp_Avci_CV.pdf
