frappe.listview_settings["Student Result Log"] = {
  get_indicator: function (doc) {
    if (doc.is_achieved) {
      return [__("CLO Achieved"), "green", "is_achieved,=,true"];
    } else {
      return [__("CLO Not Achieved"), "red", "is_achieved,=,false"];
    }
  },
};
