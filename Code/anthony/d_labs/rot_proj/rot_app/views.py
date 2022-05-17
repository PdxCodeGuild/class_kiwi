from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'rot_app/index.html')


def answer(request):
    og = request.POST['original']

    rot13_dict = {
        "a": "n",
        "b": "o",
        "c": "p",
        "d": "q",
        "e": "r",
        "f": "s",
        "g": "t",
        "h": "u",
        "i": "v",
        "j": "w",
        "k": "x",
        "l": "y",
        "m": "z",
        "n": "a",
        "o": "b",
        "p": "c",
        "q": "d",
        "r": "e",
        "s": "f",
        "t": "g",
        "u": "h",
        "v": "i",
        "w": "j",
        "x": "k",
        "y": "l",
        "z": "m",
        " ": " "
    }

    encoded_list = []
    for x in og:
        encoded_list.append(rot13_dict[x])

    list = ''.join(encoded_list)

    context = {
        'og': og,
        'list': list

    }

    print(''.join(encoded_list))
    return render(request, 'rot_app/answer.html', context)
