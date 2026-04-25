import streamlit as st


def simple_fit_estimate(resume_text: str, jd_text: str) -> int:
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    if not jd_words:
        return 0
    overlap = len(resume_words.intersection(jd_words))
    score = int((overlap / len(jd_words)) * 100)
    return max(0, min(score, 100))


st.set_page_config(page_title="Option B - Job Fit Analyzer", layout="wide")
st.title("Option B: Job Fit Analyzer")
st.caption("Compares resume content with a job description.")

st.subheader("Inputs")
resume_text = st.text_area("Paste your resume text", height=220)
jd_text = st.text_area("Paste one job description", height=220)

if st.button("Analyze Fit"):
    if not resume_text.strip() or not jd_text.strip():
        st.error("Please provide both resume and job description text.")
    else:
        fit_score = simple_fit_estimate(resume_text, jd_text)
        st.success(f"Estimated fit score: {fit_score}%")

        st.markdown("### Strengths (placeholder)")
        st.write("- Replace with LLM-generated top strengths.")

        st.markdown("### Gaps (placeholder)")
        st.write("- Replace with LLM-generated skill and experience gaps.")

        st.markdown("### Improvement Suggestions (placeholder)")
        st.write("- Replace with tailored next steps for the candidate.")
