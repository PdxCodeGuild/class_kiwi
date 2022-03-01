# Credit Card Validator

"""
Let's write a function credit_card_validator which returns whether a string containing 
a credit card number is valid as a boolean. The steps are as follows:
"""
card_no = '4556737586899855'


def credit_card_validator():
    # Convert the input string into a list of ints

    # ---- option 1 -----
    c_card = []
    for char in card_no:
        c_card.append(int(char))

    # ---- option 2 -----
    # c_card = list(card_no)
    # for i in range(len(c_card)):
    #     c_card[i] = int(card_no[i])

    # ---- option 3 -----
    # list_cc = [int(char) for char in card_no]

    # ---- option 4 ----
    # mapped_cc = map(int, card_no)
    # print(mapped_cc)
    # list_cc = list(mapped_cc)
    # print(list_cc)

    # Slice off the last digit. That is the check digit.
    check_digit = c_card.pop()

    # Reverse the digits.
    # --- option 1 --- slicing
    c_card = c_card[::-1]

    # --- option 2 --- .reverse()
    # c_card.reverse()

    # --- option 3 --- reversed()
    # c_card = list(reversed(c_card))
    # print(c_card)

    # Double every other element in the reversed list (starting with the first number in the list).
    # --- option 1 ---
    for index, value in enumerate(c_card):
        if index % 2 == 0:
            c_card[index] = value * 2

    # --- option 2 ---
    # for x in range(0, len(c_card), 2):
    #     c_card[x] += c_card[x]
    # print(c_card)

    # --- option 3 ---
    # c_card[::2] = [2 * i for i in c_card[::2]]

    # Subtract nine from numbers over nine.
    for index, value in enumerate(c_card):
        if value > 9:
            c_card[index] = value - 9

    # c_card = [n - 9 if n > 9 else n for n in c_card]

    # Sum all values.
    total = sum(c_card)

    # Take the second digit of that sum.
    last_digit = total % 10

    # If that matches the check digit, the whole card number is valid.
    if last_digit == check_digit:
        return True
    else:
        return False


print(credit_card_validator())
