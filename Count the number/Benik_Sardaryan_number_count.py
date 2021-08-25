numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = 0
odd = 0

for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Количество чётных чисел:", even, "\nКоличество нечётных чисел:", odd)
