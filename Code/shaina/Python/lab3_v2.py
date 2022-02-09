# Lab 3: Version 2 ---- Handles numbers 100-999
'''
The biggest change on this version is adding a 'hundreds' dictionary
and adding to function to seperate and return appropriate function
'''
# Number is input
num = int(input('Enter number: '))

# Dictionaries with int as key, and values as english representation
ones = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: ''
}

tens = {
    1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
    6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety', 0: ''
}

hundreds = {
    1: 'One Hundred', 2: 'Two Hundred', 3: 'Three Hundred', 4: 'Four Hundred', 5: 'Five Hundred',
    6: 'Six Hundred', 7: 'Seven Hundred', 8: 'Eight Hundred', 9: 'Nine Hundred', 0: ''
}

# Function breaking number into seperate digits and returning appropriate phrase
def phrase(num):
    huns_digit = num//100
    tens_digit = (num%100)//10
    ones_digit = num%10
    phrase = f'{hundreds[huns_digit]} {tens[tens_digit]} {ones[ones_digit]}'
    
    if ones_digit == 0 and tens_digit == 0 and huns_digit == 0:
        return 'Zero'
    if tens_digit == 1 and ones_digit == 1:
        return f'{hundreds[huns_digit]} Eleven'
    elif tens_digit == 1 and ones_digit == 2:
        return f'{hundreds[huns_digit]} Twelve'
    elif tens_digit == 1 and ones_digit == 3:
        return f'{hundreds[huns_digit]} Thirteen'
    elif tens_digit == 1 and 3 < ones_digit <= 9:
        return f'{hundreds[huns_digit]} {ones[ones_digit]}teen'
    else:    
        return phrase

phrase(num)
# Input number returned as a phrase
print(f"You've entered {phrase(num)}")
