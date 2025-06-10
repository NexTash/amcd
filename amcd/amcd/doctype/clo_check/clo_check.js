frappe.ui.form.on("CLO Check", {
  refresh(frm) {
    frm.add_custom_button(__("Download CLO File"), function () {
      frm.call("download_clo_file").then((r) => {
        if (r.message) {
          const file_url = r.message.file_url;
          window.location.href = file_url;
        }
      });
    });
  },
});
