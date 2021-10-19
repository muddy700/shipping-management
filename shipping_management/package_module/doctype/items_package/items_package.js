// Copyright (c) 2021, Mohamed M Mohamed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Items Package", {
  refresh: function (frm) {
    frm.add_custom_button("Add New Package", () => {
      frappe.new_doc("Items Package", {
        owner: frm.doc.owner,
        source: frm.doc.source,
        // owner_full_name: frm.doc.owner
      });
    });
    frm.add_custom_button("Add New Customer", () => {
      frappe.new_doc("Customer", {
        // owner_full_name: frm.doc.owner
      });
    });
  },
});

cur_frm.fields_dict["parent_container"].get_query = function (doc, cdt, cdn) {
  var current_package = locals[cdt][cdn];
  return {
    filters: {
      status: "Free",
      shipping_mode: current_package.shipping_mode,
      location: current_package.source,
    },
  };
};
