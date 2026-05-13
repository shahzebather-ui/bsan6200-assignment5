# BSAN6200 Assignment 5 — Option B (Job Fit Analyzer)

**Student:** Shahzeb Ather  
**Course:** Text Mining & Social Media Analytics (Spring 2026)  
**Repository:** [bsan6200-assignment5](https://github.com/shahzebather-ui/bsan6200-assignment5) (public)

---

## 1. Project title and option

**Job Fit Analyzer — Option B:** RAG over multiple job descriptions plus a Streamlit UI that compares your resume to a selected posting and returns **Skill Gap**, **Keyword Alignment**, and **Fit Summary** analyses with optional display of retrieved JD chunks.

---

## 2. Your name

Shahzeb Ather

---

## 3. Project description

The app loads **10+ job descriptions** and **one resume**, chunks JDs for **ChromaDB**, retrieves **top‑k** relevant chunks per task, and calls the **Hugging Face Inference API** (`Qwen/Qwen2.5-7B-Instruct`) to generate structured analyses. Prompts were iterated **three times** (v1 baseline → v2 evidence + 3×3 skill gap schema → v3 severity labels on gaps + three recommendations). Evaluation notes live in `evaluation/test_results.md`; the business write-up is in `memo.md`.

---

## 4. Setup instructions

1. **Clone** this repository and `cd` into the repo root.  
2. **Python 3.10+** recommended. Install dependencies:  
   `python3 -m pip install -r requirements.txt`  
3. Create a **`.env`** file in the repo root (do **not** commit it):  
   `HF_TOKEN=hf_...` (Hugging Face **read** token with Inference access).  
4. Add inputs:  
   - Resume: `data/resume/` (first `.pdf` or `.txt` found), **or** upload in the app **Resume** tab for the session.  
   - JDs: `data/job_descriptions/*.txt` (and optional `data/jd_metadata.csv` for UI labels).  
5. **Run Streamlit:**  
   `python3 -m streamlit run streamlit_app.py`  
   Or double-click **`run_streamlit.command`** (macOS). Open the URL shown (usually **http://localhost:8501**).  
6. **Notebook (development / rubric):** open `notebooks/rag_pipeline.ipynb` and run **all cells** top-to-bottom; **save** with outputs before submission.

---

## 5. Models and tools used

| Layer | Choice |
|--------|--------|
| UI | **Streamlit** (tabs, metrics, resume upload, dark theme via `.streamlit/config.toml`) |
| Vector store | **ChromaDB** (ephemeral client, in-memory collection on startup) |
| Embeddings / retrieval | Chroma **default embedding** for `query_texts` |
| LLM | **Hugging Face Inference API** — `Qwen/Qwen2.5-7B-Instruct` |
| Languages / libs | Python, **pandas**, **python-dotenv**, **pypdf**, **huggingface_hub** |
| Analysis artifacts | `evaluation/test_results.md`, `ai_log.md`, `memo.md` |

---

## 6. Paid vs free path

- **Free path used here:** **Hugging Face Inference API** with a free-tier compatible **inference** model and a personal **HF_TOKEN** (rate limits apply). No OpenAI/Gemini keys required for the submitted path.  
- **Paid alternative (course note):** OpenAI or Gemini APIs (~\$1–\$5 for the whole assignment if you go that route) — not required for this repo’s default `streamlit_app.py`.

---

## 7. Key findings

- **Chunking:** Paragraph-based chunking with overlap was used as the **default** for the app; a **fixed-window** chunker is available for **comparison** in the notebook.  
- **Retrieval:** Conditioning the prompt on **top‑k JD chunks** improved **grounding** versus passing only the full JD, especially for long postings.  
- **Prompt iteration:** v2 improved **structure and quotes**; v3 improved **prioritization language** (severity) and **brevity** (three actions), with occasional **severity edge cases** (e.g., bonus vs required).  
- **UI:** Session-level **fit** and **keyword %** metrics update after successful runs (parsed from model text); **RAG expanders** support grading and debugging.

---

## 8. File descriptions

| Path | Role |
|------|------|
| `streamlit_app.py` | Main app: chunking, Chroma indexing, retrieval, three prompts (v3 Skill Gap), HF calls, UI tabs and metrics |
| `notebooks/rag_pipeline.ipynb` | Exploratory RAG, chunking comparison, prompt experiments — **run all cells** before submit |
| `evaluation/test_results.md` | Qualitative + quantitative run log (v1 / v2 / v3) |
| `memo.md` | Short business memo summarizing approach and findings |
| `ai_log.md` | AI assistance log (Tier 2 compliance) |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | App theme (blue / slate dark) |
| `run_streamlit.command` | macOS double-click launcher for Streamlit |
| `.gitignore` | Ignores `.env`, `__pycache__`, `.DS_Store`, local `scripts/` helpers |
| `data/job_descriptions/` | JD text files |
| `data/resume/` | Local resume PDF/TXT (optional in git — add if you want clones runnable without upload) |
| `data/jd_metadata.csv` | Optional friendly names for the JD dropdown |

---

## Quick run

```bash
cd bsan6200-assignment5
python3 -m pip install -r requirements.txt
python3 -m streamlit run streamlit_app.py
```

Ensure `.env` contains `HF_TOKEN` before launching.
