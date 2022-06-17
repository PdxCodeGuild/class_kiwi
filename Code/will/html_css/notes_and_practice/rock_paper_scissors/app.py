from flask import Flask, render_template, request
import random

app = Flask(__name__)

# localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['post'])
def results():
    outcome = request.form

    user = outcome['rps']
    comp = random.choice(['rock', 'paper', 'scissors'])

    if user == comp:
        message = 'It is a tie!'

    elif user == 'rock':
        if comp == 'scissors':
            message = 'You win!'
        
        else:
            message = 'Computer wins'
    elif user == 'paper':
        if comp == 'rock':
            message = 'You win!'

        else:
            message = 'Computer wins'

    elif user == 'scissors':
        if comp == 'paper':
            message = 'You win!'

        else:
            message = 'Computer wins'

    return render_template('results.html', user=user, comp=comp, message=message)

#@app.route('/contact')
#def contact():
#    return render_template('contact.html')