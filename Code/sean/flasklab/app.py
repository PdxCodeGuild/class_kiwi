from flask import Flask, render_template, Request
import random, string

app = Flask(__name__)

@app.route("/")
def index():
    print("home page")


from flask import Flask, render_template, request
import random
from string import ascii_lowercase as lower, ascii_uppercase as upper, punctuation as punc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/password', methods=['POST'])
def generate_password():
    uppercase = int(request.form['uppercase'])
    lowercase = int(request.form['lowercase'])
    numbers = int(request.form['numbers'])
    specialcharacters = int(request.form['specialcharacters'])
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    u_list = random.choices(upper, k=uppercase)
    l_list = random.choices(lower, k=lowercase)
    n_list = random.choices(nums, k=numbers)
    s_list = random.choices(punc, k=specialcharacters)
    password = u_list + l_list + n_list + s_list
    random.shuffle(password)
    password = ''.join(password)
    password = f'Your new password is: {password}'
    return render_template('index.html', password=password)