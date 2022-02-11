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
        user_credit_card = input('Enter your credit card: ')
        user_error = input(f'Is this correct? {user_credit_card}')
        if user_error.title() == 'Yes':
            break
    credit_card_list = []
    for num in user_credit_card:
        credit_card_list.append(int(num))
    return credit_card_list


credit_card = credit_card_num()

# removing the last digit
last_num_credit = credit_card.pop()

# reversing the list
credit_card[::-1]

# for num in credit_card[::2]:

print(credit_card, last_num_credit)


"""
# def credit_card_num():
#     user_credit_card = ''
#     credit_card_list = []
#     user_credit_card = input('Enter your credit card num')

#     for num in user_credit_card:
#         credit_card_list.append(num)
#     return(credit_card_list)
# """
