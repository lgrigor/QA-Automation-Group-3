class Parrot:
    
    color = 'green'

    # instance attributes
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
 
    # instance method
    def sing(self, song):
        some = 10
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

Parrot.beak = True


blu.color = 'blue' #Instance attribute
Parrot.beak = True #Class attribute

#print(blu.name, blu.beak, blu.color)
#print(woo.name, woo.beak, woo.color)

