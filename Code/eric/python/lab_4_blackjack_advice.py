## Black Jack Advice
#Version 1

# Build an application that allows the user to input cards and return a value advising to hit, stay, or blackjack

#Dictionary of card values
cards = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}
 # Define inputs
first_card = input('What is your first card? ')
second_card = input('What is your second card? ')

# print(first_card)

#capitalize inputs
first_card_cap = first_card.capitalize()
second_card_cap = second_card.capitalize()


# Convert cards to values
first_card_value = cards[first_card_cap]
second_card_value = cards[second_card_cap]


#define function
def blackjack(hand_input):
    if hand_input > 21:
        return print(f'{hand_input} Bust')

    elif hand_input == 21:
        return print(f'{hand_input} BlackJack!')

    elif 21 > hand_input >= 17:
        return print(f'{hand_input} Stay')

    elif hand_input < 17:
        return print(f'{hand_input} Hit')

#build function
if first_card_value + second_card_value >=17:
    hand = first_card_value + second_card_value
    
    blackjack(hand)


elif first_card_value + second_card_value < 17:
    third_card = input('Hit! \nWhat is your third card? ')
    third_card_cap = third_card.capitalize()
    third_card_value = cards[third_card_cap]
    hand = first_card_value + second_card_value + third_card_value
    
    blackjack(hand)


#celebrate and try to figure out version 2