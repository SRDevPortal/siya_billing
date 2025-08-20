app_name = "siya_billing"
app_title = "Siya Billing"
app_publisher = "SR Developer"
app_description = "Auto create Patient/Customer/Address/Contact, Sales Invoice & Payment"
app_email = "webdevelopersriaas@gmail.com"
app_license = "MIT"

# If you want to require ERPNext for install:
# required_apps = ["erpnext"]

# Public API + Doc Events (adjust to your api.py functions)
doc_events = {
    "Sales Invoice": {
        "on_submit": "siya_billing.api.create_payment_entry_on_invoice_submit"
    },
    "Patient": {
        "after_insert": "siya_billing.api.ensure_customer_links_for_patient"
    }
}
