// Copyright (c) 2025, Nextash and contributors
// For license information, please see license.txt

frappe.query_reports["Students Assessment"] = {
    "filters": [
        {
            "fieldname": "student",
            "label": "Student",
            "fieldtype": "Link",
            "options": "Student"  
        },
        {
            "fieldname": "session",
            "label": "Session",
            "fieldtype": "Link",
            "options": "Session"
        },
        {
            "fieldname": "assessment_type",
            "label": "Assessment Type",
            "fieldtype": "Link",
            "options": "Assessment Type"
        },
        {
            "fieldname": "subject",
            "label": "Subject",
            "fieldtype": "Link",
            "options": "Subject"
        }
    ]
};
