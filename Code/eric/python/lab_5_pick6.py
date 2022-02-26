#Lab 5 Pick6
#Generate 2 lists of 6 numbers and compare. For every duplicate assign an escalating monetary value and calculate winnings

#import 'random' module
import random

# Set up value dictionary
winnings = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

#define number generator function
def pick6():
    numbers = []
    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)
    return numbers

#define winning ticket variable
winning_ticket = pick6()
## test winning_ticket = [1, 4, 6, 3, 6, 7]
# build pick6 game loop
wallet = 0
tickets = int(input('How many tickets? '))
total_winnings = 0
#build out logic for list comparison
# def compare():
#     tallys = []
    
#     for slot in range(6):
#         if winning_ticket[slot] == user_ticket[slot]:
#             tallys.append(1)

#         elif winning_ticket[slot] != user_ticket[slot]:
#             tallys.append(0)   

#     return sum(tallys)

#version 1 loop
# for i in range(tickets):
#     wallet = wallet - 2
#     user_ticket = pick6()
#     ### test user_ticket = [1, 9, 6, 4, 6, 9]
#     tallys = []
    
#     for slot in range(6):
#         if winning_ticket[slot] == user_ticket[slot]:
#             tallys.append(1)

#         elif winning_ticket[slot] != user_ticket[slot]:
#             tallys.append(0)
    
#     # print(tallys)           
#     # print(winning_ticket)
#     # print(user_ticket)
#     wins = sum(tallys)
#     # print(wins)
#     cash_won = winnings[wins]
#     total_winnings = cash_won + total_winnings
#     wallet = wallet + cash_won
#     # print(wallet)
    
# print(f'You have won: {total_winnings}')
# print(f'Your current wallet is: {wallet}')
        
    
#version 2 loop 

for i in range(tickets):
    wallet = wallet - 2
    user_ticket = pick6()
    
    tallys = []
    
    for slot in range(6):
        if winning_ticket[slot] == user_ticket[slot]:
            tallys.append(1)

        elif winning_ticket[slot] != user_ticket[slot]:
            tallys.append(0)
    
    wins = sum(tallys)
    cash_won = winnings[wins]
    total_winnings = cash_won + total_winnings
    wallet = wallet + cash_won

expenses = tickets * 2   
roi = (total_winnings - expenses) / expenses 

print(f'You have won: {total_winnings}')
print(f'Your current wallet is: {wallet}')
print(f'Your ROI is: {roi}')