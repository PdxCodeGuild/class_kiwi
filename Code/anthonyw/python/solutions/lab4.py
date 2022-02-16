# Blackjack Advice
"""
Let's write a python program to give basic blackjack playing advice 
during a game by asking the player for cards. First, ask the user for 
three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, 
figure out the point value of each card individually. Number cards are worth their number, 
all face cards are worth 10. At this point, assume aces are worth 1. 
Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
"""

# Create table 'dictionary' for cards and values
deck = {
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


def validate_card(prompt):
    card = input(prompt).upper()
    while card not in deck:
        card = input(prompt).upper()

    return card


# Ask the user for 3 playing cards
# Validate input
card1 = validate_card("Enter your first card: ")

card2 = validate_card("Enter your second card: ")

card3 = validate_card("Enter your third card: ")

# Calculate total point value of all 3 cards
total = deck[card1] + deck[card2] + deck[card3]

# Give advice based on total point value
if total <= 16:
    print("Hit!")
elif 17 <= total <= 20:
    print("Stay")
elif total == 21:
    print("Blackjack!")
else:
    print("Already busted :(")
