#Lab 04 - Blackjack advice - version 1 - Working

#Define dictionary to hold deck of cards
deck = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1
}

#Define blank list to hold player cards
pcards = []

#Ask player for three cards, store cards in blank list
cone = str.upper(input('What is your first card?: '))
if cone not in deck:
    print('Invalid card, please try again')
else:
    pcards.append(int(deck[cone]))
ctwo = str.upper(input('What is your second card?: '))
if ctwo not in deck:
    print('Invalid card, please try again')
else:
    pcards.append(int(deck[ctwo]))
cthree = str.upper(input('What is your third card? '))
if cthree not in deck:
    print('Invalid card, please try again')
else:
    pcards.append(int(deck[cthree]))

total = pcards[0] + pcards[1] + pcards[2]

if total < 17:
    print(total, 'Hit!')
elif 17 <= total < 21:
    print(total, 'Stay!')
elif total == 21:
    print(total, 'BLACKJACK!!!!')
else:
    print(total, 'You Done Busted Out, try again sucka!')