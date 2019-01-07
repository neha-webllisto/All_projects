class Test:
	def __init__(self):
		self.data = 'Test data'
		print("initial method")

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name


obj = Test()
print("data", obj.data)
obj.set_name("Python")
print(obj.get_name())