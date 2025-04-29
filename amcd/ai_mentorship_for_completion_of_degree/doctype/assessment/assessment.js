// Copyright (c) 2025, Umer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Assessment", {
	refresh(frm) {
        if(frm.doc.assesment_result.length > 0){
        frm.add_custom_button(__("Download Record"), function () {
          frm.call("download_assessment_results").then((r) => {
            if (r.message) {
              const file_url = r.message.file_url;
              window.location.href = file_url;
            }
          });
        });
        }
        if(frm.doc.attach_file){
        frm.add_custom_button(__("Upload Record"), function () {
            frm.call("upload_assessment_results").then((r) => {
              if (r.message) {
                frappe.show_alert({
                  message: __("File uploaded successfully"),
                  indicator: "green",
                });
              }
            });
          });
        }
      },
});
