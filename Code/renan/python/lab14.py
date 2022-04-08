import requests


# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json'
# })

# joke = response.json()                                                           

# print(joke)

#Part 2

search_term = input("Please enter a term: ")


response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})

#Create REPL 
def search(search_term):
    success = True 
#Conditional Statement
    if response == :
        print('Tell Me Another Joke') 
    
    else:
        print("Thank You For Your Humor, but I can't laugh anymore")
        success = False 
    return success 

joke = response.json()                                                           

print(joke)

