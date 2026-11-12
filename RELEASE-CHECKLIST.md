# Candidate package release review

**Blocked — not yet approved for distribution.** See [release status](RELEASE.md) and [runtime verification](docs/runtime-v16/VERIFICATION.md). The target is the official ERPNext v16.34.0 image (Frappe 16.33.0), pinned by index digest `sha256:1a91412a37c58d7829d8a8e078f01fdfa068ef136a2212dd1579d32f030c10c3`. The fork's `assessment` branch is the upstream v16.34.0 tag plus one package commit. The image is used directly; no Dockerfile is required.

- [ ] **Slice 3 — answer key:** Validate each intended finding on the pinned runtime with positive and negative controls, recording evidence, applicability and limits. Keep hypotheses labeled and private.
- [ ] **Slice 5 — agent dry run:** Use only the packaged candidate repository, record setup and assessment time, report and rubric scores, apply fixes, and repeat affected checks.
- [ ] **Slice 6 — independent review:** A reviewer other than the assembler inspects the exact package file list and contents, links, hidden files, private material and secrets; checks public history separately and private access; compares the revision with the dry run; and records SHA-256, reviewer, date and evidence in RELEASE.md. Re-review changes and repeat affected checks.
- [ ] **Slice 7 — Jordan approval:** Obtain Jordan's approval to push and distribute; only then push the branch and set the fork default branch.

Do not include interviewer materials, reports, caches or real credentials in the candidate package.
