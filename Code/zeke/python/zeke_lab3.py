#convert a number(67) into its worded form 'sixty-seven' O-99


# # plus_twenty ={}

# # while a 
 
# # 20 // 10
# thirty = 300// 10 
# twenty = 200// 10

# if 300//10 == [30]:
#     print(f'thirty')
#     input(30)


# while twenty <

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
}
msc ={
    0:'',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy', 
    8: 'eighty',
    9: 'ninety',
}

hundred = {
    1 : 'onehundred',
    2 : 'twohundred',
    3 : 'threehundred',
    4 : 'fourhundred',
    5 : 'fivehundred',
    6 : 'sixhundred',
    7 : 'sevenhundred',
    8 : 'eighthundred',
    9 : 'ninehundred',
    }
num = int(input("Please enter a number here: " ))

if num <= 19:
    print(f'{numbers[num]}')

elif num <100:
    ones_digit = num%10#84 % 10 = 4      144 % 10 = 4
    tens_digit = num//10#84 // 10 = 8     144 // 10 = 14    144 /10 =14.4
    print(f'{msc[tens_digit]}{numbers[ones_digit]}')


    # print(f'{msc[tens_digit]}{numbers[ones_digit]}')
    if ones_digit == 0:
        print(f'{msc[tens_digit]}')
    else:
        print(f'{msc[tens_digit]}{numbers[ones_digit]}')
        
#num = 569//100 = 5         569 % 100= 69 

elif num >=100:
    tens_digit = num //10
    ones_digit = num % 10
    hundred_digit = num // 100
    x = tens_digit %10
    if ones_digit == 0:
        print(f'{hundred[hundred_digit]}{msc[x]}')
    else:    
        print(f'{hundred[hundred_digit]}{msc[x]}{numbers[ones_digit]}')



# if num >=100:

   
    # print(f'{msc[tens_digit]}{numbers[ones_digit]}')
# print("x =", x) # 569 // 10
# print("tens_digit", tens_digit)
  
# print(num%1000)
# print(num //100)
# hundreds = num //100

# print(numbers[hundreds])


    # elif num < 100:
    #     print 

    

#################################################################################

#convert a number(67) into its worded form 'sixty-seven' O-99
# Handle numbers from 100-999.


   
# print(test_word)

# print(zero_19[])
# user_input =int(input(f'pick a number between 0-99? '))
# print(numbers[user_input])
# if user_input in numbers:
#     a = user_input % 10
#     print(a)




# print(plus_twenty[user_input])
# # print(plus_twenty[20])
# # print(plus_twenty['twenty')



#################################################################################

# practice on lab

