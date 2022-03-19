from flask import Flask, render_template
import string

app = Flask(__name__)




@app.route('/')
def index ():
    return render_template('Lab6_Flask_index.html')

@app.route('/ciper_text', methods=['POST'])
def rot13 (message):
    alphabet = string.ascii_lowercase
    user_string = ''
    for i in message:
        if i in alphabet:
            if alphabet.index(i) < 13:
                user_string += alphabet[alphabet.index(i) + 13]
            else: user_string += alphabet[alphabet.index(i) - 13]

    return user_string 
    
    



if __name__ == "__main__":
    app.run()


# @app.route('/about')
# def about():
#     return render_template('about.html')


