numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0 
count_even = 0
for x in numbers:
        if not x % 2:
           count_even += 1
        else:
           count_odd += 1
print ("Number of even_numbers :", count_even)
print ("Number of odd_numbers :", count_odd)
