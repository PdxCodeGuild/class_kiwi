from django.shortcuts import render, get_list_or_404
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


# Index
def index(request):
    form = NewTweetForm()
    tweets = Tweet.objects.all().order_by('-published_date')[:20]
    context = {'form':form, 'tweets': tweets}
    return render(request, 'messages_app/index.html', context)

# Post
@login_required
def new_tweet(request):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            tweet = Tweet()
            tweet.user = request.user
            tweet.text = form.cleaned_data['text']
            tweet.save()
        
        return HttpResponseRedirect(reverse('index'))

# Delete
@login_required
def delete_tweet(request, tweet_id):

    if Tweet.objects.filter(id=tweet_id, user=request.user).exists():
        tweet = Tweet.objects.get(id=tweet_id, user=request.user)
        tweet.delete()
    return HttpResponseRedirect(reverse(index))

# Like
@login_required
def like_tweet(request, tweet_id):
    if Tweet.objects.filter(id=tweet_id).exists():
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.likes += 1
        tweet.save()
    return HttpResponseRedirect(reverse(index))

 # Dislike
def dislike_tweet(request, tweet_id):
    if Tweet.objects.filter(id=tweet_id).exists():
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.dislikes += 1
        tweet.save()
    return HttpResponseRedirect(reverse(index))

def detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    context = {"tweet": tweet}
    return render(request, 'messages_app/details.html', context)