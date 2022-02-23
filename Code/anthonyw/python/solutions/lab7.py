"""
Write a program that prompts the user for a string, 
and encodes it with ROT13. For each character, find the corresponding character, 
add it to an output string. Notice that there are 26 letters in the English language, 
so encryption is the same as decryption.
"""
import string


# prompt the user for a string
original_input = input("Please enter a string: ").lower()
shift = int(input("Enter amount of rotation: "))

output = ""
# for each character find corresponding character
for letter in original_input:
    if letter in string.ascii_lowercase:
        position = string.ascii_lowercase.find(letter)
        encrypted_letter = string.ascii_lowercase[(position + shift) % 26]
        # add to output string
        output += encrypted_letter
    else:
        output += letter

# show the user the encrypted message
print(output)
