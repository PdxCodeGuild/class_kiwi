import requests

joke_search = input("Please enter a joke search term: ")
response = requests.get(f"https://icanhazdadjoke.com/search?term={joke_search}", headers = { 
    "Accept": "application/json"
})

joke = response.json()
joke_number = 0
user_response = "yes" 
while user_response == "yes":
    try:
        if user_response == "no":
            break
        else:
            print(joke["results"][joke_number]["joke"] + "\n")
            joke_number += 1
            user_response = input(f"Would you like to hear the next {joke_search} joke? ")
    except IndexError as error: # If there are no more jokes then an IndexError will occur
        print(f"There are no more {joke_search} jokes.")
        break