# Lab 4: Blackjack Advice

"""
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

* Less than 17, advise to "Hit"
* Greater than or equal to 17, but less than 21, advise to "Stay"
* Exactly 21, advise "Blackjack!"
* Over 21, advise "Already Busted"

Print out the current total point value and the advice.

```
What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
"""

cards_list = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "j": 10,
    "Q": 10,
    "K": 10
}

user1 = input("what is your first card? ")
user2 = input("what is your second card? ")
user3 = input("what is your third card? ")

def sum(user1, user2, user3):
    j = cards_list[user1]
    k = cards_list[user2]
    r = cards_list[user3]
    total = j + k + r
    print(f"your total is {total}. ") 
    if total == 21:
        print("You WON!")
    elif total < 17:                      # Less than 17, advise to "Hit"
        print("hit")
    elif total >= 17 and total < 21:     # Greater than or equal to 17, but less than 21, advise to "Stay"
        print("stay")  
    elif total > 21:
        print("bust")                     # Over 21, advise "Already Busted"
                         
sum(user1, user2, user3)    
 