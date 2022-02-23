"""
    Will Carter 
    Jose Ramirez
    Sean Schmidt
    Eric Hollister
    Anthony Wallace
    Matthew Holmes 
    Renan Harrigan
    Nestor Perez
"""
    
"""LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side,
and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. 
A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, 
they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.
"""

# When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. 
# We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.
import random

# create players dictionary


dice = ["L", "R", "C", "", "", ""]
keep_playing = 'y'
while keep_playing == 'y':
    center_pot = 0
    winner = False
    players = []

    # create logic for dice rolls
    while True:
        players_name = input("Please enter a players name('done' to quit): ").lower()
        if players_name == "done":
            break
        players.append({"name": players_name, "chips": 3})
            
    while winner == False:
        for index, player in enumerate(players):
            for i in range(min(player["chips"], 3)):
                dice_roll = random.choice(dice)
                if dice_roll == "L":
                    players[index-1]["chips"] += 1
                    players[index]["chips"] -= 1
                elif dice_roll == "R":
                    if index == len(players) - 1:
                        players[0]["chips"] += 1
                        players[index]["chips"] -= 1
                    else:
                        players[index+1]["chips"] += 1
                        players[index]["chips"] -= 1
                elif dice_roll == "C":
                    players[index]["chips"] -= 1
                    center_pot += 1
                else:
                    continue

            total = len(players) * 3

            if player["chips"] + center_pot == total:
                winner = True
                break
    print(f"{players[index]['name']} wins! You won {center_pot} chips!!!")
    keep_playing = input("Would you like to play again(y/n): ").lower()
    # create while loop to keep gameplay going