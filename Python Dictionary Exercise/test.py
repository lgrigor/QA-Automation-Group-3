

x = []

for b in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if b %2 == 0:
        x.append(b/2)
    else:
        continue
    print('Added', b)

print(x)