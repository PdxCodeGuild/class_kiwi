"""
Requests:

"""

import requests

response = requests.get("https://google.com")

# print(response) # <Response [200]>

# print(dir(response))
"""
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', 
 '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
 '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 
 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 
 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 
 'request', 'status_code', 'text', 'url']
"""

# print(response.text)

# https://api.dictionaryapi.dev/api/v2/entries/en/<word>  replace "word" with word to seatch
# 
"""
dictonary_look_up_api = requests.get(
    "https://api.dictionaryapi.dev/api/v2/entries/en/kiwi")

# print(dictonary_look_up_api.text)

# word = dictonary_look_up_api
# print(type(word)) # <class 'list'>

word = dictonary_look_up_api.json()

# print(type(word)) # <class 'list'>

print(word[0]['meanings'][0]["definitions"][0]['definition'])
"""

word_look_up = input('Please enter the word you wish to look up: \n')

dictonary_look_up_api = requests.get(
    f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_look_up}")

word = dictonary_look_up_api.json()

print(word[0]['meanings'][0]["definitions"][0]['definition'])