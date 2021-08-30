'''Write a Python function that takes a number as an argument and check the number is prime or not.
Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
'''
def prime(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        for x in range (2,n):
            if(n% x==0):
                return 0

        return 1
print(prime(607))




