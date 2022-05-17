
from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.

def encode(request):
    english_to_rot13 = {
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m",

    }
    
    user_input = request.GET.get('uncoded_message', '').lower()
    input_post_encode =""
    for x in user_input:
        y = english_to_rot13.get(x)
        if y != None:
            input_post_encode += y

    
        
    return render(request, 'index.html', {'input_post_encode':input_post_encode})





def input_page(request):
    
    return render(request, 'index.html')
