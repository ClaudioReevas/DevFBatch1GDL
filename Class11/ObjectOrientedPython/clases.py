class Persona():
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name + self.house

	def get_age(self):
		return self.age

persona = Persona("hugo", 30)

print persona.get_name()
print persona.get_age()