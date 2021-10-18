// Copyright (c) 2021, Mohamed M Mohamed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
  refresh: function (frm) {
    frm.add_custom_button("Create Package", () => {
      frappe.new_doc("Items Package", {
        owner: frm.doc.name,
      });
    });
  },
});
