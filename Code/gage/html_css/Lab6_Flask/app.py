from flask import Flask, render_template, request
import random
import string


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/result', methods=['post'])
def result():
    # Gathers the count for each type of character
    form_dict = request.form
    abc_amount = form_dict['abc_count']
    num_amount = form_dict['num_count']
    pun_amount = form_dict['pun_count']
    # Stores the max amount of characters for each var
    abc_counter = 0
    num_counter = 0
    pun_counter = 0
    # Stores the randomly generated characters for each type
    abc_pass = ''
    num_pass = ''
    pun_pass = ''
    
    while abc_counter < int(abc_amount): # Adds random alpha characters to the pre-shuffled list
        abc_counter += 1
        abc_pass += random.choice(string.ascii_letters)
    while num_counter < int(num_amount): # Adds random digit characters to the pre-shuffled list
        num_counter += 1
        num_pass += random.choice(string.digits)
    while pun_counter < int(pun_amount): # Adds random punctuation characters to the pre-shuffled list
        pun_counter += 1
        pun_pass += random.choice(string.punctuation)
    # Gathers total character count in the password
    amount = abc_counter + num_counter + pun_counter

    # Adds each var together and converts them to a list
    pre_shuffle = list(abc_pass + num_pass + pun_pass)
    
    # Shuffles the list to make it random
    random.shuffle(pre_shuffle)
    rand_pass = ''.join(pre_shuffle) # Converts back to list
    return render_template('result.html', rand_pass=rand_pass, amount=amount)