import random

def generate_numbers():
    numbers = []
    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)
        
    return numbers

pick6 = generate_numbers()

winning_ticket = generate_numbers()

balance = 0

print(pick6)
print(winning_ticket)

for pick in pick6:
    print(pick6)
    
for win in winning_ticket:
    print(winning_ticket)
    