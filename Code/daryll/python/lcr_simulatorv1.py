
# Johnathan Murphy, Gage Lieble, Joseph Brown-Womack, Shaina Davis, Chad Lattimer, Daryll Selga, Ian Davis-TA
import random

while True:
    players = []
    dice = ["L", "C", "R", ".", ".", "."]
    center_pot = 0

    def roll_dice(chips):
        # Determines how many times a player can roll the dice.
        dice_roll = []
        if chips > 3: # if user has more than 3 chips, limit dice rolls to 3.
            for number in range(3):
                dice_roll.append(random.choice(dice))
        else:
            for number in range(chips): # if user has 3 chips or less, roll dice = to number of chips
                dice_roll.append(random.choice(dice))
        return dice_roll

    def rules(player):
        # Determines if a player rolls an 'L', 'R', or 'C', to pass the chip either left, right or center pot.
        dice_results = roll_dice(players[player]["chips"])
        for dice in dice_results:
            if dice == ".": # If player rolls a '.', then continue
                continue
            elif dice == "L": # If player rolls an 'L', playerpasses chip to left
                players[player]["chips"] -= 1
                players[player - 1]["chips"] += 1
            elif dice == "R": 
                players[player]["chips"] -= 1 
                if player == len(players) - 1: # If player rolls an 'R' and is the last player, then player passes chip to first player
                    players[0]["chips"] += 1
                else:
                    players[player + 1]["chips"] += 1 # Else if player rolls an 'R', player passes chip to right
            elif dice == "C": # Player passes chip to center pot
                players[player]["chips"] -= 1
                global center_pot 
                center_pot += 1

    def winner():
        # Determines a winner by adding all players with zero chips to broke_players, once there is only one winning player, the function returns the winning player and exits
        broke_players = 0
        winning_player = []
        for item in range(len(players)):
            if players[item]["chips"] == 0:
                broke_players += 1
            if players[item]["chips"] >= 1:
                winning_player.append(players[item]["name"])
        if len(winning_player) == 1:
            return winning_player

    while True:
        user_player = input("Enter player name or type 'done': ")
        if user_player == "done":
            break
        else:
            players.append({"name": user_player, "chips": 3})

    while winner() == None: # If the winning_player is None the loops continues to run until a winning player is determined.
        for player in range(len(players)):
            rules(player)
            winner()
    print(f"\nThe winner is: {winner()}")
    print(f"Center Pot: {center_pot}")
    
    play_again = input("Do you want to play again? 'y' or 'n': ")
    if play_again == "n":
        break
    else:
        continue
        