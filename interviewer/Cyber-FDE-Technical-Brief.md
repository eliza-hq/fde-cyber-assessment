CONFIDENTIAL: interviewers only. Do not share with candidates.

**Status: BLOCKED. Do not distribute the assessment.**

# Cyber FDE Assessment Technical Brief

## Target and source

The target is stock official frappe/erpnext:v16.34.0, running ERPNext 16.34.0 and Frappe 16.33.0. E Corp and all fixture data are fictional. There is no custom app or planted bug. The stock image is used directly, with no Dockerfile.

| Image | Pinned digest |
| --- | --- |
| frappe/erpnext:v16.34.0, multi-architecture index | sha256:1a91412a37c58d7829d8a8e078f01fdfa068ef136a2212dd1579d32f030c10c3 |
| mariadb | sha256:d36f18d65a0459510b8b0f643b226a6d299e3206486e2b64ff20754a6d291707 |
| redis | sha256:3f9c6e23ed6bea3b41d0ef709fc164c1a0b7c00d5a21a60e0e9c33ada5496881 |

Candidate source is the assessment branch of eliza-hq/fde-cyber-erpnext-assessment, upstream ERPNext tag v16.34.0 plus one package commit. Reviewed and pushed commit: a6f0e549f9ff6637cf1b0bf224ab66e71ec6eab6. The fork default remains develop.

## Services and isolation

| Path or service | Role and boundary |
| --- | --- |
| Browser to frontend | Only published entrypoint: 127.0.0.1:8080. The stock Frappe nginx frontend joins both networks. |
| Internal network | Backend, websocket, workers, scheduler, database and Redis use the internal network. It is configured without egress. Site creation and configuration also use it. |
| Storage | Project volumes hold site, database, queue and log data. Reset and teardown remove project data. |

A backend outbound connection failed during verification, and no other ports were published. This is evidence for the tested setup, not a claim that containers alone guarantee isolation. Candidates must stop if they cannot verify safe operation. They must use only the local target, containers and source, fictional data, and a controlled machine. No external testing, denial of service, real recipients, or third-party uploads of target data or credentials are allowed.

## Lifecycle and fixtures

Docker Desktop or Docker Engine with Compose v2 is required, with approximately 4 GB of memory available to Docker and 2-3 GB free disk. Supported instructions cover macOS arm64 or x86_64 and Linux. From assessment/:

| Command | Effect |
| --- | --- |
| ./assessment.sh up | Start and initialize the target. |
| ./assessment.sh status | Show container status. |
| ./assessment.sh reset | Delete data and restore fixtures. |
| ./assessment.sh down | Remove project containers, networks and volumes. Shared images remain. |

The setup wizard creates E Corp. Fixtures include two customers, two suppliers, two non-stock items, two submitted sales orders, two submitted sales invoices, two submitted purchase orders and two private customer file attachments. Disposable accounts include Administrator, Sales User, Accounts User, Auditor and a customer portal user. Credentials appear in the candidate README. The portal user is linked to a customer and has no desk roles.

## Verification and limitations

On 2026-11-12, runtime verification on macOS arm64 with Docker Desktop passed startup, version and architecture checks, setup, login, desk and portal permission checks, retained-state restart, reset, fixture repeat, the outbound connection check, exposure and teardown. A cached-image empty-volume startup reached login in 56 seconds. A cold pull was not measured. Fresh startup and sales login were rechecked after the E Corp fixture rename; other rows describe the earlier verification.

First-party image source was compared with the ERPNext and Frappe upstream tags, with exclusions recorded in VERIFICATION.md. Generated frontend assets were not rebuilt for comparison, and one ERPNext JavaScript lockfile differed in resolved dependencies. These limits matter when describing source equivalence.

The private advisory triage's incomplete repository feed counted 76 version-affected, 66 not-affected and 55 unknown entries. A subsequent patch audit identified 12 proposed version reclassifications to apply; its 243 rows were all undetermined for patch presence. Neither version matches nor scanner matches establish a confirmed finding. Runtime answer-key validation remains pending. The intended categories are applicable-verified, version-match-unverified and not-applicable.

## Candidate package and integrity

The package is candidate/ in this private workspace and assessment/ in the public fork. The reviewed commit's file hashes are:

| File in assessment/ | SHA-256 |
| --- | --- |
| README.md | fbd912302a4384c6b925d4d91b6d2e7d904fd31ff4360686941bed10823d7bfe |
| UPSTREAM-LICENSE | 4234a14fb0a788985bf429eb9ea73bfb93139967e8dcee191f7d4f621970c800 |
| assessment.sh | 006236a336475ca2f888b1bf5b3401030f37bb2def3ccfbafbb8ec94acb6ca48 |
| compose.yaml | da73fdf409d497c84097395495f9125d879d5a9741ce87fb442c77f7037b5f98 |
| fixtures.py | 4b45bea2d1f848d25892a955624f1b4df16234e8be86878f51f189c9217b8243 |

The independent review of the exact commit passed history and scope, metadata, content and hints, secret regex, hashes, digests and drift checks. The secret scan was regex-only because gitleaks and trufflehog were unavailable.

## Release sequence and change control

1. A person validates the private answer key on the pinned runtime, recording applicability, controls and limitations. This gate precedes the dry run because the latter is scored against the key.
2. A person performs a timed dry run using only a fresh clone of the public assessment branch, produces candidate deliverables, records friction and scores the work. Apply fixes and repeat affected checks. The two gates share a Docker project and port and must not run simultaneously.
3. Re-review any changes and update the release record. Set assessment as the fork's default branch before distribution. Jordan approved the existing branch push; distribution remains blocked pending the gates. RELEASE.md and the checklist govern final approval and release.

Model-provider cyber safeguards blocked agents from the first two gates. No individual operator is named in the source. Do not send the package to candidates until all remaining gates and release approval are complete.

Keep interviewer/ and docs/ out of the public fork and candidate package. Push only refs/heads/assessment with --no-follow-tags. Any candidate/ change requires re-syncing the fork's assessment/, a new commit, renewed independent review and updated hashes in RELEASE.md. Check the exact package and public history for private material and secrets before release.
