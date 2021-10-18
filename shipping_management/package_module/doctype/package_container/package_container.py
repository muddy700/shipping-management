# Copyright (c) 2021, Mohamed M Mohamed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PackageContainer(Document):
	def before_save(self):
		self.code_number = f'CN-{self.name}'
		if self.status != 'Free':
			validateRoute(self)
		if self.status == 'Free':
			self.source = 'Null'
			self.destination = 'Null'


def validateRoute(self):
	if self.source == self.destination:
		frappe.throw('No Such Route:- Source and Destination must have different values.');
	# elif (self.number_of_packages < 1):
	# 	frappe.throw('Enter Valid Number of Packages');
	else:
		pass