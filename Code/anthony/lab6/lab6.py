# Lab6: Credit Card Validation


# Enter CC Number
credit_card_number = input("Please enter Credit Card information: ")

# create empty list
card_string = []
# convert empty string into a list of ints
for x in credit_card_number:
    card_string.append(x)
# convert strings in list to INTERGERS
for x in range(0, len(card_string)):
    card_string[x] = int(card_string[x])
# assign check digit and remove last didigt
check_digit = card_string.pop(-1)
print(card_string)
# reverse the digits
card_string.reverse()
print(card_string)
# double every other element in the reversed list
for x in range(0, len(card_string), 2):
    int(card_string[x])
    card_string[x] += card_string[x]
print(card_string)

# subtract 9 from numbers over nine
for x in range(len(card_string)):
    if card_string[x] > 9:
        card_string[x] = card_string[x]-9
print(card_string)

# sum all the values
total = sum(card_string)
print(total)

# second digit on sum
second_digit = total % 10
print(second_digit)

# boolean true prints valid
if check_digit == second_digit:
    print(True, "Valid!")
else:
    print(False, "Invalid!")
