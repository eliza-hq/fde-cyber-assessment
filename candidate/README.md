# E Corp application security assessment

E Corp is a fictional customer seeking a security assessment of its ERPNext deployment. This directory is the self-contained candidate package. The deployment runs the official ERPNext v16.34.0 image, built on Frappe v16.33.0. Source to review is upstream ERPNext tag v16.34.0 (https://github.com/frappe/erpnext/tree/v16.34.0) and Frappe tag v16.33.0 (https://github.com/frappe/frappe/tree/v16.33.0), and the application source inside the running containers at /home/frappe/frappe-bench/apps. First-party source was compared with these tags excluding generated and built assets; JavaScript dependency resolutions differ. Treat in-container source as authoritative for what runs. From this directory, confirm running versions with `docker compose -p cyberfde exec backend bench version`. E Corp plans to open its customer portal to trade customers. Assess the application to inform the launch decision and explain your results to E Corp's technical lead and business owner. All data and accounts are synthetic and disposable. See [the exercise brief](Cyber-FDE-Final-Exercise.md) (also available as a [Word document](Cyber-FDE-Final-Exercise.docx)) for the situation, focus areas and task. The assessment covers the three focus areas defined in the brief: portal data isolation, internal role separation, and advisory applicability for those areas. The report and presentation cover only those areas.

Allow approximately four hours for investigation and report writing, excluding setup. Plan your work and conduct one to three rounds, using what you learn to decide whether to continue. Stop at the time limit and document next steps.

## Setup

You need Docker Desktop or Docker Engine with Compose v2, approximately 4 GB of memory available to Docker, and 2–3 GB of free disk space. Use macOS on arm64 or x86_64, or Linux. From this directory:

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

## Example AI prompt

I'm completing a take-home security assessment as part of a job interview. The exercise authorizes me to test a disposable ERPNext v16.34.0 instance that I run locally with Docker at http://127.0.0.1:8080. The customer, E Corp, is fictional, and all data and accounts are synthetic.

The rules and the task are in README.md and Cyber-FDE-Final-Exercise.md in this directory. Read both before doing anything else.

Boundaries (follow them exactly): work only against the local target, its containers, and the upstream ERPNext v16.34.0 and Frappe v16.33.0 source. Keep everything on localhost. No external hosts, no denial of service, no mail to real recipients, and no sending target data or credentials to any other third-party service. If a step might cross a boundary, stop and ask me.

The brief limits the assessment to three focus areas: portal data isolation, internal role separation, and advisory applicability for those areas. Stay within them. If we notice something outside them, note it for next steps and move on.

## Deliverables

Submit a written report and your presentation materials to the coordinator. For the three focus areas, explain in the report your plan and rationale, actions and lessons from each round, evidence and reproduction steps, impact and preconditions, confidence and assumptions. Distinguish observations from hypotheses, including failed tests and disproved concerns. Prioritize recommendations and explain what you would test next and why. List observations outside the three focus areas under next steps only. List tools and AI assistance used, their contributions, and how you checked their output. A well-supported negative or limited result is a valid outcome; we assess your reasoning and evidence, not the number of findings.

In your report and presentation, recommend launch, a narrower launch, or delay. State launch conditions, who accepts the remaining risk, and what evidence would change your view.

Prepare a 30-minute customer-facing presentation for E Corp's technical lead and business owner, including discussion and questions. Plan to present for about 15 minutes. Choose your format and explain impact, evidence, confidence, priorities, and next steps to technical and nontechnical listeners. Be ready to defend your approach and assumptions.
