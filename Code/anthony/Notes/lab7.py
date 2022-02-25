###  Lab 7 Practice  ###
################################
##                            ##
##   Lab 7: ROT Cipher        ##
##   Author: Anthony Billie   ##
##   Date: 2/24/2022          ##
##                            ##
################################

# """
# Write a program that prompts the user for a string, and encodes it with ROT13.
# For each character, find the corresponding character, add it to an output string.
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.
# """
import string


# prompt user for string
user_input = input("Please enter a string: ")

output = ''
# convert charactter to corresponding output (ROT13)
for character in user_input:
    position = string.ascii_lowercase.find(character)
    encrypted = string.ascii_lowercase[(position + 13) % 26]
    output += encrypted
print(output)


# ADD character to output string
