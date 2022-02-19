import string
# open file
with open('words.txt') as file:
    words = file.read()

# remove all words that are not 5 letters
# remove all words that contain special characters
words = words.split('\n')

five_letter_words = []
for word in words:
    if len(word) == 5 and word.isalpha(): # isalpha() checks for alabetical character abc...ect
        five_letter_words.append(word.lower())

# print(five_letter_words)

output = "\n".join(five_letter_words)
with open('words.txt', 'w') as file:
    file.write(output)
