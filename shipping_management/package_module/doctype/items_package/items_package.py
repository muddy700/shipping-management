# Copyright (c) 2021, Mohamed M Mohamed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemsPackage(Document):
	def before_save(self):
		self.shipping_code = f'SC-{self.name}'
		self.outstanding = self.cost - self.paid
		self.number_of_items_types = len(self.items)
		self.total_items = findTotalItems(self.items)
		self.has_approved = validatePayment(self.outstanding)
		validateRoute(self.source, self.destination)


def findTotalItems(items):
	total = 0;
	for item in items:
		total += item.quantity
	return total

def validatePayment(outstanding):
	if outstanding == 0:
		return 1;
	else:
		return 0;

def validateRoute(source, destination):
	if source == destination:
		frappe.throw('No Such Route:- Source and Destination must have different values.');
	else: 
		pass
