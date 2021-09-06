class Parrot:
    '''This is a docstring. I have created a new Parrot class'''
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        if isinstance(age, int):
            self.age = age        
        else:
            print('age must be integer')
            exit(1)
        if isinstance(name, str):
            self.name = name
        else:
            print('name must be text')
            exit(1)

# instantiate the Parrot class
blu = Parrot(10, 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

#print(Parrot.__doc__)