

# Quotes API

For this lab we'll be using the [Favqs Quotes API](https://favqs.com/api) to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the `requests` library.


## Version 1: Get a Random Quote

The URL to get a random quote is [https://favqs.com/api/qotd](https://favqs.com/api/qotd), send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

## Version 2: List Quotes by Keyword

The Favqs Quote API also supports getting a list of quotes associated with a given keyword `https://favqs.com/api/quotes?page=<page>&filter=<keyword>`. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.

```
> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:
```

This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers [here](https://requests.readthedocs.io/en/master/user/quickstart/#custom-headers) and documentation on authorization with the Favqs API [here](https://favqs.com/api/) under "Authorization".

```python
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
```

## Other Quote APIs

- [Programming Quotes](https://programming-quotes-api.herokuapp.com/)
- [Quotes Garden](https://pprathameshmore.github.io/QuoteGarden/)
  - get random quote `https://quote-garden.herokuapp.com/quotes/random`
  - get quotes by keyword `https://quote-garden.herokuapp.com/quotes/search/<keyword/`

