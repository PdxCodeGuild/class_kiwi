
# AJAX

AJAX stands for "asynchronous javascript and XML", and allows you to execute HTTP requests from JavaScript. You can read more about AJAX [here](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started), [here](https://developer.mozilla.org/en-US/docs/AJAX) and [here](https://www.w3schools.com/xml/ajax_intro.asp).


- [AJAX in Axios](#ajax-in-axios)
  - [Setting Query Parameters](#setting-query-parameters)
  - [Setting Custom Request Headers](#setting-custom-request-headers)
  - [Sending Data](#sending-data)
- [AJAX in Vanilla JavaScript](#ajax-in-vanilla-javascript)
- [AJAX in jQuery](#ajax-in-jquery)
- [CORS](#cors)
- [JSONP](#jsonp)



## AJAX in Axios

[Axios](https://github.com/axios/axios) is a JavaScript library which handles AJAX more succinctly. Ultimately it's built upon vanilla JavaScript, so it doesn't offer anything you can't otherwise do with vanilla JS.

```es6
axios({
  method: 'get',
  url: 'https://favqs.com/api/qotd'
}).then((response) => {
  console.log(response.data)
})
```

### Setting Query Parameters

You can set query parameters using string concatenation or by setting the `params` property. Just remember that if you use string concatenation, you may have to use `encodeURIComponent` if the value has special characters in it. If you use `params` with Axios, it will automatically encode your parameters for you.

```javascript
let business_name = 'Schmitt & Associates'
let url1 = "http://example.com/?business=" + business_name
let url2 = "http://example.com/?business=" + encodeURIComponent(business_name)
console.log(url1) // INVALID: http://example.com/?business=Schmitt & Associates
console.log(url2) // VALID: http://example.com/?business=Schmitt%20%26%20Associates
```

The code below sends the request to `https://opentdb.com/api.php?amount=10&category=18&difficulty=easy`

```javascript
axios({
    method: 'get',
    url: 'https://opentdb.com/api.php',
    params: {
        amount: 10,
        category: 18,
        difficulty: 'easy'
    }
}).then((response) => {
    this.questions = response.data.results
})
```

### Setting Custom Request Headers

Depending on the API specification, you may need to put an API key inside the headers of the request.

```javascript
axios({
    method: 'get',
    url: 'https://favqs.com/api/qotd',
    headers: {
        'x-api-key': 'api_key'
    }
}).then((response) => {
    console.log(response.data)
})
```

### Sending Data

```javascript
axios({
    method: 'post',
    url: 'https://favqs.com/api/qotd',
    data: {
        name: 'joe',
        age: '34'
    }
}).then((response) => {
    console.log(response.data)
})
```

## AJAX in Vanilla JavaScript

Here's how to execute an AJAX request in native JavaScript. You can read more about XMLHttpRequest [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest). If you have many query parameters, consider using a function to [convert an object](https://stackoverflow.com/questions/111529/how-to-create-query-parameters-in-javascript). Remember status 200 means 'success'.

```javascript
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
    }
};
xhttp.open("GET", 'https://api.iify.org/?format=json');
xhttp.send();
```

The possible values for `readyState` are shown below, you can find more info [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState)
- 0 UNSENT: the request has not yet been sent
- 1 OPENED: the connection has been opened
- 2 HEADERS_RECEIVED: the response headers have been received
- 3 LOADING: the response body is loading
- 4 DONE: the request has been completed


Adding a key-value pair to the request header is done by invoking `setRequestHeader` when the connection is open.

```javascript
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 1) {
        xhttp.setRequestHeader('Authorization', 'Token token="a1b2c3"')
    } else if (this.readyState === 4 && this.status === 200) {
        let data = JSON.parse(xhttp.responseText);
        // do something with data
    } else if (this.readyState === 4 && this.status === 404) {
        // handle 404
    }
};
xhttp.open("GET", url);
xhttp.send();
```


It's possible to hide the messiness inside a function by passing a callback function.

```javascript
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

http_get("https://api.ipify.org/?format=json", function(data) {
    console.log(data);
});
```


## AJAX in jQuery

```javascript
$.ajax({
    method: "GET", // specify the HTTP Verb
    url: 'https://api.iify.org/?format=json' // specify the URL
}).done(function(data) {
    console.log(data); // log the data we get in response
}).fail(function() {
    alert("error"); // indicate that an error has occurred
});
```





## CORS

CORS stands for 'cross-origin resources sharing', and represents a relaxation of the [same origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). You can read more about CORS on the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

If you receive the response "No 'Access-Control-Allow-Origin' header is present on the requested resource", it's because the remote server you're sending to the request from has security controls in place that prevent access from a client. You can read more about CORS [here](https://stackoverflow.com/questions/43871637/no-access-control-allow-origin-header-is-present-on-the-requested-resource-whe) and [here](https://security.stackexchange.com/questions/108835/how-does-cors-prevent-xss).


## JSONP

JSONP (short for "JSON with Padding") is an additional security feature some APIs offer or require. You can read more about JSONP [here](https://stackoverflow.com/questions/3839966/can-anyone-explain-what-jsonp-is-in-layman-terms) and [here](https://stackoverflow.com/questions/16097763/jsonp-callback-function).


