"""
Lotto Pick 6
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/9/2022
"""

# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 
# 'winner'. Then try playing pick6 100,000 times, 
# with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, 
# and the number of matches between the ticket and the winning numbers 
# determines the payoff.
# 
# Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
#
# If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
# Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000

# One function you might write is pick6() which will generate a list of 6 random numbers,
# which can then be used for both the winning numbers and tickets.
# Another function could be num_matches(winning, ticket) which returns the number of matches 
# between the winning numbers and the ticket.

########## STEPS ##########

# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance

import random 
from lab_5test import lotto_check 

def pick6():
    numbers =[]
    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)

    return numbers


winning_nums = pick6()


balance = int(0)

variance_1 = 0
variance_2 = 0
variance_3 = 0
variance_4 = 0
variance_5 = 0 
variance_6 = 0

loop_var = int(0)
while loop_var < 100000:
    player_nums = pick6()
    loop_var += 1
    balance -= 2
    lotto_count = lotto_check(winning_nums,player_nums)
    if lotto_count == 1:
        balance += 4
        variance_1 += 1
    if lotto_count == 2:
        balance += 7
        variance_2 += 1
    if lotto_count == 3:
        balance += 100
        variance_3 += 1
    if lotto_count == 4:
        balance += 50000
        variance_4 += 1
    if lotto_count == 5:
        variance_5 += 1
        balance += 1000000
    if lotto_count == 6:
        balance += 25000000
        variance_6 += 1
print(f"Your balance after playing the lottery is ${balance}.")
roi = (balance / 200000)
print (f'Your ROI is %{roi}')
# print(winning_nums)

print(f'Variance is as follows 1, {variance_1}. 2, {variance_2}. 3, {variance_3}. 4, {variance_4}. 5, {variance_5}. 6, {variance_6}')