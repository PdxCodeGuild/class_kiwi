
import requests
import time

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

print(response)
dad_joke_reposit = response.json()
# print(lab_14)
print(dad_joke_reposit['joke'])

time.sleep(6)

while True:
    user_search = input("Please enter a search term, you may type 'exit' at anytime to exit: ")
    if user_search == 'exit':
        break
    else:
        dad_joke_repl = requests.get(f"https://icanhazdadjoke.com/search?term={user_search}", headers={ 'Accept': 'application/json'})
        ver_two = dad_joke_repl.json()

        print(ver_two['results'][0]['joke'])


# dad_joke_list = []
# while True: 
#     for punctuation in string.punctuation:
#         if punctuation in (dad_joke_rep ['joke']):
#             dad_joke_split = dad_joke_rep['joke'].split(punctuation)
#             dad_joke_list.append(dad_joke_split)
#     break
