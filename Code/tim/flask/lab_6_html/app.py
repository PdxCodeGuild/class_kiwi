import string
from flask import Flask, render_template, request
import random


app = Flask(__name__)


@app.route('/')
def index():


    return render_template('index.html')
@app.route("/password", methods=['POST'])
def password():
    charcount = request.form
    count = charcount['charcount']
    count = int(count)
    password = string.ascii_letters

    password = password + string.digits

    all_chars = password + string.punctuation
    # charcount = 10
    random_pw = random.choices(all_chars, k=count)
    random_pw = "".join(random_pw)

    return render_template("password.html", random_pw=random_pw)