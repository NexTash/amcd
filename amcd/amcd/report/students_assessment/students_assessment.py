# Copyright (c) 2025, Umer and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data, None

def get_columns():
    """Returns the columns for the report."""
    return [
        {"label": "Student", "fieldname": "student", "fieldtype": "Data", "width": 250},
        {"label": "Roll Number", "fieldname": "roll_number", "fieldtype": "Data", "width": 150},
        {"label": "Assessment", "fieldname": "roll_number", "fieldtype": "Data", "width": 150},
        {"label": "CLO", "fieldname": "clo", "fieldtype": "Data", "width": 150},
        {"label": "Attainment Level", "fieldname": "attainment_level", "fieldtype": "Data", "width": 200},
        {"label": "Obtain Marks", "fieldname": "obtain_marks", "fieldtype": "Data", "width": 150},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": "Assessment Type", "fieldname": "assessment_type", "fieldtype": "Data", "width": 200},
        {"label": "Subject", "fieldname": "subject", "fieldtype": "Data", "width": 200},
        {"label": "Section", "fieldname": "section", "fieldtype": "Data", "width": 150},
    ]

def get_data(filters):
    """Fetches the data based on applied filters."""
    filters_dict = {key: filters[key] for key in ['roll_number', 'subject', 'section', 'assessment', 'clo'] if filters.get(key)}
    
    # Fetch results from the 'Student Result Log' DocType
    result_data = frappe.get_list('Student Result Log', filters=filters_dict, fields=["*"])

    return [
        {
            "student": result.student,
            "roll_number": result.roll_number,
            "section": result.section,
            "subject": result.subject,
            "assessment": result.assessment,
            "assessment_type": result.assessment_type,
            "clo": result.clo,
            "attainment_level": result.attainment_level,
            "obtain_marks": result.obtain_marks,
            "status": f"<span class='text-success'>CLO Achieved</span>" if result.is_achieved else f"<span class='text-danger'>CLO Not Achieved</span>",
        }
        for result in result_data
    ]
