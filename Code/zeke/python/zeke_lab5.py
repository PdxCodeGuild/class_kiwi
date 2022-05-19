# Have the computer play pick6 many times and determine net balance.



# A ticket contains 6 numbers, 1 to 99, 
# and the number of matches between the ticket and the winning numbers determines the payoff. 
# Order matters,if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
# If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
# Calculate your net winnings (the sum of all expenses and earnings).

# Initially the program will pick 6 random numbers as the 'winner'. 
# Then try playing pick6 100,000 times, with the ticket cost and payoff below.
##################################################################
# Player TICKET

import random

def pick6():
    tickets = [ ]
    for i in range(6):
        tickets.append((random.randint(1, 99)))
        # print(random.randint(1, 99))
        
    return tickets
player_ticket=pick6()
# Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers
#  and the ticket.
####################################################################
# WINNING TICKET

# for i in range(6):
#     winning_ticket.append(random.randint(1,99))
# winning_ticket = pick6()
winning_ticket = pick6()
print(winning_ticket)
#####################################################################
# print(winning_ticket)

# for i in range(5):
#     print(pick6())

#####################################################################
# COST OF TICKETS
balance = 0
total_earnnings = 0
money_spent = 0
earnings = 0

for i in range(100000):
    player_ticket = pick6()
    balance = balance -2 
    money_spent = money_spent +2
    matches = 0
    print(player_ticket)
    
    # while balance <10:
    #     balance = balance + 2
    #     print(balance)
    # print(winning_ticket[0]== player_ticket[0])


    if winning_ticket[0] == player_ticket[0]:
        print(f'you win')
        matches = matches +1
    # checks if winning and player ticket matches in spot 0
    if winning_ticket[1]== player_ticket[1]:
        print(f'you win')
        matches = matches +1
    if winning_ticket[2]== player_ticket[2]:
        print(f'you win')
        matches = matches +1
    if winning_ticket[3]== player_ticket[3]:
        print(f'you win')
        matches = matches +1
    if winning_ticket[4]== player_ticket[4]:
        print(f'you win')
        matches = matches +1  
    if winning_ticket[5]== player_ticket[5]:
        print(f'you win')
        matches = matches +1  

    # print(counter)
    #printing (counter) prints the total 

    total_earnings ={
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000

    }

    if matches == 1:
        print(f'you have earned ${total_earnings[1]}')
        balance = total_earnings[1] + balance 
        earnings = total_earnings[1]
    if matches == 2:
        print(f'you have earned ${total_earnings[2]}')
        balance = total_earnings[2] + balance 
        earnings = total_earnings[2]
    if matches == 3:
        print(f'you have earned ${total_earnings[3]}')
        balance = total_earnings[3] + balance 
        earnings = total_earnings[3]
    if matches == 4:
        print(f'you have earned ${total_earnings[4]}')
        balance = total_earnings[4] + balance 
        earnings = total_earnings[4]
    if matches == 5:
        print(f'you have earned ${total_earnings[5]}')
        balance = total_earnings[5] + balance 
        earnings = total_earnings[5]
    if matches == 6:
        print(f'you have earned ${total_earnings[6]}')
        balance = total_earnings[6] + balance 
        earnings = total_earnings[6]
    if matches == 0:
        print(f'you have no matches')
print(f'your balance ${balance}')
print(f'your earnings: {earnings}')
print(f'your money spent: {money_spent}')
x = earnings-money_spent
roi = x /money_spent
print(f'Your Return of Investment: {roi}')