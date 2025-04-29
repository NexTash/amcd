frappe.listview_settings['Student Result Log'] = {
	get_indicator: function(doc) {
		var status_color = {
			"CLO Not Achieved": "red",
			"CLO Achieved": "green"
		};
		return [__(doc.clo_status), status_color[doc.clo_status], "status,=,"+doc.clo_status];
	},
};
