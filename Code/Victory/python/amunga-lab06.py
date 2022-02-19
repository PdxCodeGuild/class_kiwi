#Create an input for the credit card.

credit_num = list(input('Please enter the credit number: '))

check_digit = credit_num.pop()
credit_num.reverse

values_of_cards = []

for i, num in enumerate(credit_num):

    if i % 2 == 0:
        double_digits = int(num) * 2
        if double_digits > 9:
            double_digits=double_digits - 9
        
        values_of_cards.append(double_digits)
    else:
        values_of_cards.append(int(num))

sum_of_values = sum(values_of_cards)

if sum_of_values % 10 == int(check_digit):
    print(f"Your card is a valid credit number.")
else:
    print(f"Your card is not a valid credit number.")


