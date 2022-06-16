from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image =models.ImageField(upload_to='profile_pics', blank=True, null=True)
    about_me = models.TextField()

    def __str__(self):
        return self.author

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug=models.CharField(default=True, max_length=110)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    date_edited = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    def __str__(self):
        return f"{self.author} Blog Post: {self.title} {self.date_created.year}/{self.date_created.month}/{self.date_created.day}"




class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=1)
    # parent_body = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Comment: {self.body[:20]}"
