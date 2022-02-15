import math

card_number = input('Please enter your credit card number: ')

number_list = list(card_number)
number_list2 = []

for number in number_list:
    number_list2.append(int(number))

check_digit = number_list2.pop(-1)
number_list2.reverse()


multiply_list = []
check_list = []

for i in number_list2[1::2]:
    check_list.append(i)

multiply_list = [i*2 for i in number_list2[::2]]


minus_list = []

for i in multiply_list:
    if i > 9:
        new_num = i - 9
        minus_list.append(new_num)
    else:
        new_num = i
        minus_list.append(new_num)

for i in minus_list:
    if i <= 9:
        check_list.append(i)
test = sum(check_list)
validation_number = sum(check_list) % 10

if validation_number == check_digit:
    print("Credit card number is valid.")
else:
    print("Credit card number is not valid.")

print(number_list2)
print(multiply_list)
print(minus_list)
print(check_list)
print(test)
print(validation_number)