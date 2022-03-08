#1
"""
import time
import requests
import re

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

response_dict = response.json()
joke = response_dict["joke"]


joke_list = re.split(pattern = r"[.,?!]",
         string = joke)

for i in joke_list:
    if i == '':
        del joke_list[-1]
    
print(joke_list[0])
time.sleep(3)
print(joke_list[1])
"""

#2
import time
import requests
import re

while True:

    search_term = input("What would you like to search for? Type 'done' to exit. ")
    
    if search_term == "done":
        break
    
    response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
        'Accept': 'application/json'
    })

    response_dict = response.json()
    print(response_dict)
    
    """
    joke = response_dict["joke"]


    joke_list = re.split(pattern = r"[.,?!]",
            string = joke)

    for i in joke_list:
        if i == '':
            del joke_list[-1]
        
    print(joke_list[0])
    time.sleep(3)
    print(joke_list[1])
    """

Where do rabbits go after they get married? On a bunny-moon.                                    Where do rabbits go after they get married
PZDd', 'joke': 'When does a joke become a dad joke? When it becomes apparent.'},
{'id': 'FBQ7wskbMmb', 'joke': "Want to hear a joke about construction? Nah, I'm still working on it."},
{'id': 'rc2E6EdiNe', 'joke': "Want to hear my pizza joke? Never mind, it's too cheesy."},
{'id': 'EYo4TCAdUf', 'joke': 'I tried to write a chemistry joke, but could never get a reaction.'},
{'id': '8USSSfVn3ob', 'joke': "I've been trying to come up with a dad joke about momentum . . . but I just can't seem to get it going."},
{'id': 'ozPmbFtWDlb', 'joke': "Some people say that comedians who tell one too many light  many levels."}
], 'search_term': '$joke', 'status': 200, 'total_jokes': 12, 'total_pages': 1}