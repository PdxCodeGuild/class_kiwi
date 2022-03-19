import string

def rot13 (message):
    alphabet = string.ascii_lowercase
    user_string = ''
    for i in message:
        if i in alphabet:
            if alphabet.index(i) < 13:
                user_string += alphabet[alphabet.index(i) + 13]
            else: user_string += alphabet[alphabet.index(i) - 13]

    return user_string 