one_numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
ten_numbers = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}
number = int(input("Please enter a number: ")) # user inputted number and turns it into an integer for the following arithmetic operations 
# takes number and parses them into individual digits and turns them into a string
def convert(number):
    tens_digit = str(number//10) # floor division by 10 essentially removes the number after the decimal point and turns it back into a string
    ones_digit = str(number%10) # modulus by 10 returns the remainder number essentially making it a single number and turns it back into a string

    for ten in tens_digit: # iterates through user inputted tens_digit with variable "ten"
        if ten == "0":
            for one in one_numbers: # iterates through one_numbers dictionary with a variable "one"
                if ones_digit == one: # if the user inputted number equals the variable "one" in the one_numbers dictionary, print the value from the one_numbers dictionary
                    return one_numbers[one]
                    break # break so it doesn't continue to reiterate through one_numbers dictionary once a condition is matched
        elif tens_digit == "1":
            for one in one_numbers:
                if ones_digit == one: # if the user inputted number equals the variable "one" in the one_numbers dictionary, print the value from the one_numbers dictionary for numbers 11-19
                    return one_numbers["1" + one]
                    break
        elif ones_digit == "0": # if the user inputted ones_digit equals "0" then print the value in the ten_numbers dictionary
            return ten_numbers[tens_digit]
        else: # if the user inputted ones_digit does not equal "0", then print the value in the ten_numbers dictionary and one_numbers dictionary
            return f"{ten_numbers[tens_digit]}-{one_numbers[ones_digit]}"

print(convert(number))