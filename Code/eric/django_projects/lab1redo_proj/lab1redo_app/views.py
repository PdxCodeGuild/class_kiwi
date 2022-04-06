from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'lab1redo_app/index.html')

def rot(request):
    letter_values = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'n' : 'a',
    'o' : 'b',
    'p' : 'c',
    'q' : 'd',
    'r' : 'e',
    's' : 'f',
    't' : 'g',
    'u' : 'h',
    'v' : 'i',
    'w' : 'j',
    'x' : 'k',
    'y' : 'l',
    'z' : 'm'
    }

    user_string = request.GET.get('plain_text', '').lower()
    value_string = " "
    for letter in user_string:
        letters = letter in letter_values.get()
        if letters == True:
            value_string += letter_values[letter]
    
    return render(request, 'index.html', {'Converted Text':value_string})

    
