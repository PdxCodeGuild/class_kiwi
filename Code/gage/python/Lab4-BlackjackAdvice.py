
'''

VERSION 1

# Dictionary that stores each cards name and value
blackjack_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9, 
    "10": 10, 
    "J": 10,
    "Q": 10,
    "K": 10
}

# Three inputs for each of the users card
user_hand_one = str(input("Enter your first playing card  (for face cards enter the first letter): ").upper())
user_hand_two = str(input("Enter your second playing card (for face cards enter the first letter): ").upper())
user_hand_three = str(input("Enter your third playing card  (for face cards enter the first letter): ").upper())

# Checks if user entered a vlaid card name ************************** if user_hand_one or user_hand_two or user_hand_three not in blackjack_values DOES NOT WORK? This is why i typed out each if and elif statment separetly
if user_hand_one not in blackjack_values:
    print( f"'{user_hand_one}' is not allowed, Please enter a valid card name *Face cards should be typed as the first letter only*")
elif user_hand_two not in blackjack_values:
    print( f"'{user_hand_two}' is not allowed, Please enter a valid card name *Face cards should be typed as the first letter only*")
elif user_hand_three not in blackjack_values:
    print( f"'{user_hand_three}' is not allowed, Please enter a valid card name *Face cards should be typed as the first letter only*")
else:
    # Adds all user card values together
    hand_value = blackjack_values[user_hand_one] + blackjack_values[user_hand_two] + blackjack_values[user_hand_two]

    # Determines which adivce to give the user based on hand_value math
    if hand_value < 17:
            print( f"{hand_value} You should HIT!")
    elif 17 <= hand_value < 21:
            print( f"{hand_value} You should STAY!")
    elif hand_value == 21:
            print( f"{hand_value} BLACKJACK!")
    else:
            print( f"{hand_value} You already BUSTED!")


'''


'''

VERSION 2

# Dictionary that stores each cards name and value
blackjack_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9, 
    "10": 10, 
    "J": 10,
    "Q": 10,
    "K": 10
}


# Three inputs for each of the users card
user_hand_one = str(input("Enter your first playing card  (for face cards enter the first letter): ").upper())
user_hand_two = str(input("Enter your second playing card (for face cards enter the first letter): ").upper())
user_hand_three = str(input("Enter your third playing card  (for face cards enter the first letter): ").upper())
# Checks if user entered a vlaid card name ************************** if user_hand_one or user_hand_two or user_hand_three not in blackjack_values DOES NOT WORK? This is why i typed out each if and elif statment separetly
if user_hand_one not in blackjack_values:
    print( f"'{user_hand_one}' is not allowed, Please enter a valid card name *Face cards should be typed as the first letter only*")
elif user_hand_two not in blackjack_values:
    print( f"'{user_hand_two}' is not allowed, Please enter a valid card name *Face cards should be typed as the first letter only*")
elif user_hand_three not in blackjack_values:
    print( f"'{user_hand_three}' is not allowed, Please enter a valid card name *Face cards should be typed as the first letter only*")

else:
    # Adds all user card values together
    hand_value = blackjack_values[user_hand_one] + blackjack_values[user_hand_two] + blackjack_values[user_hand_two]

    if hand_value + 11 < 21:
        blackjack_values["A"] = 11
        hand_value = blackjack_values[user_hand_one] + blackjack_values[user_hand_two] + blackjack_values[user_hand_two]
    # Determines which adivce to give the user based on hand_value math
    if hand_value < 17:
            print( f"{hand_value} You should HIT!")
    elif 17 <= hand_value < 21:
            print( f"{hand_value} You should STAY!")
    elif hand_value == 21:
            print( f"{hand_value} BLACKJACK!")
    else:
            print( f"{hand_value} You already BUSTED!")


'''