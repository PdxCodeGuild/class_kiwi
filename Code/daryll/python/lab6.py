cc_input = list(input("Please enter your credit card number: "))
credit_card = []
double_cc = []
minus_9cc = []
# Turns credit card number from cc_input into an integer and creates a new list credit_card
for i in cc_input:
    i = int(i)
    credit_card.append(i)

cc_validation = credit_card.pop(-1) # Removes last digit in credit card and stores it in cc_validation
credit_card.reverse() # Reverses the credit card numbering
# Enumerates index and value in credit_card and doubles the value on every other index and creates a new list double_cc
for x, y in enumerate(credit_card):
    if x % 2 == 0:
        y = y * 2
        double_cc.append(y)
    else:
        double_cc.append(y)
# If the value in double_cc is over 9 then subtract 9 from the value and create a new list called minus_9cc
for x in double_cc:
    if x > 9:
        x = x - 9
        minus_9cc.append(x)
    else:
        minus_9cc.append(x)
# Sum of all the values in minus_cc
sum_cc = 0
for x in minus_9cc:
    sum_cc += x
# Compares the value of the last number in the credit card to the value of the last number in the sum of the credit card    
cc_digit = sum_cc % 10
# Prints True of the credit card number is valid
print(cc_validation == cc_digit, "Valid!")