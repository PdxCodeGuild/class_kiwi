'''
Lab 5
Pick6
'''

import random

def generate_rand_num(random_nums:list):
    '''
    Adds 6 random numbers to empty list'''
    for i in range(6):
        random_nums.append(random.randint(1,99))
    return random_nums

def generate_user_num(user_nums:list):
    '''input 6 numbers from input into an empty list'''
    for i in range(6):
        user_nums.append(int(input('Please enter a number 1-99: ')))
        
    return user_nums
    
def pick6(interations:int):
    '''Will Compare 6 numbers of your choosing to 6 randomly generated numbers'''
    while True: 
        cost = 0
        bank =  500000
        user_nums = []
        random_nums = []
        generate_rand_num(random_nums)
        generate_user_num(user_nums)

        winings = 0
        for i in range(interations):
            win = 0
            cost += 2
            # for number in random_nums:
            #     if number in user_nums:  
            for number in range(len(random_nums)):
                if random_nums[number] == user_nums[number]:
                    win += 1
            if win == 1:
                winings += 4
            elif win == 2:
                winings += 7
            elif win == 3:
                winings += 100
            elif win == 4:
                winings += 50000
            elif win ==5:
                winings += 1000000
            elif win == 6:
                winings += 25000000        
        
        bank -= cost
        if winings != 0:
            roi = (winings - cost)/ winings             # -- Version 2
            print(f' Your return on investment is {roi} and your cost was ${cost}')
            print(f'\nyou won {win} times and made {winings}$ your new balance is {winings + bank}')
        else:
            print(f'\nYou had no winnings and your cost was ${cost}')    
            print(f'\nyou won {win} times and made {winings}$ your new balance is {winings + bank}') 
        play_again = input("\nWould you like to play again? Press 'q' for quit or any key to continue: ")
        if play_again.lower() == 'q':
             break

if __name__ == '__main__':
    pick6(100000)





    

