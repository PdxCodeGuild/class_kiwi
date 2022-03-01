## Lab 14 Dad Joke API

#Use Dad Joke API to retrieve and display a dad joke. It may not be funny
#version 1

#import the modules to use
import time
import requests

#set up URL as a variable
url = "https://icanhazdadjoke.com"

#setting up get request
# response = requests.get("https://icanhazdadjoke.com", headers={
    # 'Accept': 'application/json'
# })

# setting up joke as a json file (list)
# joke = response.json()

# print(joke['joke'])

#version 2 
#create the input
search_term = input('In a word, what kind of jokes are you looking for: ')

#add search term to API request
response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})


joke = response.json()

#set a timer
time.sleep(1)
#print the first joke
print(joke['results'][0]['joke']) 

# create a loop to get the jokes
for i in range(len(joke)):
    answer = input('Would you like to hear another one? (y/n) ').lower()
             
    if answer == 'y':
        time.sleep(3)
        print(joke['results'][i+1]['joke']) 
    
    elif answer == 'n':
        print('See you next time')
        break
    
    else:
        print('not a valid response')
        continue
