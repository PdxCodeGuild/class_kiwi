# Lab 4: Blackjack Advice
"""Blackjack advice for beginners from a beginner"""

# dictionary of card and their values
card_value = {
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}

def card_total(total):
    if total < 17:
        return "Recommended to Hit!"
    elif 17 <= total < 21:
        return "Recommended to stay."
    elif total == 21:
        return "You hit BLACKJACK!!!"
    else:
        return "You already busted :("
    
# Prompting user for cards
card1 = input("What's your first card: ")
card2 = input("what's your second card: ")
card3 = input("What's your third card: ")

# calculating total for function 
total = card_value[card1] + card_value[card2] + card_value[card3]

# Version 2 (Optional)
if card1 == "A" or card2 == "A" or card3 == "A":
    if total + 10 < 21 :
        total += 10

# using function to determine recommendation
print(card_total(total))
    
