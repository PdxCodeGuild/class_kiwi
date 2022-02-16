# Check Card - 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5


def card_validation(card_num): 
    
    # Gathers the last digit of the card number for later checking use
    check_digit = card_num.pop(-1)

    card_num.reverse() 

    # Base list to store everyother doubled digit
    card_num_doubled = []

    # Doubles every other digit in the card number and minuss '9' for any number over 9 
    for digit in card_num[0::2]:#<------ Targets everyother number starting at the first number of the card
        double = digit * 2
        if double > 9:
            double -= 9
        card_num_doubled.append(double)

    # Removed every other digit starting at the second number of the card
    card_num = card_num[1::2]

    # Calculates the total sum of both the doubled digits and the base digits
    total_sum = list(str((sum(card_num_doubled) + sum(card_num))))

    # Checks if the check digit (Popped from above) is the same as the total sums second digit
    if check_digit == int(total_sum[1]):
        return True
    else:
        return False

# User card converts the card number into a string in order to make it possible to cycle through the number
user_card = str(4556737586899855)
user_card_list = []                                       #--------------------------- May be a better way to convert a long integer into a list* 
# Stores the cycled results of each number as an integer into the list
for numbers in user_card:
    user_card_list.append(int(numbers))

# Checks if the function returend valid or invalid and diplays the correct output
if card_validation(user_card_list) == True:
    print( f"""
---------------------------------------
The card number '{user_card}' is valid! 
---------------------------------------
    """)
else:
    print( f"""
---------------------------------------
The card number '{user_card}' is invalid. 
---------------------------------------
    """)

