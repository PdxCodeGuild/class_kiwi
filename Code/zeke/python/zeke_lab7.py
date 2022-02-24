# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
# Version 2 (optional)
# Allow the user to input the amount of rotation used in the encryption / decryption.


letters_list = {
'a':'n',
'b':'o',
'c':'p',
'd':'q',
'e':'r',
'f':'s',
'g':'t',
'h':'u',
'i':'v',
'j':'w',
'k':'x',
'l':'y',
'm':'z',
'n':'a',
'o':'b',
'p':'c',
'q':'d',
'r':'e',
's':'f',
't':'g',
'u':'h',
'v':'i',
'w':'j',
'x':'k',
'y':'l',
'z':'m',
}

user_input = input(f'Please tell enter your first and last name: ')

encrypted_string = ''

for letter in user_input:
    encrypted_string +=letters_list[letter]
print(encrypted_string)

#####################################################################
