# Lab 14: Dad Joke API

Use the [Dad Joke API](https://icanhazdadjoke.com/api) to get a dad joke and display it to the user. You may want to also use [time.sleep](https://www.geeksforgeeks.org/sleep-in-python/) to add suspense.


## Part 1

Use the [requests](../docs/15%20Requests.md) library to send an HTTP request to `https://icanhazdadjoke.com/` with the `Accept` header as `application/json`. This will return a dad joke in JSON format. You can then use the `.json()` method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

```python
response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})
```


## Part 2

Add the ability to "search" for jokes using [another endpoint](https://icanhazdadjoke.com/api#search-for-dad-jokes). Create a REPL that allows one to enter a search term and go through jokes one at a time.


```python
response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})
```
