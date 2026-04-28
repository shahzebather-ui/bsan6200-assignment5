# BSAN6200 Assignment 5 - Option B (Job Fit Analyzer)

## Student
Shahzeb Ather

## Project Description
This project builds a job fit analyzer using language models and retrieval-augmented generation (RAG). The app compares resume content against job descriptions and returns a fit-oriented analysis.

Current output includes:
- fit assessment summary,
- top matching strengths,
- key skill/experience gaps,
- targeted improvement suggestions.

## Setup Instructions
1. Clone this repository.
2. Open a terminal in the repo root.
3. Install dependencies:
   - `python3 -m pip install -r requirements.txt`
4. Add API credentials in `.env` (never commit secrets):
   - `HF_TOKEN=hf_xxxxxxxxxxxxxxxxx`
5. Run the app:
   - `python3 -m streamlit run streamlit_app.py`
6. Add input files:
   - resume in `data/resume/`
   - job descriptions in `data/job_descriptions/`

## Models and Tools Used
- Python
- Streamlit
- Pandas
- ChromaDB (vector store)
- Hugging Face Inference API
- Notebook-based RAG/prompt iteration workflow

## Key Findings
- Starter pipeline runs locally with Streamlit and token-based auth.
- Environment/setup issues were resolved by pinning installation and run commands to the same Python interpreter.
- Benchmarking across multiple real job descriptions (10+ target) and documenting prompt iteration quality changes.

## File Descriptions
- `streamlit_app.py`: Option B user interface and analysis flow
- `notebooks/rag_pipeline.ipynb`: data prep, retrieval, and prompt testing
- `evaluation/test_results.md`: tracked evaluation outputs and prompt iterations
- `memo.md`: business memo
- `ai_log.md`: AI usage log with progression
- `data/`: input files (resume + job descriptions)
