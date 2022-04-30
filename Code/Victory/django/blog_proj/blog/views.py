from msilib.schema import ListView
from django.http import Http404
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method=='POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Successful registration')
            return redirect('/login')
        else:
            messages.error(request, 'Unable to register, please try again')
    else:
        form = RegForm()
    context = {
        'form': form
    }

    return render(request, 'blog/register.html', context)


def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect('/profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else: 
                    messages.info(request, f"Successful Login {username}")
                    return redirect('profile')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        # messages.error(request, 'Invalid Credentials')
    
        form = AuthenticationForm
    context = {
        'form': form
    }

    return render(request, 'blog/login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logget out')
    return redirect(reverse('login'))


def profile(request):

    # posts = BlogPost.objects.all()
    posts = BlogPost.objects.all().order_by('-date_created')

    return render(request, 'blog/profile.html', {'posts':posts})

    
    
class BlogDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
 
@login_required
def create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = BlogPost()
            blog.author = request.user
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.save()
            return redirect('profile')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create.html', {'form':form})

@login_required 
def edit(request,pk):
    blog = BlogPost.objects.get(id=pk)
    form = BlogPostForm(instance=blog)

    context   = {'blog':blog, 'form':form}
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()

            return redirect('profile') 
    return render(request, 'blog/edit.html', context)
    
# def delete(request,pk):

#     blog = BlogPost.objects.get(id=pk)
#     if request.method == 'POST':
#         blog.delete()
#         return redirect ('profile')
    
#     context = {'blog':blog}
#     return render(request, 'blog/delete.html', context)

@login_required
def delete(request,pk):
    
    blog = BlogPost.objects.get(id=pk,author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect ('profile')
    
    context = {'blog':blog}
    return render(request, 'blog/delete.html', context)


