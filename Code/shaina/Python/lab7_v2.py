# Lab 7: Version 2
import string

# User's phrase to encrypt
original_string = input("Enter phrase to encrypt: ").lower()
encryption_level = input("Enter numberic level to encrypt: ")

if encryption_level in string.ascii_letters + string.punctuation:
    encryption_level = input("Enter a number: ")
encryption_level = int(encryption_level)

# Iterates each character and converts to new letter by selected index spaces.
new_string = ''

for letter in original_string:
    if letter in string.whitespace + string.punctuation:
        new_string += letter
    else:
        position = string.ascii_lowercase.find(letter)
        encrypted_letter = string.ascii_lowercase[(position + encryption_level) % 26]
        new_string += encrypted_letter

# Output of input encrypted        
print(f'Your phrase encrypted is: {new_string}')        
