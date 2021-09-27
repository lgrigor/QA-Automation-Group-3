import re
file = open(r"C:\Users\Aram\Desktop\text.txt")
all_raws = file.readlines()

dictionary = dict()

for each_raw in all_raws:
    each_raw = re.findall(r"[^\W_]", each_raw.lower())

    for each_letter in each_raw:

        if each_letter in dictionary:
            dictionary[each_letter] += 1
        else:
            dictionary[each_letter] = 1


new_list = sorted(list(dictionary.keys()))

for each_key in new_list:
    print(each_key, "=", dictionary[each_key])