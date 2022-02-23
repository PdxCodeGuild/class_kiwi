# Lab 5

import random

# dictionary of winning ticket amounts
matching_ticket_amount = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

# function to generate a list of 6 random integers
def generate_numbers():
    numbers = []
    for i in range(6):
        number = random.randint(1, 99)  # change 99 to 5 for testing
        numbers.append(number)

    return numbers


# function to compares two list for matching values at same index
def number_matches(winning_ticket, customer_ticket):
    list_index = 0
    result = []
    for i in winning_ticket:
        if i == customer_ticket[list_index]:
            result.append(list_index)
        list_index = list_index + 1

    number_of_matches = len(result)
    return(number_of_matches)


# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = generate_numbers()
print(f'The winning ticket numbers are: {winning_ticket}')

# Start your balance at 0
gross_winnings = 0
ticket_cost = 0

# Loop 100,000 times, for each loop:
for i in range(100000): # change 100000 to 5 for testing

    # Generate a list of 6 random numbers representing the customer ticket
    customer_ticket = generate_numbers()
    #print(f'The customer number picks are: {customer_ticket}')   

    # Subtract 2 from your balance (you bought a ticket)
    ticket_cost = ticket_cost - 2
    #print('ticket_cost: ', ticket_cost)

    # Find how many numbers match
    matches = number_matches(winning_ticket, customer_ticket)
    #print(f'The number of matches between tickets: {matches}')

    # match with dictionary amount
    winning_match_amount = matching_ticket_amount.get(matches)
    #print('winning_match_amount: ', winning_match_amount)

    # Add to your balance of the winnings from your matches
    gross_winnings += winning_match_amount
    #print('gross winnings: ', gross_winnings)

    net_winnings = gross_winnings + ticket_cost
    #print('net winnings: ', net_winnings)

# After the loop, print the final balance
print(f'Gross: ${gross_winnings:.2f}')
print(f'Net: ${net_winnings:.2f}')

# version 2 
expenses = ticket_cost * -1
roi = (gross_winnings - expenses) / expenses
print(f'Expenses: ${expenses:.2f}')
print(f'ROI: {roi:.2f}')