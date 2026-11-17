# Cyber FDE assessment maintainer workspace

This private workspace produces the candidate package and holds interviewer material.
Candidates never see this repository.

## Target

The disposable target is stock ERPNext v16.34.0 on Frappe v16.33.0.
It uses the official ERPNext image pinned by digest.
E Corp is a fictional customer, and the fixtures are synthetic.
There is no custom app or planted bug.

## Layout

- [`candidate/`](candidate/) is the self-contained package distributed by the coordinator as a single archive.
- [`Cyber-FDE-Interviewer-Guide.docx`](Cyber-FDE-Interviewer-Guide.docx) is the confidential interviewer guide.
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

**Cleared for release** (Jordan, 2026-11-17). [RELEASE.md](RELEASE.md) is the source of truth for status and review evidence.

The remaining gates are answer-key validation on the runtime and a timed dry run.
Model-provider cyber safeguards stopped agents from doing both. A person must run
them in order and record the evidence in access-controlled storage.
Any change to `candidate/` requires a renewed independent review.

Never copy the interviewer guide or `docs/` content into the candidate package.
