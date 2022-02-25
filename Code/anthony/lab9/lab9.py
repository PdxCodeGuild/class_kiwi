###  Lab 9  ###
################################
##                            ##
##   Lab 9:Compute ARI        ##
##   Author: Anthony Billie   ##
##   Date: 2/22/2022          ##
##                            ##
################################

# import text and derive the following
# characters
# words
# sentences
import math
# dictionary
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

with open('book.txt') as book_file:
    book = book_file.read()


# word conversion
# print(book_words)

# character converstion
char = []
for x in book:
    char.append(x)
    # sum of all characters
char_sum = len(char)
# print(char_sum)

# words conversion
string = book.split()
word_sum = len(string)
# print(string_sum)

# sentences conversion
sentence = book.split('.')
sentence_sum = len(sentence)


# ARI
value = 4.71 * (char_sum/word_sum) + 0.5 * (word_sum/sentence_sum)-21.43
# roundup
ari = math.ceil(value)
# ari logic to choose grade level from dictionar
if ari > 14:
    grade = ari_scale[14]['grade_level']
else:
    grade = ari_scale[ari]['grade_level']
# logic to choose ages
if ari > 14:
    age = ari_scale[14]['ages']
else:
    age = ari_scale[ari]['ages']


print(f"The ARI for book.txt is {ari}.")
print(f"This corresonpnds to a {grade} level of difficulty ")
print(f"that is suitable for an average person {age} years old.")
