class Student:
	_schoolName = 0b0100010101 # class attribute
	_schoolName **= 2
	global school
	school = 10


	def __init__(self, name, age):
		self.name=name # instance attribute
		self.age=age # instance attribute 

	def __print_private_attribute(self):
		print(self._schoolName)
		print(some_variable)

class schoolboy(Student):
	def __init__(self, name, age):
		Student.__init__(self, name, age)


std = schoolboy("Steve", 25)
#print(std.__schoolName)

some_variable = 'global'

std.print_private_attribute()
print(school)

#print(std._Student__schoolName)

#print(std.name)
#std.age = 20
#print(std.age)

