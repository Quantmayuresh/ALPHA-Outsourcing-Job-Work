// Copyright (c) 2024, Quantbit Technologies Pvt ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Challan Wise Subcontracting Analysis"] = {
	"filters": [
		{"fieldname": "company","fieldtype": "Link","label": "Company","options": "Company","reqd": 1},
        {"fieldname": "from_date","fieldtype": "Date","label": "From Date","reqd": 1},
        {"fieldname": "to_date","fieldtype": "Date","label": "To Date","reqd": 1},
		{"fieldname": "name", "fieldtype": "Data", "label": "IN/OUT Challan"},
        // {"fieldname": "subcontracting", "fieldtype": "Data", "label": "IN Challan"},
		{"fieldname": "include_weight","fieldtype": "Check","label": "Include Weight",},
	]
};
