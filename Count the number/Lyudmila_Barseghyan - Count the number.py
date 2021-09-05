"""Count the number """
   
# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

even_mumber = 0
odd_number = 0
for number in numbers:
    if number % 2 != 0:
        odd_number += 1
    else:
        even_mumber += 1


print("Number of even numbers : {}".format(even_mumber))
print("Number of odd numbers : {}".format(odd_number))