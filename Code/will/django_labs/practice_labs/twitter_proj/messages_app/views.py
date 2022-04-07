from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import Tweet
# Create your views here.


def index(request):
    tweets = Tweet.objects.all().order_by('-publish_date')[:20]
    return render(request, 'messages_app/index.html', {
        'tweets': tweets, 'form': NewTweetForm()
    })


def new_tweet(request):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            tweet = Tweet()
            tweet.user = request.user
            tweet.text = forms.cleaned_data['text']
            tweet.save()

    return HttpResponseRedirect(reverse('index'))
