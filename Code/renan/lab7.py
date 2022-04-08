# code = ord('a')
# code += 13
# print(chr(code))

# message = 'Hello World'
# print(message[0])
#
import string


#prompt the user for a string
orginal_input = input("PLeaser enter a string: ")

output = ""
#for each character find corresponding character
for letter in orginal_input:
    
    if letter in string.ascii_lowercase:
    
        position = string.ascii_lowercase.find(letter)
   
        encrypted_letter = string.ascii_lowercase[(position +13) % 26]
    
#add to output string
        output += encrypted_letter
    else:
        output += letter
#show the user the encrypted message
print(output)