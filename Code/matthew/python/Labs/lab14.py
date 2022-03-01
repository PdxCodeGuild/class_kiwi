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
# """
# response = requests.get('https://icanhazdadjoke.com/search?term=&page=1', headers={
#     'Accept': 'application/json',
# })
# dad_jokes_list = response.json()
# print(dad_jokes_list)

# print(dad_jokes_list['results'][1]['joke'])

counter = 0
break_loop = ['no', 'stop', 'quit', 'q', 'exit']
yes = ['yes','yeah','yea','ya','y']

while True:

    if counter == 0:
        response = requests.get(f'https://icanhazdadjoke.com/search?term=&page=1', headers={
    'Accept': 'application/json',
    })
    elif counter >= 1:
        change_pg = input('Would you like to change the page your on?: \n')
        if change_pg in yes:
            page = input('What page do you want to start on? \n')
            for i in page:
                while True:
                    if i.isdigit() == False:
                        page = input('What page do you want to start on? \n')
                    else:
                        break
        response = requests.get(f'https://icanhazdadjoke.com/search?term=&page={page}', headers={
        'Accept': 'application/json',
        })

    dad_jokes_list = response.json()
    joke = dad_jokes_list['results'][counter]['joke']

    # print(dad_jokes_list['current_page'])
    
    print('Joke incoming')
    time.sleep(.5)
    print('In three')
    time.sleep(.75)
    print('two')
    time.sleep(1)
    print('one')
    time.sleep(1.25)
    print(f"\n{joke}")
    counter += 1
    again = input('\nWould you like to hear another one?\n')
    if again.lower() in break_loop :
        break

# """
# --- Term search
'''

break_loop = ['no', 'stop', 'quit', 'q', 'exit']
yes = ['yes','yeah','yea','ya','y']
counter = 0
while True:
    look_up_wrd = input('What type of jokes do you want to hear? (enter a keyword):\n')

    url = f'https://icanhazdadjoke.com/search?term={look_up_wrd}'
    response = requests.get(url, headers={
        'Accept': 'application/json'
    })
    dad_jokes_list = response.json()

    joke = dad_jokes_list['results'][counter]['joke']
    print('Joke incoming')  
    time.sleep(.5)
    print('In three')
    time.sleep(.75)
    print('two')
    time.sleep(1)
    print('one')
    time.sleep(1.25)
    print(f"\n{joke}")
    counter += 1
    again = input('\nWould you like to hear another one?\n')
    if again.lower() in break_loop :
        break
    different_word = input("would you like to look for a different kind of joke?: \n")
    if different_word.lower() in yes:
            look_up_wrd = input('What type of jokes do you want to hear? (enter a keyword):\n')
#  '''

# # from PIL import Image
# from io import BytesIO
# # import urllib
# response = requests.get("https://icanhazdadjoke.com/j/<joke_id>.png")

# # print(dir(response))
# print(response.url)
# # print(response.raw) # <urllib3.response.HTTPResponse object at 0x0000020FB1511BD0>

# joke_image = response.url

# # with open('sample_image.png', 'wb') as file:
# #     file.write(joke_image)
# #     file.close()


# urllib.request.urlretrieve(joke_image,'C:\Users\wmatt\Pictures')


