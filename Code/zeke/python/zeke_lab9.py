# Lab 9: Compute Automated Readability Index
# Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S.
#  grade level for a given block of text. The general formula to compute the ARI is as follows:

# ARI Formula

# ari = 4.71*(n_characters/n_words) + 0.5*(n_words/n_sentences)-21.43


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

# find words
# find characters

# find sentences


with open('/Users/ezekielwells/Desktop/class_kiwi/Code/zeke/python/emma.txt') as word_file:
    words = word_file.read()

import string
# print(type(words))

punctuations = string.punctuation
# print(punctuations)

sentence = words.replace('\n','')
# for item in words:
#     if item in punctuations:
#         sen_count += 1
sentence = sentence.split('.')
# sentence = sentence.split('?')
# sentence = sentence.split('!')

sen_count = len(sentence)


# print(type(sentence))
print(f'sentence: {sen_count}')


# print(words)
# words = words.replace('.','')
# words = words.replace(',','')
# print(words)
words = words.split()
word_count= len(words)
print(f'words: {word_count} ')


# print(type(words))

count_characters = 0
# test = ['hello', 'friday', 'sunshine']
characters = string.ascii_letters

for word in words:
    count_characters += len(word)
  
    # print(word, len(word), count_characters)
print(f'characters: {count_characters}')
# print(characters)

# ari = 4.71*(n_characters/n_words) + 0.5*(n_words/n_sentences)-21.43
a= 4.71 * (count_characters/word_count) + 0.5 * (word_count/sen_count)-21.43

a = round(a)

# print(sentence)

ari_scale[a]
print(ari_scale[a])

print(f'''The ARI for Emma is {a}
This corresponds to a {ari_scale[a]['grade_level']}th Grade level of difficulty
that is suitable for an average person {ari_scale[a]['ages']} years old.''')
print(punctuations)