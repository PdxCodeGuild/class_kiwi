import random





'''
VERSION 1
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
'''


# Pick six generates a list of 6 random numbers
def pick_six():
    numbers = []
    for nums in range(6):
        random_num = random.randint(1,99)
        numbers.append(random_num)
    return numbers

# Checks each index for matching values based on the winning numbers and the ticket numbers
def match_check(win, ticket):
    win_counter = 0
    if ticket_nums[0] == win_nums[0]:
        win_counter += 1
    if ticket_nums[1] == win_nums[1]:
        win_counter += 1
    if ticket_nums[2] == win_nums[2]:
        win_counter += 1
    if ticket_nums[3] == win_nums[3]:
        win_counter += 1
    if ticket_nums[4] == win_nums[4]:
        win_counter += 1
    if ticket_nums[5] == win_nums[5]:
        win_counter += 1
    return win_counter


# Win amount is the storage for total times a win occurs
win_amount = 0
# Times played stores the amount of times the loops has looped
times_played = 0
# Checks the amount of 'money spent'
balance = 0
while times_played < 100000:

    win_nums =  pick_six() 
    ticket_nums = pick_six()#[1,2,3,4,5,6]
    print(ticket_nums)
    print(win_nums)
    # Everytime a win occurs that value is added to the win amount storage
    if match_check(win_nums, ticket_nums) == 1:
        win_amount += 4
    if match_check(win_nums, ticket_nums) == 2:
        win_amount += 7
    if match_check(win_nums, ticket_nums) == 3:
        win_amount += 100
    if match_check(win_nums, ticket_nums) == 4:
        win_amount += 50000
    if match_check(win_nums, ticket_nums) == 5:
        win_amount += 1000000
    if match_check(win_nums, ticket_nums) == 6:
        win_amount += 25000000
   
    # Calculates the profit/loss
    balance -= 2
    # Counts how many times played
    times_played += 1

final_balance = balance + win_amount

print( f"You played {times_played} times. and you matched {win_amount} numbers.")

if final_balance < 0: 
    final_balance = str(final_balance)
    final_balance = final_balance.replace("-", "")
    print( f"Unfortunately you lost ${final_balance}.00, Thanks for playing though.")
else:
    print( f"Awesome! you made ${final_balance}!")

'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
VERSION 1
'''



'''
VERSION 2
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
'''

roi = int(final_balance) / balance
print( f"Your ROI ratio is {roi}")


'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
VERSION 2
'''

