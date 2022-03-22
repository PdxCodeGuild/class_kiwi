
# Routes

- [Routes](#routes)
  - [Overview](#overview)
  - [Connecting the Project's `urls.py` to the App's `urls.py`](#connecting-the-projects-urlspy-to-the-apps-urlspy)
  - [Connecting an App's `urls.py` to a View](#connecting-an-apps-urlspy-to-a-view)
  - [Reverse URL Lookup](#reverse-url-lookup)
  - [Parameters in the Path](#parameters-in-the-path)


## Overview

Routes connect the **path** part of a URL to a **view**. The routes are stored in a `urls.py` file, which can be found in both the project folder and in each of the apps' folders. Routes are evaluated **in order**: whichever route matches first is the one used. You can visualize Django's routing system as a series of pipes, first the incoming request hits the project's `urls.py`, which the directs it to one of the app's `urls.py`, which then directs it to a view. You can read more about routes [here](https://docs.djangoproject.com/en/4.0/topics/http/urls/) and [here](https://docs.djangoproject.com/en/4.0/ref/urls/).


## Connecting the Project's `urls.py` to the App's `urls.py`

The `include` function allows you to combine the routes of multiple `urls.py` files into one. This is used to connect the project's 'main' `urls.py` to the `urls.py` in each of the apps.

**myproject/urls.py**
```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # route to admin panel
    path('admin/', admin.site.urls),
    # all routes in 'myapp/urls.py' will be under localhost:8000/mypath/...
    path('mypath/', include('myapp.urls'))
]
```

## Connecting an App's `urls.py` to a View

**myapp/urls.py**
```python
from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    # localhost:8000/mypath/
    path('', views.index, name='index'),
    # localhost:8000/mypath/about/
    path('about/', views.about, name='about'),
]
```

**myapp/views.py**
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('you are at the index')

def about(request)
    return HttpResponse('you are at the )
```

## Reverse URL Lookup

The `app_name` in the `urlspy` and the `name=` in each of the path are used to perform a reverse url lookup: [04 Templates - Reverse URL Lookup](04%20-%20Templates.md#reverse-url-lookup).

**myapp/urls.py**
```python
from django.urls import path

app_name = 'myapp' # <-------------
urlpatterns = [
    path('', views.index, name='index'), # <----------
]
```

## Parameters in the Path

You can specify a parameter in your path using `<type:var_name>`, where `type` is the data type of the parameter (e.g. `str`, `int`, etc). See the [views.md](03%20-%20Views.md#path-parameters) file.

