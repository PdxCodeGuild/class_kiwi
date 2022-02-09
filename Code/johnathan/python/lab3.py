# # Lab 3: Number to Phrase

# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# ```python
# x = 67
# tens_digit = x//10
# ones_digit = x%10
# ```
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

#Step 1) Create a dictionary and store the key values



number2phrase_dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15:'fifteen', 16:'sixteen', 17: 'seventeen', 18: 'eighteen', 19:'nineteen', 20: 'twenty',
 30:'thiry', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70:'seventy', 80: 'eighty', 90: 'ninety', 100: 'one-hundred', 200: 'two-hundred',
  300:'three-hundred', 400:'four-hundred', 500:'five-hundred', 600:'six-hundred', 700:'seven-hundred', 800:'eight-hundred', 900: 'nine-hundred'}

#Step 2) Take input from user -- convert to integer 

user_entry = input('Enter a number from 0-999: ')
entry_int = int(user_entry)

if entry_int in number2phrase_dic:
    print(number2phrase_dic [entry_int])

#Use modulus to extract ones and tens digits (hint) -- so you don't have to keep typing stuff out!
#use .get() to access a value with a key
elif entry_int not in number2phrase_dic and entry_int < 100:
    ones_digit = entry_int % 10 # renders ones digit by giving the remainder
    tens_digit = int(entry_int /10) * 10 # Provides the coefficient *10 to recieve a tens digit 
    print(number2phrase_dic.get(tens_digit), number2phrase_dic.get(ones_digit))

elif entry_int not in number2phrase_dic and entry_int >= 100:
    ones_digit = entry_int % 10 # renders ones digit by giving the remainder
    tens_digit = int(entry_int /100) *10 # Provides the coefficient *10 to recieve a tens digit 
    hundreds_digit = (int(entry_int% 1000) // 100) * 100
    print(number2phrase_dic.get(hundreds_digit), number2phrase_dic.get(tens_digit), number2phrase_dic.get(ones_digit))
    
# ## Version 2
# Handle numbers from 100-999.

# ## Version 3 (optional)

# Convert a number to roman numerals.

# ## Version 4 (optional)

# Convert a time given in hours and minutes to a phrase.