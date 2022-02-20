'''         +-+#^#+--+#^#+--+#^#+-+             
              Project: ROT Cipher                 ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/14/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''

# Program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 







from string import ascii_letters, ascii_lowercase


def rot13 (user_input, num):
    """Encrypts letter by adding changing it to a defined letter at another index"""
    from string import ascii_lowercase

    # create list with letters sorted starting with designated letter instead of a
    # I have no idea why it wouldn't get the last letter of the list without ascii_lowercase[-1]
    rot = list(ascii_lowercase[num:-1] +ascii_lowercase[-1] +ascii_lowercase[0:num])
    print(rot)
    index_nums = []
    rot_list = []
    
    # get index value of user_input chars within ascii_lowercase
    for char in user_input:
        x = ascii_lowercase.index(char)
        index_nums.append(x)
    
    print(index_nums)

    # take index values and apply them to rot_list[index values] to get corresponding char
    for char in index_nums:
        x = rot[char]
        rot_list.append(x)

    print(rot_list)
    print("".join(rot_list))
    

def rot_decrypt (user_input, num):
    """Encrypts letter by adding changing it to a defined letter at another index"""
    from string import ascii_lowercase

    # create list with letters sorted starting with designated letter index value
    rot = list(ascii_lowercase[num:-1] +ascii_lowercase[-1] +ascii_lowercase[0:num])
    decrypted = []
    
    # for char in user_input take the value of the corresponding rot, and apply that index value to the ascii_lowercase
    # append that char to a decrypted list
    for char in user_input:
        x = rot.index(char)
        b = ascii_lowercase[x]
        decrypted.append(b)

    print(decrypted)
    print("".join(decrypted))
   




def main():


    # Encrypt user_input to rot_13
    while True: 

        user_phrase = input("Enter word to convert\n").lower().strip().replace(" ", "") # ensures input is a valid number
        if user_phrase.isalpha() == True:
            break
        else:
            print("Enter a valid input")
            continue


    # Designate amount of rotations for encryption        
    while True:
        try:    
            user_num = int(input("Enter number to determine starting letter for encryption\n"))
            break
        except ValueError:
            print("Enter valid input, 1-26")
            continue

        

    rot13(user_phrase, user_num)


    # Decrypt back to ascii_lowercase
    while True: 

        user_phrase = input("Enter word to convert\n").lower().strip().replace(" ", "") # ensures input is a valid number
        if user_phrase.isalpha() == True:
            break
        else:
            print("Enter a valid input")
            continue


    # Enter amount of rotations to decrypt
    while True:
        try:    
            user_num = int(input("Enter number to determine starting letter for encryption\n"))
            break
        except ValueError:
            print("Enter valid input, 1-26")
            continue


    rot_decrypt(user_phrase, user_num)



if __name__ == "__main__":
    main()
