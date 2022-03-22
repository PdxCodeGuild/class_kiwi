
# Django Overview

- [Django Overview](#django-overview)
  - [Overview](#overview)
  - [Management Commands](#management-commands)
    - [Custom Management Commands](#custom-management-commands)
  - [Resources](#resources)
    - [General](#general)
    - [Tutorials](#tutorials)
    - [Videos](#videos)
    - [Forums](#forums)
    - [Libraries](#libraries)
    - [Tools](#tools)



## Overview

Django is a back-end framework written in Python. Django is a **high-level framework** meaning that it provides a great deal of functionality for you, but you have to connect the pieces together. You have to learn things the 'django way'. This also means that isn't necessarily any deeper intuition behind things, the only answer may be "that's just how Django does things".

For comparison, [Flask](http://flask.pocoo.org/) is also a Python-based back-end framework, but whereas Django is high-level, Flask is low-level, meaning you're only given the most barebones functionality and have to do everything else yourself. Again, it's a balance of convenience and control.

The core of Django is the [request-response cycle](django_diagram.png). A request is received by the server, it follows a **route**, actives a **view**, which then uses **models** and a **template** to generate a **response**, which is then rendered in the user's browser. The following docs will cover each of these topics in turn, but bear in mind that they're all interdependent.

- Route: a mapping between a URL and a view
- View: a Python function which receives a request (url) and creates a response (html+css+js)
- Template: an HTML file with special syntax for filling in data
- Model: a Python class that parallels a database table

Django applications are contained in a **project** which can have multiple **apps**. Each app has its own routes, views, templates, and models. How you divide up the functionality of the application is up to your discretion, what's important is that it makes sense to you.



## Management Commands

Management commands are executed in a terminal to perform operations on a django project. You can view a full list of the management commands [here](https://docs.djangoproject.com/en/4.0/ref/django-admin/)

| Command                               | Description                                                                            |
| ------------------------------------- | -------------------------------------------------------------------------------------- |
| `django-admin startproject myproject` | create a Django project                                                                |
| `python manage.py startapp myapp`     | create an app                                                                          |
| `python manage.py runserver`          | run the server                                                                         |
| `python manage.py makemigrations`     | stage changes to the database                                                          |
| `python manage.py migrate`            | apply changes to the database                                                          |
| `python manage.py createsuperuser`    | create an admin (which has access to the admin panel)                                  |
| `python manage.py collectstatic`      | collects static files from each app and puts them into one folder, used for deployment |
| `python manage.py shell`              | open an interactive session, often used to do database operations                      |

### Custom Management Commands

If you need to execute some Python code to perform administrative operations (load data into a database from a file or API, erase saved files, etc), you can write a custom management command. These are executed just like other management commands (`runserver`, `startapp`, `migrate`, etc). To create a custom management command, first create a `management` folder inside your app. Inside of that, create a `commands` folder. Inside of that, create a `mycommand.py`. \

- myproject
  - myproject
  - myapp
    - management
      - commands
        - mycommand.py


Inside your `mycommand.py`, write the following.

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        print('hello!')
```

Now you can execute this function using `python manage.py <command name>`. Any parameters you write after the `<command name>` will be passed to the `handle` function.



## Resources

### General

- [MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Wikipedia](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Official Docs](https://docs.djangoproject.com/en/4.0/)
  - [Table of Contents](https://docs.djangoproject.com/en/4.0/contents/)

### Tutorials

- [Official Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Real Python](https://realpython.com/tutorials/django/)
- [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/archive/)

### Videos

- [Corey Schafer's Video Series](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [The Net Ninja's Video Series](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
- [The Django Book](https://djangobook.com/beginning-django-tutorial-contents/)
- [Traversey Media](https://www.youtube.com/watch?v=e1IyzVyrLSU)
- [Dennis Ivy](https://www.youtube.com/watch?v=4RWFvXDUmjo)

### Forums

- [Official Forum](https://forum.djangoproject.com/)

### Libraries

- [Django Packages](https://djangopackages.org/)
- [A List](https://vsupalov.com/favorite-django-packages-2019/)

### Tools

- [SQLite Browser](http://sqlitebrowser.org/)
