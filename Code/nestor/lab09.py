# Lab 9: Compute Automated Readability Index
import string
import math




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

with open("A_Tale_of_Two_Cities.txt", encoding="utf-8") as book_file:
    book = book_file.read()


book = book.replace('?', '.')
book = book.replace('!', '.')
book = book.replace('\n', '')
sentences = book.split('.')
sentences_len = len(sentences)
# print(sentences_len)

book = book.replace(",", "|")
book = book.replace('"', '|')
book = book.replace("'", "|")
book = book.replace('!"', '|')
book = book.replace('/', '|')
book = book.replace('?"', '|')
book = book.replace("\'", '|')
book = book.replace('--', '|')
book = book.replace('(', '|')
book = book.replace(')', '|')
book = book.replace("\n", '|')
book = book.replace('"', '|')
book = book.replace(';', '|')
book = book.replace('|', ' ')

words = book.split()
word_len = len(words)
# print(word_len)

characters = 0 
for character in book:
    characters += 1
# print(characters)

ari_formula = 4.71 * (characters / word_len) + 0.5 * (word_len / sentences_len) - 21.43
ari = math.ceil(ari_formula)
print(f"the ARI for A Tale of Two Cities is {ari}")
print(f"This corresponds to a {ari_scale[ari]['grade_level']} Grade level of difficulty")
print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")

# print(ari)
# print(ari_scale)
