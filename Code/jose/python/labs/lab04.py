#  black jack advice

# create dictionarey for cards and assign values.


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


#  Ask user for 3 playing cards
# Validate input

card1 = validate_card("Enter your first card: ")

card2 = validate_card("Enter your second card: ")

card3 = validate_card("Enter your third card: ")


# Calculate point value of the 3 cards

total = deck[card1] + deck[card2] + deck[card3]


# Give advise based on point value
if total <= 16:
    print("Hit!")

elif total <= total <= 20:
    print("Stay")
elif total == 21:
    print("BlackJack!!!")
else:
    print("Already busted :(")
