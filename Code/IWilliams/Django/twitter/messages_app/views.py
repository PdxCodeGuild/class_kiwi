from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

from messages_app.forms import NewTweetForm
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404

# Create your views here.
def index(request):
    tweets =Tweet.objects.all().order_by('-published_date')[:20]
    
    return render(request, 'messages_app/index.html', {
        'tweets': tweets, 
        'form': NewTweetForm()
    })
@login_required    
def new_tweet(request):
    if request.method =='POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            tweet = Tweet()
            tweet.user = request.user 
            tweet.text = form.cleaned_data['text']
            tweet.save()
            
    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_tweet(request, tweet_id):
    #tweet = Tweet.objects.get(id=tweet_id, user=request.user)
    tweet = get_list_or_404(Tweet, id=tweet_id, user=request.user)
    tweet.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def like(request, tweet_id):
    if Tweet.objects.filter(id=tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.likes +=1
        tweet.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def dislike(request, tweet_id):
    if Tweet.objects.filter(id=tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.dislikes +=1
        tweet.save()
    return HttpResponseRedirect(reverse('index'))

def detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'messages_app/detail.html', {
        'tweet': tweet
    })
        

# @login_required
# def delete_tweet(request, tweet_id):
#     #tweet = Tweet.objects.get(id=tweet_id, user=request.user)
#     #tweet = get_list_or_404(Tweet, id=tweet_id, user=request.user)
#     if Tweet.objects.filter(id=tweet_id, user=request.user).exists():  
#         tweet = Tweet.objects.get(id=tweet_id, user=request.user)
#         tweet.delete()
#     return HttpResponseRedirect(reverse('index'))