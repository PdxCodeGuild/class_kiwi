# # Lab 4: Blackjack Advice
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
# Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Step Create a dictionary for card values.

black_jack_dict = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                '9': 9, '10':10, 'j': 10, 'q': 10, 'k': 10}

# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
players_card1 = input('Please enter your first playing card: ')
players_card2 = input ('Please enter your second playing card: ')
players_card3 = input ('Please enter your third playing card: ')

# Then, figure out the point value of each card individually. 
# test -- renders point value 
# print (black_jack_dict [players_card1.lower()])
# print (black_jack_dict [players_card2.lower()])
# print (black_jack_dict [players_card3.lower()])

# Convert all player inputs to an integer and sum them together 



card1_int = int(black_jack_dict [players_card1.lower()])
card2_int = int(black_jack_dict [players_card2.lower()])
card3_int = int(black_jack_dict [players_card3.lower()])

players_hand = card1_int + card2_int + card3_int

print(players_hand)

# offer advice through if elif 

if players_hand <= 13: 
    print ('Hit')
elif 13 <= players_hand <= 20:
    print ('Stay')
elif players_hand == 21:
    print ('Black Jack!')
else:
    print ('Bust')


# ## Version 2 (optional)

# Aces can be worth 11 if they won't put the total point value of both cards over 21. 
# Remember that you can have multiple aces in a hand. 
# Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. 
# For one half, add 1, for the other, add 11. 
# This ensures if you have multiple aces that you account for the full range of possible values.