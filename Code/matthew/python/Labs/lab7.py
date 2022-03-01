"""
Lab 7
Rot13 Cipher

Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

"""
'''
translation = {'a' : 'n', 'b' : 'o', 'c' : 'p','d' : 'q','e' : 'r','f' : 's','g' : 't', 'h' : 'u','i' : 'v',
'j' : 'w','k' : 'x','l' : 'y', 'm' : 'z', 'n' : 'a', 'o' : 'b', 'p' : 'c', 'q' : 'd', 'r' : 'e', 's' : 'f', 't' : 'g',
 'u' : 'h', 'v' : 'i', 'w' : 'j', 'x' : 'k', 'y' : 'l', 'z' : 'm',  
}
'''


def rot13_encrypt(user_input):
    '''
    takes input string and returns encrypted string
    '''
    translation = {  # translating between the input string and ecrypted string
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
    'z' : 'm',
    ' ' : ' '
    
}
    letters_list = []
    encryption = []
    encrypted = ''
    for letter in user_input: # separating the input into indavidual indexes in a list
        letters_list.append(letter)
    for letter in letters_list: # encrypting the input using the translation dictionary
        encryption.append(translation[letter])
    encrypted += ''.join(encryption) # creating the encrypted text
    return encrypted

def rot13_decryption(encrpyted_text):
    '''
    takes encrypted text and decrypts it
    '''
    translation = {  # translating between the input string and ecrypted string
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
    'z' : 'm',
    ' ' : ' '
}
    letters_list = []
    decryption = []
    decrypted = ''
    for letter in encrpyted_text:
        letters_list.append(letter)
    for letter in letters_list:
        decryption.append(translation[letter])
    decrypted += ''.join(decryption)
    return decrypted

# letter_string = 'abcdefg'
# encrypted_string = rot13_encrypt(letter_string)
# print(encrypted_string) # nopqrst
# print(rot13_decryption(encrypted_string)) #abcde
letter_string = input('Enter the text you would like to encrypt ')
text = rot13_encrypt(letter_string)
print(text)
print(rot13_decryption(text)) 