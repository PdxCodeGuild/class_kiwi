# Lab 6

credit_card_number = "4556737586899855"
print("credit card number: ", credit_card_number)

# create function
def credit_card_validator(credit_card_number):

    # Convert the input string into a list of ints
    convert_to_list = list(credit_card_number)
    print("convert to list: ", convert_to_list)
    # from https://realpython.com/python-map-function/
    convert_to_int = list(map(int, convert_to_list)) 
    print("convert to integers: ", convert_to_int)
    
    # Slice off the last digit. That is the check digit.
    check_digit = convert_to_int.pop(-1)
    print("check digit: ", check_digit)

    # Reverse the digits.
    reverse_list = convert_to_int[::-1]
    print("reverse list: ", reverse_list) 

    # Double every other element in the reversed list (starting with the first number in the list).
    #newlist = [expression for item in iterable if condition == True]
    double_every_other = reverse_list
    double_every_other[::2] = [n * 2 for n in double_every_other[::2]]
    print("double every other: ", double_every_other)

    # Subtract nine from numbers over nine.
    # from https://stackoverflow.com/questions/2951701/is-it-possible-to-use-else-in-a-list-comprehension
    # wow, it worked! :)
    subtract_nine = double_every_other
    subtract_nine = [n - 9 if n > 9 else n for n in subtract_nine]
    print("subtract nine over nine: ", subtract_nine)

    # Sum all values.
    sum_list = sum(subtract_nine)
    print("sum list:", sum_list)

    # Take the second digit of that sum.
    second_digit = sum_list % 10
    print("second digit:", second_digit)

    # If that matches the check digit, the whole card number is valid.
    # True Valid!
    if second_digit == check_digit:
        print("Valid!")
    else: 
        print("Invalid!")

    return(credit_card_number)

# call function
(credit_card_validator(credit_card_number))