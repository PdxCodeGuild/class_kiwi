# Lab 14: Part 1

import requests

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

jokes = response.json()

joke = jokes['joke']

print(joke)

# Lab 14: Part 2

in_valid = ['yes', 'yep', 'yeah', 'yup', 'y', 'yea']

while True:
    search_term = input("Choose a dad joke genre or type done: ")

    if search_term == 'done':
        print('Goodbye ..... I personally prefer Bestbuy')
        break

    response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
    })
    
    i = 0
    while in_valid:
        jokes_results = response.json()
        jokes = jokes_results['results']
        print(jokes_results['total_jokes'])
        
        if i == jokes_results['total_jokes']:
            print("We've given it all we got captain. There are no more results to show!")
            break

        joke = jokes_results['results'][i]['joke']
        print(joke)
        
        next_joke = input('Do you want the next joke?: ').lower()
        if next_joke in in_valid and i + 1 <= jokes_results['total_jokes']:
            i += 1
            continue
        else:
            break

