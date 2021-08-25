

#
# Get Fizz, Buzz and FizzBuzz
#
# Write a Python program which iterates the integers from 1 to 50.
# For multiples of 3 print "Fizz" instead of the number.
# For multiples of 5 print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5 - print "FizzBuzz" instead of the number.
# For the rest - print the number.
#
# Please write in a .doc file and attach it when submitting.


for x in range(1, 51):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    else:
        print(x)


