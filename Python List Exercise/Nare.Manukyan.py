# Exercise 1: Reverse a given list in Python

reverse_list = [100, 200, 300, 400, 500]
reverse_list.reverse()
print(reverse_list)

# Exercise 2: Add item 7000 after 6000 in the following Python List

add_item_list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
add_item_list[2][2].append(7000)
print(add_item_list)

# Exercise 3: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list

nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
nested_list[2][1][2].extend(sub_list)
print(nested_list)

# Exercise 4: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

python_list = [5, 10, 15, 20, 25, 50, 20]
index = python_list .index(20)
python_list [index] = 200
print(python_list )

