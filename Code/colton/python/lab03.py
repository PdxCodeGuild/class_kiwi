'''         +-+#^#+--+#^#+--+#^#+-+             
            Project: Number to Phrase             ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/7/22                     ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''

num_convert = {
    
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "fourty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "one hundred",
    200 : "two hundred",
    300 : "three hundred",
    400 : "four hundred",
    500 : "five hundred",
    600 : "six hundred",
    700 : "seven hundred",
    800 : "eight hundred",
    900 : "nine hundred",
    1000 : "one thousand"


}

num_convertnumeral = {

    0 : "",
    1 : "I",
    2 : "II",
    3 : "III",
    4 : "IV",
    5 : "V",
    6 : "VI",
    7 : "VII",
    8 : "VIII",
    9 : "IX",
    10 : "X",
    11 : "XI",
    12 : "XII",
    13 : "XIII",
    14 : "XIV",
    15 : "XV",
    16 : "XVI",
    17 : "XVII",
    18 : "XVIII",
    19 : "XIX",
    20 : "XX",
    30 : "XXX",
    40 : "XL",
    50 : "L",
    60 : "LX",
    70 : "LXX",
    80 : "LXXX",
    90 : "XC",
    100 : "C",
    200 : "CC",
    300 : "CCC",
    400 : "CD",
    500 : "D",
    600 : "DC",
    700 : "DCC",
    800 : "DCCC",
    900 : "MD",
    1000 : "M"

    

}


def num_to_phrase(number):
    """Function takes number and translates it into a word"""
    
    hunnys = (number // 100)* 100 # Used to get the last three digits of number rounded down to the nearest hundreth
    tens = (number % 100) - (number % 10) # Used to get last two digits of a number rounded down to the nearest tenth
    ones = (number % 10) # Used to get last digit of a number
    special = (number % 100) # Used to get last two digits of a number

    word = "" # Output

    while True:
        x = len(str(number)) # Gets length of number input

        if number == 0:
            #### Runs if number is 0
            word = ("zero")
            return word

        if x == 1:
            #### Runs if there is one char
            word = (f"{num_convert[ones]}")
            return word
        elif x == 2: 
            #### Runs if there are two chars
            if number > 19:
                word = (f"{num_convert[tens]} {num_convert[ones]}")
                return word
            else:
                # Runs if the last two digits are within range 1-19
                word = (f"{num_convert[special]}")
                return word
                    
        elif x == 3:
            #### Runs if there are three chars
            if special > 19:
                word = (f"{num_convert[hunnys]} {num_convert[tens]} {num_convert[ones]}")
                return word
                
            elif special <= 19: 
                # Runs if the last two digits are within range 1-19
                word = (f"{num_convert[hunnys]} {num_convert[special]}")
                return word


def num_to_numeral(number):
    """Converts number to roman numeral"""
    number
    return
        

def main():
    """Main blocks of code"""
    while True:
        try:
            user_input = int(input("Enter a number to convert or type done \n"))
            x = len(str(user_input)) # gets number length
            if x > 3: # If user input is greater than 999 it will repeat loop
                print("Please enter a number from 1 - 999")
                continue
            elif user_input == "done": # Exits application
                exit()

            while True:
                try:
                    user_input2 = input("Would you like to convert to Numerals or Words? \n").lower().strip()
                    
                    if user_input2 == "numerals": # Not done yet
                        # print(num_to_numeral(user_input))
                        break

                    elif user_input2 == "words": 
                        print(num_to_phrase(user_input))
                        break

                except ValueError:
                    print("Try again, Numerals or Words?\n")
                    continue
                
                break   

        except ValueError:
            print("Try again, enter valid number.\n  ")

            
                



if __name__ == "__main__":
    main()

