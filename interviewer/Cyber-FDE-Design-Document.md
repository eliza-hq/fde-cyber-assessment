CONFIDENTIAL: interviewers only. Do not share with candidates.

**Status: BLOCKED. Do not distribute the assessment.**

# Cyber FDE Assessment Design

## Purpose and scope

This assessment tests application security investigation and customer communication. Candidates investigate a disposable ERPNext deployment for the fictional customer E Corp, explain their evidence and uncertainty, and recommend next steps. Interviewers assess how well candidates make and defend decisions under time constraints.

The exercise focuses on application behavior and security reasoning. It excludes DevSecOps pipelines, infrastructure engineering and production hardening, multiple targets or difficulty tiers, automated scoring, real customer data and external targets.

## Assessment stages

1. **Earlier interview:** A separate defensibility check asks the candidate to respond to an unverified scanner result, explain safe next steps, and communicate current uncertainty to E Corp.
2. **Take-home:** Allow approximately four hours for investigation and report writing, excluding setup. Candidates plan and conduct one to three rounds, use evidence to decide whether to continue, and document a stopping point and remaining work.
3. **Customer presentation:** In 30 minutes including discussion, the candidate presents to a technical lead and a business owner. The candidate chooses the format and explains evidence, impact, confidence, priorities and next steps.

## Design choices

**A stock, pinned target.** The official frappe/erpnext:v16.34.0 image runs ERPNext 16.34.0 and Frappe 16.33.0. The public source branch corresponds to the running first-party source, subject to the asset and dependency qualifications in runtime verification. A common target makes the exercise repeatable. There is no custom app and no planted bug.

**Reasoning over finding count.** A version or scanner match alone does not prove applicability. Candidates should check preconditions and distinguish observations from hypotheses. A supported negative result, disproved concern or explicit limitation earns credit. The answer key must reflect what is actually verified on the pinned runtime.

**Public and private separation.** Candidate materials contain the scenario, scope, setup and deliverables. The interviewer packet, answer key, triage and dry-run record stay private. This preserves the exercise and supports consistent assessment.

**Why the target changed.** The earlier ERPNext 17 develop attempt required a large amd64 custom build under emulation and had dependency and lockfile drift. It achieved limited diagnostic runtime checks but did not establish a reproducible candidate environment or complete lifecycle coverage. The stable v16 image offers an official, reproducible, native arm64 target. The earlier attempt is archived and is not shipped.

## Evaluation

The packet's nine dimensions are plan and rationale; execution and iteration; evidence and reproducibility; impact and priority; confidence and separation; next tests; tools and AI verification; scope and safety; and customer communication. Score observed behavior, not the number of findings. Record evidence for each score and explain dimensions not observed.

The rubric, equal weights and proposed threshold are **drafts for dry-run calibration only**, not approved live scoring or an automatic hiring decision. The proposed discussion signal is a mean of at least 3.0 across scored dimensions, with no 1 in scope and safety or confidence and separation. Do not count an unscored dimension as zero. Consider accommodations, safety and the whole interview record in a structured debrief.

### Deliverable to rubric trace

| Candidate evidence | Rubric dimensions |
| --- | --- |
| Plan, assumptions and rationale | Plan and rationale; confidence and separation |
| Rounds, decisions and stopping | Execution and iteration |
| Evidence, reproduction, failed tests and disproved concerns | Evidence and reproducibility; confidence and separation |
| Impact, preconditions and recommendations | Impact and priority |
| Confidence and next tests | Confidence and separation; next tests |
| Tool and AI contributions and checks | Tools and AI verification |
| Work within authorized boundaries | Scope and safety |
| Presentation and discussion | Customer communication; evidence and reproducibility; impact and priority; confidence and separation; next tests |
| Defense of approach and assumptions | Plan and rationale; confidence and separation; customer communication |

Ask in both the earlier round and final: “How do you prove to me that your finding is accurate and I'm actually safe?” Probe evidence that would change confidence, safe controls, limits and next actions. Use the same core prompt and consistent follow-ups. Score independently before debrief and resolve differences with examples.

Red flags include treating a version match or unverified AI output as proof; mixing observation and hypothesis; testing outside scope; asking for token or cost budgets upfront instead of framing priorities; saying “found nothing” without confidence and next tests; excessive time or rounds without a justified stopping point; and jargon that leaves the business owner without an action. The budget question is a discussion signal, not an automatic failure. A setup problem is a signal about the materials, not automatically a candidate failure.

## Risks and safeguards

The target is intentionally disposable. Limit testing to the supplied local target, its containers and source on a controlled machine. Use synthetic data, keep the target on localhost, and prohibit external testing, denial of service, real mail recipients and uploads of target data or credentials to third parties. Internet access is for setup and research. Containers alone do not establish isolation; stop and contact the coordinator if safe operation cannot be verified.

Setup friction can consume assessment time. The candidate README states prerequisites and excludes setup from the four-hour investigation. The pending dry run must test timing, ambiguity, scoring agreement and the materials. Access-controlled interviewer materials and release review reduce the risk of exposing private evaluation guidance.

## Status and open decisions

Release is blocked. A person must validate the answer key on the runtime and then complete a timed, scored dry run from the public branch. Model-provider cyber safeguards blocked agents from both gates. Apply fixes and repeat affected checks. The fork's default branch must then be set to assessment. The exact package was independently reviewed and pushed with Jordan's approval; distribution is not yet approved. The rubric, weights and hiring signal remain subject to calibration. See RELEASE.md for the current release record and the private human gate instructions for the sequence.
