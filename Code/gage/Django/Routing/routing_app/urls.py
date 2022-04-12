from django.urls import URLPattern, path
from . import views


app_name = 'routing_app'
urlpatterns = [
    #8000/routing/bio
    path('bio/', views.bio, name='bio'),
    #8000/routing/animations
    path('animations/', views.animations, name='animations'),
    #8000/routing/blog
    path('blog/', views.blog, name='blog'),
    #8000/routing/company
    path('company/', views.company, name='company'),
]