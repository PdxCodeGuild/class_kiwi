


# Any API

Pick any API and build an command-line interface to read data. 

1. Look through the documentation, figure out the endpoints (urls) and parameters (query string, headers)
2. Try entering the url into the address bar of your browser and see if you can get JSON in response.
3. Look into how the API does authentication. Some APIs don't require authentication. Some might have to register an account to get an API key, and then you'll have to put the API key in the query string or in a request header.
4. Try sending the request through from Python using `requests`, look at the format of the response, and if necessary copy the json into a JSON viewer to pick through it.
5. Pick through the data, using keys for dictionaries and indices for lists.


## Lists

- [List from Mixed Analytics](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)
- [List on GitHub](https://github.com/public-apis/public-apis)
- [Another list on GitHub](https://github.com/n0shake/Public-APIs)
- [ApiList.fun](https://apilist.fun/)
- [programmableweb.com](https://www.programmableweb.com/category/all/apis)
- [public-apis.io](https://public-apis.io/)
- [public-apis.xyz](https://public-apis.xyz/)

## Some Selected APIs

- Astronomical Data: [api.nasa.gov](https://api.nasa.gov/#live_example)
- Books: [openlibrary.org](https://openlibrary.org/dev/docs/api/books)
- Cats: [TheCatAPI](https://thecatapi.com/)
- Jokes: [JokeAPI](https://sv443.net/jokeapi/v2/)
- Legos: [Brickset API](https://brickset.com/tools/webservices/v2) **responds with [XML](https://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python)**
- Number Facts: [numbersapi.com](http://numbersapi.com/#42)
- Photos: [flickr.com](https://www.flickr.com/services/api/) (requires key)
- Plants: [Trefle](https://trefle.io/)
- Pokemon: [PokeAPI](https://pokeapi.co/)
- Trivia: [opendb.com](https://opentdb.com/api_config.php)
- USA Population Data: [datausa.io](https://datausa.io/about/api/)
- Users: [randomuser.me](https://randomuser.me/documentation), [reques.in](https://reqres.in/), [jsonplaceholder](https://jsonplaceholder.typicode.com/)
- Weather: [OpenWeatherMap](https://openweathermap.org/api)

