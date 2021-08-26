#Python Tuple Exercise


#Exercise 1:
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple(reversed(tuple1))
print(tuple1)


#Exercise 2:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])


#Exercise 3:
tuple1 = (10, 20, 30, 40)
(x, y, z, k) = tuple1
print(x, y, z, k)

#Exercise 4:
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)

#Exercise 5:
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#Exercise 6:
tuple1 = (50, 10, 60, 70, 50)
x = tuple1.count(50)
print(x)

#Exercise 7*:
tuple1 = (50,)
print(tuple1)

