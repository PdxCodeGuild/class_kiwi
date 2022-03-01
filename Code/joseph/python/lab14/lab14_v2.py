# Lab 14 - Dad Joke API - Version 2 - Working Final
'''
Use the Dad Joke API to get a dad joke and display it to the user.
You may want to also use time.sleep to add suspense.

Part 2
Add the ability to "search" for jokes using another endpoint. Create a REPL
that allows one to enter a search term and go through jokes one at a time.

response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}",
headers={'Accept': 'application/json'}
)
'''

# imports
import requests
import random
import time

# define search term
term = input("Welcome to Dad's Joke World, please input a topic: ")

# define request response
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()

# set variables for jokes and number of jokes on the topic
jokes = response_json["results"]

total_jokes = response_json["total_jokes"]

# loop through jokes, print the joke or break if jokes = 0
if total_jokes > 1:
    for i in range(len(jokes)):
        print(f"I found {total_jokes - i} jokes about {term}. Here's one:\n")
        time.sleep(3)
        print(jokes[i]['joke'],"\n")
        cont = input("Would you like to see the next one? Press Y for yes:"
        ).upper()
        if cont == "Y":
            continue
        else:
            break
elif total_jokes == 1:
    print(f"I got one, and only one, joke about {term}. Here it is:\n",
    jokes[0]["joke"]
    )
else:
    print(f"Wow, you have terrible taste in jokes:\n{term} has 0 jokes.\n  Please try again"
    )

