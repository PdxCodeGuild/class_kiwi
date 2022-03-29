from django.urls import path
from . import views

app_name = "ari"

urlpatterns = [
    path("", views.index, name="index"),
    path("ARI_app/result/", views.compute, name="result"),
]
