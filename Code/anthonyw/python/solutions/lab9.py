

# Open book
import math
filename = "the_great_gatsby.txt"
with open(filename, encoding="utf-8") as book:
    text = book.read()

# Get number of words
word = text.split()
words = len(word)

# Get number of sentences
exclamation = text.count('! ') + text.count('!\n')
periods = text.count('. ') + text.count('.\n')
questions = text.count('? ') + text.count('?\n')
sentences = exclamation + periods + questions

# Get number of characters
num_characters = 0
for char in text:
    if char.isalpha():
        num_characters += 1

# Create ARI function


def ari():
    formula = math.ceil(4.71 * (num_characters / words) +
                        0.5 * (words / sentences) - 21.43)

    if formula > 14:
        return 14
    return formula


# Copy ARI score dictionary
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

# print result
output = f"""--------------------------------------------------------

The ARI for {filename} is {ari()}
This corresponds to a {ari_scale[ari()]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari()]['ages']} years old.

--------------------------------------------------------
"""

print(output)
