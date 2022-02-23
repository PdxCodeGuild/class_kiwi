print("Welcome to the ROT Encryption Cipher!")
code = input("Please type your message here to be encrypted: ").lower()

cyper = {
        "a":"n",
        "b":"o",
        "c":"p",
        "d":"q",
        "e":"r",
        "f":"s",
        "g":"t",
        "h":"u",
        "i":"v",
        "j":"w",
        "k":"x",
        "l":"y",
        "m":"z",
        "n":"a",
        "o":"b",
        "p":"c",
        "q":"d",
        "r":"e",
        "s":"f",
        "t":"g",
        "u":"h",
        "v":"i",
        "w":"j",
        "x":"k",
        "y":"l",
        "z":"m",
        " ":" "}

encrypted_list = []


#to loop throught the message and grab values from the dict
for i in code:
    val = cyper[i]
    encrypted_list.append(val)


# joining the list back into one string
output = "".join(encrypted_list)

print(output)