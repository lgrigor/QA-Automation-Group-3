class Student:
	schoolName = 'XYZ School' # class attribute

	def __init__(self, name, age, DOB):
		self.name=name # instance attribute
		self.age=age # instance attribute 
		self.DOB=DOB
		
	def __add__(self, other):
		return (self.name + other.name).upper()

	def __eq__(self, other):
		if self.age == other.age:
			return True
		else:
			return False

Olive = Student('Olive', 18, 1991)
Franko = Student('Franko', 20, 2000)
print(Olive == Franko)

