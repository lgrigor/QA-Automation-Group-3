import re
from collections import Counter


text = open(r"C:\Users\ARARAT MANUKYAN\Desktop\text.txt", "rt")
lines = text.read()
line = re.findall("\w+", lines)
letters=str(line)
letters=letters.capitalize()
sorted = True
print(Counter(letters))
