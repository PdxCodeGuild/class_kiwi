import random 
winnings = 0
expenses = 0
matches = 0 

winning_dic = {
    0: 0, 
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def pick_six():
    num_list = [random.randint(0,99) for i in range(6)]
    return num_list

# winning_ticket = pick_six()


def buy_ticket():
    global expenses
    expenses += 2 
    return pick_six()

# my_ticket = buy_ticket()

# print(my_ticket)
# print(expenses)


#for i in range(100000):

def comparison_tool(winning_ticket, ticket):
    global matches 
    for i, value in enumerate(ticket):
        if winning_ticket[i] == value:
            matches+= 1
    return matches 

def win_values(x):
    return winning_dic[x]

winning_ticket = pick_six()

# ticket = buy_ticket()
# x = comparison_tool(winning_ticket, ticket)

# print(x)
for i in range(100000):
    my_ticket = buy_ticket()
    winnings += win_values(comparison_tool(winning_ticket, my_ticket))
    my_ticket =[]
    matches = 0


# print(winnings)
# print(expenses)

Return_on_investment = ((winnings - expenses)/expenses) 

print(f'Your return on investment is {Return_on_investment}.')