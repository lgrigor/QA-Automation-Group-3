import re

heading = r'<h1>TITLE</h1>'
print(re.match(r'<.*>', heading).group())