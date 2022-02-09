# Lab 3: Number to Phrase

# Convert given number to english representation
# input for number
number = int(input("Please provide a number: "))

# extraction of ones and tens digits
tens_digit = number//10
ones_digit = number % 10
hundreds_digit = number//100


# ones function
def ones(num):
    """
    Function to extract ones digit name
    """
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"


# tens function


def tens(num):
    """
    Function to extract tens digit names
    """
    if num == 1:
        return "one"
    elif num == 2:
        return "twenty"
    elif num == 3:
        return "thirty"
    elif num == 4:
        return "fourty"
    elif num == 5:
        return "fifty"
    elif num == 6:
        return "sixty"
    elif num == 7:
        return "seventy"
    elif num == 8:
        return "eighty"
    elif num == 9:
        return "ninety"


# teens function


def teens(num):
    """
    Funcuntion to extract names for numbers in the teens
    """
    if num == 1:
        return "eleven"
    elif num == 2:
        return "twelve"
    elif num == 3:
        return "thirteen"
    elif num == 4:
        return "fourteen"
    elif num == 5:
        return "fifteen"
    elif num == 6:
        return "sixteen"
    elif num == 7:
        return "seventeen"
    elif num == 8:
        return "eighteen"
    elif num == 9:
        return "nineteen"
    elif num == 0:
        return "ten"


def hundred(num):
    if num == 1:
        return "one hundred"
    elif num == 2:
        return "two hundred"
    elif num == 3:
        return "three hundred"
    elif num == 4:
        return "found hundred"
    elif num == 5:
        return "five hundred"
    elif num == 6:
        return "six hundred"
    elif num == 7:
        return "seven hundred"
    elif num == 8:
        return "eight hundred"
    elif num == 9:
        return "nine hundred"


# If statement to test numbers used and provide output
if 19 < number < 99:
    total = tens(tens_digit), ones(ones_digit)
    print(total)
elif 9 < number < 20:
    total = teens(ones_digit)
    print(total)
elif number < 10:
    total = ones(ones_digit)
    print(total)
elif 99 < number < 109:
    total = hundred(hundreds_digit), ones(ones_digit)
    print(total)
elif 110 < number < 120:
    total = hundred(hundreds_digit), teens(ones_digit)
    print(total)
elif number > 119:
    total = hundred(hundreds_digit), tens(tens_digit % 10), ones(ones_digit)
    print(total)
