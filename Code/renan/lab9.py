
#ARI_Automated Readability Index
#Open Txt File to read 
total_words = 0
total_char = 0
total_sent = 0
#Importing your file(book) using file IO
with open("ulysses.txt", encoding ="utf-8") as file:
    
    ulysses_contents = file.read()
    
#Get Total Words and Characters...#Split tool splits words...characters...and sentences
    words = ulysses_contents.split() 
    total_char = len(ulysses_contents)
    total_words += len(words)
    total_sent = len(ulysses_contents.split(".")) #len totals the items the split tool divided
   
print("Total Characters and Words and Sentences are: ", total_char, total_words, total_sent)

#Input numbers in formula to compute ARI
ari_output = int(4.71 *(total_char/total_words) + 0.5  * (total_words/total_sent) - 21.43)

 
#ARI Scale

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

#Created a value to correspond with the values of the ARI Output to the Key:Values with the ARI Scale
grade_age_level = ari_scale[ari_output]

print(f"Your Automated Readability Index Score Is {ari_output} {ari_scale[ari_output]}") #f string allows you to use read the variable you already defined

print(f"This corresponds to {grade_age_level['grade_level']} level of difficulty")

print(f"This is suitable for an person who is {grade_age_level['ages']} years old")
