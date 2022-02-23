
# 3 input statements for each of the 3 cards
card_1 = input("\nWelcome! Here is a list of all of the cards\nA, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K\n\nPlease enter your first card: ").lower()
card_2 = input("\n\n\nPlease enter your second card now: ").lower()
card_3 = input("\n\n\nPlease enter your thrid card now: ").lower()


# Dict of the value of all cards
cards_dict = {"a": 1,
              "j": 10,
              "q": 10,
              "k": 10,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10    
              }


# a funtion that grabs each value from the DICT and adds them all up
def black_jack(card_1, card_2, card_3):
    value_1 = cards_dict[card_1]
    value_2 = cards_dict[card_2]
    value_3 = cards_dict[card_3]
    total = value_1 + value_2 + value_3
    if total == 21:
        print(f"You have {total}, thats Blackjack!")
    elif total < 17:
        print(f"You have {total}, You should Hit.")
    elif total > 21:
        print(f"You have {total}, You already Busted.")
    elif total >= 17 and total < 21:
        print(f"You have {total}, You should Stay.")


# if statement that makes sure each card is actually a valid card, if they all are then it calls the funtion above.
if card_1 not in cards_dict.keys():
    print("You entered an invalid card")
elif card_2 not in cards_dict.keys():
    print("You entered an invalid card")
elif card_3 not in cards_dict.keys():
    print("You entered an invalid card")
else:
    black_jack(card_1, card_2, card_3)

