// Copyright (c) 2024, Quantbit Technologies Pvt ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Test Report"] = {
    "filters": [
        {
            "fieldname": "company",
            "fieldtype": "Link",
            "label": "Company",
            "options": "Company"
        },
        {
            "fieldname": "from_date",
            "fieldtype": "Date",
            "label": "From Date"
        },
        {
            "fieldname": "to_date",
            "fieldtype": "Date",
            "label": "To Date"
        },
        {
            "fieldname": "in_or_out",
            "fieldtype": "Select",
            "label": "IN Or OUT",
            "options": ["OUT","IN"]
        },
        {
            "fieldname": "supplier_id",
            "fieldtype": "Link",
            "label": "Supplier Id",
            "options": "Supplier"
        },
        {
            "fieldname": "item",
            "fieldtype": "Link",
            "label": "Item Id",
            "options": "Item"
        },
        {
            "fieldname": "entry_type",
            "fieldtype": "Select",
            "label": "Entry Type",
            "options": ["Subcontracting", "Material Loan Given"]
        }

    ]
};