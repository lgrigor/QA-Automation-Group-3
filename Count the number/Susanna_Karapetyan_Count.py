# Task 1

# Count the number

# Write a Python program to count the number of even and odd numbers from a series of numbers.
#
# Sample numbers :
#     numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected output :
#     Number of even numbers : 5
#     Number of odd numbers : 4
#
# Please write in a .doc file and attach it when submitting.


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd_numbers = 0
even_numbers = 0

for number in numbers:
    if number % 2 == 0:
        print("Number of even numbers : ", number)
        even_numbers = even_numbers + number


    else:
        print("Number of odd numbers : ", number)
        odd_numbers = odd_numbers + number

print("Final count of even numbers : ", even_numbers)
print("Final count of odd numbers : ", odd_numbers)
