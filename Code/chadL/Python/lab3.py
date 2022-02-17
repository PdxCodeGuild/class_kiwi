#Lab 3: Number to Phrase
    #version 1
"""  
ones_dict = {
    "0": " ",
    "1": "one", 
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

tens_dict  = {
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",    
}

i = int(input("enter a numerical number to get your spoken number. "))

def answer(i):
    if i > 19:
        tens_digit = i//10
        ones_digit = i%10
        tens_digit = str(tens_digit)
        ones_digit = str(ones_digit)
        p = tens_dict[tens_digit]
        y = ones_dict[ones_digit]
        print(p, y)
    elif i < 20:
        i = str(i)
        p = ones_dict[i]
        print(p)
     
answer(i)
"""

#  #  #                                      Version 2                           ###



ones_dict = {
    "0": " ",
    "1": "one", 
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

tens_dict  = {
    "0": "and",
    "1": " ",
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",    
}
hundreds_dict = {
    "1": "one hundred",
    "2": "two hundred",
    "3": "three hundred",
    "4": "four hundred",
    "5": "five hundred",
    "6": "six hundred",
    "7": "seven hundred",
    "8": "eight hundred",
    "9": "nine hundred",
}

i = int(input("enter a numerical number to get your spoken number. "))     #user tpyes in number to receive words

def answer(i):                                                # function to split numbers for proccessing into words
    if i > 19 and i < 100:                                        # if statement to catch numbers more than 20
        tens_digit = i//10
        ones_digit = i%10
        tens_digit = str(tens_digit)
        ones_digit = str(ones_digit)
        p = tens_dict[tens_digit]
        y = ones_dict[ones_digit]
        print(p, y)
    elif i < 20:                        # if statement to hit the teens
        i = str(i)
        p = ones_dict[i]
        print(p)
    elif i > 99:
        ones_digit = i%10
        tens_digit = i//10
        
        hundreds_digit = tens_digit//10
        tens_digit = tens_digit%10
        
        ones_digit = str(ones_digit)
        tens_digit = str(tens_digit)
        hundreds_digit = str(hundreds_digit)
        if tens_digit == "1":
            print(hundreds_dict[hundreds_digit] + ones_dict[tens_digit + ones_digit]) 
                
        j = ones_dict[ones_digit]
        h = tens_dict[tens_digit]
        k = hundreds_dict[hundreds_digit]
        #print(ones_dict, tens_dict, hundreds_digit )
        #print(tens_digit + ones_digit )
        #print(tens_digit)
        #print(hundreds_digit)
        print(k,h,j)
answer(i)
