from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/final_result', methods=['post'])
def final_result():
    result = request.form
    user = result['rps']

    comp = random.choice(['rock', 'paper', 'scissors'])
    if comp == user:
        message = "It's a tie!"
    elif user == 'rock':
        if comp == 'scissors':
            message = "You win!"
        else:
            message = "You Lost."
    elif user == 'paper':
        if comp == 'rock':
            message = "You win!"
        else:
            message = "You Lost."
    else:
        if comp == 'paper':
            message = "You win!"
        else:
            message = "You Lost."
    
    return render_template("results.html", user=user, comp=comp, message=message)