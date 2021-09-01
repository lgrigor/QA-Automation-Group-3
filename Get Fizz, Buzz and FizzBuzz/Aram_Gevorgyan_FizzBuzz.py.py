for numbers in range(1, 51):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print('FizzBuzz')
        continue
    if numbers % 3 == 0:
        print('Fizz')
        continue
    elif numbers % 5 == 0:
        print('Buzz')
        continue
    print(numbers)


