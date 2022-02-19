
#Convert a number into its english representation

##>>Essentially put the string of one
num = int(input('Please provide me a number: '))

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

###>>>User puts a number then it is converted to a string

tens_digit = num//10
firs_digit = num%10


def num_to_str(num):
    '''
    Create a function that turns a user input into the string version
    '''

    if tens_digit == 0:
        return one_digits[num]
    elif tens_digit == 1:
        return firs_tens[num]
    
    elif 2<= tens_digit <= 9:
        if firs_digit ==0:
            return sec_tens[num] 
        elif 1<= firs_digit <= 9:
            new_str = sec_tens[tens_digit] + one_digits[firs_digit]

            return new_str
    
print(num_to_str(num))

        
    