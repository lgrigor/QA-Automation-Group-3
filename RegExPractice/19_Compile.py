import re

pattern = re.compile(r"cookie")
sequence = "Cake and cookie"

print(pattern.search(sequence).group())

#print(re.search(pattern, sequence).group())

pattern = "cookie"
sequence = "Cake and cookie"
re.search(pattern, sequence)
