"""
1. Convert the input string into a list of ints
2. Slice off the last digit. That is the check digit.
3. Reverse the digits.
4. Double every other element in the reversed list (starting with the first number in the list).
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.
"""
current_card = "4556737586899855"
# collecting credit card number from user


# def valid_cc(input):
#     while True:
#         credit_card = input("Please enter in a credit card number: ")
#         if range(len(credit_card)) < 17 and range(len(credit_card)) > 15:
#             return credit_card
#         else:
#             return "Invalid credit card number, please enter a valid credit card number"


def credit_card_validator(credit_card):
    # slicing off last number from credit card
    sliced_cc = current_card[-1:]
    print(f"sliced cc: {sliced_cc}")

    # reversing the order of the credit card
    reverse_cc = credit_card[::-1]
    print(f"reversed cc: {reverse_cc}")

    # doubling the second number in the reversed credit card order
    double_num = []
    # for i in range(len(reverse_cc)):
    #     if i % 2 == 0:
    #         double = int(reverse_cc[i]) * 2
    #         double_num.append(double)
    # return double_num

    for i, value in enumerate(reverse_cc):
        if i % 2 == 0:
            double = int(reverse_cc[i]) * 2
            double_num.append(double)
        else:
            same = int(reverse_cc[i])
            double_num.append(same)
    print(f"numbers doubled: {double_num}")

    # subtracting 9 from every number over 9 in list
    sub_num = []
    for i in range(len(double_num)):
        if double_num[i] > 9:
            sub = double_num[i] - 9
            sub_num.append(sub)
        else:
            no_change = int(double_num[i])
            sub_num.append(no_change)
    print(f"subtracted numbers: {sub_num}")

    # calculating the total of the remaining numbers in credit card
    total = []
    for i, value in enumerate(sub_num):
        if sub_num[i] >= 0:
            i += i
        total = sum(sub_num)
    print(f"total: {total}")

    # total_second_digit = total.split()
    separate = str(total)
    two_split = []
    for i in separate:
        two_split = list(separate.split(i))
        two_split.append(i)
    print(f"second digit: {two_split[-1]}")

    # if total_second_digit == sliced_cc:
    #     print(f"valid {total_second_digit} = {sliced_cc}")
    if two_split[-1] == sliced_cc:
        # return "card valid {two_split[-1]} == {sliced_cc}"
        return True
    else:
        return False


print(credit_card_validator(current_card))
