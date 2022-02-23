# Lab 9

# set variables from book
with open("beowulf.txt", encoding="utf-8") as book_file:
    book = book_file.read()
book_name = "beowulf.txt"

# character seperation and count
characters = list(book)

ch_counter = 0
for ch in characters:
    ch_counter += 1


# words seperation and count
words = book.replace('.', '')
words = book.replace(',', '')
words = book.split()

w_counter = 0
for word in words:
    w_counter += 1


# sentences seperation and count
sentences = book.split('.')

s_counter = 0
for sentence in sentences:
    s_counter += 1


# # Function calculating ARI: (4.71(characters/words)) + (0.5(words/sentences)) - 21.43
def ARI():
    formula = round((4.71 * (ch_counter/w_counter)) + (0.5 * (w_counter/s_counter)) - 21.43)
    if formula > 14:
        return 14
    return formula


# # ARI scale dictionary
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

# # Example output
# '''
# --------------------------------------------------------
# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.
# --------------------------------------------------------
# '''
print(f'''
The ARI for {book_name} is {ARI()}
This corresponds to a {ari_scale[ARI()]['grade_level']} Grade level of difficulty
that is suitable for an average person {ari_scale[ARI()]['ages']} years old.
''')