# E Corp application security assessment

E Corp is a fictional customer seeking a security assessment of its ERPNext deployment. This repository is upstream ERPNext v16.34.0 plus this `assessment/` directory. The deployment runs the official ERPNext v16.34.0 image, built on Frappe v16.33.0 (source at github.com/frappe/frappe, tag v16.33.0). The image's application source matches these tags; it also contains built front-end assets and some differently resolved JavaScript dependency versions. Assess the application and explain your results to E Corp's technical lead and business owner. All data and accounts are synthetic and disposable.

Allow approximately four hours for investigation and report writing, excluding setup. Plan your work and conduct one to three rounds, using what you learn to decide whether to continue. Stop at the time limit and document next steps.

## Setup

You need Docker Desktop or Docker Engine with Compose v2, approximately 4 GB of memory available to Docker, and 2–3 GB of free disk space. Use macOS on arm64 or x86_64, or Linux. From the `assessment/` directory:

```sh
./assessment.sh up      # start and initialize
./assessment.sh status  # show container status
./assessment.sh reset   # delete data and restore fixtures
./assessment.sh down    # remove containers, networks, and volumes
```

Open http://127.0.0.1:8080. The disposable accounts are:

| Account | Password | Role |
| --- | --- | --- |
| Administrator | admin | Administrator |
| sales@example.invalid | assessment-demo | Sales User |
| accounts@example.invalid | assessment-demo | Accounts User |
| viewer@example.invalid | assessment-demo | Auditor |
| portal@example.invalid | assessment-demo | Customer portal user |

## Boundaries

Test only the supplied local target, its containers and source. Keep it on localhost; do not test external targets, use denial-of-service techniques, import real data, or send mail to real recipients. Do not upload target data or credentials to third parties. Use internet access for setup and research only. If you cannot operate within these boundaries, stop and contact the coordinator.

## Deliverables

Submit a written report and your presentation materials to the coordinator. In the report, explain your plan and rationale, actions and lessons from each round, evidence and reproduction steps, impact and preconditions, confidence and assumptions. Distinguish observations from hypotheses, including failed tests and disproved concerns. Prioritize recommendations and explain what you would test next and why. List tools and AI assistance used, their contributions, and how you checked their output. A well-supported negative or limited result is a valid outcome; we assess your reasoning and evidence, not the number of findings.

Prepare a 30-minute customer-facing presentation including discussion and questions. Choose your format and explain impact, evidence, confidence, priorities, and next steps to technical and nontechnical listeners. Be ready to defend your approach and assumptions.
