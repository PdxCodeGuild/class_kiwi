import math
with open('persuasion.txt') as file:     
    lab9_book = file.read()
#print(lab9_book)


#Assign a variable for len sentences, this will be split by either '!, , or .'
sentence = lab9_book.split('.')
sentence = list(sentence)
sentences = float(len(sentence)-1) #After several tests, spliting by '.' adds a len

# print(sentences)
#Assign a variable for len sentences, this will be split spaces.
word = lab9_book.split()
words = float(len(word))
# print(words)
#Assign a variable for characters. spaces will be replace by blank and then character will be counted

character = lab9_book.replace(' ', '')
character = lab9_book.replace('\n','')
characters = float(len(character))
print(characters)


def ari():
    ari = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
    
    ari = math.ceil(ari)
    if ari > 14:
        return 14
    else:
        return ari


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

print(f"\nThe ARI for gettysburg-persuasion.txt is {ari()}. This corresponds to the {ari_scale[ari()].get('grade_level')} grade level of difficulty that is suitable for an average person {ari_scale[ari()].get('ages')}. ")



