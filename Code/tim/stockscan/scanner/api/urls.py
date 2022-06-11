from django.urls import path
from .views import main, save_history, get_history

urlpatterns = [
    path('home', main),
    path('', main),
    path('save_history', save_history),
    path('get_user_history', get_history)
]