# BSAN6200 Assignment 5 - Option B (Job Fit Analyzer)

## Student
Your Name Here

## Project Description
This project builds a job fit analyzer using language models and retrieval-augmented generation (RAG).
It compares a resume against multiple job descriptions and returns:
- fit summary,
- top matching strengths,
- key gaps,
- targeted improvement suggestions.

## Setup Instructions
1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies from `requirements.txt`.
4. Add API credentials in `.env` (never commit secrets).
5. Run the app:
   - `streamlit run streamlit_app.py`

## Models and Tools Used
- Python
- Streamlit
- Pandas
- Notebook-based RAG pipeline
- LLM API (to be finalized during implementation)

## Paid vs Free Path
- Paid path: OpenAI or Gemini API
- Free path: HuggingFace Inference API or local model setup

## Key Findings
TBD after experiments and evaluation.

## File Descriptions
- `streamlit_app.py`: Option B user interface and analysis flow
- `notebooks/rag_pipeline.ipynb`: data prep, retrieval, and prompt testing
- `evaluation/test_results.md`: tracked evaluation outputs and prompt iterations
- `memo.md`: business memo
- `ai_log.md`: AI usage log with progression
