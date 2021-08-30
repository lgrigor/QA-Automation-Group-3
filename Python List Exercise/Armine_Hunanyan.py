#List
#Ex1:
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print('Reversed list:', list1)
 

#Ex2:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(1,'7000')
print(list1[2][2])
 

#Ex3:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend('hij')
print(list1)

#Ex4:
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1[3])
list1[3] = 200
print(list1)

