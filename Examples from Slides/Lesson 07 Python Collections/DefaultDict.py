from collections import defaultdict

def some():
    return [1, 2, 3]

d = defaultdict(some)

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d['ddd'])