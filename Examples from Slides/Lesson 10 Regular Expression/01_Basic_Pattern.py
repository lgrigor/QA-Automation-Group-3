import re

pattern = r"Cookie"
sequence = "Cookie Something Cookie"
if re.search(pattern, sequence):
	print("Match!")
else:
	print("Not a match!")
