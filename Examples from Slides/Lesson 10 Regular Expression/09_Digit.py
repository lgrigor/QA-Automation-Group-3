import re

print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())
