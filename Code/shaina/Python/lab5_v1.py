# Lab 5: Version 1
import random

# function generating random list of 6 numbers
def pick6():
    numbers = []

    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)
    
    return numbers

# Balance starts at 0
balance = 0

# loop 100,000 times
for i in range(100000):
    winning = pick6()
    ticket = pick6()
    balance -= 2    #  each ticket is $2

# Calculate the matches   
    match = 0
    if winning[0] == ticket[0]:
        match += 1
    if winning[1] == ticket[1]:
        match += 1
    if winning[2] == ticket[2]:
        match += 1
    if winning[3] == ticket[3]:
        match += 1
    if winning[4] == ticket[4]:
        match += 1
    if winning[5] == ticket[5]:
        match += 1

# Based on matches, add winnings to balance
    if match == 1:
        balance += 4
    elif match == 2:
        balance += 7
    elif match == 3:
        balance += 100
    elif match == 4:
        balance += 50000
    elif match == 5:
        balance += 1000000
    elif match == 6:
        balance += 25000000

# After loop print final balance
print(f'The final balance is ${balance}')
