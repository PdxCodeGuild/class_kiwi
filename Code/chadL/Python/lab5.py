# Lab 5: Pick6
import random
"""

Steps
Generate a list of 6 random numbers representing the winning tickets

Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
Version 2---------------------------------------------------------
The ROI (return on investment) is defined as (earnings - expenses)/expenses.
 Calculate your ROI, print it out along with your earnings and expenses.
 a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
 
lottery_numbers = []                                           # storage holder for our 6 lucky numbers
for i in range(0,6):
    number = random.randint(1,99)
    while number in lottery_numbers:
        number = random.randint(1,99)
    lottery_numbers.append(number)

counter = 0                                                  #Start your balance at 0
for number in lottery_numbers:
    if number in lottery_numbers:
        counter +=1 
        
print(f" your lottery numbers are: {lottery_numbers}.")

wallet = 0    
"""
                                      









winnings = 0 
expenses = 0 
matches = 0

winning_dict = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 100000,
    6: 250000
}

def pick_six():
    num_list = [random.randint(0,99) for i in range(6)]
    return(num_list)

#winning_ticket = pick_six()

def ticket_bought():                #tracking expenses
    global expenses
    expenses += 2  
    return pick_six()

#my_ticket = ticket_bought()
#print(expenses)       #alt +shift down key

def comparison_tool(winning_ticket, ticket):
    global matches
    for i, value in enumerate(ticket):
        if winning_ticket[i] == value:
            matches += 1
    return matches

def win_values(x):
    return winning_dict[x]   

winning_ticket = pick_six()         # resets match ticket
for i in range(100000):    
    my_ticket = ticket_bought()
    
    winnings += win_values(comparison_tool(winning_ticket, my_ticket) )   
    my_ticket =[]
    matches = 0 
    
print(f"your wiinings are: {winnings}, and your expenses are: {expenses}") 



