# Exercise 1: Reverse the following tuple

simple_tuple = (10, 20, 30, 40, 50)
reverse_tuple = simple_tuple[::-1]
print(reverse_tuple)

# Exercise 2: Access value 20 from the following tuple

tuple_value = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple_value[1][1])

# Exercise 3: Unpack the following tuple into 4 variables

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a, b, c, d)

# Exercise 4: Copy element 44 and 55 from the following tuple into a new tuple

first_tuple = (11, 22, 33, 44, 55, 66)
new_tuple = first_tuple[3:5]
another_tuple = first_tuple[3], first_tuple[4]
print(new_tuple)
print(another_tuple)

# Exercise 5: Modify the first item (22) of a list inside a following tuple to 222

tuple_list = (11, [22, 33], 44, 55)
tuple_list[1][0] = 222
print(tuple_list)

# Exercise 6: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

# Exercise 7*: Create a tuple with single item 50

single_tuple = (50,)
print(single_tuple)
