import string

original_input = input("Enter a word: ").lower()

encrypted_output = ""
for letter in original_input:
    if letter not in string.whitespace + string.punctuation:
        # if letter in string.ascii_lowercase: # also works
        letter_index = string.ascii_lowercase.find(letter)
        encrypted = string.ascii_lowercase[(letter_index + 13) % 26]
        encrypted_output += encrypted
        
    else: 
        encrypted_output += letter

# print(encrypted_output)

unectrypted_output = ""
for letter in encrypted_output:
    if letter not in string.whitespace + string.punctuation:
        unencrypt_letter = string.ascii_lowercase.find(letter)
        unectrypt = string.ascii_lowercase[(unencrypt_letter - 13) % 26]
        unectrypted_output += unectrypt
    else:
        unectrypted_output += letter

# print(unectrypted_output)