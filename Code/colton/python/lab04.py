# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

import random
import time
from turtle import hideturtle


card_values = {

    "1" : 1,
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
    "K" : 10,
    "A" : 1,
    "Done" : 0

}


dealer_hand = random.randint(15, 23)


cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random_card = random.choice(cards)



# total += card_values[user_input]


total = 0
while True:
    ### This will get user input and actively add them together, if they enter a value that equals more than 21 than it will print an error
    try:
        user_gamechoice = input("Play the game instead of advice? Yes or No \n").capitalize().strip()
        if user_gamechoice == "Yes":
            
            while True:
                    try:
                        
                        user_input = input("Hit or Stay? \n").capitalize().strip()
                        print(total)
                        if user_input == "Stay":
                            if dealer_hand > total and dealer_hand <= 21:
                                print(f"{total}, dealer wins with {dealer_hand}")
                                time.sleep(3)
                                
                                while True:
                                    user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                    if user_input2 == "Yes":
                                        total = 0
                                        break
                                    elif user_input2 == "No":
                                        exit()
                                    else:
                                        print("Enter Yes or No")
                                    
                                    continue
                            

                            if dealer_hand < total and total <= 21:
                                print(f"{total}, beats dealer with {dealer_hand}")
                                time.sleep(3)
                                
                                while True:
                                    user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                    if user_input2 == "Yes":
                                        total = 0
                                        break
                                    elif user_input2 == "No":
                                        exit()
                                    else:
                                        print("Enter Yes or No")
                                break
                            
                        
                        elif user_input == "Hit":
                            total += card_values[random_card]
                            
                            if random_card == "Ace":    
                                while True:
                                    try:
                                        user_input = int(input("Is your ace worth 1 or 11?"))
                                        if user_input == 1:
                                            total += user_input
                                            break
                                        elif user_input == 11:
                                            total += user_input
                                            break
                                        elif user_input != 1 or user_input != 11:
                                            print("1 or 11")
                                            continue
                                        
                                    except ValueError:
                                        print("Try again")
                                        continue   
                                    total += user_input
                                    break
                                    
                            elif  total > 21:
                                print("That is a bust, try again")
                                while True:
                                    user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                    if user_input2 == "Yes":
                                        total = 0
                                        break
                                    elif user_input2 == "No":
                                        exit()
                                    else:
                                        print("Enter Yes or No")


                    
                            if total >= 17 and total <= 20:
                                print(f"{total} You should stay")



                            elif total == 21:
                                print(f"{total}! Blackjack!")
                                while True:
                                    user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                    if user_input2 == "Yes":
                                        total = 0
                                        break
                                    elif user_input2 == "No":
                                        exit()
                                    else:
                                        print("Enter Yes or No")

                            else:
                                print("Please enter valid input")

                    except ValueError: # If user input does not match dictionary key print error
                        print(f"{user_input} is not a valid input")

        elif user_gamechoice == "No":
        
            while True:
                    try:
                        
                        info = (", ".join(card_values.keys())).replace(", Done", "")
                        print(info)
                        user_input = input("What are your cards? If that is all your cards type 'done'\n").capitalize().strip()
                        
                        if user_input == "Ace":
                            

                            while True:
                                try:
                                    user_input = int(input("Is your ace worth 1 or 11?"))
                                    if user_input == 1:
                                        total += user_input
                                        break
                                    elif user_input == 11:
                                        total += user_input
                                        break
                                    elif user_input != 1 or user_input != 11:
                                        print("1 or 11")
                                        continue
                                    
                                except ValueError:
                                    print("Try again")
                                    continue   
                                total += user_input
                                break

                        else:
                            total += card_values[user_input]
                        


                        if total > 21:
                            print("That is a bust, try again")
                            while True:
                                user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                if user_input2 == "Yes":
                                    total = 0
                                    break
                                elif user_input2 == "No":
                                    exit()
                                else:
                                    print("Enter Yes or No")


                        
                        if user_input == "Done":
                            if total < 17:
                                print(f"{total} You should hit again")
                            while True:
                                user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                if user_input2 == "Yes":
                                    total = 0
                                    break
                                elif user_input2 == "No":
                                    exit()
                                else:
                                    print("Enter Yes or No")
                                
                                    

                            if total >= 17 and total <= 20:
                                print(f"{total} You should stay")
                                while True:
                                    user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                    if user_input2 == "Yes":
                                        total = 0
                                        break
                                    elif user_input2 == "No":
                                        exit()
                                    else:
                                        print("Enter Yes or No")



                            elif total == 21:
                                print(f"{total}! Blackjack!")
                                while True:
                                    user_input2 = input("Would you like to try again? Yes or No\n").capitalize().strip()
                                    if user_input2 == "Yes":
                                        total = 0
                                        break
                                    elif user_input2 == "No":
                                        exit()
                                    else:
                                        print("Enter Yes or No")
                        


                        else:
                            continue



                    except KeyError: # If user input does not match dictionary key print error
                        print(f"{user_input} is not a valid input")


    except ValueError:
        print("Enter valid input bruv")





if __name__ == "__main__":
    main()