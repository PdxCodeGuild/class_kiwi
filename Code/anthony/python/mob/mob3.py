import random


with open('work.txt') as file:
    doc = file.read()
# word list
doc_list = doc.split()
# random word
random_word = random.choice(doc_list)
# spaces -- string
spaces = len(random_word) * '_'
print(random_word)
# counter
counter = 10
while counter > 1:
    #input --- string
    character = input('Guess a letter: ')
    # logic
    if character not in random_word:
        counter -= 1
        print(f'Guesses remaining: {counter}')
    if character in random_word:
        holder = random_word.find(character)  # index
        new_letter = random_word[holder]  # letter string
        ouput = spaces.replace()
        # output = spaces.replace('_', new)
        # print(output)
