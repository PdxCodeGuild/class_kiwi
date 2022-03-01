
import requests

# useless_facts_api = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
# print(useless_facts_api)

url = "https://uselessfacts.jsph.pl/random.json?language=en"

response = requests.get(url)

random_fact = response.json()

print(random_fact['text'])



