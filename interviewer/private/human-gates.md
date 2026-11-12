# CONFIDENTIAL: human release gates (slices 3 and 5)

Model providers' cyber safeguards blocked both gates for agents on 2026-11-12, so Jordan decided a person runs them. Do slice 3 first, because slice 5 is scored against its answer key. Both use the same Docker project (`cyberfde`, port 8080), so never run them at the same time.

## Slice 3: answer-key validation (~2–3 h)

Inputs: `interviewer/private/advisory-triage.md` (see "Priority runtime validation candidates"), `interviewer/private/patch-presence.md` (published version ranges for 243 advisory rows, from a 2026-11-12 agent source audit), and the runtime in `candidate/` (`./assessment.sh up`).

Start with the three priority advisories, which the patch audit could not resolve. GHSA-cc74-rc2g-p7hw lists ERPNext below 16.37.0 as affected, so the pin is in range. For GHSA-r8px-9662-x39c and GHSA-9pp9-wgp9-3p3j, the audit found related checks missing at the pinned Frappe tag but could not tie them to the advisories. Also apply the audit's 12 Frappe "not affected by version" reclassifications to the triage.

1. Start clean: `./assessment.sh reset`. Note the start time.
2. For each priority advisory in the triage (aim for at least 3 reproduced or rigorously ruled out):
   - Confirm the version precondition on the running image (`bench version`, or the installed file or package version).
   - **Positive control:** the request or action that should show the advisory's behavior, using the least-privileged fixture user it needs. Save the exact command and the trimmed response.
   - **Negative control:** the same action where it must fail (another user, missing role, or an unaffected path). Save the exact command and the trimmed response.
   - If it doesn't reproduce, record exactly why: already patched, precondition absent in stock config, feature disabled, or other.
   - Set the classification in the triage: applicable-verified, version-match-unverified or not-applicable.
3. Write `interviewer/private/answer-key.md` with a CONFIDENTIAL header. For each item give: ID and source URL, component, preconditions, repro steps, positive and negative evidence, severity for E Corp, and what strong and weak candidate answers look like. Add a section on stock-ERPNext risk surfaces candidates commonly report (portal scope, attachments, role permissions, API exposure, login rate limiting, the lab's default Administrator password), with observed behavior and scoring guidance when no advisory backs the claim.
4. Finish with `./assessment.sh down`. Record the wall time.

## Slice 5: timed dry run (~4.5 h, best done by someone who hasn't seen the answer key)

1. Clone only the public package into a fresh directory: `git clone --branch assessment https://github.com/eliza-hq/fde-cyber-erpnext-assessment.git`. Use nothing from this private repo.
2. Follow `assessment/README.md` exactly. Record timestamps for: clone done, `up` started, `up` ready, investigation start, each round's end, report done.
3. Keep a friction log: every unclear, wrong, slow or broken step, with the exact command and output. Also log anything that looked like a hint or like interviewer material.
4. Produce what a candidate would: the report and a 30-minute presentation outline.
5. Run `./assessment.sh down`, then confirm with `docker ps -a`, `docker volume ls` and `docker network ls` that nothing from the `cyberfde` project remains.
6. Score the report against the rubric in `Cyber-FDE-Interviewer-Packet.md` and the answer key. Save the record as `interviewer/private/dry-run.md` (timings, friction log, scores, and fixes needed).

## After both

Fix any package issues the friction log finds. Any change to `assessment/` needs a new commit, a renewed independent package review, and updated hashes in `RELEASE.md`. Then mark the gates done in `RELEASE.md` and set `assessment` as the fork's default branch.
