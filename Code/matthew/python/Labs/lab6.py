'''
Credit Card validation

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list (starting with the first number in the list).
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.

Credit Card Num :4556737586899855
'''


def credit_card_num():
    while True:
        # getting credit card info from user
        user_credit_card = input('Enter your credit card: ')
        user_error = input(f'Is this correct? y/n {user_credit_card} ')
        if user_error.title() == 'Y':
            break
    credit_card_list = []
    # converting credit card str into a list
    for num in user_credit_card:
        credit_card_list.append(int(num))
    return credit_card_list


# creating the credit card 
# credit_card = credit_card_num()

credit_card_ex = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5] # using as an example

def credit_card_check(credit_card):
    # removing the last digit
    last_num_credit = credit_card.pop()

    # reversing the list
    credit_card =credit_card[::-1]

    # doubling every other number
    for num, value in enumerate(credit_card): # num = index position and value = position value
        if num % 2 == 0: # will check for odd and even, if it is even it will be 0.
            credit_card[num] = value * 2

    for num, value in enumerate(credit_card): 
        if value > 9:
            credit_card[num] = value - 9

    sum_credit_card = sum(credit_card)
    sum_credit_card = sum_credit_card % 10

    if sum_credit_card == last_num_credit:
        return True, print("valid")
    else: 
        return False, print('invalid')

    
credit_card_check(credit_card_ex)



"""
# def credit_card_num():
#     user_credit_card = ''
#     credit_card_list = []
#     user_credit_card = input('Enter your credit card num')

#     for num in user_credit_card:
#         credit_card_list.append(num)
#     return(credit_card_list)
# """
