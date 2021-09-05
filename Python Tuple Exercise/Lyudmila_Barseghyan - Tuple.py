"""Python Tuple Exercise"""
# Exercise 1: Reverse the following tuple
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

# Exercise 2: Access value 20 from the following tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

# Exercise 3: Unpack the following tuple into 4 variables
tuple1 = (10, 20, 30, 40)
(number_1, number_2, number_3, number_4) = tuple1
print(number_1)
print(number_2)
print(number_3)
print(number_4)

# Exercise 4: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
ind1 = tuple1.index(44)
ind2 = tuple1.index(55)
tuple2 = tuple([tuple1[ind1], tuple1[ind2]])
print(tuple2)

# Exercise 5: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# Exercise 6: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

# Exercise 7*: Create a tuple with single item 50
tuple1 = (50,)