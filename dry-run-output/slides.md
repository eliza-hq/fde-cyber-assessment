# E Corp customer portal security
## Decision discussion — 15 minutes, plus 15 minutes questions

---
# Recommendation: delay launch

- Direct tests did not reproduce cross-customer order or invoice access.
- Relevant advisories match installed versions; fix presence and reachability remain uncertain.
- Sales can read account names; role expectations and ownership need decisions.
- Business owner accepts residual risk after technical evidence and conditions are met.

---
# What we tested

- One linked portal account, two synthetic customers, known order and invoice links, and two private files.
- Sales, Accounts and Auditor list permissions on selected records.
- Two advisories assessed using interviewer-only notes and installed source; this is not an independent candidate advisory exercise.
- Three short rounds; not an exhaustive security assessment.

---
# Portal isolation: bounded result

- Own order and invoice returned 200; other customer's equivalents returned 403.
- Both private file URLs returned 403 to portal user, including its own.
- Unknown original demo link and untested alternate paths prevent a universal conclusion.
- Exposure, if present, could disclose customer terms or invoices.

---
# Staff roles: clarify and constrain

- Sales invoice and GL lists denied; account list allowed.
- Accounts could list invoices and GL entries; Auditor could list GL entries.
- Auditor write permissions were not tested. Agree the access matrix, then validate it.

---
# Advisory uncertainty

- Frappe file-read advisory: version matches; candidate containment change not verified as advisory fix; direct file URLs denied in our tests.
- ERPNext SQL injection advisory: version matches; exact fix and vulnerable endpoint unknown.
- Neither a version match nor a denied direct URL proves exploitability or safety.

---
# Conditions for reconsidering launch

1. Name engineering and business owners; agree access expectations.
2. Verify fixes, upgrade supported components and run regression tests.
3. Re-test isolation, private files and staff read/write permissions.
4. Technical lead documents evidence; business owner accepts residual risk.

---
# Decisions and discussion

- Technical lead: who owns patching and permission review, and when can evidence be delivered?
- Business owner: does Sales need chart-of-accounts or private-contract access? What residual risk is acceptable?
- What evidence or operational constraint would change the launch date?
