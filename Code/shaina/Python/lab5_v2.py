# Lab 5: Version 2
import random

# function generating random list of 6 numbers
def pick6():
    numbers = []

    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)
    
    return numbers

# expenses and earnings starts at 0
expenses = 0
earnings = 0

# loop 100,000 times
for i in range(100000):
    winning = pick6()
    ticket = pick6()
    expenses -= 2    #  each ticket is $2

# Calculate the matches   
    match = 0
    for i in range(6):
        if winning[i] == ticket[i]:
            match += 1

# Based on matches, add winnings to earnings
    if match == 1:
        earnings += 4
    elif match == 2:
        earnings += 7
    elif match == 3:
        earnings += 100
    elif match == 4:
        earnings += 50000
    elif match == 5:
        earnings += 1000000
    elif match == 6:
        earnings += 25000000

# Function calculating the ROI or return on investment
def ROI(earnings, expenses):
    ROI = (earnings - expenses) / expenses
    return ROI
    
# After loop print ROI, expneses, and earnings
print(f'''
Your earnings were ${earnings:.2f}.
Your expenses were ${expenses:.2f}.
The final return on investment is {ROI(earnings, expenses):.2f}
''')
