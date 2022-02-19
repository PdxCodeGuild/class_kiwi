#Lab 6: Credit Card Validation
"""
Let's write a function credit_card_validator which returns whether a string containing a credit card number is valid as a boolean. 
The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list (starting with the first number in the list).
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
True Valid!
"""



user_input = input("please enter your credit card numbers ")
user_input = list(user_input)

def card_number(user_input):
    number_list = []
    reversed_card = []
    card9 = []
    for l in user_input:
       number_list.append(int(l))
    verify_digit1 = number_list.pop()                      #taking off last digit
    
    for l in number_list[::-1]:                         #loop through reversed order
        reversed_card.append(l)
    counter = 0
    for l in reversed_card[0::2]:                   #multiply number pulled out
        num = (l*2)
        reversed_card[counter] = num
        counter +=2 
    for l in reversed_card:                     #take 9 from value if over 9
        if l > 9:
                I9 = l - 9 
                card9.append(I9)
        else:
                card9.append(l)
    card_sum = 0                        #sum of all itms
    for l in card9:
        card_sum +=l
    card_total = str(card_sum)
    check_digit = card_total[-1]
    check_digit = int(check_digit)
    
    if verify_digit1 == check_digit:
        return True
    else: 
         return False
card_number(user_input)
valid = card_number(user_input)
if valid == True:
    print("credit card is valid")
elif valid == False:
    print("number is not valid")
           


     

"""
Let's write a function credit_card_validator which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Reverse the digits.
Double every other element in the reversed list (starting with the first number in the list).
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
True Valid!

------option 1-------
card_no = '4556737586899855'
c_card = []
for char in card_no:
    c_card.append(int(char))
------option 1-------

------option 2--------------
c_card = list(card_no)
for i in range(len(c_card)):
    card[i] = int(card_no[i])
 ------option 2--------------
 
 ------- option 3 -----------
 list_cc = [int(x) for char in card_no]  
------- option 3 -----------

------option 4 -----------------
list_cc = list(map(int, card_no))
list_cc = list(mapped_cc)
------option 4 -----------------

check_digit = c_card.pop()

c_card = c_card[::-1]      or c_card.reverse()    or    c_card = list(reversed(c_card))
-----option 1---------
for index, value in enumerate(c_card):
    if num % 2 == 0:
        c_card[num] = value * 2



for index, value in enumerate(c_card):
    if value >9:
        c_card[index] = value - 9
        
or
c_card = [n-9 if n> 9 else n for n in c_card]


total = sum(c_card)

#take 2nd digit of that sum
last_digit = total % 10


if las_digit ==check_digit:

else:
    print("invalid credit card)















"""











