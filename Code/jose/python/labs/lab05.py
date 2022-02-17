
import random


def pick6():
    # Generate a 6 element list with random numbers between 1-99
    tickets = []
    for i in range(6):
        tickets.append(random.randint(1, 99))

    return tickets


# Generate a list of 6 random numbers representing the winning tickets
NUM_OF_TICKETS = 100_000


winning_ticket = pick6()


# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:
# NUM_OF_TICKETS = 100_000
for x in range(NUM_OF_TICKETS):

    # Generate a list of 6 random numbers representing the ticket
    user_ticket = pick6()


# subtract 2 from your balance (you bout a ticket)
    balance -= 2

 # Find how many numbers match:
    matches = 0
    for y in range(6):
        if winning_ticket[y] == user_ticket[y]:
            matches += 1

#  add to your balance the winnings from your matches

    if matches == 6:
        balance += 25_000_000
    elif matches == 5:
        balance += 1_000_000
    elif matches == 4:
        balance += 50_000
    elif matches == 3:
        balance += 100
    elif matches == 2:
        balance += 7
    elif matches == 1:
        balance += 4

# After the loop, print the final balance
print(f"Your final balance is ${balance}")
