# Lab 9 Compute Automated Readability Index

# by Agatha Christie: https://www.gutenberg.org/cache/epub/863/pg863.txt
book_title = "The Mysterious Affair at Styles"

# read in text
with open('The_Mysterious_Affair_at_Styles.txt', encoding='utf-8') as text:
    text = text.read().splitlines()

# get char count
rejoin = ' '.join(text)
# char_string = rejoin.replace(" ","") # add if whitespace not included as a character
# if whitespace is included as a character use...
char_count = int(len(rejoin))

# get word count
words = rejoin.split() # split at whitespace
word_count = int(len(words))

# get sentence count
# not perfect since not all . are sentence endings, like Mrs. or Mr.
sentences = rejoin.split('.') + rejoin.split('?') + rejoin.split('!')
sentence_count = int(len(sentences))

# given formula
ari_compute = 4.71 * (char_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43
# round up 
ari_round_up = int(-(-ari_compute // 1))

# given ARI scale
ari_scale = {
     1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages': '6-7', 'grade_level': '1st Grade'},
     3: {'ages': '7-8', 'grade_level': '2nd Grade'},
     4: {'ages': '8-9', 'grade_level': '3rd Grade'},
     5: {'ages': '9-10', 'grade_level': '4th Grade'},
     6: {'ages': '10-11', 'grade_level': '5th Grade'},
     7: {'ages': '11-12', 'grade_level': '6th Grade'},
     8: {'ages': '12-13', 'grade_level': '7th Grade'},
     9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

# compare formula output to ARI scale
ari = ari_scale.get(ari_round_up)

# print results
print(f'''
--------------------------------------------------------

The ARI score for "{book_title}" is {ari_round_up}.
This corresponds to a {ari['grade_level']} level of difficulty
that is suitable for an average person {ari['ages']} years old.

--------------------------------------------------------
'''
)