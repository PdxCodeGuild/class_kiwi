###  Lab 15 Practice  ###
################################
##                            ##
## Lab 15: Quotes API         ##
##   Author: Anthony Bilie    ##
##   Date: 03/022022          ##
##                            ##
################################

"""
For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.

Version 1: Get a Random Quote

The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

"""
#import requests
import requests
# url for random quote
url = "https://favqs.com/api/qotd"
# send get request to api
response = requests.get(url)
# convert to json data
quote = response.json()
# parse json data to find actual quote
qod = (quote['quote']['body'])
# parse json data to find author
author = (quote['quote']['author'])
print(f"""
Quote of the day: {qod}
Author: {author}
""")
