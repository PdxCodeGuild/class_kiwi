# Lab 3: Number To Phrase
# Version 1

# creating dictionary for conversion
first_number = {
    "1": "Ten",
    "2": "Twenty",
    "3": "Thirty",
    "4": "Forty",
    "5": "Fifty",
    "6": "Sixty",
    "7": "Seventy",
    "8": "Eighty",
    "9": "Ninety",
    "0": "Zero"
}
teen_number = {
    "1": "Eleven",
    "2": "Twelve",
    "3": "Thirteen",
    "4": "Fourteen",
    "5": "Fifteen",
    "6": "Sixteen",
    "7": "Seventeen",
    "8": "Eighteen",
    "9": "Nineteen"
}
second_number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": ""
}
hundred_number = {
    "1": "One Hundred",
    "2": "Two Hundred",
    "3": "Three Hundred",
    "4": "Four Hundred",
    "5": "Five Hundred",
    "6": "Six Hundred",
    "7": "Seven Hundred",
    "8": "Eight Hundred",
    "9": "Nine Hundred"
}

# user providing number to convert
user_input = input("Please provide a number to convert to its english representation: ")
user = []
for i in user_input:
    user.append(i)
original_number = int(user_input)



# Version 1 formulas for creating conversion
if len(user_input) < 3:
    tens_digit = original_number // 10
    ones_digit = original_number % 10
    tens = str(tens_digit)
    ones = str(ones_digit)
    if len(user_input) < 2:
        teen = user[0]
    else:
        teen = user[1]
    
# Version 2 formulas for creating conversion
if len(user_input) > 2:
    hundred_digit = original_number // 100
    new_tens_digit = (original_number // 10) % 10
    hundred = str(hundred_digit)
    new_tens = str(new_tens_digit)
    teen = user_input[2]
    teen_num = original_number % 100



def conversion(number):
     # converting number if 0 - 10
    if tens == "0":
        # ones == second_number[ones]
        return f"You entered {user_input} which converts to {second_number[ones]}"
    # converting number 11 - 19
    if int(user_input) > 10 and int(user_input) < 20:
        return f"You entered {user_input} which converts to {teen_number[teen]}"
        
    elif tens in first_number and ones in second_number:
        return f"You entered {user_input} which converts to {first_number[tens]} {second_number[ones]}"
    

    # Version 2
def hundred_conversion(number):
    # converting number if range 111 - 119
    if hundred in hundred_number and teen_num > 10 and teen_num < 20:
        return f"You entered {user_input} which converts to {hundred_number[hundred]} {teen_number[teen]}"
    
    elif hundred in hundred_number and new_tens == "0" and teen == "0":
        return f"You entered {user_input} which converts to {hundred_number[hundred]}"
    
    # converting number if 100+
    elif hundred in hundred_number:
        return f"You entered {user_input} which converts to {hundred_number[hundred]} {first_number[new_tens]} {second_number[teen]}"
    

if len(user_input) < 3:
    print(conversion(original_number))
else:
    print(hundred_conversion(original_number))