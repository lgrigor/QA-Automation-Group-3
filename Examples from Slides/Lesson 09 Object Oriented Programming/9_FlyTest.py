class Parrot:
    def fly(self):
        print("Parrot can fly")
        
    def swim(self):
        print("Parrot can't swim")
        
class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


Yura_Polk = Parrot()
Sirush = Penguin()

for bird in (Yura_Polk, Sirush):
    bird.fly()
    bird.swim()