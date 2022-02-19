# Lab 7: Version 1

# Dictionaries to set values to string inputs and outputs
letters = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
    'i': 8, 'j': 9,'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
    'w': 22, 'x': 23, 'y': 24, 'z': 25
}
n_letters = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
    8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
    15:'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
    22: 'w', 23: 'x', 24: 'y', 25: 'z'
}

# User's phrase to encrypt
string = input("Enter phrase to encrypt: ").lower()

# Function that iterates each character and convert to new letter by 13 index spaces.
def encrypt(string):
    new_string = []
    for i in string:
        for letter in string: 
            if letter == ' ':
                new_string.append(' ')
            elif letters[letter] <= 12:
                new_letter = letters[letter] + 13
                new_string.append(n_letters[new_letter])
            elif letters[letter] > 12:
                new_letter = letters[letter] - 13
                new_string.append(n_letters[new_letter])            
        return ''.join(new_string)

# Output of input encrypted        
print(f'Your phrase encrypted is: {encrypt(string)}')        
