one_digits ={
    1: "one", 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight',
    9: 'nine'
}
#The unequal string of 10-19 means typing the hardway

firs_tens ={
    10:'ten', 11:'eleven', 12: 'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
    16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'
}
# given that 'num // 10' equals to a single digit of 2 to 9, each number below is a rep of that by 10.

sec_tens = {
    2:'twenty-', 3:'thirty-', 4:'forty-', 5:'fifty-', 6:'sixty-', 7:'Seventy-',
    8:'eighty-', 9:'ninety-'
}

hund_reds = {
    1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5:'five hundred', 6:'six hundred',
    7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'
}

sec_hundreds = {
    20:'twenty ', 30:'thirty ', 40:'forty ', 50:'fifty ', 60:'sixty ', 70:'Seventy ',
    80:'eighty ', 90:'ninety '
}

numb = int(input('Please enter a number: '))

floor_hun = numb // 100
modulo_hun = numb % 100
tens_digit = numb // 10
ones_digit = numb % 10
tens_mod = modulo_hun//10
'''
if modulo_hun == 0:
    print(hund_reds[floor_hun])
elif 1<= modulo_hun <= 99:
    if 1<= modulo_hun < 10:
        ones_hundred = hund_reds[floor_hun]+ ' and ' + one_digits[modulo_hun]
        print(ones_hundred)
    elif 10<= modulo_hun <= 19:
        tens_hundred = hund_reds[floor_hun]+ ' and ' + firs_tens[modulo_hun]
        print(tens_hundred)
    
    elif 20<= modulo_hun <= 99:
        if tens_digit == 0:
            sec_tens_hundred = hund_reds[floor_hun] + ' and ' + sec_hundreds[modulo_hun]
            print(sec_tens_hundred)
        
        else:
            sec_tens_hundred = hund_reds[floor_hun] + sec_hundreds[modulo_hun] + one_digits[ones_digit]

        #else:
            #sec_tens_hundred = hund_reds[floor_hun] + ' and ' + sec_hundreds[modulo_hun] + one_digits[ones_digit]
            #print(sec_tens_hundred)



'''
if modulo_hun == 0:
    new_hunds =hund_reds[floor_hun]
    print(new_hunds)
    #new_hunds = hund_reds[modulo_hun] +' and ' + sec_hundreds[modulo_hun]
elif 1<= modulo_hun <=9:
    new_hunds =hund_reds[floor_hun] + ' and ' + one_digits[modulo_hun]
    print(new_hunds)
elif 10<= modulo_hun <=19:
    new_hunds =hund_reds[floor_hun] + ' and ' + firs_tens[modulo_hun]
    print(new_hunds)
elif 20 <= modulo_hun <= 99:
    if ones_digit == 0:
        new_hunds =hund_reds[floor_hun] + ' and ' + sec_hundreds[modulo_hun]
        print(new_hunds)
    else:
        new_hunds =hund_reds[floor_hun] + ' and ' + sec_tens[tens_mod] + one_digits[ones_digit]
        print(new_hunds)







        
    