# Susanna, Aram, Mary, Armine

import re

file = open("/Users/susannakarapetyan/PythonACA/basic/bdg_file.txt")

raws = file.readlines()


dictionary = dict()
for raw in raws:
    words = re.findall(r"\w+", raw.lower())


    for word in words:


        if word in dictionary:
            dictionary[word] += 1

        else:
            dictionary[word] = 1

print(dictionary)








