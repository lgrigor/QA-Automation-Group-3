import collections

d = collections.OrderedDict({'a': 1})
d['b'] = 2
d['c'] = 3
print(d)

d.move_to_end('a')
print(d)
