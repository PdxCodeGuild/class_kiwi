from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('del_item/<groceryitem_id>', views.del_item, name='del-item'),
    path('add_item', views.add_item, name='add_item'),
    path('update_item/<groceryitem_id>', views.update_item, name='update-item'),
    

]