"""
Compute ARI
Version 1
Timothy Hampton
Hampton12101@gmail.com 
"""
from string import punctuation
import math

file_name = input("Please input a file name: ")
punc = punctuation
read_file = open(file_name, "r")

open_file =  read_file.read()
# print(open_cities)
# char_counter = float(0)
# sent_counter = float(0)
# word_counter = float(len(open_cities.split()))

char_counter = float(0)
sent_counter = float(0)
word_counter = float(len(open_file.split()))
sent_delimiter_list = [".",'!',"?",]
for char in open_file:
    if char != " " and char not in sent_delimiter_list:
        char_counter += 1
# print(char_counter)

for char in open_file:

    if char in sent_delimiter_list:
        sent_counter += 1
        

# print(sent_counter)
# print(word_counter)
# step_1 = char_counter/word_counter
# step_2 = step_1 *4.71
# step_3 = word_counter/sent_counter
# step_4 = step_3 * 0.5 + step_2
# step_5 = step_4 - 21.43 
# step_6 = math.ceil(step_5)
ari = math.ceil(4.71*char_counter/word_counter+ 0.5*word_counter/sent_counter-21.43)
# print(step_1)
# print(step_2)
# print(step_3)
# print(step_4)
# print(step_5)

# print(step_6)

# print(step_6)
print(f"The ARI for {file_name} is {ari}.")

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

ari_grade = ari_scale[ari]
print(f"This corresponds to a {ari_grade['grade_level']} grade level of difficulty.")
print(f"That is suitable for an average person {ari_grade['ages']} years old.")
