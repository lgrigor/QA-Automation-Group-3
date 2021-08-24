#Exercise 1: Reverse the following tuple
tuple1 = (10, 20, 30, 40, 50)
tuple2 =tuple1[::-1]
print(tuple2)
#queshion in 3 line


#Exercise 2: Access value 20 from the following tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print (tuple1[1][1])

#Exercise 3: Unpack the following tuple into 4 variables
tuple1 = (10, 20, 30, 40)
zero, one, two, three = tuple1
print(zero)
print(one)
print(two)
print(three)
#ununderstand 14 line


#Exercise 4: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)


#Exercise 5: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


#Exercise 6: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
tuple2 = tuple1.count(50)
print(tuple2)

#Exercise 7*: Create a tuple with single item 50

tuple = (50,)
print(type(tuple))

