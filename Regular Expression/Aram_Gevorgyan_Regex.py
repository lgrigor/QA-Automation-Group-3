import re

words = r'fox', r'dog', r'horse'
#words = 'fox', 'dog', 'horse'
sequence = 'The quick brown fox jumps over the lazy dog'

for pattern in words:

    if re.search(pattern, sequence):
        print('Match! ' + pattern)
    else:
        print('Not Matched! ' + pattern)


