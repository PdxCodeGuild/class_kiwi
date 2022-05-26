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
    comp = random.choice(["rock", "paper", "scissors"])

    if user == comp:
        message = "It's a tie!"
    elif user == "rock":
        if comp == "scissors":
            message = "You win!"
        else:
            message = "Computer wins"
    elif user == "paper":
        if comp == "rock":
            message = "You win!"
        else:
            message = "Computer wins"
    else:
        if comp == "paper":
            message = "You win!"
        else:
            message = "Computer wins"

    print(user, comp, message)

    return render_template('result.html', user=user, comp=comp, message=message)
