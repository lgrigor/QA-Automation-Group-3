import re

def match_text():
        if text == "":
            for word in wrdsrch:
                if re.search(word, default_text):
                        print("Matched in default text -", word)
                else:
                        print("Not Matched! -", word)
        else:
            for word in wrdsrch:
                if re.search(word, text):
                        print("Matched -", word)
                else:
                        print("Not Matched! -", word)


default_text = "The quick brown fox jumps over the lazy dog"

default_words = ["fox", "dog", "horse"]


for word in default_words:
    if re.search(word,  default_text):
        print("Matched -", word)
    else:
        print("Not Matched! -", word)


text = input("Введите ваш текст: ")

search = input(r"Введите, что нужно найти в тексте: ")

wrdsrch = re.split(r"\s", search)


match_text()
