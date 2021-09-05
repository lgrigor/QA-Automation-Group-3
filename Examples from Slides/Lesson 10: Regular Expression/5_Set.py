import re

print(re.search(r'[0-6]', 'Number: 5').group())

print(re.search(r'Number: [^5]', 'Number: 0').group())

print(re.search(r'Number: [^5]', 'Number: 5'))