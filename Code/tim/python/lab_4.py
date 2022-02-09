"""
Black Jack Advice
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/8/2022
"""
# We want to build a dictionary for card values

# We want to greet the user and ask for three playing card values

# Then we want to take their card input, index them values and figure out their total

# For now, we will assume aces are worth 1, all other card values remain standard
"""
#### our advice is as follows ####
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted!"

"""
# then we will print out the current point value and our advice

# I.e. "15 Hit."


##### We want to build a dictionary for card values
Cards = {'A': int(1), 
"2" : int(2),
"3" : int(3),
"4" : int(4),
"5" : int(5),
"6" : int(6),
"7" : int(7),
"8" : int(8),
"9" : int(9),
"10": int(10), 
"J" : int(10),
"Q" : int(10),
"K" : int(10)}

##### We want to greet the user and ask for three playing card values

print("Hello, I will help you win at BlackJack")

Card_1 = input("What is your first card? ").upper()

Card_2 = input("What is your second card? ").upper()

Card_3 = input("What is your third card? ").upper()

# print(Card_1,Card_2,Card_3)

# we successfully indexed these, now let's make sure they're the right type,
# we want them to be a str
# print(
# type(Card_1),
# type(Card_2),
# type(Card_3)
# )

# output was STR for 1, 2, k so I suspect it will be okay.
### This was not tested with the change of adding .upper to the card1-3 variables


##### Then we want to take their card input, index them values and figure out their total
Card_1_Value = Cards.get(Card_1)
Card_2_Value = Cards.get(Card_2)
Card_3_Value = Cards.get(Card_3)

# print(Card_1_Value)
# print(Card_2_Value)
# print(Card_3_Value)

total_value = Card_1_Value + Card_2_Value + Card_3_Value

# print(total_value)


"""
#### our advice is as follows ####
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted!"

"""
##### then we will print out the current point value and our advice

if total_value < 17:
    print(f'Your card value is {total_value} I would Hit.')
elif 17 <= total_value < 21:
    print(f'Your card value is {total_value} I would Stay.')
elif total_value == 21:
    print(f'Your card value is 21!!! Blackjack!')
else:
    print('It is too late, you have already busted :(')

