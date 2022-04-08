import random
import string


from re import template
from django.shortcuts import render

# Create your views here.
def index2():
            
    letters = str(string.ascii_lowercase)
    # print(letters)

    digits = string.digits  
    # print(digits) 

    punctuation = string.punctuation
    # print(punctuation)  

    all_characters = letters + digits + punctuation
    # print(random.choice(all_characters))

    # Password Generator

    characters = []

    while len(characters) < 10:
        characters.append(random.choice(all_characters))

    password = characters #this returns the characters for the password generator
    return password
    
def index(request):
    results = index2()#This sends the logic to the index.html page with the key value "results"
    #If you want to add multiple key value pair, use this method below....
    #context={
        #"results":results
        
   # }
    
   # return render(request,'pg_app/index.html',context)
    return render(request,'pg_app/index.html',{"results":results})

    

# return render('pg_app/index.html', password=password)