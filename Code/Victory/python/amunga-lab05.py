#Create a function that generates 6 random lotto numbers, then computer plays against it 100000 times to determine if it wins.
import random

lotto_ticket = [] # This is the winning ticket

for i in range(6):
    num = random.randint(1,99)
    lotto_ticket.append(num)

#print(lotto_ticket)


#ticket_comparison = 0 #compares if index in tickets match

cash_at_hand = 0
cost_of_ticket = 0
times_ticks_match =0

for x in range(100000):

    user_ticket = [] # Computer generated tickets used to play

    for z in range(6):
        numb = random.randint(1,99)
        user_ticket.append(numb)
#print(user_ticket)
    ticket_comparison = 0 #resets it to zero for each ticket
    for y in range(6):
        if user_ticket[y] == lotto_ticket[y]:
            ticket_comparison += 1

    cost_of_ticket += 2

    if ticket_comparison == 6:
        cash_at_hand += 25000000
        times_ticks_match += 1
    elif ticket_comparison == 5:
        cash_at_hand += 1000000
        times_ticks_match += 1
    elif ticket_comparison == 4:
        cash_at_hand += 50000
        times_ticks_match += 1
    elif ticket_comparison == 3:
        cash_at_hand += 100
        times_ticks_match += 1
    elif ticket_comparison == 2:
        cash_at_hand += 7
        times_ticks_match += 1
    elif ticket_comparison ==1:
        cash_at_hand += 4
        times_ticks_match += 1

#print(cost_of_ticket)
print(f"You have spent {cost_of_ticket} dollars on tickets. By playing that many times, you have earned ${cash_at_hand}.")
#print(cash_at_hand)
print(f"\nThe winning ticket is {lotto_ticket}, to win that much you played {times_ticks_match} times  ")
#print(times_ticks_match) #Because I am getting a cash at hand of 25000000, I have this as proof program is running. This is only number changing in the loop

'''Version 2'''
#Return of Investment = (earnings-expenses)/expenses
profit = cash_at_hand - cost_of_ticket
#print(profit)

return_of_investment = profit/cost_of_ticket
print('\nThe return of investment is', return_of_investment)




