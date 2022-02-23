'''
Lab 5
Pick6

I messed up my orignal lab 5, I had the user choosing their own numbers and I think I the win counter was 
working the way it was supposed to
'''

import random

def generate_rand_num(random_nums:list):
    '''
    Adds 6 random numbers to empty list'''
    for i in range(6):
        random_nums.append(random.randint(1,99))
    return random_nums

def generate_user_num(user_nums:list):
    for i in range(6):
        user_nums.append(random.randint(1,99))
    return user_nums
        
    
def pick6(interations:int):
    '''Will Compare 6 random numbers to 6 randomly generated numbers'''
    cost = 0
    bank =  0
    matches = 0
    winings = 0
    random_nums = []
    generate_rand_num(random_nums)
    for i in range(interations):
        user_nums = []
        # print(random_nums)
        generate_user_num(user_nums)
        # print(user_nums)
        cost += 2
    
        for number in range(len(random_nums)):
            win = 0
            if random_nums[number] == user_nums[number]:
                matches += 1
                win += 1
            if win == 6:
                winings += 25000000
            elif win == 5:
                winings += 1000000
            elif win == 4:
                winings += 50000
            elif win == 3:
                winings += 100
            elif win ==2:
                winings += 7
            elif win == 1:
                winings += 4        
    
    bank -= cost
    if winings != 0:
        roi = (winings - cost)/ winings             # -- Version 2
        print(f'\nYour return on investment is {roi} and your cost was ${cost}')
        print(f'\nyou won {matches} times and made {winings}$ your new balance is {winings + bank}')
    else:
        print(f'\nYou had no winnings and your cost was ${cost}')    
        print(f'\nyou won {matches} times and made {winings}$ your new balance is {winings + bank}') 
    

if __name__ == '__main__':
    pick6(100000)





    