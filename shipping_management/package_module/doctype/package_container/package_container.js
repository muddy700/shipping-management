// Copyright (c) 2021, Mohamed M Mohamed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Package Container", {
  refresh: function (frm) {
    frm.add_custom_button("Add New Container", () => {
      frappe.new_doc("Package Container", {
        status: frm.doc.status,
        location: frm.doc.location,
      });
    });
  },
});
