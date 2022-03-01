import requests

response = requests.get("https://icanhazdadjoke.com", headers = { 
    "Accept": "application/json"
})

joke = response.json()

print(joke["joke"])