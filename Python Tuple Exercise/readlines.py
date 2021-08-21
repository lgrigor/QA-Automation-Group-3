
"""with open("Files\demofile.txt", "r+") as f:
    l1 = f.readline()
    print(l1)"""

f = open("Files\demofile.txt", "r+")

#l1 = f.readline(2)
l2 = f.readlines()
f.write('sdada')
f.close()

#print(l1)
print(l2)
