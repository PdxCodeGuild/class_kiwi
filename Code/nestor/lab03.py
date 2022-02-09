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
    "9": "Ninety"
}
teen_number = {
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen", 
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen"
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
    "9": "Nine"
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
num_list = []

#user providing number to convert
user_input = input("Please provide a number to convert to its english representation: ")
original_number = int(user_input)
num_list = list(user_input)

                 
# Version 1 formulas for creating conversion
tens_digit = original_number // 10
ones_digit = original_number % 10
tens = str(tens_digit)
ones = str(ones_digit)

# Version 2 formulas for creating conversion
hundred_digit = original_number // 100
new_tens_digit = (original_number // 10) % 10
hundred = str(hundred_digit)
new_tens = str(new_tens_digit)

# converting number if in teen range 11 - 19
if tens == "1" and ones == "1":
    print(f"You entered {user_input} which converts to {teen_number['11']}")
elif tens == "1" and ones == "2":
    print(f"You entered {user_input} which converts to {teen_number['12']}")
elif tens == "1" and ones == "3":
    print(f"You entered {user_input} which converts to {teen_number['13']}")
elif tens == "1" and ones == "4":
    print(f"You entered {user_input} which converts to {teen_number['14']}")
elif tens == "1" and ones == "5":
    print(f"You entered {user_input} which converts to {teen_number['15']}")
elif tens == "1" and ones == "6":
    print(f"You entered {user_input} which converts to {teen_number['16']}")
elif tens == "1" and ones == "7":
    print(f"You entered {user_input} which converts to {teen_number['17']}")
elif tens == "1" and ones == "8":
    print(f"You entered {user_input} which converts to {teen_number['18']}")
elif tens == "1" and ones == "9":
    print(f"You entered {user_input} which converts to {teen_number['19']}")

# converting number if 0 - 10 
elif tens == "0" and ones == "1":
    print(f"You entered {user_input} which converts to {second_number['1']}")
elif tens == "0" and ones == "2":
    print(f"You entered {user_input} which converts to {second_number['2']}")
elif tens == "0" and ones == "3":
    print(f"You entered {user_input} which converts to {second_number['3']}")
elif tens == "0" and ones == "4":
    print(f"You entered {user_input} which converts to {second_number['4']}")
elif tens == "0" and ones == "5":
    print(f"You entered {user_input} which converts to {second_number['5']}")
elif tens == "0" and ones == "6":
    print(f"You entered {user_input} which converts to {second_number['6']}")
elif tens == "0" and ones == "7":
    print(f"You entered {user_input} which converts to {second_number['7']}")
elif tens == "0" and ones == "8":
    print(f"You entered {user_input} which converts to {second_number['8']}")
elif tens == "0" and ones == "9":
    print(f"You entered {user_input} which converts to {second_number['9']}")
elif tens == "1" and ones == "0":
    print(f"You entered {user_input} which converts to {first_number['1']}")
    

# converting number if 20 - 90 ish
elif tens == "2": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['2']}-{second_number[ones]}")
elif tens == "3": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['3']}-{second_number[ones]}")
elif tens == "4": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['4']}-{second_number[ones]}")
elif tens == "5": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['5']}-{second_number[ones]}")
elif tens == "6": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['6']}-{second_number[ones]}")
elif tens == "7": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['7']}-{second_number[ones]}")
elif tens == "8": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['8']}-{second_number[ones]}")
elif tens == "9": 
    second_num = second_number[ones]
    print(f"You entered {user_input} which converts to {first_number['9']}-{second_number[ones]}")
    
# Version 2
# converting number if 100+
elif hundred == "1": 
    print(f"You entered {user_input} which converts to {hundred_number['1']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "2": 
    print(f"You entered {user_input} which converts to {hundred_number['2']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "3": 
    print(f"You entered {user_input} which converts to {hundred_number['3']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "4": 
    print(f"You entered {user_input} which converts to {hundred_number['4']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "5": 
    print(f"You entered {user_input} which converts to {hundred_number['5']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "6": 
    print(f"You entered {user_input} which converts to {hundred_number['6']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "7": 
    print(f"You entered {user_input} which converts to {hundred_number['7']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "8": 
    print(f"You entered {user_input} which converts to {hundred_number['8']} {first_number[new_tens]}-{second_number[ones]}")
elif hundred == "9": 
    print(f"You entered {user_input} which converts to {hundred_number['9']} {first_number[new_tens]}-{second_number[ones]}")