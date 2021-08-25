# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#Exercise 1: Reverse a given list in Python
x = [100, 200, 300, 400, 500]
x.reverse()
print(x)



#Exercise 2: Add item 7000 after 6000 in the following Python List
list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list[2][2].insert(2, 7000)
print(list)


#Exercise 3: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend (['h', 'i', 'j'])
print(list1)

#Exercise 4: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

given_list = [5, 10, 15, 20, 25, 50, 20]
x = given_list.index(20)
given_list[x] = 200
print(given_list)