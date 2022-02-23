## convert a digit into a word

#version 1
#hint from lab
# x = int()
# tens_digit = x//10
# ones_digit = x%10

#word conversion dictionaries
tens = {
    1 : "Ten",
    2 : "Twenty",
    3 : "Thirty",
    4 : "Forty",
    5 : "Fifty",
    6 : "Sixty",
    7 : "Seventy",
    8 : "Eighty",
    9 : "Ninety",
}

ones = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine" 
}

teens = {
    0 : "Ten",
    1 : "Eleven",
    2 : "Twelve",
    3 : "Thirteen",
    4 : "Fourteen",
    5 : "Fifteen",
    6 : "Sixteen",
    7 : "Seventeen",
    8 : "Eighteen",
    9 : "Nineteen" 
}
# def function for process
# def phrase(num):
#     '''Will convert number input into words'''
    
#     #split the number to places
#     tens_digit = num//10
#     ones_digit = num%10

#     #create statements to identify path of number
#     if tens_digit > 0 and ones_digit == 0:
#         return tens[tens_digit]

#     elif tens_digit == 1 and ones_digit > 0:
#         return teens[ones_digit]

#     elif tens_digit > 1 and ones_digit > 0:
#         return tens[tens_digit] + '-' + ones[ones_digit]

#     elif tens_digit ==0 and 0 <= ones_digit <=9:
#         return ones[ones_digit]

# print("Please enter a number: ")
# print(phrase(int(input())))

#version 2

hundreds = {
    1 : "One hundred",
    2 : "Two Hundred",
    3 : "Three Hundred",
    4 : "Four Hundred",
    5 : "Five Hundred",
    6 : "Six Hundred",
    7 : "Seven Hundred",
    8 : "Eight Hundred",
    9 : "Nine Hundred"
}

def hundos(num):
    '''Will convert numbers input into words'''
    
    #split the number to places
    hundreds_digit = num//100
    tens_digit = num//10
    ones_digit = num%10
   
    #create statements to identify path of number

    if hundreds_digit >= 1:
        tened = num - (hundreds_digit * 100)
        tens_digit = tened//10
        ones_digit = tened%10
        
        if tens_digit == 0 and ones_digit == 0:
            return hundreds[hundreds_digit]

        elif tens_digit > 1 and ones_digit == 0:
            return hundreds[hundreds_digit] + ' and ' + tens[tens_digit]
        
        elif tens_digit >= 0:
            return hundreds[hundreds_digit] + ' and ' + teens[ones_digit]

        elif tens_digit > 1 and ones_digit > 0:
            return hundreds[hundreds_digit] + ' and ' + tens[tens_digit] + '-' + ones[ones_digit]
    
    elif hundreds_digit < 1:
    
        if tens_digit > 0 and ones_digit == 0:
            return tens[tens_digit]

        elif tens_digit == 1 and ones_digit > 0:
            return teens[ones_digit]

        elif tens_digit > 1 and ones_digit > 0:
            return tens[tens_digit] + '-' + ones[ones_digit]

        elif tens_digit == 0 and 0 <= ones_digit <=9:
            return ones[ones_digit]
        
    

print("Please enter a number: ")
print(hundos(int(input())))
