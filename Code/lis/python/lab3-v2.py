#Lab 3 Version 2

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
def nums_100_to_999(input_number):

    if 100 <= input_number <= 999:

        first_digit = input_number // 100
        second_digit = input_number // 10 % 10
        third_digit = input_number % 10

        second_digit_convert = second_digit * 10
        if second_digit_convert == 10 and third_digit > 0:
            second_digit_convert = second_digit_convert + third_digit

        first_digit_text = digits[first_digit]
        second_digit_text = digits[second_digit_convert]
        third_digit_text = digits[third_digit]

        if 10 < second_digit_convert < 20:
            third_digit_text = ''
        if second_digit == 0:
            second_digit_text = ''
        if third_digit == 0:
            third_digit_text = ''

        return(f'You entered: {first_digit_text} hundred {second_digit_text}{third_digit_text}')


# create input loop
while True:
    input_number = input("Enter a number from 100-999, or 'done' to quit: ")

    if input_number == 'done':
        break

    input_number = int(input_number)

    # call function
    print(nums_100_to_999(input_number))
