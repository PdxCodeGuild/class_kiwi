# VERSION 1


#input to collect users number
num = int(input("give me a number: "))


# 3 seprate lists holding all the numbers
tens_list = [" ", "teens", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
ones_list = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
below_twenty_list = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


#a funtion that processes numbers 20-99
def cal(num):
        tens = num//10
        ones = num%10
        tens_string = tens_list[tens]
        ones_string = ones_list[ones]
        print(tens_string, ones_string)


#a function that processes numbers 1-19
def cal_2(num):
    answer = below_twenty_list[num]
    print(answer)



#if statement that calls either funtion to deal with 1-19 or 20-99
if num > 19:

    cal(num)

elif num < 20:

    cal_2(num)








# VERSION 2


#input to collect users number
num = int(input("give me a number: "))


# 3 seprate lists holding all the numbers
hundreds_list = [" ", "One Hundred", "Two Hundred", "Three Hundred", "Four Hundred", "Five Hundred", "Six Hundred", "Seven Hundred", "Eight Hundred", "Nine Hundred"]
tens_list = [" ", "teens", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
below_twenty_list = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


#a funtion that processes numbers 20-99
def cal(num):
        tens = num//10
        ones = num%10
        tens_string = tens_list[tens]
        ones_string = below_twenty_list[ones]
        print(tens_string, ones_string)


#a function that processes numbers 1-19
def cal_20(num):
    answer = below_twenty_list[num]
    print(answer)


# a funtion that processes numbers 100-999 (thing one was a pain)
def cal_100(num):
    tens = num//10
    ones = num%10

    hundreds = tens//10
    new_tens = tens%10
    hundreds_string = hundreds_list[hundreds]
    if new_tens < 2:
        less_then_20 = str(new_tens) + str(ones)
        less_then_20 =  int(less_then_20)
        tens_string = below_twenty_list[less_then_20]
        print(hundreds_string, tens_string )

    elif new_tens >= 2:
        tens_string = tens_list[new_tens]
        ones_string = below_twenty_list[ones]
        print(hundreds_string, tens_string, ones_string)
    


#if statement that calls between 3 funtions that deal with numbers ranging from 1-19, 20-99, 100-999
if num > 19 and num < 100:

    cal(num)

elif num < 20:

    cal_20(num)

elif num > 99:

    cal_100(num)


