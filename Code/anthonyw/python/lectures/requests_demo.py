import requests

# user_definition = input("Please enter a word: ")

# response = requests.get(
#     f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_definition}")

# word = response.json()

# print(word[0]["meanings"][0]["definitions"][0]["definition"])


url = "https://uselessfacts.jsph.pl/random.json?language=en"

response = requests.get(url)

fact = response.json()
print(fact['text'])
