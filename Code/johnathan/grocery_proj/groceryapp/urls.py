from django.urls import path
from .import views

app_name = "grocery_list" 

urlpatterns=[
    path("",views.index,name="index"),

    path("add_item",views.add_item,name="add"),

    path("buy/<int:item_id>/",views.buy_item, name="buy"),
    path("delete/<int:item_id>/",views.delete_item, name="delete")

]
