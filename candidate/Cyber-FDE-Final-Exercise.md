# Cyber Forward Deployed Engineer Final Exercise

Cyber | E Corp customer portal launch

**FORMAT**  
Take-home. About four hours of investigation and report writing, excluding setup. Then a 30-minute customer presentation, including discussion and questions. Plan to present for about 15 minutes.

**YOUR OUTPUT**  
A written report and presentation materials in any format. AI tools are allowed; say how you used them and how you checked their output. Be ready to defend every decision.

## The situation

E Corp is a fictional company that runs stock ERPNext for sales, invoicing and purchasing. It plans to open the customer portal to trade customers so they can view their own orders, invoices and documents. A launch date is set; it is a business target, not an agreed risk threshold. The technical lead and business owner have asked Eliza for an application security assessment to inform the launch decision.

## What the company needs

**Technical lead:** Evidence on whether the portal and internal roles keep users within their own data, which published advisories apply to this release, and prioritized fixes.

**Business owner:** A clear recommendation to launch, narrow the launch or delay; launch conditions; remaining risk; and who should accept it.

## Product and technical context

The target is the official ERPNext v16.34.0 image on Frappe v16.33.0, with no custom code. Synthetic data includes two customers, two suppliers, orders, invoices and private files attached to customer records. Disposable accounts include Administrator, Sales User, Accounts User, Auditor and one customer portal user linked to one customer.

Setup, credentials, boundaries and commands are in [README.md](README.md) in this package.

## Focus areas

Investigate only these three areas. Your report and presentation cover only them. The discovery notes are fictitious and unverified and may be wrong; confirming, bounding or disproving them is a valid result. If you notice something outside these areas, list it under next steps; do not investigate it.

1. **Portal data isolation.** Discovery note: a staff member said a portal user opened another customer's invoice from a link during an internal demo. Nobody reproduced it; the link and user are unknown. Contracts are also stored as private files on customer records. Question: can the portal user see or retrieve anything belonging to the other customer, including orders, invoices and private files?

2. **Internal role separation.** Discovery note: finance expects Auditor to be read-only and Sales users not to see accounting records. Default permissions have not been reviewed. Question: do the Sales User, Accounts User and Auditor accounts stay within those expectations?

3. **Advisory applicability.** Discovery note: a dependency scanner matched many published Frappe and ERPNext advisories by version. The team proposes an upgrade, but none is tested or scheduled. Question: for two or three published advisories that relate to areas 1 or 2, does this release actually have the issue? Work through version, fix presence, reachability and preconditions. A version match is not proof.

No one owns patching, permission review or security sign-off for launch. Use this as context for your recommendations; it is not an area to investigate.

## Delivery and solution context

You are the Cyber FDE, working hands-on against a disposable local copy. E Corp’s technical lead and business owner are your audience; E Corp engineering would implement fixes. E Corp accepts risk. You are not expected to find a certain number of issues or prove the application safe.

Test only the local target, its containers and source; keep it on localhost. No external targets, denial of service, real data, mail to real recipients, or uploads of target data or credentials to third parties. Use internet access for setup and research only. Stop and contact the coordinator if you cannot operate within these boundaries.

## Your task

**Plan:** Decide the order and depth across the three focus areas within four hours, and say why. Run one to three rounds, using what you learn to decide whether to continue. Stop at the time limit; report actions and lessons from each round.

**Investigate the focus areas:** For each focus area, conclude confirmed, bounded or disproved, with evidence and reproduction steps. Separate observations from hypotheses. Record failed tests and disproved concerns, confidence and assumptions.

**Impact and priority:** Explain impact and preconditions in E Corp’s terms and order your recommendations.

**Launch recommendation:** Recommend launch, a narrower launch or delay. State launch conditions, who accepts remaining risk and what evidence would change your view.

**Next steps:** Prioritize what you would test next and why; this may include areas outside the three focus areas. List tools and AI assistance used, their contributions and how you checked their output.

**Close with the decision you need:** State what you need from the technical lead and business owner.

## What we will assess

We assess work only within the three focus areas; depth and evidence in those areas count more than breadth. We assess reasoning, evidence, calibrated confidence, safe conduct within the boundaries, and clear communication to technical and nontechnical listeners. We do not assess the number of findings or acronyms. A well-supported negative or limited result is valid. Do not invent results or claim the assessment proves the application safe.
