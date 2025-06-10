import frappe

def validate(doc, method):
    if frappe.flags.in_setup_wizard:
        return
    
    amcd_settings = frappe.get_single("AMCD Settings")
    organization_domain = amcd_settings.get("organization_domain")
    
    if not organization_domain:
        frappe.throw("Organization domain is not set in AMCD Settings")
    
    if not doc.email:
        frappe.throw("Email is required")

    if "@" in doc.email:
        email_domain = doc.email.split("@")[1]
        if email_domain != organization_domain:
            frappe.throw(f"Email domain must match the organization's domain: {organization_domain}")
    else:
        frappe.throw("Invalid email format")