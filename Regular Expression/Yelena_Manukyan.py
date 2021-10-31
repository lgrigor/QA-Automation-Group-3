import re

words = r'fox','dog','hours'
text = 'The quick brown fox jumps over the lazy dog.'
for word in words:
  if (re.search(word,text)):
    print ('Matched')
  else:
    print('Not Matched')
