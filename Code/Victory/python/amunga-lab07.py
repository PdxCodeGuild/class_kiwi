
'''
This assignment kicked my ass and I couldn't find a solution on my own. Using google, i found the solution at the link below but I could not submit it until I 
was able to explain it to myself as i did.
# https://www.geeksforgeeks.org/replace-every-character-of-string-by-character-whose-ascii-value-is-k-times-more-than-it/

'''
#Create a function that reads through a string from users and returns an intended message

#Create user input/message and turn it into a list
user_input = input('Please enter the message: ')
user = list(user_input)

#create the decipher function, takes user input and the cipher key
def decipher_function(user, cipher_num):
    '''create a var for string, return the string, print the function'''
    message = ""

    for t in range(len(user)):
        index_value = ord(user[t])
        if index_value + cipher_num > 122:
            cipher_num -= (122-index_value)
            new_shift = cipher_num % 26 # 26 is the range of characters from a to z
            message += chr(96 + new_shift)
        else:
            message += chr(index_value + cipher_num)



    return message

print(decipher_function(user, 13))

'''Version 2'''
#the user chooses the number of rotation, incase of version 1, it will be the 'cipher_num'
user_message = input('What is the version 2 message: ').lower()
user_msm = list(user_message)
rot_user = int(input('Please enter the number to rotate the message: ')) # I abbreviated 'rot' for rotation

def version2_cypher(user_msm, rot_user):

    ver_2_msm = ""

    for j in range(len(user_msm)):

        index_val = ord(user_msm[j])
        if index_val + rot_user > 122:
            rot_user -= (122-index_val)
            new_rot = rot_user % 26
            ver_2_msm += chr(96 + new_rot)
        else:
            ver_2_msm += chr(index_val + rot_user)
    
    return ver_2_msm

print(version2_cypher(user_msm, rot_user))
