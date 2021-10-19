# Copyright (c) 2021, Mohamed M Mohamed and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class PackageContainer(Document):
	def before_save(self):
		self.code_number = f'CN-{self.name}'
		self.source = self.location
		if self.status != 'Free':
			validateRoute(self)
			# if self.source != 'Null' and self.destination != 'Null':
			# 	changePackagesStatus(self)
		if self.status == 'Free':
			if self.destination != 'Null':
				self.location = self.destination
				self.number_of_packages = 0
			self.source = 'Null'
			self.destination = 'Null'


def validateRoute(self):
	if self.source == self.destination:
		frappe.throw('No Such Route:- Source and Destination must have different values.')
	elif self.source == 'Null':
		frappe.throw('Source Country Cannot Be Null');
	elif self.destination == 'Null':
		frappe.throw('Destination Country Cannot Be Null');
	else:
		changePackagesStatus(self)

def changePackagesStatus(self):
	packages = frappe.get_all("Items Package", filters={"status": ('!=', 'Delivered'), "parent_container": self.name })
	for single_package in packages:
		frappe.db.sql("""update `tabItems Package` set status=%(container_status)s where name=%(package_name)s""", {"container_status": self.status, "package_name": single_package.name})
	self.number_of_packages = len(packages)
	frappe.msgprint(f"All Packages Belongs To '{self.code_number}' Container Have Been Modified  Their Statuses To '{self.status}'")