from unicodedata import name
from django.urls import URLPattern, path
# . is short cut for calling the views file. Because it is in the same folder
from . import views

urlpatterns = [
    # 8000/hello
    path('', views.hello, name='hello'),

    # 8000/hello/bruce
    path('bruce', views.bruce, name='bruce'),

    # 8000/hello/battman
    path('batman', views.batman, name='batman'),

    # 8000/hello/stringname
    path('<str:name>', views.say_hello, name='say_hello'),
    # <str:name> calls the f string on views.py.
    # creates a dynamic URL ex: hello/matthew
    # prints 'hello matthew' on page

]
