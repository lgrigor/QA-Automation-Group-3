"""Get Fizz, Buzz and FizzBuzz """

numbers = range(1,51)

for number in numbers:
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)