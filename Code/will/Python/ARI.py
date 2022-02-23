# ARI Calculator - Version 1

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



with open('beyond_good_evil.txt') as file:
    contents = file.read()

num_characters = 0
for char in contents:
    num_characters += 1

# count common sentence ending punctuations. add ' ' after to ensure end of statement
num_exclam = contents.count('! ')
num_question = contents.count('? ')
num_elipses = contents.count('... ')

# subtract number of elipses from total periods so elipses aren't counted twice
num_period = contents.count('. ') - num_elipses
num_sentences = num_question + num_exclam + num_period + num_elipses


num_words = 0
contents_words = contents.split()
for word in contents_words:
    num_words += 1

#The score is computed by multiplying the number of characters divided by the number of words by 4.71, ]
# adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
# If the result is a decimal, always round up. 
difficulty_score = round(4.71 * (num_characters / num_words) + 0.5 * (num_words / num_sentences) - 21.43)

# Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
if difficulty_score > 14:
    print('The ARI for Beyond Good and Evil is 14.')
    print(f'This corresponds to a {ari_scale[14]["grade_level"]} level of difficulty.')
    print(f'That is suitable for an average person {ari_scale[14]["ages"]} years old.')

# if score is 0
elif difficulty_score <= 0:
    print('Book did not receive a valid ARI, please try again.')

# All scores 1-14
else:
    print(f'The ARI for Beyond Good and Evil is {difficulty_score}.')
    print(f'That corresponds to a {ari_scale[difficulty_score]["grade_level"]} level of difficulty')
    print(f'That is suitable for an average person {ari_scale[difficulty_score]["ages"]} years old.')