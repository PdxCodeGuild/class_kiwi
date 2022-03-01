import random
wallet = 0
ticket = 2
match = 0
total_matches = 0
total_matches_1 = 0
total_matches_2 = 0
total_matches_3 = 0
total_matches_4 = 0
total_matches_5 = 0
total_matches_6 = 0
total_games = 0
winnings = 0

def rand_6():
    # Generates a list of random numbers from 1 to 99
    numbers = []
    for i in range(6):
        number = random.randint(1, 99)
        numbers.append(number)
    return numbers

# Iterates through 100,000 games randomly picking the user ticket and winning ticket minus $2 for each game played
for x in range(100000):
    user_ticket = rand_6()
    winning_ticket = rand_6()
    wallet -= ticket
    # Adds the number of matches for each game
    if user_ticket[0] == winning_ticket[0]:
        match += 1
    if user_ticket[1] == winning_ticket[1]:
        match += 1
    if user_ticket[2] == winning_ticket[2]:
        match += 1
    if user_ticket[3] == winning_ticket[3]:
        match += 1
    if user_ticket[4] == winning_ticket[4]:
        match += 1
    if user_ticket[5] == winning_ticket[5]:
        match += 1
    # Determine total money won for each game
    if match == 1:
        winnings = 4
        total_matches_1 += match
    elif match == 2:
        winnings = 8
        total_matches_2 += match
    elif match == 3:
        winnings = 100
        total_matches_3 += match
    elif match == 4:
        winnings = 50000
        total_matches_4 += match
    elif match == 5:
        winnings = 1000000
        total_matches_5 += match
    elif match == 6:
        winnings = 25000000
        total_matches_6 += match
    
    total_games += 1 # Adds to total number of games played
    total_matches += match # Adds number of matches to total matches
    wallet += winnings # Add winning money to current wallet
    winnings = 0 # Resets money won for each game
    match = 0 # Reset number of matches for each game

print(f"""
Total games played: {total_games}\n
Total games matching 1 number: {total_matches_1}
Total games matching 2 number: {total_matches_2}
Total games matching 3 number: {total_matches_3}
Total games matching 4 number: {total_matches_4}
Total games matching 5 number: {total_matches_5}
Total games matching 6 number: {total_matches_6}
Total matching numbers: {total_matches}
""")
currency = "${:,}".format(wallet)
print(f"Your current wallet: {currency}")