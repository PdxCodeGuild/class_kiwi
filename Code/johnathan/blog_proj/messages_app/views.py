from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import reverse

from .models import Posts
# Create your views here.

def index(request):
    posts = Posts.objects.all().order_by('-published_date')[:20]

    return render(request, 'messages_app/index.html', {
        'posts': posts,
        'forms': NewPostsForm()
    })

def new_posts(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            posts= Posts()
            posts.user = request.user
            posts.text = form.cleaned_data['text']
            posts.save()
    return HttpResponseRedirect(reverse('index'))