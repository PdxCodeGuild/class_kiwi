##Lab 9 Compute Automated Readability Index
# Compute the readability of a text document
import math
#import text
with open('civil_disobedience.txt', encoding='utf-8') as civil_file:
    civil = civil_file.read()

title = "The Duty of Civil Disobedience"
#break text into wordlist
#removing periods and changing variable
word_list = civil.replace('.', '')
#removing commas
word_list = word_list.replace(',', '')
#removing semicolons
word_list = word_list.replace(';', '')
#removing apostrophe 
word_list = word_list.replace('"', '')
# removing question mark
word_list = word_list.replace('?', '')
#  removing underscore
word_list = word_list.replace('_', '')
# removing dash
word_list = word_list.replace('-', '')
# removing &
word_list = word_list.replace('&', '')
#removing '
word_list = word_list.replace("'", "")
#remove exclamation
word_list = word_list.replace('!', '')
#account for line breaks
word_list = word_list.replace('\n', ' ')

#split based on white space
civil_words = word_list.split()

#find number of words
word_count = len(civil_words)

#loop to find number of characters
character = list(civil)
character_count = len(character)

#loop tp find number of sentences
sentences = civil.replace('?', '.')
sentences = sentences.replace('!', '.')
sentences = sentences.replace('\n', ' ')
sentence_list = sentences.split('.')
sentence_count = len(sentence_list)

#input into 4.71(characters/words) + .5(words/sentences) - 21.43 make sure it rounds up
first = 4.71 * (character_count/word_count)
second = .5 * (word_count/sentence_count)
ari_original = math.ceil(first + second - 21.43)
ari = math.ceil(first + second - 21.43)


# compare score to ARI dictionary
#import ari dictionary
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

if ari > 14:
    ari = 14

age = ari_scale[ari]['ages']
grade_level = ari_scale[ari]['grade_level']

if ari in ari_scale:
    print(f'The ARI for {title} is {ari_original}.\nThis corresponds to a {grade_level} level of difficulty \nthat is suitable for an average person {age} years old.')
    


#site https://www.delftstack.com/howto/python/python-round-up/ for .ceil