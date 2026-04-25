# Option B Test Results

## Evaluation Goal
Evaluate how well the Option B pipeline identifies resume-job alignment, gaps, and actionable recommendations across multiple job postings.

## Test Matrix (fill one row per run)
| Run ID | Resume Version | JD ID | Prompt Version | Model | Retrieval Settings | Notes |
|---|---|---|---|---|---|---|
| R01 | resume_v1 | jd_sample_01 | v1 | hf-inference | top_k=3 | Baseline |
| R02 | resume_v1 | jd_sample_01 | v2 | hf-inference | top_k=5 | Added clearer rubric wording |
| R03 | resume_v1 | jd_sample_02 | v2 | hf-inference | top_k=5 | Second sample JD |

## Scoring Rubric (0-5 scale)
- **Fit signal quality:** Does the score/summary reflect true overlap?
- **Strength extraction quality:** Are strengths concrete and evidence-based?
- **Gap detection quality:** Are missing requirements correctly identified?
- **Actionability:** Are suggestions specific enough to act on?
- **Consistency:** Do repeated runs produce stable conclusions?

## Quantitative Notes (per run)
- Estimated fit score:
- Strength coverage (% of true strengths captured):
- Gap precision (% of listed gaps that are valid):
- Response latency (seconds):

## Prompt Iteration Log
1. **Version 1 (baseline):** "Compare resume and job description. Provide score, strengths, and gaps."
2. **Version 2 (structured):** Added required output schema, evidence snippets, and no-hallucination instruction.
3. **Version 3 (target):** Add weighting (must-have vs nice-to-have) and prioritize top 3 resume improvements.

## Qualitative Notes
- What looked correct:
- What looked weak:
- Hallucination or mismatch notes:
- Cases where score felt too high/too low:

## Failure Analysis
- Failure pattern:
- Probable root cause:
- Proposed fix:

## Next Actions
- Expand from sample JDs to 10+ real postings.
- Compare at least 2 prompt versions across same JD set.
- Record before/after improvements tied to rubric metrics.
