'''         +-+#^#+--+#^#+--+#^#+-+             
                Project: Pick6                    ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/9/22                     ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''

##### Version 1 did not ever get a winner for me, when comparing index position as well ######


import random

winners = []

# Append a list six times with a random number
for x in range(6): 
    x = random.randint(1, 99)
    winners.append(x)


# test = [1, 2, 3, 4, 5]
# test2 = [5, 4, 2, 3, 1]
user_tickets = []


cost = 0
matches = 0
player_earnings = 0

print(f"{winners} These are the winning numbers")
# # Loop 100,000 times generating new ticket each time
# # Update balance
# # Check for winning numbers
# # Add any winnings to balance

for i in range(100000):
    # adds 2 dollars to player balance for each ticket
    cost += 2
    # generate list of 6 random numbers
    for x in range(6): 
        x = random.randint(1, 99)
        user_tickets.append(x)
        
    for i, num in enumerate(user_tickets): # compares user_tickets(index, value) to winners(index, value)
        if num == winners[i]:  
            matches += 1

### if the index of a number matches the num in the same index within winners add 1 to matches, 
### after each ticket compare to match pay out and pay accordingly 
    if matches == 1:
        player_earnings += 4
    elif matches == 2:
        player_earnings += 7
        print("here's 7")
    elif matches == 3:
        player_earnings += 100
        print("here's a 100")
    elif matches == 4:
        player_earnings += 50000
        print(user_tickets)
    elif matches == 5:
        player_earnings += 100000
        print(user_tickets)
    elif matches == 6:
        player_earnings += 25000000
        print(user_tickets)            


            

    user_tickets = [] # Resets user_tickets list back to blank after each ticket has been reviewed
    matches = 0 # Resets matches per ticket back to zero



# Print total cost, earnings, return on investment after 100,000 tickets
print(f"""
    *Total Cost*           *Earnings*
      {-cost}$               {player_earnings - cost}$     
      
      -Return on Investment-
          {round((player_earnings - cost)/cost, 2)}$ """) 



