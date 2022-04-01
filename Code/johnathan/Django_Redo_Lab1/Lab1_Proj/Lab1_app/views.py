from multiprocessing import context
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Lab1_Model

# # Create your views here.

# def index(request):
#     return render(request, 'Lab1/index.html')



def Lab1_view(request):
    Lab1_instances = Lab1_Model.objects.all()
    context = {
        'Lab1_instances': Lab1_instances
    }
    return render(request, 'Lab1\index.html', context)

def rot13(request):
    import string
    user_data = request.POST['blog']
    # lab1model = Lab1_Model
    # lab1model.save()
    alphabet = string.ascii_lowercase
    user_string = ''
    for i in user_data:
        if i in alphabet:
            if alphabet.index(i) < 13:
                user_string += alphabet[alphabet.index(i) + 13]
            else: user_string += alphabet[alphabet.index(i) - 13]
    print(user_data)
    return render(request, 'Lab1/encrypt.html', {'user_string':user_string})
