from django.urls import reverse
from django.shortcuts import redirect, render
from .models import BlogPost
from .forms import PostForm


# Create your views here.

def home(request):
    new= PostForm()
    posts=BlogPost.objects.all()
    context= {
        'posts':posts,
        'new':new
    }
    return render(request, 'blog/home.html', context)

def new_post(request):
    if request.POST:
        form= PostForm(request.POST)
        if form.is_valid():
            post= BlogPost()
            post.user= request.user
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
    return redirect(reverse('home'))

def view_post(request, id):
    post= BlogPost.objects.get(id=id)
    context= {
        'post':post
    }
    return render(request, 'blog/view.html', context )