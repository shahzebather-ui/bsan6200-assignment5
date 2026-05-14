# Business Memo: Job Fit Analyzer (Option B)

**To:** Hiring and analytics stakeholders  
**From:** Shahzeb Ather  
**Date:** May 13, 2026  
**Re:** BSAN6200 Assignment 5 — LLM + RAG prototype for resume–job comparison  

---

## Purpose

This memo summarizes a **Job Fit Analyzer** built for **Option B** of the course assignment: a small **retrieval-augmented generation (RAG)** pipeline plus a **Streamlit** application that compares **one candidate resume** to **multiple job descriptions (JDs)**. The goal is faster, more structured triage of fit, keyword overlap, and skill gaps than manual read-through alone, while keeping outputs grounded in the provided text.

---

## What we built

- **Inputs:** One resume (PDF or TXT) and **10** JD files under `data/job_descriptions/`, with optional **CSV metadata** for friendly labels in the UI.  
- **Processing:** JDs are **chunked** (default: **paragraph-based** chunks with overlap; **fixed character windows** were implemented for comparison in the notebook), embedded in **ChromaDB**, and **top‑k** chunks are retrieved per analysis type to condition the model.  
- **Outputs:** Three analyses — **Skill Gap Report**, **Keyword Alignment**, and **Fit Summary** — using the **Hugging Face Inference API** and **`Qwen/Qwen2.5-7B-Instruct`**.  
- **UI:** Streamlit app with **Analyze** vs **Resume** tabs (including **session resume upload**), a small **metrics row** (fit score and keyword % when parseable after a run), and **RAG chunk** expanders for transparency.

---

## Prompt iterations (v1 → v2 → v3)

1. **v1 (baseline)**  
   Standard three analyses with flexible bullet counts. Outputs were sometimes **generic** or **under-cited** relative to the JD.

2. **v2 (structure + evidence)**  
   Skill Gap was tightened to **exactly three strengths and three gaps**, each with a **short quote** from the JD or resume, plus a fixed **five** recommended actions and an explicit **fit score**. This improved **scannability** and **auditability** but recommendations could still feel **template-like**, and **severity of requirements** (must-have vs bonus) was not explicit.

3. **v3 (prioritization + brevity)**  
   Skill Gap gaps now require **[Severity: High / Medium / Low]** with simple rules tied to **must-have vs preferred/bonus** language, and recommendations were **capped at three** actions. In testing, severity labels **mostly** tracked the JD, with occasional **mismatches** when the model treated a **Bonus** line as **High** or when wording was ambiguous across chunks.

**Net:** v3 is the **submission** prompt set for Skill Gap; Keyword and Fit prompts stayed stable aside from the shared RAG context pattern.

---

## Evaluation approach

- **Quantitative:** Fit scores and keyword match rates as reported by the model, plus informal latency notes where captured.  
- **Qualitative:** Per-run notes in `evaluation/test_results.md` (output quality, what worked, what failed, next change).  
- **Coverage:** Multiple real JDs (e.g., analyst and operations-style roles) to stress-test **domain vocabulary** and **retrieval**.

**Failure patterns observed:** (1) occasional **severity vs JD language** inconsistency; (2) **keyword lists** sometimes noisy or duplicated; (3) **truncation risk** on very long outputs mitigated by raising generation limits and tightening bullet caps.

---

## Recommendations for use

- Treat outputs as **decision support**, not automated hiring decisions: always **spot-check** quotes against the JD and resume.  
- For production, add **human rubrics**, **calibration** on a labeled set, and **logging** of prompts/retrieved chunks for compliance.  
- **Next engineering steps (out of scope for this assignment):** post-process scores from structured JSON instead of regex; add **explicit must-have extraction** as a first-class retrieval query; fine-tune or swap models if cost and latency allow.

---

## Limitations

- **Single-resume** scope; no multi-candidate ranking.  
- **No ground-truth labels** for “true” fit — metrics are **model-reported**.  
- **Retrieval** depends on chunking and **top‑k**; missed must-haves in chunks can weaken gap detection.  
- **API and model variability** (latency, occasional formatting drift).

---

## Conclusion

The deliverable meets the course objective: an **end-to-end Option B** pipeline with **documented chunking**, **vector retrieval**, **three prompt iterations**, and **recorded qualitative evaluation**. The largest practical gain is **structured, cited skill-gap reporting** with **explicit prioritization** in v3; the main residual risk is **model consistency** on severity and long outputs, which should be monitored in any real deployment.

## Course recording (Zoom)

The assignment calls for a **short recording** that includes a **demo of the Streamlit app / code**. The intended format is **demo-first**: **screen-share the running app**, walk through one JD, show **retrieved chunks** and at least one full analysis path, and briefly point to the **notebook** and **`evaluation/test_results.md`** for rigor. A **full slide deck is not required**; at most, a **single title slide** (project name, Option B, your name) is optional if it helps you open cleanly.

*Draft for local editing — align wording with your final notebook screenshots and rubric before submission.*
