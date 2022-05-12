from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('web_form.html')

@app.route("/index.html")
def iframe():
    return render_template('index.html')

@app.route("/password.html", methods=['POST'])
def password():
    result = request.form
    upper = int(result['upper'])
    lower = int(result['lower'])
    numbers = int(result['numbers'])
    special = int(result['special'])
    pupper = ''.join(random.choices(string.ascii_uppercase, k=upper))
    plower = ''.join(random.choices(string.ascii_lowercase, k=lower))
    pnumbers = ''.join(random.choices(string.digits, k=numbers))
    pspecial = ''.join(random.choices(string.punctuation, k=special))
    wordpass = (pupper + plower + pnumbers + pspecial)
    password = ''.join(random.sample(wordpass,len(wordpass)))
    return render_template("/password.html", password=password)