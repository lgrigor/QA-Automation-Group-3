'''Exercise 1: Reverse a given list in Python
Given List: list1 = [100, 200, 300, 400, 500]
Expected output: [500, 400, 300, 200, 100]
'''
numbers = [100, 200, 300, 400, 500]
numbers.reverse()
print('reversed' , numbers)

'''Exercise 2: Add item 7000 after 6000 in the following Python List
Given List: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

''''Exercise 3: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
Given List: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]
Expected output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)


'''Exercise 4: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
Given: list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output: list1 = [5, 10, 15, 200, 25, 50, 20]
'''
list1 = [5, 10, 15, 20, 25, 50, 20]
20 in list1
index = list1.index(20)
list1 [index] = 200
print (list1) 
