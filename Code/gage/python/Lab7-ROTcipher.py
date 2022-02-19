import string

'''


VERSION 1


# Base letters 
alphabet = list(string.ascii_lowercase)
# ROT 13 base letters
rot = list("nopqrstuvwxyzabcdefghijklm") 
# Converts users input into a list with all lower case chars
user_phrase = list(input("Enter a phrase: ").lower())

# Empty vars to store the final out put and a counter to change the index
output = ""
index_counter = 0

# Loops until whole word is encrypted
while index_counter < len(user_phrase):
    get_index = rot.index(user_phrase[index_counter]) #Takes user phrase and grabs the index of each char using the counter
    output += (alphabet[get_index]) # Finds what the index from above converts into
    index_counter += 1 # Adds to the index counter


print( f"Your encrypted phrase is '{output}'")

'''



'''
VERSION 2

# Base letters 
alphabet = list(string.ascii_lowercase)
# ROT 13 base letters
rot = list("nopqrstuvwxyzabcdefghijklm") 
# Converts users input into a list with all lower case chars
user_rot = int(input("How many rotations?: "))
user_phrase = input("Enter a phrase: ").lower()

# If statment checks if the ROT input is even or odd
if (user_rot % 2) == 0:
    print( f"You decrypted your message! '{user_phrase}'") # If the number is even it will decrypt the message

else:
        # If the number is odd it will encrypt the message
    output = ""
    index_counter = 0

    # Loops until whole word is encrypted
    while index_counter < len(user_phrase):
        get_index = rot.index(user_phrase[index_counter]) #Takes user phrase and grabs the index of each char using the counter
        output += (alphabet[get_index]) # Finds what the index from above converts into
        index_counter += 1 # Adds to the index counter


    print( f"Your encrypted phrase is '{output}'")
   
'''

