# Stock ERPNext v16 runtime verification

Verified 2026-11-12 on macOS arm64 with Docker Desktop, project `cyberfde`. The fresh startup, setup and sales login were rechecked after the E Corp fixture rename; other rows record the earlier runtime verification. All records and credentials are fictional and disposable. The stock image was already cached. Commands below run from `candidate/` unless stated otherwise.

| Check | Result | Evidence |
| --- | --- | --- |
| Image and architecture | PASS | `docker image inspect` reported `linux/arm64`; `bench version` reported ERPNext 16.34.0 and Frappe 16.33.0. Compose uses official index digest `sha256:1a91412a37c58d7829d8a8e078f01fdfa068ef136a2212dd1579d32f030c10c3`. |
| Source provenance | PASS for first-party source | Extracted image source using `docker create` and `docker cp`, then compared with `diff -rq` against ERPNext v16.34.0 and Frappe v16.33.0 upstream tags, excluding `.git`, `node_modules`, `__pycache__`, `*.pyc`, `*.egg-info`, and `dist`. Generated front-end assets were not rebuilt for comparison. ERPNext `banking/yarn.lock` differs: the image resolves follow-redirects 1.16.0 versus 1.15.11 and proxy-from-env 2.1.0 versus 1.1.0 in the tag. |
| Empty-volume startup | PASS | `./assessment.sh up` reached login in 56 seconds with cached images. The earlier fixture revision was exercised by reset in 62 seconds, including teardown; a fresh startup also succeeded after the rename. |
| Setup wizard | PASS | After a fresh startup, `frappe.db.get_single_value('System Settings','setup_complete')` returned 1 and `frappe.db.get_value` returned `["E Corp", "EC"]` for the company name and abbreviation. |
| Login page and users | PASS | After the rename, POST `/api/method/login` returned HTTP 200 for `sales@example.invalid` with `assessment-demo`. Earlier verification returned HTTP 200 for Administrator and all four fixture users. |
| Desk permissions | PASS | Sales User listed Sales Orders (200); Accounts User listed Sales Invoices (200); Auditor listed Accounts (200) and create Account returned 403. |
| Portal scope | PASS | `/orders` returned 200 and listed Northstar order `SAL-ORD-2026-00001`; its detail returned 200. Bluebird order `SAL-ORD-2026-00002` returned 403. |
| Retained state | PASS | `docker compose -p cyberfde restart` followed by a Customer GET returned 200. Repeated `./assessment.sh up` succeeded with the existing site. |
| Reset | PASS | Created customer `Reset Marker` (200), ran `./assessment.sh reset` (62 seconds), then marker GET returned 404 and Northstar GET 200. |
| Fixture repeat | PASS | Re-ran the mounted fixture script via bench; Sales Order and Purchase Order counts remained two each. |
| Egress | PASS | `docker compose -p cyberfde exec -T backend python -c 'import socket; socket.create_connection(("1.1.1.1",443),timeout=3)'` returned `Network is unreachable`. |
| Exposure | PASS | `docker compose -p cyberfde port frontend 8080` returned `127.0.0.1:8080`; status showed no other published ports. Backend, DB, Redis, and workers use the internal network; only frontend also uses the public network. |
| Down | PASS | `./assessment.sh down`; project-filtered `docker ps -aq`, `docker network ls -q` and `docker volume ls -q` returned no results. Shared images retained. |

A true cold pull was not performed because the official image is shared. `docker buildx imagetools inspect --raw frappe/erpnext@sha256:4fe8ebe0aa9a238602331e127c69b667e67aec5eecc11190ba1d68749780fb7f` reports 893,564,459 compressed layer bytes (about 894 MB). At an assumed sustained 100 Mbit/s, transfer alone would take about 72 seconds; actual cold startup depends on network, registry, unpacking, and the DB/Redis images. This is an estimate, not a measurement.

Fixture inventory: two customers, two suppliers, two non-stock items, two submitted Sales Orders, two submitted Sales Invoices, two submitted Purchase Orders, and two private customer file attachments. Portal user is linked to Northstar through a Contact and the customer portal-user table. Administrator password is `admin`; the fixture script sets `assessment-demo` for all four fixture users (sales login reverified after the rename).
