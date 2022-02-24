# Lab 4: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
#  First, ask the user for three playing cards 
# (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
#  Number cards are worth their number, 
# all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"

# Then, figure out the point value of each card individually.

print('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q','K')
card1=input('please enter your card 1: ').upper()
card2=input('please enter your card 2: ').upper()
card3=input('please enter your card 3: ').upper()

user_input ={
    'A': 1, 
    'J': 10,
    'Q': 10,
    'K': 10,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10':10,
}

# card1 = user_input
# card2 =
# card3 =
print(card1, card2, card3)
print(f'Your total is:{user_input[card1]+user_input[card2]+user_input[card3]}')
total = user_input[card1]+user_input[card2]+user_input[card3]
# print(total)

if total < 17:
    print("advise to Hit")
elif total == 17 or total == 18 or total ==19 or total ==20:
    print("stay")
elif total == 21:
    print("Black Jack!")
else:
    print("You Loose")



# total = sum(card1 + card2 + card3)
# print(total)


# total = users
# if > 17 




