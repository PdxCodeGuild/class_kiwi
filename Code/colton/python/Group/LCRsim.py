import random


def get_names():
    names_scores = {}
    num = 1
    while True:
        user_name = input("enter player name")
        if user_name == "done":
            break
        else:
            names_scores.update({num : {"name" : user_name, "chips" : 3}})
            num += 1
    
    return names_scores

def dice_roll():
    rolls = ["L", "R", "C", ".", ".", "."]
    dice_roll = random.choice(rolls)
    return dice_roll



players = get_names()
pot = 0



print(players.values())

print()
while True:

    for i, keys in enumerate(players):
        dice = dice_roll()
        if (players[i]["chips"])== 0:
            break
        
        elif dice == 'L':
            (players[i]["chips"]) -= 1
            (players[i-1]["chips"]) += 1
            print("wtf")
            continue
        elif dice == "R":
            (players[i]["chips"]) -= 1
            (players[i+1]["chips"]) += 1
            print("wtf")
            continue
        elif dice == "C":
            (players[i]["chips"]) -= 1
            pot += 1
            print("wtf")
            continue
        elif dice == ".":
            print("wtf")
            continue
    
    break
        