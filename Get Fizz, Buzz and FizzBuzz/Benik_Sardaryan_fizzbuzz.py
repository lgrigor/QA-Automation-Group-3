x = range(1, 51)


for n in x:
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    elif n % 5 == 0:
        print("Buzz")
        continue
    else:
        print(n)
