def peaks(data: list[int]) -> int:
    n = len(data)
    for i in range (0, n):
        if data[i] > data [i+1] and data[i] > data[i - 1]:
            return i 
    return n 

import random 

players = [{'name': 'Gage', 'Chips': 3} , {'name': 'John', 'Chips': 3}]

dice = ['L', 'C', 'R,', '.', '.', '.']

center_pot = 0 

def roll_dice(chips):
    dice_roll = []
    for number in range (chips):
        dice_roll.append(random.choice(dice))
    return dice_roll

print(roll)