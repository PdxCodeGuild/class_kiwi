from django.shortcuts import render
import random

# Create your views here.


def index(request):
    return render(request, 'rps_app/index.html')


def results(request):
    choice = request.GET['choice']

    computer = random.choice(['rock', 'paper', 'scissors'])
    player = choice
    if player == computer:
        message = 'We have a tie'
    elif player == 'rock':
        if computer == 'scissors':
            message = 'Player Wins!'
        else:
            message = 'Computer Wins!'
    elif player == 'paper':
        if computer == 'rock':
            message = 'Player Wins!'
        else:
            message = 'Computer Wins!'
    else:
        if computer == 'paper':
            message = 'Player Wins!'
        else:
            message = 'Computer Wins!'

    context = {
        'computer': computer,
        'player': player,
        'message': message
    }

    return render(request, 'rps_app/results.html', context)
