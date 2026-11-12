import frappe
from frappe.utils import today, add_days, getdate
from frappe.desk.page.setup_wizard.setup_wizard import setup_complete

if not frappe.is_setup_complete():
    year = getdate().year
    result = setup_complete(dict(language='English', country='United States', timezone='America/Chicago', currency='USD', company_name='E Corp', company_abbr='EC', fy_start_date=f'{year}-01-01', fy_end_date=f'{year}-12-31', chart_of_accounts='Standard', full_name='Administrator'))
    if result.get('status') != 'ok':
        raise RuntimeError(f'Setup failed: {result}')


def add(doctype, name, **fields):
    if frappe.db.exists(doctype, name):
        return frappe.get_doc(doctype, name)
    return frappe.get_doc(dict(doctype=doctype, **fields)).insert(ignore_permissions=True)

for name in ('Northstar Workshop', 'Bluebird Outfitters'):
    add('Customer', name, customer_name=name, customer_type='Company', customer_group='Commercial', territory='All Territories')
for name in ('Cedar Components', 'Maple Wholesale'):
    add('Supplier', name, supplier_name=name, supplier_group='All Supplier Groups', supplier_type='Company')
for code in ('DEMO-SERVICE', 'DEMO-SUPPLY'):
    add('Item', code, item_code=code, item_name=code, item_group='Products', stock_uom='Nos', is_stock_item=0)
for email, first, role, kind in (
    ('sales@example.invalid', 'Sales', 'Sales User', 'System User'),
    ('accounts@example.invalid', 'Accounts', 'Accounts User', 'System User'),
    ('viewer@example.invalid', 'Viewer', 'Auditor', 'System User'),
    ('portal@example.invalid', 'Portal', 'Customer', 'Website User'),
):
    add('User', email, email=email, first_name=first, user_type=kind, send_welcome_email=0, new_password='assessment-demo', roles=[{'role': role}])
customer = frappe.get_doc('Customer', 'Northstar Workshop')
if not any(row.user == 'portal@example.invalid' for row in customer.portal_users):
    customer.append('portal_users', {'user': 'portal@example.invalid'})
    customer.save(ignore_permissions=True)
if not frappe.db.exists('Contact', {'email_id': 'portal@example.invalid'}):
    frappe.get_doc(dict(doctype='Contact', first_name='Portal', last_name='Contact', email_ids=[dict(email_id='portal@example.invalid', is_primary=1)], links=[dict(link_doctype='Customer', link_name='Northstar Workshop')], user='portal@example.invalid')).insert(ignore_permissions=True)

for index, customer in enumerate(('Northstar Workshop', 'Bluebird Outfitters'), 1):
    for doctype in ('Sales Order', 'Sales Invoice'):
        marker = f'Fictional {doctype} {index}'
        if not frappe.db.exists(doctype, {'customer': customer, 'docstatus': 1}):
            fields = dict(doctype=doctype, customer=customer, company='E Corp', transaction_date=today(), posting_date=today(), delivery_date=add_days(today(), 7), remarks=marker, items=[dict(item_code='DEMO-SERVICE', qty=1, rate=100 * index, delivery_date=add_days(today(), 7))])
            doc = frappe.get_doc(fields).insert(ignore_permissions=True)
            doc.submit()
for index, supplier in enumerate(('Cedar Components', 'Maple Wholesale'), 1):
    marker = f'Fictional Purchase Order {index}'
    if not frappe.db.exists('Purchase Order', {'supplier': supplier, 'docstatus': 1}):
        doc = frappe.get_doc(dict(doctype='Purchase Order', supplier=supplier, company='E Corp', transaction_date=today(), schedule_date=add_days(today(), 7), remarks=marker, items=[dict(item_code='DEMO-SUPPLY', qty=2, rate=25, schedule_date=add_days(today(), 7))])).insert(ignore_permissions=True)
        doc.submit()
for index, customer in enumerate(('Northstar Workshop', 'Bluebird Outfitters'), 1):
    filename = f'fictional-note-{index}.txt'
    if not frappe.db.exists('File', {'file_name': filename, 'attached_to_doctype': 'Customer', 'attached_to_name': customer}):
        frappe.get_doc(dict(doctype='File', file_name=filename, content=f'Fictional customer note {index}.', is_private=1, attached_to_doctype='Customer', attached_to_name=customer)).insert(ignore_permissions=True)
frappe.db.commit()
