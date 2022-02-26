"""
Credit Card Validation
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/11/2022
"""

test_list = '4556737586899855'
user_input = input("Please enter your Credit Card number.")
list_cc = [int(x) for x in user_input]
# print(list_cc)



check_digit = list_cc.pop()


# print()

# step2_list_cc = slice(0,15)

step_2 = list_cc

# print(step_2)

step_3 = step_2.copy()
step_3.reverse() 

# print(step_3)

# print(step3_list_cc)

step_4 = step_3.copy()

for counter, ccnum in enumerate(step_4):
    if counter%2 == 0 :
        step_4[counter] *= 2
        


step_5 = step_4.copy()

# print(step_4)

for counter, ccnum in enumerate(step_5):    
    if ccnum > 9:
        step_5[counter] -= 9

# print(step_5)
step_6 = step_5.copy()
step_6 = sum(step_5)

# print(step_6)

def get_second_digit(digi_input):
    str_input = str(digi_input)
    lst_input = [int(x) for x in str_input]
    if len(lst_input) > 1:
        last_digi = lst_input[1]
    if  len(lst_input) <= 1:
        last_digi = None
    
    
    return last_digi

step_7 = get_second_digit(step_6)    
# print(step_7)
validation = step_7 == check_digit

print(validation)

# print(check_digit)

