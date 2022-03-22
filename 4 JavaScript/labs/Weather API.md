

# Weather API

Let's use the [OpenWeatherMap API](https://openweathermap.org/api/one-call-api) to display a weather forecast.

## Part 1: Setup

First [make an account](https://openweathermap.org/register), then copy your [api key](https://home.openweathermap.org/api_keys) and put it into a `secrets.js` file in the same directory as your `lab07-weather_api.html`. Make sure `secrets.js` is in the `.gitignore` and then add it to your html file using `<script src="secrets.js"></script>`.


## Part 2: Get the Weather

The OpenWeatherMap API requires the latitude and longitude to get the weather at a given location. To get the user's current latitude and longitude, we can use the [geolocation api](https://www.w3schools.com/html/html5_geolocation.asp). Another strategy is to use another api to get the user's IP address ([ipify](https://www.ipify.org/), and then another to get the latitude and longitude for the IP address ([ipstack](https://ipstack.com/documentation)).

```javascript
navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
})
```

Once you have the latitude and longitude, you can make the call to [OpenWeatherMap](https://openweathermap.org/api/one-call-api) to get the forecast and display the information in the page.


`https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&
exclude=hourly,daily&appid={YOUR API KEY}`


The API gives back Unix Timestamps, which are the number of seconds passed since midnight of January 1st, 1970. You can convert them to JavaScript datetimes like so...

```javascript
let unix_timestamp = 1592482891
let datetime = new Date(unix_timestamp*1000)
console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)
```

You can then use the [datetime methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#Examples) to get the different components.


## Part 3: Use Icons

We can display an icon representing the current weather, below is the data from the api, note the `icon` property.

```json
{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}
```

OpenWeatherMap provides their own [icons](https://openweathermap.org/weather-conditions#Icon-list) you can use by taking the `icon` property in the response from the api and building a url. The url can then be the `src` attribute of an `img` element.

```html
<img src="http://openweathermap.org/img/wn/04d.png"/>
```

There are also these [more minimal icons](https://websygen.github.io/owfont/). Checkout the [usage section](https://websygen.github.io/owfont/#usage) for how to use them; download the zip file, extract file `owfont-regular.css` and put it next to your `html` file, and include it in your html. Then you can use an `i` element to display the icon. For these, you'll need to use the `id` property of the weather data.

```html
<i class="owf owf-800-d"></i>
```
