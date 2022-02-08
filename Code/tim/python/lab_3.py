"""
Average Numbers
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/7/2022
"""

# Convert a number to it's English Representation I.E. 67 - Sixty seven
# 
# First let's start with taking the input
# 

user_input = int(input('Pick a number between 0-99: '))

# We will use Modulus to extract the ones and tens digits => index them to a list of strings

# Starting will the modulus reduction

ones_digit = user_input%10

# print(f'{ones_digit}') ###### Tested it, it worked.

tens_digit = user_input%100//10

# print(f'{tens_digit}') ###### Tested it, it worked.

# Modulus reduction completed. now we will use this to index a list of strings, 

# Here we will build the list of strings, first.


ones_english = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]




# print(f'Your ones digit indexes in the {ones_english[ones_digit]}s spot.')

# tested the ones indexing, it works.
# ran into an issue where the 10-19 digits would give an issue, hence tens_special
tens_special = ["ten", 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens_english = ["",
f'{tens_special[ones_digit]}',
'twenty-',
'thirty-',
'fourty-',
'fifty-',
'sixty-',
'seventy-',
'eighty-',
'ninety-'
]

# print(f"Your tens digit indexis in the {tens_english[tens_digit]} spot")

# tested both my tens_special and tens_english variables and they work.


hundreds_digit = user_input%1000//100

hundreds_english = ['',
'one-hundred ',
'two-hundred ',
'three-hundred ',
'four-hundred ',
'five-hundred ',
'six-hundred ',
'seven-hundred ',
'eight-hundred ',
'nine-hundred '
]

# 
# {tens_english[tens_digit]}{ones_english[ones_digit]}')
## tested hundreds_digit in seperate file, this will work.
if  user_input == 0:
    print ("zero")

elif tens_digit == 1:
    print(f'{tens_english[tens_digit]}')

# elif hundreds_digit == 0:
#     print(f'{tens_english[tens_digit]}{ones_english[ones_digit]}')
else:
    print(f'{hundreds_english[hundreds_digit]}{tens_english[tens_digit]}{ones_english[ones_digit]}')

#### Tested and it works

## we will be upgrading to be able to handle numbers 100-999 as well.





