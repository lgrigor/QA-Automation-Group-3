import re

pattern = "cookie"
sequence = "Cake and cookie"
match_object = re.search(pattern, sequence)

print(match_object.group())
print(match_object.span())
print(match_object.string)
print(match_object)
