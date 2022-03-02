# Lab 14-v2 Dad Joke API
'''
Add the ability to "search" for jokes using another endpoint. Create a REPL 
that allows one to enter a search term and go through jokes one at a time.
'''

import requests

search_term = input("enter a search term: ")

response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})

json_results = response.json()
results = json_results['results']
joke = results[0]['joke']
print(joke)
joke_number = 0

try:
  for item in response:
      another_joke = input(f"Press the return key for another {search_term} joke or type 'done' to quit:")
      if another_joke == 'done':
        break

      joke_number += 1
      print(results[joke_number]['joke'])

except IndexError:
    print(f"That was all of the {search_term} jokes")