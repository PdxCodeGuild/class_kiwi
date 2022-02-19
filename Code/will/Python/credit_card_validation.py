import math

card_number = input('Please enter your credit card number: ')

number_list = list(card_number)
number_list2 = []

for number in number_list:
    number_list2.append(int(number))

check_digit = number_list2.pop(-1)
number_list2.reverse()

check_list = []

for index, number in enumerate(number_list2):
    if index % 2 == 0:
        double_number = number * 2
        if double_number > 9:
            sub_number = double_number -9
            check_list.append(sub_number)

        elif double_number <= 9:
            check_list.append(double_number)
    else:
        check_list.append(number)

validation_number = sum(check_list) % 10

if validation_number == check_digit:
    print("Credit card number is valid.")
else:
    print("Credit card number is not valid.")