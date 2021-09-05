import re

statement = 'Please contact us at: levon-grigoryan@gmail.com'
match = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)

if match:
	print("Email address:", match.group('email'))
	print("Username:", match.group('username'))
	print("Host:", match.group('host'))
else:
    print('Match not found')