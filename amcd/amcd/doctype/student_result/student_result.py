# Copyright (c) 2025, Umer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentResult(Document):
    def on_submit(self):
        for row in self.results:
            student_log = frappe.get_doc({
                'doctype': 'Student Result Log',
                'student_result': self.name,
                'roll_number': row.student,
                'student_result': self.name,
                'clo': row.clo,
                'attainment_level': row.attainment_level,
                'obtain_marks': row.obtain_marks,
                'is_achieved': row.is_achieved,
                'status': "CLO Achieved" if row.is_achieved else "CLO Not Achieved",
            })

            student_log.insert()
    
    def on_cancel(self):
        frappe.db.delete('Student Result Log', {'student_result': self.name})
    