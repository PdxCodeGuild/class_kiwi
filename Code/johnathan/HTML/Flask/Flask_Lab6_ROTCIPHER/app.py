from flask import Flask, render_template, request
import string

app = Flask(__name__)




@app.route('/')
def index ():
    return render_template('Lab6_Flask_index.html')

@app.route('/ciper_text', methods=['POST'])

def rot13 ():
    result = request.form
    user_data = result['blog']
    alphabet = string.ascii_lowercase
    # message = {'Lab6_Flask_index.html'}
    user_string = ''
    for i in user_data:
        if i in alphabet:
            if alphabet.index(i) < 13:
                user_string += alphabet[alphabet.index(i) + 13]
            else: user_string += alphabet[alphabet.index(i) - 13]
    return render_template('encrypt.html', user_string=user_string)

# print(rot13(message))
#     print(result)
    





# @app.route('/about')
# def about():
#     return render_template('about.html')


