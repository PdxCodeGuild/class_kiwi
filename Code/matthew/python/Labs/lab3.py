'''
Lab 3 
Number to phrase
'''
# -- Version 1 
'''
Im having a lot of issues with my python, the code will run as I have it then randomly return an
error. Even if no code or variables have changed. For example I was running 61. I got sixty-one, sixty-one, KeyError: 6.
Sometimes my if statements will run like " if 10 >= x <= 12" and sometimes I have to change it to "if x >= 10 and x < 13".
Again not chaning anything just running the code. If I dont change the code it will either skip over the code even if the variables 
fit the if statement or the opposite. 

'''



def num_to_phrase(x: int ) -> str: 
    '''
    Convertring numbers(int) into text(str) EX: 99 to ninety-nine
    '''
    numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 0:'Zero'}
    tens = {1: 'Ten', 2: 'Twenty', 3: 'Thirty', 5 : 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
    teens = {1:'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'}
    hundreds = {1: 'One Hundred and ', 2: 'Two Hundred and ', 3: 'Three Hundred and ', 4: 'Four Hundred and ', 5: 'Five Hundred and ', 
    6: 'Six Hundred and ', 7: 'Seven Hundred and ', 8: 'Eight Hundred and ', 9: 'Nine Hundred and '}
    hundredth_digit = x//100
    tens_digit = (x//10) - (hundredth_digit * 10)
    ones_digit = x%10
    # tens_digit_str = ''
    # ones_digit_str = ''
    
    tens_digit_str = tens[tens_digit]
    ones_digit_str = numbers[ones_digit]
    if x <= 99: # if x is under 99
        if x == 10: # checking to see if x is 10
            return tens_digit_str
        elif ones_digit == 0: # checking to see if x = x0
            return tens_digit_str
        elif 11 <= x <= 19: # checking to see if x is a teen
            return teens[ones_digit]
        else: # all other values of xx
            return tens_digit_str + '-' + ones_digit_str     
    elif x >= 100: # --- Version 2
        hundredth_str = hundreds[hundredth_digit] # creating a hundreth str
        if tens_digit == 1 and ones_digit == 0: # checking for x10
            return hundredth_str + tens_digit_str
        elif tens_digit == 1 and ones_digit != 0: # checking for x13-x19 (teens)
            return hundredth_str + teens[ones_digit]
        elif ones_digit == 0: # checking for xx0
            return hundredth_str + tens[tens_digit]
        else: # all other values of xxx
            return hundredth_str + tens[tens_digit] + '-' + numbers[ones_digit]


# print(num_to_phrase(118))
# print(num_to_phrase(20))
# print(num_to_phrase(156))
# print(num_to_phrase(87))


