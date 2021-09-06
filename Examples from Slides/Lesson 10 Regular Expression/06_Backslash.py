import re

## (Scenario 1) This treats '\s' as an escape character, '\s' defines a space
a = re.search(r'Not a\sregular character', 'Not a regular character').group()

## (Scenario 2) '\' is treated as an ordinary character, because '\r' is not a recognized escape character
b = re.search(r'Just a \regular character', 'Just a \regular character').group()

## (Scenario 3) '\s' is escaped using an extra `\` so its interpreted as a literal string '\s’
c = re.search(r'Just a \\sregular character', 'Just a \sregular character').group()

print(a)
print(b)
print(c)
