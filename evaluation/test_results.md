# Option B Test Results

## Evaluation Goal

Evaluate how well the Option B pipeline identifies resume-job alignment, gaps, and actionable recommendations across different job postings.

## Test Matrix


| Run ID | Resume Version | JD ID        | Prompt Version | Model        | Retrieval Settings | Notes                        |
| ------ | -------------- | ------------ | -------------- | ------------ | ------------------ | ---------------------------- |
| R01    | resume_v1      | jd_sample_01 | v1             | hf-inference | top_k=3            | Baseline                     |
| R02    | resume_v1      | jd_sample_01 | v2             | hf-inference | top_k=5            | Added clearer rubric wording |
| R03    | resume_v1      | jd_sample_02 | v2             | hf-inference | top_k=5            | Second sample JD             |


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

- Failure pattern: Outputs can become generic and miss evidence-based prioritization.
- Probable root cause: Prompt constraints were not strict on evidence citation and must-have weighting.
- Proposed fix: Enforce evidence citation, must-have-first ranking, and concise output rules.

### Run R05130038

- Date: 2026-05-13 00:44
- JD: `job4_investment_analyst_tamarsecurities.txt`
- Prompt version: v1
- Analysis type: Skill Gap Report
- Quant notes: fit score=75, keyword match=50%, latency=N/A
- Output summary: Model identified key skills that matched with Job Description for the role.
- What worked: Output was structured and aligned with job
- What failed: Missed some skills and some recommendations were too generic.
- Next change: Add constraint to avoid repeating similar skills.

### Run R05130045

- Date: 2026-05-13 00:53
- JD: `job4_investment_analyst_tamarsecurities.txt`
- Prompt version: v1
- Analysis type: Keyword Alignment
- Quant notes: fit score=75, keyword match=65%, latency=N/A
- Output summary: Matched 13 keywords.
- What worked: Keyword extraction was clear and the matched vs missing split was easy to interpret.
- What failed: Keyword ranking didn't prioritize must have skills.
- Next change: Add explicit words for handling terms such as SQL, ETL, and BI tool variants.

### Run R05130053

- Date: 2026-05-13 00:59
- JD: `job4_investment_analyst_tamarsecurities.txt`
- Prompt version: v1
- Analysis type: Fit Summary
- Quant notes: fit score=75, keyword match=50%, latency=N/A
- Output summary: Fit summary gave a good recommendation with many strengths for this role.
- What worked: Fit summary was concise and aligned with major JD requirements.
- What failed: Some statements were generic and lacked role-specific evidence from the JD and resume.
- Next change: Add instruction to cite one JD and one resume evidence phrase for each key claim.

### Run R05130100

- Date: 2026-05-13 01:03
- JD: `job5_data_analyst_coframe.txt`
- Prompt version: v1
- Analysis type: Skill Gap Report
- Quant notes: fit score=65, keyword match=80%, latency=N/A
- Output summary: Output was structured clearly and aligned with the selected analysis type.
- What worked: Response format was clear and concise.
- What failed: Some points were generic and lacked role-specific evidence.
- Next change: Prioritize must-have skills before optional/preferred criteria in scoring.

### Run R05130104

- Date: 2026-05-13 01:06
- JD: `job5_data_analyst_coframe.txt`
- Prompt version: v1
- Analysis type: Keyword Alignment
- Quant notes: fit score=65, keyword match=80%, latency=N/A
- Output summary: Model response was mostly relevant and followed the requested output structure.
- What worked: The response separated strengths and gaps in a readable way.
- What failed: Some important job description tools were not emphasized.
- Next change: Add one solid action item per missing skills and areas.

### Run R05130106

- Date: 2026-05-13 01:10
- JD: `job5_data_analyst_coframe.txt`
- Prompt version: v1
- Analysis type: Fit Summary
- Quant notes: fit score=65, keyword match=80%, latency=N/A
- Output summary: The recommendation was clear and consistent with identified gaps.
- What worked: The final recommendation was easy to interpret and decision-friendly.
- What failed: Some fit statements were generic and lacked direction.
- Next change: Add instruction to prioritize must-have qualifications before preferred ones.

### Run R05130111

- Date: 2026-05-13 01:15
- JD: `job10_derivatives_risk_and_operations_east_west_bank.txt`
- Prompt version: v1
- Analysis type: Skill Gap Report
- Quant notes: fit score=75, keyword match=40%, latency=N/A
- Output summary: Output highlighted role-relevant strengths while surfacing missing must-have skills.
- What worked: Recommendations were good and tied to identified missing skills.
- What failed: Some bullets repeated similar ideas instead of adding distinct insights.
- Next change: Ask for unique recommendations only, with no repeated action items.

### Run R05130115

- Date: 2026-05-13 01:18
- JD: `job10_derivatives_risk_and_operations_east_west_bank.txt`
- Prompt version: v1
- Analysis type: Keyword Alignment
- Quant notes: fit score=75, keyword match=40%, latency=N/A
- Output summary: Keyword output was structured and identified both matched and missing terms.
- What worked: Matched vs missing keyword separation was clear and easy to act on.
- What failed: Keyword ranking did not clearly prioritize must-have requirements.
- Next change: Add synonym mapping guidance for equivalent technical terms.

### Run R05130120

- Date: 2026-05-13 01:25
- JD: `job10_derivatives_risk_and_operations_east_west_bank.txt`
- Prompt version: v1
- Analysis type: Fit Summary
- Quant notes: fit score=75, keyword match=40%, latency=N/A
- Output summary: Fit summary delivered a balanced recommendation with clear strengths and concerns.
- What worked: Recommendation was clear and easy to interpret for hiring decisions.
- What failed: The final recommendation needed better explanation.
- Next change: Ask it to focus on the top 3 important gaps and top 3 matching skills.

### Run R05131149
- Date: 2026-05-13 11:56
- JD: `job4_investment_analyst_tamarsecurities.txt`
- Prompt version: v2
- Analysis type: Skill Gap Report
- Quant notes: fit score=70, keyword match=50%, latency=N/A
- Output summary: Skill gap now shows 3 strengths and 3 gaps, each with a short quote from the JD or resume.
- What worked: The format is clear and easier to check than before.
- What failed: Some quotes are short paraphrases, not exact copy-paste lines.
- Next change: Add High/Medium/Low labels for the 3 gaps for v3.



### Run R05131405
- Date: 2026-05-13 14:11
- JD: `job5_data_analyst_coframe.txt`
- Prompt version: v2
- Analysis type: Skill Gap Report
- Quant notes: fit score=75, keyword match=60%, latency=N/A
- Output summary: Three strengths had resume quotes; three gaps named missing tools; fit score 75.
- What worked: Strength bullets were specific and easy to verify from the quotes.
- What failed: ap bullets did not include matching job description quotes like the strengths did.
- Next change: Add strict rule:  no tool names in gaps unless job description explicitly lists them.



### Run R05131529
- Date: 2026-05-13 15:34
- JD: `job10_derivatives_risk_and_operations_east_west_bank.txt`
- Prompt version: v2
- Analysis type: Skill Gap Rerport
- Quant notes: fit score=70, keyword match=75%, latency=N/A
- Output summary: V2 skill gap gave 3 strengths and 3 gaps and a 70 fit score.
- What worked: Both sides used chunk-backed wording and gaps correctly stressed derivatives, compliance, and model validation versus the resume.
- What failed: The five recommended actions are fairly generic compared to the sharper, cited gap bullets.
- Next change: For v3, cap recommendations at three bullets and add High/Medium/Low severity on each gap.



### Run R05131544
- Date: 2026-05-13 15:50
- JD: `job4_investment_analyst_tamarsecurities.txt`
- Prompt version: v3
- Analysis type: Skill Gap Report
- Quant notes: fit score=75, keyword match=85%, latency=N/A
- Output summary: V3 gave 3 strengths, 3 severity gaps, 3 actions, fit 75.
- What worked: Severity tags and the three-item recommendation list made the report shorter and easier to scan than five actions in v2.
- What failed: Evidence was stronger on strengths than on one or two gap bullets.
- Next change: Freeze v3 code; document severity decisions and edge cases.



### Run R05131551
- Date: 2026-05-13 15:58
- JD: `job5_data_analyst_coframe.txt`
- Prompt version: v3
- Analysis type: Skill Gap Report
- Quant notes: fit score=85, keyword match=75%, latency=N/A
- Output summary: V3 gave 3 strengths with quotes, 3 severity-tagged gaps, 3 actions, fit 85, keyword match 75%.
- What worked: The 3 / 3 / 3 layout stayed tight and the three actions each pointed at one of the listed tool gaps.
- What failed: Recommended actions read a bit generic compared to the job description's exact tool name
- Next change: No further prompt or app changes planned; v3 is the last coded iteration documented.

