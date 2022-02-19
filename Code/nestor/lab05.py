import random

# Version 1


def pick_6(x):
    """creates random numbers list based on user input"""
    iterations = list()
    while len(iterations) < x:
        iterations.append(random.randint(1, 99))
    return iterations


# User specifies ticket purchased amount
ticket = int(input("Enter amount of tickets purchased: "))

# winning ticket to compare
winning_ticket = pick_6(6)
ticket_list = list()


def ticket_comparison(ticket):
    """function to compare winning ticket to random ticket"""
    new_ticket = list()
    rounds = 0
    total_win = 0
    while rounds < ticket:
        new_ticket = pick_6(6)
        total_win -= 2
        ticket_list.append(new_ticket)
        rounds += 1
        matches = 0
        for i, value in enumerate(new_ticket):
            if value == winning_ticket[i]:
                matches += 1
        if matches == 6:
            total_win += 25_000_000
        elif matches == 5:
            total_win += 1_000_000
        elif matches == 4:
            total_win += 50_000
        elif matches == 3:
            total_win += 100
        elif matches == 2:
            total_win += 7
        elif matches == 1:
            total_win += 4
    return total_win


print(f"Winning Ticket: {winning_ticket}")
print(f"total won: {ticket_comparison(ticket)}")

# Version 2
# calculating return on investment and printing out
expense = ticket * (-2)
ROI = (ticket_comparison(ticket) - expense / expense)
print(f"ROI = {ROI}")
