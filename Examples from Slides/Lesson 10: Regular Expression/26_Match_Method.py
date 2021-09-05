import re

pattern = re.compile('COOKIE', re.IGNORECASE)
match = pattern.search("I am not a cookie monster")

print("Start index:", match.start())
print("End index:", match.end())
print("Tuple:", match.span())