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
hundred_numbers = {
    "1": "one-hundred",
    "2": "two-hundred",
    "3": "three-hundred",
    "4": "four-hundred",
    "5": "five-hundred",
    "6": "six-hundred",
    "7": "seven-hundred",
    "8": "eight-hundred",
    "9": "nine-hundred"
}
number = input("Please enter a number: ") 
number = number.zfill(3) # takes number and pads to three digits

def convert(number):
    huns = number[0]
    tens = number[1]
    ones = number[2]

    for hun in huns:
        if hun == "0":
            for ten in tens: # iterates through user inputted tens_digit with variable "ten"
                if ten == "0":
                    for one in ones: # iterates through one_numbers dictionary with a variable "one"
                        if ones == one: # if the user inputted number equals the variable "one" in the one_numbers dictionary, print the value from the one_numbers dictionary
                            return one_numbers[one]
                            break # break so it doesn't continue to reiterate through one_numbers dictionary once a condition is matched
                elif tens == "1":
                    for one in ones:
                        if ones == one: # if the user inputted number equals the variable "one" in the one_numbers dictionary, print the value from the one_numbers dictionary for numbers 11-19
                            return one_numbers["1" + one]
                            break
                elif ones == "0": # if the user inputted ones_digit equals "0" then print the value in the ten_numbers dictionary
                    return ten_numbers[tens]
                else: # if the user inputted ones_digit does not equal "0", then print the value in the ten_numbers dictionary and one_numbers dictionary
                    return f"{ten_numbers[tens]}-{one_numbers[ones]}"
        else:
            for ten in tens: # iterates through user inputted tens_digit with variable "ten"
                if ten == "0":
                    for one in ones: # iterates through one_numbers dictionary with a variable "one"
                        if ones == "0":
                            return hundred_numbers[hun]
                        elif ones == one: # if the user inputted number equals the variable "one" in the one_numbers dictionary, print the value from the one_numbers dictionary
                            return f"{hundred_numbers[hun]} {one_numbers[one]}"
                            break # break so it doesn't continue to reiterate through one_numbers dictionary once a condition is matched
                elif tens == "1":
                    for one in one_numbers:
                        if ones == one: # if the user inputted number equals the variable "one" in the one_numbers dictionary, print the value from the one_numbers dictionary for numbers 11-19
                            return f"{hundred_numbers[hun]} {one_numbers['1' + one]}"
                            break
                elif ones == "0": # if the user inputted ones_digit equals "0" then print the value in the hundred_numbers and ten_numbers dictionary
                    return f"{hundred_numbers[hun]} {ten_numbers[tens]}"
                else: # if the user inputted ones_digit does not equal "0", then print the value in the hundred_numbers dictionary, ten_numbers dictionary and one_numbers dictionary
                    return f"{hundred_numbers[huns]} {ten_numbers[tens]}-{one_numbers[ones]}"

print(convert(number))   