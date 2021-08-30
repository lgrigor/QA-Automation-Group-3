Write a Python program to count the number of lines in a text file.


with open(r"D:\Helena\ForTeacher.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)



file = open("D:\Helena\ForTeacher.txt","r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

print(line_count)
