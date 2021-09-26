# Benik Helena Yelena

import re

text = open("text.txt", "r")

text_sym = re.compile(r"[^a-zA-Z0-9]")

text = text.read()

text = text_sym.sub(" ", text)

text = text.lower()

text = text.split()

text_dict = dict()


for word in text:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1

print(text_dict)
