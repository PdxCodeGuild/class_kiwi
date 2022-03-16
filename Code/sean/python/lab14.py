import re
import requests
from time import sleep


#version 1
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

