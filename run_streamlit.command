#!/bin/bash
# Double-click in Finder: opens Terminal, starts Streamlit, opens your browser.
set -e
cd "$(dirname "$0")" || exit 1
echo "Starting Streamlit from: $(pwd)"
echo "If the browser does not open: http://localhost:8501"
# One command per line (do not paste two cd lines together).
python3 -m streamlit run streamlit_app.py
