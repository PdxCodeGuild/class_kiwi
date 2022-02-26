# # Lab 9: Compute Automated Readability Index

# Compute the ARI for a given body of text loaded in from a file. 
# The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
# The general formula to compute the ARI is as follows:

# ![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

# The score is computed by multiplying the number of characters* divided by the number of words* by 4.71,
# adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. 
# **If the result is a decimal, always round up.** Scores greater than 14 should be presented as having the same age 
# and grade level as scores of 14.

#1 convert ebook into a .txt file
#2 open file in read mode

beowolf_file = open('beowolf.txt', encoding ='utf-8')
beowolf_text = beowolf_file.read()




# Make a function to split text into sentences
import string
def break_sentences(text): 
    num_sentences = 0 
    for i in range(len(beowolf_text)):
        if beowolf_text[i] == '.' or beowolf_text[i] == '?' or beowolf_text[i] == '!':
            num_sentences += 1
    return num_sentences
num_sentences = break_sentences(beowolf_text)
# Make a function to break text into words

# print(num_sentences)
 
def word_count(text):
    # beowolf_text.replace(as)
    words = 0
    for character in string.punctuation + string.digits:
        if character in text:
            text = text.replace(character, '')
    words = text.split()
    #     words.append(str(i.lower))  
    return len(words)

# print(word_count(beowolf_text))

# create a function to break up characters in the text

def characters_counter(text):
    num_characters = 0
    for i in text:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
            num_characters += 1
    return num_characters

# print(characters_counter(beowolf_text))

def ARI_score(text):
    character_count = characters_counter(text)
    words_num = word_count(text)
    sent_count = break_sentences(text)
    ari = 4.71*(character_count/words_num) + 0.5*(words_num/sent_count)-21.43
   
   
    # char_div_words = ((characters_counter(text) / word_count(text)))
    # words_div_sent = (word_count(text))/break_sentences(text)
    # ari = 4.71*(char_div_words) + 0.5*(words_div_sent)-21.43

    # # ARI = (((char_div_words * 4.71) + (words_div_sent * 0.5)) - 21.43)
    return ari

beowolf_ARI = round(ARI_score(beowolf_text))



# Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.


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

print(f"The ARI for BeoWulf is {beowolf_ARI}. \nThis corresponds to {ari_scale[beowolf_ARI]['grade_level']} level of difficulty. \nThat is suitable for ages {ari_scale[beowolf_ARI]['ages']} years old.")
# The output should look something like the following:

#     --------------------------------------------------------

#     The ARI for gettysburg-address.txt is 12
#     This corresponds to a 11th Grade level of difficulty
#     that is suitable for an average person 16-17 years old.

#     --------------------------------------------------------