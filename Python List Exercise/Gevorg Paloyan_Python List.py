#Python List Exercise

#Exercise 1
list1 = [100,200,300,400,500,600]
reverslist1 = list1[ : : -1]
print(reverslist1)

#Exercise 2
list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2[2][2].append(7000)
print(list2)

#Exercise 3
list3 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
givenList = ["h", "i", "j"]
list3[2][1][2].extend(givenList)
print(list3)

#Exercise 4
list4 = [5, 10, 15, 20, 25, 50, 20]
indexOf20 = list1.index(20)
list1[indexOf20] = 200
print(list1)


#Exercise 4.1
list4 = [5, 10, 15, 20, 25, 50, 20]
y = 0
for x in list4:
    if x == 20:
        list4.remove(20)
        list4.insert(y, 200)
        print(list4)
        break
    y += 1

