import re

pattern = 'fox', 'dog', 'horse'

sample_text = "The quick brown fox jumps over the lazy dog."

for i in pattern:
   if re.search(i, sample_text):
       print("Matched: ", '"' + i + '"', "word exists in the string")
   else:
       print("Not Matched!", '"' + i + '"', "word doesn't exist in the string")

