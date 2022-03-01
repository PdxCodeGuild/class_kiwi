# lab 14: Dad Joke API
# Version 1

import requests
import sys

# response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})

# dad_joke = response.json()
# print(dad_joke['joke'])

# Version 2
quit = True
while quit:
    search = input("What topic would you like to hear about? ")
    # response = requests.get("https://icanhazdadjoke.com/search?{search}", headers={'Accept': 'application/json'})
    response = requests.get("https://icanhazdadjoke.com/search", params={"term": search}, headers={'Accept': 'application/json'})
    dad_joke = response.json()
    user = input("Would you like to hear a joke?[y/n]: ").lower()
    
    if user == 'y':
        try:
            print(dad_joke['results'][0]['joke'])
            continue
        except IndexError:
            print(f"Sorry, there are no jokes about {search}. Please enter a different topic.")
            continue
    elif user == 'n':
        quit = False
    else:
        print("Sorry, command not recognized. Please enter either 'y' or 'n'")
        continue