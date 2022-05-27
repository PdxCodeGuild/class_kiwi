from django.urls import path

from grocery_app.views import add_item, delete_item, index, update_item

urlpatterns = [
    path('', index, name='index'),
    path('add-item', add_item, name='add-item'),
    path('update-item/<int:item_id>', update_item, name='update-item'),
    path('delete-item/<int:item_id>', delete_item, name='delete-item'),
]