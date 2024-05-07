from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
# importing forms
from messages_app.forms import NewTweetForm
# importing models
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404

# Create your views here.
def index(request):
    tweets= Tweet.objects.all().order_by('-pub_date')[:20]
    form= NewTweetForm()
    context= {
        'tweets': tweets,
        'form': form
    }
    return render(request, 'messages_app/index.html', context)

@login_required
def new_tweet(request):
    if request.method == "POST":
        form= NewTweetForm(request.POST)
        if form.is_valid():
            tweet= Tweet()
            tweet.user= request.user
            tweet.text= form.cleaned_data['text']
            tweet.save()
    return HttpResponseRedirect(reverse('messages:index'))

@login_required
def like(request, tweet_id):
    if Tweet.objects.filter(id=tweet_id):
        tweet= Tweet.objects.get(id=tweet_id)
        tweet.likes += 1
        tweet.save()
    return redirect(reverse('messages:index'))

@login_required
def dislike(request, tweet_id):
    if Tweet.objects.filter(id=tweet_id):
        tweet= Tweet.objects.get(id=tweet_id)
        tweet.dislikes += 1
        tweet.save()
    return redirect(reverse('messages:index'))


@login_required
def del_tweet(request, tweet_id):
# helps reduce user error
# wont load a page that doesnt exits ex: delete/30000
    if Tweet.objects.filter(id=tweet_id, user=request.user).exists():
        tweet= Tweet.objects.get(id=tweet_id, user=request.user)
        tweet.delete()
    return redirect(reverse('messages:index'))

# @login_required
def detail(request, tweet_id):
    tweet= Tweet.objects.get(id=tweet_id)
    return render(request, 'messages_app/detail.html',{
        'tweet': tweet
    })


 
# other delete options w/ no filtering

# @login_required
# def del_tweet(request, tweet_id):
#     # tweet= Tweet.objects.get(id=tweet_id, user=request.user)
#     tweet= get_list_or_404(Tweet, id=tweet_id, user=request.user)
#     tweet.delete()
#     return redirect(reverse('messages:index'))

