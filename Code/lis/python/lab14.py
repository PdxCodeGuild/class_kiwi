# Lab 14 Dad Joke API
'''
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the Accept header
as application/json. This will return a dad joke in JSON format. You can then use the .json() method 
on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.
'''

import requests

response = requests.get("https://icanhazdadjoke.com/", headers={
    'Accept': 'application/json'
})

json_file = response.json()
joke = json_file['joke']

print(joke)