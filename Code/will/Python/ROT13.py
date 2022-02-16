from string import ascii_letters


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

def encrypt_decrypt(comparison_list):
    encoded_letters = []
    
    for letter in comparison_list:
        if letter in rot_thirteen.keys():
            encoded_letters.append(rot_thirteen.get(letter))
        elif letter not in rot_thirteen.keys():
            encoded_letters.append(letter)
        
    return encoded_letters

rot_thirteen = {'a': 'n', 'b': 'o',
'c': 'p', 'd': 'q',
'e': 'r', 'f': 's',
'g': 't', 'h': 'u',
'i': 'v', 'j': 'w',
'k': 'x', 'l': 'y',
'm': 'z', 'n': 'a',
'o': 'b', 'p': 'c',
'q': 'd', 'r': 'e',
's': 'f', 't': 'g',
'u': 'h', 'v': 'i',
'w': 'j', 'x': 'k',
'y': 'l', 'z': 'm'}

english_letters = list(ascii_letters)

user_input = input('Please enter your word or phrase you would like to encode/decrypt: ')
user_input = user_input.lower()
number_of_encryptions = int(input('How many times would you like to run your phrase through encryption/decryption: '))

comparison_list = list(user_input)
rotation_amount = 0

encoded_letters = encrypt_decrypt(comparison_list)
rotated_phrase = []

if rotation_amount < (number_of_encryptions - 1):   
    while rotation_amount < (number_of_encryptions - 1):
        rotated_phrase = encrypt_decrypt(encoded_letters)
        mencoded_letters.clear()
        more_encoded_letters = encrypt_decrypt(rotated_phrase)
        rotation_amount += 1






encoded_phrase = ''.join(rotated_phrase)

print(encoded_phrase)