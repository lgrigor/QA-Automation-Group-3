'''Write a Python program to search some words in the string. If the word matches, print "Matched - " and the word, otherwise print "Not Matched!".

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
'''
import re
sequence = "The quick brown fox jumps over the lazy dog"
animal = ["dog","fox","horse"]
for x in animal:
 if re.search(x,  sequence):
       print ('Found a match',x)
 else:
       print('Not matched!')




