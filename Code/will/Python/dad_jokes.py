import requests

# Dad Joke API - Part 1
# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json'
# })
# joke = response.json()

# print(joke['joke'])


# Dad Joke API - Part 2

more_jokes = True

while more_jokes == True:

    search_term = input("What do you want your dad joke to be about? ")
    response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
        'Accept': 'application/json'
    })

    your_joke = response.json()
    total = your_joke['total_jokes']
    print(total)
    counter = 0
    
    if total == 0:
        print("No jokes exist for that term, please try again.")

    else:
        for i in range(total):
            print(your_joke['results'][i]['joke'])
            counter += 1
            get_more = input("Would you like to get another joke, y/n? ")
        
            if get_more == "y" and counter == total:
                print("There are no more jokes for this term, enter another.")
                break
            elif get_more == "y" and counter != total:
                continue
            else:
                more_jokes = False
                break
