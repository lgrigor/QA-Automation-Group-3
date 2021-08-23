# Exercise 1: Reverse the following tuple

from functools import total_ordering


tuple1 = (10, 20, 30, 40, 50)

# Expected output: (50, 40, 30, 20, 10)

x = tuple1[::-1]

print("Exercise 1, output:", x)

# Exercise 2: Access value 20 from the following tuple

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# Expected output: 20

x = tuple1[1][1]

print("Exercise 2, output:", x)

# Exercise 3: Unpack the following tuple into 4 variables

tuple1 = (10, 20, 30, 40)

first_variable, second_variable, third_variable, fourth_variable = tuple1

print("Exercise 3, output:", first_variable, second_variable, third_variable, fourth_variable)

# Exercise 4: Copy element 44 and 55 from the following tuple into a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)

# Expected output: tuple2: (44, 55)

tuple2 = tuple1[3], tuple1[4]

print("Exercise 4, output:", tuple2)

# Exercise 5: Modify the first item (22) of a list inside a following tuple to 222

tuple1 = (11, [22, 33], 44, 55)

# Expected output: tuple1: (11, [222, 33], 44, 55)

tuple1[1][0] = 222

print("Exercise 5, output:", tuple1)

# Exercise 6: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)

# Expected output: 2

x = tuple1.count(50)

print("Exercise 6, output:", x)
