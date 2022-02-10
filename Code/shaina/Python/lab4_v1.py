# Lab 4: Version 1  ---- Aces = 1

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
while True:
    card1 = input('What is your first card?: ').upper()
    card2 = input('What is your second card?: ').upper()
    card3 = input('What is your third card?: ').upper()
   
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
