// Copyright (c) 2024, Quantbit Technologies Pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Material Movement', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Material Movements Item', {
	source_warehouse: function(frm) {
		frm.call({
			method:'available_qty',
			doc:frm.doc
		})
	}
});
frappe.ui.form.on('Material Movements Item', {
	item_code: function(frm) {
		frm.call({
			method:'available_qty',
			doc:frm.doc
		})
	}
});



//  set Source warehouse in Bulk Material Transfer Details
frappe.ui.form.on('Material Movements Item', {
    set_source_warehouse(frm) {
        if (frm.doc.set_target){
            frm.doc.items.forEach(function(i){
                i.source_warehouse = frm.doc.set_source_warehouse;
            });
           
        } frm.refresh_field('items');
    }
});

frappe.ui.form.on('Material Movements Item', {
    item_code: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        if (frm.doc.set_source_warehouse) {
            frappe.model.set_value(child.doctype, child.name, 'source_warehouse', frm.doc.set_source_warehouse);
        }
        frm.refresh_field('items');
    }
});


//  set Target warehouse in Bulk Material Transfer Details
frappe.ui.form.on('Material Movement', {
    set_target_warehouse(frm) {
        if (frm.doc.set_target){
            frm.doc.items.forEach(function(i){
                i.target_warehouse = frm.doc.set_target_warehouse;
            });
           
        } frm.refresh_field('items');
    }
});

frappe.ui.form.on('Material Movements Item', {
    item_code: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        if (frm.doc.set_target_warehouse) {
            frappe.model.set_value(child.doctype, child.name, 'target_warehouse', frm.doc.set_target_warehouse);
        }
        frm.refresh_field('items');
    }
});