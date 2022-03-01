import requests
import time

# request to retrieve random dad joke the url from an API
# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json',
# })
# search a dad joke
while True:
    user = input("Would you like to search a joke? yes or no ").lower()
    if user == 'no':
        break
    elif user == 'yes':
        search_term = input(f'Search a joke here: ')
        response2 = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
            'Accept': 'application/json'
        })
        joke2 = response2.json()
        holder = 0
        for x in response2:
            print(joke2['results'][holder]['joke'])
            user = input(
                'Would you like to see the next joke? yes or no: ').lower()
            if user == 'no':
                break
            elif user == 'yes':
                holder += 1
            else:
                print("please enter yes or no")
    else:
        print("please enter yes or no")
    # prompt user to repeat again


# transforming from string to json data
# joke = response.json()
# # time.sleep method for delay
# time.sleep(3)
# print(joke['joke'])
