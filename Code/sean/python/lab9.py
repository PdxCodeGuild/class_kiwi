from string import ascii_letters
import math

with open("lab9.txt") as file:   #opening text file and reading and saving into a variable 
    text_file = file.read()


character_list = []


for letter in text_file:           #looping throught to see if letters are in ascii and then appending to character list if they are
    if letter in ascii_letters:
        character_list.append(letter)
    else:
        continue            #ignoring everything else

words_list = text_file.split(" ")       #spliting at white spaces to get words seperated
sentence_list = text_file.split(".")       #all sentences have a . so i decided to split there


formula = 4.71 * (len(character_list) / len(words_list)) + 0.5 * (len(words_list) / len(sentence_list)) - 21.43 #math formula for ARI


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


#f string using veriables to get info from dicts
print(f"The ARI for lab9.txt is {math.ceil(formula)}, This corresponds to a {ari_scale[math.ceil(formula)]['grade_level']} level of difficulty that is suitable for an average person {ari_scale[math.ceil(formula)]['ages']} years old.")