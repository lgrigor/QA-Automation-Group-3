'''Write a Python program to count the number of even and odd numbers from a series of numbers.'''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = 0
even = 0
for x in numbers:
        if  x % 2 == 1:
    	     odd+=1
        else:
    	     even+=1
print("Number of even numbers :", even)
print("Number of odd numbers :" , odd)