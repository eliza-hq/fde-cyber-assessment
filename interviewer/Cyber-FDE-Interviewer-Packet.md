# Cyber FDE Interviewer Packet

CONFIDENTIAL: interviewers only. Do not share with candidates.

**BLOCKED — NOT CLEARED FOR RELEASE.**

See RELEASE.md. The answer key is pending validation against the pinned Target.

Use this packet to prepare and calibrate, not to score live candidates against specific findings.

Do not distribute the assessment.

Draft v0.1 | 2026-11-12 | Owner: ____________________

## 1. Assessment at a glance

**Purpose.** Assess application security investigation and the ability to explain evidence, uncertainty, impact, and next steps to a customer.

| Stage | Format and purpose |
| --- | --- |
| Earlier interview | A separate defensibility check probes how the candidate justifies a decision and responds to new evidence. |
| Take-home | Approximately four hours of investigation and report writing, excluding initial setup. The candidate plans and conducts one to three rounds, then reports and documents next steps. |
| Presentation | A 30-minute customer-facing session, including discussion and questions, for a technical lead and a business owner. The candidate chooses the format. |

**Candidate package and target.** The fictional E Corp assessment uses the `assessment` branch of [eliza-hq/fde-cyber-erpnext-assessment](https://github.com/eliza-hq/fde-cyber-erpnext-assessment): upstream ERPNext tag `v16.34.0` plus the assessment package. The official image runs ERPNext 16.34.0 and Frappe 16.33.0. The root source matches the running target. Record the branch commit actually reviewed. The package uses synthetic fixtures, with no custom app or planted bugs. See [runtime verification](../docs/runtime-v16/VERIFICATION.md).

**Authorized boundary.**

- Test only the supplied local disposable Target and its explicitly authorized containers and source, on a controlled machine with no customer or production access.

- Use fictional data.

- Do not expose the Target, test external hosts, use denial-of-service techniques, send mail to real recipients, or upload Target data or credentials to third-party tools.

- Internet access is for setup and research, not testing.

- Containers alone do not establish isolation.

- If the runtime or isolation cannot be verified, the candidate must stop and contact the coordinator.

## 2. What success looks like

- Chooses a focused investigation plan and explains priorities, assumptions and tradeoffs.
- Uses observations to decide whether and how to iterate; stops within the time guidance and records what remains.
- Provides evidence another reviewer can follow, with preconditions, controls, limitations and confidence.
- Separates observed behavior from hypotheses. Correctly identifying a limitation or disproving a concern earns credit.
- Explains plausible impact and prioritizes proportionately for E Corp, without claiming more than the evidence supports.
- Communicates clearly to technical and nontechnical listeners and adjusts when challenged.
- Works within scope and explains tool and AI contributions and verification. Tool choice alone earns no credit.

A version or lockfile match alone does not establish vulnerability. Check installation, execution, reachability and relevant preconditions before asserting applicability.

## 3. Scoring rubric

Use this proposed rubric for Dry run calibration only.

Score observed behavior, not finding count.

A missing opportunity or setup failure may leave a dimension unscored; record why.

Scores and weights are not approved for live use.

| Dimension | 1 Below bar | 2 Approaching | 3 Meets | 4 Strong |
| --- | --- | --- | --- | --- |
| Plan and rationale | No coherent plan or priorities. | Lists checks with little rationale. | Prioritizes checks and explains assumptions. | Connects priorities to risk, time and tradeoffs. |
| Execution and iteration | Cannot explain actions or results. | Lists actions with little adaptation. | Explains each round and how evidence shaped the next or stopping. | Adjusts efficiently, explains alternatives and stopping decisions. |
| Evidence and reproducibility | Claims lack supporting evidence. | Some evidence, but key steps or context missing. | Gives relevant evidence, steps, inputs and controls sufficient to follow. | Another reviewer can reproduce or assess limits; controls isolate the claim. |
| Impact and priority | Impact asserted without basis. | Impact or ordering is vague; preconditions missing. | States plausible impact, preconditions and prioritized recommendations. | Connects impact and priority to customer context and material limitations. |
| Confidence and separation | Presents guesses as facts. | Labels some uncertainty but mixes claims and observations. | Separates observations, hypotheses and disproved concerns; calibrates confidence. | Updates confidence explicitly with supporting and contrary evidence. |
| Next tests | No useful next steps. | Generic tests without purpose. | Proposes focused next tests and why they matter. | Orders discriminating tests by uncertainty, value and constraints. |
| Tools and AI verification | Cannot explain tool or AI output; accepts it uncritically. | Names tools but verification is unclear. | States contributions and how outputs were checked. | Explains verification limits and uses independent checks where useful. |
| Scope and safety | Tests beyond authorization or disregards a boundary. | Notices some boundaries but leaves material gaps. | Respects boundaries and stops or asks when isolation is uncertain. | Anticipates boundary risks and explains safe choices and escalation. |
| Customer communication | Audience cannot follow claims or action. | Explains some details but misses an audience or questions. | Explains evidence, impact, confidence, priorities and next steps to both audiences. | Adapts language, handles challenge and helps both audiences decide what to do. |

### Deliverable to rubric trace

| Candidate deliverable | Rubric row(s) |
| --- | --- |
| Report: plan, rationale and assumptions | Plan and rationale; Confidence and separation |
| Report: rounds, decisions and stopping | Execution and iteration |
| Report: evidence, reproduction, failed tests and disproved concerns | Evidence and reproducibility; Confidence and separation |
| Report: impact, preconditions and prioritized recommendations | Impact and priority |
| Report: confidence and next tests | Confidence and separation; Next tests |
| Report: tools, AI contributions and checks | Tools and AI verification |
| Work within authorized boundaries | Scope and safety |
| 30-minute presentation, materials and discussion | Customer communication; Evidence and reproducibility; Impact and priority; Confidence and separation; Next tests |
| Defend approach and assumptions | Plan and rationale; Confidence and separation; Customer communication |

### Combining scores and hire signal

- **Proposed for calibration:** weight the nine dimensions equally.

- Calculate the mean only across scored dimensions and retain the evidence behind each score.

- A proposed positive signal is a mean of at least 3.0, with no score of 1 in scope and safety or confidence and separation.

- This is a discussion aid, not an automatic decision or approved hiring bar.

- Consider material safety concerns, missing evidence, accommodations and the whole interview record in a structured debrief.

- Do not treat unscored dimensions as zero.

- The Dry run must test weights, bar, score agreement and time expectations before use.

## 4. Stage-by-stage guide

### Earlier round defensibility check

**Suggested prompt:** “You have four hours to assess an unfamiliar application for E Corp. A scanner reports a serious issue, but you have not reproduced it. Explain what you would do next, what you would tell the customer now, and why.”

Use the same core prompt for every candidate. Follow up consistently:

- “How do you prove to me that your finding is accurate and I'm actually safe?”

- What evidence would change your confidence?

- What preconditions and safe controls would you check?

- What would you do if time or access ran out?

- How would you explain a negative result to a business owner?

- What would you prioritize instead if the issue proved inapplicable?

- **Strong:** Explains a risk-based sequence, verifies applicability safely, states uncertainty and stopping points, and changes the conclusion when evidence changes.

- **Weak:** Treats a scanner label as proof, cannot defend priorities, overstates impact, or cannot explain a safe next step.

Record specific statements; do not expect one tool or a predetermined finding.

### Report review checklist

| Requested element | Look for |
| --- | --- |
| Plan and rationale | Priorities, assumptions, time allocation and why the checks were chosen. |
| Execution in each round | Actions, what was learned, and how results shaped the next round or stopping decision. |
| Evidence and reproduction | Observations, inputs, steps, environment, controls and enough detail to assess or repeat the claim. |
| Impact and preconditions | A plausible affected party and consequence, prerequisites and limitations. |
| Confidence and assumptions | Clear separation of observations and hypotheses; failed tests and disproved concerns recorded. |
| Recommendations and priority | Proportionate ordering and rationale connected to evidence and impact. |
| Next tests | Specific unresolved questions, safe tests and reasons for their order. |
| Tools and AI | What each contributed and how its output was checked. |
| Defensibility | Choices and assumptions the candidate can explain and revise under challenge. |

### 30-minute customer presentation

Suggested timing:

- 3 minutes for context and scope;

- 10 minutes for prioritized results and evidence;

- 5 minutes for impact, confidence and limitations;

- 5 minutes for recommendations and next tests;

- 7 minutes for questions.

Adapt the flow to the candidate’s chosen format while preserving discussion time.

**Ask in the final:** “How do you prove to me that your finding is accurate and I'm actually safe?”

**Technical lead prompts:**

- “What did you observe, and how could we reproduce it?”

- “Which preconditions and negative controls matter?”

- “What evidence would change your conclusion?”

**Business owner prompts:**

- “What does this mean for E Corp?”

- “What should we do first, and why?”

- “How certain are you, and what remains unknown?”

**Good looks like:** The candidate gives a clear, proportionate account to both personas, distinguishes evidence from inference, handles a challenge without defensiveness, and names practical next actions.

A well-supported limitation or negative result is a valid outcome.

## 5. Things to look out for

### Green flags

- Verifies installation, execution, reachability and preconditions before calling an advisory applicable; uses positive and negative controls when appropriate.
- Explains why a test failed or a concern was disproved and updates confidence accordingly.
- Documents a stopping point around the four-hour investigation and report-writing guidance and prioritizes remaining tests.
- States a setup problem promptly and stops if safe operation cannot be verified. Treat this as a signal about the materials, not automatically as a candidate failure.
- Translates technical evidence into a decision and an appropriately qualified business consequence.

### Red flags

- Claims applicability from a version or lockfile match alone, or pastes scanner output without validation. Relies on unverified AI output.
- Mixes hypotheses with observed behavior or offers no negative controls where they would distinguish a claim.
- Tests external hosts, uses denial of service, imports real data, exposes the Target, or uploads Target data or credentials to third-party tools.
- Asks for token or cost budgets upfront instead of framing and prioritizing the assessment. Probe the reason; this is a discussion signal, not an automatic failure.
- Says “found nothing” without a confidence level and the next tests that would change it.
- Takes excessive time or conducts excessive rounds beyond the four-hour and one-to-three-round guidance without a justified stopping point or remaining work.
- Uses jargon with the business owner without explaining impact or action.

### Interviewer pitfalls

- Do not reward tool sophistication over reasoning, penalize an honest “no confirmed vulnerability,” anchor on an expected answer, or leak the rubric.

- Ask what evidence supports the candidate's conclusion, including a negative conclusion.

- Record evidence rather than impressions.

## 6. Answer key and findings

Consult the access-controlled [answer key](private/answer-key.md) for validation and controls, and the [advisory triage](private/advisory-triage.md) for applicability status and sources. The answer key is pending validation; do not treat version matches or hypotheses as confirmed findings. Credit defensible negative and limited conclusions.

## 7. Fairness, consistency and confidentiality

- Score independently before debrief.

- Record specific evidence and distinguish missing evidence from poor performance.

- Resolve differences with examples, not consensus pressure.
- Give every candidate the same core prompts, boundaries, materials and evaluation criteria.

- Use consistent follow-ups and record material deviations.
- Coordinate accommodations through the designated hiring process.

- Apply agreed adjustments consistently and protect private details.

- Do not infer ability from an accommodation request.
- Explain the approximately four-hour investigation and report-writing guidance, excluding initial setup.

- Answer time questions consistently; record agreed adjustments, setup delays and stopping points.

- Do not invent a penalty before calibration.
- Keep the Interviewer package, answer key and evaluation notes in access-controlled storage, outside candidate channels and Drive folders shared with candidates.

- Check access and storage history before release.

## 8. Scorecard template

Complete one copy per candidate after the relevant stages.

Use 1–4 or N/O (not observed); cite evidence and explain N/O.

Proposed scores are for Dry run calibration until release and rubric approval.

Candidate: ____________________  Interviewer: ____________________  Date: __________

| Dimension | Score | Evidence notes |
| --- | --- | --- |
| Plan and rationale | ____ | ______________________________ |
| Execution and iteration | ____ | ______________________________ |
| Evidence and reproducibility | ____ | ______________________________ |
| Impact and priority | ____ | ______________________________ |
| Confidence and separation | ____ | ______________________________ |
| Next tests | ____ | ______________________________ |
| Tools and AI verification | ____ | ______________________________ |
| Scope and safety | ____ | ______________________________ |
| Customer communication | ____ | ______________________________ |
| Flags and context | — | ______________________________ |
| Overall recommendation and rationale | — | ______________________________ |

## 9. Open items before use

- **Answer key:** Validate findings and controls on the pinned runtime (slice 3).
- **Dry run:** Time an agent run using the packaged repository, score it, and apply fixes (slice 5).
- **Independent package review:** Inspect the exact package and history, record SHA-256 and review evidence (slice 6).
- **Approval:** Obtain Jordan's approval before pushing or distributing (slice 7). See [release checklist](../RELEASE-CHECKLIST.md).

## 10. Packet use and ownership

Owner: ____________________  Reviewer: ____________________  Last reviewed: __________

This draft supports internal preparation only.

The owner tracks the open items, updates this Interviewer package after independent validation and calibration, and records the release decision under the release checklist.

Do not distribute the assessment while RELEASE.md remains blocked.