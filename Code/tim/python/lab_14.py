"""
Dad Jokes API
Version 1
Timothy Hampton
Hampton12101@gmail.com 
"""
import requests


response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})
# print(response)
text = response.json()
# print(text)

dad_joke = text['joke']
# print(joke)
# version one complete

search_term = input("What would you like to search? Or press enter to cancel. ")
search_response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})
search = search_response.json()
# print(search)
search_array = search["results"]

while len(search_term) >= 1:
    for x in search_array:
        dj = x['joke']
        # print(dj)
        cont = input("Would you like to see the next result for your dad joke search? Y or N ").lower()
        
        if cont == "y":
            print(dj)
        else:
            break
    
    search_term = input("What would you like to search? Or press enter to cancel. ")
    search_response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
    })
    search = search_response.json()
    search_array = search["results"]
