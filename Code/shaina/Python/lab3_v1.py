# Lab 3: Version 1 ---- Handles numbers 0-99

# Number is input
num = int(input('Enter number: '))

# Dictionaries with int as key, and values as english representation
ones = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'
}

tens = {
    1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
    6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety', 0: ''
}

# Function breaking number into seperate digits and returning appropriate phrase
def phrase(num = int):
    tens_digit = num//10
    ones_digit = num%10
    phrase = tens[tens_digit] + '-' + ones[ones_digit]
    
    if ones_digit == 0 and tens_digit == 0:
        return 'Zero'
    if ones_digit == 0 and tens_digit > 0:
        return f'{tens[tens_digit]}'
    elif num == 11:
        return 'Eleven'
    elif num == 12:
        return 'Twelve'
    elif num == 13:
        return 'Thirteen'
    elif 13 < num < 20:
        return f'{ones[ones_digit]}teen'
    else:    
        return phrase

# Input number returned as a phrase
print(f"You've entered {phrase(num)}")
