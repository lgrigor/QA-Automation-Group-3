import re

statement = 'Please contact us at: levon-grigoryan@gmail.com'
new_email = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'lgrigor@submarine.com', statement)
print(new_email)

statement = 'Please contact us at: levon-grigoryan@gmail.com'
new_email = re.subn(r'[\w\.-]+@[\w\.-]+', r'lgrigor@submarine.com', statement)
print(new_email)