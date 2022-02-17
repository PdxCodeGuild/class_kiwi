# Lab 7: ROT Cipher
# Version 1

text = input("Please enter in a string: ").lower().replace(" ", "")


def encrypt(text):
    cipher = []
    for i in range(len(text)):
        char = text[i]
        encrypt = ord(char) + 13
        if encrypt < 123:
            encrypt = chr(encrypt)
            cipher.append(encrypt)
            # print(cipher)
        elif encrypt >= 122:
            repeat = (encrypt % 122) + 96
            repeat = chr(repeat)
            cipher.append(repeat)
            # print(cipher)
    return cipher


print(encrypt(text))
