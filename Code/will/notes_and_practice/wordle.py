import string

# open file
with open('words.txt') as file:
    # read file
    words = file.read()

# separate words into a list split at new line character
words = words.split('\n')


# remove all words that are not 5 letters
# remove any words that contain special characters
word_list = []
for i in words:
    if len(i) == 5 and i.isalpha():
        word_list.append(i.lower())

output = '\n'.join(word_list)
    
with open('words.txt', 'w') as file:
    file.write(output)