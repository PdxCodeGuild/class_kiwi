#lab 09 - ARI Computation - Working

#imports
import re
import math

#test text
#text = "The quick brown fox jumped over the lazy dog."

filename = input("Input the filename: ")
with open(filename, "rt", encoding="utf8") as file:
    text = file.read()

#define variables
n_chars = len(re.findall(r'\w', text))
n_words = len(re.findall(r'\w+', text))
n_sents = len(re.findall(r'\.|\?|\!', text))

#define ari
ari = math.ceil(4.71 * (n_chars / n_words) + 0.5 * (n_words / n_sents) - 21.43)
if ari > 14:
    ari = 14

#ari dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
#print(n_chars, n_words, n_sents)

#print title and author
for line in re.findall('Title:\s(.*)', text):
    print('The title of this book is:', line)
for line in re.findall('Author:\s(.*)', text):
    print('The author of this book is:', line)

#print ari output
print('The ARI for',filename ,'is',ari)
print('This corresponds to a',(ari_scale[ari]['grade_level']), 'level of difficulty')
print('That is suitable for an average person', (ari_scale[ari]['ages']), 'years old.\n')
