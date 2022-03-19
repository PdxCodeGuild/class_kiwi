from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play_game', methods=['POST'])
def play_game():
    result = request.form
    user = result['rps']
    computer = random.choice(['rock', 'paper', 'scissors'])
    if user == computer:
        message = "It is a tie!"
    elif user == "rock":
        if computer == "scissors":
            message = "You Win!"
        else:
            message = "Computer Wins :("
    elif user == "paper":
        if computer == "rock":

            message = 'You Win!'
        else:
            message = "Computer Wins :("
    else:
        if computer == "paper":
            message = "You Win!"
        else:
            message = "Computer Wins :("

    return render_template('results.html', user=user, computer = computer, message = message )
