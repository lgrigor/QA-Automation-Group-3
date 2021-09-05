import re

"""
IGNORECASE (I) - Allows case-insensitive matches.
DOTALL (S) - Allows . to match any character, including newline.
MULTILINE (M) - Allows start of string (^) and end of string ($) anchor to match newlines as well.
VERBOSE (X) - Allows you to write whitespace and comments within a regular expression to make it more readable.
"""

statement = 'Please contact us at: levon-grigoryan@gmail.com, lgrigor@GMAIL.COM'

pattern = re.compile(r"""
[\w\.-]+ #First part
@ #Matches @ sign within email addresses
gmail.com #Domain """, re.X | re.I)

addresses = re.findall(pattern, statement)
for address in addresses:
	print("Address: ", address)