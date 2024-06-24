from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/password", methods=["POST"])
def password():
    result = request.form
    upper = int(result["pwu"])
    lower = int(result["pwl"])
    numbers  = int(result["pwn"])
    special = int(result["pws"])
    pw_length = upper + lower + numbers + special 
    random_pw = []
    while len(random_pw) < pw_length:
        for x in range(upper):
            random_pw.append(random.choice(string.ascii_uppercase))
        for x in range(lower):
            random_pw.append(random.choice(string.ascii_lowercase))
        for x in range(numbers):
            random_pw.append(random.choice(string.digits))
        for x in range(special):
            random_pw.append(random.choice(string.punctuation))
    random.shuffle(random_pw)
   
    return render_template("password.html", random_pw=random_pw)



