import collections

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}

chain = collections.ChainMap(d1, d2)

chain['d'] = 10
del chain['d']

print(chain['d'])

