'''
Lab 5
Pick6
'''

import random


bank = 2000000
cost = 0
while True: 
    user_nums = []
    for i in range(6):
        user_nums.append(int(input('Please enter a number 1-99: ')))    

    for i in range(100000):
        win = 0
        winings = 0
        cost + 2
        random_nums = []
        for i in range(6):
            random_nums.append(random.randint(1,99))
        # for i in range(6):
        #     user_nums.append(int(input('Please enter a number: ')))
        for number in random_nums:
            if number in user_nums:
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
    bank - cost
    if winings != 0:
        roi = (winings - cost)/ winings
        print(f' Your return on investment is {roi}')
    else:
        print('\nYou had no winnings')
    print(f'\nYour numbers {user_nums} the numbers you need to match {random_nums}')
    print(f'\nyou won {win} times and made {winings}$ your new balance is {winings + bank}') 
    play_again = input("\nWould you like to play again? 'Q' for quit or any key to continue: ")
    if play_again == 'q':
        break



    

