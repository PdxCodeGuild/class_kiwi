# Lab 6: Credit Card Validation
# Let's write a function credit_card_validator which returns whether a string containing
# a credit card number is valid as a boolean. The steps are as follows:

# Step 1) Convert the input string into a list of ints

user_credit_card = list(input('Please enter your credit card info: '))
# print (user_credit_card)

# Step 2) Slice off the last digit. That is the check digit.

check_digit = (int(user_credit_card.pop()))

# print(user_credit_card)
# print(check_digit)

# Step 3) Reverse the digits.
user_credit_card.reverse()

# print(user_credit_card)
# Step 4) Double every other element in the reversed list (starting with the first number in the list).

doubled_digits_rev_list = []

for index, digit in enumerate (user_credit_card):
        if index % 2 == 0:
            doubled_digit = int(digit)*2
# Subtract nine from numbers over nine.
            if doubled_digit> 9:
                doubled_digit = doubled_digit - 9

            doubled_digits_rev_list.append(int(digit)*2)
        else:
            doubled_digits_rev_list.append(int(digit))

# print(doubled_digits_rev_list)
# Sum all values.
total = (int(sum(doubled_digits_rev_list)) + check_digit)
# print(total)
string_total = str(total)
# Take the second digit of that sum.
new_list = list(string_total)
# print(user_credit_card)

if len((user_credit_card)) < 15:
    print('Invalid credit card number. Try again.')

if (string_total[1]) == str(check_digit):
     print(f'{user_credit_card} is a valid credit card number.')
else:
     print('Invalid credit card number. Try again.')
# If that matches the check digit, the whole card number is valid.



# Here is a valid credit card number to test with: 4556737586899855

# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# True Valid!