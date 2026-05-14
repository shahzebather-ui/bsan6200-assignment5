# AI Usage Log (Tier 2)

BSAN6200 Assignment 5 — Option B. Each entry includes **Date**, **Tool**, what I asked, what I used, and what I changed.

---

### Entry 1

- **Date:** 2026-05-01  
- **Tool:** Cursor (AI-assisted editor)  
- **What I asked:** Help scaffolding the Option B repo (`streamlit_app.py`, `notebooks/`, `evaluation/`).  
- **What I used:** Suggested folder layout and starter imports.  
- **What I modified:** Kept the structure; rewrote prompts, chunking, and paths for my JD files and rubric.

### Entry 2

- **Date:** 2026-05-05  
- **Tool:** Cursor  
- **What I asked:** Debug `pip`/import errors and HF Inference client wiring.  
- **What I used:** `InferenceClient` + `python-dotenv` pattern.  
- **What I modified:** Model id and `max_tokens` after Skill Gap truncation.

### Entry 3

- **Date:** 2026-05-08  
- **Tool:** Cursor  
- **What I asked:** How to add Chroma retrieval and pass top‑k JD chunks into prompts.  
- **What I used:** Retrieval outline from assistant.  
- **What I modified:** `TOP_K_CHUNKS` and retrieval query text after reviewing chunks.

### Entry 4

- **Date:** 2026-05-10  
- **Tool:** Cursor  
- **What I asked:** Tighter Skill Gap prompt (structure + evidence).  
- **What I used:** Draft wording.  
- **What I modified:** Hand-edited v2/v3 rules (3+3, quotes, severity, three actions) for grading.

### Entry 5

- **Date:** 2026-05-11  
- **Tool:** Cursor  
- **What I asked:** Streamlit UI polish (theme, tabs, metrics).  
- **What I used:** CSS / layout ideas.  
- **What I modified:** **Rejected** putting a logger script in the repo; kept it local and **gitignored** `scripts/`.

### Entry 6

- **Date:** 2026-05-12  
- **Tool:** Cursor  
- **What I asked:** Fix metric tiles stuck on “Pending.”  
- **What I used:** `st.rerun()` after runs + parse order suggestion.  
- **What I modified:** Implemented rerun + score parsing; verified on a live Skill Gap run.

### Entry 7

- **Date:** 2026-05-13  
- **Tool:** Cursor  
- **What I asked:** README + memo alignment with rubric.  
- **What I used:** Section outlines.  
- **What I modified:** Personalized findings to match `evaluation/test_results.md`.

### Entry 8

- **Date:** 2026-05-13  
- **Tool:** Cursor + local Jupyter  
- **What I asked:** Save notebook outputs before deadline.  
- **What I used:** `jupyter nbconvert --execute` (Anaconda `python`).  
- **What I modified:** Ran notebook in-place so cells show outputs in the submitted `.ipynb`.

---

**Progression:** scaffolding → API/runtime → RAG + prompts → UI + eval logs → submission packaging.

**Case where my approach beat the AI suggestion:** I did **not** ship the logger script to GitHub (Entry 5); I kept evaluation logs in `evaluation/test_results.md` and local tooling only.
