# create dictionary
digits = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

# create function
def nums_zero_to_ninetynine(input_number):
    #get dictionary item is less than 20
    if 0 <= input_number <= 19:

        digits_to_nineteen = digits.get(input_number)

        return(f'You entered: {digits_to_nineteen}')

    if 20 <= input_number <= 99:
        # break apart digits and get corresponding dictionary items
        first_digit = input_number // 10
        first_digit_convert = first_digit * 10
        first_digit_text = digits.get(first_digit_convert)

        second_digit = input_number % 10
        second_digit_text = digits.get(second_digit)
        # manipulate text 
        if second_digit_text == 'zero':
            second_digit_text = ''

        return(f'You entered: {first_digit_text}{second_digit_text}')


# create input loop
while True:
    input_number = input("Enter a number from 0-99, or 'done' to quit: ")

    if input_number == 'done':
        break

    input_number = int(input_number)

    # call function
    print(nums_zero_to_ninetynine(input_number))