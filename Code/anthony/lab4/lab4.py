# Lab 4

# Ask Player for cards (3 cards 3 inputs)


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


def value(num, num2, num3):
    """
    Logic for advice based off total score of cards
    """
    if num in card_value:
        value1 = card_value[num]

    if num2 in card_value:
        value2 = card_value[num2]

    if num3 in card_value:
        value3 = card_value[num3]

    total = value1 + value2 + value3

    return total


def advice(total):
    if total < 17:
        answer = "Hit"
    elif 17 <= total < 21:
        answer = "Stay"
    elif total == 21:
        answer = "Blackjack!"
    else:
        answer = "Already Busted"

    return answer


final_value = value(card1, card2, card3)
final_advice = advice(final_value)

print(final_value, final_advice)
