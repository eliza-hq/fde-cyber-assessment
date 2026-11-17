# Release readiness: candidate-ready Cyber FDE assessment

Released 2026-11-17 by Jordan’s decision; slices 3, 5 and 6 waived.

Get the assessment to a state where Jordan can send it to candidates (first final: next Monday). Candidates must be able to extract the distributed candidate archive, start a pinned disposable target in minutes on a Mac or Linux laptop, and spend their ~4 hours on AppSec reasoning, not setup. Interviewers get a private, validated answer key and rubric.

This supersedes the target choice in [cyber-fde-assessment.md](cyber-fde-assessment.md) (ERPNext 17 `develop` @ `5a86717…`). The rest of that brief (deliverables, rubric intent, boundaries) still stands.

## Decision update (2026-11-12, Jordan): stock ERPNext only

The target is stock ERPNext only: the official ERPNext v16.34.0 image (Frappe 16.33.0) with synthetic data. The fictional customer is E Corp; there is no custom app and no planted bugs. The answer key is the upstream advisories reproduced on the target, plus guidance for scoring candidates' reasoning when a version match is not confirmed. Where this section conflicts with the original decision below, this section wins.

## Original decision: retarget to official ERPNext v16.34.0

- **Target** = official multi-arch image `frappe/erpnext:v16.34.0` pinned by digest (local: `frappe/erpnext@sha256:1a91412a37c58d7829d8a8e078f01fdfa068ef136a2212dd1579d32f030c10c3` — verify it is the multi-arch index digest, not a single-platform one). MariaDB and Redis are pinned by digest as in `candidate/compose.yaml`.
- **Why:** the `develop` runtime needs a 9.4 GB amd64 custom build under emulation, with lockfile/dependency drift and no official image. A stable release has an official, reproducible, native-arm64 image and known advisories to pin.
- **Source = runtime:** The coordinator distributes `candidate/` as a self-contained archive. Source to review is upstream ERPNext tag v16.34.0 (https://github.com/frappe/erpnext/tree/v16.34.0) and Frappe tag v16.33.0 (https://github.com/frappe/frappe/tree/v16.33.0), and the application source inside the running containers at /home/frappe/frappe-bench/apps. The image also contains built front-end assets and some differently resolved JavaScript dependency versions.
- The `develop` experiment (`docs/runtime-attempt/`) is archived under `docs/archive/`, not shipped.

## Done when

- From a fresh copy of the distributed candidate archive, `./assessment.sh up` starts the target on `http://127.0.0.1:<port>` in under ~15 min on Apple Silicon (native arm64, no emulation). `reset` restores the known synthetic state. `down` removes all project containers, networks and volumes. A restart with retained state keeps working.
- The running image's Frappe/ERPNext versions match the pinned tag. The ERPNext source in the image matches upstream tag `v16.34.0`.
- Synthetic fixtures exist in stock ERPNext: E Corp with the setup wizard completed, customers, suppliers, items and transactions. Users: Administrator, at least two desk users with ordinary roles, and one website/portal user linked to a customer with no desk roles. Credentials are in the candidate README (disposable).
- Isolation: only the web entrypoint is published, and only on 127.0.0.1. App, workers, DB and Redis sit on an internal network with no egress, verified by a failed outbound connect from the backend.
- Answer key: the top upstream advisories are reproduced on the running target, with a positive control and a negative control, or documented as not reproducible along with why. Upstream advisories for the pinned Frappe/ERPNext versions are triaged as applicable-verified, version-match-unverified, or not-applicable, with sources.
- The candidate README and interviewer guide reference only the v16.34.0 target. The guide covers the meeting-note red flags: asking for token/cost budgets upfront, "found nothing" without a confidence level and next tests, and excessive time or rounds. It also includes the pressure question "How do you prove to me that your finding is accurate and I'm actually safe?" for both the earlier round and the final.
- A person conducts a dry run using only a fresh copy of the distributed candidate archive, is timed, produces a report, and is scored with the rubric. Its fixes are applied.
- An independent reviewer checks the exact candidate package's file list. It must contain no interviewer material, no answer hints in comments, and no secrets.

## Cut

- ERPNext 17 `develop` runtime. Replaced by the official stable image.
- A custom Python TCP relay. Use the stock Frappe nginx `frontend` container as the only dual-homed service.
- The earlier agent dry-run plan is superseded; a human dry run is a release gate.
- DevSecOps/infra exercises, difficulty tiers, automated scoring. (Unchanged.)

## Data shape

- **Candidate package** (`candidate/` in a single archive): `README.md`, `compose.yaml`, `assessment.sh` (up / reset / down / status), fixtures loader.
- **Interviewer materials** (private, never in the candidate package): the root interviewer guide; a validated answer key and dry-run record remain release gates.
- **Release record** (`RELEASE.md`): pinned digests, reviewer/date, evidence links, status.

## Slices

1. Target runtime on v16.34.0 + fixtures + lifecycle script. Verified by clean up, logins, restart, reset, down, egress test and native arm64 timing.
2. Advisory triage for the pinned versions (in parallel with 1). Verified by sourced table.
3. Answer-key validation on the runtime. Verified by reproduction with controls.
4. Candidate README + interviewer guide + docx + RELEASE docs. Verified by a trace from each deliverable to a rubric row, and a grep check for leaked answers.
5. Human dry run from a fresh copy of the distributed archive, then fixes. Verified by a timed record and rubric scores.
6. Independent release review of the exact package. Verified by file list and secret scan.
7. Jordan approves distribution.

## Risks

- Docker Desktop resources: ~2 GB pull. The README states its prerequisites.
- Candidates running a knowingly vulnerable app: bound to localhost, synthetic data only, explicit boundary rules.
