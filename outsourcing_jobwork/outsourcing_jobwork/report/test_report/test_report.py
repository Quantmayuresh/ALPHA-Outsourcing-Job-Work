# Copyright (c) 2024, Quantbit Technologies Pvt ltd and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data = [], []
    columns = get_col()
    data = get_data(filters)
    if not data:
        frappe.msgprint("No data")
    return columns, data
 
def get_col():
    return [
        {
            "fieldname": "name",
            "fieldtype": "Link",
            "label": "Subcontracting",
            "options": "Subcontracting"
        },
        {
            "fieldname": "raw_item_code",
            "fieldtype": "Data",
            "label": "Raw Item Code"
        },
        {
            "fieldname": "raw_item_name",
            "fieldtype": "Data",
            "label": "Raw Item Name"
        },
        {
            "fieldname": "supplier_id",
            "fieldtype": "Link",
            "label": "Supplier Id",
            "options": "Supplier"
        },
        {
            "fieldname": "company",
            "fieldtype": "Link",
            "label": "Company",
            "options": "Company"
        },
        {
            "fieldname": "posting_date",
            "fieldtype": "Date",
            "label": "Posting Date"
        },
        {
            "fieldname": "source_warehouse",
            "fieldtype": "Link",
            "label": "Source Warehouse",
            "options": "Warehouse"
        },
        {
            "fieldname": "target_warehouse",
            "fieldtype": "Link",
            "label": "Target Warehouse",
            "options": "Warehouse"
        },
        {
            "fieldname": "production_quantity",
            "fieldtype": "Float",
            "label": " Production Quantity"
        },
        {
            "fieldname": "production_done_quantity",
            "fieldtype": "Float",
            "label": " Production Done Quantity"
        },
        {
            "fieldname": "production_remaining_quantity",
            "fieldtype": "Float",
            "label": " Production Remianing Quantity"
        }
    ]

def add_condition(condition_list, params_list, condition, param_value):
    if param_value:
        condition_list.append(condition)
        params_list.append(param_value)

def get_data(filters):
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    sup_id = filters.get("supplier_id")
    comp = filters.get("company")
    item = filters.get("item")
    entry_type = filters.get("entry_type")
    in_or_out = filters.get("in_or_out")
    conditions = []
    params = [comp,from_date, to_date]

    if from_date and to_date and comp:
        if in_or_out == 'OUT':
            sql_query = """
                        SELECT sc.name, sc.supplier_id, sc.company, sc.posting_date, sc.source_warehouse, sc.target_warehouse, isc.raw_item_code, isc.raw_item_name, isc.production_quantity, isc.production_done_quantity,
                        (isc.production_quantity - isc.production_done_quantity) AS production_remaining_quantity
                        FROM `tabSubcontracting` as sc
                        LEFT JOIN `tabItems Subcontracting` isc on sc.name = isc.parent
                        WHERE sc.company = %s AND DATE(sc.posting_date) BETWEEN %s AND %s AND sc.docstatus = 1
                        """
        else:
            sql_query = """
                        SELECT sc.name, sc.supplier_id, sc.company, sc.posting_date, sc.source_warehouse, sc.target_warehouse, isc.raw_item_code, isc.raw_item_name, isc.production_out_quantity as production_quantity, isc.production_done_quantity,
                        (isc.production_out_quantity - isc.production_done_quantity) AS production_remaining_quantity
                        FROM `tabSubcontracting` as sc
                        LEFT JOIN `tabOut Subcontracting List` isc on sc.name = isc.parent
                        WHERE sc.company = %s AND DATE(sc.posting_date) BETWEEN %s AND %s AND sc.docstatus = 1
                        """

        if sup_id:
            add_condition(conditions, params, "sc.supplier_id = %s", sup_id)
        
        if item:
            add_condition(conditions, params, "isc.raw_item_code = %s", item)

        if entry_type:
            add_condition(conditions, params, "sc.out_entry_type = %s", entry_type)

        if in_or_out:
            add_condition(conditions, params, "sc.in_or_out = %s", in_or_out)

        if conditions:
            sql_query += " AND " + " AND ".join(conditions)

        data = frappe.db.sql(sql_query, tuple(params), as_dict=True)
        return data

    else:
        frappe.throw("Company, From Date, To Date is Mandatory")
