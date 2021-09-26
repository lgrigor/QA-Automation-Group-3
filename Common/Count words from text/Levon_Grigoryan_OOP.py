import re

class word_counter(object):

    def __init__(self, file):
        f = open(file, "r")
        all_lines = f.readlines()

        self.dictionary = dict()

        for each_line in all_lines:

            all_words = re.split(r"[\s\W_]+", each_line)

            while '' in all_words:
                all_words.remove('')

            for each_word in all_words:
                each_word = each_word.capitalize()

                if each_word in self.dictionary:
                    self.dictionary[each_word] += 1
                else:
                    self.dictionary[each_word] = 1
                    
        f.close()

    def print_randomly(self):
        for word, count in self.dictionary.items():
            print(f'{word} - {count}')

    def print_alphabet(self):
        sorted_words = list(self.dictionary.keys())
        for word in sorted(sorted_words):
            print(f'{word} - {self.dictionary[word]}')

    def print_decreasing(self, type):
        sorted_counts = sorted(list(self.dictionary.values()), reverse=type)
        i = 0

        while i == 0:
            for word, count in self.dictionary.items():
                if len(sorted_counts) == 0:
                    i = 1
                elif count == sorted_counts[0]:
                    sorted_counts.pop(0)
                    print(f'{word} - {count}')
                else:
                    continue

    def print_word_count(self, word):
        if word in self.dictionary.keys():
            return self.dictionary[word]
        else:
            return 0

    def __add__(self, other): #FIXME
        new = self.dictionary.copy()
        new.update(other.dictionary)
        #print(type(new))
        return new

file1 = word_counter(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Practice\text.txt")
file2 = word_counter(r"C:\Users\Levon Grigoryan\Desktop\Visual Studio Code\Practice\text copy.txt")

#file1.print_word_count('The')
#file2.print_word_count('dsadsadsa')

#file1.print_decreasing(False)
