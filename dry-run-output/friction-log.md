# Dry-run friction and timing

17 November 2026, America/Chicago. Approximate start 12:12; final data collection 12:13. Target was already running, so setup time was not measured. Three rounds executed in roughly one minute; reporting followed. This is a substantially compressed dry run, not evidence that a candidate can complete the full exercise in four hours.

- The exercise file is under `candidate/`, not repository root; located with `rg --files`. Minor navigation friction.
- Host Python did not have `requests`; the first script failed before any requests. Used the existing application-container Python and service network instead. This depends on Docker access and is within the target containers.
- Portal list HTML was insufficient to establish its dynamic data contents. Direct known-record routes and positive own-record controls were used; list behavior remains a next step.
- Advisory inventory supplies matching ranges but not verified fix references or exact paths for these two cases. Local candidate fix is explicitly unverified; a stronger assessment requires upstream fix comparison and safe reachability validation.
- No write authorization tests were performed for Auditor; no claim of read-only behavior is justified.
- Timing is too compressed to validate the exercise's four-hour design or 15-minute presentation delivery. A human timed run and runtime answer-key validation remain necessary.

- **Candidate realism contamination:** the worker consulted `interviewer/private/advisory-triage.md` and `patch-presence.md`, materials unavailable to candidates. The advisory analysis and timing therefore cannot validate independent candidate performance.
- Round 1 reproduction requires the documented `sed` substitution before piping `check.py` into the backend container; localhost inside that container is not the frontend.
- A source-only follow-up examined `get_file_path`, `get_file` and `pdf_to_base64`; no fourth testing round was performed. The advisory fix identity, reachable trigger and SQL injection path remain unresolved.
