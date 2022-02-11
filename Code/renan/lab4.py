#Python program to give basic blackjack playing advice during a game 
# Ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10.

#Define Card Values as well as Choices
card_value = {
    
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
   "J": 10,
   "Q": 10, 
   "K": 10
         
}


user_choice = input("Whats Your First Card 1: ") 

user_choice2 = input("Whats Your Second Card 2: ") 

user_choice3 = input("Whats Your Third Card 3: ") 

#Define Sum
sum = (card_value[user_choice] + card_value[user_choice2] + card_value[user_choice3])

print(sum)

#Define Your Print Statements
if sum <= 16:
    print("Hit")
    
if 17 <= sum < 21:
    print("Stay")

if sum == 21:
    print("Blackjack!")

if sum > 21:
    print("Already Busted")
    

