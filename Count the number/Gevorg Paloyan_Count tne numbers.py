numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
countOfEven = 0
countOfOdd = 0
for x in numbers:
   if x % 2 == 0:
       countOfEven += 1
   else:
       countOfOdd += 1
print("Number of even numbers : ", countOfEven)
print("Number of odd numbers : ", countOfOdd)
