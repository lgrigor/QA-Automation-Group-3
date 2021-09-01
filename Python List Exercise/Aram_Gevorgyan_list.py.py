list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2[2][2].insert(2, 7000)
print(list2)


list3 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list3_1 = ["h", "i", "j"]
list3[2][1][2].extend(list3_1)
print(list3)


list4 = [5, 10, 15, 20, 25, 50, 20]
x = list4.index(20)
list4[x] = 200
print(list4)




