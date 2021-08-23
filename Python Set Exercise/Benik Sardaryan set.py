# Exercise 1: Return a new set of identical items from a given two set
 
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Expected output: {40, 50, 30}

x = set1.intersection(set2)

print("Exercise 1, output:", x)

# Exercise 2: Returns a new set with all items from both sets by removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Expected output: {70, 40, 10, 50, 20, 60, 30}

x = set1.union(set2)

print("Exercise 2, output:", x)

# Exercise 3: Given two Python sets, update the first set with items that exist only in the first set and not in the second set.

set1 = {10, 20, 30}
set2 = {20, 40, 50}

# Expected output: {10, 30}

x = set1.difference(set2)

print("Exercise 3, output:", x)

# Exercise 4: Remove items 10, 20, 30 from the following set at once

set1 = {10, 20, 30, 40, 50}

# Expected output: {40, 50}

x = set1.symmetric_difference({10, 20, 30})

print("Exercise 4, output:", x)

# Exercise 5: Return a set of all elements in either A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Expected output: {20, 70, 10, 60}

x = set1.symmetric_difference(set2)

print("Exercise 5, output:", x)
