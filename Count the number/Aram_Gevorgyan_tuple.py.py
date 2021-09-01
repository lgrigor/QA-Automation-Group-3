tuple1 = (10, 20, 30, 40, 50)
#x = list(tuple1)
#x.reverse()
#y = tuple(x)
#print(y)
tuple1 = tuple1[::-1]
print(tuple1)


tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple2[1][1])


tuple3 = (10, 20, 30, 40)
a, b, c, d = tuple3
print(a, b, c, d)


tuple4 = (11, 22, 33, 44, 55, 66)
tuple4_1 = tuple4[3:5]
print(tuple4_1)


tuple5 = (11, [22, 33], 44, 55)
tuple5[1][0] = 222
print(tuple5)


tuple6 = (50, 10, 60, 70, 50)
print(tuple6.count(50))


tuple7 = (50,)
print(tuple7)
