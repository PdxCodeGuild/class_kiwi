from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    slug = models.SlugField(max_length=200, unique=True)

    class Meta: ordering= ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class GroceryItem(models.Model):
    category = models.ForeignKey(Category, related_name= 'groceryitems',
    on_delete=models.CASCADE)

    name= models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='groceryitems/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta: ordering= ('name',)
    index_together = (('id', 'slug'))

    def __str__(self):
        return self.name
