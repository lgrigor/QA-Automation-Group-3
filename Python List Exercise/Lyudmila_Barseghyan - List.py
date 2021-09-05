"""Python List Exercise"""

# Exercise 1: Reverse a given list in Python
# Example 1
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Example 2
list2 = [100, 200, 300, 400, 500]
print(list2[::-1])


# Exercise 2: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)


# Exercise 3: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)


# Exercise 4: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
index_20 = list1.index(20)
list1[index_20] = 200
print(list1)