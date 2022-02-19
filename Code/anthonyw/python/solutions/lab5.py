# Pick 6
"""
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

"""
import random
import time


def pick6():
    # Generate a 6 element list with random numbers between 1-99
    # tickets = random.sample(range(1, 49), 6)

    tickets = []

    for i in range(6):
        tickets.append(random.randint(1, 99))

    return tickets


NUM_OF_TICKETS = 100_000
# Steps
# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = pick6()

# Start your balance at 0
balance = 0
earnings = 0
expenses = NUM_OF_TICKETS * 2

start_time = time.time()
# Loop 100,000 times, for each loop:
for x in range(NUM_OF_TICKETS):
    # Generate a list of 6 random numbers representing the ticket
    user_ticket = pick6()

    # Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    # expenses += 2

    # Find how many numbers match
    matches = 0
    for y in range(6):
        if winning_ticket[y] == user_ticket[y]:
            matches += 1

    # Add to your balance the winnings from your matches
    if matches == 6:
        balance += 25_000_000
        earnings += 25_000_000
    elif matches == 5:
        balance += 1_000_000
        earnings += 1_000_000
    elif matches == 4:
        balance += 50_000
        earnings += 50_000
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 1:
        balance += 4
        earnings += 4
# After the loop, print the final balance
print(
    f"Your final balance is ${balance}. You spent a total of ${expenses} on tickets and earned ${earnings} from winnings")
stop_time = time.time()
print(f"This took: {round(stop_time - start_time, 3)}s")
