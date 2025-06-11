// Copyright (c) 2025, Umer and contributors
// For license information, please see license.txt

frappe.query_reports["Students Assessment"] = {
  filters: [
    {
      fieldname: "roll_number",
      label: "Student",
      fieldtype: "Link",
      options: "Student",
    },
    {
      fieldname: "assessment",
      label: "Assessment",
      fieldtype: "Link",
      options: "Assessment",
    },
    {
      fieldname: "subject",
      label: "Subject",
      fieldtype: "Link",
      options: "Subject",
    },
    {
      fieldname: "section",
      label: "Section",
      fieldtype: "Link",
      options: "Section",
    },
    {
      fieldname: "clo",
      label: "CLO",
      fieldtype: "Link",
      options: "CLO",
    },
  ],
};
