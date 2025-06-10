// Copyright (c) 2025, Umer and contributors

frappe.ui.form.on("Student Result", {
  assessment: function (frm) {
    frm.doc.results = [];

    if (frm.doc.assessment) {
      frappe.db.get_doc("Assessment", frm.doc.assessment).then((doc) => {
        frappe.db.get_list('Course Enrollment', {
          filters: {
            'section': doc.section,
            'course': doc.subject,
            'status': 'Enrolled'
          },
          fields: ["*"],
          order_by: "student"
        }).then(students => {
          students.forEach(student => {
            doc.no_clo.forEach(row => {
              let d = frm.add_child("results");
              d.student = student.student;
              d.student_name = student.student_name;
              d.clo = row.clo;
              d.attainment_level = row.attainment_level;
            });
          });
          frm.refresh_field("results");
        });
      });
    }
  },
});

frappe.ui.form.on("Result", {
  obtain_marks(frm, cdt, cdn) {
    const row = locals[cdt][cdn];
    if (parseFloat(row.obtain_marks) >= parseFloat(row.attainment_level)) {
      row.status = "<span style='color:green'>CLO Achieved</span>";
      row.is_achieved = 1;
    } else {
      row.status = "<span style='color:red'>CLO Not Achieved</span>";
      row.is_achieved = 0;
    }

    frm.refresh_field("results");
  },
});
