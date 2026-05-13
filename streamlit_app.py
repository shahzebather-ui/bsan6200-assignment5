"""
Assignment 5 -- Option B: Job Fit Analyzer
BSAN 6200 | Spring 2026

Run with: python -m streamlit run streamlit_app.py

YOUR TASKS (search for TODO):
1. Implement your chunking strategy
2. Write 3 analysis prompts (Skill Gap, Keyword Alignment, Fit Summary)
3. These must be developed and iterated in your notebook first
"""

import streamlit as st
import chromadb
from huggingface_hub import InferenceClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Job Fit Analyzer", page_icon="🎯", layout="wide")

# ── Config ──
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
TOP_K_CHUNKS = 5


# ══════════════════════════════════════════
# Helper functions
# ══════════════════════════════════════════

def load_text_file(filepath):
    """Load a .txt file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf_file(filepath):
    """Load a .pdf file."""
    from pypdf import PdfReader
    reader = PdfReader(filepath)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def load_file(filepath):
    """Load a .txt or .pdf file."""
    if filepath.endswith(".pdf"):
        return load_pdf_file(filepath)
    else:
        return load_text_file(filepath)


def load_all_jds(jd_dir="data/job_descriptions"):
    """Load all JD files from the directory."""
    docs = []
    if not os.path.exists(jd_dir):
        return docs
    for filename in sorted(os.listdir(jd_dir)):
        filepath = os.path.join(jd_dir, filename)
        if filename.endswith((".txt", ".pdf")):
            text = load_file(filepath)
            if text.strip():
                docs.append({"text": text, "source": filename})
    return docs


def load_resume(resume_dir="data/resume"):
    """Load the resume file (first .txt or .pdf found)."""
    if not os.path.exists(resume_dir):
        return ""
    for filename in os.listdir(resume_dir):
        if filename.endswith((".txt", ".pdf")):
            return load_file(os.path.join(resume_dir, filename))
    return ""


def ask_llm(hf_client, prompt):
    """Send a prompt to the LLM and return the response."""
    response = hf_client.chat_completion(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        # Skill Gap asks for many bullets; 500 often truncates mid-list.
        max_tokens=1800,
        temperature=0.1,
        stop=["\n\n\n"],
    )
    return response.choices[0].message.content.strip()


# ══════════════════════════════════════════
# TODO 1: Chunking strategy
# ══════════════════════════════════════════

def chunk_documents_paragraph(documents, max_chars=1200, overlap=150):
    """Strategy 1: merge paragraphs up to max_chars with tail overlap."""
    chunks = []
    for doc in documents:
        text = doc["text"].strip()
        source = doc["source"]
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        current = ""
        for p in paragraphs:
            if len(p) > max_chars:
                for part in p.replace(". ", ".\n").split("\n"):
                    part = part.strip()
                    if not part:
                        continue
                    if len(current) + len(part) + 2 <= max_chars:
                        current = f"{current}\n\n{part}".strip()
                    else:
                        if current:
                            chunks.append({"text": current, "source": source})
                        tail = current[-overlap:] if overlap and current else ""
                        current = f"{tail}\n\n{part}".strip() if tail else part
            else:
                if len(current) + len(p) + 2 <= max_chars:
                    current = f"{current}\n\n{p}".strip() if current else p
                else:
                    if current:
                        chunks.append({"text": current, "source": source})
                    tail = current[-overlap:] if overlap and current else ""
                    current = f"{tail}\n\n{p}".strip() if tail else p
        if current:
            chunks.append({"text": current, "source": source})
    return chunks


def chunk_documents_fixed_window(documents, window=900, stride=600):
    """Strategy 2: fixed-size character windows (for notebook comparison)."""
    chunks = []
    for doc in documents:
        text = doc["text"].strip()
        source = doc["source"]
        if not text:
            continue
        start = 0
        while start < len(text):
            piece = text[start : start + window]
            if piece.strip():
                chunks.append({"text": piece.strip(), "source": source})
            start += stride
    return chunks


def chunk_documents(documents):
    """Default pipeline chunker (paragraph-based)."""
    return chunk_documents_paragraph(documents)


def build_retrieval_query(analysis_type, jd_text, resume_text):
    """Short query for similarity search over JD chunks."""
    resume_snip = (resume_text[:500] + "…") if len(resume_text) > 500 else resume_text
    if analysis_type == "Skill Gap Report":
        return f"skills qualifications requirements responsibilities experience education\n{resume_snip}"
    if analysis_type == "Keyword Alignment":
        return f"keywords tools technologies must have preferred requirements\n{resume_snip}"
    return f"overall role fit responsibilities summary\n{jd_text[:400]}\n{resume_snip}"


def retrieve_jd_context(collection, source_filename, analysis_type, jd_text, resume_text, top_k=TOP_K_CHUNKS):
    """Retrieve top-k JD chunks for the selected posting (RAG context)."""
    q = build_retrieval_query(analysis_type, jd_text, resume_text)
    try:
        res = collection.query(
            query_texts=[q],
            n_results=top_k,
            where={"source": source_filename},
        )
    except Exception:
        res = collection.query(query_texts=[q], n_results=top_k)
    docs = (res.get("documents") or [[]])[0]
    metas = (res.get("metadatas") or [[]])[0]
    lines = []
    for i, d in enumerate(docs):
        src = metas[i].get("source", source_filename) if i < len(metas) else source_filename
        lines.append(f"[chunk {i + 1} | {src}]\n{d}")
    return "\n\n".join(lines) if lines else ""


# ══════════════════════════════════════════
# TODO 2: Analysis prompts
# Write your 3 analysis prompts below.
# Must be developed in your notebook first
# with 3+ iterations documented.
# ══════════════════════════════════════════

SKILL_GAP_PROMPT = """
You are a job-fit evaluator.

Task:
Compare the candidate resume to the job description and produce a skill gap report.

Rules:
- Use only the provided resume and JD text.
- Do not invent experience or certifications.
- Be concise and specific.

Output:
1) Matching Skills (5-10 bullets)
2) Missing Skills / Gaps (5-10 bullets)
3) Recommended Actions (5 bullets)
4) Fit Score (0-100) with a short explanation
"""


KEYWORD_PROMPT = """
You are a keyword alignment assistant.

Task:
Extract important keywords from the job description and check whether they appear
(or close equivalent appears) in the candidate resume.

Rules:
- Use only provided text.
- Avoid over-claiming matches.

Output:
1) Top JD Keywords (10-20)
2) Matched Keywords
3) Missing Keywords
4) Keyword Match Rate (%) = matched / total * 100
5) Top 3 keywords to add or emphasize in resume
"""


FIT_SUMMARY_PROMPT = """
You are a hiring-side reviewer.

Task:
Write a brief fit summary comparing this resume to the job description.

Rules:
- Use evidence from both texts.
- Keep it realistic and balanced.
- No hallucinations.

Output:
- Fit Summary (3-4 sentences)
- Top 3 Strengths (bullets)
- Top 3 Concerns (bullets)
- Recommendation: Strong Fit / Moderate Fit / Low Fit
"""


ANALYSIS_TYPES = {
    "Skill Gap Report": SKILL_GAP_PROMPT,
    "Keyword Alignment": KEYWORD_PROMPT,
    "Fit Summary": FIT_SUMMARY_PROMPT,
}


# ══════════════════════════════════════════
# Load resources (cached)
# ══════════════════════════════════════════

@st.cache_resource
def load_vectorstore():
    jd_docs = load_all_jds()
    if not jd_docs:
        return None, []
    chunks = chunk_documents(jd_docs)
    client = chromadb.Client()
    collection = client.create_collection("job_fit")
    collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[f"chunk_{i}" for i in range(len(chunks))],
    )
    return collection, jd_docs


@st.cache_data
def load_metadata():
    path = "data/jd_metadata.csv"
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()


@st.cache_resource
def load_llm():
    token = os.environ.get("HF_TOKEN", "")
    if not token:
        return None
    return InferenceClient(token=token)


# ══════════════════════════════════════════
# Analysis logic
# ══════════════════════════════════════════

def run_analysis(hf_client, analysis_prompt, jd_text, resume_text, retrieved_context=""):
    """Run analysis with optional RAG context from retrieved JD chunks."""
    ctx_block = ""
    if retrieved_context.strip():
        ctx_block = f"""
Retrieved excerpts from this job description (use as primary JD evidence; cite chunk numbers when helpful):
{retrieved_context}

"""
    full_prompt = f"""{analysis_prompt}
{ctx_block}
Full Job Description:
{jd_text}

Candidate Resume:
{resume_text}"""

    return ask_llm(hf_client, full_prompt)


# ══════════════════════════════════════════
# UI
# ══════════════════════════════════════════

collection, jd_docs = load_vectorstore()
metadata = load_metadata()
hf_client = load_llm()
resume_text = load_resume()

st.title("🎯 Job Fit Analyzer")
st.caption("Compare your resume against job descriptions.")

# ── Error checks ──
if not hf_client:
    st.error("HF_TOKEN not found. Add it to your .env file.")
    st.stop()

if collection is None:
    st.error("No JDs found in data/job_descriptions/. Add your job description files there.")
    st.stop()

if not resume_text:
    st.error("No resume found in data/resume/. Add your resume file there.")
    st.stop()

# ── Sidebar ──
with st.sidebar:
    st.header("About")
    st.write("This tool compares your resume against job descriptions using RAG.")
    st.write(f"**JDs loaded:** {len(jd_docs)}")
    st.write(f"**Resume loaded:** Yes")
    st.write(f"**Model:** {MODEL_ID}")
    st.write(f"**Retrieval top-k:** {TOP_K_CHUNKS}")
    st.divider()
    st.caption("BSAN 6200 | Assignment 5 | Option B")

# ── JD selector ──
col_select, col_analysis = st.columns([1, 1])

with col_select:
    st.subheader("1. Select a Job Description")

    if not metadata.empty:
        jd_options = {
            f"{row['company']} -- {row['title']}": row["filename"]
            for _, row in metadata.iterrows()
        }
    else:
        jd_options = {doc["source"]: doc["source"] for doc in jd_docs}

    selected_label = st.selectbox("Choose a JD:", list(jd_options.keys()))
    selected_filename = jd_options[selected_label]

    # Find the JD text
    jd_text = ""
    for doc in jd_docs:
        if doc["source"] == selected_filename:
            jd_text = doc["text"]
            break

    with st.expander("Preview job description"):
        st.text(jd_text[:1000] + ("..." if len(jd_text) > 1000 else ""))

with col_analysis:
    st.subheader("2. Choose Analysis Type")
    analysis_type = st.radio(
        "Select analysis:",
        list(ANALYSIS_TYPES.keys()),
    )

# ── Run analysis ──
st.divider()

if st.button("🔍 Run Analysis", type="primary", use_container_width=True):
    with st.spinner(f"Running {analysis_type}..."):
        try:
            prompt = ANALYSIS_TYPES[analysis_type]
            retrieved = retrieve_jd_context(
                collection, selected_filename, analysis_type, jd_text, resume_text
            )
            with st.expander("Retrieved JD chunks (RAG)", expanded=False):
                st.text(retrieved or "(no retrieval results)")
            result = run_analysis(hf_client, prompt, jd_text, resume_text, retrieved)
            st.subheader(f"Results: {analysis_type}")
            st.markdown(result)
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

st.divider()

if st.button("📊 Run All 3 Analyses", use_container_width=True):
    for name, prompt in ANALYSIS_TYPES.items():
        with st.spinner(f"Running {name}..."):
            try:
                retrieved = retrieve_jd_context(
                    collection, selected_filename, name, jd_text, resume_text
                )
                with st.expander(f"Retrieved chunks — {name}", expanded=False):
                    st.text(retrieved or "(no retrieval results)")
                result = run_analysis(hf_client, prompt, jd_text, resume_text, retrieved)
                st.subheader(name)
                st.markdown(result)
                st.divider()
            except Exception as e:
                st.error(f"{name} failed: {str(e)}")
