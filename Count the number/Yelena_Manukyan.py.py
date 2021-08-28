numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x=list(numbers)
even=0
odd=0
for num in x:
    if num % 2 ==0:
        even+=1
    else:
        odd += 1 
print('Number of even numbers :',even)
print('Number of odd numbers  :', odd)
    
