# Cyber FDE Interviewer Guide

**Confidential — interviewers only, never share with candidates**

Cyber | E Corp customer portal launch

Cleared for live use; see RELEASE.md. The answer key in section 6 and Appendix A has not been validated on the running instance. Score candidates on reasoning, evidence and calibration, never on whether they found a specific advisory.



## 1. Assessment at a glance

**Purpose.** Assess application security investigation and the ability to explain evidence, uncertainty, impact, and next steps to a customer.

| Stage | Format and purpose |
| --- | --- |
| Earlier interview | A separate defensibility check probes how the candidate justifies a decision and responds to new evidence. |
| Take-home | Approximately four hours of investigation and report writing, excluding initial setup. The candidate plans and conducts one to three rounds, then reports and documents next steps. |
| Presentation | A 30-minute customer-facing session, including discussion and questions, for a technical lead and a business owner. The candidate chooses the format. |

**Candidate package and target.** The fictional E Corp assessment uses the self-contained candidate/ package distributed as a single archive. The official image runs ERPNext 16.34.0 and Frappe 16.33.0. Source to review is upstream ERPNext tag v16.34.0 (https://github.com/frappe/erpnext/tree/v16.34.0) and Frappe tag v16.33.0 (https://github.com/frappe/frappe/tree/v16.33.0), and the application source inside the running containers at /home/frappe/frappe-bench/apps. The image also contains built front-end assets and some differently resolved JavaScript dependency versions. The package uses synthetic fixtures, with no custom app or planted bugs. See runtime verification.

**Authorized boundary.**

- Test only the supplied local disposable Target and its explicitly authorized containers and source, on a controlled machine with no customer or production access.

- Use fictional data.

- Do not expose the Target, test external hosts, use denial-of-service techniques, send mail to real recipients, or upload Target data or credentials to third-party tools.

- Internet access is for setup and research, not testing.

- Containers alone do not establish isolation.

- If the runtime or isolation cannot be verified, the candidate must stop and contact the coordinator.

### Review the work

Focus: Assess portal data isolation, internal role separation and advisory applicability. Look for a reasoned plan, one to three investigation rounds, reproducible evidence, preconditions, confidence, prioritized recommendations and next tests.

Judgment: Distinguish observations from hypotheses. A supported negative or limited result is valid. A version match alone does not establish advisory applicability; check fix presence, reachability and preconditions. Do not reward finding count or tool choice.

Safety and tools: Expect work within the local target and authorized boundaries, with tool and AI contributions explained and checked. If safe operation cannot be verified, the candidate should stop and contact the coordinator.

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

Use this rubric for live scoring and calibration.

Score observed behavior, not finding count. An undetermined or bounded advisory conclusion earns credit when the candidate explains the missing evidence and the next discriminating check; a failed reproduction alone does not prove it inactive. Only one portal user is supplied, so some preconditions cannot be fully exercised in four hours.

A missing opportunity or setup failure may leave a dimension unscored; record why.

Scores and weights are approved for live use (Jordan, 2026-11-17). Recalibrate after the first few candidates.

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

- **Weighting:** weight the nine dimensions equally.

- Calculate the mean only across scored dimensions and retain the evidence behind each score.

- A proposed positive signal is a mean of at least 3.0, with no score of 1 in scope and safety or confidence and separation.

- This is a discussion aid, not an automatic decision or approved hiring bar.

- Consider material safety concerns, missing evidence, accommodations and the whole interview record in a structured debrief.

- Do not treat unscored dimensions as zero.

- A recommended dry run can test weights, bar, score agreement and time expectations.

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

Plan about 15 minutes for the candidate to present and the remaining 15 minutes for discussion and questions. Expect a more technical bar than the RAG final: concrete metrics, numbers, controls and evidence of rigor where appropriate. Do not demand invented precision.

Suggested presentation flow:

- 2 minutes for context and scope;
- 7 minutes for prioritized results and evidence;
- 3 minutes for impact, confidence and limitations;
- 3 minutes for recommendations and next tests.

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

A strong candidate can say: “I'm 20% confident there's nothing; here are the four additional tests I'd run next.” Reward the calibration and discriminating tests, not the specific percentage.

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

The answer key is **static and unvalidated against the running instance**. Do not treat any row as a confirmed finding or require candidates to find one. Appendix A retains the advisory inventory and static patch comparisons. Version matches, fixed-version metadata and missing candidate checks do not prove exploitability or fix absence. Reachability and conditions remain unverified. Credit defensible negative and limited conclusions.

The person validating the key should first examine these in-range priorities, all unvalidated with paths and conditions unverified:

- GHSA-877j-rg2w-v649 (ERPNext; customer documents via print and portal views; fixed in 16.52.0) — focus area 1, portal data isolation.
- GHSA-29xj-69vf-fmmh (ERPNext; selling documents and RFQs in customer and supplier portals; fixed in 16.52.0) — focus area 1, portal data isolation.
- GHSA-45p2-2pp7-f8w2 (ERPNext; Payment Entries outside user permissions in Accounts; fixed in 16.52.0) — focus area 2, internal role separation.
- GHSA-r8px-9662-x39c (Frappe; authenticated file read; ordinary role per advisory, path unverified) — focus area 1, portal data isolation, or focus area 2, internal role separation, where the affected files cross those boundaries.

GHSA-cc74-rc2g-p7hw (Selling/Buying SQL injection) and GHSA-9pp9-wgp9-3p3j (upload path traversal/RCE) are secondary: they are relevant only if a candidate links them to focus area 1 or 2 with evidence. Two related file containment checks are missing in the pinned source, but their attribution to those advisories is unverified. Other in-range portal advisories GHSA-v93q-wwv7-hm54 and GHSA-qr6v-w65q-v497, and role advisories such as GHSA-6vch-gx2g-m2cv, are reasonable alternatives. The key must not require a specific advisory. Use positive and negative controls and document results before calling anything applicable.

An undetermined or bounded advisory outcome earns credit when the candidate explains the missing evidence and next discriminating check. A failed reproduction alone does not prove an advisory inactive. Only one portal user is supplied, so some preconditions cannot be fully exercised in four hours.

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
- Keep this guide, the answer key and evaluation notes in access-controlled storage, outside candidate channels and Drive folders shared with candidates.

- Check access and storage history when maintaining the materials.

## Appendix A Advisory inventory and static patch comparisons

Use this inventory to plan validation, not as a runtime answer key. Retrieved 2026-11-12. No entry is validated against the running instance. Repository inventory is incomplete (Frappe 97 and ERPNext first 100; pagination failed). Source paths, configuration, authentication and conditions are unchecked except the priority notes above. The 12 reclassifications below reflect published 16.x ranges from the later static audit; they do not establish fix presence. “Undetermined” means no verified patch comparison, not absence. “Not compared” means the row was outside the audit's affected/unknown scope. The 243 audited unique repository and dependency pairs were all undetermined; neither tag metadata nor a range proves source fix or runtime behavior. Upstream tags are not verified image commits; built frontend assets and some JavaScript dependency resolutions differ.

Ranges ending in an arrow show published affected range and patched version, including older major versions. “Not affected” is a version classification only. Scanner matches require installed artifact, execution, reachability and preconditions; no JS or OS package scan was done. Scanner publication cutoff was not established. Original scanner duplicates are retained. No result proves the application safe.

### Repository advisory inventory

| Advisory ID | Component | Affected ranges / fixes | Fix present? | Reachability / preconditions | Status |
| --- | --- | --- | --- | --- | --- |
| GHSA-37jh-f235-72qp | frappe | <15.122.0 → 15.122.0; <16.50.0 → 16.50.0 | Undetermined | Unauthorized document submission and modification due to missing validation in Document.update(); path and conditions unverified | version-affected |
| GHSA-qrxv-3vjh-gpx7 | frappe | <16.36.0 → 16.36.0; <15.121.2 → 15.121.2 | Undetermined | Sandbox bypass via imported functions leaking into Jinja globals through module-path hooks; path and conditions unverified | version-affected |
| GHSA-6pmg-vc6m-6wrr / CVE-2026-119144 | frappe | <16.21.0 | Not compared | Possibility of Server Side Template Injection; path and conditions unverified | not-affected |
| GHSA-9pp9-wgp9-3p3j | frappe | < 16.34.0 → 16.34.0; < 15.121.0 → 15.121.0 | Undetermined | Remote code execution via path traversal; path and conditions unverified | version-affected |
| GHSA-h3mh-9vmc-cpfg | frappe | <16.35.0 → 16.35.0; <15.121.1 → 15.121.1 | Undetermined | OAuth2 password grant bypasses two-factor authentication; path and conditions unverified | version-affected |
| GHSA-r8px-9662-x39c | frappe | <16.33.1 → 16.33.1; <15.120.1 → 15.120.1 | Undetermined | Authenticated Arbitrary File Read via File Attachment Handling; path and conditions unverified | version-affected |
| GHSA-wrh5-p77r-jpvq | frappe | <v16.33.0 → v16.33.0; <v15.120.0 → v15.120.0 | Undetermined | Unauthorized users can send sms via the API; path and conditions unverified | not affected by version (reclassified) |
| GHSA-vp4r-5v6w-r962 | frappe | <16.33.0 | Not compared | Blind SQL Injection via X-Frappe-Request-Id header; path and conditions unverified | not-affected |
| GHSA-p4w2-9mr5-6prj | frappe | <16.33.0 | Not compared | Blind SQL Injection in frappe.desk.doctype.event.event.get_events; path and conditions unverified | not-affected |
| GHSA-c76w-4wg2-hpgf | frappe | <16.32.0 | Not compared | Stored spreadsheet formula injection in CSV and XLSX exports; path and conditions unverified | not-affected |
| GHSA-h9jq-7pgf-hw8q | frappe | <16.33.0 | Not compared | restrict_ip allowlist bypassed for API key, OAuth, and header-based authentication; path and conditions unverified | not-affected |
| GHSA-22v9-hw3x-x59w | frappe | < 16.25.0 | Not compared | Unauthorised modification of records due to missing validation; path and conditions unverified | not-affected |
| GHSA-7cxg-q8x5-rpjh | frappe | <16.35.0 → 16.35.0; <15.121.1 → 15.121.1 | Undetermined | Broken Access Control in File list/report queries; path and conditions unverified | version-affected |
| GHSA-55m4-gj6h-q6rc | frappe | <16.31.0 | Not compared | Disabled users continue to receive Document Follow email notifications; path and conditions unverified | not-affected |
| GHSA-8v98-cfpm-9p67 / CVE-2026-109601 | frappe | <v16.30.0 → v16.30.0; <v15.117.0 → v15.117.0 | Undetermined | Arbitrary file read via an attribute in outgoing email HTML; path and conditions unverified | not affected by version (reclassified) |
| GHSA-hxfh-hh23-fvch | frappe | <v16.31.0 → v16.31.0; <v15.118.0 → v15.118.0 | Undetermined | Stored XSS in dashboard chart; path and conditions unverified | not affected by version (reclassified) |
| GHSA-r8gf-89pc-pmv3 | frappe | <16.30.0 | Not compared | IDOR via an SMS Settings' API; path and conditions unverified | not-affected |
| GHSA-7vpf-q96h-59x4 / CVE-2026-66059 | frappe | <16.23.0 | Not compared | Field-level permission bypass via Document Follow; path and conditions unverified | not-affected |
| GHSA-fgx7-fvpx-mw3g / CVE-2026-66058 | frappe | <16.23.0 | Not compared | Unrestricted access to a Document Follow API; path and conditions unverified | not-affected |
| GHSA-78c5-55xg-jm7m / CVE-2026-66057 | frappe | <v16.29.0 → v16.29.0; <v15.116.0 → v15.116.0 | Undetermined | Open Redirect via Unsanitized OAuth State Param.; path and conditions unverified | not affected by version (reclassified) |
| GHSA-p25m-7rvg-6fvr / CVE-2026-66003 | frappe | <v15.115.0 → v15.115.0 | Undetermined | Access control bypass via REST API; path and conditions unverified | unknown |
| GHSA-c2xv-c53h-qvr5 / CVE-2026-66002 | frappe | <v16.27.0 → v16.27.0; <v15.115.0 → v15.115.0 | Undetermined | User Enumeration via PDDR; path and conditions unverified | not affected by version (reclassified) |
| GHSA-2ph8-x773-8p2x / CVE-2026-66001 | frappe | <16.26.0 | Not compared | Improper Authorization in OAuth2 Consent Endpoint; path and conditions unverified | not-affected |
| GHSA-cgwf-xgph-hxgm / CVE-2026-63654 | frappe | tbd → tbd; tbd → tbd | Undetermined | Unauthenticated Workflow approval; path and conditions unverified | unknown |
| GHSA-2c6h-wv85-fxvj / CVE-2026-62315 | frappe | tbd → tbd; tbd → tbd | Undetermined | Mass assignment in client endpoint; path and conditions unverified | unknown |
| GHSA-3vqc-c545-w7jg / CVE-2026-58503 | frappe | <v16.16.0 | Not compared | Unauthenticated User Enumeration via reset_password; path and conditions unverified | not-affected |
| GHSA-58w2-4cjg-hvp6 / CVE-2026-55852 | frappe | <16.23.0 | Not compared | TarSlip RCE in Package Import; path and conditions unverified | not-affected |
| GHSA-mf6r-q34j-pjw7 / CVE-2026-55823 | frappe | <16.23.0 | Not compared | Possibility of SQL injection in reportview; path and conditions unverified | not-affected |
| GHSA-wcm9-vvcc-r8pr / CVE-2026-66000 | frappe | <16.23.0 | Not compared | Stale authorization in Document Follow allows revoked users to continue receiving document data; path and conditions unverified | not-affected |
| GHSA-rx6h-4p83-m76x / CVE-2026-53569 | frappe | tbd → tbd; tbd → tbd | Undetermined | Missing authorization in toggle_like and mark_as_seen; path and conditions unverified | unknown |
| GHSA-pj59-9hv9-rmrv | frappe | <16.17.0 | Not compared | Authenticated SSRF / LFI via pdfkit; path and conditions unverified | not-affected |
| GHSA-r24j-xrj8-273q / CVE-2026-49394 | frappe | <16.19.0 | Not compared | Auth. bypass via update_page; path and conditions unverified | not-affected |
| GHSA-7f28-gm9h-q6rg / CVE-2026-49391 | frappe | <16.19.0 | Not compared | Stored XSS via Data Import; path and conditions unverified | not-affected |
| GHSA-fwrv-4rw4-97fw / CVE-2026-48127 | frappe | <16.20.0 | Not compared | Arbitrary File Attachment Injection via File-Handling API Endpoints; path and conditions unverified | not-affected |
| GHSA-cjjx-3v2x-37mf / CVE-2026-47765 | frappe | <v16.20.0 → v16.20.0; <v15.110.0 → v15.110.0 | Undetermined | Lack of Permissions in restore/bulk_restore; path and conditions unverified | not affected by version (reclassified) |
| GHSA-w8g7-j846-j248 / CVE-2026-47422 | frappe | <= v16.18.2 → > v16.18.2; <= v15.107.5 → > v15.107.5 | Undetermined | Unrestricted API access to an API in reportview; path and conditions unverified | not affected by version (reclassified) |
| GHSA-89m3-vggh-725v / CVE-2026-47278 | frappe | <16.18.3 | Not compared | Comment Spoofing; path and conditions unverified | not-affected |
| GHSA-wx8j-cw4r-vrhv / CVE-2026-47199 | frappe | <v16.18.3 → v16.18.3; <v15.108.0  → v15.108.0 | Undetermined | check_safe_sql_query Permits SELECT INTO OUTFILE; path and conditions unverified | not affected by version (reclassified) |
| GHSA-3w78-3cj3-p949 / CVE-2026-47194 | frappe | <v16.18.3 → v16.18.3; <v15.108.0 → v15.108.0 | Undetermined | Host header poisoning can redirect magic login links to an attacker-controlled domain; path and conditions unverified | not affected by version (reclassified) |
| GHSA-mcr4-jc52-ww6x / CVE-2026-47185 | frappe | <16.18.0 | Not compared | Broken Access Control in Workspace Save API; path and conditions unverified | not-affected |
| GHSA-gvg7-4p32-j648 / CVE-2026-47182 | frappe | < 16.17.4 | Not compared | Broken Access Control on Private Files; path and conditions unverified | not-affected |
| GHSA-78rj-jch8-42m8 / CVE-2026-44976 | frappe | <16.17.4 | Not compared | IDOR in update_onboarding_step; path and conditions unverified | not-affected |
| GHSA-9cxj-48g3-jx22 / CVE-2026-44975 | frappe | <16.17.4 | Not compared | Missing authorization on reset form tours; path and conditions unverified | not-affected |
| GHSA-9c55-cq5r-qj5x / CVE-2026-44206 | frappe | <v16.17.4 → v16.17.4; <v15.107.2 → v15.107.2 | Undetermined | DB Schema Enumeration; path and conditions unverified | not affected by version (reclassified) |
| GHSA-cw6v-39qx-7r74 / CVE-2026-44207 | frappe | < 16.17.0 | Not compared | Insecure Direct Object Reference for email accounts; path and conditions unverified | not-affected |
| GHSA-rx63-c3fh-8926 / CVE-2026-53568 | frappe | <v16.17.4 → v16.17.4; <v15.107.2 → v15.107.2 | Undetermined | Stored XSS in Frappe Report/List View.; path and conditions unverified | not affected by version (reclassified) |
| GHSA-xh7m-j2j2-82f2 / CVE-2026-44208 | frappe | <16.17.0 | Not compared | IDOR in submit_discussion(); path and conditions unverified | not-affected |
| GHSA-q6m6-759h-46jp / CVE-2026-50026 | frappe | <v16.17.0 → v16.17.0; <v15.107.0 → v15.107.0 | Undetermined | Lack of permissions checks in 'relink' and 'set_email_password' endpoints; path and conditions unverified | not affected by version (reclassified) |
| GHSA-2wx6-8gmq-x4fw / CVE-2026-44205 | frappe | < 15.106.0 → 15.106.0 | Undetermined | Stored Cross-Site Scripting (XSS) in User Profile through Image Upload; path and conditions unverified | unknown |
| GHSA-w4p4-fp9m-47gj / CVE-2026-42219 | frappe | <16.19.0 | Not compared | Path Traversal via 'download_backups'; path and conditions unverified | not-affected |
| GHSA-h9hf-57r4-cm65 / CVE-2026-41581 | frappe | <16.16.0 | Not compared | Possible SQL Injection via get_blog_list; path and conditions unverified | not-affected |
| GHSA-234v-jfr8-v2f8 / CVE-2026-41482 | frappe | <16.18.3 | Not compared | Possible Path Traversal and Local File Inclusion via Chrome PDF Generator; path and conditions unverified | not-affected |
| GHSA-vxmp-h244-wv3r / CVE-2026-47739 | frappe | <16.16.0 | Not compared | Stored XSS in Note; path and conditions unverified | not-affected |
| GHSA-67rf-pxgh-vfqv / CVE-2026-39352 | frappe | <16.15.0 | Not compared | Arbitrary File Read via Path Traversal; path and conditions unverified | not-affected |
| GHSA-583g-fg76-fhfr / CVE-2026-35614 | frappe | <16.14.0 | Not compared | Possibility of SQL injection in bulk_update; path and conditions unverified | not-affected |
| GHSA-8ggw-hfr6-rw3x / CVE-2026-39351 | frappe | <16.14.0 | Not compared | Unrestricted Doctype access via API exploit; path and conditions unverified | not-affected |
| GHSA-2c4m-999q-xhx4 / CVE-2026-31877 | frappe | <15.84.0 → 15.84.0; <14.99.0 → 14.99.0 | Undetermined | Possibility of SQL Injection due to improper field sanitization; path and conditions unverified | unknown |
| GHSA-mggg-hmjm-j6c2 / CVE-2026-31878 | frappe | <16.6.0 | Not compared | Possible SSRF by any authenticated user; path and conditions unverified | not-affected |
| GHSA-qmhf-rgx2-8p25 / CVE-2026-31879 | frappe | <16.10.0 | Not compared | Workspace modification and stored XSS due to improper resource ownership checks; path and conditions unverified | not-affected |
| GHSA-w3g7-m7xr-2w38 / CVE-2026-29081 | frappe | <15.100.0  → 15.100.0 ; <14.100.1 → 14.100.1 | Undetermined | Possibility of SQL Injection due to improper fieldname sanitization; path and conditions unverified | unknown |
| GHSA-5h4c-9p23-4c3m / CVE-2026-29077 | frappe | <15.98.0 → 15.98.0; <14.100.0 → 14.100.0 | Undetermined | Broken Access Control in DocShare; path and conditions unverified | unknown |
| GHSA-vm63-r48g-7wqh / CVE-2026-28436 | frappe | 16.11.0 → 16.11.0; 15.102.0 → 15.102.0 | Undetermined | Stored XSS in avatar_macro.html; path and conditions unverified | unknown |
| GHSA-7m8v-g2pr-h2f7 / CVE-2026-25956 | frappe | <15.94.0 → 15.94.0; <14.99.14 → 14.99.14 | Undetermined | XSS and Open Redirect in Sign Up; path and conditions unverified | unknown |
| GHSA-qq98-vfv9-xmxh / CVE-2025-68929 | frappe | <15.88.1 → 15.88.1; <14.99.6 → 14.99.6 | Undetermined | Possibility of RCE due to SSTI; path and conditions unverified | unknown |
| GHSA-cx24-w5gm-5vv9 | frappe | <15.91.1  → 15.91.1 ; <14.99.10 → 14.99.10 | Undetermined | Authenticated XSS via leaderboard; path and conditions unverified | unknown |
| GHSA-xj39-3g4p-f46v / CVE-2025-68953 | frappe | <15.88.1 → 15.88.1; <14.99.6 → 14.99.6 | Undetermined | Path traversal allowed reading certain files; path and conditions unverified | unknown |
| GHSA-mp93-8vxr-hqq9 / CVE-2025-66205 | frappe | <15.86.0 → 15.86.0; <14.99.2 → 14.99.2 | Undetermined | Possibility of SQL Injection due to improper validations; path and conditions unverified | unknown |
| GHSA-v4wg-gqfr-rpjm / CVE-2025-66206 | frappe | <15.86.0 → 15.86.0; <14.99.2 → 14.99.2 | Undetermined | Path traversal allowed reading certain files; path and conditions unverified | unknown |
| GHSA-j9jr-qrpj-g855 / CVE-2025-62407 | frappe | <15.83.0 → 15.83.0; <14.98.0 → 14.98.0 | Undetermined | Open Redirect on Login Page; path and conditions unverified | unknown |
| GHSA-qrq5-v93p-8xhw | frappe | <15.86.0 → 15.86.0; <14.99.2 → 14.99.2 | Undetermined | Possible LDAP injection due to unsanitised inputs; path and conditions unverified | unknown |
| GHSA-mggw-6xqj-rphj / CVE-2025-52048 | frappe | <15.72.0 → 15.72.0; <14.96.10 → 14.96.10 | Undetermined | Possibility of SQL injection due to missing validation; path and conditions unverified | unknown |
| GHSA-6rpr-2hjx-w9vp / CVE-2025-55732 | frappe | <15.74.2 → 15.74.2; <14.96.15 → 14.96.15 | Undetermined | Possibility of SQL Injection due to improper validations; path and conditions unverified | unknown |
| GHSA-5p8f-568f-vfq2 / CVE-2025-55731 | frappe | <15.74.2 → 15.74.2; <14.96.15 → 14.96.15 | Undetermined | Possibility of Authenticated SQL Injection due to improper validations; path and conditions unverified | unknown |
| GHSA-cprh-gp85-wxvq / CVE-2025-28062 | frappe | <15.72.0  → 15.72.0 ; <14.96.10 → 14.96.10 | Undetermined | Account takeover via CSRF; path and conditions unverified | unknown |
| GHSA-p284-r7rh-wq7j / CVE-2025-52898 | frappe | <15.58.0 → 15.58.0; <14.94.3 → 14.94.3 | Undetermined | Account takeover via password reset token leakage; path and conditions unverified | unknown |
| GHSA-hv29-66qg-2v6p / CVE-2025-52896 | frappe | <15.57.0 → 15.57.0; <14.94.2 → 14.94.2 | Undetermined | Authenticated XSS via data import; path and conditions unverified | unknown |
| GHSA-mhj8-jfhf-mcw9 / CVE-2025-52895 | frappe | <15.58.0 → 15.58.0; <14.94.3 → 14.94.3 | Undetermined | Possibility of SQL injection due to improper validations; path and conditions unverified | unknown |
| GHSA-6phg-4wmq-h5h3 / CVE-2025-30217 | frappe | <14.93.2 → 14.93.2; <15.55.0 → 15.55.0 | Undetermined | Possibility of SQL injection due to improper validations; path and conditions unverified | unknown |
| GHSA-v342-4xr9-x3q3 / CVE-2025-30213 | frappe | <14.91.0 → 14.91.0; <15.52.0 → 15.52.0 | Undetermined | Possibility of Remote Code Execution due to improper validation; path and conditions unverified | unknown |
| GHSA-qrv3-jc3h-f3m6 / CVE-2025-30214 | frappe | <14.89.0 → 14.89.0; <15.51.0 → 15.51.0 | Undetermined | Information disclosure leading to account takeover; path and conditions unverified | unknown |
| GHSA-3hj6-r5c9-q8f3 / CVE-2025-30212 | frappe | <14.89.0  → 14.89.0 ; <15.51.0 → 15.51.0 | Undetermined | Possibility of SQL injection due to improper validations; path and conditions unverified | unknown |
| GHSA-gjqf-v2f6-962h | frappe | <15.41.0 → 15.41.0; <14.81.4 → 14.81.4 | Undetermined | Privilege escalation via document action; path and conditions unverified | unknown |
| GHSA-7g27-q225-j894 / CVE-2024-34074 | frappe | <=15.25.0 → 15.26.0; <=14.73.0 → 14.74.0 | Undetermined | Open redirect on login page; path and conditions unverified | unknown |
| GHSA-hq5v-q29v-7rcw / CVE-2024-27105 | frappe | <15.16.0 | Not compared | File Permissions can by bypassed using certain endpoints; path and conditions unverified | not-affected |
| GHSA-fxfv-7gwx-54jh / CVE-2024-24813 | frappe | <=14.63.0 → 14.64.0 | Undetermined | SQL Injection from reporting logic; path and conditions unverified | unknown |
| GHSA-7p3m-h76m-hg9v / CVE-2024-24812 | frappe | < 15.5.0 → 15.5.0; <14.59.0 → 14.59.0 | Undetermined | Frappe Authenticated Reflected Cross site scripting (XSS) in portal pages; path and conditions unverified | unknown |
| GHSA-v3vh-7qx4-f582 | frappe | <=14.58.0 → 14.59.0; <=15.4.1 → 15.5.0 | Undetermined | frappe.flags.in_safe_exec can become False while executing a Server Script; path and conditions unverified | unknown |
| GHSA-v248-pv3c-jvgw | frappe | <15.3.0 → 15.4.0; <14.57.0 → 14.58.0 | Undetermined | HTML injection in printview; path and conditions unverified | unknown |
| GHSA-439c-3956-r8q7 / CVE-2023-51769 | frappe | <14.49.0 → 14.49.0 | Undetermined | Cross-Site Scripting (XSS) Attack on exceptions and Blog Page; path and conditions unverified | unknown |
| GHSA-j2w9-8xrr-7g98 / CVE-2023-46127 | frappe | <14.49.0 → 14.49.0 | Undetermined | Possible HTML injection by any Desk user; path and conditions unverified | unknown |
| GHSA-38fg-mjcm-3hc6 | frappe | >14.0.0,<14.45.0 → 14.45.0 | Undetermined | Error logs could potentially leak secrets; path and conditions unverified | unknown |
| GHSA-4jj9-5vgc-gc4j | frappe | <14.31.0 → 14.31.0; 13.52.0 → 13.52.0 | Undetermined | Possible HTML Injection attack; path and conditions unverified | unknown |
| GHSA-53wh-f67g-9679 / CVE-2023-41328 | frappe | < 13.46.1  → 13.46.1; <14.20.0 → 14.20.0 | Undetermined | Possibility of limited SQL injection due to insufficient validation; path and conditions unverified | unknown |
| GHSA-wp7j-3w22-93j6 | frappe | <13.46.1 → 13.46.1; <14.20.0 → 14.20.0 | Undetermined | html2text is not safe on user input; path and conditions unverified | unknown |
| GHSA-whww-ggp5-r2xq | frappe | < 13.22.0 → 13.22.0 | Undetermined | Improper Authorization while renaming docs; path and conditions unverified | unknown |
| GHSA-7xv4-ggpj-g48q | frappe | <13.32.0 → 13.32.0 | Undetermined | Weak authentication when accessing print view using key; path and conditions unverified | unknown |
| GHSA-f939-v9q6-j3wg | frappe | < 13.46.3 → 13.46.3; < 14.21.1 → 14.21.1 | Undetermined | Improper Access Control for Email Templates; path and conditions unverified | unknown |
| GHSA-cc74-rc2g-p7hw | erpnext | < 15.121.6 → 15.121.6; < 16.37.0 → 16.37.0 | Undetermined | Possibility of SQL injection in the Selling and Buying modules due to missing validation; path and conditions unverified | version-affected |
| GHSA-ggr3-x356-w97h | erpnext | < 16.34.0 | Not compared | Unauthorised modification of bulk transaction logs in the Utilities module due to missing validation; path and conditions unverified | not-affected |
| GHSA-grg4-q5gc-4g4x | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to asset depreciation data of other companies in the Assets module due to missing validation; path and conditions unverified | version-affected |
| GHSA-45p2-2pp7-f8w2 | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to Payment Entries outside the user's permissions in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-chqg-f85c-wxr7 | erpnext | < 16.34.0 | Not compared | Unauthorised access to subscription plan details of invoices in the Accounts module due to missing validation; path and conditions unverified | not-affected |
| GHSA-6937-44rq-87xr | erpnext | < 16.34.0 | Not compared | Unauthorised access to Timesheet billing data in the Projects module due to missing validation; path and conditions unverified | not-affected |
| GHSA-9jrr-9pr6-7mv8 | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Exposure of imported supplier e-invoices as public files in the Regional module; path and conditions unverified | version-affected |
| GHSA-c3mc-qh7f-hwcv | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised stopping and closing of Work Orders of other companies in the Manufacturing module due to missing validation; path and conditions unverified | version-affected |
| GHSA-mmcf-jq27-crrp | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised closing of Purchase Orders of other companies in the Buying module due to missing validation; path and conditions unverified | version-affected |
| GHSA-jfr9-q72f-854x | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised closing of Sales Orders of other companies in the Selling module due to missing validation; path and conditions unverified | version-affected |
| GHSA-fjj8-qq2m-h96w | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised reposting of accounting entries in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-98p6-cv49-h8c3 | erpnext | < 15.124.2 → 15.124.2; < 16.53.0 → 16.53.0 | Undetermined | Unauthorised access to item valuation and average purchase cost in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-8mhv-pfp8-m66q | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to party addresses through Tax Rule in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-rcpm-332h-mj8f | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to inter-company invoice and order items in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-6vch-gx2g-m2cv | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to account balances through a dashboard chart in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-gj65-6744-3fv4 | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Stored cross-site scripting in CRM notes due to missing validation; path and conditions unverified | version-affected |
| GHSA-64h3-xccr-q5jr | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to source documents through Payment Requests in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-5jjr-hp7q-gmwr | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised creation of POS Invoice Merge Logs in POS due to missing validation; path and conditions unverified | version-affected |
| GHSA-42cf-qgvq-xv9h | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Asset details in the Assets module due to missing validation; path and conditions unverified | version-affected |
| GHSA-x2f8-27qm-r3hf | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised Stock Reservation Entries beyond Sales Order limits in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-77q9-p3mx-p357 | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised BOM replacement in the Manufacturing module due to missing validation; path and conditions unverified | version-affected |
| GHSA-v3gf-jphf-f4xp | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised unreconciliation of payments in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-qrv3-vxh2-xx3g | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Bank Transaction amounts in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-9jx6-f65v-r6h7 | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised modification of bank reconciliation in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-4mg4-7qq3-phxc | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised creation of Serial No and Batch records in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-93gm-m6q2-39pc | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised status modification of Period Closing Voucher processing in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-877j-rg2w-v649 | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to customer documents through print and portal views due to missing validation; path and conditions unverified | version-affected |
| GHSA-hfj8-f2p9-f2xf | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to Sales Order items in the Selling module due to missing validation; path and conditions unverified | version-affected |
| GHSA-v93q-wwv7-hm54 | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to Project costing in the customer portal due to missing validation; path and conditions unverified | version-affected |
| GHSA-29xj-69vf-fmmh | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to complete selling documents and RFQs in the customer and supplier portals due to missing validation; path and conditions unverified | version-affected |
| GHSA-crxr-qmq5-mm3q | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Bank Transactions of other companies in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-xmw8-rg38-x88j | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to supplier portal records through a party identity mix-up due to missing validation; path and conditions unverified | version-affected |
| GHSA-qr6v-w65q-v497 | erpnext | < 15.124.0 → 15.124.0; < 16.52.0 → 16.52.0 | Undetermined | Unauthorised access to Issues in the customer portal due to missing validation; path and conditions unverified | version-affected |
| GHSA-6xf4-gr7h-2h57 | erpnext | < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to stock value in Stock dashboards due to missing validation; path and conditions unverified | version-affected |
| GHSA-7455-jhmp-j2h2 | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Activity Cost rates in the Projects module due to missing validation; path and conditions unverified | version-affected |
| GHSA-gqm4-wpw8-qrc9 | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Serial No and Batch ledgers in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-26pv-59j4-p5m7 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to e-invoice files in the Regional module due to missing validation; path and conditions unverified | version-affected |
| GHSA-6g2x-j4rj-hr5c | erpnext | < 15.123.0 → 15.123.0; < 16.51.0 → 16.51.0 | Undetermined | Unauthorised access to stock balances of restricted warehouses in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-5c7v-wfg4-j4g2 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to POS Profile cashiers in POS due to missing validation; path and conditions unverified | version-affected |
| GHSA-x6mc-x6wm-h5jc | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Taxes and Charges Templates in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-qxrv-9vhj-49xm | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to loyalty point balances in the Selling module due to missing validation; path and conditions unverified | version-affected |
| GHSA-hf2q-xhq6-q394 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to payment allocations in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-w3rc-76j9-46jq / CVE-2026-124316 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to Material Requests in the Buying module due to missing validation; path and conditions unverified | version-affected |
| GHSA-4h65-m5q4-xwc4 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to the Chart of Accounts in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-m9wx-ccvr-729q | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to Bank Statement Import files in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-rcp6-4mfg-757h | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to taxes and charges of transactions in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-p7rx-846g-j6hr | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Payment Terms Templates in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-58wx-2f38-8f44 | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised access to Payment Term settings in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-q6rj-xw5g-c4j7 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to Loyalty Program terms in the Selling module due to missing validation; path and conditions unverified | version-affected |
| GHSA-xw35-vc29-fjxw | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to POS Opening Entries in POS due to missing validation; path and conditions unverified | version-affected |
| GHSA-x7vm-cw74-82wv | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to warehouse-wise stock quantities in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-3xh3-23fp-77m7 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to actual stock quantities in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-wvgx-whr3-44vr | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to valuation rates in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-3f93-crcf-9p9j | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to Sales Order and Purchase Order values in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-45w5-68c8-75vp | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to purchase cost data in the Assets module due to missing validation; path and conditions unverified | version-affected |
| GHSA-w587-ghqf-6jpp | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to BOM costs in the Manufacturing module due to missing validation; path and conditions unverified | version-affected |
| GHSA-h7xr-2wpr-7444 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to Item master data in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-5q53-5vm3-cjq8 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to Communications in the CRM and Support modules due to missing validation; path and conditions unverified | version-affected |
| GHSA-g966-fmq7-gp99 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to private files in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-2f98-mq8r-pvrh | erpnext | < 15.122.0 → 15.122.0; < 16.50.0 → 16.50.0 | Undetermined | Possibility of SQL injection due to missing validation; path and conditions unverified | version-affected |
| GHSA-f3vx-j6r6-67c7 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised creation of Serial No and Batch records and file access in the Stock module due to missing validation; path and conditions unverified | version-affected |
| GHSA-w264-5p9f-hfwm / CVE-2026-124314 | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to open activities in the CRM module due to missing validation; path and conditions unverified | version-affected |
| GHSA-m668-9q43-8g29 | erpnext | < 15.124.2 → 15.124.2; < 16.53.0 → 16.53.0 | Undetermined | Unauthorised access and modification of data due to missing validation; path and conditions unverified | version-affected |
| GHSA-gjr3-hvp7-6pgm | erpnext | < 16.36.0 → 16.36.0 | Undetermined | Unauthorised cancellation of Stock Reservation Entries in the Manufacturing module due to missing validation; path and conditions unverified | version-affected |
| GHSA-g7r2-v98g-6wcr | erpnext | < 16.35.0 → 16.35.0; < 15.121.3 → 15.121.3 | Undetermined | Unauthorised access to sensitive data due to missing validation; path and conditions unverified | version-affected |
| GHSA-x267-fgf5-54q9 | erpnext | < 15.124.2 → 15.124.2; < 16.50.0 → 16.50.0 | Undetermined | Unauthorised modification of clearance dates in the Accounts module due to missing validation; path and conditions unverified | version-affected |
| GHSA-f6fx-777q-q9jp | erpnext | < 15.121.4 → 15.121.4; < 16.36.0 → 16.36.0 | Undetermined | Unauthorised access to child table rows of transactions due to missing validation; path and conditions unverified | version-affected |
| GHSA-734c-hv9r-mg2c | erpnext | < 16.23.0 | Not compared | Stored cross-site scripting due to missing validation; path and conditions unverified | not-affected |
| GHSA-v38v-9h2p-hr8v | erpnext | < 16.34.0 | Not compared | Possibility of SQL injection due to missing validation; path and conditions unverified | not-affected |
| GHSA-9vph-hqmm-g7hq | erpnext | < 16.34.0 | Not compared | Unauthorised access to data due to missing validation; path and conditions unverified | not-affected |
| GHSA-xp5c-86f4-7ppf | erpnext | < 16.32.0 | Not compared | Possibility of SQL injection due to missing validation; path and conditions unverified | not-affected |
| GHSA-pg3r-7236-pg74 | erpnext | < 16.32.0 | Not compared | Unauthorised Document modification due to missing validation; path and conditions unverified | not-affected |
| GHSA-p4jx-mqwq-66cj | erpnext | < 16.34.0 | Not compared | Unauthorised modification of data due to missing validation; path and conditions unverified | not-affected |
| GHSA-f99r-gp2w-xghj | erpnext | < 16.33.0 | Not compared | Stored cross-site scripting due to missing validation; path and conditions unverified | not-affected |
| GHSA-wp9w-rxmg-6pfj | erpnext | < 16.34.0 | Not compared | Unauthorised status modification due to missing validation; path and conditions unverified | not-affected |
| GHSA-qcff-6669-j3gj | erpnext | < 16.34.0 | Not compared | Unauthorised access to financial data due to missing validation; path and conditions unverified | not-affected |
| GHSA-vg6r-89q7-wh34 | erpnext | < 16.34.0 | Not compared | Unauthorised record creation due to missing validation; path and conditions unverified | not-affected |
| GHSA-cgjf-xw8x-qjjc | erpnext | < 15.121.3 → 15.121.3; < 16.35.0 → 16.35.0 | Undetermined | Unauthorised modification of data due to missing validation; path and conditions unverified | version-affected |
| GHSA-vr45-2p9x-3vjc | erpnext | < 16.34.0 | Not compared | Unauthorised record creation due to missing validation; path and conditions unverified | not-affected |
| GHSA-wwgm-3pv3-gmqh | erpnext | < 16.23.0 | Not compared | Unauthorised access to party records due to missing validation; path and conditions unverified | not-affected |
| GHSA-2r76-j6jj-jj56 | erpnext | < 16.34.0 | Not compared | Unauthorised Document modification due to missing validation; path and conditions unverified | not-affected |
| GHSA-49wp-r82c-j825 | erpnext | < 15.121.1 → 15.121.1; < 16.34.2 → 16.34.2 | Undetermined | Unauthorised Document modification due to missing validation; path and conditions unverified | version-affected |
| GHSA-cgxw-2996-9vj3 | erpnext | < 16.33.0 | Not compared | Unauthorised access to personal data due to missing validation; path and conditions unverified | not-affected |
| GHSA-726x-68g4-fj9v | erpnext | < 15.121.3 → 15.121.3; < 16.35.0 → 16.35.0 | Undetermined | Unauthorised access to financial data due to missing validation; path and conditions unverified | version-affected |
| GHSA-794x-fhm7-58j7 | erpnext | < 16.34.1 → 16.34.1 | Undetermined | Unauthorised invocation of internal methods due to missing validation; path and conditions unverified | version-affected |
| GHSA-mp29-fjc5-h86p | erpnext | < 16.34.2 → 16.34.2 | Undetermined | Possibility of SQL injection due to missing validation; path and conditions unverified | version-affected |
| GHSA-q6qw-66cm-f9wj | erpnext | < 16.33.0 | Not compared | Unauthorised access to financial data due to missing validation; path and conditions unverified | not-affected |
| GHSA-5wpj-6rvp-9ff7 / CVE-2026-108374 | erpnext | < 16.34.0 | Not compared | Unauthorised status modification due to missing validation; path and conditions unverified | not-affected |
| GHSA-7j2w-hg27-8g3q | erpnext | < 15.121.3 → 15.121.3; < 16.35.0 → 16.35.0 | Undetermined | Unauthorised sending of transactional email due to missing validation; path and conditions unverified | version-affected |
| GHSA-pr7v-95jp-gwwv | erpnext | < 16.34.0 | Not compared | Unauthorised access to data due to missing validation; path and conditions unverified | not-affected |
| GHSA-jp5q-723q-g826 | erpnext | < 16.32.0 | Not compared | Possibility of SQL injection due to missing validation; path and conditions unverified | not-affected |
| GHSA-jfwr-g9v2-57c9 | erpnext | < 16.33.0 | Not compared | Unauthorised access to data due to missing validation; path and conditions unverified | not-affected |
| GHSA-rv4r-c8v3-3hrc | erpnext | < 16.32.0 | Not compared | Account takeover via stored cross-site scripting; path and conditions unverified | not-affected |
| GHSA-h787-3x6w-8x4m | erpnext | < 16.34.0 | Not compared | Possibility of SQL injection due to missing validation; path and conditions unverified | not-affected |
| GHSA-562g-3qrh-3w2f | erpnext | < 16.15.0 | Not compared | Unauthorised record creation due to missing validation; path and conditions unverified | not-affected |
| GHSA-g72f-g9wf-42vr | erpnext | < 16.26.0 | Not compared | Unauthorised access to financial data due to missing validation; path and conditions unverified | not-affected |
| GHSA-fwgg-5fp9-rg78 | erpnext | < 16.14.0 | Not compared | Unauthorised modification of master data due to missing validation; path and conditions unverified | not-affected |
| GHSA-73jx-q3gp-r24f | erpnext | < 16.21.0 | Not compared | Possibility of SQL injection due to missing validation; path and conditions unverified | not-affected |
| GHSA-rqv5-h4rv-w57m | erpnext | < 16.8.0 | Not compared | Possibility of SQL injection due to missing validation; path and conditions unverified | not-affected |
| GHSA-c496-q7g2-62vv | erpnext | < 16.22.0 | Not compared | Unauthorised modification of records due to missing validation; path and conditions unverified | not-affected |

### Python dependency scanner inventory

| Advisory ID | Component | Affected ranges / fixes | Fix present? | Reachability / preconditions | Status |
| --- | --- | --- | --- | --- | --- |
| PYSEC-2026-4322 | brotli 1.2.0 | ECOSYSTEM: introduced 0, fixed 1.2.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 1.2.1 |
| PYSEC-2026-4322 | brotli 1.2.0 | ECOSYSTEM: introduced 0, fixed 1.2.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 1.2.1 |
| PYSEC-2026-4320 | certifi 2026.7.22 | ECOSYSTEM: introduced 2019.03.09, fixed 2026.10.18 | Undetermined | Execution and conditions unverified | Scanner match; fix 2026.10.18 |
| PYSEC-2026-4320 | certifi 2026.7.22 | ECOSYSTEM: introduced 2019.03.09, fixed 2026.10.18 | Undetermined | Execution and conditions unverified | Scanner match; fix 2026.10.18 |
| CVE-2026-112940 | filelock 3.20.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.2.1 |
| CVE-2026-112913 | filelock 3.20.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.2.1 |
| CVE-2026-112936 | filelock 3.20.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.0.9 |
| CVE-2026-112910 | filelock 3.20.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.2.1 |
| CVE-2026-112909 | filelock 3.20.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.2.1 |
| CVE-2026-112915 | filelock 3.20.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.2.1 |
| CVE-2026-114145 | gitpython 3.1.61 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 3.2.1 |
| CVE-2026-110859 | gitpython 3.1.61 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 3.2.0 |
| CVE-2026-110858 | gitpython 3.1.61 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 3.2.0 |
| CVE-2026-110856 | gitpython 3.1.61 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 3.2.0 |
| CVE-2026-110857 | gitpython 3.1.61 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 3.2.0 |
| CVE-2026-110855 | gitpython 3.1.61 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 3.2.0 |
| PYSEC-2026-4114 | oauthlib 3.3.1 | ECOSYSTEM: introduced 3.0.0, fixed 4.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 4.0.0 |
| PYSEC-2026-4114 | oauthlib 3.3.1 | ECOSYSTEM: introduced 3.0.0, fixed 4.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 4.0.0 |
| CVE-2026-49272 | oauthlib 3.3.1 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 4.0.1 |
| PYSEC-2026-2860 | pdfkit 1.0.0 | ECOSYSTEM: introduced 0, last_affected 1.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix none listed |
| PYSEC-2026-2860 | pdfkit 1.0.0 | ECOSYSTEM: introduced 0, last_affected 1.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix none listed |
| PYSEC-2026-4327 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4328 | pillow 12.3.0 | ECOSYSTEM: introduced 11.3.0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4326 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4339 | pillow 12.3.0 | ECOSYSTEM: introduced 11.0.0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4340 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4343 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4334 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4337 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4341 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4330 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4338 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4335 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4336 | pillow 12.3.0 | ECOSYSTEM: introduced 11.2.1, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4331 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4332 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4329 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4333 | pillow 12.3.0 | ECOSYSTEM: introduced 12.0.0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4342 | pillow 12.3.0 | ECOSYSTEM: introduced 11.0.0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| PYSEC-2026-4363 | pillow 12.3.0 | ECOSYSTEM: introduced 0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112895 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112400 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112897 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112395 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112404 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112899 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112900 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112893 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112891 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112390 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112401 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112391 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112894 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112406 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112399 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112892 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-112393 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-96638 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-96640 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-96778 | pillow 12.3.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| GHSA-78g4-xqwv-q3g8 | pillow 12.3.0 | ECOSYSTEM: introduced 11.1.0, fixed 13.0.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 13.0.0 |
| CVE-2026-119196 | pyasn1 0.6.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 0.6.5 |
| CVE-2026-119194 | pyasn1 0.6.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 0.6.5 |
| CVE-2026-119197 | pyasn1 0.6.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 0.6.5 |
| CVE-2026-119195 | pyasn1 0.6.4 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 0.6.5 |
| PYSEC-2026-4145 | pyjwt 2.13.0 | ECOSYSTEM: introduced 0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4146 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.11.0, last_affected 2.13.0 | Undetermined | Execution and conditions unverified | Scanner match; fix none listed |
| PYSEC-2026-4149 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.4.0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4152 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.9.0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4144 | pyjwt 2.13.0 | ECOSYSTEM: introduced 0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4143 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.13.0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4148 | pyjwt 2.13.0 | ECOSYSTEM: introduced 0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4140 | pyjwt 2.13.0 | ECOSYSTEM: introduced 0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4141 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.0.0a1, fixed 2.15.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.15.0 |
| PYSEC-2026-4147 | pyjwt 2.13.0 | ECOSYSTEM: introduced 0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4151 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.13.0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4150 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.13.0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4142 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.13.0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-4183 | pyjwt 2.13.0 | ECOSYSTEM: introduced 2.1.0, fixed 2.15.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.15.0 |
| GHSA-pxh4-856f-4h89 | pyjwt 2.13.0 | ECOSYSTEM: introduced 0, fixed 2.14.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.14.0 |
| PYSEC-2026-3910 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.16.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.16.1 |
| PYSEC-2026-3911 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.16.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.16.1 |
| PYSEC-2026-3913 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.16.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.16.0 |
| PYSEC-2026-4153 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.18.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.18.0 |
| PYSEC-2026-4154 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.18.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.18.1 |
| PYSEC-2026-4160 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.19.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.19.0 |
| PYSEC-2026-4159 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.19.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.19.0 |
| PYSEC-2026-4156 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.18.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.18.1 |
| PYSEC-2026-4155 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.18.1 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.18.1 |
| PYSEC-2026-4158 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.17.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.17.0 |
| PYSEC-2026-4157 | pypdf 6.15.0 | ECOSYSTEM: introduced 0, fixed 6.19.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 6.19.0 |
| CVE-2026-113792 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.20.1 |
| CVE-2026-113795 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.20.0 |
| CVE-2026-113793 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.20.1 |
| CVE-2026-113794 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.20.0 |
| CVE-2026-113786 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.1 |
| CVE-2026-113791 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.0 |
| CVE-2026-113790 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.0 |
| CVE-2026-113789 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.0 |
| CVE-2026-115572 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.2 |
| CVE-2026-115585 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.2 |
| CVE-2026-115580 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.2 |
| CVE-2026-119208 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.3 |
| CVE-2026-119206 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.3 |
| CVE-2026-119209 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.3 |
| CVE-2026-119207 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.3 |
| CVE-2026-119203 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.4 |
| CVE-2026-119205 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.4 |
| CVE-2026-119204 | pypdf 6.15.0 | package range not found in OSV record | Undetermined | Execution and conditions unverified | Scanner match; fix 6.21.4 |
| PYSEC-2026-4177 | urllib3 2.7.0 | ECOSYSTEM: introduced 1.10.3, fixed 2.8.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.8.0 |
| PYSEC-2026-4176 | urllib3 2.7.0 | ECOSYSTEM: introduced 2.6.2, fixed 2.8.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.8.0 |
| PYSEC-2026-4175 | urllib3 2.7.0 | ECOSYSTEM: introduced 1.26.0, fixed 2.8.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 2.8.0 |
| PYSEC-2026-3412 | weasyprint 68.0 | ECOSYSTEM: introduced 0, last_affected 68.1 | Undetermined | Execution and conditions unverified | Scanner match; fix none listed |
| PYSEC-2026-3412 | weasyprint 68.0 | ECOSYSTEM: introduced 0, last_affected 68.1 | Undetermined | Execution and conditions unverified | Scanner match; fix none listed |
| PYSEC-2026-3940 | weasyprint 68.0 | ECOSYSTEM: introduced 0, fixed 70.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 70.0 |
| PYSEC-2026-4311 | weasyprint 68.0 | ECOSYSTEM: introduced 0, fixed 70.0 | Undetermined | Execution and conditions unverified | Scanner match; fix 70.0 |
| PYSEC-2026-4312 | werkzeug 3.1.6 | ECOSYSTEM: introduced 0, fixed 3.1.9 | Undetermined | Execution and conditions unverified | Scanner match; fix 3.1.9 |

## Appendix B Running the recommended human follow-ups

These procedures are recommended follow-ups, waived at release and not performed. Model-provider cyber safeguards prevented agents from performing both tasks on 2026-11-12, so a person runs them. Run slice 3 first, because slice 5 is scored against its answer key. Both use the same Docker project (`cyberfde`, port 8080), so never run them at the same time. Keep all outputs in access-controlled storage, never in the candidate package.

### Slice 3: answer-key validation (about 2–3 hours)

Inputs: the priority advisories in section 6, the inventory and patch comparisons in Appendix A, and the runtime in `candidate/` (`./assessment.sh up`).

Start with the four priority advisories, which the static audit could not resolve: GHSA-877j-rg2w-v649, GHSA-29xj-69vf-fmmh, GHSA-45p2-2pp7-f8w2 and GHSA-r8px-9662-x39c. See section 6 for their focus areas and reasonable alternatives.

1. Start clean with `./assessment.sh reset`. Note the start time.
2. For at least three priority advisories, attempt to reproduce or rigorously rule out applicability:
- Confirm the version precondition on the running image (`bench version`, or the installed file or package version).
- **Positive control:** run the request or action that should show the advisory's behavior, using the least-privileged fixture user it needs. Save the exact command and the trimmed response.
- **Negative control:** run the same action where it must fail (another user, a missing role or an unaffected path). Save the exact command and the trimmed response.
- If it does not reproduce, record the evidence and any established reason; a failed reproduction alone does not prove inactivity. If the reason remains unknown, record missing evidence and the next discriminating check.
- Classify it as applicable-verified, version-match-unverified or not-applicable, and update Appendix A.
3. Write the validated answer key with a CONFIDENTIAL header. For each item give the ID and source URL, component, preconditions, reproduction steps, positive and negative evidence, severity for E Corp, and what strong and weak candidate answers look like.
4. Add a section on stock ERPNext risk surfaces candidates commonly report: portal scope, attachments, role permissions, API exposure, login rate limiting and the lab's default Administrator password. Record the observed behavior and scoring guidance for claims that no advisory backs.
5. Finish with `./assessment.sh down`. Record the wall time.

### Slice 5: timed dry run (about 4.5 hours)

Use someone who has not seen the answer key where possible.

1. Extract a fresh copy of the distributed candidate archive into a new directory. Use nothing from this private workspace.
2. Follow the package `README.md` exactly. Record timestamps for: extraction done, `up` started, `up` ready, investigation start, the end of each round, and report done.
3. Keep a friction log of every unclear, wrong, slow or broken step, with the exact command and output. Log anything that looked like a hint or like interviewer material.
4. Produce what a candidate would: the report and a presentation for the 30-minute session.
5. Run `./assessment.sh down`, then confirm with `docker ps -a`, `docker volume ls` and `docker network ls` that nothing from the `cyberfde` project remains.
6. Score the report against the rubric in section 3 and the validated answer key. Save the record (timings, friction log, scores and fixes needed) in access-controlled storage.

### After both follow-ups

Address package issues the friction log finds. An independent review of any changed candidate package is recommended. Record follow-up results and review evidence in RELEASE.md.
