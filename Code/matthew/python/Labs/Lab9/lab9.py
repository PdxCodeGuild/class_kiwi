"""
Lab 9:
Compute Automated Readability Index

The score is computed by multiplying the number of characters divided by the number of words by 4.71, 
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. 
If the result is a decimal, always round up. 
Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
"""
import string


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

with open('pride_and_prejudice.txt', encoding='utf-8') as file:
    pride_and_prejudice = file.read()

# getting sentace count
sentences_in_book =  len(pride_and_prejudice.split('.'))
# removing periods and comas
pride_and_prejudice = pride_and_prejudice.replace(',','')
pride_and_prejudice = pride_and_prejudice.replace('.','')
# splitting the string by any whitespace into a list
pride_and_prejudice = pride_and_prejudice.split()
# getting total word count
word_count = len(pride_and_prejudice)

character_count = 0

for word in pride_and_prejudice:
    for letter in word:
        if letter in string.ascii_letters:
            # adding one for every letter in each word to get total character count
            character_count += 1

score = (4.71 * (character_count/word_count) + .5 * (word_count/sentences_in_book) - 21.43)
score = round(score)

book = 'Pride and Predjudice'

print(f"""
The Ari for {book} is {score}
This corresponds to a {ari_scale[score]['grade_level']} level of difficulty
that is sutibale for an average person {ari_scale[score]['ages']}
""")

