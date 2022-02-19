# Lab 3: Version 3 ---- Roman numerals to 999

# Number is input
num = int(input('Enter number: '))

# Dictionaries with int as key, and values as Roman number representation
ones = {
    1: 'I', 2: 'II', 3: 'II', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 0: ''
}

tens = {
    1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L',
    6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC', 0: ''
}

hundreds = {
    1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D',
    6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM', 0: ''
}

# Function breaking number into seperate digits and returning appropriate phrase
def phrase(num):
    huns_digit = num//100
    tens_digit = (num%100)//10
    ones_digit = num%10
    phrase = f'{hundreds[huns_digit]}{tens[tens_digit]}{ones[ones_digit]}'
    
    if num == 0:
        return f'{num} does not exist in Roman Numerals'
    else:    
        return phrase

phrase(num)
# Input number returned as a phrase
print(f"{num} translates to {phrase(num)} in Roman Numerals")
