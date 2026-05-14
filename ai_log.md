# AI Usage Log (Tier 2)

Minimum log for BSAN6200 Assignment 5 — Option B. Each entry: **date**, **tool**, **what I asked**, **what I used**, **what I changed**.

---

1. **2026-05-01 · Cursor / ChatGPT-class assistant** — Asked for help scaffolding the Option B repo layout (`streamlit_app.py`, `notebooks/`, `evaluation/`). Used folder structure and starter imports. **I kept** the layout; **I rewrote** prompts, chunking, and data paths to match my JD files and rubric.

2. **2026-05-05 · Cursor** — Debugged `pip`/import errors and HF Inference client usage. Used suggested `InferenceClient` pattern and `python-dotenv`. **I adjusted** model id and `max_tokens` after truncation during Skill Gap runs.

3. **2026-05-08 · Cursor** — Asked how to add Chroma retrieval and pass top‑k JD chunks into prompts. Used the retrieval outline. **I tuned** `TOP_K_CHUNKS` and query strings after manual review of chunk quality.

4. **2026-05-10 · Cursor** — Requested tighter Skill Gap prompt (structured bullets, evidence). Used draft wording. **I edited** v2/v3 rules myself (3+3, severity labels, three actions) to match what I wanted graded.

5. **2026-05-11 · Cursor** — Asked for Streamlit UI polish (theme, tabs, metrics). Used CSS/theme ideas. **I rejected** pushing a local logger script to GitHub; **I kept** it machine-only and added `scripts/` to `.gitignore` so submission stays clean.

6. **2026-05-12 · Cursor** — Debugging Streamlit metric tiles not updating; assistant suggested rerender patterns. **I accepted** `st.rerun()` after runs and moving score parse order; **I verified** against a live Skill Gap output.

7. **2026-05-13 · Cursor** — README and memo drafts for rubric sections. Used outline text. **I personalized** findings, dates, and examples to match my logged runs in `evaluation/test_results.md`.

8. **2026-05-13 · Cursor** — Notebook execution timing before deadline; used `jupyter nbconvert --execute` command suggestion. **I ran** execution with my local Anaconda interpreter so outputs save in the `.ipynb` for submission.

---

**Progression:** early scaffolding → runtime/API fixes → RAG + prompt iterations → UI/eval polish → submission packaging.

**Where I overrode AI:** severity / logging / repo hygiene choices (entry 5) and all prompt wording I hand-edited after drafts (entry 4).
