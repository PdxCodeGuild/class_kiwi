import requests
#fetching the data...put the data in a variable to be able to print later
# response = requests.get("https://google.com") 
#dir allows you to see what properties
# print(dir(response))
# print(response.text) gets you all the code for said web address
# print(response.text)

#Using API's https://dictionaryapi.dev/
user_definition = input("Please enter a word: ")

response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_definition}") 

word = response.json()                                                           

print(word[0]["meanings"][0]["definitions"][0]["definition"])


