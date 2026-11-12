# Cyber FDE application security assessment

Create a repeatable take-home assessment for Cyber FDE candidates that tests application security investigation and customer communication. Candidates will assess a disposable ERPNext/Frappe target and explain their evidence and next steps; interviewers will use a private answer key and rubric to evaluate the work consistently.

## Current target correction

The assessed source is [eliza-hq/fde-cyber-erpnext-assessment](https://github.com/eliza-hq/fde-cyber-erpnext-assessment) at `5a86717902e25a07e7cb1923fb84ca552fd687ee`. The existing candidate Docker prototype uses a different ERPNext 16 image and does not implement this target. Its prior checks do not validate this revision. A matching pinned runtime and complete lifecycle verification remain outstanding; see [release status](../../RELEASE.md).

## Done when

- A candidate can follow the public instructions to start, access, reset, and dispose of the pinned target in an isolated environment with synthetic data. The instructions identify prerequisites, permitted testing boundaries, deliverables, and approximately four hours of expected work.
- The target's exact ERPNext/Frappe versions and deployment inputs are pinned and reproducible. An internal reviewer can recreate it from the published instructions and verify isolation and disposal without access to real customer data or systems.
- The candidate instructions request a report covering the investigation plan, execution, evidence, confidence, next tests, and tools and AI use. The report requirements ask candidates to explain and defend their approach and assumptions.
- A separate earlier interview round includes a defensibility check. Private interviewer materials provide its prompt and evaluation guidance.
- The exercise includes a 30-minute customer-facing presentation, with its audience, purpose, and expected format stated to candidates.
- The private interviewer materials contain a validated answer key, evidence and reproduction guidance, a scoring rubric, the earlier interview round’s defensibility prompt and evaluation guidance, and guidance for evaluating the report and presentation. The rubric rewards defensible reasoning, calibrated confidence, and communication, including when a candidate correctly identifies a limitation or disproves a suspected issue.
- An internal dry run uses the candidate-facing materials and target as provided. Its record captures setup and completion time, observed findings, ambiguity or failure points, rubric calibration, and fixes made before release. A reviewer can repeat the final setup and verify the resulting materials are consistent.
- Every intended finding and any referenced known CVE is checked against the pinned target and documented with evidence and applicability. Unverified claims are removed or explicitly identified as hypotheses; the assessment does not assume a version is vulnerable solely because a CVE exists.
- Public candidate materials do not expose the private answer key or rubric. The release process identifies the public and private artifacts and checks their separation.

## Scope

Produce one candidate-facing assessment package, one reproducible disposable target, and one private interviewer package. Cover application security investigation of the running application and relevant application behavior, followed by a candidate report and customer-facing presentation. Include setup, isolation, reset and teardown instructions, synthetic data, and the internal dry run needed to make the exercise usable and fair.

## Cut

- DevSecOps pipeline, infrastructure engineering, and production hardening exercises. The assessment is focused on application security.
- Multiple target applications, difficulty tiers, or candidate-specific deployments. One repeatable target is enough to evaluate the role.
- Automated scoring or a bespoke assessment platform. A private rubric supports interviewer judgment.
- Real customer data, live customer systems, and external targets. The exercise uses synthetic data and an isolated disposable environment.

## Data shape

The assessment consists of three related artifacts and a dry-run record:

- **Candidate package:** scenario, authorized scope and boundaries, prerequisites, target lifecycle instructions, time guidance, report requirements, and presentation instructions.
- **Target specification:** pinned application and deployment versions, configuration and synthetic fixtures, access details, isolation assumptions, and reset and teardown procedure.
- **Interviewer package:** for each validated finding, its applicability, evidence and reproduction steps, impact and limitations, and expected candidate reasoning; plus the earlier interview round’s defensibility prompt and evaluation guidance, and a rubric for the report and presentation. Suspected but unvalidated findings are labeled as hypotheses and are not treated as established answers.
- **Dry-run record:** target revision, elapsed setup and assessment time, observations, findings and evidence, rubric calibration, issues, and resolutions. Private evaluation details remain outside the candidate package.

## Decisions

- Use a pinned, disposable ERPNext/Frappe target so candidates investigate the same reproducible application. Validate actual behavior and CVE applicability on that target.
- Publish candidate instructions while keeping the answer key and rubric private, preserving a consistent assessment without disclosing expected answers.
- Guide candidates toward approximately four hours of work, then a 30-minute customer-facing presentation. The dry run checks whether the guidance is realistic.
- Assess defensibility in a separate earlier interview round, with the prompt and evaluation guidance kept in the private interviewer package. The take-home report also asks candidates to defend their approach and assumptions and disclose evidence, confidence, next tests, and tool and AI use.
- Run the complete exercise internally and correct material problems before release. Use only synthetic data and isolate the target throughout its lifecycle.

## Terms

See [the glossary](../../GLOSSARY.md) for Candidate package, Target, Interviewer package, and Dry run.

## Slices

1. Specify the target and safety boundary, including versions, synthetic data, access, isolation, reset, and disposal. Verified by recreating and tearing down the target from its instructions and checking that it has no real customer data or access to external systems.
2. Investigate the pinned target and prepare the private answer key. Verified by independently reproducing each intended finding and checking each referenced CVE for applicability, with evidence recorded.
3. Write the candidate package and private rubric against the validated target. Verified by tracing each requested deliverable to an evaluation criterion and checking that public materials contain no private answers or rubric.
4. Conduct an internal dry run, calibrate the rubric, and repair issues. Verified by a recorded run using the final candidate path, review of timing and scoring, and a repeat of setup and affected checks after corrections.

## Run with

`/estack-build docs/work-items/cyber-fde-assessment.md`, under pStack's Feature playbook.

## Risks

- An unpinned dependency or changed upstream image could make the target inconsistent or invalidate findings. Pin all deployment inputs and verify them during the dry run.
- A disposable application with known weaknesses could expose other systems if isolation or teardown fails. Check the boundary and cleanup before release.
- A four-hour estimate or rubric may disadvantage candidates if setup consumes too much time or scoring rewards tool choice over reasoning. Use the dry run to calibrate both.
- Public and private materials could be mixed during distribution. Check the release artifacts and their access before sending them to candidates.
