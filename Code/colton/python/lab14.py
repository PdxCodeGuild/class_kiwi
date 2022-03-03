'''         +-+#^#+--+#^#+--+#^#+-+             
             Project: Dad Joke API                ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/25/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''

# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
# with the accept header as application/json.
# This will return a dad joke in JSON format.
# You can then use the .json() method on the response to get a dictionary. 
# Get the joke out of the dictionary and show it to the user.

# Add the ability to "search" for jokes using another endpoint. 
# Create a REPL that allows one to enter a search term and go through jokes one at a time. 
# You can also add support for multiple pages.


# access requests library
def random_joke_generator():
    """Pulls random joke from icanhazdadjoke.com and returns a joke"""
    import requests
    response = requests.get("https://icanhazdadjoke.com/",
    headers = {"User-Agent": "My Library (https://github.com/Tatumc4561/fantastic-broccoli)", 
    "Accept": "application/json"})

    # print(dir(response))
    joke_library = response.json()

    random_joke = joke_library['joke']
    x = (f"""
***************************************************************************************************
{random_joke}
***************************************************************************************************
""")


    return x




def joke_search():
    """Creates a REPL to search a joke on icanhazdadjoke.com"""
    
    import time
    import requests

    while True:
        
        user_choice = input(f"Would you like to hear a joke? Yes or No\n").lower().strip()


        if user_choice == "no":
            return "I don't want to hear any jokes"
        
        else:
            
            try:
                user_category = input("Enter a catergory for the joke:  ")
                
                # Send request to icanhazdadjoke.com/search  + query string parameter "?term=''", "?"
                search_response = requests.get(f"https://icanhazdadjoke.com/search?limit=30&term={user_category}",
                headers = {"Accept": "application/json",
                        "User-Agent": "My Library (https://github.com/Tatumc4561/fantastic-broccoli)"}) 
                joke_search_lib = search_response.json()
                
                joke_num = 0 # index of current joke
                joke_search = joke_search_lib['results'][joke_num]['joke'] # Calls the joke within a "joke_num" dictionary 
                
                time.sleep(2)
                print(f"""
***************************************************************************************************
{joke_search}
***************************************************************************************************
""")
                
            except IndexError: # index doesn't exit within the search_reponse.json()
                time.sleep(1)
                print(f"""
***************************************************************************************************
                    Sorry no categories for {user_category} exist
***************************************************************************************************
""")
                continue  
            
            while True:
                next_joke = input(f"Would you like another {user_category} joke?\n").lower().strip()
                if next_joke == "no":
                    break
                else:
                    joke_num += 1 # updates current joke index
                    try:
                        time.sleep(1)
                        joke_search = joke_search_lib['results'][joke_num]['joke']
                        print(f"""
***************************************************************************************************
{joke_search}
***************************************************************************************************
""")
                        continue
                        
                    except IndexError: # index for joke did not exist
                        time.sleep(1)
                        print(f"""
***************************************************************************************************
                    That was all the jokes, sorry, try a different category
***************************************************************************************************
""")                
                        joke_num = 0
                        break
                    
            continue
               
                    

    




def main():

    print(random_joke_generator())
    joke_search()



if __name__ == "__main__":
    main()