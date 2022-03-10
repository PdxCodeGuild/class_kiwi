"""
Quotes
Version 1
Timothy Hampton
Hampton12101@gmail.com 
"""

import requests


page = 1
while True:
    keyword = input("Enter a keyword to search for quotes: ")
    if len(keyword) == 0:
        break    
    
    while True:

        response = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={keyword}", headers = 
        {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})


        response_json = response.json()
        j_quotes = response_json['quotes']

        list_of_quotes = map(lambda quote:quote["author"] + " - " + quote["body"], j_quotes)
        list_of_quotes = list(list_of_quotes)
        list_length = len(list_of_quotes)
        print(f"{list_length} quotes associated with {keyword} - {page}")
        print(*list_of_quotes,sep ="\n ")
        user_input = input("enter 'next page' or 'done': ").lower()
        
        if user_input == 'next page':
            page += 1
        elif user_input == 'done':
            break
    


