# Lab 4: Version 2  ---- Aces = 1 or 11

# Dictionary containing card values
card_values = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
    'J': 10, 'Q': 10, 'K': 10
}

# Function add ing values together
def move(card1: str, card2:str, card3: str) -> int:
    '''
    function will add card values together and return sum
    '''
    point = card_values[card1] + card_values[card2] + card_values[card3]
    return point

# Ask user for their three cards. Will loop program
card1 = input('What is your first card?: ').upper()
card2 = input('What is your second card?: ').upper()
card3 = input('What is your third card?: ').upper()

while True:
 
    if card1 not in card_values:
        print('Please enter valve card values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)')
        continue

    elif card2 not in card_values:
        print('Please enter valve card values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)')
        continue

    elif card3 not in card_values:
        print('Please enter valve card values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)')
        continue

    point = move(card1, card2, card3)

    if point < 17:
        print(f'{move(card1, card2, card3)} Hit')

    elif 17<= point < 21:
        print(f'{move(card1, card2, card3)} Stay')

    elif point == 21:
        print(f'{move(card1, card2, card3)} Blackjack!')

    else:
        print(f'{move(card1, card2, card3)} Already Busted')

    break


# if one of the cards is an ace it will give 2nd choice
point = move(card1, card2, card3)

if card1 == 'A' or card2  == 'A' or card3 == 'A':
        point2 = (point + 10)
        if point2 < 17:
            print(f'or {point2} Hit if you count Ace as 11 points')

        elif 17<= point2 < 21:
            print(f'or {point2} Stay if you count Ace as 11 points')

        elif point2 == 21:
            print(f'or {point2} Blackjack if you count Ace as 11 points!')

        else:
            print(f'or {point2} Already Bustedif you count Ace as 11 points')
            