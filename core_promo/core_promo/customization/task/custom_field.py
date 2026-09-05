import frappe


def create_task_types():
	task_types = ["Like", "Retweet", "Comment", "Quote Tweet"]

	for task_type in task_types:
		if not frappe.db.exists("Task Type", task_type):
			doc = frappe.get_doc({"doctype": "Task Type", "name": task_type})
			doc.insert(ignore_permissions=True)


def delete_task_types():
	task_types = ["Like", "Retweet", "Comment", "Quote Tweet"]

	for task_type in task_types:
		if frappe.db.exists("Task Type", task_type):
			frappe.delete_doc("Task Type", task_type, ignore_permissions=True, force=True)
