import re

#
# Print randomly
def print_randomly():
    for word, count in dictionary.items():
        print(f'{word} - {count}')

#
# Print by alphabet
def print_alphabet():
    sorted_words = list(dictionary.keys())
    for word in sorted(sorted_words):
        print(f'{word} - {dictionary[word]}')

#
# if revers=True print by decreasing, else if revers=True print by ascending
def print_decreasing(type):
    sorted_counts = sorted(list(dictionary.values()), reverse=type)
    i = 0

    while i == 0:
        for word, count in dictionary.items():
            if len(sorted_counts) == 0:
                i = 1
            elif count == sorted_counts[0]:
                sorted_counts.pop(0)
                print(f'{word} - {count}')
            else:
                continue


f = open (r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Practice\text.txt", "r")
all_lines = f.readlines()
#print(all_lines, end='')
#exit(0)

dictionary = dict()

for each_line in all_lines:
    #print(each_line)
    #exit(0)

    all_words = re.split(r"[\s\W_]+", each_line)
    #print(all_words)
    #exit(0)

    while '' in all_words:
        all_words.remove('')
    #print(all_words)
    #exit(0)

    for each_word in all_words:
        each_word = each_word.capitalize()
        #print(each_word)
        #exit(0)

        if each_word in dictionary:
            dictionary[each_word] += 1
        else:
            dictionary[each_word] = 1


print_randomly()

print_alphabet()

print_decreasing(True)

print_decreasing(False)
