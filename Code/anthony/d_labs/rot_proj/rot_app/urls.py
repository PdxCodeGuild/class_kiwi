from django.urls import URLPattern, path
from . import views


app_name = 'rot_app'


urlpatterns = [
    path('rot/', views.index, name='index'),

    path('answer/', views.answer, name='answer')
]
