# Lyudmila, Seda, Gohar
import re

outfile = open("/home/lyuka/Downloads/text.txt", "r")
text = outfile.readlines()
counts = dict()

for line in text:
    print(line)    

    words = re.findall(r'\w{2,}', line)
    print(words)

    for word in words:
        print(word)
        word = word.lower()

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        
print(counts)

list_new = sorted(list(counts.keys()))

for key in list_new:
    print(key, ":", counts[key])
