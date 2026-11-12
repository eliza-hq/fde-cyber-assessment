# Cyber FDE assessment maintainer workspace

This private workspace produces the candidate package and holds interviewer material.
Candidates never see this repository.

## Target

The disposable target is stock ERPNext v16.34.0 on Frappe v16.33.0.
It uses the official ERPNext image pinned by digest.
E Corp is a fictional customer, and the fixtures are synthetic.
There is no custom app or planted bug.

## Layout

- [`candidate/`](candidate/) is the package that ships as `assessment/` on the
  `assessment` branch of the public fork
  [eliza-hq/fde-cyber-erpnext-assessment](https://github.com/eliza-hq/fde-cyber-erpnext-assessment).
- [`interviewer/`](interviewer/) holds the interviewer packet in Markdown and DOCX.
- [`interviewer/private/`](interviewer/private/) holds advisory triage, the
  patch-presence audit, and human gate instructions. The answer key and dry-run
  record belong here.
- [`docs/`](docs/) holds the specification, runtime verification, and archive.
- [`RELEASE.md`](RELEASE.md) records release status and package evidence.
  [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md) lists the release review gates.

## Run locally

From `candidate/`:

```sh
./assessment.sh up      # start and initialize
./assessment.sh status  # show container status
./assessment.sh reset   # delete data and restore fixtures
./assessment.sh down    # remove containers, networks, and volumes
```

Open http://127.0.0.1:8080. See the [candidate README](candidate/README.md)
for prerequisites, disposable credentials, and assessment boundaries.

## Release

**Blocked:** the package is not yet approved for distribution. The `assessment`
branch was pushed at `a6f0e549` and independently reviewed. It is not yet the
fork's default branch. [RELEASE.md](RELEASE.md) is the source of truth for status,
review evidence, and hashes.

The remaining gates are answer-key validation on the runtime and a timed dry run.
Model-provider cyber safeguards stopped agents from doing both. A person must run
them in order using [the human gate instructions](interviewer/private/human-gates.md).
The fork's default branch must also be set to `assessment` before distribution.

Any change to `candidate/` requires re-syncing the fork's `assessment/`, a new
commit, a renewed independent review, and updated hashes in RELEASE.md.

Never copy `interviewer/` or `docs/` content into the candidate package or public
fork. Push only `refs/heads/assessment` with `--no-follow-tags`.
