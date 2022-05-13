# LAB 5

import random
# Pick 6 random numbers at the 'winner'

# user pick  6

# myticket


def pick6():
    """
   users 6 numbers
    """
    numbers_list = []
    for x in range(6):
        numbers = random.randint(1, 99)
        numbers_list.append(numbers)

    return numbers_list

# winning ticket


def win_ticket():
    """
    winning 6 numbers
    """
    numbers_list = []
    for x in range(6):
        number = random.randint(1, 99)
        numbers_list.append(number)

    return numbers_list


# number of matches
def num_matches(winning, ticket):
    matches = 0
    for x in range(len(winning)):
        if winning[x] == ticket[x]:
            matches += 1
    return matches


# monies won dictionary
monies_dict = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}


# winning ticket
winning = win_ticket()
# zero balance
balance = 0
# loop 100,00 times for each loop .
for x in range(100000):
    match_list = []
    # generate a ticket
    ticket = pick6()
    # subtract balance for playing game
    balance -= 2
    # find how many matches
    matches = num_matches(winning, ticket)
    # monies won
    if matches > 0:
        balance += monies_dict[matches]
# loop complete
# print final balance
print(f"Your final balance is ${balance}.")

# Version 2
# Print (ROI) Return on investment ---- (earnings - expenses)/ expenses
# expenses
expenses = 2 * -100000
earnings = balance - expenses
# roi
roi = (earnings - expenses)/expenses
print(f"Your exepenses are {expenses}.")
print(f"Your earnings are {earnings}.")
print(f"Your Return on Investment(ROI) is {round(roi,2)}.")
