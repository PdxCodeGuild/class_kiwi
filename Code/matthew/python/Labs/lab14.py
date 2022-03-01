"""
Dad joke API
"""
import requests
import time
'''
response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

dad_jokes = response.json()

joke = dad_jokes['joke']

# print(joke)
'''

# --- Version 2

response = requests.get('https://icanhazdadjoke.com/search', headers={
    'Accept': 'application/json'
})

dad_jokes_list = response.json()

# print(dad_jokes_list['results'][1]['joke'])
counter = 0
joke = dad_jokes_list['results'][counter]['joke']
break_loop = ['no', 'stop', 'quit', 'q', 'exit']
while True:
    print('Joke incoming')
    time.sleep(.5)
    print('In three')
    time.sleep(.75)
    print('two')
    time.sleep(1)
    print('one')
    time.sleep(1.25)
    print(f"\njoke")
    counter += 1
    again = input('\nWould you like to hear another one?\n')
    if again.lower() in break_loop :
        break