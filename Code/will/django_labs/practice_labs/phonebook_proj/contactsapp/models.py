from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    is_cool = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'

        else:
            return f'{self.first_name}'

    def coolness(self):
        if self.is_cool:
            return 'cool'

        else:
            return 'not cool'

    def __str__(self):
        return f'{self.full_name()} -- {self.coolness()}'
