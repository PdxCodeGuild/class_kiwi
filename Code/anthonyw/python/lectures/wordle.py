import string

# Open file
with open('words.txt') as file:
    # Read file
    words = file.read()

words = words.split('\n')

# Remove all words that are not 5 letters
# Remove any words that contain special characters
five_letter_words = []
for i in words:
    if len(i) == 5 and i.isalpha():
        five_letter_words.append(i.lower())

output = "\n".join(five_letter_words)
with open('wordlist.txt', 'w') as file:
    file.write(output)
