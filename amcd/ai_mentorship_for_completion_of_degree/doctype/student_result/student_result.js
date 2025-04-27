// Copyright (c) 2025, Nextash and contributors
frappe.ui.form.on("Student Result", {
        assessment: function(frm) {
            if (frm.doc.assessment) {
                frappe.db.get_doc('Assessment', frm.doc.assessment)
                    .then(doc => {
                        frm.clear_table('results');
                        (doc.no_clo || []).forEach(row => {
                            let d = frm.add_child('results');
                            d.clo = row.clo;
                            d.assessment_marks = row.assessment_marks;
                            d.subject = doc.subject;
                            d.session = doc.sesssion;
                            d.assessment_type = doc.assessment_type;
                        });
                        frm.refresh_field('results');
                    });
            }
        }
    
});

frappe.ui.form.on('Result', {
    obtain_marks(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (row.obtain_marks < row.assessment_marks) {
            row.status = 'Fail';
        } else {
            row.status = 'Pass';
        }
        row.passfail = (row.status === 'Pass') ? 1 : 0;
        frm.refresh_field('results');
    },
    on_submit(frm) {
        frm.doc.results.forEach((row) => {
            if (row.status === 'Pass') {
                row.passfail = 1;}
             else {
                row.passfail = 0;
            }
        });
        frm.refresh_field('results');
        // frappe.msgprint('Passfail checkboxes have been updated on submission');
    }
});
