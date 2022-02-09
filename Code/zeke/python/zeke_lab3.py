#convert a number(67) into its worded form 'sixty-seven' O-99


# # plus_twenty ={}

# # while a 
 
# # 20 // 10
# thirty = 300// 10 
# twenty = 200// 10

# if 300//10 == [30]:
#     print(f'thirty')
#     input(30)


# while tewnty <

numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',                                      
    7: 'seven',  
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy', 
    80: 'eighty',
    90: 'ninety',
}


num = 84

print(num%100)
print(num //100)
hundreds = num //100

print(numbers[hundreds])
units = num%10
print( hundreds, units)

if num <100:
    tens_digits = num //10#8
    ones_digits = num%10#4
    test_word = numbers[tens_digits] + " - " + numbers[ones_digits] # ones_digit[8],numbers [4]
print(test_word)


# print("test", numbers[14])
# print("test", numbers[70])
# print("test", numbers[80])
# print("test", numbers[351])

# # print(zero_19[])
# user_input =int(input(f'pick a number between 0-99? '))
# print(numbers[user_input])
# if user_input in numbers:
#     a = user_input % 10
#     print(a)



# print(plus_twenty[user_input])
# # print(plus_twenty[20])
# # print(plus_twenty['twenty')