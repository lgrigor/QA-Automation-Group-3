import re

statement = 'Please contact us at: levon-grigoryan@gmail.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)

if match:
	print("Email address:", match.group()) # The whole matched text
	print("Username:", match.group(1)) # The username (group 1)
	print("Host:", match.group(2)) # The host (group 2)
