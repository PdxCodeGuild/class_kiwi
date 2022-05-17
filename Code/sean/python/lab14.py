import re
import requests
from time import sleep


# version 1

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

joke_dict = response.json()

joke_str = joke_dict['joke']


joke_list = re.split(pattern = r"[?!.,]",
 string = joke_str)


print(joke_list[0])
sleep(1)
print(joke_list[1])


# version 2
game = True

while game:
    search_term = input("What kind of joke would you like to hear? ")

    response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
        'Accept': 'application/json'
    })

    joke_dict = response.json()
    joke_dict = joke_dict["results"]
    jokes_list = []

    for i in joke_dict:
        joke = i["joke"]
        jokes_list.append(joke)


    for joke in jokes_list:
        
        new_joke = re.split(pattern = r"[?!.,]",
        string = joke)


        print(new_joke[0])
        sleep(1)
        print(new_joke[1])
        sleep(1)
        
        user = input("Would you like to hear another? type yes or type done: ").lower
        if user == "yes":
            continue
        else:
            game = False
            break