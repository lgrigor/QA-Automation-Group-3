a={10, 20, 30, 40, 50}
b={30, 40, 50, 60, 70}
c=a.intersection(b)
print(c)


d= {10, 20, 30, 40, 50}
e= {30, 40, 50, 60, 70}
f=d|e
print (f)


g= {10, 20, 30}
h= {20, 40, 50}
i=g.difference(h)
print (i)


j={10, 20, 30, 40, 50}
j.difference_update({10, 20, 30})
print (j)



m= {10, 20, 30, 40, 50}
n= {30, 40, 50, 60, 70}
o=m.symmetric_difference(n)
print(o)







