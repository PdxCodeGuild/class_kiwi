from django.urls import URLPattern, path
from . import views # Targets the views.py file

urlpatterns = [

    #8000/Hello
    path('', views.hello, name='hello'), #path name (In search) - Targets 'hello' function - naming the path 'hello'

    #8000/hello/bruce
    path('bruce', views.bruce, name='bruce'),

    #8000/hello/any_name
    path('<str:name>', views.say_hello, name="say_hello") 
]


      