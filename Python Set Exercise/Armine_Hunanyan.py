#Set
#Ex1:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print( set1.intersection(set2))

#Ex2:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1|set2)


#Ex3:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))

 
#Ex4:
set1 = {10, 20, 30, 40, 50}
#Expected output: {40, 50}
print(set2.difference(set1))

#Ex5:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print (set1.symmetric_difference(set2))

