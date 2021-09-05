import re

statement = 'Please contact us at: levon-grigoryan@gmail.com, lgrigor@submarine.com'
addresses = re.finditer(r'[\w\.-]+@[\w\.-]+', statement)

for address in addresses:
	print(address)
