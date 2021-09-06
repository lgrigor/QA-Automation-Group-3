import collections

count = collections.Counter('soooooommmmmeeeee sssttttttrrrrriiiiinnnnnnnggggg')
count = collections.Counter(['a','a','a','a','a','b','b','b','b'])
count.subtract('o'*5000)
print(count['o'])

