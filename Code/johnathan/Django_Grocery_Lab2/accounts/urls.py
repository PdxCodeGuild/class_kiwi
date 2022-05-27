from django.urls import path

from accounts.views import signin, signout, signup

urlpatterns = [
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
]