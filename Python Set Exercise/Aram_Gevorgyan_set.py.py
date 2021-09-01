set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))


set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))


set1 = {10, 20, 30, 40, 50}
delete = [10, 20, 30]
set1.difference_update(delete)
print(set1)


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

