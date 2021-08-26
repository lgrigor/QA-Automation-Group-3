#Python Set Exercise

#Exercise 1:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection(set2)
print(set1)

#Exercise 2:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#set1.update(set2)
newSet = set1.union(set2) 
print(newSet)

#Exercise 3:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference(set2)
print(set1)

#Exercise 4:
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

#Exercise 5:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)

