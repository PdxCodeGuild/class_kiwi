card_number = input('Please enter your credit card number: ')

number_list = list(card_number)
list_to_check = []

for number in number_list:
    list_to_check.append(int(number))
print(list_to_check)
check_digit = list_to_check.pop(-1)
list_to_check.reverse()

for i in list_to_check[::2]:
    i *= 2



print(list_to_check)
print(check_digit)