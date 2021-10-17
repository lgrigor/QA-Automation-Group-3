import re

text = "The quick brown fox jumps over the lazy dog."
words = ["dog", "fox", "horse"]
for word in words:
    if re.search(word, text):
        print("Matched!")
    else:
        print("Not Matched!")