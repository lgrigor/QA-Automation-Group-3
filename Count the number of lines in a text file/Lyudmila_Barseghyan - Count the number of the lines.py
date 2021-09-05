"""Write a Python program to count the number of lines in a text file."""

f = open('file.txt', 'r')
lines = f.readlines()
print(len(lines))