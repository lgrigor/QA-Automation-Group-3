class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name, + abc.age)

p1 = Person("Xachik", 102)
p2 = Person("Helena", 507)
p1.myfunc()
p2.myfunc()
print(p1)
print(p2)