from django.db import models
from django.urls import reverse

class ShopList(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ShopItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    purchased = models.BooleanField(null=False, blank=False)
    shop_list = models.ForeignKey(ShopList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.shop_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ["purchased"]