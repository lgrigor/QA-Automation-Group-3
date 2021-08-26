def isPrimeNumber(num):
 if num > 1:
   seq = int(num**0.5)
   for x in range(2, seq):
     if (num % x) == 0:
       print("the number is not prime")
       return
     else:
       primeNumber = "the number is prime"
   print(primeNumber)

 else:
   print("A prime number is a natural number greater than 1")


isPrimeNumber(num)


