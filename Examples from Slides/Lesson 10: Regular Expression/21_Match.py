import re

pattern = "C"
sequence1 = "IceCream"
sequence2 = "Cake"

# No match since "C" is not at the start of "IceCream"
print("Sequence 1: ", re.match(pattern, sequence1))
print("Sequence 2: ", re.match(pattern, sequence2))