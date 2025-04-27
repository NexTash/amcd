# Copyright (c) 2025, Nextash and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
    columns = get_columns(filters)
    data = get_data(filters)
    chart = get_chart(data)
    return columns, data, None, chart

def get_columns(filters):
    columns = [
        {
            "label": "Student",
            "fieldname": "student",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": "Student Id",
            "fieldname": "student_id",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Session",
            "fieldname": "session",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Assessment Marks",
            "fieldname": "assessment_marks",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "CLO",
            "fieldname": "clo",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Assessment Type",
            "fieldname": "assessment_type",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Subject",
            "fieldname": "subject",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Obtain Marks",
            "fieldname": "obtain_marks",
            "fieldtype": "Data",
            "width": 150
        }
    ]
    return columns

def get_data(filters):
    data = []
    result_filters = {}

    # Apply filters to the query if any
    if filters.get('student'):
        result_filters['student'] = filters.get('student')
    if filters.get('session'):
        result_filters['session'] = filters.get('session')
    if filters.get('subject'):
        result_filters['subject'] = filters.get('subject')
    if filters.get('assessment_type'):
        result_filters['assessment_type'] = filters.get('assessment_type')

    # Fetch data from the Student Result Log DocType
    result_data = frappe.get_list('Student Result Log', filters=result_filters, fields=["*"])

    for result in result_data:
        data.append({
            "student": result.student,
            "student_id": result.student_id,
            "session": result.session,
            "assessment_marks": result.assessment_marks,
            "clo": result.clo,
            "assessment_type": result.assessment_type,
            "subject": result.subject,
            "status": result.status,
            "obtain_marks": result.obtain_marks
        })

    return data

def get_chart(data):
    return {
        "data": {
            "labels": [d['subject'] for d in data],
            "datasets": [{
                "name": "Obtain Marks",
                "values": [d['obtain_marks'] for d in data]
            }]
        },
        "type": "bar",
        "title": "Obtain Marks per Subject",
        "height": 500,
        "animate": True,
        "axisOptions": {
            "xAxis": {
                "title": "Subjects",
                "gridLines": {
                    "display": True
                }
            },
            "yAxis": {
                "title": "Marks",
                "gridLines": {
                    "display": True
                },
                "scale": "linear"
            }
        }
    }
