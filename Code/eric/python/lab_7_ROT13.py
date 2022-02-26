##Lab 7 ROT Cipher

#version 1
# Accept an input
user_string = input("Please enter a message: ")

#make it all lower case
user_string = user_string.lower()


#dictionary?
letter_values = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'n' : 'a',
    'o' : 'b',
    'p' : 'c',
    'q' : 'd',
    'r' : 'e',
    's' : 'f',
    't' : 'g',
    'u' : 'h',
    'v' : 'i',
    'w' : 'j',
    'x' : 'k',
    'y' : 'l',
    'z' : 'm'
}

#Dissect the input
#convert the input into a dictionary or ascii value
def rot13(user_string):
    value_string = " "
    for letter in user_string:
        letters = letter in letter_values.keys()
        if letters == True:
            value_string += letter_values[letter]
    return value_string
  
converted_text = rot13(user_string)

print(f"Encoded message:{converted_text}")
    



#Add 13 to the value
#account for loop over

#Turn value back into letters