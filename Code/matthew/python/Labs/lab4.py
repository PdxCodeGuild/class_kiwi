'''
Lab 4
BlackJack Advice
'''
# --- Version 1
cards = { 
    'A': 1,
    'a': 1, 
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'j': 10,
    'Q': 10,
    'q': 10,
    'K': 10,
    'k':10
    
}
total = 0
user_cards = []
while True:
    total = 0
    user_cards = []
    print('\nPlease enter three playing cards')
    user_cards.append(input("\nEnter your first card (A,1,2,3,4,5,6,7,8,9,J,Q,K) "))
    user_cards.append(input("\nEnter your second card (A,1,2,3,4,5,6,7,8,9,J,Q,K) "))
    user_cards.append(input("\nEnter your first card (A,1,2,3,4,5,6,7,8,9,J,Q,K) "))
    if 'q' in user_cards:
        break
    for card in user_cards:
        if card in cards:
            total += cards[card]

    if total < 17:
        print(f'\n{total} Hit')
    elif 17 >= total < 21:
        print(f'\n{total} Stay')
    elif total == 21:
        print(f'\n{total} BlackJack')
    elif total < 21:
        print('\n{total} Busted')

# print(user_cards)