from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)
# $env:FLASK_APP="app.py"
# $env:FLASK_ENV = "development"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/pass")
def pass_page():
    return render_template("pass.html")


@app.route("/generate", methods=["POST"])
def password_func():
    result = request.form
    input_1 = int(result["lowercase"])
    input_2 = int(result["uppercase"])
    input_3 = int(result["special"])
    input_4 = int(result["number"])

    shuffled_pass = ""

    lowercase = random.sample(string.ascii_lowercase, input_1)
    uppercase = random.sample(string.ascii_uppercase, input_2)
    special_chars = random.sample(string.punctuation, input_3)
    numbers = random.sample(string.digits, input_4)

    char_amt = input_1 + input_2 + input_3 + input_4
    raw_password = lowercase + uppercase + special_chars + numbers  # combining lists
    # print(raw_password) # test before shuffle
    random.shuffle(raw_password)
    shuffled_pass = "".join(raw_password)

    return render_template("password_gen.html", shuffled_pass=shuffled_pass)
