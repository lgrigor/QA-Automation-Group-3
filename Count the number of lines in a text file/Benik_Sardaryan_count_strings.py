file = open("file.txt", "r")

count_line = 0

for line in file:
    count_line += 1

print(count_line)