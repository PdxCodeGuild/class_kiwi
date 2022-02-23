
#VERSION 1


import random
print("Welcome to Pick 6.")


def pick_6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))

    return nums


def num_matches(winning, ticket):
    matching_numbers = 0
    if winning[0] == ticket[0]:
        matching_numbers += 1
    if winning[1] == ticket[1]:
        matching_numbers += 1
    if winning[2] == ticket[2]:
        matching_numbers += 1
    if winning[3] == ticket[3]:
        matching_numbers += 1
    if winning[4] == ticket[4]:
        matching_numbers += 1
    if winning[5] == ticket[5]:
        matching_numbers += 1
    return matching_numbers


winning = pick_6()

balance = 0

for i in range(100000):
    ticket = pick_6()
    balance -= 2
    check = num_matches(winning, ticket)
    if check == 1:
        balance += 4
    if check == 2:
        balance += 7
    if check == 3:
        balance += 100
    if check == 4:
        balance += 50000
    if check == 5:
        balance += 1000000
    if check == 6:
        balance += 25000000

print(f"You bought 100,000 pick6 tickets and your \ncurrent balance after playing is ${balance}.")


#VERSION 2

import random
print("Welcome to Pick 6.")


def pick_6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))

    return nums


def num_matches(winning, ticket):
    matching_numbers = 0
    if winning[0] == ticket[0]:
        matching_numbers += 1
    if winning[1] == ticket[1]:
        matching_numbers += 1
    if winning[2] == ticket[2]:
        matching_numbers += 1
    if winning[3] == ticket[3]:
        matching_numbers += 1
    if winning[4] == ticket[4]:
        matching_numbers += 1
    if winning[5] == ticket[5]:
        matching_numbers += 1
    return matching_numbers


winning = pick_6()


earnings = 0
expenses = 0
balance = 0


for i in range(100000):
    ticket = pick_6()
    balance -= 2
    expenses -= 2
    check = num_matches(winning, ticket)
    if check == 1:
        balance += 4
        earnings += 4
    if check == 2:
        balance += 7
        earnings += 7
    if check == 3:
        balance += 100
        earnings += 100
    if check == 4:
        balance += 50000
        earnings += 50000
    if check == 5:
        balance += 1000000
        earnings += 1000000
    if check == 6:
        balance += 25000000
        earnings += 25000000

roi = earnings - expenses/expenses

print(f"You bought 100,000 pick6 tickets and your \ncurrent balance after playing is ${balance}.")
print(f"Your ROI is ${roi}.")