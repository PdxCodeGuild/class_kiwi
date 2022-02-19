# Lab 4

# Ask Player for cards (3 cards 3 inputs)


from ast import Str


card1 = input("What's your first card? ")
card2 = input("What's your second card? ")
card3 = input("What's your third card? ")

# dictionary for card and point value
card_value = {
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

# Function to retrieve card value


def value(num, num2, num3):
    """
    Logic for advice based off total score of cards
    """
    if num and num2 and num3 in card_value:
        value1 = card_value[num]
        value2 = card_value[num2]
        value3 = card_value[num3]
        total = value1 + value2 + value3
    else:
        total = (f"Please enter a valid value: {', '.join(card_value.keys())}")

    return total

# Function for advice


def advice(total: int):
    """
    function to provide advice based off totaled numbered cards
    """
    if total < 17:
        answer = "Hit"
    elif 17 <= total < 21:
        answer = "Stay"
    elif total == 21:
        answer = "Blackjack!"
    else:
        answer = "Already Busted"

    return answer


def logic(x, y):
    if x == int:
        output = x, y
    else:
        output = y


finish = logic(value, advice)
print(finish)
# final_value = value(card1, card2, card3)
#     final_advice = advice(final_value)
#     print(final_value, final_advice)
#     print(value(card1, card2, card3))
# else:
#     print(final_value)


output = logic(value, advice)
