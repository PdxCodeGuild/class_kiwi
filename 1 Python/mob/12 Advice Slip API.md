
# Advice Slip API


Let's use the [Advice Slip API](https://api.adviceslip.com/) and [requests module](../docs/15%20Requests.md) and [json module](../../0%20General/07%20JSON,%20CSV,%20&%20XML.md#json) to write a small program to give out advice.

## Part 1

The API endpoint `https://api.adviceslip.com/advice` will return a random advice slip. Send a request to this URL and display the advice given in response.

```json
{
    "slip": {
        "id": 217,
        "advice": "Identify sources of happiness."
    }
}
```

## Part 2


Another endpoint `https://api.adviceslip.com/advice/search/{query}` will allow you to search advice slips. Prompt the user for a term to search with, put that string into the URL, send the request, and display the results.

For example `https://api.adviceslip.com/advice/search/joy` will resond with the following json:

```json
{
    "total_results": "3",
    "query": "joy",
    "slips": [
        {
            "id": 61,
            "advice": "Once in a while, eat some sweets you used to enjoy when you were younger.",
            "date": "2015-01-13"
        },
        {
            "id": 128,
            "advice": "When you're at a concert or event, enjoy the moment, enjoy being there. Try leaving your camera in your pocket.",
            "date": "2015-12-11"
        },
        {
            "id": 160,
            "advice": "Enjoy a little nonsense now and then.",
            "date": "2017-03-20"
        }
    ]
}
```





