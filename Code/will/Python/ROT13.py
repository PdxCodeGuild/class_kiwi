import string

# ROT13 - Version 1

#rot_thirteen = {'a': 'n', 'b': 'o',
#'c': 'p', 'd': 'q',
#'e': 'r', 'f': 's',
#'g': 't', 'h': 'u',
#'i': 'v', 'j': 'w',
#'k': 'x', 'l': 'y',
#'m': 'z', 'n': 'a',
#'o': 'b', 'p': 'c',
#'q': 'd', 'r': 'e',
#'s': 'f', 't': 'g',
#'u': 'h', 'v': 'i',
#'w': 'j', 'x': 'k',
#'y': 'l', 'z': 'm'}

#english_letters = list(ascii_letters)

#user_input = input('Please enter your word or phrase you would like to encode: ')
#user_input = user_input.lower()

#comparison_list = list(user_input)

#encoded_letters = []

#for letter in comparison_list:
#    if letter in rot_thirteen.keys():
#        encoded_letters.append(rot_thirteen.get(letter))
#    elif letter not in rot_thirteen.keys():
#        encoded_letters.append(letter)

#encoded_phrase = ''.join(encoded_letters)

#print(encoded_phrase)




# ROT13 - Version 2


user_input = input('Please enter your word or phrase you would like to encode/decrypt: ')
user_input = user_input.lower()
encryption_rotations = int(input('How many times would you like to rotate: '))

output = ''
# for each character find corresponding character
for letter in user_input:
    if letter in string.ascii_lowercase:
        position = string.ascii_lowercase.find(letter)
        encrypted_letter = string.ascii_lowercase((position + encryption_rotations) % 26)
        # add to output string
        output += encrypted_letter
    else:
        output += letter

# show encrypted message
print(output)