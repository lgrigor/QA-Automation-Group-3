import re

outfile = open("/home/lyuka/Downloads/text.txt", "r")
text = outfile.readlines()
counts = dict()

for line in text:
    print(line)
    
    letters = re.findall(r'\w', line)
    print(letters)

    for letter in letters:
        print(letter)
        letter = letter.lower()
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

print(counts)

list_new = sorted(list(counts.keys()))

for key in list_new:
    print(key, ":", counts[key])