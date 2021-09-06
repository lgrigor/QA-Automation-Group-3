import re

statement = 'Please contact us at: levon-grigoryan@gmail.com, lgrigor@submarine.com'
pattern = re.compile(r'[:,]')

address = pattern.split(statement)
print(address)
