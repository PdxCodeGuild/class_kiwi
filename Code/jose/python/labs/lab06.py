
# Credit card validator

card_no = '4556737586899855'
# Convert the input string into a list of ints


def ccv():

    # option 1----------------------------------------
    c_card = []
    for char in card_no:
        c_card.append(int(char))

    # print(c_card)

    # OPTION 2 ------------------------------------------------
    # c_card = list(card_no)
    # for card in c_card:
    #     c_card.append(int(card))

    # print(c_card)
    # OPTION 3---------------------------------------

    # list_cc = [int(x) for x in card_no]
    # print(list_cc)

    # OPTION 4---------------------------------------------------

    # list_cc = list(map(int, card_no))
    # print(list_cc)

    # Slife off the last digit. That is the check digit.
    check_digit = c_card.pop()
    # print(c_card)
    # print(check_digit)
    #
    # Option 1 ------------------------- slicing
    # Reverse the digit.
    c_card = c_card[::-1]

    # OPTION 2 ----------------------------------.reverse()
    # c_card.reverse()
    # print(c_card)

    # OPTION 3 --------------------------------------reversed()     function
    # c_card = list(reversed(c_card))
    # print(c_card)

    # Double every other element in the reversed list (starting witht he first number in the list.)
    # Option 1

    for index, value in enumerate(c_card):
        if index % 2 == 0:
            c_card[index] = value * 2

    # Subtract nine from numbers over nine.

    for index, value in enumerate(c_card):
        if value > 9:
            c_card[index] = value - 9

    # Sum all values.
    total = sum(c_card)

    # Take the second digit of that sum.
    last_digit = total % 10
    print(last_digit)

    # If that matches the check digit, the whole card number is valid.
    if last_digit == check_digit:
        print("Valid credit card")
        return True
    else:
        print("Invalid card number")
        return False


ccv()
