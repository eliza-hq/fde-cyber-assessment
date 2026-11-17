# Release status

**Cleared for release — approved by Jordan on 2026-11-17.**

The target is the stock official `frappe/erpnext:v16.34.0` image, pinned to multi-architecture index digest `sha256:1a91412a37c58d7829d8a8e078f01fdfa068ef136a2212dd1579d32f030c10c3` (ERPNext 16.34.0, Frappe 16.33.0). The coordinator distributes the self-contained `candidate/` directory as a single archive. Source to review is upstream ERPNext tag v16.34.0 (https://github.com/frappe/erpnext/tree/v16.34.0) and Frappe tag v16.33.0 (https://github.com/frappe/frappe/tree/v16.33.0), and the application source inside the running containers at /home/frappe/frappe-bench/apps. The image also contains built front-end assets and some differently resolved JavaScript dependency versions. E Corp and its fixtures are fictional; there is no custom app or planted bug. The stock image is used directly, so no Dockerfile is needed.

[Runtime verification](docs/runtime-v16/VERIFICATION.md) records macOS arm64 startup, versions, logins, isolation, restart, reset and teardown. A cold pull was not measured. The release decision and waived gates are recorded below and in the [review checklist](RELEASE-CHECKLIST.md).

- Slice 3 (answer-key runtime validation): waived by Jordan on 2026-11-17; not performed.
- Slice 5 (timed dry run): waived by Jordan on 2026-11-17; not performed.
- Slice 6 (independent package review): waived by Jordan on 2026-11-17; not performed.
- [x] Slice 7: Jordan approved distribution on 2026-11-17.

## Package review

2026-11-17: Jordan decided package file and archive hashes are not required; the independent package review was waived.

The following historical review and hashes are superseded: they describe the former release vehicle, not the archive now planned for distribution.

The independent gpt-6.1-terra review on 2026-11-12 of commit `5bc96f00dce062696e987d0dea30b2d10463b0d0` passed structure, history, secret-regex, digest, and drift checks. It failed only on the README source claim, which has been fixed. A renewed independent gpt-6.1-terra review on 2026-11-12 of commit `a6f0e549f9ff6637cf1b0bf224ab66e71ec6eab6` passed all six checks (history and scope, metadata, content and hints, secret regex, hashes matching this record, digests and drift). The reviewer had neither gitleaks nor trufflehog, so the secret scan was regex-only.

- Commit: `a6f0e549f9ff6637cf1b0bf224ab66e71ec6eab6`
- Author and committer: `Jordan Taylor <jordan@eliza.com>`
- Commit tree: `d63224ac434116f224fe36553a97f5d6fe10e293`
- `assessment/` tree: `28c0b4d5ef2e41ac3081abc34c95662f3e40d388`
- Archive: `assessment-a6f0e549f9.tar.gz`, produced with `git archive --format=tar.gz --prefix=fde-cyber-erpnext-assessment/ a6f0e549f9ff6637cf1b0bf224ab66e71ec6eab6 -o /private/tmp/claude-501/-Users-jordantaylor-Development-eliza-cyber-fde-assessment/e1939f64-ba01-4460-a7c3-44bde2bfb006/scratchpad/slice6/assessment-a6f0e549f9.tar.gz`; SHA-256 `c61e93c9ecaf5d30199c4d6f3dcb4d39e3fa080968b78ed7530d9129809699d9`.

| File | SHA-256 |
| --- | --- |
| `assessment/README.md` | `fbd912302a4384c6b925d4d91b6d2e7d904fd31ff4360686941bed10823d7bfe` |
| `assessment/UPSTREAM-LICENSE` | `4234a14fb0a788985bf429eb9ea73bfb93139967e8dcee191f7d4f621970c800` |
| `assessment/assessment.sh` | `006236a336475ca2f888b1bf5b3401030f37bb2def3ccfbafbb8ec94acb6ca48` |
| `assessment/compose.yaml` | `da73fdf409d497c84097395495f9125d879d5a9741ce87fb442c77f7037b5f98` |
| `assessment/fixtures.py` | `4b45bea2d1f848d25892a955624f1b4df16234e8be86878f51f189c9217b8243` |

Historical, superseded: the former branch was pushed on 2026-11-12 with Jordan's approval and deleted from the fork on 2026-11-17 at Jordan's request.

Model-provider cyber safeguards blocked agents from the answer-key validation and the dry run. On 2026-11-12 Jordan decided a person runs both. These gates were waived at release on 2026-11-17. Answer-key validation on the runtime and a timed dry run remain recommended follow-ups; record results in access-controlled storage.

Archived history: the earlier ERPNext 17 `develop` experiment at `5a86717…` was superseded.
