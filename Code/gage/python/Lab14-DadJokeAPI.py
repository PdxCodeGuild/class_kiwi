import requests

'''

# PART 1

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

dad_joke = response.json()['joke']

print(dad_joke)

'''

# PART 2
while True:
    joke_index = 0  # Tracks the index value for each joke
    user_search = input("Search for a joke or type 'exit': ")
    if user_search == "exit":
        break
    else:
        print(f"Results for : {user_search}") # shows the user what they searched for
        response = requests.get( f"https://icanhazdadjoke.com/search?term={user_search}", headers={ # Gathers API
        'Accept': 'application/json'
    })
        search_result = response.json()['results'][joke_index]['joke'] # Gathers the joke as a string through the index and key values of the api data
        # Formatted for user in Terminal V
        print(f"""
-----------Joke {joke_index + 1}---------
{search_result}
--------------------------""")

        while True:
            next_joke = input( f"Would you like to see the next result for {user_search} y/n?: ") # Loops through the entire list of jokes
            if next_joke == 'y':
                joke_index += 1 # Adds one to the index value to get next joke string
                if joke_index == len(response.json()['results']): # Checks if the user has reached the end of the joke list
                    # Formatted for user in Terminal V
                    print("""
--------------------------                   
You've reached the end of the page! 
--------------------------""")
                    break
                else:
                    next_result = response.json()['results'][joke_index]['joke']
                    # Formatted for user in Terminal V
                    print(f"""
-----------Joke {joke_index + 1}----------
{next_result}
--------------------------""")
                
            else:
                break

    


