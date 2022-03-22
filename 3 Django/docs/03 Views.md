
# Views



- [Views](#views)
  - [Overview](#overview)
  - [Requests](#requests)
    - [The Request Object](#the-request-object)
    - [Path Parameters](#path-parameters)
    - [Receiving Query Parameters](#receiving-query-parameters)
    - [Receiving a Form Submission](#receiving-a-form-submission)
    - [Receiving JSON](#receiving-json)
  - [Responses](#responses)
    - [Responding with a String / Raw HTML](#responding-with-a-string--raw-html)
    - [Responding with a Template](#responding-with-a-template)
    - [Responding with JSON](#responding-with-json)
    - [Redirecting](#redirecting)


## Overview

**Views** are python functions that do the bulk of the work, they receive the incoming request and return a response. The view can then respond with HTML, JSON, text, etc. An app's views are contained in its `views.py` file. You can read more about views [here](https://docs.djangoproject.com/en/4.0/topics/http/views/) and [here](https://docs.djangoproject.com/en/4.0/ref/request-response/).

```python
from django.http import HttpResponse
def index(request):
    return HttpResponse('hello world!')
```

## Requests

### The Request Object

The request object received by the view contains lots of important information.

- `request.method` tells you which of the HTTP methods was used (GET, POST, etc)
- `request.body` the raw request body, you can also use `request.read()`
- `request.path` path of the requested page, e.g. `"/music/bands/beatles/"`
- `request.GET` dictionary of query parameters
- `request.POST` dictionary of form parameters
- `request.COOKIES` a dictionary of cookies


### Path Parameters

You can specify parameters in the path using a datatype (`int`, `str`) and a name. Those values will then be automatically taken out of the path and passed as parameters to the view function. A common use for these is for a detail view for a record, with the primary key of the record specified in the path.

**urls.py**
```python
from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    # e.g. /detail/5/, /detail/23/
    path('detail/<int:todo_item_id>/', views.detail, name='detail')
]
```

**views.py**
```python
from django.shortcuts import get_object_or_404
from .models import TodoItem
def detail(request, todo_item_id):
    # look up the TodoItem with the given id
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    # pass that todo item to the template to be rendered
    return render(request, 'todoapp/detail.html', {'todo_item': todo_item})
```


### Receiving Query Parameters

Query parameters are passed as part of the url and are turned into dictionary-like objects. For example, if the path entered is `/mypath/?myvar=mytext`, we can retrieve the query parameters by name.

```python
def view(request):
    print(request.GET['myvar']) # 'mytext'
```

### Receiving a Form Submission

When a form is submitted to a view, the data in the form is arranged into a dictionary. The `name` attributes of the input elements become the `keys` and the values the user enters into the input elements become the `values`. The view can then use the key to get the values out of the dictionary. For more about forms, check out [Templates - Forms](04%20-%20Templates.md#forms).


**myapp/templates/myapp/mytemplate.html**
```html
<form action="{% url 'myapp:mypathname' %}" method="post">
  <input name="myname"/>
  <button type="submit">submit</button>
</form>
```

**myapp/urls.py**
```python
from django.urls import path

app_name = 'myapp'
urlpatterns = [
    path('mypath/', views.myview, name='mypathname')
]
```

**myapp/views.py**
```python
from django.http import HttpResponse
def myview(request):
    print(request.POST['myname'])
    return HttpResponse('ok')
```


### Receiving JSON

To read JSON data sent via AJAX, you can use the built-in `json` module to read the request's body. This turns the JSON into a Python dictionary.


```javascript
axios({
    method: 'post',
    url: '{% url 'myapp:mypathname' %}',
    data: {foo: 'bar', hello: 'world'}
}).then(function(response) {
    console.log(response.data)
})
```

```python
import json
def postdata(request):
    data = json.loads(request.body)
    print(data)
    return HttpResponse('ok')
```


## Responses

### Responding with a String / Raw HTML

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def fruits(request):
    fruits = ['apples', 'bananas', 'plums']
    html = '<ul>'
    for fruit in fruits:
        html += '<li>' + fruit + '</li>'
    html += '</ul>'
    return HttpResponse(html)
```

### Responding with a Template

To render a template, use the `render` function. The first parameter is the original request, the second is the location of the template, and the third is a dictionary containing the variables to be rendered.

```python
from django.shortcuts import render
from .models import TodoItem
def index(request):
    todo_items = TodoItem.objects.all()
    context = {'todo_items': todo_items}
    return render(request, 'todos/index.html', context)
```

### Responding with JSON

To respond with JSON, you can just pass a dictionary to a `JsonResponse`.

**myapp/urls.py**
```python
from django.http import JsonResponse
def myview(request):
    data = {'foo': 'bar', 'hello': 'world'}
    return JsonResponse(data)
```

You can then send an HTTP request to this view via ajax.

**myapp/templates/myapp/index.html**
```javascript
axios{
    method: 'get',
    path: "{% url 'myapp:myview' %}"
}).then(function(response) {
    console.log(response.data)
})
```


### Redirecting

To redirect, you can use the HttpResponseRedirect class. You can redirect to a full url `http://mysite.com/` or if you put a path `/mypath/`, django will add it to the current domain `http://localhost:8000/mypath/`. This can cause issues (`reverse('google.com')` will redirect to `localhost:8000/google.com`.

```python
from django.http import HttpResponseRedirect
def myview(request):
    ...
    return HttpResponseRedirect('/mypath/')
```
```python
def myview(request):
    ...
    return HttpResponseRedirect('http://mysite.com/')
```

It's also best to use the [reverse](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#reverse) function to look up the url using the name rather than hard-coding it. This does the same reverse url redirect as the template: [04 Template - Reverse URL Lookup](04%20-%20Templates.md#reverse-url-lookup)

```python
from django.http import HttpResponseRedirect
from django.urls import reverse
def add(request):
    return HttpResponseRedirect(reverse('myapp:myview'))
```

You can also use the [redirect](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#redirect) function. The difference is explained [here](https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect).

```python
from django.shortcuts import redirect
def redirect(request):
    return redirect('http://www.mozilla.org/')
```
