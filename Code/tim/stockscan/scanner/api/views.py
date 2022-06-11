from django.shortcuts import render
from django.http import HttpResponse

from .models import MyUser
# Create your views here.

def main(request):
    return HttpResponse("Hello")

# we need to pass in the value that got searched from the page
# look up --- trying to pass value to get in django (think query params / url)
# getting the param with key of search value of symbol (From above) 


def save_history(request):
    # print(str(request.user)) username=str(request.user)
    # print('hampt' == str(request.user))
    # print(str(request.user))
    username = str(request.user)
    does_user_exist = MyUser.objects.filter(username=username).count() > 0#filter(username=str(request.user)) >
    # print(user.)
    print(does_user_exist)
    # queryset = MyUser.objects.filter(request.user)
    # print(queryset.query
    # x = queryset.get()
    if not does_user_exist: 
        u = MyUser(username=username, historical_searches=[request.GET['search']])
        u.save()

    else:
        # print(request.user.id)
        symbol = request.GET['search']
        user = MyUser.objects.get(username=username)
        pre_append = user.historical_searches.split(',')
        pre_append.append(symbol)
        user.historical_searches = pre_append
        user.save()
        print(type(user.historical_searches))
        print(user.historical_searches)
        # get user append to historical searches & save
    
    return HttpResponse({"message": ""})

def get_history(request):
    username = str(request.user)
    user = MyUser.objects.get(username=username)
    return HttpResponse({'{"historical_searches": "'+user.historical_searches+'"}'})