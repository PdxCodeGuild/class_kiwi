"""
Rot 13 Cipher
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/11/2022
"""


# First we want to prompt the user for a 'str' input 

# We will want to Encode it later with ROT13 which is a 13 space rotational encryption

# We will need to encode each character and then add it to an output str




english_to_rot13 = {
"a" : "n",
"b" : "o",
"c" : "p",
"d" : "q",
"e" : "r",
"f" : "s",
"g" : "t",
"h" : "u",
"i" : "v",
"j" : "w",
"k" : "x",
"l" : "y",
"m" : "z",
"n" : "a",
"o" : "b",
"p" : "c",
"q" : "d",
"r" : "e",
"s" : "f",
"t" : "g",
"u" : "h",
"v" : "i",
"w" : "j",
"x" : "k",
"y" : "l",
"z" : "m",

}

user_input = input('Please enter your secret message: ').lower()
# user_input = user_input.split(" ")
user_input = str(user_input)
input_post_encode =""
for x in user_input:
    y = english_to_rot13.get(x)
    if y != None:
        input_post_encode += y
    
    

print(f"Your ecoded secret message is {input_post_encode}....shhh")

continue_playing = input("Do you want to continue and decode your message? \nY or N ").lower()

# print(continue_playing)
input_decode =""
if continue_playing != "n":
    for x in input_post_encode:
        y = english_to_rot13.get(x)
        input_decode += y
print(input_decode)