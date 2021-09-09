# Exercise 1: Return a new set of identical items from a given two set

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 & set2)

# Exercise 2: Returns a new set with all items from both sets by removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 | set2)

# Exercise 3: Given two Python sets, update the first set with items that exist only in the first set
# and not in the second set.

set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1 - set2)

# Exercise 4: Remove items 10, 20, 30 from the following set at once

set1 = {10, 20, 30, 40, 50}
set1.difference_update([10, 20, 30])
print(set1)

# Exercise 5: Return a set of all elements in either A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 ^ set2)

