# CONFIDENTIAL — Advisory triage

Retrieved 2026-11-12. Static triage only; no runtime validation and no claim of exploitability. Image ID sha256:1a91412a37c58d7829d8a8e078f01fdfa068ef136a2212dd1579d32f030c10c3. Source root in image: `/home/frappe/frappe-bench`.

## Image and provenance

Frappe **16.33.0**, ERPNext **16.34.0**, Python **3.14.7**, Node **24.20.0**. The image removes `.git` in both apps: exact image commits cannot be proven from Git metadata. Upstream tag references resolve to [Frappe 33bf510b17afcaaa857ed38b921d8e9e50dcd232](https://github.com/frappe/frappe/tree/33bf510b17afcaaa857ed38b921d8e9e50dcd232) and [ERPNext 80c2c9e0e000dad049366810919426449519ada5](https://github.com/frappe/erpnext/tree/80c2c9e0e000dad049366810919426449519ada5); these are tag commits, not verified image commits. Compare full source trees before treating as identical.

Installed Python inventory (`env/bin/pip freeze`):
```
annotated-types==0.8.0
asttokens==3.0.2
babel==2.16.0
barcodenumber==0.5.0
beautifulsoup4==4.13.5
bleach-allowlist==1.0.3
brotli==1.2.0
cachetools==7.1.8
certifi==2026.7.22
cffi==2.1.1
chardet==5.2.0
charset-normalizer==3.5.1
click==8.4.2
croniter==6.0.0
cryptography==50.0.1
cssselect==1.5.0
cssselect2==0.10.1
cssutils==2.11.1
dataclasses-json==0.6.7
decorator==5.3.1
distro==1.9.0
docopt==0.6.2
duckdb==1.4.5
email-reply-parser==0.5.12
# Editable install with no version control (erpnext==16.34.0)
-e /home/frappe/frappe-bench/apps/erpnext
et_xmlfile==2.0.0
executing==2.2.1
filelock==3.20.4
filetype==1.2.0
fonttools==4.64.0
# Editable install with no version control (frappe==16.33.0)
-e /home/frappe/frappe-bench/apps/frappe
gitdb==4.0.12
GitPython==3.1.61
google-api-core==2.34.0
google-api-python-client==2.188.0
google-auth==2.48.0
google-auth-httplib2==0.4.2
google-auth-oauthlib==1.2.4
googleapis-common-protos==1.75.2
googlemaps==4.10.0
gunicorn @ git+https://github.com/frappe/gunicorn@54b59ca884c79dcf04d4882658a32bbaf17e999f
hiredis==3.3.1
holidays==0.103
html5lib==1.1
httplib2==0.32.0
idna==3.19
ipython==8.37.0
isodate==0.7.2
jedi==0.20.0
Jinja2==3.1.6
ldap3==2.9.1
lxml==6.1.2
markdown2==2.5.5
markdownify==1.2.3
MarkupSafe==3.0.3
marshmallow==3.26.2
matplotlib-inline==0.2.2
more-itertools==11.1.0
mt-940==5.0.0
mypy_extensions==1.1.0
mysqlclient==2.2.7
nh3==0.3.7
num2words==0.5.14
oauthlib==3.3.1
openpyxl==3.1.5
orjson==3.11.9
packaging==26.3
parso==0.8.7
passlib==1.7.4
pdfkit==1.0.0
pdfminer.six==20260107
pdfplumber==0.11.10
pexpect==4.9.0
phonenumbers==9.0.38
pillow==12.3.0
plaid-python==7.2.1
premailer==3.10.0
prompt_toolkit==3.0.53
proto-plus==1.28.4
protobuf==7.36.1
psutil==7.0.0
psycopg2-binary==2.9.12
ptyprocess==0.7.0
pure_eval==0.2.3
pyarrow==25.0.1
pyasn1==0.6.4
pyasn1_modules==0.4.2
pycountry==24.6.1
pycparser==3.0
pydantic==2.12.5
pydantic_core==2.41.5
pydyf==0.12.1
Pygments==2.21.0
PyJWT==2.13.0
PyMySQL==1.1.2
pyOpenSSL==26.4.0
pyotp==2.9.0
pyparsing==3.3.2
pypdf==6.15.0
pypdfium2==5.13.0
pyphen==0.18.1
PyPika @ git+https://github.com/frappe/pypika@2c50e6142b2d61d2d243e466fdd5dc03b3d918f2
pypng==0.20220715.0
PyQRCode==1.2.1
python-dateutil==2.9.0.post0
python-stdnum==2.2
python-youtube==0.9.9
pytz==2025.2
PyYAML==6.0.3
RapidFuzz==3.14.6
rauth==0.7.3
redis==7.1.1
requests==2.33.1
requests-oauthlib==2.0.0
RestrictedPython==8.5
rq==2.6.1
rsa==4.9.1
semantic-version==2.10.0
sentry-sdk==1.45.1
six==1.17.0
smmap==5.0.3
soupsieve==2.9.2
sql_metadata==3.0.1
sqlglot==30.17.0
sqlparse==0.6.0
stack-data==0.6.3
tenacity==9.1.4
terminaltables==3.1.10
tinycss2==1.5.1
tinyhtml5==2.1.0
traceback-with-variables==2.2.1
traitlets==5.16.1
typing-inspect==0.9.0
typing-inspection==0.4.4
typing_extensions==4.16.0
Unidecode==1.4.0
uritemplate==4.2.0
urllib3==2.7.0
vobject==0.9.9
wcwidth==0.8.3
weasyprint==68.0
webencodings==0.6.1
websockets==15.0.1
Werkzeug==3.1.6
Whoosh==2.7.4
xlrd==2.0.2
xlsxwriter==3.2.9
zopfli==0.4.3
zxcvbn==4.5.0
```

JS lockfiles shipped (SHA-256; all paths below `apps/`; lockfiles contain exact package versions and transitive resolution, not proof of runtime bundling):
```
4e39da1b48edcc235f1973302d96b283219b44774f07f447256319b66adfa608  apps/frappe/yarn.lock
6042d7dc9d09df104e18912d2f2f0fa63fa6329adb30ee72e7835b03b8b4090a  apps/frappe/ui/yarn.lock
ba6a3285c968d3e7ac606652b1aee15ed9c3ea133c019a7c0697533cf5dad8f0  apps/erpnext/yarn.lock
267d9f2306b991e414608760b78929512f4b98ac14be9880e28aac5eac958433  apps/erpnext/banking/yarn.lock
```

## Priority runtime validation candidates

1. [GHSA-cc74-rc2g-p7hw](https://github.com/frappe/erpnext/security/advisories/GHSA-cc74-rc2g-p7hw) — ERPNext SQL injection, advisory says any authenticated user including portal without roles; fixed 16.37.0. Selling/buying controllers exist (`apps/erpnext/erpnext/controllers/`); exact endpoint and its code path not identified, so default-site reachability is unverified.
2. [GHSA-r8px-9662-x39c](https://github.com/frappe/frappe/security/advisories/GHSA-r8px-9662-x39c) — file attachment read; advisory says one ordinary role, no write permission; fixed 16.33.1. File handling code exists (`apps/frappe/frappe/core/doctype/file/file.py`, `apps/frappe/frappe/utils/file_manager.py`), but exact vulnerable path and ability to trigger remain unverified.
3. [GHSA-9pp9-wgp9-3p3j](https://github.com/frappe/frappe/security/advisories/GHSA-9pp9-wgp9-3p3j) — authenticated upload destination traversal with potential RCE, fixed 16.34.0; upload/file handlers exist (`apps/frappe/frappe/handler.py`, `apps/frappe/frappe/utils/file_manager.py`). Specific permission and vulnerable path unknown; prioritize only if a low-privilege user can reach it.

## Repository advisory inventory

Source: GitHub repository security-advisory API for [Frappe](https://api.github.com/repos/frappe/frappe/security-advisories?per_page=100) and [ERPNext](https://api.github.com/repos/frappe/erpnext/security-advisories?per_page=100). Deduplicated by GHSA and limited to records published by 2026-11-12 UTC. Classification evaluates explicit 16.x ranges using PEP 440; no explicit 16.x range = unknown (not proof of impact). A range naming only another major is conservatively unknown. Table entries represent advisory version matching, not verified vulnerable code: unless discussed above, source path, feature configuration, auth level and exact preconditions are **not checked**. Older-major ranges and additional records may be missing.

Counts in this incomplete, deduplicated repository feed: version-affected: 76, not-affected: 66, unknown: 55.

| Repo | Advisory | CVE | Summary | 16.x affected range | Class |
|---|---|---|---|---|---|
| frappe | [GHSA-37jh-f235-72qp](https://github.com/frappe/frappe/security/advisories/GHSA-37jh-f235-72qp) | — | Unauthorized document submission and modification due to missing validation in Document.update() | <16.50.0 | version-affected |
| frappe | [GHSA-qrxv-3vjh-gpx7](https://github.com/frappe/frappe/security/advisories/GHSA-qrxv-3vjh-gpx7) | — | Sandbox bypass via imported functions leaking into Jinja globals through module-path hooks | <16.36.0 | version-affected |
| frappe | [GHSA-6pmg-vc6m-6wrr](https://github.com/frappe/frappe/security/advisories/GHSA-6pmg-vc6m-6wrr) | CVE-2026-119144 | Possibility of Server Side Template Injection | <16.21.0 | not-affected |
| frappe | [GHSA-9pp9-wgp9-3p3j](https://github.com/frappe/frappe/security/advisories/GHSA-9pp9-wgp9-3p3j) | — | Remote code execution via path traversal | < 16.34.0 | version-affected |
| frappe | [GHSA-h3mh-9vmc-cpfg](https://github.com/frappe/frappe/security/advisories/GHSA-h3mh-9vmc-cpfg) | — | OAuth2 password grant bypasses two-factor authentication | <16.35.0 | version-affected |
| frappe | [GHSA-r8px-9662-x39c](https://github.com/frappe/frappe/security/advisories/GHSA-r8px-9662-x39c) | — | Authenticated Arbitrary File Read via File Attachment Handling | <16.33.1 | version-affected |
| frappe | [GHSA-wrh5-p77r-jpvq](https://github.com/frappe/frappe/security/advisories/GHSA-wrh5-p77r-jpvq) | — | Unauthorized users can send sms via the API | no 16.x range | unknown |
| frappe | [GHSA-vp4r-5v6w-r962](https://github.com/frappe/frappe/security/advisories/GHSA-vp4r-5v6w-r962) | — | Blind SQL Injection via X-Frappe-Request-Id header | <16.33.0 | not-affected |
| frappe | [GHSA-p4w2-9mr5-6prj](https://github.com/frappe/frappe/security/advisories/GHSA-p4w2-9mr5-6prj) | — | Blind SQL Injection in frappe.desk.doctype.event.event.get_events | <16.33.0 | not-affected |
| frappe | [GHSA-c76w-4wg2-hpgf](https://github.com/frappe/frappe/security/advisories/GHSA-c76w-4wg2-hpgf) | — | Stored spreadsheet formula injection in CSV and XLSX exports | <16.32.0 | not-affected |
| frappe | [GHSA-h9jq-7pgf-hw8q](https://github.com/frappe/frappe/security/advisories/GHSA-h9jq-7pgf-hw8q) | — | restrict_ip allowlist bypassed for API key, OAuth, and header-based authentication | <16.33.0 | not-affected |
| frappe | [GHSA-22v9-hw3x-x59w](https://github.com/frappe/frappe/security/advisories/GHSA-22v9-hw3x-x59w) | — | Unauthorised modification of records due to missing validation | < 16.25.0 | not-affected |
| frappe | [GHSA-7cxg-q8x5-rpjh](https://github.com/frappe/frappe/security/advisories/GHSA-7cxg-q8x5-rpjh) | — | Broken Access Control in File list/report queries | <16.35.0 | version-affected |
| frappe | [GHSA-55m4-gj6h-q6rc](https://github.com/frappe/frappe/security/advisories/GHSA-55m4-gj6h-q6rc) | — | Disabled users continue to receive Document Follow email notifications | <16.31.0 | not-affected |
| frappe | [GHSA-8v98-cfpm-9p67](https://github.com/frappe/frappe/security/advisories/GHSA-8v98-cfpm-9p67) | CVE-2026-109601 | Arbitrary file read via an attribute in outgoing email HTML | no 16.x range | unknown |
| frappe | [GHSA-hxfh-hh23-fvch](https://github.com/frappe/frappe/security/advisories/GHSA-hxfh-hh23-fvch) | — | Stored XSS in dashboard chart | no 16.x range | unknown |
| frappe | [GHSA-r8gf-89pc-pmv3](https://github.com/frappe/frappe/security/advisories/GHSA-r8gf-89pc-pmv3) | — | IDOR via an SMS Settings' API | <16.30.0 | not-affected |
| frappe | [GHSA-7vpf-q96h-59x4](https://github.com/frappe/frappe/security/advisories/GHSA-7vpf-q96h-59x4) | CVE-2026-66059 | Field-level permission bypass via Document Follow | <16.23.0 | not-affected |
| frappe | [GHSA-fgx7-fvpx-mw3g](https://github.com/frappe/frappe/security/advisories/GHSA-fgx7-fvpx-mw3g) | CVE-2026-66058 | Unrestricted access to a Document Follow API | <16.23.0 | not-affected |
| frappe | [GHSA-78c5-55xg-jm7m](https://github.com/frappe/frappe/security/advisories/GHSA-78c5-55xg-jm7m) | CVE-2026-66057 | Open Redirect via Unsanitized OAuth State Param. | no 16.x range | unknown |
| frappe | [GHSA-p25m-7rvg-6fvr](https://github.com/frappe/frappe/security/advisories/GHSA-p25m-7rvg-6fvr) | CVE-2026-66003 | Access control bypass via REST API | no 16.x range | unknown |
| frappe | [GHSA-c2xv-c53h-qvr5](https://github.com/frappe/frappe/security/advisories/GHSA-c2xv-c53h-qvr5) | CVE-2026-66002 | User Enumeration via PDDR | no 16.x range | unknown |
| frappe | [GHSA-2ph8-x773-8p2x](https://github.com/frappe/frappe/security/advisories/GHSA-2ph8-x773-8p2x) | CVE-2026-66001 | Improper Authorization in OAuth2 Consent Endpoint | <16.26.0 | not-affected |
| frappe | [GHSA-cgwf-xgph-hxgm](https://github.com/frappe/frappe/security/advisories/GHSA-cgwf-xgph-hxgm) | CVE-2026-63654 | Unauthenticated Workflow approval | no 16.x range | unknown |
| frappe | [GHSA-2c6h-wv85-fxvj](https://github.com/frappe/frappe/security/advisories/GHSA-2c6h-wv85-fxvj) | CVE-2026-62315 | Mass assignment in client endpoint | no 16.x range | unknown |
| frappe | [GHSA-3vqc-c545-w7jg](https://github.com/frappe/frappe/security/advisories/GHSA-3vqc-c545-w7jg) | CVE-2026-58503 | Unauthenticated User Enumeration via reset_password | <v16.16.0 | not-affected |
| frappe | [GHSA-58w2-4cjg-hvp6](https://github.com/frappe/frappe/security/advisories/GHSA-58w2-4cjg-hvp6) | CVE-2026-55852 | TarSlip RCE in Package Import | <16.23.0 | not-affected |
| frappe | [GHSA-mf6r-q34j-pjw7](https://github.com/frappe/frappe/security/advisories/GHSA-mf6r-q34j-pjw7) | CVE-2026-55823 | Possibility of SQL injection in reportview | <16.23.0 | not-affected |
| frappe | [GHSA-wcm9-vvcc-r8pr](https://github.com/frappe/frappe/security/advisories/GHSA-wcm9-vvcc-r8pr) | CVE-2026-66000 | Stale authorization in Document Follow allows revoked users to continue receiving document data | <16.23.0 | not-affected |
| frappe | [GHSA-rx6h-4p83-m76x](https://github.com/frappe/frappe/security/advisories/GHSA-rx6h-4p83-m76x) | CVE-2026-53569 | Missing authorization in toggle_like and mark_as_seen | no 16.x range | unknown |
| frappe | [GHSA-pj59-9hv9-rmrv](https://github.com/frappe/frappe/security/advisories/GHSA-pj59-9hv9-rmrv) | — | Authenticated SSRF / LFI via pdfkit | <16.17.0 | not-affected |
| frappe | [GHSA-r24j-xrj8-273q](https://github.com/frappe/frappe/security/advisories/GHSA-r24j-xrj8-273q) | CVE-2026-49394 | Auth. bypass via update_page | <16.19.0 | not-affected |
| frappe | [GHSA-7f28-gm9h-q6rg](https://github.com/frappe/frappe/security/advisories/GHSA-7f28-gm9h-q6rg) | CVE-2026-49391 | Stored XSS via Data Import | <16.19.0 | not-affected |
| frappe | [GHSA-fwrv-4rw4-97fw](https://github.com/frappe/frappe/security/advisories/GHSA-fwrv-4rw4-97fw) | CVE-2026-48127 | Arbitrary File Attachment Injection via File-Handling API Endpoints | <16.20.0 | not-affected |
| frappe | [GHSA-cjjx-3v2x-37mf](https://github.com/frappe/frappe/security/advisories/GHSA-cjjx-3v2x-37mf) | CVE-2026-47765 | Lack of Permissions in restore/bulk_restore | no 16.x range | unknown |
| frappe | [GHSA-w8g7-j846-j248](https://github.com/frappe/frappe/security/advisories/GHSA-w8g7-j846-j248) | CVE-2026-47422 | Unrestricted API access to an API in reportview | no 16.x range | unknown |
| frappe | [GHSA-89m3-vggh-725v](https://github.com/frappe/frappe/security/advisories/GHSA-89m3-vggh-725v) | CVE-2026-47278 | Comment Spoofing | <16.18.3 | not-affected |
| frappe | [GHSA-wx8j-cw4r-vrhv](https://github.com/frappe/frappe/security/advisories/GHSA-wx8j-cw4r-vrhv) | CVE-2026-47199 | check_safe_sql_query Permits SELECT INTO OUTFILE | no 16.x range | unknown |
| frappe | [GHSA-3w78-3cj3-p949](https://github.com/frappe/frappe/security/advisories/GHSA-3w78-3cj3-p949) | CVE-2026-47194 | Host header poisoning can redirect magic login links to an attacker-controlled domain | no 16.x range | unknown |
| frappe | [GHSA-mcr4-jc52-ww6x](https://github.com/frappe/frappe/security/advisories/GHSA-mcr4-jc52-ww6x) | CVE-2026-47185 | Broken Access Control in Workspace Save API  | <16.18.0 | not-affected |
| frappe | [GHSA-gvg7-4p32-j648](https://github.com/frappe/frappe/security/advisories/GHSA-gvg7-4p32-j648) | CVE-2026-47182 | Broken Access Control on Private Files | < 16.17.4 | not-affected |
| frappe | [GHSA-78rj-jch8-42m8](https://github.com/frappe/frappe/security/advisories/GHSA-78rj-jch8-42m8) | CVE-2026-44976 | IDOR in update_onboarding_step | <16.17.4  | not-affected |
| frappe | [GHSA-9cxj-48g3-jx22](https://github.com/frappe/frappe/security/advisories/GHSA-9cxj-48g3-jx22) | CVE-2026-44975 | Missing authorization on reset form tours | <16.17.4 | not-affected |
| frappe | [GHSA-9c55-cq5r-qj5x](https://github.com/frappe/frappe/security/advisories/GHSA-9c55-cq5r-qj5x) | CVE-2026-44206 | DB Schema Enumeration | no 16.x range | unknown |
| frappe | [GHSA-cw6v-39qx-7r74](https://github.com/frappe/frappe/security/advisories/GHSA-cw6v-39qx-7r74) | CVE-2026-44207 | Insecure Direct Object Reference for email accounts | < 16.17.0 | not-affected |
| frappe | [GHSA-rx63-c3fh-8926](https://github.com/frappe/frappe/security/advisories/GHSA-rx63-c3fh-8926) | CVE-2026-53568 | Stored XSS in Frappe Report/List View. | no 16.x range | unknown |
| frappe | [GHSA-xh7m-j2j2-82f2](https://github.com/frappe/frappe/security/advisories/GHSA-xh7m-j2j2-82f2) | CVE-2026-44208 |  IDOR in `submit_discussion()` | <16.17.0 | not-affected |
| frappe | [GHSA-q6m6-759h-46jp](https://github.com/frappe/frappe/security/advisories/GHSA-q6m6-759h-46jp) | CVE-2026-50026 | Lack of permissions checks in 'relink' and 'set_email_password' endpoints | no 16.x range | unknown |
| frappe | [GHSA-2wx6-8gmq-x4fw](https://github.com/frappe/frappe/security/advisories/GHSA-2wx6-8gmq-x4fw) | CVE-2026-44205 | Stored Cross-Site Scripting (XSS) in User Profile through Image Upload | no 16.x range | unknown |
| frappe | [GHSA-w4p4-fp9m-47gj](https://github.com/frappe/frappe/security/advisories/GHSA-w4p4-fp9m-47gj) | CVE-2026-42219 | Path Traversal via 'download_backups' | <16.19.0 | not-affected |
| frappe | [GHSA-h9hf-57r4-cm65](https://github.com/frappe/frappe/security/advisories/GHSA-h9hf-57r4-cm65) | CVE-2026-41581 | Possible SQL Injection via get_blog_list | <16.16.0 | not-affected |
| frappe | [GHSA-234v-jfr8-v2f8](https://github.com/frappe/frappe/security/advisories/GHSA-234v-jfr8-v2f8) | CVE-2026-41482 | Possible Path Traversal and Local File Inclusion via Chrome PDF Generator | <16.18.3 | not-affected |
| frappe | [GHSA-vxmp-h244-wv3r](https://github.com/frappe/frappe/security/advisories/GHSA-vxmp-h244-wv3r) | CVE-2026-47739 | Stored XSS in Note | <16.16.0 | not-affected |
| frappe | [GHSA-67rf-pxgh-vfqv](https://github.com/frappe/frappe/security/advisories/GHSA-67rf-pxgh-vfqv) | CVE-2026-39352 | Arbitrary File Read via Path Traversal | <16.15.0 | not-affected |
| frappe | [GHSA-583g-fg76-fhfr](https://github.com/frappe/frappe/security/advisories/GHSA-583g-fg76-fhfr) | CVE-2026-35614 | Possibility of SQL injection in bulk_update | <16.14.0 | not-affected |
| frappe | [GHSA-8ggw-hfr6-rw3x](https://github.com/frappe/frappe/security/advisories/GHSA-8ggw-hfr6-rw3x) | CVE-2026-39351 | Unrestricted Doctype access via API exploit | <16.14.0 | not-affected |
| frappe | [GHSA-2c4m-999q-xhx4](https://github.com/frappe/frappe/security/advisories/GHSA-2c4m-999q-xhx4) | CVE-2026-31877 | Possibility of SQL Injection due to improper field sanitization | no 16.x range | unknown |
| frappe | [GHSA-mggg-hmjm-j6c2](https://github.com/frappe/frappe/security/advisories/GHSA-mggg-hmjm-j6c2) | CVE-2026-31878 | Possible SSRF by any authenticated user | <16.6.0 | not-affected |
| frappe | [GHSA-qmhf-rgx2-8p25](https://github.com/frappe/frappe/security/advisories/GHSA-qmhf-rgx2-8p25) | CVE-2026-31879 | Workspace modification and stored XSS due to improper resource ownership checks | <16.10.0 | not-affected |
| frappe | [GHSA-w3g7-m7xr-2w38](https://github.com/frappe/frappe/security/advisories/GHSA-w3g7-m7xr-2w38) | CVE-2026-29081 | Possibility of SQL Injection due to improper fieldname sanitization | no 16.x range | unknown |
| frappe | [GHSA-5h4c-9p23-4c3m](https://github.com/frappe/frappe/security/advisories/GHSA-5h4c-9p23-4c3m) | CVE-2026-29077 | Broken Access Control in DocShare | no 16.x range | unknown |
| frappe | [GHSA-vm63-r48g-7wqh](https://github.com/frappe/frappe/security/advisories/GHSA-vm63-r48g-7wqh) | CVE-2026-28436 | Stored XSS in avatar_macro.html | 16.11.0 | unknown |
| frappe | [GHSA-7m8v-g2pr-h2f7](https://github.com/frappe/frappe/security/advisories/GHSA-7m8v-g2pr-h2f7) | CVE-2026-25956 | XSS and Open Redirect in Sign Up | no 16.x range | unknown |
| frappe | [GHSA-qq98-vfv9-xmxh](https://github.com/frappe/frappe/security/advisories/GHSA-qq98-vfv9-xmxh) | CVE-2025-68929 | Possibility of RCE due to SSTI | no 16.x range | unknown |
| frappe | [GHSA-cx24-w5gm-5vv9](https://github.com/frappe/frappe/security/advisories/GHSA-cx24-w5gm-5vv9) | — | Authenticated XSS via leaderboard | no 16.x range | unknown |
| frappe | [GHSA-xj39-3g4p-f46v](https://github.com/frappe/frappe/security/advisories/GHSA-xj39-3g4p-f46v) | CVE-2025-68953 | Path traversal allowed reading certain files | no 16.x range | unknown |
| frappe | [GHSA-mp93-8vxr-hqq9](https://github.com/frappe/frappe/security/advisories/GHSA-mp93-8vxr-hqq9) | CVE-2025-66205 | Possibility of SQL Injection due to improper validations | no 16.x range | unknown |
| frappe | [GHSA-v4wg-gqfr-rpjm](https://github.com/frappe/frappe/security/advisories/GHSA-v4wg-gqfr-rpjm) | CVE-2025-66206 | Path traversal allowed reading certain files | no 16.x range | unknown |
| frappe | [GHSA-j9jr-qrpj-g855](https://github.com/frappe/frappe/security/advisories/GHSA-j9jr-qrpj-g855) | CVE-2025-62407 | Open Redirect on Login Page | no 16.x range | unknown |
| frappe | [GHSA-qrq5-v93p-8xhw](https://github.com/frappe/frappe/security/advisories/GHSA-qrq5-v93p-8xhw) | — | Possible LDAP injection due to unsanitised inputs | no 16.x range | unknown |
| frappe | [GHSA-mggw-6xqj-rphj](https://github.com/frappe/frappe/security/advisories/GHSA-mggw-6xqj-rphj) | CVE-2025-52048 | Possibility of SQL injection due to missing validation | no 16.x range | unknown |
| frappe | [GHSA-6rpr-2hjx-w9vp](https://github.com/frappe/frappe/security/advisories/GHSA-6rpr-2hjx-w9vp) | CVE-2025-55732 | Possibility of SQL Injection due to improper validations | no 16.x range | unknown |
| frappe | [GHSA-5p8f-568f-vfq2](https://github.com/frappe/frappe/security/advisories/GHSA-5p8f-568f-vfq2) | CVE-2025-55731 | Possibility of Authenticated SQL Injection due to improper validations | no 16.x range | unknown |
| frappe | [GHSA-cprh-gp85-wxvq](https://github.com/frappe/frappe/security/advisories/GHSA-cprh-gp85-wxvq) | CVE-2025-28062 | Account takeover via CSRF | no 16.x range | unknown |
| frappe | [GHSA-p284-r7rh-wq7j](https://github.com/frappe/frappe/security/advisories/GHSA-p284-r7rh-wq7j) | CVE-2025-52898 | Account takeover via password reset token leakage | no 16.x range | unknown |
| frappe | [GHSA-hv29-66qg-2v6p](https://github.com/frappe/frappe/security/advisories/GHSA-hv29-66qg-2v6p) | CVE-2025-52896 | Authenticated XSS via data import | no 16.x range | unknown |
| frappe | [GHSA-mhj8-jfhf-mcw9](https://github.com/frappe/frappe/security/advisories/GHSA-mhj8-jfhf-mcw9) | CVE-2025-52895 | Possibility of SQL injection due to improper validations | no 16.x range | unknown |
| frappe | [GHSA-6phg-4wmq-h5h3](https://github.com/frappe/frappe/security/advisories/GHSA-6phg-4wmq-h5h3) | CVE-2025-30217 | Possibility of SQL injection due to improper validations | no 16.x range | unknown |
| frappe | [GHSA-v342-4xr9-x3q3](https://github.com/frappe/frappe/security/advisories/GHSA-v342-4xr9-x3q3) | CVE-2025-30213 | Possibility of Remote Code Execution due to improper validation | no 16.x range | unknown |
| frappe | [GHSA-qrv3-jc3h-f3m6](https://github.com/frappe/frappe/security/advisories/GHSA-qrv3-jc3h-f3m6) | CVE-2025-30214 | Information disclosure leading to account takeover | no 16.x range | unknown |
| frappe | [GHSA-3hj6-r5c9-q8f3](https://github.com/frappe/frappe/security/advisories/GHSA-3hj6-r5c9-q8f3) | CVE-2025-30212 | Possibility of SQL injection due to improper validations | no 16.x range | unknown |
| frappe | [GHSA-gjqf-v2f6-962h](https://github.com/frappe/frappe/security/advisories/GHSA-gjqf-v2f6-962h) | — | Privilege escalation via document action | no 16.x range | unknown |
| frappe | [GHSA-7g27-q225-j894](https://github.com/frappe/frappe/security/advisories/GHSA-7g27-q225-j894) | CVE-2024-34074 | Open redirect on login page | no 16.x range | unknown |
| frappe | [GHSA-hq5v-q29v-7rcw](https://github.com/frappe/frappe/security/advisories/GHSA-hq5v-q29v-7rcw) | CVE-2024-27105 | File Permissions can by bypassed using certain endpoints | <15.16.0 | not-affected |
| frappe | [GHSA-fxfv-7gwx-54jh](https://github.com/frappe/frappe/security/advisories/GHSA-fxfv-7gwx-54jh) | CVE-2024-24813 | SQL Injection from reporting logic | no 16.x range | unknown |
| frappe | [GHSA-7p3m-h76m-hg9v](https://github.com/frappe/frappe/security/advisories/GHSA-7p3m-h76m-hg9v) | CVE-2024-24812 | Frappe Authenticated Reflected Cross site scripting (XSS) in portal pages | no 16.x range | unknown |
| frappe | [GHSA-v3vh-7qx4-f582](https://github.com/frappe/frappe/security/advisories/GHSA-v3vh-7qx4-f582) | — | frappe.flags.in_safe_exec can become False while executing a Server Script | no 16.x range | unknown |
| frappe | [GHSA-v248-pv3c-jvgw](https://github.com/frappe/frappe/security/advisories/GHSA-v248-pv3c-jvgw) | — | HTML injection in printview | no 16.x range | unknown |
| frappe | [GHSA-439c-3956-r8q7](https://github.com/frappe/frappe/security/advisories/GHSA-439c-3956-r8q7) | CVE-2023-51769 | Cross-Site Scripting (XSS) Attack on exceptions and Blog Page | no 16.x range | unknown |
| frappe | [GHSA-j2w9-8xrr-7g98](https://github.com/frappe/frappe/security/advisories/GHSA-j2w9-8xrr-7g98) | CVE-2023-46127 | Possible HTML injection by any Desk user | no 16.x range | unknown |
| frappe | [GHSA-38fg-mjcm-3hc6](https://github.com/frappe/frappe/security/advisories/GHSA-38fg-mjcm-3hc6) | — | Error logs could potentially leak secrets | no 16.x range | unknown |
| frappe | [GHSA-4jj9-5vgc-gc4j](https://github.com/frappe/frappe/security/advisories/GHSA-4jj9-5vgc-gc4j) | — | Possible HTML Injection attack | no 16.x range | unknown |
| frappe | [GHSA-53wh-f67g-9679](https://github.com/frappe/frappe/security/advisories/GHSA-53wh-f67g-9679) | CVE-2023-41328 | Possibility of limited SQL injection due to insufficient validation | no 16.x range | unknown |
| frappe | [GHSA-wp7j-3w22-93j6](https://github.com/frappe/frappe/security/advisories/GHSA-wp7j-3w22-93j6) | — | html2text is not safe on user input | no 16.x range | unknown |
| frappe | [GHSA-whww-ggp5-r2xq](https://github.com/frappe/frappe/security/advisories/GHSA-whww-ggp5-r2xq) | — | Improper Authorization while renaming docs | no 16.x range | unknown |
| frappe | [GHSA-7xv4-ggpj-g48q](https://github.com/frappe/frappe/security/advisories/GHSA-7xv4-ggpj-g48q) | — | Weak authentication when accessing print view using key | no 16.x range | unknown |
| frappe | [GHSA-f939-v9q6-j3wg](https://github.com/frappe/frappe/security/advisories/GHSA-f939-v9q6-j3wg) | — | Improper Access Control for Email Templates | no 16.x range | unknown |
| erpnext | [GHSA-cc74-rc2g-p7hw](https://github.com/frappe/erpnext/security/advisories/GHSA-cc74-rc2g-p7hw) | — | Possibility of SQL injection in the Selling and Buying modules due to missing validation | < 16.37.0 | version-affected |
| erpnext | [GHSA-ggr3-x356-w97h](https://github.com/frappe/erpnext/security/advisories/GHSA-ggr3-x356-w97h) | — | Unauthorised modification of bulk transaction logs in the Utilities module due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-grg4-q5gc-4g4x](https://github.com/frappe/erpnext/security/advisories/GHSA-grg4-q5gc-4g4x) | — | Unauthorised access to asset depreciation data of other companies in the Assets module due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-45p2-2pp7-f8w2](https://github.com/frappe/erpnext/security/advisories/GHSA-45p2-2pp7-f8w2) | — | Unauthorised access to Payment Entries outside the user's permissions in the Accounts module due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-chqg-f85c-wxr7](https://github.com/frappe/erpnext/security/advisories/GHSA-chqg-f85c-wxr7) | — | Unauthorised access to subscription plan details of invoices in the Accounts module due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-6937-44rq-87xr](https://github.com/frappe/erpnext/security/advisories/GHSA-6937-44rq-87xr) | — | Unauthorised access to Timesheet billing data in the Projects module due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-9jrr-9pr6-7mv8](https://github.com/frappe/erpnext/security/advisories/GHSA-9jrr-9pr6-7mv8) | — | Exposure of imported supplier e-invoices as public files in the Regional module | < 16.52.0 | version-affected |
| erpnext | [GHSA-c3mc-qh7f-hwcv](https://github.com/frappe/erpnext/security/advisories/GHSA-c3mc-qh7f-hwcv) | — | Unauthorised stopping and closing of Work Orders of other companies in the Manufacturing module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-mmcf-jq27-crrp](https://github.com/frappe/erpnext/security/advisories/GHSA-mmcf-jq27-crrp) | — | Unauthorised closing of Purchase Orders of other companies in the Buying module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-jfr9-q72f-854x](https://github.com/frappe/erpnext/security/advisories/GHSA-jfr9-q72f-854x) | — | Unauthorised closing of Sales Orders of other companies in the Selling module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-fjj8-qq2m-h96w](https://github.com/frappe/erpnext/security/advisories/GHSA-fjj8-qq2m-h96w) | — | Unauthorised reposting of accounting entries in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-98p6-cv49-h8c3](https://github.com/frappe/erpnext/security/advisories/GHSA-98p6-cv49-h8c3) | — | Unauthorised access to item valuation and average purchase cost in the Stock module due to missing validation | < 16.53.0 | version-affected |
| erpnext | [GHSA-8mhv-pfp8-m66q](https://github.com/frappe/erpnext/security/advisories/GHSA-8mhv-pfp8-m66q) | — | Unauthorised access to party addresses through Tax Rule in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-rcpm-332h-mj8f](https://github.com/frappe/erpnext/security/advisories/GHSA-rcpm-332h-mj8f) | — | Unauthorised access to inter-company invoice and order items in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-6vch-gx2g-m2cv](https://github.com/frappe/erpnext/security/advisories/GHSA-6vch-gx2g-m2cv) | — | Unauthorised access to account balances through a dashboard chart in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-gj65-6744-3fv4](https://github.com/frappe/erpnext/security/advisories/GHSA-gj65-6744-3fv4) | — | Stored cross-site scripting in CRM notes due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-64h3-xccr-q5jr](https://github.com/frappe/erpnext/security/advisories/GHSA-64h3-xccr-q5jr) | — | Unauthorised access to source documents through Payment Requests in the Accounts module due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-5jjr-hp7q-gmwr](https://github.com/frappe/erpnext/security/advisories/GHSA-5jjr-hp7q-gmwr) | — | Unauthorised creation of POS Invoice Merge Logs in POS due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-42cf-qgvq-xv9h](https://github.com/frappe/erpnext/security/advisories/GHSA-42cf-qgvq-xv9h) | — | Unauthorised access to Asset details in the Assets module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-x2f8-27qm-r3hf](https://github.com/frappe/erpnext/security/advisories/GHSA-x2f8-27qm-r3hf) | — | Unauthorised Stock Reservation Entries beyond Sales Order limits in the Stock module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-77q9-p3mx-p357](https://github.com/frappe/erpnext/security/advisories/GHSA-77q9-p3mx-p357) | — | Unauthorised BOM replacement in the Manufacturing module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-v3gf-jphf-f4xp](https://github.com/frappe/erpnext/security/advisories/GHSA-v3gf-jphf-f4xp) | — | Unauthorised unreconciliation of payments in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-qrv3-vxh2-xx3g](https://github.com/frappe/erpnext/security/advisories/GHSA-qrv3-vxh2-xx3g) | — | Unauthorised access to Bank Transaction amounts in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-9jx6-f65v-r6h7](https://github.com/frappe/erpnext/security/advisories/GHSA-9jx6-f65v-r6h7) | — | Unauthorised modification of bank reconciliation in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-4mg4-7qq3-phxc](https://github.com/frappe/erpnext/security/advisories/GHSA-4mg4-7qq3-phxc) | — | Unauthorised creation of Serial No and Batch records in the Stock module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-93gm-m6q2-39pc](https://github.com/frappe/erpnext/security/advisories/GHSA-93gm-m6q2-39pc) | — | Unauthorised status modification of Period Closing Voucher processing in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-877j-rg2w-v649](https://github.com/frappe/erpnext/security/advisories/GHSA-877j-rg2w-v649) | — | Unauthorised access to customer documents through print and portal views due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-hfj8-f2p9-f2xf](https://github.com/frappe/erpnext/security/advisories/GHSA-hfj8-f2p9-f2xf) | — | Unauthorised access to Sales Order items in the Selling module due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-v93q-wwv7-hm54](https://github.com/frappe/erpnext/security/advisories/GHSA-v93q-wwv7-hm54) | — | Unauthorised access to Project costing in the customer portal due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-29xj-69vf-fmmh](https://github.com/frappe/erpnext/security/advisories/GHSA-29xj-69vf-fmmh) | — | Unauthorised access to complete selling documents and RFQs in the customer and supplier portals due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-crxr-qmq5-mm3q](https://github.com/frappe/erpnext/security/advisories/GHSA-crxr-qmq5-mm3q) | — | Unauthorised access to Bank Transactions of other companies in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-xmw8-rg38-x88j](https://github.com/frappe/erpnext/security/advisories/GHSA-xmw8-rg38-x88j) | — | Unauthorised access to supplier portal records through a party identity mix-up due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-qr6v-w65q-v497](https://github.com/frappe/erpnext/security/advisories/GHSA-qr6v-w65q-v497) | — | Unauthorised access to Issues in the customer portal due to missing validation | < 16.52.0 | version-affected |
| erpnext | [GHSA-6xf4-gr7h-2h57](https://github.com/frappe/erpnext/security/advisories/GHSA-6xf4-gr7h-2h57) | — | Unauthorised access to stock value in Stock dashboards due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-7455-jhmp-j2h2](https://github.com/frappe/erpnext/security/advisories/GHSA-7455-jhmp-j2h2) | — | Unauthorised access to Activity Cost rates in the Projects module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-gqm4-wpw8-qrc9](https://github.com/frappe/erpnext/security/advisories/GHSA-gqm4-wpw8-qrc9) | — | Unauthorised access to Serial No and Batch ledgers in the Stock module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-26pv-59j4-p5m7](https://github.com/frappe/erpnext/security/advisories/GHSA-26pv-59j4-p5m7) | — | Unauthorised access to e-invoice files in the Regional module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-6g2x-j4rj-hr5c](https://github.com/frappe/erpnext/security/advisories/GHSA-6g2x-j4rj-hr5c) | — | Unauthorised access to stock balances of restricted warehouses in the Stock module due to missing validation | < 16.51.0 | version-affected |
| erpnext | [GHSA-5c7v-wfg4-j4g2](https://github.com/frappe/erpnext/security/advisories/GHSA-5c7v-wfg4-j4g2) | — | Unauthorised access to POS Profile cashiers in POS due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-x6mc-x6wm-h5jc](https://github.com/frappe/erpnext/security/advisories/GHSA-x6mc-x6wm-h5jc) | — | Unauthorised access to Taxes and Charges Templates in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-qxrv-9vhj-49xm](https://github.com/frappe/erpnext/security/advisories/GHSA-qxrv-9vhj-49xm) | — | Unauthorised access to loyalty point balances in the Selling module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-hf2q-xhq6-q394](https://github.com/frappe/erpnext/security/advisories/GHSA-hf2q-xhq6-q394) | — | Unauthorised access to payment allocations in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-w3rc-76j9-46jq](https://github.com/frappe/erpnext/security/advisories/GHSA-w3rc-76j9-46jq) | CVE-2026-124316 | Unauthorised access to Material Requests in the Buying module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-4h65-m5q4-xwc4](https://github.com/frappe/erpnext/security/advisories/GHSA-4h65-m5q4-xwc4) | — | Unauthorised access to the Chart of Accounts in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-m9wx-ccvr-729q](https://github.com/frappe/erpnext/security/advisories/GHSA-m9wx-ccvr-729q) | — | Unauthorised access to Bank Statement Import files in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-rcp6-4mfg-757h](https://github.com/frappe/erpnext/security/advisories/GHSA-rcp6-4mfg-757h) | — | Unauthorised access to taxes and charges of transactions in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-p7rx-846g-j6hr](https://github.com/frappe/erpnext/security/advisories/GHSA-p7rx-846g-j6hr) | — | Unauthorised access to Payment Terms Templates in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-58wx-2f38-8f44](https://github.com/frappe/erpnext/security/advisories/GHSA-58wx-2f38-8f44) | — | Unauthorised access to Payment Term settings in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-q6rj-xw5g-c4j7](https://github.com/frappe/erpnext/security/advisories/GHSA-q6rj-xw5g-c4j7) | — | Unauthorised access to Loyalty Program terms in the Selling module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-xw35-vc29-fjxw](https://github.com/frappe/erpnext/security/advisories/GHSA-xw35-vc29-fjxw) | — | Unauthorised access to POS Opening Entries in POS due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-x7vm-cw74-82wv](https://github.com/frappe/erpnext/security/advisories/GHSA-x7vm-cw74-82wv) | — | Unauthorised access to warehouse-wise stock quantities in the Stock module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-3xh3-23fp-77m7](https://github.com/frappe/erpnext/security/advisories/GHSA-3xh3-23fp-77m7) | — | Unauthorised access to actual stock quantities in the Stock module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-wvgx-whr3-44vr](https://github.com/frappe/erpnext/security/advisories/GHSA-wvgx-whr3-44vr) | — | Unauthorised access to valuation rates in the Stock module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-3f93-crcf-9p9j](https://github.com/frappe/erpnext/security/advisories/GHSA-3f93-crcf-9p9j) | — | Unauthorised access to Sales Order and Purchase Order values in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-45w5-68c8-75vp](https://github.com/frappe/erpnext/security/advisories/GHSA-45w5-68c8-75vp) | — | Unauthorised access to purchase cost data in the Assets module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-w587-ghqf-6jpp](https://github.com/frappe/erpnext/security/advisories/GHSA-w587-ghqf-6jpp) | — | Unauthorised access to BOM costs in the Manufacturing module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-h7xr-2wpr-7444](https://github.com/frappe/erpnext/security/advisories/GHSA-h7xr-2wpr-7444) | — | Unauthorised access to Item master data in the Stock module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-5q53-5vm3-cjq8](https://github.com/frappe/erpnext/security/advisories/GHSA-5q53-5vm3-cjq8) | — | Unauthorised access to Communications in the CRM and Support modules due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-g966-fmq7-gp99](https://github.com/frappe/erpnext/security/advisories/GHSA-g966-fmq7-gp99) | — | Unauthorised access to private files in the Accounts module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-2f98-mq8r-pvrh](https://github.com/frappe/erpnext/security/advisories/GHSA-2f98-mq8r-pvrh) | — | Possibility of SQL injection due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-f3vx-j6r6-67c7](https://github.com/frappe/erpnext/security/advisories/GHSA-f3vx-j6r6-67c7) | — | Unauthorised creation of Serial No and Batch records and file access in the Stock module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-w264-5p9f-hfwm](https://github.com/frappe/erpnext/security/advisories/GHSA-w264-5p9f-hfwm) | CVE-2026-124314 | Unauthorised access to open activities in the CRM module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-m668-9q43-8g29](https://github.com/frappe/erpnext/security/advisories/GHSA-m668-9q43-8g29) | — | Unauthorised access and modification of data due to missing validation | < 16.53.0 | version-affected |
| erpnext | [GHSA-gjr3-hvp7-6pgm](https://github.com/frappe/erpnext/security/advisories/GHSA-gjr3-hvp7-6pgm) | — | Unauthorised cancellation of Stock Reservation Entries in the Manufacturing module due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-g7r2-v98g-6wcr](https://github.com/frappe/erpnext/security/advisories/GHSA-g7r2-v98g-6wcr) | — | Unauthorised access to sensitive data due to missing validation | < 16.35.0 | version-affected |
| erpnext | [GHSA-x267-fgf5-54q9](https://github.com/frappe/erpnext/security/advisories/GHSA-x267-fgf5-54q9) | — | Unauthorised modification of clearance dates in the Accounts module due to missing validation | < 16.50.0 | version-affected |
| erpnext | [GHSA-f6fx-777q-q9jp](https://github.com/frappe/erpnext/security/advisories/GHSA-f6fx-777q-q9jp) | — | Unauthorised access to child table rows of transactions due to missing validation | < 16.36.0 | version-affected |
| erpnext | [GHSA-734c-hv9r-mg2c](https://github.com/frappe/erpnext/security/advisories/GHSA-734c-hv9r-mg2c) | — | Stored cross-site scripting due to missing validation | < 16.23.0 | not-affected |
| erpnext | [GHSA-v38v-9h2p-hr8v](https://github.com/frappe/erpnext/security/advisories/GHSA-v38v-9h2p-hr8v) | — | Possibility of SQL injection due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-9vph-hqmm-g7hq](https://github.com/frappe/erpnext/security/advisories/GHSA-9vph-hqmm-g7hq) | — | Unauthorised access to data due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-xp5c-86f4-7ppf](https://github.com/frappe/erpnext/security/advisories/GHSA-xp5c-86f4-7ppf) | — | Possibility of SQL injection due to missing validation | < 16.32.0 | not-affected |
| erpnext | [GHSA-pg3r-7236-pg74](https://github.com/frappe/erpnext/security/advisories/GHSA-pg3r-7236-pg74) | — | Unauthorised Document modification due to missing validation | < 16.32.0 | not-affected |
| erpnext | [GHSA-p4jx-mqwq-66cj](https://github.com/frappe/erpnext/security/advisories/GHSA-p4jx-mqwq-66cj) | — | Unauthorised modification of data due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-f99r-gp2w-xghj](https://github.com/frappe/erpnext/security/advisories/GHSA-f99r-gp2w-xghj) | — | Stored cross-site scripting due to missing validation | < 16.33.0 | not-affected |
| erpnext | [GHSA-wp9w-rxmg-6pfj](https://github.com/frappe/erpnext/security/advisories/GHSA-wp9w-rxmg-6pfj) | — | Unauthorised status modification due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-qcff-6669-j3gj](https://github.com/frappe/erpnext/security/advisories/GHSA-qcff-6669-j3gj) | — | Unauthorised access to financial data due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-vg6r-89q7-wh34](https://github.com/frappe/erpnext/security/advisories/GHSA-vg6r-89q7-wh34) | — | Unauthorised record creation due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-cgjf-xw8x-qjjc](https://github.com/frappe/erpnext/security/advisories/GHSA-cgjf-xw8x-qjjc) | — | Unauthorised modification of data due to missing validation | < 16.35.0 | version-affected |
| erpnext | [GHSA-vr45-2p9x-3vjc](https://github.com/frappe/erpnext/security/advisories/GHSA-vr45-2p9x-3vjc) | — | Unauthorised record creation due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-wwgm-3pv3-gmqh](https://github.com/frappe/erpnext/security/advisories/GHSA-wwgm-3pv3-gmqh) | — | Unauthorised access to party records due to missing validation | < 16.23.0 | not-affected |
| erpnext | [GHSA-2r76-j6jj-jj56](https://github.com/frappe/erpnext/security/advisories/GHSA-2r76-j6jj-jj56) | — | Unauthorised Document modification due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-49wp-r82c-j825](https://github.com/frappe/erpnext/security/advisories/GHSA-49wp-r82c-j825) | — | Unauthorised Document modification due to missing validation | < 16.34.2 | version-affected |
| erpnext | [GHSA-cgxw-2996-9vj3](https://github.com/frappe/erpnext/security/advisories/GHSA-cgxw-2996-9vj3) | — | Unauthorised access to personal data due to missing validation | < 16.33.0 | not-affected |
| erpnext | [GHSA-726x-68g4-fj9v](https://github.com/frappe/erpnext/security/advisories/GHSA-726x-68g4-fj9v) | — | Unauthorised access to financial data due to missing validation | < 16.35.0 | version-affected |
| erpnext | [GHSA-794x-fhm7-58j7](https://github.com/frappe/erpnext/security/advisories/GHSA-794x-fhm7-58j7) | — | Unauthorised invocation of internal methods due to missing validation | < 16.34.1 | version-affected |
| erpnext | [GHSA-mp29-fjc5-h86p](https://github.com/frappe/erpnext/security/advisories/GHSA-mp29-fjc5-h86p) | — | Possibility of SQL injection due to missing validation | < 16.34.2 | version-affected |
| erpnext | [GHSA-q6qw-66cm-f9wj](https://github.com/frappe/erpnext/security/advisories/GHSA-q6qw-66cm-f9wj) | — | Unauthorised access to financial data due to missing validation | < 16.33.0 | not-affected |
| erpnext | [GHSA-5wpj-6rvp-9ff7](https://github.com/frappe/erpnext/security/advisories/GHSA-5wpj-6rvp-9ff7) | CVE-2026-108374 | Unauthorised status modification due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-7j2w-hg27-8g3q](https://github.com/frappe/erpnext/security/advisories/GHSA-7j2w-hg27-8g3q) | — | Unauthorised sending of transactional email due to missing validation | < 16.35.0 | version-affected |
| erpnext | [GHSA-pr7v-95jp-gwwv](https://github.com/frappe/erpnext/security/advisories/GHSA-pr7v-95jp-gwwv) | — | Unauthorised access to data due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-jp5q-723q-g826](https://github.com/frappe/erpnext/security/advisories/GHSA-jp5q-723q-g826) | — | Possibility of SQL injection due to missing validation | < 16.32.0 | not-affected |
| erpnext | [GHSA-jfwr-g9v2-57c9](https://github.com/frappe/erpnext/security/advisories/GHSA-jfwr-g9v2-57c9) | — | Unauthorised access to data due to missing validation | < 16.33.0 | not-affected |
| erpnext | [GHSA-rv4r-c8v3-3hrc](https://github.com/frappe/erpnext/security/advisories/GHSA-rv4r-c8v3-3hrc) | — | Account takeover via stored cross-site scripting | < 16.32.0 | not-affected |
| erpnext | [GHSA-h787-3x6w-8x4m](https://github.com/frappe/erpnext/security/advisories/GHSA-h787-3x6w-8x4m) | — | Possibility of SQL injection due to missing validation | < 16.34.0 | not-affected |
| erpnext | [GHSA-562g-3qrh-3w2f](https://github.com/frappe/erpnext/security/advisories/GHSA-562g-3qrh-3w2f) | — | Unauthorised record creation due to missing validation | < 16.15.0 | not-affected |
| erpnext | [GHSA-g72f-g9wf-42vr](https://github.com/frappe/erpnext/security/advisories/GHSA-g72f-g9wf-42vr) | — | Unauthorised access to financial data due to missing validation | < 16.26.0 | not-affected |
| erpnext | [GHSA-fwgg-5fp9-rg78](https://github.com/frappe/erpnext/security/advisories/GHSA-fwgg-5fp9-rg78) | — | Unauthorised modification of master data due to missing validation | < 16.14.0 | not-affected |
| erpnext | [GHSA-73jx-q3gp-r24f](https://github.com/frappe/erpnext/security/advisories/GHSA-73jx-q3gp-r24f) | — | Possibility of SQL injection due to missing validation | < 16.21.0 | not-affected |
| erpnext | [GHSA-rqv5-h4rv-w57m](https://github.com/frappe/erpnext/security/advisories/GHSA-rqv5-h4rv-w57m) | — | Possibility of SQL injection due to missing validation | < 16.8.0 | not-affected |
| erpnext | [GHSA-c496-q7g2-62vv](https://github.com/frappe/erpnext/security/advisories/GHSA-c496-q7g2-62vv) | — | Unauthorised modification of records due to missing validation | < 16.22.0 | not-affected |

## Python dependency scan

Installed pip-audit into an isolated temporary virtual environment; audited extracted pinned freeze with `pip-audit -r requirements.txt --disable-pip --no-deps -f json`. Editable Frappe/ERPNext and VCS-pinned gunicorn/PyPika were excluded because they are not index pins; they were not audited by this run. The current PyPI advisory feed returned **117 raw findings across 13 packages**, including duplicate IDs/aliases. These are scanner version matches, not verified reachable code paths; the scanner does not provide a reliable publication-date cutoff, so publication by 2026-11-12 has not been independently established for each. No JS SCA or OS package scan was run. Each advisory below links to its record; fix `none` means no fix listed, not necessarily no fix exists. Static paths/preconditions for these matches remain unverified; `apps/frappe/frappe/utils/pdf.py` imports pdfkit.

| Package | Version | Advisory (scanner ID) | Fix versions |
|---|---|---|---|
| brotli | 1.2.0 | [PYSEC-2026-4322](https://osv.dev/vulnerability/PYSEC-2026-4322) | 1.2.1 |
| brotli | 1.2.0 | [PYSEC-2026-4322](https://osv.dev/vulnerability/PYSEC-2026-4322) | 1.2.1 |
| certifi | 2026.7.22 | [PYSEC-2026-4320](https://osv.dev/vulnerability/PYSEC-2026-4320) | 2026.10.18 |
| certifi | 2026.7.22 | [PYSEC-2026-4320](https://osv.dev/vulnerability/PYSEC-2026-4320) | 2026.10.18 |
| filelock | 3.20.4 | [CVE-2026-112940](https://nvd.nist.gov/vuln/detail/CVE-2026-112940) | 4.2.1 |
| filelock | 3.20.4 | [CVE-2026-112913](https://nvd.nist.gov/vuln/detail/CVE-2026-112913) | 4.2.1 |
| filelock | 3.20.4 | [CVE-2026-112936](https://nvd.nist.gov/vuln/detail/CVE-2026-112936) | 4.0.9 |
| filelock | 3.20.4 | [CVE-2026-112910](https://nvd.nist.gov/vuln/detail/CVE-2026-112910) | 4.2.1 |
| filelock | 3.20.4 | [CVE-2026-112909](https://nvd.nist.gov/vuln/detail/CVE-2026-112909) | 4.2.1 |
| filelock | 3.20.4 | [CVE-2026-112915](https://nvd.nist.gov/vuln/detail/CVE-2026-112915) | 4.2.1 |
| gitpython | 3.1.61 | [CVE-2026-114145](https://nvd.nist.gov/vuln/detail/CVE-2026-114145) | 3.2.1 |
| gitpython | 3.1.61 | [CVE-2026-110859](https://nvd.nist.gov/vuln/detail/CVE-2026-110859) | 3.2.0 |
| gitpython | 3.1.61 | [CVE-2026-110858](https://nvd.nist.gov/vuln/detail/CVE-2026-110858) | 3.2.0 |
| gitpython | 3.1.61 | [CVE-2026-110856](https://nvd.nist.gov/vuln/detail/CVE-2026-110856) | 3.2.0 |
| gitpython | 3.1.61 | [CVE-2026-110857](https://nvd.nist.gov/vuln/detail/CVE-2026-110857) | 3.2.0 |
| gitpython | 3.1.61 | [CVE-2026-110855](https://nvd.nist.gov/vuln/detail/CVE-2026-110855) | 3.2.0 |
| oauthlib | 3.3.1 | [PYSEC-2026-4114](https://osv.dev/vulnerability/PYSEC-2026-4114) | 4.0.0 |
| oauthlib | 3.3.1 | [PYSEC-2026-4114](https://osv.dev/vulnerability/PYSEC-2026-4114) | 4.0.0 |
| oauthlib | 3.3.1 | [CVE-2026-49272](https://nvd.nist.gov/vuln/detail/CVE-2026-49272) | 4.0.1 |
| pdfkit | 1.0.0 | [PYSEC-2026-2860](https://osv.dev/vulnerability/PYSEC-2026-2860) | none listed |
| pdfkit | 1.0.0 | [PYSEC-2026-2860](https://osv.dev/vulnerability/PYSEC-2026-2860) | none listed |
| pillow | 12.3.0 | [PYSEC-2026-4327](https://osv.dev/vulnerability/PYSEC-2026-4327) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4328](https://osv.dev/vulnerability/PYSEC-2026-4328) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4326](https://osv.dev/vulnerability/PYSEC-2026-4326) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4339](https://osv.dev/vulnerability/PYSEC-2026-4339) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4340](https://osv.dev/vulnerability/PYSEC-2026-4340) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4343](https://osv.dev/vulnerability/PYSEC-2026-4343) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4334](https://osv.dev/vulnerability/PYSEC-2026-4334) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4337](https://osv.dev/vulnerability/PYSEC-2026-4337) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4341](https://osv.dev/vulnerability/PYSEC-2026-4341) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4330](https://osv.dev/vulnerability/PYSEC-2026-4330) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4338](https://osv.dev/vulnerability/PYSEC-2026-4338) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4335](https://osv.dev/vulnerability/PYSEC-2026-4335) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4336](https://osv.dev/vulnerability/PYSEC-2026-4336) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4331](https://osv.dev/vulnerability/PYSEC-2026-4331) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4332](https://osv.dev/vulnerability/PYSEC-2026-4332) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4329](https://osv.dev/vulnerability/PYSEC-2026-4329) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4333](https://osv.dev/vulnerability/PYSEC-2026-4333) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4342](https://osv.dev/vulnerability/PYSEC-2026-4342) | 13.0.0 |
| pillow | 12.3.0 | [PYSEC-2026-4363](https://osv.dev/vulnerability/PYSEC-2026-4363) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112895](https://nvd.nist.gov/vuln/detail/CVE-2026-112895) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112400](https://nvd.nist.gov/vuln/detail/CVE-2026-112400) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112897](https://nvd.nist.gov/vuln/detail/CVE-2026-112897) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112395](https://nvd.nist.gov/vuln/detail/CVE-2026-112395) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112404](https://nvd.nist.gov/vuln/detail/CVE-2026-112404) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112899](https://nvd.nist.gov/vuln/detail/CVE-2026-112899) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112900](https://nvd.nist.gov/vuln/detail/CVE-2026-112900) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112893](https://nvd.nist.gov/vuln/detail/CVE-2026-112893) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112891](https://nvd.nist.gov/vuln/detail/CVE-2026-112891) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112390](https://nvd.nist.gov/vuln/detail/CVE-2026-112390) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112401](https://nvd.nist.gov/vuln/detail/CVE-2026-112401) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112391](https://nvd.nist.gov/vuln/detail/CVE-2026-112391) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112894](https://nvd.nist.gov/vuln/detail/CVE-2026-112894) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112406](https://nvd.nist.gov/vuln/detail/CVE-2026-112406) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112399](https://nvd.nist.gov/vuln/detail/CVE-2026-112399) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112892](https://nvd.nist.gov/vuln/detail/CVE-2026-112892) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-112393](https://nvd.nist.gov/vuln/detail/CVE-2026-112393) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-96638](https://nvd.nist.gov/vuln/detail/CVE-2026-96638) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-96640](https://nvd.nist.gov/vuln/detail/CVE-2026-96640) | 13.0.0 |
| pillow | 12.3.0 | [CVE-2026-96778](https://nvd.nist.gov/vuln/detail/CVE-2026-96778) | 13.0.0 |
| pillow | 12.3.0 | [GHSA-78g4-xqwv-q3g8](https://osv.dev/vulnerability/GHSA-78g4-xqwv-q3g8) | 13.0.0 |
| pyasn1 | 0.6.4 | [CVE-2026-119196](https://nvd.nist.gov/vuln/detail/CVE-2026-119196) | 0.6.5 |
| pyasn1 | 0.6.4 | [CVE-2026-119194](https://nvd.nist.gov/vuln/detail/CVE-2026-119194) | 0.6.5 |
| pyasn1 | 0.6.4 | [CVE-2026-119197](https://nvd.nist.gov/vuln/detail/CVE-2026-119197) | 0.6.5 |
| pyasn1 | 0.6.4 | [CVE-2026-119195](https://nvd.nist.gov/vuln/detail/CVE-2026-119195) | 0.6.5 |
| pyjwt | 2.13.0 | [PYSEC-2026-4145](https://osv.dev/vulnerability/PYSEC-2026-4145) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4146](https://osv.dev/vulnerability/PYSEC-2026-4146) | none listed |
| pyjwt | 2.13.0 | [PYSEC-2026-4149](https://osv.dev/vulnerability/PYSEC-2026-4149) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4152](https://osv.dev/vulnerability/PYSEC-2026-4152) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4144](https://osv.dev/vulnerability/PYSEC-2026-4144) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4143](https://osv.dev/vulnerability/PYSEC-2026-4143) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4148](https://osv.dev/vulnerability/PYSEC-2026-4148) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4140](https://osv.dev/vulnerability/PYSEC-2026-4140) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4141](https://osv.dev/vulnerability/PYSEC-2026-4141) | 2.15.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4147](https://osv.dev/vulnerability/PYSEC-2026-4147) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4151](https://osv.dev/vulnerability/PYSEC-2026-4151) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4150](https://osv.dev/vulnerability/PYSEC-2026-4150) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4142](https://osv.dev/vulnerability/PYSEC-2026-4142) | 2.14.0 |
| pyjwt | 2.13.0 | [PYSEC-2026-4183](https://osv.dev/vulnerability/PYSEC-2026-4183) | 2.15.0 |
| pyjwt | 2.13.0 | [GHSA-pxh4-856f-4h89](https://osv.dev/vulnerability/GHSA-pxh4-856f-4h89) | 2.14.0 |
| pypdf | 6.15.0 | [PYSEC-2026-3910](https://osv.dev/vulnerability/PYSEC-2026-3910) | 6.16.1 |
| pypdf | 6.15.0 | [PYSEC-2026-3911](https://osv.dev/vulnerability/PYSEC-2026-3911) | 6.16.1 |
| pypdf | 6.15.0 | [PYSEC-2026-3913](https://osv.dev/vulnerability/PYSEC-2026-3913) | 6.16.0 |
| pypdf | 6.15.0 | [PYSEC-2026-4153](https://osv.dev/vulnerability/PYSEC-2026-4153) | 6.18.0 |
| pypdf | 6.15.0 | [PYSEC-2026-4154](https://osv.dev/vulnerability/PYSEC-2026-4154) | 6.18.1 |
| pypdf | 6.15.0 | [PYSEC-2026-4160](https://osv.dev/vulnerability/PYSEC-2026-4160) | 6.19.0 |
| pypdf | 6.15.0 | [PYSEC-2026-4159](https://osv.dev/vulnerability/PYSEC-2026-4159) | 6.19.0 |
| pypdf | 6.15.0 | [PYSEC-2026-4156](https://osv.dev/vulnerability/PYSEC-2026-4156) | 6.18.1 |
| pypdf | 6.15.0 | [PYSEC-2026-4155](https://osv.dev/vulnerability/PYSEC-2026-4155) | 6.18.1 |
| pypdf | 6.15.0 | [PYSEC-2026-4158](https://osv.dev/vulnerability/PYSEC-2026-4158) | 6.17.0 |
| pypdf | 6.15.0 | [PYSEC-2026-4157](https://osv.dev/vulnerability/PYSEC-2026-4157) | 6.19.0 |
| pypdf | 6.15.0 | [CVE-2026-113792](https://nvd.nist.gov/vuln/detail/CVE-2026-113792) | 6.20.1 |
| pypdf | 6.15.0 | [CVE-2026-113795](https://nvd.nist.gov/vuln/detail/CVE-2026-113795) | 6.20.0 |
| pypdf | 6.15.0 | [CVE-2026-113793](https://nvd.nist.gov/vuln/detail/CVE-2026-113793) | 6.20.1 |
| pypdf | 6.15.0 | [CVE-2026-113794](https://nvd.nist.gov/vuln/detail/CVE-2026-113794) | 6.20.0 |
| pypdf | 6.15.0 | [CVE-2026-113786](https://nvd.nist.gov/vuln/detail/CVE-2026-113786) | 6.21.1 |
| pypdf | 6.15.0 | [CVE-2026-113791](https://nvd.nist.gov/vuln/detail/CVE-2026-113791) | 6.21.0 |
| pypdf | 6.15.0 | [CVE-2026-113790](https://nvd.nist.gov/vuln/detail/CVE-2026-113790) | 6.21.0 |
| pypdf | 6.15.0 | [CVE-2026-113789](https://nvd.nist.gov/vuln/detail/CVE-2026-113789) | 6.21.0 |
| pypdf | 6.15.0 | [CVE-2026-115572](https://nvd.nist.gov/vuln/detail/CVE-2026-115572) | 6.21.2 |
| pypdf | 6.15.0 | [CVE-2026-115585](https://nvd.nist.gov/vuln/detail/CVE-2026-115585) | 6.21.2 |
| pypdf | 6.15.0 | [CVE-2026-115580](https://nvd.nist.gov/vuln/detail/CVE-2026-115580) | 6.21.2 |
| pypdf | 6.15.0 | [CVE-2026-119208](https://nvd.nist.gov/vuln/detail/CVE-2026-119208) | 6.21.3 |
| pypdf | 6.15.0 | [CVE-2026-119206](https://nvd.nist.gov/vuln/detail/CVE-2026-119206) | 6.21.3 |
| pypdf | 6.15.0 | [CVE-2026-119209](https://nvd.nist.gov/vuln/detail/CVE-2026-119209) | 6.21.3 |
| pypdf | 6.15.0 | [CVE-2026-119207](https://nvd.nist.gov/vuln/detail/CVE-2026-119207) | 6.21.3 |
| pypdf | 6.15.0 | [CVE-2026-119203](https://nvd.nist.gov/vuln/detail/CVE-2026-119203) | 6.21.4 |
| pypdf | 6.15.0 | [CVE-2026-119205](https://nvd.nist.gov/vuln/detail/CVE-2026-119205) | 6.21.4 |
| pypdf | 6.15.0 | [CVE-2026-119204](https://nvd.nist.gov/vuln/detail/CVE-2026-119204) | 6.21.4 |
| urllib3 | 2.7.0 | [PYSEC-2026-4177](https://osv.dev/vulnerability/PYSEC-2026-4177) | 2.8.0 |
| urllib3 | 2.7.0 | [PYSEC-2026-4176](https://osv.dev/vulnerability/PYSEC-2026-4176) | 2.8.0 |
| urllib3 | 2.7.0 | [PYSEC-2026-4175](https://osv.dev/vulnerability/PYSEC-2026-4175) | 2.8.0 |
| weasyprint | 68.0 | [PYSEC-2026-3412](https://osv.dev/vulnerability/PYSEC-2026-3412) | none listed |
| weasyprint | 68.0 | [PYSEC-2026-3412](https://osv.dev/vulnerability/PYSEC-2026-3412) | none listed |
| weasyprint | 68.0 | [PYSEC-2026-3940](https://osv.dev/vulnerability/PYSEC-2026-3940) | 70.0 |
| weasyprint | 68.0 | [PYSEC-2026-4311](https://osv.dev/vulnerability/PYSEC-2026-4311) | 70.0 |
| werkzeug | 3.1.6 | [PYSEC-2026-4312](https://osv.dev/vulnerability/PYSEC-2026-4312) | 3.1.9 |

## Limitations and handoff

GitHub ERPNext advisory pagination repeatedly returned the same first 100 records even when requesting subsequent pages, so inventory is **not exhaustive**. Frappe returned 97. OSV/NVD/Huntr were not independently exhaustively queried, and source-level code-path, auth and configuration checks are incomplete for most records. Scanner results and broad range labels should not be promoted to verified findings. Resolve missing advisories with correctly paginated sources, verify affected commits and file paths, inspect bundled JS dependencies, then test with a disposable site and positive/negative controls. This document contains no runtime tests.
