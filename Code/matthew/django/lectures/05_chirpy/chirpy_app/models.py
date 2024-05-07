from django.contrib.auth.models import User
from django.db import models


# For importing ~User objects~ (username, password, email, first_name, last_name)


# Create your models here.

class Cheep(models.Model):
    chirp = models.CharField(max_length=125)
    # auto_now gives timestamp based off settings time_zone
    date_published = models.DateTimeField(auto_now=True)
    # on_delete=CASCADE - deletes all user data and associated information
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}: {self.date_published} -- {self.chirp}'
