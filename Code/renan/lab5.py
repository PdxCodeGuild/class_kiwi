import random

def pick6():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(1, 99))
        #numbers = random.sample(range(1, 99), 6) optional random list
    return numbers

num_of_tickets = 100_000

winning_ticket = pick6()

print('WINNING:', winning_ticket)

balance = 0


for x in range(num_of_tickets):
    user_ticket = pick6()
       
    
    balance-= 2
    
    matching_ticket = 0
    for y in range(6):
        if winning_ticket[y] == user_ticket[y]:
            matching_ticket += 1
    
    if matching_ticket == 6:
        balance += 25_000_000
    elif matching_ticket == 5:
        balance += 1_000_000
    elif matching_ticket == 4:
        balance += 50_000
    elif matching_ticket == 3:
        balance += 100
    elif matching_ticket == 2:
        balance += 7
    elif matching_ticket == 1:
        balance += 4
    
print(f"Your final balance is ${balance}")
