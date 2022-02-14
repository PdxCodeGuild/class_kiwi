"""
Credit Card Validation
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/11/2022
"""

user_input = '4556737586899855'
list_cc = [int(x) for x in user_input]
# print(list_cc)

check_digit = slice(15,16)
# print(list_cc[check_digit])
step2_list_cc = slice(0,15)

# print(list_cc[step2_list_cc])

