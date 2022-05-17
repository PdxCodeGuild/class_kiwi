# Mob Lab
# Anthony Billie
# Zeke Wells
# Timothy Hampton
# Lis Fano
# Colton Tatum
# Irron Williams
# Victory Amunga
"""
LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

# Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

# If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

# When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.
"""
import random

# While statement until user enters 'done'
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")
player3 = input("Enter your name: ")

players = {
    player1: 3,
    player2: 3,
    player3: 3
}


# def get_names():
#     player = []
#     while True:
#         user_name = input("Enter player name: ")
#         num = 1
#         if user_name == 'done':
#             break
#         else:
#             player.append({"name": user_name, "chips": 3})
#     return player


def dice_roll():
    dice_side = ['L', 'C', 'R', '.', '.', '.']
    dice = random.choice(dice_side)
    return dice

# For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

# ask the player whether they'd like to play again.


# player = get_names()
game_over = False
while game_over == False:
    center_pot = 0
    for i in players:
        dice = dice_roll()
        # if players[player1] == 0 and players[player2] == 0 or players[player2] == 0 and players[player3] == 0 or players[player3] == 0 and players[player1] == 0:
        #     print("game over")
        #     game_over = True
        #     break
        if dice == ".":
            continue
        elif dice == "L":
            if i == player1:
                players[player1] -= 1
                players[player3] += 1
            elif i == player2:
                players[player2] -= 1
                players[player1] += 1
            elif i == player3:
                players[player3] -= 1
                players[player2] += 1
        elif dice == "R":
            if i == player1:
                players[player1] -= 1
                players[player2] += 1
            elif i == player2:
                players[player2] -= 1
                players[player3] += 1
            elif i == player3:
                players[player3] -= 1
                players[player1] += 1
        elif dice == "C":
            if i == player1:
                players[player1] -= 1
                center_pot += 1
            elif i == player2:
                players[player2] -= 1
                center_pot += 1
            elif i == player3:
                players[player3] -= 1
                center_pot += 1
    game_over == True

# While statement to run program

# create lcr as functions
