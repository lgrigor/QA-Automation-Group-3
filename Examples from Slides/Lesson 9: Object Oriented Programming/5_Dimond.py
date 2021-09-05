# Python Program to depict multiple inheritance
# when every class defines the same method

class Class1:	
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")
	
class Class4(Class2, Class3):
	def m(self):
		print("In Class4")

obj = Class4()

obj.m()







"""
Class2.m(obj) # Output: In Class2
Class3.m(obj) # Output: In Class3
obj1 = Class1() # Output: In Class1
obj1.m()
"""
#print(Class4.mro())