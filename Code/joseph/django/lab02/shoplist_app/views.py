from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ShopList, ShopItem

class ListListView(ListView):
    model = ShopList
    template_name = "shoplist_app/index.html"

class ItemListView(ListView):
    model = ShopItem
    template_name = "shoplist_app/shop_list.html"

    def get_queryset(self):
        return ShopItem.objects.filter(shop_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["shop_list"] = ShopList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ShopList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new shopping list"
        return context

class ItemCreate(CreateView):
    model = ShopItem
    fields = [
        "shop_list",
        "title",
        "description",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        shop_list = ShopList.objects.get(id=self.kwargs["list_id"])
        initial_data["shop_list"] = shop_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        shop_list = ShopList.objects.get(id=self.kwargs["list_id"])
        context["shop_list"] = shop_list
        context["title"] = "Create a new shopping item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.shop_list_id])

class ItemUpdate(UpdateView):
    model = ShopItem
    fields = [
        "shop_list",
        "title",
        "description",
        "purchased",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["shop_list"] = self.object.shop_list
        context["title"] = "Edit shopping item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.shop_list_id])

class ListDelete(DeleteView):
    model = ShopList
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ShopItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shop_list"] = self.object.shop_list
        return context