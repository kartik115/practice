class EmployeeNode:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		self.next = None

class EmployeeStack:
	def __init__(self):
		self.start = None

