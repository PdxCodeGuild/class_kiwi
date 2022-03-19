from flask import Flask, render_template, request
import random
import string


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/result', methods=['post'])
def result():

    ascii = list(string.ascii_letters + string.digits)
    form_dict = request.form
    amount = form_dict['char_count']
    counter = 0
    rand_pass = ''
    while counter < int(amount):
        counter += 1
        rand_pass += random.choice(ascii)
    print(rand_pass)
    return render_template('result.html', amount=amount, rand_pass=rand_pass)