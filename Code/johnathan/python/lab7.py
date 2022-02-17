# # Lab 7: ROT Cipher

import string



# Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.


# | Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
# |---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
# | English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
# | ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|

# <!-- To wrap around from index 25 to 0 use modulus %26 to give you the remainder -->

# *** Resources used: https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods 
# *** https://www.pythonprogramming.in/python-list-alphanumeric-characters.html

message = input('Please insert your message to encrypt: ' ).lower()

def rot13 (message):
    alphabet = string.ascii_lowercase
    user_string = ''
    for i in message:
        if i in alphabet:
            if alphabet.index(i) < 13:
                user_string += alphabet[alphabet.index(i) + 13]
            else: user_string += alphabet[alphabet.index(i) - 13]
    else: user_string += i 

    return user_string 

print(rot13(message))


