from collections import deque

my_string = 'abracadabra'

my_deque = deque(my_string)
my_deque.appendleft('5')
my_deque.append('5')

print(my_deque)