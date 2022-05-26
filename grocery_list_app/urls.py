from django.urls import path
from . import views


app_name = "grocery"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("save/", views.save_item, name="save"),
    path("<pk>/delete", views.GroceryDelete.as_view(), name="delete"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("<pk>/update", views.check_item, name="check"),
]
