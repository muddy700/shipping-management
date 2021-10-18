# Copyright (c) 2021, Mohamed M Mohamed and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Customer(Document):
	def before_save(self):
		self.full_name = f'{self.first_name or ""} {self.last_name or ""}'
