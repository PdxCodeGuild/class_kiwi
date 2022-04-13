from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_lowercase as lower, ascii_uppercase as upper, punctuation as punc


# Create your views here.
def index(request):
    if request.method == "POST":
        uppercase = request.POST['uppercase']
        lowercase = request.POST['lowercase']
        numbers = request.POST['numbers']
        specialcharacters = request.POST['specialcharacters']
        uppercase = int(uppercase)
        lowercase = int(lowercase)
        numbers = int(numbers)
        specialcharacters = int(specialcharacters)
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        u_list = random.choices(upper, k=uppercase)
        l_list = random.choices(lower, k=lowercase)
        n_list = random.choices(nums, k=numbers)
        s_list = random.choices(punc, k=specialcharacters)
        password = u_list + l_list + n_list + s_list
        random.shuffle(password)
        password = ''.join(password)
        password = f'Your new password is: {password}'
        password_dict = {"password": password}
        return render(request, 'lab1_app/index.html', {'password': password_dict['password']})

    else:    
        return render(request, 'lab1_app/index.html')


def generate_password(request, number):
    print(number)
    print(request)
    #password = f'Your new password is: {password}'
    return render(request, 'lab1_app/index.html', number)


    
