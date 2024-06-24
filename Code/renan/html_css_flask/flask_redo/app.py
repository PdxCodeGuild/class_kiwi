from flask import Flask, render_template
import random
import string

app = Flask(__name__)


#localhost:5000/
@app.route('/')
def index():
            
    letters = str(string.ascii_lowercase)
    # print(letters)

    digits = string.digits  
    # print(digits) 

    punctuation = string.punctuation
    # print(punctuation)  

    all_characters = letters + digits + punctuation
    # print(random.choice(all_characters))

    # Password Generator

    characters = []

    while len(characters) < 10:
        characters.append(random.choice(all_characters))

    password = characters 
    

    return render_template('index.html',password=password)
