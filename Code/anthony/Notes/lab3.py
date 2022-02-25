###  Lab 3 Practice  ###
################################
##                            ##
##   Lab 3: Number to Phrase  ##
##   Author: Anthony Bilie    ##
##   Date: 2/16/2022          ##
##                            ##
################################

# Version 1
# Version 2 = Handle numbers from 100-99
# Convert a given number into its english representation.
# For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Hint: you can use modulus to extract the ones and tens digit.
# user input
x = int(input("Please enter a number from 0-999: "))
# label digits
tens_digit = x//10
ones_digit = x % 10
hundreds_digit = x//100
# strings to capture output strings
ones = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seveenteen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
hundreds = ["", "one-hundred", "two-hundred", "three-hundred", "four-hundred",
            "five-hundred", "six-hundred", "seven-hundred", "eight-hundred", "nine-hundred"]
# logic to determine output
if x < 10:
    print(ones[ones_digit])
elif 9 < x < 20:
    print(teens[ones_digit])
elif 19 < x < 100:
    if ones_digit == 0:
        print(tens[tens_digit])
    else:
        print(tens[tens_digit] + " " + ones[ones_digit])
else:
    if 99 < x < 110:
        if ones_digit == 0:
            print(hundreds[hundreds_digit])
        else:
            print(hundreds[hundreds_digit] + " " + ones[ones_digit])
    elif 109 < x < 120:
        print(hundreds[hundreds_digit] + " " + teens[ones_digit])
    elif x > 119:
        if ones_digit == 0:
            print(hundreds[hundreds_digit] + " " + tens[tens_digit % 10])
        else:
            print(hundreds[hundreds_digit] + " " +
                  tens[tens_digit % 10] + " " + ones[ones_digit])
