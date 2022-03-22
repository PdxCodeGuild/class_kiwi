
# Django Quickstart

## 1) Project Setup

1. Create a project: `django-admin startproject myproject`, if you get 'command not found', try `python -m django startproject myproject`
2. Move into the project folder: `cd myproject`
3. Create the database with built-in models: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Set the timezone in your `myproject/settings.py`: (e.g. `TIME_ZONE = 'America/Los_Angeles'`) [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## 2) App Setup

1. Create an app: `python manage.py startapp myapp`
2. Add `'myapp'` to the list of `INSTALLED_APPS`:

**myproject/settings.py**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'myapp'
]
```

## 3) Creating a View and a Route

1. Create a view:

**myapp/views.py**
```python
from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')
```

2. Create a `urls.py` in your app folder with a path to your view:

**myapp/urls.py**
```python
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('myview/', views.myview, name='myview')
]
```

3. In your project `urls.py` create a path your your app's `urls.py`:

**myproject/urls.py**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls'))
]
```

4. Run the server `python manage.py runserver` and in your browser's address bar, type `localhost:8000/myapp/myview/` and you should see `hello world!`


## 4) Render a Template

1. Inside your app folder `myapp`, create a folder called `templates`. Inside of that, create a folder with the same name as your app `myapp`. Then inside of that, create your template `mytemplate.html`.

```
myproject
    myapp
        templates
            myapp
                mytemplate.html
        ...
    myproject
        ...
```

2. Inside your `mytemplate.html`, put some text to make sure the template is being served by django.

**myapp/templates/myapp/mytemplate.html**
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>{{ message }}</h1>
  </body>
</html>
```

3. Change your view to render the template instead of responding with plain text.

**myapp/views.py**
```python
from django.shortcuts import render

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myapp/mytemplate.html', context)
```

4. Go to `localhost:8000/myapp/myview/` and you should see `Hello World!` in an `h1` element.

## 5) Define Your Models

1. Create your model(s):

**myapp/models.py**
```python
from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    
    def __str__(self):
        return self.myfield
```

1. Run migrations to create the tables from your model(s):
  - `python manage.py makemigrations`
  - `python manage.py migrate`

3. Register your model with the admin panel:

**myapp/admin.py**
```python
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
```

4. Log into your admin panel `localhost:8000/admin`, you should see your models. Enter in some dummy data.

## 6) Render Data in the Template

1. Amend your view to retrieve data from the database and pass it to the template:

**myapp/views.py**
```python
from django.shortcuts import render
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)
```

2. Use the data to generate HTML inside your template:


**myapp/templates/myapp/mytemplate.html**
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <ul>
      {% for myinstance in myinstances %}
      <li>{{ myinstance.myfield }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

3. Go to `localhost:8000/myapp/myview` to see the blog posts you entered into the admin panel.

## 7) Create a Form

1. Create a view for receiving a form submission:

**myapp/views.html**
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')
```

2. Create a route to get to that view:

**myapp/urls.py**
```python
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('myview/', views.myview, name='myview'),
    path('mycreate/', views.mycreate, name='mycreate')
]
```

3. Create a form inside your template:


**myapp/templates/myapp/mytemplates.html**
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <form action="{% url 'myapp:mycreate' %}" method="post">
            {% csrf_token %}
            <input type="text" name="myfield"/>
            <button type="submit">submit</button>
        </form>
        <ul>
            {% for myinstance in myinstances %}
            <li>{{ myinstance.myfield }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

4. Submit the form and check that the view received it by looking for the result of `print(request.POST)` in the terminal running Django.

5. Save the data from the form in the database and redirect back to the first view.

**myapp/views.py**
```python
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))
```
