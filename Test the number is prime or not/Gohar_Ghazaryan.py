def primechecker(x):
    if (x > 1):
        is_prime = True
        for i in range(2,int(x/2+1)):
            if (x % i == 0):
                is_prime = False
                print(x, "is not a prime number")
                print(x, "bajanvum e", i, "-i")
                break
        if (is_prime):
            print(x,"is a prime number")
 
x = int(input("enter number "))
primechecker(x)
