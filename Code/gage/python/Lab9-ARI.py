import math
with open("Alice-Wonder.txt", encoding = "utf-8") as file:
    book = file.read()


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

# Separate characters - also reomoves \n
characters = list(book.replace("\n", ''))
# Separate words - each whitespace
words = book.split()
# Separate sentences - removes \n
sentences = book.replace("\n", '')
sentences = sentences.split(".")

# 4.71 * characters / words + .5 * words / sentences - 21.43

# Division 
char_word = len(characters) / len(words)
sent_word = len(words) / len(sentences)

equation_half_one = 4.71 * char_word
equation_half_two = 0.5 * sent_word - 21.43

ari = equation_half_one + equation_half_two



if ari > 14:
     ari = 14
elif type(ari) == float :
    ari = math.ceil(ari)

final_output = print( f"""
-------------------------------------------------------------------------------

The ARI for Alice-Wonder.txt is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} Grade level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old!

-------------------------------------------------------------------------------
""")
