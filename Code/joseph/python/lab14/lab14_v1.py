# Lab 14 - Dad Joke API - Version 1 - Working Final
'''
Use the Dad Joke API to get a dad joke and display it to the user.
You may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/
with the Accept header as application/json. This will return a dad joke in JSON
format. You can then use the .json() method on the response to get a dictionary
Get the joke out of the dictionary and show it to the user.

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})
'''

# imports
import requests
import random

# define request response
response_json = requests.get(
    "https://icanhazdadjoke.com",
    headers={"Accept": "application/json"}
).json()

joke = response_json["joke"]

print(joke)