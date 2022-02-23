# Lab 7 ROT13


# Write a program that prompts the user for a string, and encodes it with ROT13.
# For each character, find the corresponding character, add it to an output string.
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.
# dictionary for rot13
rot13_dict = {
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
    "n": "a",
    "o": "b",
    "p": "c",
    "q": "d",
    "r": "e",
    "s": "f",
    "t": "g",
    "u": "h",
    "v": "i",
    "w": "j",
    "x": "k",
    "y": "l",
    "z": "m",
    " ": " "
}

# Prompt user for string
user_string = input("Please enter a string: ")
print(user_string)

# encode string with rot 13
# for loop to run through each character in string and append it to a new string
encoded_list = []
for x in user_string:
    encoded_list.append(rot13_dict[x])

print(''.join(encoded_list))
