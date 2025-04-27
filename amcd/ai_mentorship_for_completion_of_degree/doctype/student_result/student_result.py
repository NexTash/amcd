# Copyright (c) 2025, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentResult(Document):
    def on_submit(self):
        for row in self.results:
            student_log = frappe.get_doc({
                'doctype': 'Student Result Log',
                'student': self.student, 
                'student_id':self.student_roll_no,
                'assessment_type': self.assessment_type,
                'clo': row.clo,
                'assessment_marks': row.assessment_marks,
                'subject': row.subject,
                'obtain_marks': row.obtain_marks,
                'status': row.status or "pass",
                'session': row.session
                
            })            
            student_log.insert()
